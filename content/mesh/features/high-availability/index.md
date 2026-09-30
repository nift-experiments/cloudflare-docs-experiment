---
cp9:
  canonical: https://developers.cloudflare.com/mesh/features/high-availability/
  description: Configure active-passive replicas to provide high availability for routed Cloudflare Mesh networks.
  full_title: High availability for Cloudflare Mesh nodes · Cloudflare Docs
  head_html: <title>High availability for Cloudflare Mesh nodes · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure active-passive replicas to provide high availability for routed Cloudflare Mesh networks."><link rel="canonical" href="https://developers.cloudflare.com/mesh/features/high-availability/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/mesh/features/high-availability/index.md"><meta property="og:title" content="High availability for Cloudflare Mesh nodes · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure active-passive replicas to provide high availability for routed Cloudflare Mesh networks."><meta property="og:url" content="https://developers.cloudflare.com/mesh/features/high-availability/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Mesh"><meta name="algolia_product_filter" content="Cloudflare Mesh"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Mesh"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/mesh/features/high-availability/#page","headline":"High availability for Cloudflare Mesh nodes \u00b7 Cloudflare Docs","description":"Configure active-passive replicas to provide high availability for routed Cloudflare Mesh networks.","url":"https://developers.cloudflare.com/mesh/features/high-availability/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /mesh/features/high-availability/
  schema: 1
---
<p>For production deployments, you can run multiple replicas of a Mesh node in active-passive mode. All replicas share the same node identity and advertise the same <a href="/mesh/features/routes/">routes</a>. If the active replica goes down, Cloudflare automatically promotes a standby replica.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="masque-required">MASQUE required</h3>
@markup("md", "content/.markup/bodies/10774.md")
</aside>
<h2 id="when-to-use-high-availability">When to use high availability</h2>
<p>High availability provides resilience for CIDR route prefixes advertised by a Mesh node. When the active replica disconnects, Cloudflare promotes a standby so that traffic to the advertised subnets continues to flow.</p>
<p>This means HA is useful for nodes that have routes configured — nodes acting as subnet gateways for private networks behind them. If a node is only used for direct Mesh IP connectivity (no routes), HA has limited benefit because the node's Mesh IP is tied to the individual replica.</p>
<h2 id="how-it-works">How it works</h2>
<p>When you create a Mesh node with high availability enabled, Cloudflare generates a single token for that node. You install the Cloudflare One Client on multiple Linux hosts using this token. Each host registers as a replica of the same node.</p>
<ul>
<li>All replicas advertise the same CIDR routes.</li>
<li>One replica is active at a time. The others are passive standby.</li>
<li>If the active replica disconnects, Cloudflare automatically promotes a passive replica.</li>
<li>Failover is handled by Cloudflare's network.</li>
</ul>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;  subgraph replicas[&quot;Mesh node: web-server&quot;]&#10;    R1[&quot;Replica 1 &lt;br&gt; (active)&quot;]&#10;    R2[&quot;Replica 2 &lt;br&gt; (standby)&quot;]&#10;    R3[&quot;Replica 3 &lt;br&gt; (standby)&quot;]&#10;  end&#10;  CF((Cloudflare)) &lt;--&gt; R1&#10;  CF -. failover .-&gt; R2&#10;  CF -. failover .-&gt; R3&#10;  client[&quot;Client device&quot;] &lt;--&gt; CF&#10;</code></pre>
<h2 id="create-a-node-with-high-availability">Create a node with high availability</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10777.md")
</div></div>
<h2 id="add-replicas">Add replicas</h2>
<p>To add a replica to an existing high-availability node, install the Cloudflare One Client on a new Linux host and register it using the same node token.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10787.md")
</div></div>
<p>The new replica will be in standby mode until the active replica disconnects.</p>
<h2 id="view-replicas">View replicas</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10790.md")
</div></div>
<h2 id="manual-failover">Manual failover</h2>
<p>In addition to automatic failover when the active replica disconnects, you can manually promote a passive replica to active.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10793.md")
</div></div>
<h2 id="considerations">Considerations</h2>
<h3 id="setup-requirements">Setup requirements</h3>
<ul>
<li>High availability is set at node creation time and cannot be changed afterward.</li>
<li>You must install the client on at least two hosts for failover to work. A single replica means no redundancy.</li>
<li>High availability requires that the Mesh node's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> is configured to use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a>, the default protocol for the Cloudflare One Client. It does not work if the device profile uses WireGuard instead.</li>
</ul>
<h3 id="network-configuration">Network configuration</h3>
<ul>
<li>All replicas must be on the same subnet and have the same network routing configuration (Split Tunnels, static routes).</li>
<li>HA provides resilience for CIDR route prefixes. Nodes without routes do not benefit from HA failover.</li>
</ul>
<h3 id="failover-behavior">Failover behavior</h3>
<ul>
<li>Failover time depends on how quickly Cloudflare detects the active replica has disconnected (typically seconds).</li>
<li>Inbound traffic (from Mesh clients to the subnet) fails over automatically on Cloudflare's network. Cloudflare routes traffic to the newly promoted active replica.</li>
<li>Outbound traffic (from devices on the subnet through the Mesh node) does not fail over automatically. Your environment must detect that a different replica has been promoted to active and update routing tables to send traffic through the now-active host. There is no client-side failover for on-ramp traffic at this time.</li>
</ul>
