---
cp9:
  canonical: https://developers.cloudflare.com/ssl/reference/protocols/
  description: Explore Cloudflare's support for TLS protocols from 1.0 to 1.3. Learn about differences, security standards, and recommendations on what version to use.
  full_title: TLS protocols · Cloudflare SSL/TLS docs
  head_html: <title>TLS protocols · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore Cloudflare&#x27;s support for TLS protocols from 1.0 to 1.3. Learn about differences, security standards, and recommendations on what version to use."><link rel="canonical" href="https://developers.cloudflare.com/ssl/reference/protocols/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/reference/protocols/index.md"><meta property="og:title" content="TLS protocols · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore Cloudflare&#x27;s support for TLS protocols from 1.0 to 1.3. Learn about differences, security standards, and recommendations on what version to use."><meta property="og:url" content="https://developers.cloudflare.com/ssl/reference/protocols/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/reference/protocols/#page","headline":"TLS protocols \u00b7 Cloudflare SSL/TLS docs","description":"Explore Cloudflare's support for TLS protocols from 1.0 to 1.3. Learn about differences, security standards, and recommendations on what version to use.","url":"https://developers.cloudflare.com/ssl/reference/protocols/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/reference/protocols/
  schema: 1
---
<p>Cloudflare supports the following TLS protocols:</p>
<ul>
<li>TLS 1.0</li>
<li>TLS 1.1</li>
<li>TLS 1.2</li>
<li>TLS 1.3</li>
</ul>
<p>TLS 1.0 is the <a href="/ssl/edge-certificates/additional-options/minimum-tls/">version that Cloudflare sets by default</a> for all customers using certificate-based encryption.</p>
<p>For information about which cipher suites are supported between clients and the Cloudflare network, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/">Cipher suites</a>.</p>
<h2 id="understand-tls-versions">Understand TLS versions</h2>
<p>A higher TLS version implies a stronger cryptographic standard. TLS 1.2 includes fixes for known vulnerabilities found in previous versions.</p>
<p>As of June 2018, TLS 1.2 is the version required by the Payment Card Industry (PCI) Security Standards Council. Cloudflare recommends migrating to TLS 1.2 to comply with the PCI requirement.</p>
<p><a href="/ssl/edge-certificates/additional-options/tls-13/">TLS 1.3</a>, which offers additional security and performance improvements, was approved by the Internet Engineering Task Force (IETF) in May 2018.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="paypal-s-tls-1-2-requirement">PayPal's TLS 1.2 requirement</h3>
@markup("md", "content/.markup/bodies/13961.md")
</aside>
<h2 id="decide-which-version-to-use">Decide which version to use</h2>
<p>TLS 1.3 has become widely adopted. As a general rule, Cloudflare recommends setting TLS to 1.3, as it will provide the best security.</p>
<p>However, not all browser versions support TLS 1.2 and above. Depending on your particular business situation, this may present some limitations in using stronger encryption standards:</p>
<ul>
<li>
<p>Consider using TLS 1.0 or 1.1 for sites with a broad user base, particularly non-transactional sites. In this way, you minimize the possibility that some clients cannot connect to your site securely.</p>
</li>
<li>
<p>For a narrow user base and sites that run internal applications or business and productivity applications, Cloudflare recommends TLS 1.2. These sites might already have more stringent security requirements or might be subject to <a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/">PCI compliance</a>. You also need to ensure that your users upgrade to a TLS 1.2 compliant browser.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ssl/reference/compliance-and-vulnerabilities/">PCI compliance and vulnerabilities mitigation</a></li>
<li><a href="https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/">Transport Layer Security</a></li>
<li><a href="https://www.pcisecuritystandards.org/">PCI Security Standards Council</a></li>
</ul>
