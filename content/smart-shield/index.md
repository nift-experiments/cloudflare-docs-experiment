<div class="nb-description">
@markup("md", "content/.markup/bodies/346.md")
</div>
<p>Every request that reaches your origin server costs resources — bandwidth, compute, and connections. When traffic spikes or your content is requested from many locations simultaneously, your origin can become a bottleneck. Smart Shield is a bundle of origin protection and performance features that reduce the number of requests and connections between Cloudflare's network and your origin server.</p>
<p>Smart Shield includes <a href="/smart-shield/configuration/smart-tiered-cache/">Smart Tiered Cache</a>, which organizes Cloudflare data centers into upper-tier and lower-tier groups so that only upper-tier data centers contact your origin for uncached content. Combined with <a href="/smart-shield/concepts/connection-reuse/">connection reuse</a>, which packages multiple requests into a single connection to your origin, Smart Shield reduces both the volume of origin requests and the number of open connections.</p>
<p>Depending on your <a href="/smart-shield/get-started/#packages-and-availability">package tier</a>, Smart Shield can also include:</p>
<ul>
<li><a href="/smart-shield/configuration/argo/">Argo Smart Routing</a> — routes traffic through the fastest network paths to reduce latency.</li>
<li><a href="/smart-shield/configuration/regional-tiered-cache/">Regional Tiered Cache</a> — adds a regional cache layer between lower-tier and upper-tier data centers for geographic data locality (Enterprise plans, or Smart Shield Advanced).</li>
<li><a href="/smart-shield/configuration/cache-reserve/">Cache Reserve</a> — persistent cache storage that reduces cache misses for infrequently accessed content.</li>
<li><a href="/smart-shield/configuration/health-checks/">Health Checks</a> — monitors your origin server availability (Pro plans and above).</li>
<li><a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> — reserved IP addresses for origin allowlisting (Enterprise).</li>
</ul>
<p>For a visual overview of how these features work together, refer to the <a href="/smart-shield/concepts/network-diagram/">network diagram</a>.</p>
<p>Learn how to <a href="/smart-shield/get-started/">get started</a>.</p>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/347.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/348.md")
</div>
