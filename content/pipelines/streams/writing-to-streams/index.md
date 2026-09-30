---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/streams/writing-to-streams/
  description: Send data to streams via Worker bindings or HTTP endpoints
  full_title: Writing to streams · Cloudflare Pipelines Docs
  head_html: <title>Writing to streams · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Send data to streams via Worker bindings or HTTP endpoints"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/streams/writing-to-streams/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/streams/writing-to-streams/index.md"><meta property="og:title" content="Writing to streams · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send data to streams via Worker bindings or HTTP endpoints"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/streams/writing-to-streams/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/streams/writing-to-streams/#page","headline":"Writing to streams \u00b7 Cloudflare Pipelines Docs","description":"Send data to streams via Worker bindings or HTTP endpoints","url":"https://developers.cloudflare.com/pipelines/streams/writing-to-streams/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/streams/writing-to-streams/
  schema: 1
---
<p>Send events to streams using <a href="/workers/runtime-apis/bindings/">Worker bindings</a> or HTTP endpoints for client-side applications and external systems.</p>
<h2 id="send-via-workers">Send via Workers</h2>
<p>Worker bindings provide a secure way to send data to streams from <a href="/workers/">Workers</a> without managing API tokens or credentials.</p>
<h3 id="configure-pipeline-binding">Configure pipeline binding</h3>
<p>Add a pipeline binding to your Wrangler file that points to your stream:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11092.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11091.md")
</aside>
<h3 id="workers-api">Workers API</h3>
<p>The pipeline binding exposes a method for sending data to your stream:</p>
<h4 id="send-records"><code>send(records)</code></h4>
<p>Sends an array of JSON-serializable records to the stream. Returns a Promise that resolves when records are confirmed as ingested.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/11093.md")
</div>
<h3 id="typed-pipeline-bindings">Typed pipeline bindings</h3>
<p>When a stream has a defined schema, running <code>wrangler types</code> generates schema-specific TypeScript types for your pipeline bindings. Instead of the generic <code>Pipeline&lt;PipelineRecord&gt;</code>, your bindings get a named record type with full autocomplete and compile-time type checking. Refer to the <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code> documentation</a> to learn more.</p>
<h4 id="generated-types">Generated types</h4>
<p>After running <code>wrangler types</code>, the generated <code>worker-configuration.d.ts</code> file contains a named record type inside the <code>Cloudflare</code> namespace. The type name is derived from the stream name (not the binding name), converted to PascalCase with a <code>Record</code> suffix.</p>
<p>Below is an example of what generated types look like in <code>worker-configuration.d.ts</code> for a stream named <code>ecommerce_stream</code>:</p>
<pre tabindex="0"><code class="language-typescript">declare namespace Cloudflare {&#10;	type EcommerceStreamRecord = {&#10;		user_id: string;&#10;		event_type: string;&#10;		product_id?: string;&#10;		amount?: number;&#10;	};&#10;	interface Env {&#10;		STREAM: import(&quot;cloudflare:pipelines&quot;).Pipeline&lt;Cloudflare.EcommerceStreamRecord&gt;;&#10;	}&#10;}&#10;</code></pre>
<h4 id="fallback-behavior">Fallback behavior</h4>
<p><code>wrangler types</code> falls back to the generic <code>Pipeline&lt;PipelineRecord&gt;</code> type in the following scenarios:</p>
<ul>
<li><strong>Not authenticated</strong>: Run <code>wrangler login</code> to enable typed pipeline bindings.</li>
<li><strong>Stream not found</strong>: The stream ID in your Wrangler configuration does not match an existing stream.</li>
<li><strong>Unstructured stream</strong>: The stream was created without a schema.</li>
</ul>
<h2 id="send-via-http">Send via HTTP</h2>
<p>Each stream provides an optional HTTP endpoint for ingesting data from external applications, browsers, or any system that can make HTTP requests.</p>
<h3 id="endpoint-format">Endpoint format</h3>
<p>HTTP endpoints follow this format:</p>
<pre tabindex="0"><code class="language-txt">https://{stream-id}.ingest.cloudflare.com&#10;</code></pre>
<p>Find your stream's endpoint URL in the Cloudflare dashboard under <strong>Pipelines</strong> &gt; <strong>Streams</strong> or using the Wrangler CLI with either the stream ID or stream name:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler pipelines streams get &lt;STREAM_NAME_OR_ID&gt;&#10;</code></pre>
<h3 id="making-requests">Making requests</h3>
<p>Send events as JSON arrays via POST requests:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://{stream-id}.ingest.cloudflare.com \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;[&#10;    {&#10;      &quot;user_id&quot;: &quot;12345&quot;,&#10;      &quot;event_type&quot;: &quot;purchase&quot;,&#10;      &quot;product_id&quot;: &quot;widget-001&quot;,&#10;      &quot;amount&quot;: 29.99&#10;    }&#10;  ]&#x27;&#10;</code></pre>
<h3 id="authentication">Authentication</h3>
<p>When authentication is enabled for your stream, include the API token in the <code>Authorization</code> header:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://{stream-id}.ingest.cloudflare.com \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer YOUR_API_TOKEN&quot; \&#10;  &#45;d &#x27;[{&quot;event&quot;: &quot;test&quot;}]&#x27;&#10;</code></pre>
<p>The API token must have <strong>Workers Pipeline Send</strong> permission. To learn more, refer to the <a href="/fundamentals/api/get-started/create-token/">Create API token</a> documentation.</p>
<h2 id="schema-validation">Schema validation</h2>
<p>Streams handle validation differently based on their configuration:</p>
<ul>
<li><strong>Structured streams</strong>: Events must match the defined schema fields and types.</li>
<li><strong>Unstructured streams</strong>: Accept any valid JSON structure. Data is stored in a single <code>value</code> column.</li>
</ul>
<p>For structured streams, ensure your events match the schema definition. Invalid events will be accepted but dropped, so validate your data before sending to avoid dropped events. When using Worker bindings, run <code>wrangler types</code> to generate <a href="#typed-pipeline-bindings">typed pipeline bindings</a> that catch schema violations at compile time. You can also query the <a href="/pipelines/observability/metrics/#user-error-metrics">user error metrics</a> to monitor dropped events and diagnose schema validation issues.</p>
