---
cp9:
  canonical: https://developers.cloudflare.com/r2/get-started/cli/
  description: Use R2 from the command line with Wrangler, rclone, or AWS CLI.
  full_title: CLI · Cloudflare R2 docs
  head_html: <title>CLI · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Use R2 from the command line with Wrangler, rclone, or AWS CLI."><link rel="canonical" href="https://developers.cloudflare.com/r2/get-started/cli/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/get-started/cli/index.md"><meta property="og:title" content="CLI · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use R2 from the command line with Wrangler, rclone, or AWS CLI."><meta property="og:url" content="https://developers.cloudflare.com/r2/get-started/cli/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/get-started/cli/#page","headline":"CLI \u00b7 Cloudflare R2 docs","description":"Use R2 from the command line with Wrangler, rclone, or AWS CLI.","url":"https://developers.cloudflare.com/r2/get-started/cli/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/get-started/cli/
  schema: 1
---
<p>Manage R2 buckets and objects directly from your terminal. Use CLI tools to automate tasks and manage objects.</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/wrangler/">Wrangler</a></td>
<td>Single object operations and managing bucket settings with minimal setup</td>
</tr>
<tr>
<td><a href="/r2/examples/rclone/">rclone</a></td>
<td>Bulk object operations, migrations, and syncing directories</td>
</tr>
<tr>
<td><a href="/r2/examples/aws/aws-cli/">AWS CLI</a></td>
<td>Existing AWS workflows or familiarity with AWS CLI</td>
</tr>
</tbody>
</table>
<h2 id="1-create-a-bucket"><ol>
<li>Create a bucket</li>
</ol></h2>
<p>A bucket stores your objects in R2. To create a new R2 bucket:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11435.md")
</div></div>
<h2 id="2-generate-api-credentials"><ol start="2">
<li>Generate API credentials</li>
</ol></h2>
<p>CLI tools that use the S3 API (<a href="/r2/examples/aws/aws-cli/">AWS CLI</a>, <a href="/r2/examples/rclone/">rclone</a>) require an Access Key ID and Secret Access Key. If you are using <a href="/workers/wrangler/">Wrangler</a>, you can skip this step.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11436.md")
</div>
<h2 id="3-set-up-a-cli-tool"><ol start="3">
<li>Set up a CLI tool</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11443.md")
</div></div>
<h2 id="4-upload-and-download-objects"><ol start="4">
<li>Upload and download objects</li>
</ol></h2>
<p>(Optional) Create a test file to upload. Run this command in the directory where you plan to run the CLI commands:</p>
<pre tabindex="0"><code class="language-sh">echo &#x27;Hello, R2!&#x27; &gt; myfile.txt&#10;</code></pre>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11447.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls"><a href="/r2/api/s3/presigned-urls/">Presigned URLs</a></h3><p>Generate temporary URLs for private object access.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-public-buckets-r2-buckets-public-buckets"><a href="/r2/buckets/public-buckets/">Public buckets</a></h3><p>Serve files directly over HTTP with a public bucket.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cors-r2-buckets-cors"><a href="/r2/buckets/cors/">CORS</a></h3><p>Configure CORS for browser-based uploads.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles"><a href="/r2/buckets/object-lifecycles/">Object lifecycles</a></h3><p>Set up lifecycle rules to automatically delete old objects.</p></div>
