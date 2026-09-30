<p>You can use custom hostname analytics for two general purposes: exploring how your customers use your product and sharing the benefits provided by Cloudflare with your customers.</p>
<p>These analytics include <strong>Site Analytics</strong>, <strong>Bot Analytics</strong>, <strong>Cache Analytics</strong>, <strong>Security Events</strong>, and <a href="/analytics/graphql-api/features/data-sets/">any other datasets</a> with the <code>clientRequestHTTPHost</code> field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4069.md")
</aside>
<h2 id="explore-customer-usage">Explore customer usage</h2>
<p>Use custom hostname analytics to help your organization with billing and infrastructure decisions, answering questions like:</p>
<ul>
<li>&quot;How many total requests is your service getting?&quot;</li>
<li>&quot;Is one customer transferring significantly more data than the others?&quot;</li>
<li>&quot;How many global customers do you have and where are they distributed?&quot;</li>
</ul>
<p>If you see one customer is using more data than another, you might increase their bill. If requests are increasing in a certain geographic region, you might want to increase the origin servers in that region.</p>
<p>To access custom hostname analytics, either <a href="/analytics/faq/about-analytics/">use the dashboard</a> and filter by the <code>Host</code> field or <a href="/analytics/graphql-api/">use the GraphQL API</a> and filter by the <code>clientRequestHTTPHost</code> field. For more details, refer to our tutorial on <a href="/analytics/graphql-api/tutorials/end-customer-analytics/">Querying HTTP events by hostname with GraphQL</a>.</p>
<h2 id="share-cloudflare-data-with-your-customers">Share Cloudflare data with your customers</h2>
<p>With custom hostname analytics, you can also share site information with your customers, including data about:</p>
<ul>
<li>How many pageviews their site is receiving.</li>
<li>Whether their site has a large percentage of bot traffic.</li>
<li>How fast their site is.</li>
</ul>
<p>Build custom dashboards to share this information by specifying an individual custom hostname in <code>clientRequestHTTPHost</code> field of <a href="/analytics/graphql-api/features/data-sets/">any dataset</a> that includes this field.</p>
<h2 id="logpush">Logpush</h2>
<p><a href="/logs/logpush/">Logpush</a> sends metadata from Cloudflare products to your cloud storage destination or SIEM.</p>
<p>Using <a href="/logs/logpush/logpush-job/filters/">filters</a>, you can send set sample rates (or not include logs altogether) based on filter criteria. This flexibility allows you to maintain selective logs for custom hostnames without massively increasing your log volume.</p>
<p>Filtering is available for <a href="/logs/logpush/logpush-job/datasets/zone/">all Cloudflare datasets</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/4068.md")
</aside>
