<p>Regional Services gives you the ability to accommodate regional restrictions by choosing which subset of data centers decrypt and service HTTPS traffic.</p>
<p>Regional Services receives and processes traffic within designated regions for customers who need to meet regional compliance requirements or have preferences for maintaining regional control over their data. Examples of use cases include accommodating regional restrictions like <a href="https://www.cloudflare.com/trust-hub/gdpr/">GDPR</a> (General Data Protection Regulation), or fulfilling contractual agreements with customers that include geographic restrictions on data flows or data processing.</p>
<p>With Regional Services, TLS termination — the point at which encrypted HTTPS traffic is decrypted so Cloudflare can inspect and apply your security rules — only occurs inside the configured region. For example, if a hostname is configured to regionalize to the European Union (EU), any HTTPS request from the United States (US) will be forwarded in encrypted form to an EU data center before being decrypted.</p>
<h2 id="global-traffic-management">Global traffic management</h2>
<p>Regional Services accepts traffic at any Cloudflare data center worldwide and applies <a href="/ddos-protection/about/attack-coverage/">L3/L4 DDoS mitigations</a> — network-layer and transport-layer protections that block volumetric attacks without needing to decrypt traffic content. Meanwhile, security, performance, and reliability functions that require access to decrypted traffic are applied only at in-region Cloudflare locations.</p>
<p>Regional Services ensures that all of the following application-layer services (among others) operate within the selected region:</p>
<ul>
<li>Storing and retrieving content from Cache.</li>
<li>Blocking malicious HTTP payloads with the Web Application Firewall (WAF).</li>
<li>Detecting and blocking suspicious activity with Bot Management.</li>
<li>Running Cloudflare Workers scripts.</li>
<li>Load Balancing traffic to the best origin servers (or other <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/7426.md")
</div>).
<p>Regional Services is a compliance solution, not a performance optimization. Within the configured region, Cloudflare routes requests to the most performant in-region data center — using a scoring system that considers available connections, latency, and load — which is not necessarily the closest one. Refer to <a href="/support/troubleshooting/general-troubleshooting/geographic-traffic-routing/">Geographic traffic routing</a> for more details. For geographically large regions, requests may be processed at a data center farther than the closest in-region option.</p>
<h2 id="request-flow-example">Request flow example</h2>
<p>The following diagram is a high-level example of the flow of a request coming from an end user located within the US connecting to a website using Cloudflare Regional Services set to EU.</p>
<br />
<pre><code class="language-mermaid">sequenceDiagram&#10;    participant User in US as End user in US&#10;    participant CloudflarePoPNYC as Closest data center &lt;br&gt; in US&#10;    participant CloudflarePoPDUB as Data center in EU&#10;    participant EUOriginServer as Origin Server&#10;&#10;    User in US-&gt;&gt;CloudflarePoPNYC: TCP connection&#10;    Note right of User in US: TLS encryption&#10;    Note left of CloudflarePoPNYC: TCP connection&lt;br&gt; (no TLS unwrapping)&#10;    Note right of CloudflarePoPNYC: L3 DDoS protection&#10;    CloudflarePoPNYC--&gt;&gt;CloudflarePoPDUB: Forwards&lt;br&gt; encrypted request&#10;    Note right of CloudflarePoPDUB: TLS termination (decryption)&#10;    Note right of CloudflarePoPDUB: Applies security&lt;br&gt; and performance features&lt;br&gt; (for example, WAF, Configuration Rules, &lt;br&gt;Load Balancing)&#10;    Note right of CloudflarePoPDUB: TLS encryption&#10;    CloudflarePoPDUB--&gt;&gt;EUOriginServer: Requests content&#10;    EUOriginServer--&gt;&gt;CloudflarePoPDUB: Response content&#10;    Note right of CloudflarePoPDUB: TLS termination (decryption)&#10;    Note right of CloudflarePoPDUB: Caches eligible static content&lt;br&gt; (on encrypted disks)&#10;    Note right of CloudflarePoPDUB: TLS encryption&#10;    CloudflarePoPDUB-&gt;&gt;User in US: Forwards response with content&#10;</code></pre>
<br />
<h2 id="egress-behavior-and-ingress-ips">Egress behavior and ingress IPs</h2>
<p>Regional Services controls where traffic is ingested and processed (decrypted), not where it exits to your origin. Egress IPs to your origin are site-local IPs from the in-region data center where the request was processed. If you need guaranteed egress IP geolocation or origin allowlisting, use <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> in addition to Regional Services.</p>
<p>For Regional Hostnames using Cloudflare shared ingress IPs, third-party IP geolocation providers may return a location that does not match your configured region (often the United States). This is a limitation of shared IP addressing and does not affect where your traffic is actually decrypted and processed.</p>
<h2 id="ways-to-use-regional-services">Ways to use Regional Services</h2>
<p>Regional Services regionalizes traffic through several mechanisms, depending on how your traffic reaches Cloudflare. Most customers use only one of these:</p>
<ul>
<li>
<p><strong>Regional Hostnames</strong> — Regionalize proxied hostnames. You assign a region to a hostname through the <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames API</a> or the dashboard, and Cloudflare steers traffic for that hostname to in-region data centers. This is the most common option and is generally available. To set it up, refer to <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a>.</p>
</li>
<li>
<p><strong>Regionalized Spectrum Applications</strong> — Regionalize <a href="/spectrum/">Spectrum</a> HTTP/S applications. Spectrum applications use a separate regionalization mechanism from the Regional Hostnames API, and work with both <a href="/spectrum/about/static-ip/">Spectrum Static IPs</a> and <a href="/byoip/">Bring Your Own IP (BYOIP)</a>. To set it up, refer to <a href="/data-localization/regional-services/spectrum-applications/">Regionalized Spectrum Applications</a>.</p>
</li>
<li>
<p><strong>Regionalized IP Bindings</strong> — Bind a <a href="/byoip/">BYOIP</a> prefix to a region so that traffic destined for those IP addresses is processed in-region. Because bindings are managed through the API as address maps, this option is well suited to broad configurations (whole prefixes, zones, or accounts) and is fully self-serve once entitlements are enabled. This option requires the Regional Services and Regional Services for BYOIP entitlements. To set it up, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>
</li>
</ul>
<p>The following table compares the three options to help you choose:</p>
<table>
<thead>
<tr>
<th>Offering</th>
<th>How traffic is addressed</th>
<th>Granularity</th>
<th>Static IP / BYOIP</th>
<th>API</th>
<th>Availability</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a></td>
<td>Cloudflare shared IPs</td>
<td>Per hostname</td>
<td>Not supported</td>
<td>Regional Hostnames API</td>
<td>GA</td>
<td>Most deployments; regionalizing specific proxied hostnames</td>
</tr>
<tr>
<td><a href="/data-localization/regional-services/spectrum-applications/">Regionalized Spectrum Applications</a></td>
<td>Dedicated IP via Spectrum app</td>
<td>Per zone (all Spectrum HTTP/S apps)</td>
<td>Static IPs and BYOIP</td>
<td>Spectrum API</td>
<td>GA</td>
<td>Traffic addressed by IP that needs Static IPs or BYOIP</td>
</tr>
<tr>
<td><a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a></td>
<td>BYOIP prefix at the IP layer</td>
<td>Per CIDR / IP prefix (scales to whole prefixes)</td>
<td>BYOIP only</td>
<td>Data Localization Suite API</td>
<td>GA</td>
<td>Broad, self-serve regionalization managed via address maps</td>
</tr>
</tbody>
</table>
<p>All three options support <a href="/data-localization/region-support/#region-types">managed regions</a>. <a href="/data-localization/region-support/#region-types">Custom regions</a> are available for Regionalized Spectrum Applications and Regionalized IP Bindings, but not for Regional Hostnames.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="a-note-on-naming">A note on naming</h3>
@markup("md", "content/.markup/bodies/7425.md")
</aside>
<h2 id="get-started">Get started</h2>
<p>Setting up Regional Services follows the same path regardless of which option you choose:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7427.md")
</div>
<h2 id="availability-and-sla">Availability and SLA</h2>
<p>For availability and Service Level Agreements (SLAs), refer to your Cloudflare Enterprise contract. For Regional Services configurations restricted to a single country (except the US), Cloudflare's SLA includes specific exclusions: because traffic cannot fail over to data centers outside that country, there is no automatic failover if in-country capacity is unavailable. Multi-country regions (for example, the European Union) generally maintain the standard SLA.</p>
<h2 id="additional-information">Additional information</h2>
<p>For more details about the products that are compatible with Regional Services, refer to the <a href="/data-localization/compatibility/">Cloudflare product compatibility</a> page. If you have purchased these products as part of your Enterprise subscription plan, Cloudflare will only terminate TLS connections for these products in the geographic region you have configured for Regional Services.</p>
