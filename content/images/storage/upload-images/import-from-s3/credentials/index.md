---
cp9:
  canonical: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/
  description: Configure AWS IAM credentials for Amazon S3 read access.
  full_title: Credentials · Cloudflare Images docs
  head_html: <title>Credentials · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure AWS IAM credentials for Amazon S3 read access."><link rel="canonical" href="https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/index.md"><meta property="og:title" content="Credentials · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure AWS IAM credentials for Amazon S3 read access."><meta property="og:url" content="https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/#page","headline":"Credentials \u00b7 Cloudflare Images docs","description":"Configure AWS IAM credentials for Amazon S3 read access.","url":"https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/storage/upload-images/import-from-s3/credentials/
  schema: 1
---
<p>To import images, Cloudflare Images requires access to your Amazon S3 bucket. You can use credentials for any AWS Identity and Access Management (IAM) user with the correct permissions.</p>
<p>Cloudflare recommends creating a user with narrowly scoped permissions.</p>
<p>To create the required permissions:</p>
<ol>
<li>
<p>Log in to your AWS IAM account.</p>
</li>
<li>
<p>Create a policy with the following format (replace <code>&lt;BUCKET_NAME&gt;</code> with the bucket you want to grant access to):</p>
</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Action&quot;: [&quot;s3:Get*&quot;, &quot;s3:List*&quot;],&#10;			&quot;Resource&quot;: [&#10;				&quot;arn:aws:s3:::&lt;BUCKET_NAME&gt;&quot;,&#10;				&quot;arn:aws:s3:::&lt;BUCKET_NAME&gt;/*&quot;&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<ol start="3">
<li>Next, create a new user and attach the created policy to that user.</li>
</ol>
<p>You can now use both the Access Key ID and Secret Access Key to create a new source. Refer to <a href="/images/storage/upload-images/import-from-s3/enable/">Import images from S3</a> for setup instructions.</p>
