---
cp9:
  canonical: https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/
  description: Configure your Cloudflare zone for PCI DSS compliance — set minimum TLS version, configure approved cipher suites, and understand how Cloudflare interacts with PCI ASV scans.
  full_title: PCI DSS compliance · Cloudflare SSL/TLS docs
  head_html: <title>PCI DSS compliance · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure your Cloudflare zone for PCI DSS compliance — set minimum TLS version, configure approved cipher suites, and understand how Cloudflare interacts with PCI ASV scans."><link rel="canonical" href="https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/index.md"><meta property="og:title" content="PCI DSS compliance · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure your Cloudflare zone for PCI DSS compliance — set minimum TLS version, configure approved cipher suites, and understand how Cloudflare interacts with PCI ASV scans."><meta property="og:url" content="https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS,Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/#page","headline":"PCI DSS compliance \u00b7 Cloudflare SSL/TLS docs","description":"Configure your Cloudflare zone for PCI DSS compliance \u2014 set minimum TLS version, configure approved cipher suites, and understand how Cloudflare interacts with PCI ASV scans.","url":"https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS","Compliance"]}</script>
  markdown: true
  noindex: false
  route: /ssl/reference/compliance-and-vulnerabilities/
  schema: 1
---
<p>The Payment Card Industry Data Security Standard (PCI DSS) applies to any organization that stores, processes, or transmits payment card data. When your site or application runs behind Cloudflare, several PCI DSS requirements apply to how Cloudflare handles your traffic — and some require explicit configuration on your zone.</p>
<p>This guide walks through the Cloudflare configuration steps required for PCI DSS compliance, explains how Cloudflare interacts with PCI Approved Scanning Vendor (ASV) scans, and lists known scanner false positives.</p>
<h2 id="cloudflare-s-pci-dss-certification">Cloudflare's PCI DSS certification</h2>
<p>Cloudflare is certified as a <strong>Level 1 PCI DSS Service Provider</strong> — the highest certification level. You can obtain Cloudflare's current Attestation of Compliance (AOC) from the <a href="https://www.cloudflare.com/trust-hub/compliance-resources/pci-dss/">Cloudflare Trust Hub</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13967.md")
</aside>
<h2 id="shared-responsibility">Shared responsibility</h2>
<table>
<thead>
<tr>
<th>Area</th>
<th>Cloudflare</th>
<th>You</th>
</tr>
</thead>
<tbody>
<tr>
<td>TLS protocol support</td>
<td>Supports TLS 1.2 and 1.3 on all plans</td>
<td>Set minimum TLS version to 1.2 on your zone</td>
</tr>
<tr>
<td>Cipher suites</td>
<td>Offers PCI DSS-approved cipher suites</td>
<td>Enable the PCI DSS cipher suite profile on your zone. Configuring cipher suites requires an <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> subscription.</td>
</tr>
<tr>
<td>Vulnerability patching</td>
<td>Patches Cloudflare infrastructure (ROBOT, Sweet32, and others)</td>
<td>Keep your origin server and any third-party software patched</td>
</tr>
<tr>
<td>Client-side scripts</td>
<td>Client-Side Security Advanced inventories and monitors payment page scripts</td>
<td>Enable and configure Client-Side Security</td>
</tr>
</tbody>
</table>
<h2 id="configure-tls-settings">Configure TLS settings</h2>
<p>Steps 1 and 2 are required for PCI DSS compliance. Step 3 is Cloudflare's recommendation for a stronger configuration but is not mandated by PCI DSS v4.0, which sets TLS 1.2 as the minimum. A PCI scan checks each layer independently — completing only Steps 1 and 2 is sufficient to meet the standard.</p>
<h3 id="step-1-set-minimum-tls-version-to-1-2">Step 1: Set minimum TLS version to 1.2</h3>
<p>PCI DSS requirement 4.2.1 mandates strong cryptography for cardholder data in transit, with TLS 1.2 as the minimum acceptable version. TLS 1.0 and TLS 1.1 are not considered strong cryptography under PCI DSS.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>SSL/TLS</strong> &gt; <strong>Edge Certificates</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>For <strong>Minimum TLS Version</strong>, select <strong>TLS 1.2</strong> or higher.</li>
</ol>
<p>Refer to <a href="/ssl/edge-certificates/additional-options/minimum-tls/">Minimum TLS Version</a> for API and Terraform options.</p>
<h3 id="step-2-configure-pci-dss-cipher-suites">Step 2: Configure PCI DSS cipher suites</h3>
<p>PCI DSS prohibits weak and deprecated cipher algorithms. You must restrict your zone to the PCI DSS-approved cipher list.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisite">Prerequisite</h3>
@markup("md", "content/.markup/bodies/13966.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13965.md")
</aside>
<p>Follow the steps in <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/">Customize cipher suites (dashboard)</a> and select the cipher suites from the PCI DSS profile listed in <a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/#pci-dss">Compliance standards</a>. Alternatively, use the API:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/{setting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;value&quot;: [&#10;    &quot;ECDHE-ECDSA-AES128-GCM-SHA256&quot;,&#10;    &quot;ECDHE-RSA-AES128-GCM-SHA256&quot;,&#10;    &quot;ECDHE-ECDSA-AES256-GCM-SHA384&quot;,&#10;    &quot;ECDHE-RSA-AES256-GCM-SHA384&quot;,&#10;    &quot;ECDHE-ECDSA-CHACHA20-POLY1305&quot;,&#10;    &quot;ECDHE-RSA-CHACHA20-POLY1305&quot;&#10;  ]&#10;}&#x27;</code></pre>
<h3 id="step-3-enable-tls-1-3-recommended">Step 3: Enable TLS 1.3 (recommended)</h3>
<p>TLS 1.3 provides stronger security guarantees than TLS 1.2, eliminates several legacy handshake patterns, and is recommended alongside TLS 1.2 for a stronger, future-proof configuration. It is not required for PCI DSS compliance, which mandates TLS 1.2 as the minimum.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>SSL/TLS</strong> &gt; <strong>Edge Certificates</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enable <strong>TLS 1.3</strong>.</li>
</ol>
<p>Refer to <a href="/ssl/edge-certificates/additional-options/tls-13/">TLS 1.3</a> for API and Terraform options.</p>
<h2 id="verify-your-configuration">Verify your configuration</h2>
<p>After applying all settings, confirm that non-compliant connections are rejected.</p>
<h3 id="use-an-online-tls-scanner">Use an online TLS scanner</h3>
<p>Online TLS scanners give you an external view of your configuration — the same perspective a PCI ASV scan sees. Two commonly used options are:</p>
<ul>
<li><a href="https://www.ssllabs.com/ssltest/">SSL Labs Server Test</a> — enter your domain and review the report. Check that TLS 1.0 and TLS 1.1 are rejected, TLS 1.2 or higher is supported, and no weak or deprecated cipher suites are negotiated.</li>
<li><a href="https://www.sslshopper.com/ssl-checker.html">SSL Shopper SSL Checker</a> — validates your certificate chain and TLS configuration from an external vantage point.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13964.md")
</aside>
<h3 id="use-openssl">Use openssl</h3>
<p><code>openssl s_client</code> lets you test specific TLS versions from the command line. Connections using TLS 1.0 or TLS 1.1 should fail:</p>
<pre tabindex="0"><code class="language-sh">&#35; Should fail — TLS 1.0 rejected&#10;openssl s_client -connect example.com:443 -tls1&#10;&#10;&#35; Should fail — TLS 1.1 rejected&#10;openssl s_client -connect example.com:443 -tls1_1&#10;</code></pre>
<p>A rejected connection returns an error such as:</p>
<pre tabindex="0"><code class="language-sh">4087F5C1E27F0000:error:0A00042E:SSL routines:ssl3_read_bytes:tlsv1 alert protocol version&#10;</code></pre>
<p>To confirm which cipher suite is negotiated over TLS 1.2:</p>
<pre tabindex="0"><code class="language-sh">openssl s_client -connect example.com:443 -tls1_2 2&gt;/dev/null | grep -E &quot;Protocol|Cipher&quot;&#10;</code></pre>
<p>The output should show a cipher from the PCI DSS-approved list — for example <code>ECDHE-RSA-AES128-GCM-SHA256</code>.</p>
<h3 id="use-curl">Use curl</h3>
<p>To confirm TLS 1.0 and TLS 1.1 are rejected:</p>
<pre tabindex="0"><code class="language-sh">&#35; Should fail — TLS 1.0 rejected&#10;curl https://example.com --tls-max 1.0 -svo /dev/null&#10;&#10;&#35; Should fail — TLS 1.1 rejected&#10;curl https://example.com --tls-max 1.1 -svo /dev/null&#10;</code></pre>
<p>A rejected connection returns an error such as:</p>
<pre tabindex="0"><code class="language-sh">&#42; error:1400442E:SSL routines:CONNECT_CR_SRVR_HELLO:tlsv1 alert&#10;</code></pre>
<h3 id="check-from-the-dashboard">Check from the dashboard</h3>
<p>On the <strong>Edge Certificates</strong> page, select <strong>View current ciphers</strong> to see the cipher suites configured on your zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13963.md")
</aside>
<h2 id="cloudflare-pages">Cloudflare Pages</h2>
<p>It is not possible to configure minimum TLS version or cipher suites for <code>*.pages.dev</code> hostnames. These settings only apply to zones you control in the Cloudflare dashboard.</p>
<p>For payment pages hosted on a Pages project, use a <a href="/pages/configuration/custom-domains/">custom domain</a> attached to a zone you control. Zone-level TLS and cipher suite settings apply to traffic served through that custom domain.</p>
<h2 id="pci-dss-v4-client-side-requirements">PCI DSS v4 client-side requirements</h2>
<p>PCI DSS v4.0 introduced two requirements for scripts running in the consumer's browser on payment pages:</p>
<table>
<thead>
<tr>
<th>Requirement</th>
<th>Description</th>
<th>Cloudflare feature</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>6.4.3</strong></td>
<td>Maintain an inventory of all scripts on payment pages, with authorization and integrity checks</td>
<td>Page Shield</td>
</tr>
<tr>
<td><strong>11.6.1</strong></td>
<td>Detect and alert on unauthorized changes to HTTP security headers and payment page content</td>
<td>Page Shield</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/client-side-security/reference/pci-dss/">Client-side security and PCI DSS compliance</a> for setup guidance.</p>
<h2 id="pci-asv-scans">PCI ASV scans</h2>
<p>PCI DSS requires quarterly vulnerability scans by an Approved Scanning Vendor (ASV). When your domain is proxied through Cloudflare, ASV scanners interact with Cloudflare's edge network rather than your origin server directly. Several behaviors commonly arise.</p>
<h3 id="tcp-source-port-behavior">TCP source port behavior</h3>
<p>Some ASV tools report a <strong>TCP Source Port Pass Firewall</strong> finding against Cloudflare-proxied IP addresses. This is a false positive caused by how Cloudflare's anycast network handles TCP connections — the behavior is a property of Cloudflare's infrastructure, not a vulnerability in your environment.</p>
<p>If your QSA or scanning tool flags this finding, provide:</p>
<ul>
<li>Cloudflare's current <a href="https://www.cloudflare.com/trust-hub/compliance-resources/pci-dss/">Attestation of Compliance (AOC)</a></li>
<li>Documentation that your domain is proxied through Cloudflare as a PCI DSS Level 1 Service Provider</li>
</ul>
<p>Your QSA can treat this as a compensating control or documented exception based on Cloudflare's shared responsibility boundary.</p>
<h3 id="waf-and-ddos-blocking-asv-scanners">WAF and DDoS blocking ASV scanners</h3>
<p>ASV scanners send attack-pattern traffic — SQL injection probes, XSS payloads, vulnerability fingerprinting — to test your application. Cloudflare's WAF blocks many of these probes, which is correct WAF behavior, but it can prevent the scanner from completing its assessment.</p>
<p>To allow a scan without disabling your WAF:</p>
<ol>
<li>Obtain the source IP ranges used by your ASV vendor.</li>
<li>Create a <a href="/waf/custom-rules/">WAF custom rule</a> that skips managed ruleset matching for those IP ranges, scoped to your scan maintenance window.</li>
<li>Remove or disable the rule immediately after the scan completes.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13962.md")
</aside>
<h3 id="non-standard-ports">Non-standard ports</h3>
<p>Cloudflare proxies a <a href="/fundamentals/reference/network-ports/">defined set of HTTP and HTTPS ports</a>. For ports outside that list, Cloudflare's anycast network may cause those ports to appear open at the TCP layer even though they are not proxied — the TCP connection is accepted at the edge but HTTP/HTTPS requests are blocked at the application layer before reaching your origin.</p>
<p>If an ASV scan targets non-proxied ports, findings for those ports reflect Cloudflare's edge behavior rather than your origin. Configure your scan to target the ports your application actually serves on, and provide your QSA with the <a href="/fundamentals/reference/network-ports/">network ports reference</a> to document the expected behavior.</p>
<h2 id="vulnerability-mitigations">Vulnerability mitigations</h2>
<p>Cloudflare applies these mitigations by default across all proxied zones. No configuration is needed.</p>
<p>Cloudflare does not support:</p>
<ul>
<li>Header compression in TLS</li>
<li>Header compression in SPDY 3.1</li>
<li>RC4</li>
<li>SSL 3.0</li>
<li>Renegotiation with clients</li>
<li>DHE cipher suites</li>
<li>Export-grade ciphers</li>
</ul>
<p>Cloudflare mitigates:</p>
<ul>
<li>CRIME</li>
<li>BREACH</li>
<li>POODLE</li>
<li>RC4 cryptographic weaknesses</li>
<li>SSL renegotiation attacks</li>
<li>Protocol downgrade attacks</li>
<li>FREAK</li>
<li>LogJam</li>
<li>Sweet32 — 3DES is disabled for TLS 1.1 and 1.2. For TLS 1.0, Cloudflare rotates session keys before the 32 GB threshold required for a successful attack</li>
</ul>
<p>All Cloudflare servers are patched against Heartbleed, Lucky Thirteen, and CCS injection vulnerability.</p>
<h2 id="common-scanner-false-positives">Common scanner false positives</h2>
<h3 id="robot">ROBOT</h3>
<p>Security scans that report <strong>Return of Bleichenbacher's Oracle Threat (ROBOT)</strong> against a Cloudflare-proxied domain are false positives. Cloudflare validates RSA PKCS#1 v1.5 padding in real time and substitutes a random session key if padding is incorrect, eliminating any exploitable oracle.</p>
<h3 id="sweet32-cve-2016-2183">Sweet32 (CVE-2016-2183)</h3>
<p>If a scanner flags Sweet32, verify that TLS 1.0 is disabled on your zone. Refer to <a href="#step-1-set-minimum-tls-version-to-12">Set minimum TLS version to 1.2</a> for steps. With TLS 1.0 disabled, the 3DES cipher suites where Sweet32 applies are not in use and the finding does not apply to your environment.</p>
<h3 id="cfuvid-cookie-missing-secure-flag"><code>_cfuvid</code> cookie missing Secure flag</h3>
<p>Cloudflare sets the <code>_cfuvid</code> cookie on some zones for rate limiting. Some scanners may report this cookie as missing the <code>Secure</code> attribute if they scan over HTTP. If your ASV raises this finding, confirm that your ASV is scanning HTTPS endpoints and that your zone redirects HTTP traffic to HTTPS. Refer to <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> for setup steps.</p>
