---
cp9:
  canonical: https://developers.cloudflare.com/r2/objects/delete-objects/
  description: Delete individual objects or folders from an R2 bucket.
  full_title: Delete objects · Cloudflare R2 docs
  head_html: <title>Delete objects · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Delete individual objects or folders from an R2 bucket."><link rel="canonical" href="https://developers.cloudflare.com/r2/objects/delete-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/objects/delete-objects/index.md"><meta property="og:title" content="Delete objects · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Delete individual objects or folders from an R2 bucket."><meta property="og:url" content="https://developers.cloudflare.com/r2/objects/delete-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/objects/delete-objects/#page","headline":"Delete objects \u00b7 Cloudflare R2 docs","description":"Delete individual objects or folders from an R2 bucket.","url":"https://developers.cloudflare.com/r2/objects/delete-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/objects/delete-objects/
  schema: 1
---
<p>You can delete objects from R2 using the dashboard, Workers API, S3 API, or command-line tools. To empty or delete an entire bucket, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a>.</p>
<h2 id="delete-via-dashboard">Delete via dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your bucket.
3. (Optional) Select the **View prefixes as directories** checkbox to view prefixes grouped as [folders](/r2/objects/#prefixes-and-folders).
4. Select the objects or folders you want to delete. You can select a mix of both in the same operation.
5. Select **Delete**.
6. Confirm your choice in the dialog that appears.
<p>To delete all objects in a bucket at once, refer to <a href="/r2/buckets/delete-buckets/#empty-a-bucket">Empty a bucket</a>.</p>
<h2 id="delete-via-workers-api">Delete via Workers API</h2>
<p>Use R2 <a href="/workers/runtime-apis/bindings/">bindings</a> in Workers to delete objects:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		await env.MY_BUCKET.delete(&quot;image.png&quot;);&#10;		return new Response(&quot;Deleted&quot;);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>For complete documentation, refer to <a href="/r2/api/workers/workers-api-usage/">Workers API</a>.</p>
<h2 id="delete-via-s3-api">Delete via S3 API</h2>
<p>Use S3-compatible SDKs to delete objects. You'll need your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/r2/api/tokens/">R2 API token</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11407.md")
</div></div>
<p>For complete S3 API documentation, refer to <a href="/r2/api/s3/api/">S3 API</a>.</p>
<h2 id="delete-via-wrangler">Delete via Wrangler</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11404.md")
</aside>
<p>Use <a href="/workers/wrangler/install-and-update/">Wrangler</a> to delete objects. Run the <a href="/workers/wrangler/commands/r2/#r2-object-delete"><code>r2 object delete</code> command</a>:</p>
<pre tabindex="0"><code class="language-sh">wrangler r2 object delete test-bucket/image.png&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-delete-buckets-r2-buckets-delete-buckets"><a href="/r2/buckets/delete-buckets/">Delete buckets</a></h3><p>Empty all objects from a bucket and permanently delete it.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-bucket-locks-r2-buckets-bucket-locks"><a href="/r2/buckets/bucket-locks/">Bucket locks</a></h3><p>Protect objects from accidental deletion with retention policies.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles"><a href="/r2/buckets/object-lifecycles/">Object lifecycles</a></h3><p>Automatically expire objects after a specified period.</p></div>
