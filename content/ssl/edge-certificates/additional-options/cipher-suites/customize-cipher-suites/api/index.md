---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/
  description: Select allowed cipher suites for your zone using the API.
  full_title: Customize cipher suites via API · Cloudflare SSL/TLS docs
  head_html: <title>Customize cipher suites via API · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Select allowed cipher suites for your zone using the API."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/index.md"><meta property="og:title" content="Customize cipher suites via API · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Select allowed cipher suites for your zone using the API."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#page","headline":"Customize cipher suites via API \u00b7 Cloudflare SSL/TLS docs","description":"Select allowed cipher suites for your zone using the API.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/
  schema: 1
---
<p>Cipher suites are a combination of ciphers used to negotiate security settings during the <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">SSL/TLS handshake</a> (and therefore separate from the <a href="/ssl/reference/protocols/">SSL/TLS protocol</a>).</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Cipher suite customization requires an <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> subscription.</p>
<p>If you are a SaaS provider looking to restrict cipher suites for connections to <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a>, this can be configured with a <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> subscription. Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/#cipher-suites">TLS management</a> instead.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Note that:</p>
<ul>
<li>Updating the cipher suites will result in certificates being redeployed.</li>
<li>Cipher suites are used in combination with other <a href="/ssl/edge-certificates/additional-options/cipher-suites/#related-ssltls-settings">SSL/TLS settings</a>.</li>
<li>You cannot set specific TLS 1.3 ciphers. Instead, you can <a href="/ssl/edge-certificates/additional-options/tls-13/#enable-tls-13">enable TLS 1.3</a> for your entire zone and Cloudflare will use all applicable <a href="/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/">TLS 1.3 cipher suites</a>.</li>
<li>Each cipher suite also supports a specific algorithm (RSA or ECDSA) so you should consider the algorithms in use by your edge certificates when making your ciphers selection. You can find this information under each certificate listed on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page.</li>
<li>It is not possible to configure minimum TLS version nor cipher suites for <a href="/pages/">Cloudflare Pages</a> hostnames.</li>
<li>If you use Windows you might need to adjust the <code>curl</code> syntax, refer to <a href="/fundamentals/api/how-to/make-api-calls/#making-api-calls-on-windows">Making API calls on Windows</a> for further guidance.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14176.md")
</aside>
<h2 id="steps-and-api-examples">Steps and API examples</h2>
<ol>
<li>
<p>Decide which cipher suites you want to specify and which ones you want to disable (meaning they will not be included in your selection).</p>
<p>Below you will find samples covering the recommended ciphers <a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/">by security level</a> and <a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/">compliance standards</a>, but you can also refer to the <a href="/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/">full list</a> of supported ciphers and customize your choice.</p>
</li>
<li>
<p>Log in to the Cloudflare dashboard and get your Global API Key in <a href="https://dash.cloudflare.com/?to=/:account/profile/api-tokens/"><strong>My Profile</strong> &gt; <strong>API Tokens</strong></a>.</p>
</li>
<li>
<p>Get the Zone ID from the <a href="https://dash.cloudflare.com/?to=/:account/:zone/">Overview page</a> of the domain you want to specify cipher suites for.</p>
</li>
<li>
<p>Make an API call to either the <a href="/api/resources/zones/subresources/settings/methods/edit/">Edit zone setting</a> endpoint or the <a href="/api/resources/hostnames/subresources/settings/subresources/tls/methods/update/">Edit TLS setting for hostname</a> endpoint, specifying <code>ciphers</code> in the URL. List your array of chosen cipher suites in the <code>value</code> field.</p>
</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14181.md")
</div></div>
<h3 id="reset-to-default-values">Reset to default values</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14184.md")
</div></div>
<p>For guidance around custom hostnames, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/#cipher-suites">TLS settings - Cloudflare for SaaS</a>.</p>
