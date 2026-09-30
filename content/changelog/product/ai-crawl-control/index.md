---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/ai-crawl-control/
  description: '2026-06-16'
  full_title: ai-crawl-control changelog | Cloudflare Docs
  head_html: <title>ai-crawl-control changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-16"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/ai-crawl-control/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="ai-crawl-control changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-16"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/ai-crawl-control/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/ai-crawl-control/#page","headline":"ai-crawl-control changelog | Cloudflare Docs","description":"2026-06-16","url":"https://developers.cloudflare.com/changelog/product/ai-crawl-control/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/ai-crawl-control/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="pay-per-crawl-advanced-configuration"><a href="/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/">Pay Per Crawl advanced configuration</a></h2>
<p><em>2026-06-16</em></p>
<p>You can now configure advanced Pay Per Crawl settings for your zone, including:</p>
<ul>
<li><strong>Disable Pay Per Crawl by URI pattern</strong> using <a href="/rules/configuration-rules/">Configuration Rules</a> to offer free access to specific pages while charging for others.</li>
<li><strong>Dynamic pricing</strong> by having your origin return a <code>crawler-price</code> response header, or by using a <a href="/workers/">Cloudflare Worker</a> to set prices based on request properties.</li>
</ul>
<p>When dynamic pricing is enabled, Pay Per Crawl adds a <code>cf-pay-per-crawl</code> request header to origin requests so your origin or Worker can determine the appropriate price.</p>
<p>Refer to the <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration documentation</a> for details.</p>


<h2 id="introducing-redirects-for-ai-training"><a href="/changelog/post/2026-04-17-redirects-for-ai-training/">Introducing Redirects for AI Training</a></h2>
<p><em>2026-04-17</em></p>
<p>Cloudflare's network now supports redirecting verified AI training crawlers to canonical URLs when they request deprecated or duplicate pages. When enabled via <strong>AI Crawl Control</strong> &gt; <strong>Quick Actions</strong>, AI training crawlers that request a page with a canonical tag pointing elsewhere receive a 301 redirect to the canonical version. Humans, search engine crawlers, and AI Search agents continue to see the original page normally.</p>
<p>This feature leverages your existing <code>&lt;link rel=&quot;canonical&quot;&gt;</code> tags. No additional configuration required beyond enabling the toggle. Available on Pro, Business, and Enterprise plans at no additional cost.</p>
<p>Refer to the <a href="/ai-crawl-control/reference/redirects-for-ai-training/">Redirects for AI Training documentation</a> for details.</p>


<h2 id="tools-to-prepare-your-site-for-the-agentic-internet"><a href="/changelog/post/2026-04-17-tools-for-agentic-internet/">Tools to prepare your site for the agentic Internet</a></h2>
<p><em>2026-04-17</em></p>
<p>AI Crawl Control now includes new tools to help you prepare your site for the agentic Internet—a web where AI agents are first-class citizens that discover and interact with content differently than human visitors.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-content-format-insights">Content Format insights</h4>
<p>The <strong>Metrics</strong> tab now includes a <strong>Content Format</strong> chart showing what content types AI systems request versus what your origin serves. Understanding these patterns helps you optimize content delivery for both human and agent consumption.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-directives-tab-formerly-robots-txt">Directives tab (formerly Robots.txt)</h4>
<p>The <strong>Robots.txt</strong> tab has been renamed to <strong>Directives</strong> and now includes a link to check your site's <a href="https://isitagentready.com">Agent Readiness</a> score.</p>
<p>Refer to our <a href="https://blog.cloudflare.com/agent-readiness/">blog post on preparing for the agentic Internet</a> for more on why these capabilities matter.</p>


<h2 id="advanced-waf-customization-for-ai-crawl-control-blocks"><a href="/changelog/post/2026-03-24-waf-rule-preservation/">Advanced WAF customization for AI Crawl Control blocks</a></h2>
<p><em>2026-03-24</em></p>
<p>AI Crawl Control now supports extending the underlying WAF rule with custom modifications. Any changes you make directly in the WAF custom rules editor — such as adding path-based exceptions, extra user agents, or additional expression clauses — are preserved when you update crawler actions in AI Crawl Control.</p>
<p>If the WAF rule expression has been modified in a way AI Crawl Control cannot parse, a warning banner appears on the <strong>Crawlers</strong> page with a link to view the rule directly in WAF.</p>
<p>For more information, refer to <a href="/ai-crawl-control/features/manage-ai-crawlers/#waf-rule-management">WAF rule management</a>.</p>


