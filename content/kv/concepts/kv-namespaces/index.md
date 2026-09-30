---
cp9:
  canonical: https://developers.cloudflare.com/kv/concepts/kv-namespaces/
  description: A KV namespace is a key-value database replicated across Cloudflare's global network.
  full_title: KV namespaces · Cloudflare Workers KV docs
  head_html: <title>KV namespaces · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="A KV namespace is a key-value database replicated across Cloudflare&#x27;s global network."><link rel="canonical" href="https://developers.cloudflare.com/kv/concepts/kv-namespaces/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/concepts/kv-namespaces/index.md"><meta property="og:title" content="KV namespaces · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A KV namespace is a key-value database replicated across Cloudflare&#x27;s global network."><meta property="og:url" content="https://developers.cloudflare.com/kv/concepts/kv-namespaces/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/concepts/kv-namespaces/#page","headline":"KV namespaces \u00b7 Cloudflare Workers KV docs","description":"A KV namespace is a key-value database replicated across Cloudflare's global network.","url":"https://developers.cloudflare.com/kv/concepts/kv-namespaces/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/concepts/kv-namespaces/
  schema: 1
---
<p>A KV namespace is a key-value database replicated to Cloudflare’s global network.</p>
<p>Bind your KV namespaces through Wrangler or via the Cloudflare dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9523.md")
</aside>
<h2 id="jurisdictions">Jurisdictions</h2>
<p>Namespaces can optionally be restricted to a jurisdiction to durably store data only within a specific region. This feature is currently in private beta. Refer to <a href="/kv/reference/data-location/">Data location</a> for more information.</p>
<h2 id="bind-your-kv-namespace-through-wrangler">Bind your KV namespace through Wrangler</h2>
<p>To bind KV namespaces to your Worker, assign an array of the below object to the <code>kv_namespaces</code> key.</p>
<ul>
<li>
<p><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The binding name used to refer to the KV namespace.</li>
</ul>
</li>
<li>
<p><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The ID of the KV namespace.</li>
</ul>
</li>
<li>
<p><code>preview_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The ID of the KV namespace used during <code>wrangler dev</code>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9524.md")
</div>
<h2 id="bind-your-kv-namespace-via-the-dashboard">Bind your KV namespace via the dashboard</h2>
<p>To bind the namespace to your Worker in the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your **Worker**.
3. Select **Settings** > **Bindings**.
4. Select **Add**.
5. Select **KV Namespace**.
6. Enter your desired variable name (the name of the binding).
7. Select the KV namespace you wish to bind the Worker to.
8. Select **Deploy**.
