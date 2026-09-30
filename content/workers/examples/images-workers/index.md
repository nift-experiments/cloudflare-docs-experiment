---
cp9:
  canonical: https://developers.cloudflare.com/workers/examples/images-workers/
  description: Set up custom domain for Images using a Worker or serve images using a prefix path and Cloudflare registered domain.
  full_title: Custom Domain with Images · Cloudflare Workers docs
  head_html: <title>Custom Domain with Images · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up custom domain for Images using a Worker or serve images using a prefix path and Cloudflare registered domain."><link rel="canonical" href="https://developers.cloudflare.com/workers/examples/images-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/examples/images-workers/index.md"><meta property="og:title" content="Custom Domain with Images · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up custom domain for Images using a Worker or serve images using a prefix path and Cloudflare registered domain."><meta property="og:url" content="https://developers.cloudflare.com/workers/examples/images-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="JavaScript,TypeScript,Python"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/examples/images-workers/#page","headline":"Custom Domain with Images \u00b7 Cloudflare Workers docs","description":"Set up custom domain for Images using a Worker or serve images using a prefix path and Cloudflare registered domain.","url":"https://developers.cloudflare.com/workers/examples/images-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","TypeScript","Python"]}</script>
  markdown: true
  noindex: false
  route: /workers/examples/images-workers/
  schema: 1
---
<p class="article-summary">Set up custom domain for Images using a Worker or serve images using a prefix path and Cloudflare registered domain.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/images-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<p>To serve images from a custom domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong> &gt; <strong>Workers</strong> &gt; <strong>Create Worker</strong> and create your Worker.</li>
<li>In your Worker, select <strong>Quick edit</strong> and paste the following code.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16432.md")
</div></div>
<p>Another way you can serve images from a custom domain is by using the <code>cdn-cgi/imagedelivery</code> prefix path which is used as path to trigger <code>cdn-cgi</code> image proxy.</p>
<p>Below is an example showing the hostname as a Cloudflare proxied domain under the same account as the Image, followed with the prefix path and the image <code>&lt;ACCOUNT_HASH&gt;</code>, <code>&lt;IMAGE_ID&gt;</code> and <code>&lt;VARIANT_NAME&gt;</code> which can be found in the <strong>Images</strong> on the Cloudflare dashboard.</p>
<pre tabindex="0"><code class="language-js">https://example.com/cdn-cgi/imagedelivery/&lt;ACCOUNT_HASH&gt;/&lt;IMAGE_ID&gt;/&lt;VARIANT_NAME&gt;&#10;</code></pre>
