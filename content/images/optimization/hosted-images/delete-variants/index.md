---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/
  description: Remove image variants from Cloudflare Images using the dashboard or API.
  full_title: Delete variants · Cloudflare Images docs
  head_html: <title>Delete variants · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Remove image variants from Cloudflare Images using the dashboard or API."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/index.md"><meta property="og:title" content="Delete variants · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Remove image variants from Cloudflare Images using the dashboard or API."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/#page","headline":"Delete variants \u00b7 Cloudflare Images docs","description":"Remove image variants from Cloudflare Images using the dashboard or API.","url":"https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/hosted-images/delete-variants/
  schema: 1
---
<p>You can delete variants via the Images dashboard or API. The only variant you cannot delete is public.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9471.md")
</aside>
<h2 id="delete-variants-via-the-cloudflare-dashboard">Delete variants via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Delivery</strong> tab.</p>
</li>
<li>
<p>Find the variant you want to remove and select <strong>Delete</strong>.</p>
</li>
</ol>
<h2 id="delete-variants-via-the-api">Delete variants via the API</h2>
<p>Make a <code>DELETE</code> request to the delete variant endpoint.</p>
<pre tabindex="0"><code class="language-bash">curl --request DELETE https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/variants/{variant_name} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>After the variant has been deleted, the response returns <code>&quot;success&quot;: true.</code></p>
