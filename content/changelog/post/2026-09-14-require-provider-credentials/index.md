<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 14, 2026</time><h2 id="post-title">Prevent Unified Billing fallback for BYOK third-party providers</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.</p>
<p>Turn on <strong>Require provider credentials</strong> in your gateway settings. To use the API, set <code>byok_only</code> to <code>true</code> in the request body of a <a href="/api/resources/ai_gateway/methods/update/"><code>PUT</code> request to update the gateway</a>:</p>
<pre><code class="language-json">{&#10;	&quot;byok_only&quot;: true&#10;}&#10;</code></pre>
<p>To require provider credentials for one third-party request, set the <code>cf-aig-no-wholesale</code> header to <code>true</code>. This header cannot relax the gateway setting.</p>
<p>Requests without applicable credentials then return an HTTP <code>400</code> response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.</p>
<p>For configuration details and request-level controls, refer to <a href="/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</a>.</p>
</div></article></div>
