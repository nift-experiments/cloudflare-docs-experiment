---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/tunnel-capacity/
  description: Size and scale cloudflared tunnel capacity.
  full_title: Tunnel capacity for cloudflared · Cloudflare Learning Paths
  head_html: <title>Tunnel capacity for cloudflared · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Size and scale cloudflared tunnel capacity."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/tunnel-capacity/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/tunnel-capacity/index.md"><meta property="og:title" content="Tunnel capacity for cloudflared · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Size and scale cloudflared tunnel capacity."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/tunnel-capacity/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/tunnel-capacity/#page","headline":"Tunnel capacity for cloudflared \u00b7 Cloudflare Learning Paths","description":"Size and scale cloudflared tunnel capacity.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/tunnel-capacity/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/connect-private-network/tunnel-capacity/
  schema: 1
---
<p>Now that you have a Cloudflare Tunnel up and running, evaluate whether <code>cloudflared</code> has enough system resources to handle the expected volume of requests from end users.
Unlike legacy VPNs where throughput is determined by the server's memory, CPU and other hardware specifications, Cloudflare Tunnel throughput is primarily limited by the number of ports configured in system software. Therefore, when sizing your <code>cloudflared</code> server, the most important element is sizing the available ports on the machine to reflect the expected throughput of TCP and UDP traffic.</p>
<p>If you have exhausted the ports on a single machine, you will need to add additional servers running <code>cloudflared</code>.</p>
<h2 id="size-the-tunnel">Size the tunnel</h2>
<p>To determine how many <code>cloudflared</code> host servers you need:</p>
<ol>
<li>Start with our baseline recommendations:</li>
</ol>
<ul>
<li>Run a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflared-replicas"><code>cloudflared</code> replica</a> on two dedicated host machines per network location. Using two hosts enables server-side redundancy and traffic balancing.</li>
<li>Size each host with minimum 4GB of RAM and 4 CPU cores.</li>
<li>Allocate 50,000 <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/#number-of-ports">ports</a> to the <code>cloudflared</code> process on each host.</li>
</ul>
<p>This setup is usually sufficient to handle traffic from 8,000 users (4,000 per host).</p>
<ol start="2">
<li>
<p>After you have completed this learning path and have users actively engaging with the network, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/#calculate-your-tunnel-capacity">calculate</a> your actual tunnel usage.</p>
</li>
<li>
<p>Decide how much headroom you want to include and <a href="#scale-the-tunnel">resize the tunnel</a> if needed.</p>
</li>
</ol>
<h2 id="scale-the-tunnel">Scale the tunnel</h2>
<p>There are two ways to scale Cloudflare Tunnel: you could either add additional replicas of the existing tunnel (Figure 1), or you could divide your network's IP space across multiple tunnels (Figure 2).</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TB&#10;accTitle: Figure 1: Multiple replicas of a tunnel that proxies all private networks.&#10;subgraph replica1[my-tunnel]&#10;  ip1[10.0.0.0/8 &lt;/br&gt; 172.0.0.0/8 &lt;/br&gt; 192.0.0.0/8]&#10;end&#10;subgraph replica2[my-tunnel]&#10;  ip2[10.0.0.0/8 &lt;/br&gt; 172.0.0.0/8 &lt;/br&gt; 192.0.0.0/8]&#10;end&#10;subgraph replica3[my-tunnel]&#10;  ip3[10.0.0.0/8 &lt;/br&gt; 172.0.0.0/8 &lt;/br&gt; 192.0.0.0/8]&#10;end&#10;replica1 &lt;--&gt; C((Cloudflare))&#10;replica2 &lt;--&gt; C&#10;replica3 &lt;--&gt; C&#10;</code></pre>
<pre tabindex="0"><code class="language-mermaid">flowchart TB&#10;accTitle: Figure 2: Multiple tunnels proxying different private networks.&#10;subgraph tunnel-1&#10;  ip1[10.0.0.0/8]&#10;end&#10;subgraph tunnel-2&#10;  ip2[172.0.0.0/8]&#10;end&#10;subgraph tunnel-3&#10;  ip3[192.0.0.0/8]&#10;end&#10;tunnel-1 &lt;--&gt; C((Cloudflare))&#10;tunnel-2 &lt;--&gt; C&#10;tunnel-3 &lt;--&gt; C&#10;</code></pre>
<h3 id="when-to-add-replicas">When to add replicas</h3>
<p>Adding additional <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflared-replicas">replicas</a> of an existing Cloudflare Tunnel (two is the baseline recommendation) should only be done to support additional traffic to the IP routes in the tunnel. Replicas should always be added in the same physical location as one another so that they can operate in a pooled mode. If you are considering adding a replica in a different geographic location, reevaluate the network proxy design for your Cloudflare Tunnel and refer to <a href="#when-to-add-tunnels">When to add tunnels</a>.</p>
<h3 id="when-to-add-tunnels">When to add tunnels</h3>
<h4 id="servers-in-different-locations">Servers in different locations</h4>
<p>Consider creating brand new tunnels when your network is dispersed across different geographic locations. For example, assume that the network represented by <code>10.0.0.0/8</code> is almost entirely contiguous in Eastern United States, with one non-overlapping exception for <code>10.0.50.0/24</code> served out of the Pacific Northwest. Rather than serve an additional replica from the Pacific Northwest, we recommend breaking out <code>10.0.50.0/24</code> into a separate Cloudflare Tunnel. Serve this new tunnel from a host machine near the Pacific Northwest with its own balanced replica implementation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9893.md")
</aside>
<h4 id="servers-in-same-location">Servers in same location</h4>
<p>Even if all routes in your network are served from the same physical location, it may eventually make sense from a control-plane redundancy perspective to split up the network into separate tunnels rather than add replicas.</p>
<p>For instance, if you proxy the ranges <code>10.0.0.0/8</code>, <code>172.0.0.0/8</code>, and <code>192.0.0.0/8</code> from a single tunnel with multiple replicas, you may reach a point of port exhaustion with respect to the traffic flowing through the multitude of networks. It may make sense to break out <code>10.0.0.0/8</code>, <code>172.0.0.0/8</code>, and <code>192.0.0.0/8</code> into their own independent tunnels, each with their own replica. Alternatively, you could find specific applications or functions (like DNS servers or other functions that generate a high volume of independent traffic) and break them out into standalone tunnels with properly rated throughput and replica volume.</p>
