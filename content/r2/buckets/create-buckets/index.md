---
cp9:
  canonical: https://developers.cloudflare.com/r2/buckets/create-buckets/
  description: Create R2 buckets using the Cloudflare dashboard or Wrangler CLI.
  full_title: Create new buckets · Cloudflare R2 docs
  head_html: <title>Create new buckets · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Create R2 buckets using the Cloudflare dashboard or Wrangler CLI."><link rel="canonical" href="https://developers.cloudflare.com/r2/buckets/create-buckets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/buckets/create-buckets/index.md"><meta property="og:title" content="Create new buckets · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create R2 buckets using the Cloudflare dashboard or Wrangler CLI."><meta property="og:url" content="https://developers.cloudflare.com/r2/buckets/create-buckets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/buckets/create-buckets/#page","headline":"Create new buckets \u00b7 Cloudflare R2 docs","description":"Create R2 buckets using the Cloudflare dashboard or Wrangler CLI.","url":"https://developers.cloudflare.com/r2/buckets/create-buckets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/buckets/create-buckets/
  schema: 1
---
<p>You can create a bucket from the Cloudflare dashboard or using Wrangler.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11495.md")
</aside>
<h2 id="bucket-level-operations">Bucket-Level Operations</h2>
<p>Create a bucket with the <a href="/workers/wrangler/commands/r2/#r2-bucket-create"><code>r2 bucket create</code></a> command:</p>
<pre tabindex="0"><code class="language-sh">wrangler r2 bucket create your-bucket-name&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11494.md")
</aside>
<p>List buckets in the current account with the <a href="/workers/wrangler/commands/r2/#r2-bucket-list"><code>r2 bucket list</code></a> command:</p>
<pre tabindex="0"><code class="language-sh">wrangler r2 bucket list&#10;</code></pre>
<p>To delete a bucket, you must first empty it and then delete it. For detailed instructions, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a>.</p>
<h2 id="notes">Notes</h2>
<ul>
<li>Bucket names and buckets are not public by default. To allow public access to a bucket, refer to <a href="/r2/buckets/public-buckets/">Public buckets</a>.</li>
<li>For information on controlling access to your R2 bucket with Cloudflare Access, refer to <a href="/r2/tutorials/cloudflare-access/">Protect an R2 Bucket with Cloudflare Access</a>.</li>
<li>Invalid (unauthorized) access attempts to private buckets do not incur R2 operations charges against that bucket. Refer to the <a href="/r2/pricing/#frequently-asked-questions">R2 pricing FAQ</a> to understand what operations are billed vs. not billed.</li>
</ul>
