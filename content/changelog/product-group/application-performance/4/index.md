---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/application-performance/4/
  description: '2025-01-09'
  full_title: Application performance changelog - page 4 | Cloudflare Docs
  head_html: <title>Application performance changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-01-09"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/application-performance/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Application performance changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-01-09"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/application-performance/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/application-performance/4/#page","headline":"Application performance changelog - page 4 | Cloudflare Docs","description":"2025-01-09","url":"https://developers.cloudflare.com/changelog/product-group/application-performance/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/application-performance/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-rules-overview-interface"><a href="/changelog/post/2025-01-09-rules-overview/">New Rules Overview Interface</a></h2>
<p><em>2025-01-09</em></p>
<p><strong>Rules Overview</strong> gives you a single page to manage all your <a href="/rules/">Cloudflare Rules</a>.</p>
<p>What you can do:</p>
<ul>
<li><strong>See all your rules in one place</strong> – No more clicking around.</li>
<li><strong>Find rules faster</strong> – Search by name.</li>
<li><strong>Understand execution order</strong> – See how rules run in sequence.</li>
<li><strong>Debug easily</strong> – Use <a href="/rules/trace-request/">Trace</a> without switching tabs.</li>
</ul>
<p>Check it out in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview">Rules &gt; Overview</a>.</p>


<h2 id="smart-tiered-cache-optimizes-load-balancing-pools"><a href="/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/">Smart Tiered Cache optimizes Load Balancing Pools</a></h2>
<p><em>2025-01-08</em></p>
<p>You can now achieve higher cache hit rates and reduce origin load when using <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. Cloudflare automatically selects a single, optimal tiered data center for all origins in your Load Balancing Pool.</p>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-how-it-works">How it works</h4>
<p>When you use <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>, Cloudflare analyzes performance metrics across your pool's origins and automatically selects the optimal Upper Tier data center for the entire pool. This means:</p>
<ul>
<li><strong>Consistent cache location</strong>: All origins in the pool share the same Upper Tier cache.</li>
<li><strong>Higher HIT rates</strong>: Requests for the same content hit the cache more frequently.</li>
<li><strong>Reduced origin requests</strong>: Fewer requests reach your origin servers.</li>
<li><strong>Improved performance</strong>: Faster response times for cache HITs.</li>
</ul>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-example-workflow">Example workflow</h4>
<pre tabindex="0"><code class="language-txt">Load Balancing Pool: api-pool&#10;├── Origin 1: api-1.example.com&#10;├── Origin 2: api-2.example.com&#10;└── Origin 3: api-3.example.com&#10;    ↓&#10;Selected Upper Tier: [Optimal data center based on pool performance]&#10;</code></pre>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone and configure your <a href="/load-balancing/">Load Balancing Pool</a>.</p>


<h2 id="terraform-support-for-snippets"><a href="/changelog/post/2024-12-11-terraform-snippets/">Terraform Support for Snippets</a></h2>
<p><em>2024-12-11</em></p>
<p>Now, you can manage <a href="/rules/snippets/">Cloudflare Snippets</a> with <a href="/terraform/">Terraform</a>. Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.</p>
<p>Example Terraform configuration:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_snippet&quot; &quot;my_snippet&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	name = &quot;my_test_snippet_1&quot;&#10;	main_module = &quot;file1.js&quot;&#10;	files {&#10;		name = &quot;file1.js&quot;&#10;		content = file(&quot;file1.js&quot;)&#10;	}&#10;}&#10;&#10;resource &quot;cloudflare_snippet_rules&quot; &quot;cookie_snippet_rule&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	rules {&#10;		enabled = true&#10;		expression = &quot;http.cookie eq \&quot;a=b\&quot;&quot;&#10;		description = &quot;Trigger snippet on specific cookie&quot;&#10;		snippet_name = &quot;my_test_snippet_1&quot;&#10;	}&#10;	depends_on = [cloudflare_snippet.my_snippet]&#10;}&#10;</code></pre>
<p>Learn more in the <a href="/rules/snippets/create-terraform/">Configure Snippets using Terraform</a> documentation.</p>


