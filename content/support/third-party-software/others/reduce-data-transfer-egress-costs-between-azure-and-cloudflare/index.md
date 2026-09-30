<h2 id="overview">Overview</h2>
<p>Cloudflare launched Bandwidth Alliance in 2018 – a group of forward-looking cloud and storage providers who have agreed to waive or steeply discount egress costs for mutual customers. </p>
<p>Cloudflare customers using Azure can lower their egress bills between Cloudflare and Azure via <a href="https://docs.microsoft.com/en-us/azure/virtual-network/routing-preference-overview">Microsoft Routing Preference</a>.</p>
<hr />
<h2 id="how-to">How to</h2>
<p>To lower your data transfer costs from Azure and Cloudflare: </p>
<ol>
<li>In the Azure portal, go to your storage account. </li>
<li>Navigate to <strong>Network Routing &gt; Firewalls and virtual networks</strong>.</li>
<li>For <strong>Routing preference</strong>, choose <strong>Internet routing</strong>.</li>
<li>Publish route-specific endpoint to <strong>Internet routing</strong>.</li>
<li>Navigate to <strong>Properties</strong>.</li>
<li>Locate the endpoint values for <strong>Internet Routing</strong>.</li>
<li>Enter these endpoint values in your Cloudflare Dashboard.</li>
</ol>
<p><img src="/assets/upstream/images/support/bandwidth-alliance.png" alt="Example of where to enter endpoint URLs from Microsoft Azure into your Cloudflare dashboard." /></p>
<p>For additional details, refer to <a href="https://docs.microsoft.com/en-us/azure/storage/common/configure-network-routing-preference?tabs=azure-portal">Configure network routing preference for Azure Storage</a> and <a href="https://docs.microsoft.com/en-us/azure/storage/common/network-routing-preference">Microsoft Routing Preference</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/discounted-egress-for-cloudflare-customers-from-microsoft-azure-is-now-available/">Microsoft Azure data transfer announcement</a> (blog)</li>
<li><a href="https://www.cloudflare.com/bandwidth-alliance/">Bandwidth Alliance</a></li>
</ul>
