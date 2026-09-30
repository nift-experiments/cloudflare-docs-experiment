<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 18, 2025</time><h2 id="post-title">Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>You can now route private traffic to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is <strong>free for all Cloudflare One customers</strong>.</p>
<p>Previously, Tunnel routes could only be defined by IP address or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">CIDR range</a>. This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/tunnel-hostname-routing.webp" alt="Hostname-based routing in Cloudflare Tunnel" /></p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Hostname &amp; Domain Routing</strong>: Create routes for individual hostnames (e.g., <code>payroll.acme.local</code>) or entire domains (e.g., <code>*.acme.local</code>) and direct their traffic to a specific Tunnel.</li>
<li><strong>Simplified Zero Trust Policies</strong>: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.</li>
<li><strong>Precise Egress Control</strong>: Route traffic for public hostnames (e.g., <code>bank.example.com</code>) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.</li>
<li><strong>No More IP Lists</strong>: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.</li>
</ul>
<p>Get started in the Tunnels section of the Zero Trust dashboard with your first <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> or <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> route.</p>
<p>Learn more in our <a href="https://blog.cloudflare.com/tunnel-hostname-routing/">blog post</a>.</p>
</div></article></div>
