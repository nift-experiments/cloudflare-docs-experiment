---
cp9:
  canonical: https://developers.cloudflare.com/ssl/troubleshooting/err-ssl-protocol-error/
  description: Learn how to troubleshoot ERR_SSL_PROTOCOL_ERROR and similar SSL/TLS protocol errors when using Cloudflare.
  full_title: Troubleshoot ERR_SSL_PROTOCOL_ERROR · Cloudflare SSL/TLS docs
  head_html: <title>Troubleshoot ERR_SSL_PROTOCOL_ERROR · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to troubleshoot ERR_SSL_PROTOCOL_ERROR and similar SSL/TLS protocol errors when using Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/ssl/troubleshooting/err-ssl-protocol-error/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/troubleshooting/err-ssl-protocol-error/index.md"><meta property="og:title" content="Troubleshoot ERR_SSL_PROTOCOL_ERROR · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to troubleshoot ERR_SSL_PROTOCOL_ERROR and similar SSL/TLS protocol errors when using Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/ssl/troubleshooting/err-ssl-protocol-error/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/troubleshooting/err-ssl-protocol-error/#page","headline":"Troubleshoot ERR_SSL_PROTOCOL_ERROR \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to troubleshoot ERRSSLPROTOCOLERROR and similar SSL/TLS protocol errors when using Cloudflare.","url":"https://developers.cloudflare.com/ssl/troubleshooting/err-ssl-protocol-error/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/troubleshooting/err-ssl-protocol-error/
  schema: 1
