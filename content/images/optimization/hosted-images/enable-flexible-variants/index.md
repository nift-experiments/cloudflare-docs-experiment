---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/
  description: Turn on flexible variants in Cloudflare Images to allow dynamic resizing beyond predefined variant options.
  full_title: Enable flexible variants · Cloudflare Images docs
  head_html: <title>Enable flexible variants · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn on flexible variants in Cloudflare Images to allow dynamic resizing beyond predefined variant options."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/index.md"><meta property="og:title" content="Enable flexible variants · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn on flexible variants in Cloudflare Images to allow dynamic resizing beyond predefined variant options."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/#page","headline":"Enable flexible variants \u00b7 Cloudflare Images docs","description":"Turn on flexible variants in Cloudflare Images to allow dynamic resizing beyond predefined variant options.","url":"https://developers.cloudflare.com/images/optimization/hosted-images/enable-flexible-variants/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/hosted-images/enable-flexible-variants/
  schema: 1
---
<p>Flexible variants allow you to create variants with dynamic resizing which can provide more options than regular variants allow. This option is not enabled by default.</p>
<h2 id="enable-flexible-variants-via-the-cloudflare-dashboard">Enable flexible variants via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Delivery</strong> tab.</p>
</li>
<li>
<p>Enable <strong>Flexible variants</strong>.</p>
</li>
</ol>
<h2 id="enable-flexible-variants-via-the-api">Enable flexible variants via the API</h2>
<p>Make a <code>PATCH</code> request to the <a href="/api/resources/images/subresources/v1/subresources/variants/methods/edit/">Update a variant endpoint</a>.</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;flexible_variants&quot;: true}&#x27;&#10;</code></pre>
<p>After activation, you can use <a href="/images/optimization/features/#parameters">optimization parameters</a> on any Cloudflare image. For example,</p>
<p><code>https://imagedelivery.net/{account_hash}/{image_id}/w=400,sharpen=3</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9470.md")
</aside>
