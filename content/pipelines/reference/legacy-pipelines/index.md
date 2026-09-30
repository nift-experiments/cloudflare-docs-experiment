---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/reference/legacy-pipelines/
  description: Migration guide for pipelines created before September 2025 to the new Pipelines architecture.
  full_title: Legacy pipelines · Cloudflare Pipelines Docs
  head_html: <title>Legacy pipelines · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Migration guide for pipelines created before September 2025 to the new Pipelines architecture."><link rel="canonical" href="https://developers.cloudflare.com/pipelines/reference/legacy-pipelines/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/reference/legacy-pipelines/index.md"><meta property="og:title" content="Legacy pipelines · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migration guide for pipelines created before September 2025 to the new Pipelines architecture."><meta property="og:url" content="https://developers.cloudflare.com/pipelines/reference/legacy-pipelines/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/reference/legacy-pipelines/#page","headline":"Legacy pipelines \u00b7 Cloudflare Pipelines Docs","description":"Migration guide for pipelines created before September 2025 to the new Pipelines architecture.","url":"https://developers.cloudflare.com/pipelines/reference/legacy-pipelines/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/reference/legacy-pipelines/
  schema: 1
---
<p>Legacy pipelines, those created before September 25, 2025 via the legacy API, are on a deprecation path.</p>
<p>To check if your pipelines are legacy pipelines, view them in the dashboard under <strong>Pipelines</strong> &gt; <strong>Pipelines</strong> or run the <a href="/workers/wrangler/commands/pipelines/#pipelines-list"><code>pipelines list</code></a> command in <a href="/workers/wrangler/">Wrangler</a>. Legacy pipelines are labeled &quot;legacy&quot; in both locations.</p>
<p>New pipelines offer SQL transformations, multiple output formats, and improved architecture.</p>
<h2 id="notable-changes">Notable changes</h2>
<ul>
<li>New pipelines support SQL transformations for data processing.</li>
<li>New pipelines write to JSON, Parquet, and Apache Iceberg formats instead of JSON only.</li>
<li>New pipelines separate streams, pipelines, and sinks into distinct resources.</li>
<li>New pipelines support optional structured schemas with validation.</li>
<li>New pipelines offer configurable rolling policies and customizable partitioning.</li>
</ul>
<h2 id="moving-to-new-pipelines">Moving to new pipelines</h2>
<p>Legacy pipelines will continue to work until Pipelines is Generally Available, but new features and improvements are only available in the new pipeline architecture. To migrate:</p>
<ol>
<li>Create a new pipeline using the interactive setup:</li>
</ol>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<ol start="2">
<li>
<p>Configure your new pipeline with the desired streams, SQL transformations, and sinks.</p>
</li>
<li>
<p>Update your applications to send data to the new stream endpoints.</p>
</li>
<li>
<p>Once verified, delete your legacy pipeline.</p>
</li>
</ol>
<p>For detailed guidance, refer to the <a href="/pipelines/getting-started/">getting started guide</a>.</p>
