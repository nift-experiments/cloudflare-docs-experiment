---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshoot-gateway/
  description: Troubleshoot Troubleshoot Gateway issues in Gateway.
  full_title: Troubleshoot Gateway · Cloudflare One docs
  head_html: <title>Troubleshoot Gateway · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Troubleshoot Gateway issues in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshoot-gateway/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshoot-gateway/index.md"><meta property="og:title" content="Troubleshoot Gateway · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Troubleshoot Gateway issues in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshoot-gateway/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS,DNS,Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshoot-gateway/#page","headline":"Troubleshoot Gateway \u00b7 Cloudflare One docs","description":"Troubleshoot Troubleshoot Gateway issues in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshoot-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS","DNS","Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/troubleshoot-gateway/
  schema: 1
---
<p>This guide helps you troubleshoot common issues with Cloudflare Gateway policies. The issues are ordered by the most frequent problems.</p>
<h2 id="egress-policies-do-not-work-as-expected">Egress policies do not work as expected</h2>
<p>Egress policies are the most common category of issues for Gateway. Symptoms include traffic not using your dedicated egress IP, incorrect failover behavior, or high latency due to Gateway routing traffic through a distant data center.</p>
<h3 id="symptom-traffic-is-not-using-your-dedicated-egress-ip">Symptom: traffic is not using your dedicated egress IP</h3>
<p>Even with an active egress policy, you may find that traffic is egressing from a default Cloudflare IP address instead of your dedicated egress IP.</p>
<table>
<thead>
<tr>
<th>Common cause</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS resolution to an initial resolved IP</td>
<td>When an egress policy uses a <em>Domain</em> or <em>Host</em> selector, Gateway must first resolve that domain to an <a href="/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips">initial resolved IP</a>. If your account still uses a legacy range within CGNAT (carrier-grade NAT) address space, this IP may be treated as internal to Cloudflare's network and may not be subject to egress policies, which apply to traffic leaving the network. Change the selector in your egress policy from <em>Domain</em> or <em>Host</em> to <em>Destination IP</em> (using the public IP addresses of the service you are trying to reach), or <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">move your initial resolved IP range off CGNAT</a>.</td>
</tr>
<tr>
<td>Policy precedence</td>
<td>A different egress policy with a higher precedence (a lower number) is matching the traffic first. Remember that egress policies follow the same first-match-wins logic.</td>
</tr>
<tr>
<td>Split Tunnel configuration</td>
<td>The destination IP or domain is excluded from the WARP tunnel via your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> configuration (which controls whether traffic for specific IPs or domains is sent through or excluded from the WARP tunnel). Traffic that is excluded from the tunnel will not be subject to any Gateway policies, including egress.</td>
</tr>
<tr>
<td>No egress logs</td>
<td>Egress logging is available via Logpush with the Gateway Egress dataset. This is essential for troubleshooting. You can also use a third-party IP check service to verify the egress IP from a test device.</td>
</tr>
</tbody>
</table>
<h3 id="symptom-failover-is-not-working-or-is-using-the-wrong-ip">Symptom: failover is not working or is using the wrong IP</h3>
<p>Your primary dedicated egress IP becomes unavailable, but instead of using your configured secondary dedicated IP, traffic fails over to a default Cloudflare shared IP.</p>
<table>
<thead>
<tr>
<th>Common cause</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Routing or configuration issue on the Cloudflare side</td>
<td>Document the time of the incident and collect Request IDs from Gateway HTTP or DNS logs for affected users. Open a support ticket and provide this information. Temporarily, you can edit the egress policy to set your secondary IP as the primary to restore service.</td>
</tr>
</tbody>
</table>
<h3 id="symptom-users-are-egressing-from-a-geographically-distant-location">Symptom: users are egressing from a geographically distant location</h3>
<p>Gateway routes your users in one country (such as Australia) through a dedicated egress IP located in another region (such as Germany), causing high latency and breaking access to geo-restricted content.</p>
<p>Common causes and solutions:</p>
<table>
<thead>
<tr>
<th>Common cause</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single egress policy</td>
<td>You may have one broad egress policy that applies to all users regardless of their location. Create location-aware egress policies. Use the <em>User Location</em> selector in your policy to tie specific user locations to their nearest dedicated egress IP. For example, create one policy for when <em>User Location</em> is <code>United Kingdom</code>, egress via London IP; create a second policy for when <em>User Location</em> is <code>Australia</code>, egress via Sydney IP.</td>
</tr>
<tr>
<td>Incorrect geolocation data</td>
<td>The IP address of the user's ISP may not be correctly geolocated. Check the user's location as seen by Cloudflare in the Gateway logs. If it appears incorrect, you can report it to Cloudflare Support.</td>
</tr>
</tbody>
</table>
<h2 id="gateway-does-not-apply-policies-in-the-correct-order">Gateway does not apply policies in the correct order</h2>
<p>A common point of confusion is how Gateway evaluates its different policy types and the rules within them.</p>
<h3 id="symptom-a-block-policy-is-overriding-a-more-specific-allow-or-do-not-scan-policy">Symptom: a Block policy is overriding a more specific Allow or Do Not Scan policy</h3>
<p>You have a high-precedence Allow or Do Not Scan policy for a specific application (such as Allow finance.example.com), but Gateway still block traffic with a low-precedence Block policy (such as Block All High-Risk Sites).</p>
<p>The most important concept is <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Gateway policy precedence</a>, which Gateway enforces based on the policy's order number. A lower order number in the list means a higher precedence. Gateway stops processing further policies when it encounters the first rule that matches.</p>
<p>To resolve Gateway policy precedence issues:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Review the order of your DNS, Network, and HTTP policies.</li>
<li>Ensure that your most specific Allow, Do Not Scan, or Do Not Inspect policies have a lower order number than your general Block policies.</li>
<li>Drag and drop policies to reorder them as needed. An Allow policy for <code>teams.microsoft.com</code> should be placed before a general Block policy for all file sharing applications.</li>
</ol>
<h2 id="tls-decryption-breaks-applications">TLS decryption breaks applications</h2>
<p>Turning on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> is required for Gateway features such as Data Loss Prevention (DLP), Browser Isolation, and application-aware HTTP policies. However, it can cause issues with certain types of software.</p>
<h3 id="symptom-command-line-tools-cli-tools-or-native-applications-fail-with-certificate-errors">Symptom: command-line tools (CLI tools) or native applications fail with certificate errors</h3>
<p>If after turning on TLS decryption, command-line tools (such as <code>git</code>, <code>aws</code>, <code>kubectl</code>, and <code>terraform</code>) or desktop applications (such as ChatGPT or Docker) stop working, this may be due to certificate errors. Applications may return errors such as <code>SSL: CERTIFICATE_VERIFY_FAILED</code>, <code>self-signed certificate in certificate chain</code>, or similar TLS errors.</p>
<p>These applications do not use the operating system's trust store and therefore do not trust the Cloudflare root certificate that you installed. They often have their own certificate trust store or use certificate pinning, which expects the server's original certificate, not one re-signed by Cloudflare.</p>
<p>To resolve this issue:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4381.md")
</div></div>
<h3 id="symptom-the-custom-block-page-is-not-displayed">Symptom: the custom block page is not displayed</h3>
<p>When an HTTP policy blocks a user's request, their browser will return a generic error (<code>ERR_SSL_PROTOCOL_ERROR</code>) instead of your configured Gateway block page.</p>
<p>This happens because the browser does not trust the certificate presented by the block page, which is signed by the Cloudflare root certificate. This means the certificate is not installed or not trusted on the user's device.</p>
<p>To resolve this issue:</p>
<ol>
<li>Confirm that a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Cloudflare root certificate</a> is installed on the device.</li>
<li>Ensure the certificate is placed in the correct system-level trust store (such as, Keychain's System store on macOS, or Trusted Root Certification Authorities for the Local Computer on Windows).</li>
<li>If you are using a mobile device management (MDM) tool, verify that your deployment script correctly installs and trusts the certificate.</li>
</ol>
<h2 id="private-dns-and-internal-resources-are-not-working">Private DNS and internal resources are not working</h2>
<p>You have configured Gateway to resolve internal hostnames, but users are unable to access them. For example, a user connected to the Cloudflare One Client tries to access an internal service like <code>jira.mycompany.local</code>, but the DNS query fails.</p>
<table>
<thead>
<tr>
<th>Common causes</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Missing or incorrect resolver policy</td>
<td>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>. Create a policy that matches your internal domain suffix and forwards queries to your internal DNS servers' IP addresses.</td>
</tr>
<tr>
<td>Split Tunnel excludes the private IP range</td>
<td>If your internal resources are in a private IP range (such as <code>10.0.0.0/8</code>), that range must be included in the tunnel. If it is in the Exclude list of your Split Tunnel configuration, the Cloudflare One Client will not proxy the traffic.</td>
</tr>
<tr>
<td>Local Domain Fallback misconfiguration</td>
<td>Use resolver policies for corporate DNS. Only use Local Domain Fallback for domains specific to a user's immediate physical network.</td>
</tr>
</tbody>
</table>
