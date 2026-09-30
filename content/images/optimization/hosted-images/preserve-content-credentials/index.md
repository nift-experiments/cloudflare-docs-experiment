---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/
  description: Retain C2PA metadata and provenance data on images delivered from Cloudflare Images.
  full_title: Preserve Content Credentials · Cloudflare Images docs
  head_html: <title>Preserve Content Credentials · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Retain C2PA metadata and provenance data on images delivered from Cloudflare Images."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/index.md"><meta property="og:title" content="Preserve Content Credentials · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Retain C2PA metadata and provenance data on images delivered from Cloudflare Images."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/#page","headline":"Preserve Content Credentials \u00b7 Cloudflare Images docs","description":"Retain C2PA metadata and provenance data on images delivered from Cloudflare Images.","url":"https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/hosted-images/preserve-content-credentials/
  schema: 1
---
<p><a href="https://contentcredentials.org/">Content Credentials</a> (or C2PA metadata) are a type of metadata that includes the full provenance chain of a digital asset. This provides information about an image's creation, authorship, and editing flow. This data is cryptographically authenticated and can be verified using an <a href="https://contentcredentials.org/verify">open-source verification service</a>.</p>
<p>You can preserve Content Credentials on images uploaded to and delivered from Cloudflare Images.</p>
<h2 id="enable">Enable</h2>
<p>Content Credentials preservation is an account-wide setting that applies to every image delivered from <code>imagedelivery.net</code> (and any custom domains configured for your Images account).</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Delivery</strong> tab.</p>
</li>
<li>
<p>Enable <strong>Preserve Content Credentials</strong>.</p>
</li>
</ol>
<p>You can also enable it via the API by making a <code>PATCH</code> request to the <a href="/api/resources/images/subresources/v1/subresources/variants/methods/edit/">images config endpoint</a>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;preserve_content_credentials&quot;: true}&#x27;&#10;</code></pre>
<p>The behavior of this setting is determined by the <a href="/images/optimization/features/#metadata"><code>metadata</code></a> parameter applied to each delivered image or variant.</p>
<p>For example, if a variant specifies <code>metadata=copyright</code> (the default), then the EXIF copyright tag and all Content Credentials will be preserved in the resulting image and all other metadata will be discarded.</p>
<p>When Content Credentials are preserved during delivery, Cloudflare will keep any existing Content Credentials embedded in the source image and automatically append and cryptographically sign additional actions describing the transformations it applied (such as resizing or format conversion).</p>
