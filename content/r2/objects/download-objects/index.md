---
cp9:
  canonical: https://developers.cloudflare.com/r2/objects/download-objects/
  description: Download objects from R2 using the dashboard, Workers API, S3 API, or CLI tools.
  full_title: Download objects · Cloudflare R2 docs
  head_html: <title>Download objects · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Download objects from R2 using the dashboard, Workers API, S3 API, or CLI tools."><link rel="canonical" href="https://developers.cloudflare.com/r2/objects/download-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/objects/download-objects/index.md"><meta property="og:title" content="Download objects · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Download objects from R2 using the dashboard, Workers API, S3 API, or CLI tools."><meta property="og:url" content="https://developers.cloudflare.com/r2/objects/download-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/objects/download-objects/#page","headline":"Download objects \u00b7 Cloudflare R2 docs","description":"Download objects from R2 using the dashboard, Workers API, S3 API, or CLI tools.","url":"https://developers.cloudflare.com/r2/objects/download-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/objects/download-objects/
  schema: 1
---
<p>You can download objects from R2 using the dashboard, Workers API, S3 API, or command-line tools.</p>
<h2 id="download-via-dashboard">Download via dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your bucket.
3. Locate the object you want to download.
4. Select **...** for the object and click **Download**.
<h2 id="download-via-workers-api">Download via Workers API</h2>
<p>Use R2 <a href="/workers/runtime-apis/bindings/">bindings</a> in Workers to download objects:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		const object = await env.MY_BUCKET.get(&quot;image.png&quot;);&#10;		if (object === null) {&#10;			return new Response(&quot;Object not found&quot;, { status: 404 });&#10;		}&#10;		return new Response(object.body);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>For complete documentation, refer to <a href="/r2/api/workers/workers-api-usage/">Workers API</a>.</p>
<h2 id="download-via-s3-api">Download via S3 API</h2>
<p>Use S3-compatible SDKs to download objects. You'll need your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/r2/api/tokens/">R2 API token</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11403.md")
</div></div>
<p>Refer to R2's <a href="/r2/api/s3/api/">S3 API documentation</a> for all S3 API methods.</p>
<h3 id="presigned-urls">Presigned URLs</h3>
<p>For client-side downloads where users download directly from R2, use presigned URLs. Your server generates a temporary download URL that clients can use without exposing your API credentials.</p>
<ol>
<li>Your application generates a presigned GET URL using an S3 SDK</li>
<li>Send the URL to your client</li>
<li>Client downloads directly from R2 using the presigned URL</li>
</ol>
<p>For details on generating and using presigned URLs, refer to <a href="/r2/api/s3/presigned-urls/">Presigned URLs</a>.</p>
<h2 id="download-via-wrangler">Download via Wrangler</h2>
<p>Use <a href="/workers/wrangler/install-and-update/">Wrangler</a> to download objects. Run the <a href="/workers/wrangler/commands/r2/#r2-object-get"><code>r2 object get</code> command</a>:</p>
<pre tabindex="0"><code class="language-sh">wrangler r2 object get test-bucket/image.png&#10;</code></pre>
<p>The file will be downloaded into the current working directory. You can also use the <code>--file</code> flag to set a new name for the object as it is downloaded, and the <code>--pipe</code> flag to pipe the download to standard output (stdout).</p>
