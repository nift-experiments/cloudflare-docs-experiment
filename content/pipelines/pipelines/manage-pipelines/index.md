---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/pipelines/manage-pipelines/
  description: Create, configure, and manage SQL transformations between streams and sinks
  full_title: Manage pipelines · Cloudflare Pipelines Docs
  head_html: <title>Manage pipelines · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, configure, and manage SQL transformations between streams and sinks"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/pipelines/manage-pipelines/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/pipelines/manage-pipelines/index.md"><meta property="og:title" content="Manage pipelines · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, configure, and manage SQL transformations between streams and sinks"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/pipelines/manage-pipelines/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/pipelines/manage-pipelines/#page","headline":"Manage pipelines \u00b7 Cloudflare Pipelines Docs","description":"Create, configure, and manage SQL transformations between streams and sinks","url":"https://developers.cloudflare.com/pipelines/pipelines/manage-pipelines/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/pipelines/manage-pipelines/
  schema: 1
---
<p>Learn how to:</p>
<ul>
<li>Create pipelines with SQL transformations</li>
<li>View pipeline configuration and SQL</li>
<li>Delete pipelines when no longer needed</li>
</ul>
<h2 id="create-a-pipeline">Create a pipeline</h2>
<p>Pipelines execute SQL statements that define how data flows from streams to sinks.</p>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11108.md")
</div>
<h3 id="wrangler-cli">Wrangler CLI</h3>
<p>To create a pipeline, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-create"><code>pipelines create</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines create my-pipeline \&#10;  &#45;-sql &quot;INSERT INTO my_sink SELECT * FROM my_stream&quot;&#10;</code></pre>
<p>You can also provide SQL from a file:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines create my-pipeline \&#10;  &#45;-sql-file pipeline.sql&#10;</code></pre>
<p>Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-setup"><code>pipelines setup</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<h3 id="sql-transformations">SQL transformations</h3>
<p>Pipelines support SQL statements for data transformation. For complete syntax, supported functions, and data types, see the <a href="/pipelines/sql-reference/">SQL reference</a>.</p>
<p>Common patterns include:</p>
<h4 id="basic-data-flow">Basic data flow</h4>
<p>Transfer all data from stream to sink:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO my_sink SELECT * FROM my_stream&#10;</code></pre>
<h4 id="filtering-events">Filtering events</h4>
<p>Filter events based on conditions:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO my_sink&#10;SELECT * FROM my_stream&#10;WHERE event_type = &#x27;purchase&#x27; AND amount &gt; 100&#10;</code></pre>
<h4 id="selecting-specific-fields">Selecting specific fields</h4>
<p>Choose only the fields you need:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO my_sink&#10;SELECT user_id, event_type, timestamp, amount&#10;FROM my_stream&#10;</code></pre>
<h4 id="transforming-data">Transforming data</h4>
<p>Apply transformations to fields:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO my_sink&#10;SELECT&#10;  user_id,&#10;  UPPER(event_type) as event_type,&#10;  timestamp,&#10;  amount * 1.1 as amount_with_tax&#10;FROM my_stream&#10;</code></pre>
<h4 id="route-one-stream-to-multiple-tables">Route one stream to multiple tables</h4>
<p>A single pipeline can run multiple <code>INSERT</code> statements, separated by semicolons. Each statement reads from the same stream and writes to a different sink, so you can route (&quot;fan out&quot;) events from one stream into several tables based on their content.</p>
<p>This avoids running a separate pipeline for each destination. Each statement filters the stream with its own <code>WHERE</code> clause and projects only the columns relevant to that table. This can also be a used as a cost optimization as you will be <a href="/pipelines/platform/pricing/">billed</a> once for the transformations, not per statement.</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO purchases_sink&#10;SELECT user_id, product_id, amount FROM my_stream&#10;WHERE event_type = &#x27;purchase&#x27;;&#10;&#10;INSERT INTO page_views_sink&#10;SELECT user_id, product_id FROM my_stream&#10;WHERE event_type = &#x27;view_product&#x27;;&#10;</code></pre>
<p>For a complete example that fans a live event stream out into five tables, refer to <a href="/pipelines/examples/bluesky-firehose-fanout/">Fan out a stream to multiple Iceberg tables</a>.</p>
<h2 id="view-pipeline-configuration">View pipeline configuration</h2>
<h3 id="dashboard-1">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11109.md")
</div>
<h3 id="wrangler-cli-1">Wrangler CLI</h3>
<p>To view a specific pipeline, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-get"><code>pipelines get</code></a> command with either the pipeline ID or pipeline name:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines get &lt;PIPELINE_NAME_OR_ID&gt;&#10;</code></pre>
<p>To list all pipelines in your account, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-list"><code>pipelines list</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines list&#10;</code></pre>
<h2 id="delete-a-pipeline">Delete a pipeline</h2>
<p>Deleting a pipeline stops data flow from the connected stream to sink.</p>
<h3 id="dashboard-2">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11110.md")
</div>
<h3 id="wrangler-cli-2">Wrangler CLI</h3>
<p>To delete a pipeline, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-delete"><code>pipelines delete</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines delete &lt;PIPELINE_ID&gt;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11107.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Pipeline SQL cannot be modified after creation. To change the SQL transformation, you must delete and recreate the pipeline.</p>
