---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/
  description: How Route traffic works in Zero Trust.
  full_title: Route traffic · Cloudflare One docs
  head_html: <title>Route traffic · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Route traffic works in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/index.md"><meta property="og:title" content="Route traffic · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Route traffic works in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#page","headline":"Route traffic \u00b7 Cloudflare One docs","description":"How Route traffic works in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/
  schema: 1
---
<p>When the Cloudflare One Client (formerly WARP) is deployed on a device, Cloudflare will process all DNS queries and network traffic by default. However, under certain circumstances, you may need to exclude specific DNS queries or network traffic from the Cloudflare One Client. For example, you may need to resolve an internal hostname with a private DNS resolver instead of Cloudflare's <a href="/1.1.1.1/">public DNS resolver</a>.</p>
<p>Cloudflare recommends Enterprise users configure <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policies</a> to resolve traffic with custom resolvers. The Cloudflare One Client will send private DNS queries to Gateway, then Gateway will send the queries to custom resolvers based on matching policies.</p>
<p>Additionally, there are three options you can configure to exclude traffic from the Cloudflare One Client:</p>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a>: Send DNS requests for specific domains to a resolver other than Cloudflare Gateway. Use this when you have private hostnames that do not resolve on the public Internet (for example, internal corporate domains).</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6296.md")
</aside>
- [Split Tunnels](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/) Exclude mode: Exclude specific IP addresses or domains from the WARP tunnel. Excluded traffic bypasses the Cloudflare One Client and is handled by the local machine. Use this mode when you want most traffic to go through Gateway, but need to exclude certain routes for app compatibility or to run alongside a [third-party VPN](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/vpn/).
- [Split Tunnels](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/) Include mode: Only route traffic to specific IP addresses or domains through the WARP tunnel. All other traffic bypasses the Cloudflare One Client. Use this mode when you only want specific traffic processed by Gateway, such as traffic to resources behind [Cloudflare Tunnel](/cloudflare-one/networks/connectors/cloudflare-tunnel/).
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6295.md")
</aside>
<h2 id="how-the-cloudflare-one-client-handles-dns-requests">How the Cloudflare One Client handles DNS requests</h2>
<p>When you use the Cloudflare One Client together with <code>cloudflared</code> Tunnels or third-party VPNs, Cloudflare evaluates each request and routes it according to the following traffic flow:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;    %% Accessibility&#10;    accTitle: How the Cloudflare One Client handles DNS requests&#10;    accDescr: Flowchart describing how the Cloudflare One Client routes DNS queries when using Local Domain Fallback, Split Tunnels, and Gateway resolver policies.&#10;&#10;    A([&quot;User requests resource&quot;]) --&gt; B[&quot;Cloudflare One Client proxies all DNS traffic&quot;]&#10;    B --&gt; LDFCHK{&quot;Cloudflare One Client checks if domain is listed in Local Domain Fallback policies&quot;}&#10;&#10;    %% Left branch (LDF exists)&#10;    LDFCHK -- Domain exists in Local Domain Fallback policies --&gt; C[&quot;Local Domain Fallback&quot;]&#10;    C --&gt; ST[&quot;Split Tunnel processing&quot;]&#10;&#10;    ST --&gt; STCHK{&quot;Resolver IP included in WARP Tunnel per Split Tunnel configuration&quot;}&#10;    STCHK -- Resolver IP included in WARP Tunnel per Split Tunnel configuration --&gt; QW[&quot;Query sent via WARP Tunnel to be resolved&quot;]&#10;    STCHK -- Resolver IP not included in WARP Tunnel per Split Tunnel configuration --&gt; QO([&quot;Query sent to resolver IP outside WARP Tunnel&quot;])&#10;&#10;    %% Gateway evaluation after query via WARP&#10;    QW --&gt; GWALLOW{&quot;Allowed by Gateway&quot;}&#10;    GWALLOW -- Allowed by Gateway --&gt; OR[&quot;Evaluated by Cloudflare on-ramp routes&quot;]&#10;    GWALLOW -- Blocked by Gateway Network or HTTP Policy --&gt; BLK([&quot;Traffic blocked by Cloudflare&quot;])&#10;&#10;    OR --&gt; ORCHK{&quot;Onramp routes include resolver IP&quot;}&#10;    ORCHK -- Onramp routes do not include resolver IP --&gt; GP([&quot;Gateway proxies query to resolver IP via normal Cloudflare One Client egress route&quot;])&#10;    ORCHK -- Onramp routes include resolver IP --&gt; ADV[&quot;Cloudflare onramps advertise route that includes Resolver IP&quot;]&#10;    ADV --&gt; PR([&quot;Private resolver returns IP address to Cloudflare One Client&quot;])&#10;&#10;    %% Right branch (no LDF match)&#10;    LDFCHK -- Domain does not exist in Local Domain Fallback policies --&gt; GWR{&quot;Gateway checks Resolver Policies (Enterprise only)&quot;}&#10;&#10;    GWR -- Resolver policy is not matched --&gt; C1111a([&quot;1.1.1.1&quot;])&#10;&#10;    GWR -- Resolver policy is matched --&gt; MATCH((&quot;Resolver policy directs query to one of the following&quot;))&#10;    MATCH --&gt; IDNS([&quot;Internal DNS&quot;])&#10;    MATCH --&gt; C1111b([&quot;1.1.1.1&quot;])&#10;    MATCH --&gt; CUST([&quot;Custom resolver&quot;])&#10;    CUST --&gt; PNS([&quot;Private network services&lt;br&gt;(Cloudflare Tunnel, Cloudflare WAN, Cloudflare Mesh)&quot;])&#10;</code></pre>
<h4 id="terms-mentioned">Terms mentioned</h4>
<h5 id="on-ramps-how-traffic-gets-onto-cloudflare">On-ramps (how traffic gets onto Cloudflare)</h5>
<ul>
<li><span class="nb-glossary-tooltip" title="on-ramp">On-ramp</span>: Learn more about
<a href="/learning-paths/secure-internet-traffic/connect-devices-networks/choose-on-ramp/">On-ramps</a>.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a></li>
<li><a href="/mesh/">Cloudflare Mesh</a></li>
<li><a href="/cloudflare-wan/">Cloudflare WAN</a></li>
</ul>
<h5 id="routing-features-how-queries-are-handled">Routing features (how queries are handled)</h5>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a></li>
<li><a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway Resolver Policies</a></li>
</ul>
<h4 id="resolvers-where-queries-are-resolved">Resolvers (where queries are resolved)</h4>
<ul>
<li><a href="/dns/internal-dns/">Internal DNS</a></li>
<li><a href="/1.1.1.1/">1.1.1.1</a></li>
</ul>
<h2 id="add-a-dns-suffix">Add a DNS suffix</h2>
<p>To deploy a DNS suffix search list to all devices on a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a>, configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> in your Cloudflare One Client settings.</p>
<p>For older client versions, you can manually configure DNS suffixes at the device level using the following instructions.</p>
<h3 id="macos">macOS</h3>
<p>To manually configure a DNS suffix on macOS:</p>
<ol>
<li>Open <strong>System Settings</strong> (or <strong>System Preferences</strong> on older macOS versions).</li>
<li>Go to <strong>Network</strong> and select your active connection (<strong>Wi-Fi</strong> or <strong>Ethernet</strong>).</li>
<li>Select <strong>Details</strong> (or <strong>Advanced</strong>).</li>
<li>Go to the <strong>DNS</strong> tab.</li>
<li>Under <strong>Search Domains</strong>, select the <code>+</code> button and add your DNS suffix.</li>
<li>Select <strong>OK</strong>, then <strong>Apply</strong>.</li>
</ol>
<h3 id="windows">Windows</h3>
<p>To manually configure a DNS suffix on Windows:</p>
<ol>
<li>Open the <strong>Search</strong> bar in Windows, type <strong>View network connections</strong>, and select <strong>Open</strong>.</li>
<li>Right-click the network adapter (<strong>Wi-Fi</strong> or <strong>Ethernet</strong>) you want to modify and select <strong>Properties</strong>. (Admin privileges required.)</li>
<li>Double-click <strong>Internet Protocol Version 4 (TCP/IPv4)</strong>.</li>
<li>In the <strong>Internet Protocol (TCP/IP) Properties</strong> window, select <strong>Advanced</strong>.</li>
<li>Go to the <strong>DNS</strong> tab.</li>
<li>Select <strong>Append these DNS suffixes (in order)</strong>.</li>
<li>Select <strong>Add</strong>, enter your DNS suffix and select <strong>Add</strong>.</li>
<li>Select <strong>OK</strong> on all windows to apply changes.</li>
</ol>
