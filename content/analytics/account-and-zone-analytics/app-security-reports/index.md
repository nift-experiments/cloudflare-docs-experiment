<p>Application Security reports provide cyber attack insights and trends for all of the Enterprise zones in your Cloudflare account.</p>
<p>The reports are automatically generated on a monthly basis.</p>
<p>You can access reports by going to the <strong>Security reports</strong> page or via the <a href="#api">API</a>. You can access reports from previous months by selecting the month from the dropdown.</p>
<div class="nb-dash-button"></div>
<p>To download the report, select <strong>Print report</strong>.</p>
<p>Reports from before April 2025 can be accessed through <strong>Security reports</strong> &gt; <strong>Legacy reports</strong>. Due to limitations in the legacy reports, some customers may not have reports for every month prior to April 2025.</p>
<p>The current reports are curated by Cloudflare and will be expanded to include more insights. The option to create custom reports, filter by various fields, and schedule reports will be added in upcoming improvements.</p>
<hr />
<h2 id="report-types">Report types</h2>
<p>Currently, only Application Security reports are available. They cover the entire suite of products such as <a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Protection</a>, <a href="/waf/">WAF</a>, and <a href="/bots/">Bot Management</a>.</p>
<p>Reports for Application Performance, <a href="/cloudflare-one/">Cloudflare One</a>, and Network Services, such as <a href="/magic-transit/">Magic Transit</a>, will be made available in future improvements.</p>
<hr />
<h2 id="report-layout">Report layout</h2>
<p>Each report includes the following sections:</p>
<ul>
<li>Executive summary</li>
<li>Distribution of allowed and mitigated requests</li>
<li><a href="#industry-benchmarks">Industry benchmarks</a> that show how you compare to your peers by selecting your industry</li>
<li>Top five source countries of allowed traffic and mitigated traffic including a map visualization</li>
<li>Top five most targeted hostnames</li>
<li>Top five most effective mitigation rules</li>
</ul>
<p>To view more details, apply filters, analyze the data, and generate ad-hoc reports, use the <a href="/waf/analytics/security-analytics/">Security Analytics dashboard</a> or <a href="/log-explorer/">Log Explorer</a>.</p>
<h3 id="industry-benchmarks">Industry benchmarks</h3>
<p>Industry benchmarks provide additional context for your mitigated traffic by comparing your organization's attack activity against others in the same industry. These benchmarks help you understand whether the volume and frequency of attacks you experience are typical, higher, or lower than your peers — offering a clear sense of where your organization stands within its threat landscape.</p>
<p>Beyond providing context, benchmarks can also help demonstrate value to stakeholders by quantifying the scale of threats your organization faces and how effectively Cloudflare mitigates them. This information can be useful when communicating your security posture internally or when prioritizing future security investments.</p>
<p>To ensure fairness and accuracy, Cloudflare normalizes your data before comparison. For each month, we calculate the percentage of mitigated requests relative to the total requests across your account and eligible zones. This normalization ensures that benchmarks are based on relative attack intensity rather than total traffic volume so larger or smaller organizations can be compared meaningfully.</p>
<p>The result helps you interpret your mitigated traffic data in context. For example, you may see a statement such as &quot;<em>You are in the top 25% most attacked companies in the Cosmetics industry.</em>&quot; This insight enables you to better understand your threat exposure, communicate results to stakeholders, and understand value of the protection Cloudflare provides.</p>
<p>If your account is not assigned an industry or if the shown industry is incorrect, use the link within the report to select the correct industry.</p>
<p>It may take a while for your new selection to take effect, and it may only be applied to future reports.</p>
<p>If you have multiple Cloudflare accounts, select the industry that is most relevant for the specific account.</p>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<p>You must have at least one Enterprise zone. Application Security reports are automatically enabled on your Enterprise zone. No action is required.</p>
<p>If you do not have any Enterprise zones, a report will not be generated. If you have an account that is not older than one month, a report will not be generated yet.</p>
<h3 id="required-roles">Required roles</h3>
<p>A Cloudflare user must have one of the following <a href="/fundamentals/manage-members/roles/">roles</a> to download Application Security reports:</p>
<ul>
<li>Super Administrator</li>
<li>Administrator</li>
</ul>
<hr />
<h2 id="api">API</h2>
<pre><code class="language-sh">GET /accounts/{account_id}/reporting/policies&#10;</code></pre>
<pre><code class="language-sh">GET /accounts/{account_id}/reporting/policies/{policy_id}&#10;</code></pre>
<pre><code class="language-sh">GET /accounts/{account_id}/reporting/reports&#10;</code></pre>
<pre><code class="language-sh">GET /accounts/{account_id}/reporting/reports/{report_id}&#10;</code></pre>
<details class="nb-details"><summary>Data returned by the API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3148.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3147.md")
</aside>
<h3 id="cross-account-reports">Cross-account reports</h3>
<p>Each report is generated per account. You can use the <a href="#api">API</a> to retrieve the reports for all of your accounts and aggregate the data.</p>
<hr />
<h2 id="availability">Availability</h2>
<p>This feature is available in closed beta to Enterprise customers.</p>