<h2 id="cloud-connector-now-supports-r2"><a href="/changelog/post/2024-11-22-cloud-connector-r2/">Cloud Connector Now Supports R2</a></h2>
<p><em>2024-11-22</em></p>
<p>Now, you can use <a href="/rules/cloud-connector/">Cloud Connector</a> to route traffic to your <a href="/r2/">R2 buckets</a> based on URLs, headers, geolocation, and more.</p>
<p>Example setup:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;    &quot;provider&quot;: &quot;cloudflare_r2&quot;,&#10;    &quot;description&quot;: &quot;Connect to R2 bucket containing images&quot;,&#10;    &quot;parameters&quot;: {&#10;      &quot;host&quot;: &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<p>Get started using <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="smart-tiered-cache-automatically-optimizes-r2-caching"><a href="/changelog/post/2024-11-20-smart-tiered-cache-for-r2/">Smart Tiered Cache automatically optimizes R2 caching</a></h2>
<p><em>2024-11-20</em></p>
<p>You can now reduce latency and lower R2 egress costs automatically when using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> with <a href="/r2/">R2</a>. Cloudflare intelligently selects a tiered data center close to your R2 bucket location, creating an efficient caching topology without additional configuration.</p>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-how-it-works">How it works</h4>
<p>When you enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> for zones using <a href="/r2/">R2</a> as an origin, Cloudflare automatically:</p>
<ol>
<li><strong>Identifies your R2 bucket location</strong>: Determines the geographical region where your R2 bucket is stored.</li>
<li><strong>Selects an optimal Upper Tier</strong>: Chooses a data center close to your bucket as the common Upper Tier cache.</li>
<li><strong>Routes requests efficiently</strong>: All cache misses in edge locations route through this Upper Tier before reaching R2.</li>
</ol>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-benefits">Benefits</h4>
<ul>
<li><strong>Automatic optimization</strong>: No manual configuration required.</li>
<li><strong>Lower egress costs</strong>: Fewer requests to R2 reduce egress charges.</li>
<li><strong>Improved hit ratio</strong>: Common Upper Tier increases cache efficiency.</li>
<li><strong>Reduced latency</strong>: Upper Tier proximity to R2 minimizes fetch times.</li>
</ul>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone using R2 as an origin.</p>


<h2 id="stage-and-test-cache-configurations-safely"><a href="/changelog/post/2024-11-07-cache-versioning/">Stage and test cache configurations safely</a></h2>
<p><em>2024-11-07</em></p>
<p>You can now stage and test cache configurations before deploying them to production. Versioned environments let you safely validate cache rules, purge operations, and configuration changes without affecting live traffic.</p>
<h4 id="2024-11-07-cache-versioning-how-it-works">How it works</h4>
<p>With versioned environments, you can:</p>
<ol>
<li><strong>Create staging versions</strong> of your cache configuration.</li>
<li><strong>Test cache rules</strong> in a non-production environment.</li>
<li><strong>Purge staged content</strong> independently from production.</li>
<li><strong>Validate changes</strong> before promoting to production.</li>
</ol>
<p>This capability integrates with Cloudflare's broader <a href="/version-management/">versioning system</a>, allowing you to manage cache configurations alongside other zone settings.</p>
<h4 id="2024-11-07-cache-versioning-benefits">Benefits</h4>
<ul>
<li><strong>Risk-free testing</strong>: Validate configuration changes without impacting production.</li>
<li><strong>Independent purging</strong>: Clear staging cache without affecting live content.</li>
<li><strong>Deployment confidence</strong>: Catch issues before they reach end users.</li>
<li><strong>Team collaboration</strong>: Multiple team members can work on different versions.</li>
</ul>
<h4 id="2024-11-07-cache-versioning-get-started">Get started</h4>
<p>To get started, refer to the <a href="/version-management/">version management documentation</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2024-11-07-cache-versioning-important-limitation">Important limitation</h4>
@markup("md", "content/.markup/bodies/17701.md")</aside>


