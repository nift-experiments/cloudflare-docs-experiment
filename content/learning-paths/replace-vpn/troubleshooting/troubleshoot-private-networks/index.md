---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/troubleshooting/troubleshoot-private-networks/
  description: Debug private network connectivity issues.
  full_title: Troubleshoot private networks · Cloudflare Learning Paths
  head_html: <title>Troubleshoot private networks · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Debug private network connectivity issues."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/troubleshooting/troubleshoot-private-networks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/troubleshooting/troubleshoot-private-networks/index.md"><meta property="og:title" content="Troubleshoot private networks · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Debug private network connectivity issues."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/troubleshooting/troubleshoot-private-networks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/troubleshooting/troubleshoot-private-networks/#page","headline":"Troubleshoot private networks \u00b7 Cloudflare Learning Paths","description":"Debug private network connectivity issues.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/troubleshooting/troubleshoot-private-networks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/troubleshooting/troubleshoot-private-networks/
  schema: 1
---
<p>Follow this troubleshooting procedure when end users running the Cloudflare One Client have issues connecting to a private network behind Cloudflare Tunnel.</p>
<h2 id="1-is-the-cloudflare-one-client-connected-to-a-cloudflare-data-center"><ol>
<li>Is the Cloudflare One Client connected to a Cloudflare data center?</li>
</ol></h2>
<p>The Cloudflare One Client GUI should display <code>Connected</code> and <code>Your Internet is protected</code>.</p>
<div class="medium-img">
<p><img src="/assets/upstream/images/cloudflare-one/connections/warp-connected.png" alt="Cloudflare One Client GUI when connected to Cloudflare" /></p>
</div>
<p>If the Cloudflare One Client is stuck in the <code>Disconnected</code> state or frequently changes between <code>Connected</code> and <code>Disconnected</code>, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#unable-to-connect-warp">Unable to connect WARP</a>.</p>
<h2 id="2-is-the-cloudflare-one-client-connecting-to-your-private-dns-server"><ol start="2">
<li>Is the Cloudflare One Client connecting to your private DNS server?</li>
</ol></h2>
<p>This step is only needed if users access your application via a private hostname (for example, <code>wiki.internal.local</code>).</p>
<ul>
<li>
<p>If you are using <a href="/cloudflare-one/traffic-policies/resolver-policies/">custom resolver policies</a> to handle private DNS, go to your Gateway DNS logs (<strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>DNS query logs</strong>) and search for DNS queries to the hostname.</p>
</li>
<li>
<p>If you are using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> to handle private DNS, go to your Gateway Network logs (<strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Network logs</strong>) and search for port <code>53</code> traffic to your DNS server IP.</p>
</li>
</ul>
<p>If there are no relevant Gateway logs, it means that WARP was unable to forward the query to your private DNS server. Check your resolver policies or Local Domain Fallback configuration and refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#how-the-warp-client-handles-dns-requests">How WARP handles DNS requests</a>.</p>
<h2 id="3-is-network-traffic-to-the-application-going-through-the-cloudflare-one-client"><ol start="3">
<li>Is network traffic to the application going through the Cloudflare One Client?</li>
</ol></h2>
<p>Next, check if your Gateway Network logs (<strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Network logs</strong>) show any traffic to the destination IP.</p>
<p>If the Cloudflare One Client is connected but there are no network logs, it means that your private network IPs are not routing through the Cloudflare One Client. You can confirm this by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#routing-table">searching the routing table</a> on the device for the IP address of your application. Traffic to your application should route through the Cloudflare One Client interface. If another interface is used, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#3-route-private-network-ips-through-the-cloudflare-one-client">check your Split Tunnel configuration</a>.</p>
<h2 id="4-is-the-user-blocked-by-a-gateway-policy"><ol start="4">
<li>Is the user blocked by a Gateway policy?</li>
</ol></h2>
<p>To check if a Gateway block event occurred:</p>
<ol>
<li>Go to <strong>Insights</strong> &gt; <strong>Logs</strong> and select the <strong>DNS query logs</strong>, <strong>Network logs</strong>, or <strong>HTTP request logs</strong>.</li>
<li>Apply the following filters:
<ul>
<li><strong>Email</strong>: User's email address</li>
<li><strong>Event</strong>: <em>Blocked</em></li>
<li><strong>Date Time Range</strong>: Time period when the user accessed the application</li>
</ul>
</li>
</ol>
<h2 id="5-is-the-user-matching-the-correct-gateway-policy"><ol start="5">
<li>Is the user matching the correct Gateway policy?</li>
</ol></h2>
<p>Determine whether the user is matching any policy, or if they are matching a policy that has a higher priority than the expected policy.</p>
<ol>
<li>To determine the actual policy that was applied:
<ol>
<li>Go to <strong>Insights</strong> &gt; <strong>Logs</strong> and select the <strong>DNS query logs</strong>, <strong>Network logs</strong>, or <strong>HTTP request logs</strong>.</li>
<li>Apply the following filters:
<ul>
<li><strong>Email</strong>: User's email address</li>
<li><strong>Date Time Range</strong>: Time period when the user accessed the application</li>
</ul>
</li>
<li>In the search box, filter by the destination IP or FQDN.</li>
<li>In the results, select a log and note its <strong>Policy Name</strong> value.</li>
</ol>
</li>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> and compare the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">order of enforcement</a> of the matched policy versus the expected policy.</li>
<li>Compare the Gateway log values with the expected policy criteria.
<ul>
<li>
<p>If the mismatched value is related to identity, <a href="/cloudflare-one/team-and-resources/users/users/">check the user registry</a> and verify the values that are passed to Gateway from your IdP. Cloudflare updates the registry when the user enrolls in the Cloudflare One Client. If the user's identity is outdated, ask the user to re-authenticate the client (<strong>Profile</strong> &gt; <strong>Account information</strong> &gt; <strong>Re-authenticate</strong>)<sup><a href="#footnote-cloudflare-one-tunnel-troubleshoot-private-networks-mdx-1">1</a></sup>.</p>
</li>
<li>
<p>If the mismatched value is related to device posture, <a href="/cloudflare-one/reusable-components/posture-checks/#2-verify-device-posture-checks">view posture check results</a> for the user's device. Verify that the device passes the posture checks configured in the policy.</p>
</li>
</ul>
</li>
</ol>
<h2 id="6-are-the-correct-gateway-proxy-settings-enabled"><ol start="6">
<li>Are the correct Gateway proxy settings enabled?</li>
</ol></h2>
<p>Under <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>, ensure that <strong>Allow Secure Web Gateway to proxy traffic</strong> is enabled for TCP, UDP, and ICMP traffic. UDP is required for proxying DNS traffic and other UDP packets, while ICMP is required for <code>ping</code> and other administrative functions.</p>
<h2 id="7-is-the-user-s-traffic-reaching-the-tunnel"><ol start="7">
<li>Is the user's traffic reaching the tunnel?</li>
</ol></h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/#view-logs-on-your-local-machine">Review your tunnel log stream</a>. If you do not see any requests to your application, ensure that you have added the appropriate static routes to your Cloudflare Tunnel.</p>
<h2 id="8-is-the-tunnel-forwarding-requests-to-your-application"><ol start="8">
<li>Is the tunnel forwarding requests to your application?</li>
</ol></h2>
<p>Verify that you can connect to the application directly from the <code>cloudflared</code> host machine:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9882.md")
</div></div>
<p>You can also use a packet capture tool such as <code>tcpdump</code> or Wireshark to trace whether traffic from the user device successfully reaches <code>cloudflared</code> and routes to your application. Traffic to your application will carry the source IP of the <code>cloudflared</code> host.</p>
<h2 id="9-how-is-your-application-handling-requests"><ol start="9">
<li>How is your application handling requests?</li>
</ol></h2>
<ol>
<li>
<p>Check if the application server has a local firewall in place that is blocking requests from the <code>cloudflared</code> host machine.</p>
</li>
<li>
<p>Check if the application server needs to initiate any connection towards the user's device. If so, this is a limitation of <code>cloudflared</code> and you should instead <a href="/mesh/">deploy Cloudflare Mesh</a> to enable bidirectional traffic.</p>
</li>
</ol>
<h2 id="10-is-tls-inspection-affecting-the-connection-to-your-application"><ol start="10">
<li>Is TLS inspection affecting the connection to your application?</li>
</ol></h2>
<p>If there is a problem with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS inspection</a>, the user will get an <code>Insecure Upstream</code> error when they access the application in a browser. They will probably not get an error if they access the application outside of a browser.</p>
<p>Customers who have <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> enabled can check the <a href="/logs/logpush/logpush-job/datasets/account/gateway_http/">Gateway HTTP dataset</a> for any hostnames which have an elevated rate of <code>526</code> HTTP status codes.</p>
<p>To troubleshoot TLS inspection:</p>
<ol>
<li>Create a temporary Gateway HTTP policy that disables TLS inspection for all traffic to the application. For example:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination IP</td>
<td>in</td>
<td><code>10.2.3.4/32</code></td>
<td>Do Not Inspect</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>
<p>If the <code>Do Not Inspect</code> policy enables the user to connect, verify that the TLS certificate used by your application is trusted by a public <span class="nb-glossary-tooltip" title="Certificate Authority (CA)">CA</span> and not self-signed. Cloudflare Gateway is unable to negotiate TLS with applications that use self-signed certificates. For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#inspection-limitations">TLS inspection limitations</a>.</p>
<p>To work around the issue:</p>
<ul>
<li><strong>Option 1:</strong> Create a permanent <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect"><code>Do Not Inspect</code> HTTP policy</a> for this application.</li>
<li><strong>Option 2:</strong> Customers who use their <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">own certificate infrastructure</a> for inspection can opt to create an <a href="/cloudflare-one/traffic-policies/http-policies/#untrusted-certificates">Allow <em>Pass Through</em> policy</a> which enables our proxy to accept the TLS negotiation from your application. This will allow requests to flow correctly without the need for a <code>Do Not Inspect</code> policy.</li>
<li><strong>Option 3:</strong> If your application uses <code>HTTPS</code> or other common protocols, you can add a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">published application</a> to your Cloudflare Tunnel and set <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#notlsverify">noTLSVerify</a> to <code>true</code>. This will allow <code>cloudflared</code> to trust your self-signed certificate.</li>
</ul>
</li>
</ol>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-cloudflare-one-tunnel-troubleshoot-private-networks-mdx-1">In Cloudflare One Client version 2026.1 and earlier, select **Preferences** > **Account** > **Re-Authenticate Session**.</li></ol></section>
