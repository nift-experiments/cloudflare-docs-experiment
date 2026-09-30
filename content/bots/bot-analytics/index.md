<h2 id="business-and-enterprise">Business and Enterprise</h2>
<p>Business and Enterprise customers without Bot Management can use <strong>Bot Analytics</strong> to dynamically examine bot traffic. These dashboards offer less functionality than Bot Management for Enterprise but still help you understand bot traffic on your domain.</p>
<h3 id="access">Access</h3>
<p>You can access Bot Analytics by going to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>, and selecting your account and domain.</p>
<p>Go to <strong>Security</strong> &gt; <strong>Analytics</strong> &gt; <strong>Bot analysis</strong>.</p>
<p><img src="/assets/upstream/images/bots/bot-analytics-dashboard-biz.png" alt="View Bot Analytics in the Cloudflare dashboard. For more details, keep reading." /></p>
<h3 id="features">Features</h3>
<p>For a full tour of Bot Analytics, see <a href="https://blog.cloudflare.com/introducing-bot-analytics/">our blog post</a>. At a high level, the tool includes:</p>
<ul>
<li><strong>Requests by traffic type</strong>: View your total domain traffic segmented vertically by traffic type. Keep an eye on <em>automated</em> and <em>likely automated</em> traffic.</li>
<li><strong>Requests by detection source</strong>: Identify the most common detection engines used to score your traffic. Hover over a tooltip to learn more about each engine.</li>
<li><strong>Top requests by attribute</strong>: View more detailed information on specific IP addresses and other characteristics.</li>
</ul>
<p>Bot Analytics shows up to 72 hours of data at a time and can display data up to 30 days old. Bot Analytics displays data in real time in most cases.</p>
<p>Cloudflare uses adaptive bitrate technology to show sampled data — most customers will see a 1-10% sample depending on how much information they are trying to view. Tooltips on the page will display the current sample rate.</p>
<h3 id="common-uses">Common uses</h3>
<p>Business and Enterprise customers without Bot Management can use Bot Analytics to:</p>
<ul>
<li>Understand <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/1460.md")
</div> traffic
- Study recent attacks to find trends and detailed information
- Learn more about Cloudflare’s detection engines with real data
<p>For more details and granular control over bot traffic, consider upgrading to <a href="/bots/bot-analytics/#enterprise-bot-management">Bot Management for Enterprise</a>.</p>
<h2 id="enterprise-bot-management">Enterprise Bot Management</h2>
<p>Enterprise customers with Bot Management can use <strong>Bot Analytics</strong> to dynamically examine bot traffic.</p>
<h3 id="access-1">Access</h3>
<p>You can access Bot Analytics by going to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>, and selecting your account and domain.</p>
<p>Go to <strong>Security</strong> &gt; <strong>Analytics</strong> &gt; <strong>Bot analysis</strong>.</p>
<p><img src="/assets/upstream/images/bots/bot-analytics-dashboard-ent.png" alt="View Bot Analytics in the Cloudflare dashboard. For more details, keep reading." /></p>
<h3 id="features-1">Features</h3>
<p>For a full tour of Bot Analytics, see <a href="https://blog.cloudflare.com/introducing-bot-analytics/">our blog post</a>. At a high level, the tool includes:</p>
<ul>
<li><strong>Requests by bot score</strong>: View your total domain traffic and segment it vertically by traffic type. Keep an eye on <em>automated</em> and <em>likely automated</em> traffic.</li>
<li><strong>Bot score distribution</strong>: View the number of requests assigned a bot score 1 through 99.</li>
<li><strong>Bot score source</strong>: Identify the most common detection engines used to score your traffic. Hover over a tooltip to learn more about each engine.</li>
<li><strong>Top requests by attribute</strong>: View more detailed information on specific IP addresses and other characteristics.</li>
</ul>
<p>Bot Analytics shows up to one week of data at a time and can display data up to 30 days old. Bot Analytics displays data in real time in most cases.</p>
<p>Cloudflare uses adaptive bitrate technology to show sampled data — most customers will see a 1-10% sample depending on how much information they are trying to view. Tooltips on the page will display the current sample rate.</p>
<h3 id="common-uses-1">Common uses</h3>
<p>Bot Management customers can use Bot Analytics to:</p>
<ul>
<li>Understand traffic during <a href="/bots/get-started/bot-management/">your onboarding phase</a>.</li>
<li>Tune WAF custom rules to be effective but not overly aggressive.</li>
<li>Study recent attacks to find trends and detailed information.</li>
<li>Learn more about Cloudflare’s detection engines with real data.</li>
</ul>
<h3 id="api">API</h3>
<p>Data from Bot Analytics is also available via the GraphQL API. You can access <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1461.md")
</div>, bot sources, <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/1462.md")
</div>, and bot _decisions_ (_automated_, _likely automated_, etc.), and more.
<p>Read the <a href="/analytics/graphql-api/">GraphQL Analytics API documentation</a> for more information about GraphQL and basic querying.</p>
