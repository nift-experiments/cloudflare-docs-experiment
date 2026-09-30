<p>Custom metadata in AI Gateway allows you to tag requests with user IDs or other identifiers, enabling better tracking and analysis of your requests. Metadata values can be strings, numbers, or booleans, and will appear in your logs, making it easy to search and filter through your data.</p>
<h2 id="key-features">Key Features</h2>
<ul>
<li><strong>Custom Tagging</strong>: Add user IDs, team names, test indicators, and other relevant information to your requests.</li>
<li><strong>Enhanced Logging</strong>: Metadata appears in your logs, allowing for detailed inspection and troubleshooting.</li>
<li><strong>Search and Filter</strong>: Use metadata to efficiently search and filter through logged requests.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2802.md")
</aside>
<h2 id="supported-metadata-types">Supported Metadata Types</h2>
<ul>
<li>String</li>
<li>Number</li>
<li>Boolean</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2801.md")
</aside>
<h2 id="reserved-metadata">Reserved metadata</h2>
<p>Metadata keys that begin with <code>cf.</code> are reserved for metadata added by Cloudflare. Do not send your own <code>cf.*</code> metadata keys. AI Gateway removes customer-supplied <code>cf.*</code> keys before saving request metadata.</p>
<p>When a request reaches AI Gateway through a custom domain protected by <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>, AI Gateway adds the authenticated Access user ID to request metadata as <code>cf.user_id</code>. This value is the verified Access JWT <code>sub</code> claim, not the user's email address.</p>
<p>AI Gateway guarantees that <code>cf.user_id</code> is saved when a valid Access user ID is present. If the request already has five custom metadata entries, AI Gateway may remove the last custom entry so <code>cf.user_id</code> can be saved. Service-token requests and requests without a user subject do not receive <code>cf.user_id</code> metadata.</p>
<h2 id="implementations">Implementations</h2>
<h3 id="using-curl">Using cURL</h3>
<p>To include custom metadata in your request using cURL:</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &#x27;cf-aig-metadata: {&quot;team&quot;: &quot;AI&quot;, &quot;user&quot;: 12345, &quot;test&quot;:true}&#x27; \&#10;  &#45;-data &#x27;{&quot;model&quot;: &quot;openai/gpt-4.1&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What should I eat for lunch?&quot;}]}&#x27;&#10;</code></pre>
<h3 id="using-sdk">Using SDK</h3>
<p>To include custom metadata in your request using the OpenAI SDK:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2803.md")
</div>
<h3 id="using-binding">Using Binding</h3>
<p>To include custom metadata in your request using <a href="/workers/runtime-apis/bindings/">Bindings</a>:</p>
<pre><code class="language-javascript">export default {&#10;	async fetch(request, env, ctx) {&#10;		const aiResp = await env.AI.run(&#10;			&quot;@cf/mistral/mistral-7b-instruct-v0.1&quot;,&#10;			{ prompt: &quot;What should I eat for lunch?&quot; },&#10;			{&#10;				gateway: {&#10;					id: &quot;gateway_id&quot;,&#10;					metadata: { team: &quot;AI&quot;, user: 12345, test: true },&#10;				},&#10;			},&#10;		);&#10;&#10;		return new Response(aiResp);&#10;	},&#10;};&#10;</code></pre>