---
<p>If visitors to your site experience SSL protocol errors such as:</p>
<ul>
<li><code>ERR_SSL_PROTOCOL_ERROR</code> (Chrome)</li>
<li><code>Secure Connection Failed</code> or <code>PR_END_OF_FILE_ERROR</code> (Firefox)</li>
<li><code>Safari can't open the page because it couldn't establish a secure connection to the server</code> (Safari)</li>
</ul>
<p>These errors indicate that the SSL/TLS handshake failed. This can happen for many reasons, including certificate issues, protocol incompatibilities, or network interference.</p>
<h2 id="rule-out-common-causes-first">Rule out common causes first</h2>
<p>Before investigating protocol-specific issues, verify that the error is not caused by:</p>
<ul>
<li><strong>Certificate not yet active</strong> - If you recently added your domain, wait for your <a href="/ssl/edge-certificates/universal-ssl/troubleshooting/">Universal SSL certificate to activate</a>.</li>
<li><strong>Multi-level subdomain not covered</strong> - Universal SSL only covers one level of subdomains. Refer to <a href="/ssl/troubleshooting/version-cipher-mismatch/#multi-level-subdomains">ERR_SSL_VERSION_OR_CIPHER_MISMATCH</a> for solutions.</li>
<li><strong>Cipher suite mismatch</strong> - Older clients may not support modern cipher suites. Refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/">cipher suites</a> for configuration options.</li>
</ul>
<hr />
<h2 id="test-http-3-quic-compatibility">Test HTTP/3 (QUIC) compatibility</h2>
<p>HTTP/3 uses the QUIC protocol over UDP, which some networks, firewalls, or devices do not fully support. If visitors experience intermittent SSL protocol errors, HTTP/3 may be the cause.</p>
<h3 id="when-to-suspect-http-3-issues">When to suspect HTTP/3 issues</h3>
<ul>
<li>Errors occur intermittently, not on every request</li>
<li>The issue affects only some visitors (often those on corporate networks or certain ISPs)</li>
<li>Visitors report the site works after refreshing multiple times</li>
<li>The issue does not occur when using a VPN</li>
</ul>
<h3 id="how-to-test">How to test</h3>
<p>Temporarily disable HTTP/3 to determine if it is the cause:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Protocol Optimization</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Turn off **HTTP/3 (with QUIC)**.
3. Ask the affected visitor to test again.
<p>If disabling HTTP/3 resolves the issue, the visitor's network likely blocks or mishandles UDP traffic on port 443. <strong>Re-enable HTTP/3 after testing</strong> and work with the visitor to identify the specific network issue.</p>
<hr />
<h2 id="test-tls-1-3-compatibility">Test TLS 1.3 compatibility</h2>
<p>TLS 1.3 is the latest version of the TLS protocol and provides improved security and performance. However, some network security devices that perform SSL/TLS inspection may not fully support TLS 1.3.</p>
<h3 id="when-to-suspect-tls-1-3-issues">When to suspect TLS 1.3 issues</h3>
<ul>
<li>Visitors using corporate networks with SSL inspection report connection issues</li>
<li>Antivirus software with HTTPS scanning is installed on the visitor's device</li>
<li>The error occurs consistently for specific visitors but not others</li>
</ul>
<h3 id="how-to-test-1">How to test</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13960.md")
</aside>
<p>Temporarily disable TLS 1.3 to determine if it is the cause:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Find **TLS 1.3** and turn it off.
3. Ask the affected visitor to test again.
<p>If disabling TLS 1.3 resolves the issue, the visitor's network has a middlebox (firewall, proxy, or antivirus) that does not support TLS 1.3. <strong>Re-enable TLS 1.3 after testing</strong> and ask the visitor to:</p>
<ul>
<li>Update their security software to a version that supports TLS 1.3</li>
<li>Contact their IT department to update network security devices</li>
<li>Temporarily disable HTTPS scanning in their antivirus software</li>
</ul>
<p>If you cannot identify the root cause, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> with packet captures from the affected visitor showing the failed TLS handshake.</p>
<hr />
<h2 id="isp-and-network-interference">ISP and network interference</h2>
<p>Some Internet Service Providers (ISPs) and corporate networks deploy security features that can interfere with HTTPS connections:</p>
<ul>
<li><strong>Deep packet inspection (DPI)</strong> - Inspects encrypted traffic and may interfere with connections it cannot analyze</li>
<li><strong>SSL/TLS interception proxies</strong> - Intercept and re-encrypt traffic, which can fail with newer protocols</li>
<li><strong>Parental controls or content filters</strong> - May block or interfere with connections to certain sites</li>
<li><strong>Carrier-grade NAT (CGNAT)</strong> - Can cause connection issues, especially with UDP-based protocols like QUIC</li>
</ul>
<h3 id="how-to-identify-network-interference">How to identify network interference</h3>
<p>Ask the affected visitor to:</p>
<ol>
<li><strong>Try a different network</strong> - Use mobile data instead of Wi-Fi, or try a different ISP</li>
<li><strong>Use a VPN</strong> - If the site works through a VPN, the ISP or local network is likely interfering</li>
<li><strong>Disable local security software</strong> - Temporarily disable antivirus or firewall software to test</li>
<li><strong>Check with their ISP</strong> - Some ISPs have security features that can be disabled upon request</li>
</ol>
<h3 id="if-network-interference-is-confirmed">If network interference is confirmed</h3>
<p>If the issue is caused by the visitor's ISP or network:</p>
<ul>
<li>The visitor may need to contact their ISP to add the domain to an allowlist or disable specific security features</li>
<li>For corporate networks, the IT department may need to update firewall or proxy rules</li>
<li>As a site owner, you have limited options since the interference occurs outside of Cloudflare</li>
</ul>
<hr />
<h2 id="collect-diagnostic-information">Collect diagnostic information</h2>
<p>If the above steps do not resolve the issue, collect the following information from affected visitors:</p>
<ol>
<li><strong>Cloudflare diagnostic data</strong> - Ask the visitor to access <code>https://your-domain.com/cdn-cgi/trace</code> and share the output</li>
<li><strong>Exact error message</strong> - The full error text and error code from the browser</li>
<li><strong>Browser and OS version</strong> - Including any security software installed</li>
<li><strong>Network information</strong> - Whether they are on a corporate network, using a VPN, or have any proxy configured</li>
</ol>
<p>Check <a href="https://www.cloudflarestatus.com/">Cloudflare Status</a> to verify there are no ongoing incidents affecting SSL/TLS.</p>
<p>If the issue persists and affects many visitors, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> with the diagnostic information collected.</p>
