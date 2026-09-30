---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sinks/manage-sinks/
  description: Create, configure, and manage sinks for data storage
  full_title: Manage sinks · Cloudflare Pipelines Docs
  head_html: <title>Manage sinks · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, configure, and manage sinks for data storage"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sinks/manage-sinks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sinks/manage-sinks/index.md"><meta property="og:title" content="Manage sinks · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, configure, and manage sinks for data storage"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sinks/manage-sinks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sinks/manage-sinks/#page","headline":"Manage sinks \u00b7 Cloudflare Pipelines Docs","description":"Create, configure, and manage sinks for data storage","url":"https://developers.cloudflare.com/pipelines/sinks/manage-sinks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sinks/manage-sinks/
  schema: 1
---
<p>Learn how to:</p>
<ul>
<li>Create and configure sinks for data storage</li>
<li>View sink configuration</li>
<li>Delete sinks when no longer needed</li>
</ul>
<h2 id="create-a-sink">Create a sink</h2>
<p>Sinks are made available to pipelines as SQL tables using the sink name (e.g., <code>INSERT INTO my_sink SELECT * FROM my_stream</code>).</p>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11102.md")
</div>
<h3 id="wrangler-cli">Wrangler CLI</h3>
<p>To create a sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-create"><code>pipelines sinks create</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks create &lt;SINK_NAME&gt; \&#10;  &#45;-type r2 \&#10;  &#45;-bucket my-bucket \&#10;</code></pre>
<p>For sink-specific configuration options, refer to <a href="/pipelines/sinks/available-sinks/">Available sinks</a>.</p>
<p>Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-setup"><code>pipelines setup</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<h2 id="view-sink-configuration">View sink configuration</h2>
<h3 id="dashboard-1">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11103.md")
</div>
<h3 id="wrangler-cli-1">Wrangler CLI</h3>
<p>To view a specific sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-get"><code>pipelines sinks get</code></a> command with either the sink ID or sink name:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks get &lt;SINK_NAME_OR_ID&gt;&#10;</code></pre>
<p>To list all sinks in your account, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-list"><code>pipelines sinks list</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks list&#10;</code></pre>
<h2 id="delete-a-sink">Delete a sink</h2>
<h3 id="dashboard-2">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11104.md")
</div>
<h3 id="wrangler-cli-2">Wrangler CLI</h3>
<p>To delete a sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-delete"><code>pipelines sinks delete</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines sinks delete &lt;SINK_ID&gt;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11101.md")
</aside>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Sinks cannot be modified after creation. To change sink configuration, you must delete and recreate the sink.</li>
<li>The R2 Data Catalog Sink does not currently support writing to R2 buckets into a different jurisdiction.</li>
</ul>
