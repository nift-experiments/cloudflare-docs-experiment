---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/streams/manage-streams/
  description: Create, configure, and manage streams for data ingestion
  full_title: Manage streams · Cloudflare Pipelines Docs
  head_html: <title>Manage streams · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, configure, and manage streams for data ingestion"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/streams/manage-streams/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/streams/manage-streams/index.md"><meta property="og:title" content="Manage streams · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, configure, and manage streams for data ingestion"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/streams/manage-streams/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/streams/manage-streams/#page","headline":"Manage streams \u00b7 Cloudflare Pipelines Docs","description":"Create, configure, and manage streams for data ingestion","url":"https://developers.cloudflare.com/pipelines/streams/manage-streams/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/streams/manage-streams/
  schema: 1
---
<p>Learn how to:</p>
<ul>
<li>Create and configure streams for data ingestion</li>
<li>View and update stream settings</li>
<li>Delete streams when no longer needed</li>
</ul>
<h2 id="create-a-stream">Create a stream</h2>
<p>Streams are made available to pipelines as SQL tables using the stream name (for example, <code>SELECT * FROM my_stream</code>).</p>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11097.md")
</div>
<h3 id="wrangler-cli">Wrangler CLI</h3>
<p>To create a stream, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-streams-create"><code>pipelines streams create</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines streams create &lt;STREAM_NAME&gt;&#10;</code></pre>
<p>Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-setup"><code>pipelines setup</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<h3 id="schema-configuration">Schema configuration</h3>
<p>Streams support two approaches for handling data:</p>
<ul>
<li><strong>Structured streams</strong>: Define a schema with specific fields and data types. Events are validated against the schema.</li>
<li><strong>Unstructured streams</strong>: Accept any valid JSON without validation. These streams have a single <code>value</code> column containing the JSON data.</li>
</ul>
<p>To create a structured stream, provide a schema file:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines streams create my-stream --schema-file schema.json&#10;</code></pre>
<p>Example schema file:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;fields&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;user_id&quot;,&#10;			&quot;type&quot;: &quot;string&quot;,&#10;			&quot;required&quot;: true&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;amount&quot;,&#10;			&quot;type&quot;: &quot;float64&quot;,&#10;			&quot;required&quot;: false&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;tags&quot;,&#10;			&quot;type&quot;: &quot;list&quot;,&#10;			&quot;required&quot;: false,&#10;			&quot;items&quot;: {&#10;				&quot;type&quot;: &quot;string&quot;&#10;			}&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;metadata&quot;,&#10;			&quot;type&quot;: &quot;struct&quot;,&#10;			&quot;required&quot;: false,&#10;			&quot;fields&quot;: [&#10;				{&#10;					&quot;name&quot;: &quot;source&quot;,&#10;					&quot;type&quot;: &quot;string&quot;,&#10;					&quot;required&quot;: false&#10;				},&#10;				{&#10;					&quot;name&quot;: &quot;priority&quot;,&#10;					&quot;type&quot;: &quot;int32&quot;,&#10;					&quot;required&quot;: false&#10;				}&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p><strong>Supported data types:</strong></p>
<ul>
<li><code>string</code> - Text values</li>
<li><code>int32</code>, <code>int64</code> - Integer numbers</li>
<li><code>float32</code>, <code>float64</code> - Floating-point numbers</li>
<li><code>bool</code> - Boolean true/false</li>
<li><code>timestamp</code> - RFC 3339 timestamps, or numeric values parsed as Unix seconds, milliseconds, or microseconds (depending on unit)</li>
<li><code>json</code> - JSON objects</li>
<li><code>binary</code> - Binary data (base64-encoded)</li>
<li><code>list</code> - Arrays of values</li>
<li><code>struct</code> - Nested objects with defined fields</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11096.md")
</aside>
<h2 id="view-stream-configuration">View stream configuration</h2>
<h3 id="dashboard-1">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11098.md")
</div>
<h3 id="wrangler-cli-1">Wrangler CLI</h3>
<p>To view a specific stream, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-streams-get"><code>pipelines streams get</code></a> command with either the stream ID or stream name:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines streams get &lt;STREAM_NAME_OR_ID&gt;&#10;</code></pre>
<p>To list all streams in your account, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-streams-list"><code>pipelines streams list</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines streams list&#10;</code></pre>
<h2 id="update-http-ingest-settings">Update HTTP ingest settings</h2>
<p>You can update certain HTTP ingest settings after stream creation. Schema modifications are not supported once a stream is created.</p>
<h3 id="dashboard-2">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11099.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11095.md")
</aside>
<h2 id="delete-a-stream">Delete a stream</h2>
<h3 id="dashboard-3">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11100.md")
</div>
<h3 id="wrangler-cli-2">Wrangler CLI</h3>
<p>To delete a stream, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-streams-delete"><code>pipelines streams delete</code></a> command:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines streams delete &lt;STREAM_ID&gt;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11094.md")
</aside>
