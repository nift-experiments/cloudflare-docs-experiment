<h2 id="what-data-is-covered-by-the-customer-metadata-boundary">What data is covered by the Customer Metadata Boundary?</h2>
<p>Nearly all end user metadata is covered by the Customer Metadata Boundary. This includes all of the end user data for which Cloudflare is a processor, as defined in the <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare Privacy Policy</a>. Cloudflare is a data processor of Customer Logs, which are defined as end user logs that we make available to our customers via the dashboard or other online interfaces. End users are those who access or use our customers' domains, networks, websites, application programming interfaces, and applications.</p>
<p>Specific examples of this data include all of the analytics in our dashboard and APIs on requests, responses, and security products associated and all of the logs received through Logpush.</p>
<h2 id="what-data-is-not-covered-by-the-customer-metadata-boundary">What data is not covered by the Customer Metadata Boundary?</h2>
<p>Some of the data for which Cloudflare is a controller, as defined in the <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare Privacy Policy</a>.</p>
<p>Some examples:</p>
<ul>
<li>Customer account data (for example, name and billing information).</li>
<li>Customer configuration data (for example, the content of WAF custom rules).</li>
<li>Metadata that is &quot;operational&quot; in nature — data needed for Cloudflare to properly operate our network. This includes metadata such as:
<ul>
<li>System data generated for debugging (for example, internal application logs, core dumps).</li>
<li>Networking flow data (for example, sFlow samples from routers), including data on DDoS attacks.</li>
</ul>
</li>
</ul>
<h2 id="who-can-use-the-customer-metadata-boundary">Who can use the Customer Metadata Boundary?</h2>
<p>Currently, this is available for Enterprise customers as part of the Data Localization Suite.</p>
<p>The Customer Metadata Boundary is for customers who want to limit personal data transfer outside the EU or the US (depending on the selected region). These customers should already be using Regional Services, which ensures that traffic content is only ever decrypted within the geographic region specified by the customer.</p>
<h2 id="what-are-the-analytics-products-available-for-metadata-boundary">What are the analytics products available for Metadata Boundary?</h2>
<p>HTTP and Firewall analytics are available.</p>
<p>At the moment, there are no analytics available for Workers, DNS, and Load Balancing. Additionally, there are no dashboard logs or analytics for <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#limitations">Gateway</a>. Enterprise users can still export Gateway logs via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>
