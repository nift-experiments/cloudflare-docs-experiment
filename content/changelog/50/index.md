<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2024-09-23">Sep 23, 2024</time><div>
<h2 id="post-2024-09-23-ai-audit-launch"><a href="/changelog/post/2024-09-23-ai-audit-launch/">AI Crawl Control</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>Every site on Cloudflare now has access to <a href="/ai-crawl-control/"><strong>AI Audit</strong></a>, which summarizes the crawling behavior of popular and known AI services.</p>
<p>You can use this data to:</p>
<ul>
<li>Understand how and how often crawlers access your site (and which content is the most popular).</li>
<li>Block specific AI bots accessing your site.</li>
<li>Use Cloudflare to enforce your <code>robots.txt</code> policy via an automatic WAF rule.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview.png" alt="View AI bot activity with AI Audit" /></p>
<p>To get started, explore <a href="/ai-crawl-control/">AI audit</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-09-05">Sep 5, 2024</time><div>
<h2 id="post-2024-09-05-cache-rules-templates"><a href="/changelog/post/2024-09-05-cache-rules-templates/">One-click Cache Rules templates now available</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now create optimized cache rules instantly with <strong>one-click templates</strong>, eliminating the complexity of manual rule configuration.</p>
<h4 id="2024-09-05-cache-rules-templates-how-it-works">How it works</h4>
<ol>
<li>Navigate to <strong>Rules</strong> &gt; <strong>Templates</strong> in your Cloudflare dashboard.</li>
<li>Select a template for your use case.</li>
<li>Click to apply the template with sensible defaults.</li>
<li>Customize as needed for your specific requirements.</li>
</ol>
<h4 id="2024-09-05-cache-rules-templates-available-cache-templates">Available cache templates</h4>
<ul>
<li><strong>Cache everything</strong>: Adjust the cache level for all requests.</li>
<li><strong>Bypass cache for everything</strong>: Bypass cache for all requests.</li>
<li><strong>Cache default file extensions</strong>: Replicate Page Rules caching behavior by making only default extensions eligible for cache.</li>
<li><strong>Bypass cache on cookie</strong>: Bypass cache for requests containing specific cookies.</li>
<li><strong>Set edge cache time</strong>: Cache responses with status code between 200 and 599 on the Cloudflare edge.</li>
<li><strong>Set browser cache time</strong>: Adjust how long a browser should cache a resource.</li>
</ul>
<h4 id="2024-09-05-cache-rules-templates-get-started">Get started</h4>
<p>To get started, go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules"><strong>Rules &gt; Templates</strong></a> in the dashboard. For more information, refer to the <a href="/cache/how-to/cache-rules/">Cache Rules documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-09-05">Sep 5, 2024</time><div>
<h2 id="post-2024-09-05-rules-templates"><a href="/changelog/post/2024-09-05-rules-templates/">New Rules Templates for One-Click Rule Creation</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Now, you can create <strong>common rule configurations</strong> in just <strong>one click</strong> using Rules Templates.</p>
<p><img src="/assets/upstream/images/changelog/rules/rules-templates.gif" alt="Rules Templates" /></p>
<p>What you can do:</p>
<ul>
<li><strong>Pick a pre-built rule</strong> – Choose from a library of templates.</li>
<li><strong>One-click setup</strong> – Deploy best practices instantly.</li>
<li><strong>Customize as needed</strong> – Adjust templates to fit your setup.</li>
</ul>
<p>Template cards are now also available directly in the rule builder for each product.</p>
<p>Need more ideas? Check out the <a href="/rules/examples/">Examples gallery</a> in our documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-07-19">Jul 19, 2024</time><div>
<h2 id="post-2024-07-19-regionalized-generic-tiered-cache"><a href="/changelog/post/2024-07-19-regionalized-generic-tiered-cache/">Regionalized Generic Tiered Cache for higher hit ratios</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache hit ratios with <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a>. Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.</p>
<h4 id="2024-07-19-regionalized-generic-tiered-cache-how-it-works">How it works</h4>
<p>Regional content hashing groups data centers by region and uses consistent hashing to route content to designated upper-tier caches:</p>
<ul>
<li>Same content always routes to the same upper-tier data center within a region.</li>
<li>Eliminates redundant copies across multiple upper-tier caches.</li>
<li>Increases the likelihood of cache HITs for the same content.</li>
</ul>
<h4 id="2024-07-19-regionalized-generic-tiered-cache-example">Example</h4>
<p>A popular image requested from multiple edge locations in a region:</p>
<ul>
<li><strong>Before</strong>: Cached at 3-4 different upper-tier data centers</li>
<li><strong>After</strong>: Cached at 1 designated upper-tier data center</li>
<li><strong>Result</strong>: 3-4x fewer cache MISSes, reducing origin load and improving performance</li>
</ul>
<h4 id="2024-07-19-regionalized-generic-tiered-cache-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a> on your zone.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-06-17">Jun 17, 2024</time><div>
<h2 id="post-2024-06-17-okta-risk-exchange"><a href="/changelog/post/2024-06-17-okta-risk-exchange/">Exchange user risk scores with Okta</a></h2>
<div class="changelog-badges"><span>risk-score</span></div><div class="changelog-body"><p>Beyond the controls in <a href="/cloudflare-one/">Zero Trust</a>, you can now <a href="/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta">exchange user risk scores</a> with Okta to inform SSO-level policies.</p>
<p>First, configure Cloudflare One to send user risk scores to Okta.</p>
<ol>
<li>Set up the <a href="/cloudflare-one/integrations/identity-providers/okta/">Okta SSO integration</a>.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>In <strong>Your identity providers</strong>, locate your Okta integration and select <strong>Edit</strong>.</li>
<li>Turn on <strong>Send risk score to Okta</strong>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.</li>
</ol>
<p>Next, configure Okta to receive your risk scores.</p>
<ol>
<li>On your Okta admin dashboard, go to <strong>Security</strong> &gt; <strong>Device Integrations</strong>.</li>
<li>Go to <strong>Receive shared signals</strong>, then select <strong>Create stream</strong>.</li>
<li>Name your integration. In <strong>Set up integration with</strong>, choose <em>Well-known URL</em>.</li>
<li>In <strong>Well-known URL</strong>, enter the well-known URL value provided by Cloudflare One.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-06-16">Jun 16, 2024</time><div>
<h2 id="post-2024-06-16-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<div class="changelog-badges"><span>access</span><span>browser-isolation</span><span>casb</span><span>cloudflare-tunnel-sase</span><span>dex</span><span>dlp</span><span>email-security-cf1</span><span>gateway</span><span>multi-cloud-networking</span><span>cloudflare-network-firewall</span><span>network-flow</span><span>magic-transit</span><span>cloudflare-wan</span><span>network-interconnect</span><span>risk-score</span><span>cloudflare-one-client</span></div><div class="changelog-body"><p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2024-02-26">Feb 26, 2024</time><div>
<h2 id="post-2025-02-25-rum-exclude-eu"><a href="/changelog/post/2025-02-25-rum-exclude-eu/">Easily Exclude EU Visitors from RUM</a></h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.</p>
<p><img src="/assets/upstream/images/changelog/web-analytics/2025-02-26-rum-eu.png" alt="RUM Enablement UI" /></p>
<p>Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.</p>
<p>To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.</p>
<p>You can learn more about what metrics are reported by Web Analytics and how it is collected <a href="/web-analytics/data-metrics/">in the Web Analytics documentation</a>. You can enable Web Analytics on any hostname by going to the <a href="https://dash.cloudflare.com/?to=/:account/web-analytics/sites">Web Analytics</a> section of the dashboard, selecting &quot;Manage Site&quot; for the hostname you want to monitor, and choosing the appropriate enablement option.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/49/">Previous</a><span>Page 50 of 50</span></nav>
</div>
