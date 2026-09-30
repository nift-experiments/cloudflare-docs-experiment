---
cp9:
  canonical: https://developers.cloudflare.com/r2/get-started/s3/
  description: Use R2 with S3-compatible SDKs like boto3 and the AWS SDK.
  full_title: S3 · Cloudflare R2 docs
  head_html: <title>S3 · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Use R2 with S3-compatible SDKs like boto3 and the AWS SDK."><link rel="canonical" href="https://developers.cloudflare.com/r2/get-started/s3/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/get-started/s3/index.md"><meta property="og:title" content="S3 · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use R2 with S3-compatible SDKs like boto3 and the AWS SDK."><meta property="og:url" content="https://developers.cloudflare.com/r2/get-started/s3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/get-started/s3/#page","headline":"S3 \u00b7 Cloudflare R2 docs","description":"Use R2 with S3-compatible SDKs like boto3 and the AWS SDK.","url":"https://developers.cloudflare.com/r2/get-started/s3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/get-started/s3/
  schema: 1
---
<p>R2 provides support for a <a href="/r2/api/s3/api/">S3-compatible API</a>, which means you can use any S3 SDK, library, or tool to interact with your buckets. If you have existing code that works with S3, you can use it with R2 by changing the endpoint URL.</p>
<h2 id="1-create-a-bucket"><ol>
<li>Create a bucket</li>
</ol></h2>
<p>A bucket stores your objects in R2. To create a new R2 bucket:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11424.md")
</div></div>
<h2 id="2-generate-api-credentials"><ol start="2">
<li>Generate API credentials</li>
</ol></h2>
<p>To use the S3 API, you need to generate <a href="/r2/api/tokens/">credentials</a> and get an Access Key ID and Secret Access Key:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11425.md")
</div>
<p>You also need your S3 API endpoint URL which you can find at the bottom of the Create API Token confirmation page once you have created your token, or on the R2 Overview page:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com&#10;</code></pre>
<h2 id="3-use-an-aws-sdk"><ol start="3">
<li>Use an AWS SDK</li>
</ol></h2>
<p>The following examples show how to use Python and JavaScript SDKs. For other languages, refer to <a href="/r2/examples/aws/">S3-compatible SDK examples</a> for <a href="/r2/examples/aws/aws-sdk-go/">Go</a>, <a href="/r2/examples/aws/aws-sdk-java/">Java</a>, <a href="/r2/examples/aws/aws-sdk-php/">PHP</a>, <a href="/r2/examples/aws/aws-sdk-ruby/">Ruby</a>, and <a href="/r2/examples/aws/aws-sdk-rust/">Rust</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11430.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls"><a href="/r2/api/s3/presigned-urls/">Presigned URLs</a></h3><p>Generate temporary URLs for private object access.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-public-buckets-r2-buckets-public-buckets"><a href="/r2/buckets/public-buckets/">Public buckets</a></h3><p>Serve files directly over HTTP with a public bucket.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cors-r2-buckets-cors"><a href="/r2/buckets/cors/">CORS</a></h3><p>Configure CORS for browser-based uploads.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles"><a href="/r2/buckets/object-lifecycles/">Object lifecycles</a></h3><p>Set up lifecycle rules to automatically delete old objects.</p></div>
