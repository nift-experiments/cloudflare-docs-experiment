<p>AI Crawl Control enables you to take specific action for each AI crawler.</p>
<p>To manage AI crawlers:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Go to the <strong>Security</strong> tab.</li>
</ol>
<h2 id="review-ai-crawler-activity">Review AI crawler activity</h2>
<p>The <strong>Crawlers</strong> tab displays a table of AI crawlers that are requesting access to your content, and how they interact with your pages. The table provides the following information.</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>Crawler</td>
<td>The name of the AI crawler and the operator that owns it.</td>
</tr>
<tr>
<td>Category</td>
<td>The category of the AI crawler. Refer to <a href="/bots/concepts/bot/verified-bots/#legacy-categories">Verified bot categories</a>.</td>
</tr>
<tr>
<td>Requests</td>
<td>The total number of allowed and unsuccessful requests, with trend chart. Unsuccessful requests may come from any rule or response error, not just the block action in AI Crawl Control.</td>
</tr>
<tr>
<td>Robots.txt violations</td>
<td>The number of times the AI crawler has violated your <span class="nb-interactive-component" data-cf-component="GlossaryTooltip"></td>
</tr>
</tbody>
</table>
@markup("md", "content/.markup/bodies/2734.md")
</div> file.                                                               |
| Action                | The action you wish to take for the AI crawler. Refer to [Take action for each AI crawler](/ai-crawl-control/features/manage-ai-crawlers/#take-action-for-each-ai-crawler).                |
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="quality-of-ai-crawler-detection">Quality of AI crawler detection</h3>
@markup("md", "content/.markup/bodies/2733.md")
</aside>
<h3 id="filter-ai-crawler-data">Filter AI crawler data</h3>
<p>You can use filters to narrow the scope of your result:</p>
<ul>
<li><strong>Name:</strong> Search the name of the AI crawler.</li>
<li><strong>Operator:</strong> Filter by the AI crawler operator.</li>
<li><strong>Category:</strong> Filter by the category of the AI crawler (for example, AI crawler, AI assistant, or archiver).</li>
</ul>
<p>The values of the table will update according to your filter.</p>
<h2 id="take-action-for-each-ai-crawler">Take action for each AI crawler</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2742.md")
</div></div>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="need-more-advanced-control">Need more advanced control?</h3>
@markup("md", "content/.markup/bodies/2731.md")
</aside>
<h2 id="waf-rule-management">WAF rule management</h2>
<p>When you block a crawler in AI Crawl Control, the system creates or updates a WAF custom rule on your zone to enforce that block. For advanced scenarios such as adding path-based exceptions or extra user agents, you can extend this rule directly in WAF.</p>
<p>For more information, refer to <a href="/ai-crawl-control/configuration/ai-crawl-control-with-waf/">AI Crawl Control with Cloudflare WAF</a>.</p>
<h2 id="configure-block-response">Configure block response</h2>
<div class="nb-plan">
<p>Available on Paid plans</p>
</div>
<p>When blocking an AI crawler, you can configure the details of the response that gets returned to the AI crawler. Specifically, you can configure:</p>
<ul>
<li>The response code</li>
<li>The response body</li>
</ul>
<p>This provides you with a channel to open dialogue with the AI crawler owner, and to inform the AI crawler how to properly license their content, thereby creating a direct path from crawling attempt to commercial agreement.</p>
<p>To edit these values:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2743.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2730.md")
</aside>
<h3 id="edit-the-response-code">Edit the response code</h3>
<p>You can choose which HTTP response code to return when blocking an AI crawler.</p>
<p>Use the dropdown menu to select the desired response code. You can choose from:</p>
<ul>
<li><code>403 Forbidden</code>: Use this option if you wish to indicate that you do not want the AI crawler to access your content.</li>
<li><code>402 Payment Required</code>: Use this option if you wish to indicate that the AI crawler must pay to access your content.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2729.md")
</aside>
<h3 id="edit-the-response-body">Edit the response body</h3>
<p>You can write a custom message (HTTP response body) to return when blocking an AI crawler.</p>
<p>In the <strong>Response body</strong> text field, enter the response you wish to display for the AI crawler in plain text.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Use <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">pay per crawl</a> to charge AI crawlers every time they access your content.</li>
<li>Learn how AI Crawl Control interacts with WAF, including advanced rule customization, in <a href="/ai-crawl-control/configuration/ai-crawl-control-with-waf/">AI Crawl Control with Cloudflare WAF</a>.</li>
</ul>
