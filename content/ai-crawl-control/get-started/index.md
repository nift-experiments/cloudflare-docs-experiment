<p>This guide instructs you on how to:</p>
<ul>
<li>View AI crawlers that are interacting with pages in your domain (a <a href="/fundamentals/concepts/accounts-and-zones/#zones">Cloudflare zone</a>).</li>
<li>Use AI Crawl Control to block individual crawlers from accessing your content.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/">Cloudflare account</a>.</li>
<li><a href="/fundamentals/manage-domains/add-site/">Connect your domain to Cloudflare</a>.</li>
<li>Make sure your domain is <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">proxying traffic through Cloudflare</a>.</li>
</ol>
<h2 id="1-monitor-ai-crawler-activity-at-a-glance"><ol>
<li>Monitor AI crawler activity at a glance</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1608.md")
</div>
<h2 id="2-block-specific-ai-crawlers"><ol start="2">
<li>Block specific AI crawlers</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="plans"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1613.md")
</div></div>
<p>For more information, refer to <a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a>.</p>
<p>You can also create more complex rules when taking action on AI crawlers, using <a href="/waf/">Cloudflare WAF</a>. For more information on creating more specific rules, refer to <a href="/waf/custom-rules/create-dashboard/">Create a custom rule in the dashboard</a>.</p>
<h2 id="3-explore-detailed-metrics"><ol start="3">
<li>Explore detailed metrics</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1616.md")
</div></div>
<p>Note that on free plans, the <strong>Metrics</strong> tab only displays metrics for the past 24 hours.</p>
<h2 id="plan-comparison">Plan comparison</h2>
<table>
<thead>
<tr>
<th>All plans</th>
<th>Enterprise plans with Bot Management</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI crawler detection via <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent">user agent strings</a></td>
<td>Advanced AI crawler detection via <a href="/bots/reference/bot-management-variables/#ruleset-engine-fields">Bot Management detection ID</a></td>
</tr>
<tr>
<td>Maximum 24-hour analytics window</td>
<td>Configurable analytics timeframes</td>
</tr>
<tr>
<td>Allow/block controls</td>
<td>Allow/block controls, and the ability to charge AI crawlers using <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">pay per crawl</a></td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a> with granular allow/block controls.</li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a> to understand crawler patterns and content popularity.</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Explore pay per crawl</a> to test content monetization options (private beta).</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<p>Refer to the following related resources:</p>
<ul>
<li>Cloudflare blog: <a href="https://blog.cloudflare.com/nl-nl/cloudflare-ai-audit-control-ai-content-crawlers/">Start auditing and controlling the AI models accessing your content</a></li>
<li>Block AI crawlers that do not adhere to recommended guidelines using <a href="/bots/additional-configurations/ai-labyrinth/">Cloudflare AI Labyrinth</a>.</li>
<li><a href="/bots/additional-configurations/managed-robots-txt/">Direct AI crawlers with managed robots.txt</a>.</li>
</ul>