<h2 id="shard-cache-using-custom-cache-key-values"><a href="/changelog/post/2024-11-07-shard-cache-by-cache-key/">Shard cache using custom cache key values</a></h2>
<p><em>2024-11-07</em></p>
<p>Enterprise customers can now optimize cache hit ratios for content that varies by device, language, or referrer by <strong>sharding cache</strong> using up to ten values from previously restricted headers with <a href="/cache/how-to/cache-keys/">custom cache keys</a>.</p>
<h4 id="2024-11-07-shard-cache-by-cache-key-how-it-works">How it works</h4>
<p>When configuring <a href="/cache/how-to/cache-keys/">custom cache keys</a>, you can now include values from these headers to create distinct cache entries:</p>
<ul>
<li><strong><code>accept*</code> headers</strong> (for example, <code>accept</code>, <code>accept-encoding</code>, <code>accept-language</code>): Serve different cached versions based on content negotiation.</li>
<li><strong><code>referer</code> header</strong>: Cache content differently based on the referring page or site.</li>
<li><strong><code>user-agent</code> header</strong>: Maintain separate caches for different browsers, devices, or bots.</li>
</ul>
<h4 id="2024-11-07-shard-cache-by-cache-key-when-to-use-cache-sharding">When to use cache sharding</h4>
<ul>
<li>Content varies significantly by device type (mobile vs desktop).</li>
<li>Different language or encoding preferences require distinct responses.</li>
<li>Referrer-specific content optimization is needed.</li>
</ul>
<h4 id="2024-11-07-shard-cache-by-cache-key-example-configuration">Example configuration</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;cache_key&quot;: {&#10;    &quot;custom_key&quot;: {&#10;      &quot;header&quot;: {&#10;        &quot;include&quot;: [&quot;accept-language&quot;, &quot;user-agent&quot;],&#10;        &quot;check_presence&quot;: [&quot;referer&quot;]&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>This configuration creates separate cache entries based on the <code>accept-language</code> and <code>user-agent</code> headers, while also considering whether the <code>referer</code> header is present.</p>
<h4 id="2024-11-07-shard-cache-by-cache-key-get-started">Get started</h4>
<p>To get started, refer to the <a href="/cache/how-to/cache-keys/">custom cache keys documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17702.md")</aside>


<h2 id="simplified-ui-for-url-rewrites"><a href="/changelog/post/2024-10-23-url-rewrites-wildcard/">Simplified UI for URL Rewrites</a></h2>
<p><em>2024-10-23</em></p>
<p>It’s now easy to create <strong>wildcard-based <a href="/rules/transform/url-rewrite/">URL Rewrites</a></strong>. No need for complex functions—just define your patterns and go.</p>
<p><img src="/assets/upstream/images/rules/transform/create-url-rewrite-rule.png" alt="Rules Overview Interface" /></p>
<p>What’s improved:</p>
<ul>
<li><strong>Full wildcard support</strong> – Create rewrite patterns using intuitive interface.</li>
<li><strong>Simplified rule creation</strong> – No need for complex functions.</li>
</ul>
<p>Try it via <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">creating a Rewrite URL rule in the dashboard</a>.</p>


<h2 id="one-click-cache-rules-templates-now-available"><a href="/changelog/post/2024-09-05-cache-rules-templates/">One-click Cache Rules templates now available</a></h2>
<p><em>2024-09-05</em></p>
<p>You can now create optimized cache rules instantly with <strong>one-click templates</strong>, eliminating the complexity of manual rule configuration.</p>
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


<h2 id="new-rules-templates-for-one-click-rule-creation"><a href="/changelog/post/2024-09-05-rules-templates/">New Rules Templates for One-Click Rule Creation</a></h2>
<p><em>2024-09-05</em></p>
<p>Now, you can create <strong>common rule configurations</strong> in just <strong>one click</strong> using Rules Templates.</p>
<p><img src="/assets/upstream/images/changelog/rules/rules-templates.gif" alt="Rules Templates" /></p>
<p>What you can do:</p>
<ul>
<li><strong>Pick a pre-built rule</strong> – Choose from a library of templates.</li>
<li><strong>One-click setup</strong> – Deploy best practices instantly.</li>
<li><strong>Customize as needed</strong> – Adjust templates to fit your setup.</li>
</ul>
<p>Template cards are now also available directly in the rule builder for each product.</p>
<p>Need more ideas? Check out the <a href="/rules/examples/">Examples gallery</a> in our documentation.</p>


<h2 id="regionalized-generic-tiered-cache-for-higher-hit-ratios"><a href="/changelog/post/2024-07-19-regionalized-generic-tiered-cache/">Regionalized Generic Tiered Cache for higher hit ratios</a></h2>
<p><em>2024-07-19</em></p>
<p>You can now achieve higher cache hit ratios with <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a>. Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.</p>
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


<h2 id="easily-exclude-eu-visitors-from-rum"><a href="/changelog/post/2025-02-25-rum-exclude-eu/">Easily Exclude EU Visitors from RUM</a></h2>
<p><em>2024-02-26</em></p>
<p>You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.</p>
<p><img src="/assets/upstream/images/changelog/web-analytics/2025-02-26-rum-eu.png" alt="RUM Enablement UI" /></p>
<p>Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.</p>
<p>To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.</p>
<p>You can learn more about what metrics are reported by Web Analytics and how it is collected <a href="/web-analytics/data-metrics/">in the Web Analytics documentation</a>. You can enable Web Analytics on any hostname by going to the <a href="https://dash.cloudflare.com/?to=/:account/web-analytics/sites">Web Analytics</a> section of the dashboard, selecting &quot;Manage Site&quot; for the hostname you want to monitor, and choosing the appropriate enablement option.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-performance/3/">Previous</a><span>Page 4 of 4</span></nav>
