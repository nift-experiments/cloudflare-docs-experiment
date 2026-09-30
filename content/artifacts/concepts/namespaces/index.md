---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/concepts/namespaces/
  description: Organize repositories by environment or tenant.
  full_title: Namespaces · Cloudflare Artifacts docs
  head_html: <title>Namespaces · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Organize repositories by environment or tenant."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/concepts/namespaces/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/concepts/namespaces/index.md"><meta property="og:title" content="Namespaces · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Organize repositories by environment or tenant."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/concepts/namespaces/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/concepts/namespaces/#page","headline":"Namespaces \u00b7 Cloudflare Artifacts docs","description":"Organize repositories by environment or tenant.","url":"https://developers.cloudflare.com/artifacts/concepts/namespaces/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/concepts/namespaces/
  schema: 1
---
<p>Artifacts uses namespaces as top-level containers for repositories. Use them to separate repositories by environment, such as <code>prod</code>, <code>staging</code>, and <code>dev</code>, by tenant, or shard.</p>
<p>You can create a namespace explicitly or let Artifacts create one automatically. If you create a repo under a namespace name that does not exist, Artifacts creates the namespace automatically.</p>
<h2 id="use-namespaces-as-containers">Use namespaces as containers</h2>
<p>Start with one namespace per environment or tenant boundary.</p>
<ul>
<li>Use environment namespaces such as <code>prod</code>, <code>staging</code>, or <code>dev</code>.</li>
<li>Use tenant or shard namespaces when one shared namespace would become too hot or too large.</li>
<li>Keep repository names unique within each namespace.</li>
</ul>
<h2 id="choose-a-namespace-name">Choose a namespace name</h2>
<p>Start with a stable name such as <code>default</code>, <code>staging</code>, or <code>agents-realtime</code>.</p>
<p>Namespace names follow the same public naming rules as repo names:</p>
<ul>
<li>start with a letter or digit</li>
<li>use letters, digits, <code>.</code>, <code>_</code>, or <code>-</code> after the first character</li>
<li>keep the name stable across your Workers, API clients, and Git workflows</li>
</ul>
<p>If you have not chosen a namespace strategy yet, use <code>default</code> in the examples throughout this docset.</p>
<h2 id="choose-a-data-location">Choose a data location</h2>
<p>Select a jurisdiction when you create a namespace to restrict where Artifacts stores and processes repo data. Every repo in that namespace uses the selected jurisdiction.</p>
<p>You cannot change a namespace jurisdiction after creation. For supported jurisdictions and creation instructions, refer to <a href="/artifacts/guides/data-localization/">Data localization</a>.</p>
<h2 id="use-the-same-namespace-everywhere">Use the same namespace everywhere</h2>
<p>Use the same namespace name in your Wrangler binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3320.md")
</div>
<p>Use that same namespace in your REST base URL:</p>
<pre tabindex="0"><code class="language-sh">export ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;export ARTIFACTS_NAMESPACE=&quot;default&quot;&#10;export ARTIFACTS_BASE_URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE&quot;&#10;</code></pre>
<h2 id="split-namespaces-when-needed">Split namespaces when needed</h2>
<p>Start with one namespace when you are learning the product. Add more namespaces when you need clearer boundaries between environments, teams, or high-rate workloads.</p>
<p>For more information, refer to <a href="/artifacts/concepts/best-practices/#partition-namespaces-deliberately">Best practices for Artifacts</a>.</p>
