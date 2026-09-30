---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/
  description: Resolve common cipher suite configuration issues.
  full_title: Troubleshooting - Cipher suites — Edge certificates · Cloudflare SSL/TLS docs
  head_html: <title>Troubleshooting - Cipher suites — Edge certificates · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common cipher suite configuration issues."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting - Cipher suites — Edge certificates · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common cipher suite configuration issues."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/#page","headline":"Troubleshooting - Cipher suites \u2014 Edge certificates \u00b7 Cloudflare SSL/TLS docs","description":"Resolve common cipher suite configuration issues.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/
  schema: 1
---
<p>If you encounter issues with edge certificate cipher suites, refer to the following scenarios.</p>
<h2 id="compatibility-with-minimum-tls-version">Compatibility with Minimum TLS Version</h2>
<p>When you adjust the setting used for your domain's <a href="/ssl/edge-certificates/additional-options/minimum-tls/">Minimum TLS Version</a>, your domain only allows HTTPS connections using that TLS protocol version. As explained in <a href="/ssl/edge-certificates/additional-options/cipher-suites/#related-ssltls-settings">About cipher suites</a>, although configured independently, cipher suites and TLS versions are closely related.</p>
<p>Minimum TLS Version can cause issues if you are not supporting TLS 1.2 ciphers on your domain. If you experience issues, review your domain's <a href="/ssl/edge-certificates/additional-options/minimum-tls/">Minimum TLS Version</a> setting and Cloudflare's <a href="/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/">supported ciphers list</a>.</p>
<h3 id="testing-minimum-tls-version-with-curl">Testing Minimum TLS version with curl</h3>
<p>To test supported TLS versions, attempt a request to your website or application while specifying a TLS version.</p>
<p>For example, to test TLS 1.1, use the <code>curl</code> command below. Replace <code>www.example.com</code> with your Cloudflare domain and hostname.</p>
<pre tabindex="0"><code class="language-sh">curl https://www.example.com -svo /dev/null --tls-max 1.1&#10;</code></pre>
<p>If the TLS version you are testing is blocked by Cloudflare, the TLS handshake is not completed and returns an error:</p>
<p><code>* error:1400442E:SSL routines:CONNECT_CR_SRVR_HELLO:tlsv1 alert</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14161.md")
</aside>
<h2 id="compatibility-with-certificate-encryption">Compatibility with certificate encryption</h2>
<p>If you <a href="/ssl/edge-certificates/custom-certificates/uploading/">upload a custom certificate</a>, make sure the certificate is compatible with the chosen cipher suites for your zone or hostname.</p>
<p>For example, if you upload an RSA certificate, your cipher suite selection cannot only support ECDSA certificates.</p>
<h2 id="compatibility-with-cloudflare-pages">Compatibility with Cloudflare Pages</h2>
<p>It is not possible to configure minimum TLS version nor cipher suites for <a href="/pages/">Cloudflare Pages</a> hostnames.</p>
<h2 id="api-requirements-for-custom-hostname-certificate">API requirements for custom hostname certificate</h2>
<p>When using the <a href="/api/resources/custom_hostnames/methods/edit/">Edit Custom Hostname endpoint</a>, make sure to include <code>type</code> and <code>method</code> within the <code>ssl</code> object, as well as the <code>settings</code> specifications.</p>
<p>Including the <code>settings</code> only will result in the error message <code>The SSL attribute is invalid. Please refer to the API documentation, check your input and try again</code>.</p>
<h2 id="tls-1-3-settings">TLS 1.3 settings</h2>
<div class="nb-data-component" data-cf-component="Render"></div>
<h2 id="ssl-labs-weak-ciphers-report">SSL Labs weak ciphers report</h2>
<p>If you try to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">disable</a> all of the <code>WEAK</code> cipher suites according to what is listed on a <a href="https://www.ssllabs.com/ssltest/">Qualys SSL Labs</a> report, you might notice that the naming conventions are not the same.</p>
<p>This is because SSL Labs follows RFC cipher naming convention while Cloudflare follows OpenSSL cipher naming convention. The cipher suite names list in the <a href="https://www.openssl.org/docs/man1.0.2/man1/ciphers.html">OpenSSL documentation</a> may help you map the names.</p>
<h2 id="warnings-related-to-cve-2019-1559">Warnings related to CVE-2019-1559</h2>
<p>Even though applications on Cloudflare are not vulnerable to <a href="/ssl/reference/cloudflare-and-cve-2019-1559/">CVE-2019-1559</a>, some security scanners may flag your application erroneously.</p>
<p>To remove these warnings, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">Customize cipher suites</a> and exclude the following ciphers:</p>
<ul>
<li><code>ECDHE-ECDSA-AES256-SHA384</code></li>
<li><code>ECDHE-ECDSA-AES128-SHA256</code></li>
<li><code>ECDHE-RSA-AES256-SHA384</code></li>
</ul>
