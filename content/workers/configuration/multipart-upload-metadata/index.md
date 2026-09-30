---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/
  description: Define Workers configuration in JSON metadata for multipart form-data script uploads.
  full_title: Multipart upload metadata · Cloudflare Workers docs
  head_html: <title>Multipart upload metadata · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Define Workers configuration in JSON metadata for multipart form-data script uploads."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/index.md"><meta property="og:title" content="Multipart upload metadata · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Define Workers configuration in JSON metadata for multipart form-data script uploads."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#page","headline":"Multipart upload metadata \u00b7 Cloudflare Workers docs","description":"Define Workers configuration in JSON metadata for multipart form-data script uploads.","url":"https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/multipart-upload-metadata/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16620.md")
</aside>
<p>If you're using the <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload API</a> or <a href="/api/resources/workers/subresources/scripts/subresources/versions/methods/create/">Version Upload API</a> directly, <code>multipart/form-data</code> uploads require you to specify a <code>metadata</code> part. This metadata defines the Worker's configuration in JSON format, analogue to the <a href="/workers/wrangler/configuration/">wrangler.toml file</a>.</p>
<h2 id="sample-metadata">Sample <code>metadata</code></h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;main_module&quot;: &quot;main.js&quot;,&#10;	&quot;bindings&quot;: [&#10;		{&#10;			&quot;type&quot;: &quot;plain_text&quot;,&#10;			&quot;name&quot;: &quot;MESSAGE&quot;,&#10;			&quot;text&quot;: &quot;Hello, world!&quot;&#10;		}&#10;	],&#10;	&quot;compatibility_date&quot;: &quot;2021-09-14&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16619.md")
</aside>
<h2 id="attributes">Attributes</h2>
<p>The following attributes are configurable at the top-level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16618.md")
</aside>
<ul>
<li>
<p><code>main_module</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The part name that contains the module entry point of the Worker that will be executed. For example, <code>main.js</code>.</li>
</ul>
</li>
<li>
<p><code>assets</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li><a href="/workers/static-assets/">Asset</a> configuration for a Worker.</li>
<li><code>config</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li><a href="/workers/static-assets/routing/advanced/html-handling/">html_handling</a> determines the redirects and rewrites of requests for HTML content.</li>
<li><a href="/workers/static-assets/#routing-behavior">not_found_handling</a> determines the response when a request does not match a static asset.</li>
</ul>
</li>
<li><code>jwt</code> field provides a token authorizing assets to be attached to a Worker.</li>
</ul>
</li>
<li>
<p><code>keep_assets</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies whether assets should be retained from a previously uploaded Worker version; used in lieu of providing a completion token.</li>
</ul>
</li>
<li>
<p><code>bindings</code> array[object] optional</p>
<ul>
<li><a href="#bindings">Bindings</a> to expose in the Worker.</li>
</ul>
</li>
<li>
<p><code>placement</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li><a href="/workers/configuration/placement/">Smart placement</a> object for the Worker.</li>
<li><code>mode</code> field only supports <code>smart</code> for automatic placement.</li>
</ul>
</li>
<li>
<p><code>compatibility_date</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li><a href="/workers/configuration/compatibility-dates/#setting-compatibility-date">Compatibility Date</a> indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker. Highly recommended to set a <code>compatibility_date</code>, otherwise if on upload via the API, it defaults to the oldest compatibility date before any flags took effect (2021-11-02).</li>
</ul>
</li>
<li>
<p><code>compatibility_flags</code> array[string] optional</p>
<ul>
<li><a href="/workers/configuration/compatibility-flags/#setting-compatibility-flags">Compatibility Flags</a> that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a <code>compatibility_date</code>.</li>
</ul>
</li>
</ul>
<h2 id="additional-attributes-workers-script-upload-api-api-resources-workers-subresources-scripts-methods-update">Additional attributes: <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload API</a></h2>
<p>For <a href="/workers/versions-and-deployments/#upload-a-new-version-and-deploy-it-immediately">immediately deployed uploads</a>, the following <strong>additional</strong> attributes are configurable at the top-level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16617.md")
</aside>
<ul>
<li>
<p><code>migrations</code> array[object] optional</p>
<ul>
<li><a href="/durable-objects/reference/durable-objects-migrations/">Durable Objects migrations</a> to apply.</li>
</ul>
</li>
<li>
<p><code>logpush</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Whether <a href="/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/#logpush">Logpush</a> is turned on for the Worker.</li>
</ul>
</li>
<li>
<p><code>tail_consumers</code> array[object] optional</p>
<ul>
<li><a href="/workers/observability/logs/tail-workers/">Tail Workers</a> that will consume logs from the attached Worker.</li>
</ul>
</li>
<li>
<p><code>tags</code> array[string] optional</p>
<ul>
<li>List of strings to use as tags for this Worker.</li>
</ul>
</li>
<li>
<p><code>annotations</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Annotations object for the Worker version created by this upload. Also available on the <a href="#additional-attributes-version-upload-api">Version Upload API</a>.</li>
<li><code>workers/message</code> specifies a custom message for the version.</li>
<li><code>workers/tag</code> specifies a custom identifier for the version.</li>
</ul>
</li>
</ul>
<h2 id="additional-attributes-version-upload-api-api-resources-workers-subresources-scripts-subresources-versions-methods-create">Additional attributes: <a href="/api/resources/workers/subresources/scripts/subresources/versions/methods/create/">Version Upload API</a></h2>
<p>For <a href="/workers/versions-and-deployments/#upload-a-new-version-to-be-gradually-deployed-or-deployed-at-a-later-time">version uploads</a>, the following <strong>additional</strong> attributes are configurable at the top-level.</p>
<ul>
<li><code>annotations</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Annotations object specific to the Worker version.</li>
<li><code>workers/message</code> specifies a custom message for the version.</li>
<li><code>workers/tag</code> specifies a custom identifier for the version.</li>
<li><code>workers/alias</code> specifies a custom alias for this version.</li>
</ul>
</li>
</ul>
<h2 id="bindings">Bindings</h2>
<p>Workers can interact with resources on the Cloudflare Developer Platform using <a href="/workers/runtime-apis/bindings/">bindings</a>. Refer to the JSON example below that shows how to add bindings in the <code>metadata</code> part.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;bindings&quot;: [&#10;		{&#10;			&quot;type&quot;: &quot;ai&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;analytics_engine&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;dataset&quot;: &quot;&lt;DATASET&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;assets&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;browser_rendering&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;d1&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;id&quot;: &quot;&lt;D1_ID&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;durable_object_namespace&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;class_name&quot;: &quot;&lt;DO_CLASS_NAME&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;hyperdrive&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;id&quot;: &quot;&lt;HYPERDRIVE_ID&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;kv_namespace&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;namespace_id&quot;: &quot;&lt;KV_ID&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;mtls_certificate&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;certificate_id&quot;: &quot;&lt;MTLS_CERTIFICATE_ID&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;plain_text&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;text&quot;: &quot;&lt;VARIABLE_VALUE&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;queue&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;queue_name&quot;: &quot;&lt;QUEUE_NAME&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;r2_bucket&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;bucket_name&quot;: &quot;&lt;R2_BUCKET_NAME&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;secret_text&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;text&quot;: &quot;&lt;SECRET_VALUE&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;service&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;service&quot;: &quot;&lt;SERVICE_NAME&gt;&quot;,&#10;			&quot;environment&quot;: &quot;production&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;vectorize&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;,&#10;			&quot;index_name&quot;: &quot;&lt;INDEX_NAME&gt;&quot;&#10;		},&#10;		{&#10;			&quot;type&quot;: &quot;version_metadata&quot;,&#10;			&quot;name&quot;: &quot;&lt;VARIABLE_NAME&gt;&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
