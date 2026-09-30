<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/5392.md")
</div></details>
<p>Virtual networks provide routing isolation within your Cloudflare account. Each virtual network maintains its own routing table, allowing you to separate traffic between different environments, partners, or applications.</p>
<p>For example, an organization may have separate &quot;production&quot; and &quot;staging&quot; VPC networks that both use the same private IP range (such as <code>10.128.0.0/24</code>). Without virtual networks, Cloudflare cannot distinguish between <code>10.128.0.1</code> in production and <code>10.128.0.1</code> in staging. By creating two virtual networks, you can deterministically route traffic to the correct environment. Users select which virtual network they want to connect to in the Cloudflare One Client.</p>
<p>For a conceptual overview of virtual networks, including how they work across Cloudflare products, refer to <a href="/cloudflare-one/networks/virtual-networks/">Virtual networks</a>.</p>
<h2 id="use-cases">Use cases</h2>
<p>Here are a few scenarios where virtual networks may prove useful:</p>
<ul>
<li>Manage production and staging environments that use the same address space.</li>
<li>Manage acquisitions or mergers between organizations that use the same address space.</li>
<li>Allow IT professional services to access their customer's network for various administration and management purposes.</li>
<li>Allow developers or homelab users to deterministically route traffic through their home network to enforce additional security controls.</li>
<li>Guarantee additional segmentation (beyond just policy enforcement) between networks and resources for security reasons, while keeping all configuration within a single Cloudflare account.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Install <code>cloudflared</code></a> on each private network.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client</a> on user devices.</li>
</ul>
<h2 id="create-a-virtual-network">Create a virtual network</h2>
<p>In this example, &quot;private network&quot; refers to a distinct environment (such as staging or production) that has its own overlapping IP address space (<code>10.128.0.1/32</code> staging and <code>10.128.0.1/32</code> production). If your environments use non-overlapping IPs, you do not need a separate tunnel for each. Instead, you can add multiple routes to a single tunnel.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5396.md")
</div></div>
<h2 id="delete-a-virtual-network">Delete a virtual network</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5399.md")
</div></div>
<h2 id="connect-to-a-virtual-network">Connect to a virtual network</h2>
<h3 id="windows-macos-and-linux">Windows, macOS, and Linux</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5402.md")
</div></div>
<p>When you visit <code>10.128.0.3/32</code>, the Cloudflare One Client will route your request to the staging environment.</p>
<h3 id="ios-android-and-chromeos">iOS, Android, and ChromeOS</h3>
<ol>
<li>Launch the Cloudflare One Agent app.</li>
<li>Go to <strong>Advanced</strong> &gt; <strong>Connection options</strong> &gt; <strong>Virtual networks</strong>.</li>
<li>Choose the virtual network you want to connect to, for example <code>staging-vnet</code>.</li>
</ol>
<p>When you visit <code>10.128.0.3/32</code>, the Cloudflare One Client will route your request to the staging environment.</p>
