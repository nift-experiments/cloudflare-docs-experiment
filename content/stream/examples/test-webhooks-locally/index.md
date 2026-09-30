<p class="article-summary">Test Cloudflare Stream webhook notifications locally using a Cloudflare Worker and Cloudflare Tunnel.</p>
<p>Cloudflare Stream cannot send <a href="/stream/manage-video-library/using-webhooks/">webhook notifications</a> to <code>localhost</code> or local IP addresses. To test webhooks during local development, you need a publicly accessible URL that forwards requests to your local machine.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14463.md")
</aside>
<p>This example shows how to:</p>
<ol>
<li>Start a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/">Cloudflare Tunnel</a> to get a public URL for your local environment.</li>
<li>Register that URL as your webhook endpoint, which returns the signing secret.</li>
<li>Create a Cloudflare Worker that receives Stream webhook events and verifies their signatures.</li>
</ol>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a> with Stream enabled</li>
<li><a href="https://nodejs.org/">Node.js</a> (v18 or later)</li>
<li>The <a href="/workers/wrangler/install-and-update/">Wrangler CLI</a> installed (<code>npm install -g wrangler</code>)</li>
</ul>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project that will receive webhook requests:</p>
<pre><code class="language-sh">npm create cloudflare@latest stream-webhook-handler&#10;</code></pre>
<h2 id="2-start-a-cloudflare-tunnel"><ol start="2">
<li>Start a Cloudflare Tunnel</li>
</ol></h2>
<p>Before registering a webhook URL, you need a public URL that points to your local machine. In a terminal, start a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/">quick tunnel</a> that forwards to the default Wrangler dev server port (<code>8787</code>):</p>
<pre><code class="language-sh">npx cloudflared tunnel --url http://localhost:8787&#10;</code></pre>
<p><code>cloudflared</code> will output a public URL similar to:</p>
<pre><code class="language-txt">https://example-words-here.trycloudflare.com&#10;</code></pre>
<p>Copy this URL. It changes every time you restart the tunnel.</p>
<h2 id="3-register-the-tunnel-url-as-your-webhook-endpoint"><ol start="3">
<li>Register the tunnel URL as your webhook endpoint</li>
</ol></h2>
<p>Use the Stream API to set the tunnel URL as your webhook notification URL. The API response includes a <code>secret</code> field — you will need this to verify webhook signatures.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/webhook \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;notificationUrl&quot;: &quot;https://example-words-here.trycloudflare.com&quot;&#10;}&#x27;</code></pre>
<p>The response will include a <code>secret</code> field:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;notificationUrl&quot;: &quot;https://example-words-here.trycloudflare.com&quot;,&#10;		&quot;modified&quot;: &quot;2024-01-01T00:00:00.000000Z&quot;,&#10;		&quot;secret&quot;: &quot;85011ed3a913c6ad5f9cf6c5573cc0a7&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Save the <code>secret</code> value. You will use it in the next step.</p>
<h2 id="4-store-the-webhook-secret-for-local-development"><ol start="4">
<li>Store the webhook secret for local development</li>
</ol></h2>
<p>Create a <code>.dev.vars</code> file in the root of your Worker project and add the webhook secret from the API response:</p>
<pre><code class="language-txt">WEBHOOK_SECRET=85011ed3a913c6ad5f9cf6c5573cc0a7&#10;</code></pre>
<p>Replace the value with the actual secret from step 3. Wrangler automatically loads <code>.dev.vars</code> when running <code>wrangler dev</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14462.md")
</aside>
<h2 id="5-add-the-webhook-handler"><ol start="5">
<li>Add the webhook handler</li>
</ol></h2>
<p>Replace the contents of <code>src/index.ts</code> in your Worker project with the following code. This Worker receives webhook <code>POST</code> requests, <a href="/stream/manage-video-library/using-webhooks/#verify-webhook-authenticity">verifies the signature</a>, and logs the payload.</p>
<pre><code class="language-ts">export interface Env {&#10;	WEBHOOK_SECRET: string;&#10;}&#10;&#10;async function verifyWebhookSignature(&#10;	request: Request,&#10;	secret: string,&#10;): Promise&lt;{ valid: boolean; body: string }&gt; {&#10;	const signatureHeader = request.headers.get(&quot;Webhook-Signature&quot;);&#10;	if (!signatureHeader) {&#10;		return { valid: false, body: &quot;&quot; };&#10;	}&#10;&#10;	const body = await request.text();&#10;&#10;	// Parse &quot;time=&lt;unix_ts&gt;,sig1=&lt;hex_signature&gt;&quot;&#10;	const parts = Object.fromEntries(&#10;		signatureHeader.split(&quot;,&quot;).map((part) =&gt; {&#10;			const [key, value] = part.split(&quot;=&quot;);&#10;			return [key, value];&#10;		}),&#10;	);&#10;&#10;	const time = parts[&quot;time&quot;];&#10;	const receivedSig = parts[&quot;sig1&quot;];&#10;&#10;	if (!time || !receivedSig) {&#10;		return { valid: false, body };&#10;	}&#10;&#10;	// Build the source string: &quot;&lt;time&gt;.&lt;body&gt;&quot;&#10;	const sourceString = `${time}.${body}`;&#10;	const encoder = new TextEncoder();&#10;&#10;	const key = await crypto.subtle.importKey(&#10;		&quot;raw&quot;,&#10;		encoder.encode(secret),&#10;		{ name: &quot;HMAC&quot;, hash: &quot;SHA-256&quot; },&#10;		false,&#10;		[&quot;sign&quot;],&#10;	);&#10;&#10;	const signature = await crypto.subtle.sign(&#10;		&quot;HMAC&quot;,&#10;		key,&#10;		encoder.encode(sourceString),&#10;	);&#10;&#10;	const expectedSig = [...new Uint8Array(signature)]&#10;		.map((b) =&gt; b.toString(16).padStart(2, &quot;0&quot;))&#10;		.join(&quot;&quot;);&#10;&#10;	// Use a timing-safe comparison.&#10;	// Do not return early when lengths differ — that leaks the expected&#10;	// signature&#x27;s length through timing.  Compare against self and negate instead.&#10;	const expectedBytes = encoder.encode(expectedSig);&#10;	const receivedBytes = encoder.encode(receivedSig);&#10;&#10;	const lengthsMatch = expectedBytes.byteLength === receivedBytes.byteLength;&#10;	const signaturesMatch = lengthsMatch&#10;		? crypto.subtle.timingSafeEqual(expectedBytes, receivedBytes)&#10;		: !crypto.subtle.timingSafeEqual(expectedBytes, expectedBytes);&#10;&#10;	return { valid: signaturesMatch, body };&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		if (request.method !== &quot;POST&quot;) {&#10;			return new Response(&quot;Method not allowed&quot;, { status: 405 });&#10;		}&#10;&#10;		if (!env.WEBHOOK_SECRET) {&#10;			console.error(&quot;WEBHOOK_SECRET is not set&quot;);&#10;			return new Response(&quot;Server misconfigured&quot;, { status: 500 });&#10;		}&#10;&#10;		const { valid, body } = await verifyWebhookSignature(&#10;			request,&#10;			env.WEBHOOK_SECRET,&#10;		);&#10;&#10;		if (!valid) {&#10;			console.error(&quot;Invalid webhook signature&quot;);&#10;			return new Response(&quot;Invalid signature&quot;, { status: 403 });&#10;		}&#10;&#10;		console.log(&quot;Webhook signature verified successfully&quot;);&#10;&#10;		const payload = JSON.parse(body);&#10;&#10;		console.log(&quot;Stream webhook received:&quot;, JSON.stringify(payload, null, 2));&#10;		console.log(&quot;Video UID:&quot;, payload.uid);&#10;		console.log(&quot;Status:&quot;, payload.status?.state);&#10;		console.log(&quot;Ready to stream:&quot;, payload.readyToStream);&#10;&#10;		// Add your own processing logic here — for example, update a database&#10;		// or notify a downstream service.&#10;&#10;		return new Response(&quot;OK&quot;, { status: 200 });&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="6-start-the-local-dev-server"><ol start="6">
<li>Start the local dev server</li>
</ol></h2>
<p>In a separate terminal (keep the tunnel running), start the Worker locally with Wrangler:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Wrangler will load the <code>WEBHOOK_SECRET</code> from your <code>.dev.vars</code> file automatically.</p>
<h2 id="7-trigger-a-test-event"><ol start="7">
<li>Trigger a test event</li>
</ol></h2>
<p>Upload a video to Stream to trigger a webhook event. Once the video finishes processing, you will see the webhook payload logged in the terminal running <code>wrangler dev</code>, along with a confirmation that the signature was verified.</p>
<h2 id="moving-to-production">Moving to production</h2>
<p>When you are done testing locally, deploy the Worker and update the webhook URL to your production endpoint:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Then update the webhook subscription to point to your deployed Worker URL:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/webhook \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;notificationUrl&quot;: &quot;https://your-worker.your-subdomain.workers.dev&quot;&#10;}&#x27;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14461.md")
</aside>
