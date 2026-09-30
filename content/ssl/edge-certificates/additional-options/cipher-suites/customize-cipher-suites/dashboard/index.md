---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/
  description: Select allowed cipher suites for your zone in the dashboard.
  full_title: Customize cipher suites via dashboard · Cloudflare SSL/TLS docs
  head_html: <title>Customize cipher suites via dashboard · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Select allowed cipher suites for your zone in the dashboard."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/index.md"><meta property="og:title" content="Customize cipher suites via dashboard · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Select allowed cipher suites for your zone in the dashboard."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/#page","headline":"Customize cipher suites via dashboard \u00b7 Cloudflare SSL/TLS docs","description":"Select allowed cipher suites for your zone in the dashboard.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/
  schema: 1
---
<p>Cipher suites are a combination of ciphers used to negotiate security settings during the <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">SSL/TLS handshake</a> (and therefore separate from the <a href="/ssl/reference/protocols/">SSL/TLS protocol</a>).</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Cipher suite customization requires an <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> subscription.</p>
<p>If you are a SaaS provider looking to restrict cipher suites for connections to <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a>, this can be configured with a <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> subscription. Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/#cipher-suites">TLS management</a> instead.</p>
<h2 id="selection-modes">Selection modes</h2>
<p>When configuring cipher suites via dashboard, you can use three different selection modes:</p>
<ul>
<li><strong>By security level</strong>: allows you to select between the predefined <a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/">Cloudflare recommendations</a> (Modern<sup><a href="#footnote-1">1</a></sup>, Compatible, or Legacy).</li>
<li><strong>By compliance standard</strong>: allows you to select cipher suites grouped according to <a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/">industry standards</a> (PCI DSS or FIPS-140-3).</li>
<li><strong>Custom</strong>: allows you to individually select the cipher suites you would like to support.</li>
</ul>
<p>For any of the modes, you should keep in mind the following configuration conditions. If using the <strong>security level</strong> or the <strong>compliance standard</strong> mode, some actions may be blocked and explained referencing these conditions.</p>
<details class="nb-details"><summary>Configuration conditions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14174.md")
</div></details>
<h2 id="steps">Steps</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>For the <strong>Cipher suites</strong> setting select <strong>Configure</strong>.</li>
<li>Choose a mode to select your cipher suites and select <strong>Next</strong>.</li>
<li>Select a predefined set of cipher suites or, if you opted for <strong>Custom</strong>, specify which cipher suites you want to allow. Make sure you are aware of how your selection will interact with Minimum TLS version, TLS 1.3, and the certificate algorithm (ECDSA or RSA).</li>
<li>Select <strong>Save</strong> to confirm.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="modern-or-pci-dss">Modern or PCI DSS</h3>
@markup("md", "content/.markup/bodies/14173.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">When used with TLS 1.3, Modern is the same as PCI DSS.</li></ol></section>
