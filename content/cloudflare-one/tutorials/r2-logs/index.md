---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/r2-logs/
  description: This tutorial covers how to build a Cloudflare R2 bucket to store Zero Trust logs. It also shows how to connect the bucket to the Zero Trust Logpush service.
  full_title: Use Cloudflare R2 as a Zero Trust log destination · Cloudflare One docs
  head_html: <title>Use Cloudflare R2 as a Zero Trust log destination · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial covers how to build a Cloudflare R2 bucket to store Zero Trust logs. It also shows how to connect the bucket to the Zero Trust Logpush service."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/r2-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/r2-logs/index.md"><meta property="og:title" content="Use Cloudflare R2 as a Zero Trust log destination · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial covers how to build a Cloudflare R2 bucket to store Zero Trust logs. It also shows how to connect the bucket to the Zero Trust Logpush service."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/r2-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="R2"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/r2-logs/#page","headline":"Use Cloudflare R2 as a Zero Trust log destination \u00b7 Cloudflare One docs","description":"This tutorial covers how to build a Cloudflare R2 bucket to store Zero Trust logs. It also shows how to connect the bucket to the Zero Trust Logpush service.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/r2-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/r2-logs/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4293.md")
</aside>
<p>This tutorial covers how to build a <a href="/r2/buckets/">Cloudflare R2 bucket</a> to store logs, and how to connect the bucket to the Zero Trust <a href="/cloudflare-one/insights/logs/logpush/">Logpush service</a> to store logs persistently and export them into other tools.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Ensure Cloudflare R2 and the Zero Trust Logpush integration are included in your plan. For more information, contact your account team.</li>
</ul>
<h2 id="create-a-cloudflare-r2-bucket">Create a Cloudflare R2 bucket</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to the <strong>R2 Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create bucket</strong>.</li>
<li>Enter an identifiable name for the bucket, then select <strong>Create bucket</strong>.</li>
</ol>
<h2 id="create-an-r2-api-token">Create an R2 API token</h2>
<ol>
<li>Return to <strong>R2</strong>, then select <strong>Manage R2 API tokens</strong>.</li>
<li>Select <strong>Create API token</strong>.</li>
<li>In <strong>Permissions</strong>, select <strong>Object Read &amp; Write</strong>.</li>
<li>In <strong>Specify bucket(s)</strong>, choose <em>Apply to specific buckets only</em>. Select the bucket you created.</li>
<li>Configure other token settings to your preferences.</li>
<li>Select <strong>Create API Token</strong>.</li>
<li>Copy the <strong>Access Key ID</strong>, <strong>Secret Access Key</strong>, and endpoint URL values. You will not be able to access these values again.</li>
<li>Select <strong>Finish</strong>.</li>
</ol>
<h2 id="connect-a-zero-trust-logpush-job">Connect a Zero Trust Logpush job</h2>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Logs</strong>. Select <strong>Manage Logpush</strong>.</li>
<li>Select <strong>Connect a service</strong>.</li>
<li>Choose which data sets and fields you want to send to your bucket. Select <strong>Next</strong>.</li>
<li>Select <strong>S3 Compatible</strong>.</li>
<li>In <strong>S3 Compatible Bucket Path</strong>, enter the name of your bucket.</li>
<li>In <strong>Bucket region</strong>, enter <code>auto</code>.</li>
<li>Enter the values for <strong>Access Key ID</strong>, <strong>Secret Access Key</strong>, and <strong>Endpoint URL</strong> in their corresponding fields.</li>
<li>Select <strong>Push</strong>. If prompted, you do not need to prove ownership with a token challenge.</li>
</ol>
<p>The Logpush job will send the selected Zero Trust logs to your R2 bucket.</p>
