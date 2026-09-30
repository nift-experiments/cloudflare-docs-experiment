---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/
  description: Choose between untrusted and trusted isolation modes for user Workers in a Workers for Platforms dispatch namespace.
  full_title: Worker Isolation · Cloudflare for Platforms docs
  head_html: <title>Worker Isolation · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose between untrusted and trusted isolation modes for user Workers in a Workers for Platforms dispatch namespace."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/index.md"><meta property="og:title" content="Worker Isolation · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose between untrusted and trusted isolation modes for user Workers in a Workers for Platforms dispatch namespace."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare for Platforms"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/#page","headline":"Worker Isolation \u00b7 Cloudflare for Platforms docs","description":"Choose between untrusted and trusted isolation modes for user Workers in a Workers for Platforms dispatch namespace.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/
  schema: 1
---
<h3 id="untrusted-mode-default">Untrusted Mode (Default)</h3>
<p>By default, Workers inside of a dispatch namespace are considered &quot;untrusted.&quot; This provides the strongest isolation between Workers and is best in cases where your customers have control over the code that's being deployed.</p>
<p>In untrusted mode:</p>
<ul>
<li>The <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>request.cf</code></a> object is not available in Workers (see <a href="/cloudflare-for-platforms/workers-for-platforms/reference/limits/#cf-object">limits</a> for more information)</li>
<li>Each Worker has an isolated cache, when using the <a href="/workers/runtime-apis/cache/">Cache API</a> or when making subrequests using <code>fetch()</code>, which egress via <a href="/cache/">Cloudflare's cache</a></li>
<li><a href="/workers/reference/how-the-cache-works/#cache-api"><code>caches.default</code></a> is disabled for all Workers in the namespace</li>
</ul>
<p>This mode ensures complete isolation between customer Workers, preventing any potential cross-tenant data access.</p>
<h3 id="trusted-mode">Trusted Mode</h3>
<p>If you control the Worker code and want to disable isolation mode, you can configure the namespace as &quot;trusted&quot;. This is useful when building internal platforms where your company controls all Worker code.</p>
<p>In trusted mode:</p>
<ul>
<li>The <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>request.cf</code></a> object becomes available, providing access to request metadata</li>
<li>All Workers in the namespace share the same cache space when using the Cache API</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4188.md")
</aside>
<p>To convert a namespace from untrusted to trusted:</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{namespace_name}&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;name&quot;: &quot;{namespace_name}&quot;,&#10;    &quot;trusted_workers&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>If you enable trusted mode for a namespace that already has deployed Workers, you'll need to redeploy those Workers for the <code>request.cf</code> object to become available. Any new Workers you deploy after enabling trusted mode will automatically have access to it.</p>
<h3 id="maintaining-cache-isolation-in-trusted-mode">Maintaining cache isolation in trusted mode</h3>
If you need access to `request.cf` but want to maintain cache isolation between customers, use customer-specific [cache keys](/workers/examples/cache-using-fetch/#custom-cache-keys) or the [Cache API](/workers/examples/cache-api/) with isolated keys. 
<h2 id="related-resources">Related Resources</h2>
* [Platform Limits](/cloudflare-for-platforms/workers-for-platforms/reference/limits) - Understanding script and API limits
* [Cache API Documentation](/workers/runtime-apis/cache/) - Learn about cache behavior in Workers
* [Request cf object](/workers/runtime-apis/request/#the-cf-property-requestcf) - Details on the cf object properties
