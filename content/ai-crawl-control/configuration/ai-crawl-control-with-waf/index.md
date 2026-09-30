<p>AI Crawl Control works alongside other Cloudflare products, such as Cloudflare <a href="/waf/">Web Application Firewall (WAF)</a>. WAF checks incoming web and API requests, and filters undesired traffic based on rules. <a href="/waf/custom-rules/">WAF custom rules</a> allow you to perform certain actions such as enforcing <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/2749.md")
</div>.
<h2 id="order-of-precedence">Order of precedence</h2>
<ul>
<li>AI Crawl Control uses WAF custom rules to block the selection of AI crawlers the site owner has decided to block.</li>
<li>AI Crawl Control's pay per crawl feature takes place after WAF.</li>
</ul>
<pre><code class="language-mermaid">graph LR&#10;A[Traffic] --&gt; B[WAF custom rules&lt;br&gt;AI Crawl Control: Crawler blocks]&#10;B --&gt; C[Cloudflare&lt;br&gt;Bot Solutions]&#10;C --&gt; D[AI Crawl Control:&lt;br&gt;Pay Per Crawl]&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>For this reason, if you plan on using AI Crawl Control to manage AI crawlers, you may wish to modify your existing WAF custom rules such that it does not affect AI crawlers. This will allow you to manage AI crawlers only from AI Crawl Control, thereby streamlining your workflow.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="how-ai-crawl-control-uses-waf-custom-rules">How AI Crawl Control uses WAF custom rules</h3>
@markup("md", "content/.markup/bodies/2748.md")
</aside>
<h2 id="examples-of-using-waf-vs-ai-crawl-control">Examples of using WAF vs AI Crawl Control</h2>
<p>Consider the following examples.</p>
<h3 id="traffic-from-a-restricted-country-vs-pay-per-crawl">Traffic from a restricted country vs pay per crawl</h3>
<p>You may have both of the following features enabled:</p>
<ul>
<li><a href="/waf/custom-rules/use-cases/block-traffic-from-specific-countries/">WAF custom rule to block traffic from specific countries</a></li>
<li>AI Crawl Control's <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">pay per crawl</a> to charge AI crawlers when they request access to your content</li>
</ul>
<p>Since WAF custom rules are enforced before pay per crawl, traffic (including AI crawlers) from your blocked countries will continue to be blocked, even if they provide the <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#1-identify-payment-requirements">required headers</a> for pay per crawl.</p>
<h3 id="allowed-search-engine-bots-via-waf-custom-rule-vs-pay-per-crawl">Allowed search engine bots via WAF custom rule vs pay per crawl</h3>
<p>You may have both of the following features enabled:</p>
<ul>
<li><a href="/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/">WAF custom rule to allow search engine bots</a></li>
<li>AI Crawl Control's <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">pay per crawl</a> to charge all AI crawlers when they request access to your content (including search engine bots).</li>
</ul>
<p>Since custom rules are enforced before pay per crawl:</p>
<ul>
<li>Only search engine bots will be able to access your site (enforced by custom rule).</li>
<li>The search engine bots will then be charged for access to your content (enforced by AI Crawl Control's pay per crawl).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2747.md")
</aside>
<h3 id="troubleshoot-allowed-bots">Troubleshoot allowed bots</h3>
<p>If you have set certain AI crawlers to <strong>Allow</strong> in AI Crawl Control, but they are still being blocked, check for upstream WAF custom rules that may be blocking them. Since the AI Crawl Control rule only includes blocked bots, allowed bots may still be affected by other security rules that execute before the AI Crawl Control rule.</p>
<p>These upstream rules will affect traffic but may not be visible in AI Crawl Control analytics. Review your WAF custom rules to identify and modify any rules that may be blocking AI crawlers you intend to allow.</p>
<h3 id="troubleshoot-blocked-bots">Troubleshoot blocked bots</h3>
<p>If you have set certain AI crawlers to <strong>Block</strong> in AI Crawl Control, but they are still accessing your content, check for upstream rules that may be bypassing the AI Crawl Control rule. Since the AI Crawl Control rule is added at the end of existing WAF custom rules, the following types of rules may allow bots to bypass the block:</p>
<ul>
<li><strong>Skip rules</strong> that bypass WAF custom rules</li>
<li><strong>Redirect rules</strong> that change the request path</li>
<li><strong>Transform rules</strong> that modify the request</li>
</ul>
<p>To ensure blocked bots are properly blocked, move the AI Crawl Control rule to the top of your WAF custom rules, so it executes before other rules.</p>
<h3 id="conflict-in-ai-crawler-blocking-logic">Conflict in AI crawler blocking logic</h3>
<p>You may have both of the following features enabled:</p>
<ul>
<li>A WAF custom rule which blocks all bots.</li>
<li>AI Crawl Control selection which allows certain AI crawlers.</li>
</ul>
<p>In this scenario, you have two custom rules, each directing a different logic for handling AI crawlers. To resolve this issue:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2750.md")
</div>
<h2 id="extending-the-ai-crawl-control-waf-rule">Extending the AI Crawl Control WAF rule</h2>
<p>For most use cases, managing crawlers directly in AI Crawl Control is recommended. However, the underlying WAF rule supports additional customization for scenarios the dashboard does not cover.</p>
<p>The AI Crawl Control rule is named <strong>AI Crawl Control</strong> and can be found under <strong>Security</strong> &gt; <strong>Security rules</strong>. Filter by <strong>Custom rules</strong> to find it.</p>
<p>Common additions include:</p>
<ul>
<li>Path-based exceptions, such as allowing a blocked crawler to access specific sections of your site by adding an <code>AND</code> clause that excludes certain paths</li>
<li>Extra user agents or detection IDs for crawlers not listed in AI Crawl Control</li>
<li>Additional expression clauses to restrict blocking to specific hostnames or other request properties</li>
</ul>
<p>Any additions you make are preserved when you subsequently update crawler actions in AI Crawl Control. If the expression has been modified in a way AI Crawl Control cannot parse, a warning banner will appear on the <strong>Crawlers</strong> page. Select <strong>View rule in WAF</strong> in the banner to inspect or correct the rule.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2746.md")
</aside>
