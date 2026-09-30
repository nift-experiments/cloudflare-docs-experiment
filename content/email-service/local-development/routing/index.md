<p class="article-summary">Test email routing Workers locally using wrangler dev with simulated incoming emails</p>
<p>Test email routing behavior locally using <code>wrangler dev</code> to simulate incoming emails and verify your routing logic before deploying.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8595.md")
</div></details>
<h2 id="configuration">Configuration</h2>
<p>Configure your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8596.md")
</div>
<h2 id="basic-routing-worker">Basic routing worker</h2>
<pre><code class="language-javascript">import * as PostalMime from &quot;postal-mime&quot;;&#10;&#10;export default {&#10;	async email(message, env, ctx) {&#10;		// Parse the raw email message&#10;		const parser = new PostalMime.default();&#10;		const rawEmail = new Response(message.raw);&#10;		const email = await parser.parse(await rawEmail.arrayBuffer());&#10;&#10;		console.log(&quot;Received email:&quot;, {&#10;			from: message.from,&#10;			to: message.to,&#10;			subject: email.subject,&#10;			text: email.text,&#10;			html: email.html,&#10;		});&#10;&#10;		// Route based on recipient&#10;		if (message.to.includes(&quot;support@&quot;)) {&#10;			await message.forward(&quot;support-team@example.com&quot;);&#10;		} else {&#10;			await message.forward(&quot;general@example.com&quot;);&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="testing">Testing</h2>
<p>Start your development server:</p>
<pre><code class="language-bash">npx wrangler dev&#10;</code></pre>
<p>Send a test email using the local endpoint. The request body must be a raw email message in <a href="https://datatracker.ietf.org/doc/html/rfc5322">RFC 5322</a> format, and the message must include a <code>Message-ID</code> header:</p>
<pre><code class="language-bash">curl --request POST &#x27;http://localhost:8787/cdn-cgi/local/email&#x27; \&#10;  &#45;-url-query &#x27;from=sender@example.com&#x27; \&#10;  &#45;-url-query &#x27;to=recipient@example.com&#x27; \&#10;  &#45;-data-raw &#x27;Received: from smtp.example.com (127.0.0.1)&#10;        by cloudflare-email.com (unknown) id 4fwwffRXOpyR&#10;        for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&#10;From: &quot;John&quot; &lt;sender@example.com&gt;&#10;Reply-To: sender@example.com&#10;To: recipient@example.com&#10;Subject: Testing Email Workers Local Dev&#10;Content-Type: text/html; charset=&quot;windows-1252&quot;&#10;X-Mailer: Curl&#10;Date: Tue, 27 Aug 2024 08:49:44 -0700&#10;Message-ID: &lt;6114391943504294873000@ZSH-GHOSTTY&gt;&#10;&#10;Hi there&#x27;&#10;</code></pre>
<p>This will output the parsed email structure in the console:</p>
<pre><code class="language-json">{&#10;	&quot;headers&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;received&quot;,&#10;			&quot;value&quot;: &quot;from smtp.example.com (127.0.0.1) by cloudflare-email.com (unknown) id 4fwwffRXOpyR for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&quot;&#10;		},&#10;		{ &quot;key&quot;: &quot;from&quot;, &quot;value&quot;: &quot;\&quot;John\&quot; &lt;sender@example.com&gt;&quot; },&#10;		{ &quot;key&quot;: &quot;reply-to&quot;, &quot;value&quot;: &quot;sender@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;to&quot;, &quot;value&quot;: &quot;recipient@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;subject&quot;, &quot;value&quot;: &quot;Testing Email Workers Local Dev&quot; },&#10;		{ &quot;key&quot;: &quot;content-type&quot;, &quot;value&quot;: &quot;text/html; charset=\&quot;windows-1252\&quot;&quot; },&#10;		{ &quot;key&quot;: &quot;x-mailer&quot;, &quot;value&quot;: &quot;Curl&quot; },&#10;		{ &quot;key&quot;: &quot;date&quot;, &quot;value&quot;: &quot;Tue, 27 Aug 2024 08:49:44 -0700&quot; },&#10;		{&#10;			&quot;key&quot;: &quot;message-id&quot;,&#10;			&quot;value&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;&#10;		}&#10;	],&#10;	&quot;from&quot;: { &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;John&quot; },&#10;	&quot;to&quot;: [{ &quot;address&quot;: &quot;recipient@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;replyTo&quot;: [{ &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;subject&quot;: &quot;Testing Email Workers Local Dev&quot;,&#10;	&quot;messageId&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;,&#10;	&quot;date&quot;: &quot;2024-08-27T15:49:44.000Z&quot;,&#10;	&quot;html&quot;: &quot;Hi there\n&quot;,&#10;	&quot;attachments&quot;: []&#10;}&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Deploy your routing worker: <a href="/email-service/get-started/route-emails/">Route emails get started</a></li>
<li>See advanced patterns: <a href="/email-service/examples/email-routing/">Email routing examples</a></li>
</ul>