<h2 id="analytics-enhancements"><a href="/changelog/post/2026-02-09-analytics-enhancements/">Analytics enhancements</a></h2>
<p><em>2026-02-09</em></p>
<p>AI Crawl Control metrics have been enhanced with new views, improved filtering, and better data visualization.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-path-patterns.png" alt="AI Crawl Control path patterns" /></p>
<p><strong>Path pattern grouping</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Most popular paths</strong> table, use the new <strong>Patterns</strong> tab that groups requests by URI pattern (<code>/blog/*</code>, <code>/api/v1/*</code>, <code>/docs/*</code>) to identify which site areas crawlers target most. Refer to the screenshot above.</li>
</ul>
<p><strong>Enhanced referral analytics</strong></p>
<ul>
<li>Destination patterns show which site areas receive AI-driven referral traffic.</li>
<li>In the <strong>Metrics</strong> tab, a new <strong>Referrals over time</strong> chart shows trends by operator or source.</li>
</ul>
<p><strong>Data transfer metrics</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Allowed requests over time</strong> chart, toggle <strong>Bytes</strong> to show bandwidth consumption.</li>
<li>In the <strong>Crawlers</strong> tab, a new <strong>Bytes Transferred</strong> column shows bandwidth per crawler.</li>
</ul>
<p><strong>Image exports</strong></p>
<ul>
<li>Export charts and tables as images for reports and presentations.</li>
</ul>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a>.</p>


<h2 id="new-reference-documentation"><a href="/changelog/post/2026-02-09-reference-documentation/">New reference documentation</a></h2>
<p><em>2026-02-04</em></p>
<p>New reference documentation is now available for AI Crawl Control:</p>
<ul>
<li><strong><a href="/ai-crawl-control/reference/graphql-api/">GraphQL API reference</a></strong> — Query examples for crawler requests, top paths, referral traffic, and data transfer. Includes key filters for detection IDs, user agents, and referrer domains.</li>
<li><strong><a href="/ai-crawl-control/reference/bots/">Bot reference</a></strong> — Detection IDs and user agents for major AI crawlers from OpenAI, Anthropic, Google, Meta, and others.</li>
<li><strong><a href="/ai-crawl-control/reference/worker-templates/">Worker templates</a></strong> — Deploy the x402 Payment-Gated Proxy to monetize crawler access or charge bots while letting humans through free.</li>
</ul>


<h2 id="ai-crawl-control-read-only-role-now-available"><a href="/changelog/post/2026-01-13-ai-crawl-control-read-only-role/">AI Crawl Control Read Only role now available</a></h2>
<p><em>2026-01-13</em></p>
<p>Account administrators can now assign the <strong>AI Crawl Control Read Only</strong> role to provide read-only access to AI Crawl Control at the domain level.</p>
<p>Users with this role can view the <strong>Overview</strong>, <strong>Crawlers</strong>, <strong>Metrics</strong>, <strong>Robots.txt</strong>, and <strong>Settings</strong> tabs but cannot modify crawler actions or settings.</p>
<p>This role is specific for AI Crawl Control. You still require correct permissions to access other areas / features of the dashboard.</p>
<p>To assign, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> and add a policy with the <strong>AI Crawl Control Read Only</strong> role scoped to the desired domain.</p>


<h2 id="new-ai-crawl-control-overview-tab"><a href="/changelog/post/2025-12-18-overview-tab/">New AI Crawl Control Overview tab</a></h2>
<p><em>2025-12-18</em></p>
<p>The <strong>Overview</strong> tab is now the default view in AI Crawl Control. The previous default view with controls for individual AI crawlers is available in the <strong>Crawlers</strong> tab.</p>
<h4 id="2025-12-18-overview-tab-what-s-new">What's new</h4>
<ul>
<li><strong>Executive summary</strong> — Monitor total requests, volume change, most common status code, most popular path, and high-volume activity</li>
<li><strong>Operator grouping</strong> — Track crawlers by their operating companies (OpenAI, Microsoft, Google, ByteDance, Anthropic, Meta)</li>
<li><strong>Customizable filters</strong> — Filter your snapshot by date range, crawler, operator, hostname, or path</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview-tab.png" alt="AI Crawl Control Overview tab showing executive summary, metrics, and crawler groups" /></p>
<h4 id="2025-12-18-overview-tab-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong>, where the <strong>Overview</strong> tab opens by default with your activity snapshot.</li>
<li>Use filters to customize your view by date range, crawler, operator, hostname, or path.</li>
<li>Navigate to the <strong>Crawlers</strong> tab to manage controls for individual crawlers.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a> and <a href="/ai-crawl-control/features/manage-ai-crawlers/">managing AI crawlers</a>.</p>


<h2 id="pay-per-crawl-private-beta-discovery-api-custom-pricing-and-advanced-configuration"><a href="/changelog/post/2025-12-10-pay-per-crawl-enhancements/">Pay Per Crawl (Private beta) - Discovery API, custom pricing, and advanced configuration</a></h2>
<p><em>2025-12-10</em></p>
<p>Pay Per Crawl is introducing enhancements for both AI crawler operators and site owners, focusing on programmatic discovery, flexible pricing models, and granular configuration control.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-ai-crawler-operators">For AI crawler operators</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-discovery-api">Discovery API</h4>
<p>A new authenticated API endpoint allows verified crawlers to programmatically discover domains participating in Pay Per Crawl. Crawlers can use this to build optimized crawl queues, cache domain lists, and identify new participating sites. This eliminates the need to discover payable content through trial requests.</p>
<p>The API endpoint is <code>GET https://crawlers-api.ai-audit.cfdata.org/charged_zones</code> and requires Web Bot Auth authentication. Refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> for authentication steps, request parameters, and response schema.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-payment-header-signature-requirement">Payment header signature requirement</h4>
<p>Payment headers (<code>crawler-exact-price</code> or <code>crawler-max-price</code>) must now be included in the Web Bot Auth <code>signature-input</code> header components. This security enhancement prevents payment header tampering, ensures authenticated payment intent, validates crawler identity with payment commitment, and protects against replay attacks with modified pricing. Crawlers must add their payment header to the list of signed components when <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#22-sign-your-request-with-web-bot-auth">constructing the signature-input header</a>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-new-crawler-error-header">New <code>crawler-error</code> header</h4>
<p>Pay Per Crawl error responses now include a new <code>crawler-error</code> header with 11 specific <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/">error codes</a> for programmatic handling. Error response bodies remain unchanged for compatibility. These codes enable robust error handling, automated retry logic, and accurate spending tracking.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-site-owners">For site owners</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-configure-free-pages">Configure free pages</h4>
<p>Site owners can now offer free access to specific pages like homepages, navigation, or discovery pages while charging for other content. Create a <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/#disable-pay-per-crawl-by-uri-pattern">Configuration Rule</a> in <strong>Rules</strong> &gt; <strong>Configuration Rules</strong>, set your URI pattern using wildcard, exact, or prefix matching on the <strong>URI Full</strong> field, and enable the <strong>Disable Pay Per Crawl</strong> setting. When disabled for a URI pattern, crawler requests pass through without blocking or charging.</p>
<p>Some paths are always free to crawl. These paths are: <code>/robots.txt</code>, <code>/sitemap.xml</code>, <code>/security.txt</code>, <code>/.well-known/security.txt</code>, <code>/crawlers.json</code>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-get-started">Get started</h4>
<p><strong>AI crawler operators</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> | <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/">Crawl pages</a></p>
<p><strong>Site owners</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration</a></p>


<h2 id="crawler-drilldowns-with-extended-actions-menu"><a href="/changelog/post/2025-11-10-ai-crawl-control-crawler-info/">Crawler drilldowns with extended actions menu</a></h2>
<p><em>2025-11-10</em></p>
<p>AI Crawl Control now supports per-crawler drilldowns with an extended actions menu and status code analytics. Drill down into Metrics, Cloudflare Radar, and Security Analytics, or export crawler data for use in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/url-forwarding/">Redirect Rules</a>, and robots.txt files.</p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-what-s-new">What's new</h4>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-status-code-distribution-chart">Status code distribution chart</h4>
<p>The <strong>Metrics</strong> tab includes a status code distribution chart showing HTTP response codes (2xx, 3xx, 4xx, 5xx) over time. Filter by individual crawler, category, operator, or time range to analyze how specific crawlers interact with your site.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-status-codes.png" alt="AI Crawl Control status code distribution chart" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-extended-actions-menu">Extended actions menu</h4>
<p>Each crawler row includes a three-dot menu with per-crawler actions:</p>
<ul>
<li><strong>View Metrics</strong> — Filter the AI Crawl Control Metrics page to the selected crawler.</li>
<li><strong>View on Cloudflare Radar</strong> — Access verified crawler details on Cloudflare Radar.</li>
<li><strong>Copy User Agent</strong> — Copy user agent strings for use in WAF custom rules, Redirect Rules, or robots.txt files.</li>
<li><strong>View in Security Analytics</strong> — Filter Security Analytics by detection IDs (Bot Management customers).</li>
<li><strong>Copy Detection ID</strong> — Copy detection IDs for use in WAF custom rules (Bot Management customers).</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-crawler-info.png" alt="AI Crawl Control crawler actions menu" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong> to access the status code distribution chart.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Crawlers</strong> and select the three-dot menu for any crawler to access per-crawler actions.</li>
<li>Select multiple crawlers to use bulk copy buttons for user agents or detection IDs.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/">AI Crawl Control</a>.</p>


<h2 id="new-robots-txt-tab-for-tracking-crawler-compliance"><a href="/changelog/post/2025-10-21-track-robots-txt/">New Robots.txt tab for tracking crawler compliance</a></h2>
<p><em>2025-10-21</em></p>
<p>AI Crawl Control now includes a <strong>Robots.txt</strong> tab that provides insights into how AI crawlers interact with your <code>robots.txt</code> files.</p>
<h4 id="2025-10-21-track-robots-txt-what-s-new">What's new</h4>
<p>The Robots.txt tab allows you to:</p>
<ul>
<li>Monitor the health status of <code>robots.txt</code> files across all your hostnames, including HTTP status codes, and identify hostnames that need a <code>robots.txt</code> file.</li>
<li>Track the total number of requests to each <code>robots.txt</code> file, with breakdowns of successful versus unsuccessful requests.</li>
<li>Check whether your <code>robots.txt</code> files contain <a href="https://contentsignals.org/">Content Signals</a> directives for AI training, search, and AI input.</li>
<li>Identify crawlers that request paths explicitly disallowed by your <code>robots.txt</code> directives, including the crawler name, operator, violated path, specific directive, and violation count.</li>
<li>Filter <code>robots.txt</code> request data by crawler, operator, category, and custom time ranges.</li>
</ul>
<h4 id="2025-10-21-track-robots-txt-take-action">Take action</h4>
<p>When you identify non-compliant crawlers, you can:</p>
<ul>
<li>Block the crawler in the <a href="/ai-crawl-control/features/manage-ai-crawlers/">Crawlers tab</a></li>
<li>Create custom <a href="/waf/">WAF rules</a> for path-specific security</li>
<li>Use <a href="/rules/url-forwarding/">Redirect Rules</a> to guide crawlers to appropriate areas of your site</li>
</ul>
<p>To get started, go to <strong>AI Crawl Control</strong> &gt; <strong>Robots.txt</strong> in the Cloudflare dashboard. Learn more in the <a href="/ai-crawl-control/features/track-robots-txt/">Track robots.txt documentation</a>.</p>


<h2 id="enhanced-ai-crawl-control-metrics-with-new-drilldowns-and-filters"><a href="/changelog/post/2025-10-14-enhanced-metrics-drilldowns/">Enhanced AI Crawl Control metrics with new drilldowns and filters</a></h2>
<p><em>2025-10-14</em></p>
<p>AI Crawl Control now provides enhanced metrics and CSV data exports to help you better understand AI crawler activity across your sites.</p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-what-s-new">What's new</h4>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-track-crawler-requests-over-time">Track crawler requests over time</h4>
<p>Visualize crawler activity patterns over time, and group data by different dimensions:</p>
<ul>
<li><strong>By Crawler</strong> — Track activity from individual AI crawlers (GPTBot, ClaudeBot, Bytespider)</li>
<li><strong>By Category</strong> — Analyze crawler purpose or type</li>
<li><strong>By Operator</strong> — Discover which companies (OpenAI, Anthropic, ByteDance) are crawling your site</li>
<li><strong>By Host</strong> — Break down activity across multiple subdomains</li>
<li><strong>By Status Code</strong> — Monitor HTTP response codes to crawlers (200s, 300s, 400s, 500s)</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-requests-over-time.png" alt="AI Crawl Control requests over time chart with grouping tabs" title="Interactive chart showing crawler requests over time with filterable dimensions" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-analyze-referrer-data-paid-plans">Analyze referrer data (Paid plans)</h4>
<p>Identify traffic sources with referrer analytics:</p>
<ul>
<li>View top referrers driving traffic to your site</li>
<li>Understand discovery patterns and content popularity from AI operators</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-top-referrers.png" alt="AI Crawl Control top referrers breakdown" title="Bar chart showing top referrers and their respective traffic volumes" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-export-data">Export data</h4>
<p>Download your filtered view as a CSV:</p>
<ul>
<li>Includes all applied filters and groupings</li>
<li>Useful for custom reporting and deeper analysis</li>
</ul>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong>.</li>
<li>Use the grouping tabs to explore different views of your data.</li>
<li>Apply filters to focus on specific crawlers, time ranges, or response codes.</li>
<li>Select <strong>Download CSV</strong> to export your filtered data for further analysis.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control">AI Crawl Control</a>.</p>


<h2 id="enhanced-crawler-insights-and-custom-402-responses"><a href="/changelog/post/2025-08-27-ai-crawl-control-launch/">Enhanced crawler insights and custom 402 responses</a></h2>
<p><em>2025-08-27</em></p>
<p>We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.</p>
<p><strong>Enhanced Crawlers tab:</strong></p>
<ul>
<li>View total allowed and blocked requests for each AI crawler</li>
<li>Trend charts show crawler activity over your selected time range per crawler</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-table.png" alt="Updated AI Crawl Control table showing request counts and trend charts" /></p>
<p><strong>Custom block responses (paid plans):</strong>
You can now return HTTP 402 &quot;Payment Required&quot; responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.</p>
<p>For users on paid plans, when blocking AI crawlers you can configure:</p>
<ul>
<li><strong>Response code:</strong> Choose between 403 Forbidden or 402 Payment Required</li>
<li><strong>Response body:</strong> Add a custom message with your licensing contact information</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-block-response.png" alt="AI Crawl Control block response configuration interface" /></p>
<p>Example 402 response:</p>
<pre tabindex="0"><code class="language-http">HTTP 402 Payment Required&#10;Date: Mon, 24 Aug 2025 12:56:49 GMT&#10;Content-type: application/json&#10;Server: cloudflare&#10;Cf-Ray: 967e8da599d0c3fa-EWR&#10;Cf-Team: 2902f6db750000c3fa1e2ef400000001&#10;&#10;{&#10;  &quot;message&quot;: &quot;Please contact the site owner for access.&quot;&#10;}&#10;</code></pre>


<h2 id="introducing-pay-per-crawl-private-beta"><a href="/changelog/post/2025-07-01-pay-per-crawl/">Introducing Pay Per Crawl (private beta)</a></h2>
<p><em>2025-07-01</em></p>
<p>We are introducing a new feature of <a href="/ai-crawl-control/">AI Crawl Control</a> — Pay Per Crawl. <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl</a> enables site owners to require payment from AI crawlers every time the crawlers access their content, thereby fostering a fairer Internet by enabling site owners to control and monetize how their content gets used by AI.</p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/pay-per-crawl.png" alt="Pay per crawl" /></p>
<p><strong>For Site Owners:</strong></p>
<ul>
<li>Set pricing and select which crawlers to charge for content access</li>
<li>Manage payments via Stripe</li>
<li>Monitor analytics on successful content deliveries</li>
</ul>
<p><strong>For AI Crawler Owners:</strong></p>
<ul>
<li>Use HTTP headers to request and accept pricing</li>
<li>Receive clear confirmations on charges for accessed content</li>
</ul>
<p>Learn more in the <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl documentation</a>.</p>


<h2 id="ai-crawl-control-refresh"><a href="/changelog/post/2025-07-01-refresh/">AI Crawl Control refresh</a></h2>
<p><em>2025-07-01</em></p>
<p>We redesigned the AI Crawl Control dashboard to provide more intuitive and granular control over AI crawlers.</p>
<ul>
<li>From the new <strong>AI Crawlers</strong> tab: block specific AI crawlers.</li>
<li>From the new <strong>Metrics</strong> tab: view AI Crawl Control metrics.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/manage-ai-crawlers.png" alt="Block AI crawlers" /></p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/analyze-metrics.png" alt="Analyze AI crawler activity" /></p>
<p>To get started, explore:</p>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a>.</li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a>.</li>
</ul>


<h2 id="ai-crawl-control"><a href="/changelog/post/2024-09-23-ai-audit-launch/">AI Crawl Control</a></h2>
<p><em>2024-09-23</em></p>
<p>Every site on Cloudflare now has access to <a href="/ai-crawl-control/"><strong>AI Audit</strong></a>, which summarizes the crawling behavior of popular and known AI services.</p>
<p>You can use this data to:</p>
<ul>
<li>Understand how and how often crawlers access your site (and which content is the most popular).</li>
<li>Block specific AI bots accessing your site.</li>
<li>Use Cloudflare to enforce your <code>robots.txt</code> policy via an automatic WAF rule.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview.png" alt="View AI bot activity with AI Audit" /></p>
<p>To get started, explore <a href="/ai-crawl-control/">AI audit</a>.</p>



