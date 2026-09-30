---
cp9:
  canonical: https://developers.cloudflare.com/r2-sql/get-started/
  description: Create your first pipeline to ingest streaming data and write to R2 Data Catalog as an Apache Iceberg table.
  full_title: Getting started · R2 SQL docs
  head_html: <title>Getting started · R2 SQL docs</title><meta name="generator" content="Nift"><meta name="description" content="Create your first pipeline to ingest streaming data and write to R2 Data Catalog as an Apache Iceberg table."><link rel="canonical" href="https://developers.cloudflare.com/r2-sql/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-sql/get-started/index.md"><meta property="og:title" content="Getting started · R2 SQL docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create your first pipeline to ingest streaming data and write to R2 Data Catalog as an Apache Iceberg table."><meta property="og:url" content="https://developers.cloudflare.com/r2-sql/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 SQL"><meta name="algolia_product_filter" content="R2 SQL"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="R2 SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-sql/get-started/#page","headline":"Getting started \u00b7 R2 SQL docs","description":"Create your first pipeline to ingest streaming data and write to R2 Data Catalog as an Apache Iceberg table.","url":"https://developers.cloudflare.com/r2-sql/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-sql/get-started/
  schema: 1
---
<p>This guide will instruct you through:</p>
<ul>
<li>Creating your first <a href="/r2/buckets/">R2 bucket</a> and enabling its <a href="/r2-data-catalog/">data catalog</a>.</li>
<li>Creating an <a href="/r2/api/tokens/">API token</a> needed for pipelines to authenticate with your data catalog.</li>
<li>Creating your first pipeline with a simple ecommerce schema that writes to an <a href="https://iceberg.apache.org/">Apache Iceberg</a> table managed by R2 Data Catalog.</li>
<li>Sending sample ecommerce data via HTTP endpoint.</li>
<li>Validating data in your bucket and querying it with R2 SQL.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/510.md")
</div></details>
<h2 id="1-create-an-r2-bucket"><ol>
<li>Create an R2 bucket</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/515.md")
</div></div>
<h2 id="2-enable-r2-data-catalog"><ol start="2">
<li>Enable R2 Data Catalog</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/519.md")
</div></div>
<h2 id="3-create-an-api-token"><ol start="3">
<li>Create an API token</li>
</ol></h2>
<p>Pipelines must authenticate to R2 Data Catalog with an <a href="/r2/api/tokens/">R2 API token</a> that has catalog and R2 permissions.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/520.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/509.md")
</aside>
<h2 id="4-create-a-pipeline"><ol start="4">
<li>Create a pipeline</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/524.md")
</div></div>
<h2 id="5-send-sample-data"><ol start="5">
<li>Send sample data</li>
</ol></h2>
<p>Send ecommerce events to your pipeline's HTTP endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://{stream-id}.ingest.cloudflare.com \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;[&#10;    {&#10;      &quot;user_id&quot;: &quot;user_12345&quot;,&#10;      &quot;event_type&quot;: &quot;purchase&quot;,&#10;      &quot;product_id&quot;: &quot;widget-001&quot;,&#10;      &quot;amount&quot;: 29.99&#10;    },&#10;    {&#10;      &quot;user_id&quot;: &quot;user_67890&quot;,&#10;      &quot;event_type&quot;: &quot;view_product&quot;,&#10;      &quot;product_id&quot;: &quot;widget-002&quot;&#10;    },&#10;    {&#10;      &quot;user_id&quot;: &quot;user_12345&quot;,&#10;      &quot;event_type&quot;: &quot;add_to_cart&quot;,&#10;      &quot;product_id&quot;: &quot;widget-003&quot;,&#10;      &quot;amount&quot;: 15.50&#10;    }&#10;  ]&#x27;&#10;</code></pre>
<p>Replace <code>{stream-id}</code> with your actual stream endpoint from the pipeline setup.</p>
<h2 id="6-validate-data-in-your-bucket"><ol start="6">
<li>Validate data in your bucket</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/525.md")
</div>
<h2 id="7-query-your-data-using-r2-sql"><ol start="7">
<li>Query your data using R2 SQL</li>
</ol></h2>
<p>Set up your environment to use R2 SQL:</p>
<pre tabindex="0"><code class="language-bash">export WRANGLER_R2_SQL_AUTH_TOKEN=YOUR_API_TOKEN&#10;</code></pre>
<p>Or create a <code>.env</code> file with:</p>
<pre tabindex="0"><code>WRANGLER_R2_SQL_AUTH_TOKEN=YOUR_API_TOKEN&#10;</code></pre>
<p>Where <code>YOUR_API_TOKEN</code> is the token you created in step 3. For more information on setting environment variables, refer to <a href="/workers/wrangler/system-environment-variables/">Wrangler system environment variables</a>.</p>
<p>Query your data:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 sql query &quot;YOUR_WAREHOUSE_NAME&quot; &quot;&#10;SELECT&#10;    user_id,&#10;    event_type,&#10;    product_id,&#10;    amount&#10;FROM default.ecommerce&#10;WHERE event_type = &#x27;purchase&#x27;&#10;LIMIT 10&quot;&#10;</code></pre>
<p>Replace <code>YOUR_WAREHOUSE_NAME</code> with the warehouse name from step 2.</p>
<p>You can also query this table with any engine that supports Apache Iceberg. To connect other engines to R2 Data Catalog, refer to <a href="/r2-data-catalog/config-examples/">Connect to Iceberg engines</a>.</p>
<h2 id="learn-more">Learn more</h2>
<div class="nb-card nb-link-card"><h3 id="card-managing-r2-data-catalogs-r2-data-catalog-manage-catalogs"><a href="/r2-data-catalog/manage-catalogs/">Managing R2 Data Catalogs</a></h3><p>Enable or disable R2 Data Catalog on your bucket, retrieve configuration details, and authenticate your Iceberg engine.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-try-another-example-r2-sql-tutorials-end-to-end-pipeline"><a href="/r2-sql/tutorials/end-to-end-pipeline">Try another example</a></h3><p>Detailed tutorial for setting up a simple fraud detection data pipeline, and generate events for it in Python.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-pipelines-pipelines"><a href="/pipelines/">Pipelines</a></h3><p>Understand SQL transformations and pipeline configuration.</p></div>
