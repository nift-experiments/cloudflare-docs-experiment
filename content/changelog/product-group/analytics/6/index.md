<h1 id="changelog">Changelog</h1>

<h2 id="new-fields-added-to-gateway-related-datasets-in-cloudflare-logs"><a href="/changelog/post/2024-10-08-new-gateway-fields/">New fields added to Gateway-related datasets in Cloudflare Logs</a></h2>
<p><em>2024-10-08</em></p>
<p>Cloudflare has introduced new fields to two Gateway-related datasets in Cloudflare Logs:</p>
<ul>
<li>
<p><strong>Gateway HTTP</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>CategoryIDs</code>, <code>CategoryNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
<li>
<p><strong>Gateway Network</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>TransportProtocol</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
</ul>


<h2 id="try-out-magic-network-monitoring"><a href="/changelog/post/2024-09-24-magic-network-monitoring/">Try out Magic Network Monitoring</a></h2>
<p><em>2024-09-24</em></p>
<p>The free version of Magic Network Monitoring (MNM) is now available to everyone with a Cloudflare account by default.</p>
<ol>
<li>Log in to your <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Magic Monitoring</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/network-flow/get-started.png" alt="Try out the free version of Magic Network Monitoring" /></p>
<p>For more details, refer to the <a href="/network-flow/get-started/">Get started guide</a>.</p>


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>


<h2 id="easily-exclude-eu-visitors-from-rum"><a href="/changelog/post/2025-02-25-rum-exclude-eu/">Easily Exclude EU Visitors from RUM</a></h2>
<p><em>2024-02-26</em></p>
<p>You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.</p>
<p><img src="/assets/upstream/images/changelog/web-analytics/2025-02-26-rum-eu.png" alt="RUM Enablement UI" /></p>
<p>Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.</p>
<p>To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.</p>
<p>You can learn more about what metrics are reported by Web Analytics and how it is collected <a href="/web-analytics/data-metrics/">in the Web Analytics documentation</a>. You can enable Web Analytics on any hostname by going to the <a href="https://dash.cloudflare.com/?to=/:account/web-analytics/sites">Web Analytics</a> section of the dashboard, selecting &quot;Manage Site&quot; for the hostname you want to monitor, and choosing the appropriate enablement option.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/analytics/5/">Previous</a><span>Page 6 of 6</span></nav>
