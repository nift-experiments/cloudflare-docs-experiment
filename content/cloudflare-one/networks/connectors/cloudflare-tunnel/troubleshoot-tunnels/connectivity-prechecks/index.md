---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/
  description: Connectivity pre-checks in Zero Trust networking.
  full_title: Connectivity pre-checks · Cloudflare One docs
  head_html: <title>Connectivity pre-checks · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connectivity pre-checks in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/index.md"><meta property="og:title" content="Connectivity pre-checks · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connectivity pre-checks in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="QUIC,DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/#page","headline":"Connectivity pre-checks \u00b7 Cloudflare One docs","description":"Connectivity pre-checks in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["QUIC","DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/
  schema: 1
---
<p>This guide helps you validate connectivity between your environment and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Cloudflare Tunnel endpoints</a> before deploying <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>. You will run DNS and network checks from the same host machine that will run <code>cloudflared</code> to help you identify issues that may prevent <code>cloudflared</code> from connecting to Cloudflare Tunnel endpoints.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5273.md")
</aside>
<p>Running these checks before you install <code>cloudflared</code> sets your deployment up for success and narrows down the cause of any later connectivity issues.</p>
<p>This guide is structured as follows:</p>
<ol>
<li>
<p><a href="#before-you-start">Before you start</a>: Read prerequisites and terminology.</p>
</li>
<li>
<p><a href="#2-dns-test-with-dig">DNS test with dig</a>: Confirm that DNS resolves Cloudflare Tunnel endpoints to the expected IPs.</p>
</li>
<li>
<p><a href="#3-test-network-connectivity">Test network connectivity</a>: Verify that your firewall allows outbound traffic on port <code>7844</code> (TCP and UDP).</p>
</li>
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/#4-get-help">Get help</a>: What to collect and who to contact if tests fail.</p>
</li>
</ol>
<h2 id="1-before-you-start"><ol>
<li>Before you start</li>
</ol></h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>You must have:</p>
<ul>
<li>
<p>A host machine connected to the Internet where you plan to run <code>cloudflared</code>. The tests must run from the same environment where <code>cloudflared</code> will run (same network, same firewall path).</p>
</li>
<li>
<p>A terminal session with permission to run <code>dig</code> and <code>nc</code> (netcat), or similar software.</p>
</li>
</ul>
<p><code>cloudflared</code> is platform-agnostic and supports a wide range of operating systems. For details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/">Tunnel system requirements</a>.</p>
<h3 id="terminology">Terminology</h3>
<p>When troubleshooting connectivity to Cloudflare, it is important to distinguish between:</p>
<ul>
<li>
<p>Host machine: The server or virtual machine (VM) where you will run <code>cloudflared</code>.</p>
</li>
<li>
<p>Environment: The broader setup containing the host machine (network and firewall configuration).</p>
</li>
</ul>
<p>Cloudflare Tunnel errors can originate from the environment (for example, DNS or firewall policies), even though they surface as <code>cloudflared</code> errors on the host machine. This guide focuses on the environment, not on <code>cloudflared</code> itself.</p>
<p><code>cloudflared</code> establishes <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/#outbound-only-connection">outbound-only connections</a> to Cloudflare's global network over port <code>7844</code>. The specific destinations and ports are documented in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Tunnel with firewall</a>.</p>
<h2 id="2-dns-test-with-dig"><ol start="2">
<li>DNS test with dig</li>
</ol></h2>
<p>Cloudflare Tunnel requires outbound connectivity to <code>region1.v2.argotunnel.com</code> and <code>region2.v2.argotunnel.com</code> (or to the equivalent <code>us-region1</code> and <code>us-region2</code> endpoints when using the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#region-us">US region</a>, or <code>fed-region1</code> and <code>fed-region2</code> when using the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#region-fedramp-high">FedRAMP High region</a>).</p>
<p>For a successful and healthy deployment, <code>cloudflared</code> should have <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">four active replicas</a> with connectivity to both regions (that is, both <code>region1.v2.argotunnel.com</code> and <code>region2.v2.argotunnel.com</code>, or both <code>us-region1</code> and <code>us-region2</code>).</p>
<p>First, you need to verify that your DNS resolver returns the expected IP addresses for Cloudflare Tunnel endpoints.</p>
<h3 id="2-1-test-dns-with-your-current-resolver">2.1. Test DNS with your current resolver</h3>
<p>Depending on whether you are testing a global region or the US region, run one of the following commands:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5277.md")
</div></div>
<p>The <code>ANSWER SECTION</code> should include the expected IP addresses for Cloudflare Tunnel endpoints.</p>
<p>If you receive:</p>
<ul>
<li>
<p>Status <code>NOERROR</code> with valid IP addresses - Your DNS resolver is successfully returning addresses for the Tunnel hostname. Continue to <a href="#3-test-network-connectivity">Test network connectivity</a>.</p>
</li>
<li>
<p>Status <code>SERVFAIL</code>, <code>NXDOMAIN</code>, or an empty answer - Your DNS resolver cannot resolve the Tunnel endpoint. Continue to <a href="#compare-against-1111">Compare against <code>1.1.1.1</code></a>.</p>
</li>
</ul>
<h3 id="2-2-compare-against-1-1-1-1">2.2. Compare against <code>1.1.1.1</code></h3>
<p>If your original <code>dig</code> response is empty or does not match the documented IPs, test again using Cloudflare's public resolver <code>1.1.1.1</code>:</p>
<pre tabindex="0"><code class="language-sh">dig A region1.v2.argotunnel.com @1.1.1.1&#10;</code></pre>
<h4 id="if-only-1-1-1-1-works">If only <code>1.1.1.1</code> works</h4>
<p>If <code>1.1.1.1</code> returns the correct IPs, but your original resolver does not, your local DNS resolver is misconfigured or blocked.</p>
<p>To resolve:</p>
<ul>
<li>Configure the host machine to use <code>1.1.1.1</code> as its resolver.</li>
<li>If you must keep using your existing resolver, then investigate with your system administrator or ISP why it is returning different IPs. A recursive resolver should return the same response as the authoritative DNS server. If this cannot be fixed, the issue lies within your local environment and must be resolved before deploying Cloudflare Tunnel.</li>
</ul>
<h4 id="if-neither-resolver-works">If neither resolver works</h4>
<p>If neither your original resolver nor <code>1.1.1.1</code> returns an answer, your firewall may be blocking DNS queries to Cloudflare Tunnel endpoints.</p>
<p>To resolve:</p>
<ul>
<li>Check for firewall rules blocking DNS traffic altogether (UDP on port <code>53</code>) or specific DNS queries related to Cloudflare.</li>
<li>If you are behind a managed DNS or security appliance, contact that provider to understand why queries to <code>region1.v2.argotunnel.com</code> and other Cloudflare Tunnel endpoints are blocked.</li>
</ul>
<p>Once DNS resolution returns the expected IPs from your DNS resolver, proceed to connectivity testing in step 3.</p>
<h2 id="3-test-network-connectivity"><ol start="3">
<li>Test network connectivity</li>
</ol></h2>
<p>After confirming that your DNS resolver returns the correct IPs, test whether your host machine can send packets to Cloudflare on port <code>7844</code> using both UDP and TCP.</p>
<p>Choose one of the IPs from your <code>dig</code> output (for example, <code>198.41.192.167</code>) and run the following tests.</p>
<h3 id="3-1-test-udp-connectivity">3.1. Test UDP connectivity</h3>
<pre tabindex="0"><code class="language-sh">nc -uvz -w 3 198.41.192.167 7844&#10;</code></pre>
<p>Example output:</p>
<pre tabindex="0"><code class="language-sh">Connection to 198.41.192.167 port 7844 [udp/*] succeeded!&#10;</code></pre>
<h3 id="3-2-test-tcp-connectivity">3.2. Test TCP connectivity</h3>
<pre tabindex="0"><code class="language-sh">nc -vz -w 3 198.41.192.167 7844&#10;</code></pre>
<p>Example output:</p>
<pre tabindex="0"><code class="language-sh">Connection to 198.41.192.167 port 7844 [tcp/*] succeeded!&#10;</code></pre>
<h3 id="3-3-interpret-results">3.3 Interpret results</h3>
<p>These tests answer two key questions:</p>
<ul>
<li>Can the host machine send a UDP packet to Cloudflare Tunnel endpoints?</li>
<li>Can the host machine send a TCP packet to Cloudflare Tunnel endpoints?</li>
</ul>
<p>If either protocol succeeds, <code>cloudflared</code> can use that protocol to establish the tunnel.</p>
<p>You have already confirmed DNS is working in the previous steps. These connectivity tests now verify whether your environment allows traffic to Cloudflare on port <code>7844</code>. By default, <code>cloudflared</code> automatically falls back to whichever protocol is available.</p>
<p>If a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#protocol">protocol</a> is blocked but you force <code>cloudflared</code> to use it (for example, forcing QUIC when UDP is blocked), the tunnel will fail to connect.</p>
<h4 id="both-udp-and-tcp-succeed">Both UDP and TCP succeed</h4>
<p>Your firewall allows outbound traffic and return traffic to Cloudflare's tunnel endpoint on port <code>7844</code>. <code>cloudflared</code> can connect using either <code>quic</code> (UDP) or <code>http2</code> (TCP). If both UDP and TCP succeed and your DNS test in the previous section was successful, you can successfully deploy Cloudflare Tunnel in this environment.</p>
<h4 id="udp-succeeds-tcp-fails">UDP succeeds, TCP fails</h4>
<p>Outbound UDP is allowed, but TCP on port <code>7844</code> is blocked or inspected.</p>
<p><code>cloudflared</code> will only be able to connect using <code>quic</code>. If you force <code>http2</code> in your configuration while TCP is blocked, the tunnel will fail.</p>
<p>To resolve: Either allow TCP on your local network firewall on port <code>7844</code> or stop forcing <code>http2</code> to allow <code>cloudflared</code> to connect over <code>QUIC</code> instead. Refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#protocol">Protocol</a> parameter documentation for more information.</p>
<h4 id="tcp-succeeds-udp-fails">TCP succeeds, UDP fails</h4>
<p>Outbound TCP is allowed, but UDP on port <code>7844</code> is blocked.</p>
<p><code>cloudflared</code> will only be able to connect using <code>http2</code>. If you force <code>quic</code> while UDP is blocked, the tunnel will fail.</p>
<p>To resolve: Either allow UDP on the local network firewall on port <code>7844</code> or stop forcing QUIC to allow <code>cloudflared</code> to connect over HTTP/2 instead. Refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#protocol">Protocol</a> parameter documentation for more information.</p>
<h4 id="both-udp-and-tcp-fail">Both UDP and TCP fail</h4>
<p>Packets are being dropped somewhere between the host and the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Cloudflare Tunnel endpoints</a>.</p>
<p>This usually indicates a firewall policy or upstream security control that does not allow outbound traffic (or return traffic) on port <code>7844</code>.</p>
<p>To resolve: Allow all traffic over port <code>7844</code> on the local network firewall. If this does not resolve the issue, troubleshoot with your ISP or service provider.</p>
<h2 id="4-get-help"><ol start="4">
<li>Get help</li>
</ol></h2>
<p>If either DNS or network test failed, it will likely be a problem in your local environment. You will need to debug with your administrator, ISP or cloud provider. If you believe the issue is with Cloudflare, please provide detailed information when contacting support.</p>
<p>For the fastest possible troubleshooting, ensure your support ticket includes comprehensive details. The more context you provide, the faster your issue can be identified and resolved.</p>
<p>To ensure efficient resolution when <a href="/support/contacting-cloudflare-support/">contacting support</a>, include as much relevant detail as possible in your ticket:</p>
<ul>
<pre tabindex="0"><code>&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Context: Briefly describe the scenario or use&#10;		case (for example, where the user was, what they were trying to do).&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Reproduction steps: Describe the steps you took&#10;		to reproduce the issue during troubleshhooting.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Timestamps: Be specific and include the exact&#10;		time and time zone when the issue occurred.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Troubleshooting attempts: Outline any&#10;		troubleshooting steps or changes already attempted to resolve the issue.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Tunnel ID and tunnel name.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; &lt;code&gt;cloudflared&lt;/code&gt; version (run &lt;code&gt;cloudflared --version&lt;/code&gt;).&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; How the tunnel was set up (locally-managed or remotely-managed via the dashboard).&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Tunnel logs: Include the &lt;a href=&quot;/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/#view-logs-on-your-local-machine&quot;&gt;logs from your local machine&lt;/a&gt;.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Tunnel diagnostic logs: Include &lt;a href=&quot;/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/&quot;&gt;tunnel diagnostic logs&lt;/a&gt;.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;</code></pre>
</ul>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="write-a-detailed-ticket-to-resolve-your-issue-faster">Write a detailed ticket to resolve your issue faster</h3>
@markup("md", "content/.markup/bodies/5272.md")
</aside>
