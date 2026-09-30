<p>Cloudflare may crawl or make HTTP requests to your site to make sure its protected and performing properly.</p>
<h2 id="crawling-situations">Crawling situations</h2>
<h3 id="specific-products">Specific products</h3>
<p>Cloudflare will crawl your site when you have specific products enabled:</p>
<ul>
<li><a href="/cache/how-to/always-online/"><strong>Always Online</strong></a>
<ul>
<li><em>User-Agent</em>: <code>Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online)</code></li>
</ul>
</li>
<li><a href="/health-checks/"><strong>Health checks</strong></a>
<ul>
<li><em>User-Agent</em>: <code>Mozilla/5.0 (compatible; Cloudflare-Healthchecks/1.0; +https://www.cloudflare.com/; healthcheck-id: &lt;HEALTHCHECK_ID&gt;)</code></li>
<li><code>HEALTHCHECK_ID</code> is a 16-character string associated with the health check ID.</li>
</ul>
</li>
<li><a href="/load-balancing/monitors/"><strong>Load balancing monitors</strong></a>
<ul>
<li><em>User-Agent</em>: <code>Mozilla/5.0 (compatible; Cloudflare-Traffic-Manager/1.0; +https://www.cloudflare.com/traffic-manager/; pool-id: &lt;POOL_ID&gt;)</code></li>
<li><code>POOL_ID</code> is a 16-character string associated with the load balancing pool ID being monitored.</li>
</ul>
</li>
<li><a href="/speed/optimization/content/prefetch-urls/"><strong>Prefetch URLs</strong></a>
<ul>
<li><em>User-Agent</em>: <code>Mozilla/5.0 (compatible; CloudFlare-Prefetch/0.1; +http://www.cloudflare.com/)</code></li>
</ul>
</li>
<li><a href="/ssl/origin-configuration/ssl-tls-recommender/"><strong>SSL/TLS recommender</strong></a>
<ul>
<li><em>User-Agent</em>: <code>Cloudflare-SSLDetector</code></li>
<li>This crawler ignores your <code>robots.txt</code> file unless there are rules explicitly targeting the user agent.</li>
</ul>
</li>
<li><a href="/security/security-insights/review-insights/"><strong>Security Insights</strong></a>
<ul>
<li><em>User-Agent</em>: <code>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 (compatible; +https://developers.cloudflare.com/security-center/)</code></li>
</ul>
</li>
</ul>
<h3 id="other-situations">Other situations</h3>
<p>Cloudflare will also crawl your site in other, specific situations:</p>
<ul>
<li><strong>Speed tests</strong>
<ul>
<li><em>User-Agent</em>: <code>Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 PTST/190628.140653</code></li>
<li><em>Triggered when</em>: You launch a speed test from within <a href="/speed/observatory/run-speed-test/">the Cloudflare dashboard</a>.</li>
</ul>
</li>
<li><strong>Support diagnostics</strong>:
<ul>
<li><em>User-Agent</em>: <code>Cloudflare-diagnostics</code></li>
<li><em>Triggered when</em>: Cloudflare Support Engineers perform error checks and by continuous monitoring used to raise intelligent alerts in the Cloudflare dashboard.</li>
</ul>
</li>
<li><strong>Custom Hostname validation</strong>:
<ul>
<li><em>User-Agent</em>: <code>Cloudflare Custom Hostname Verification</code></li>
<li><em>Triggered when</em>: You choose to validate a custom hostname with an <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/#http-tokens">HTTP ownership token</a>.</li>
</ul>
</li>
</ul>
<h2 id="developer-product-crawlers">Developer product crawlers</h2>
<p><a href="/browser-run/"><strong>Browser Run</strong></a> is a Cloudflare developer product that can crawl third-party websites on behalf of Cloudflare customers. Unlike the crawlers in the Crawling situations section, it does not crawl your site as part of a Cloudflare service you have enabled. It is used by developers building applications with Cloudflare's platform.</p>
<p>The <a href="/browser-run/quick-actions/crawl-endpoint/"><strong>Browser Run /crawl endpoint</strong></a> uses a <em>User-Agent</em> of <code>CloudflareBrowserRenderingCrawler/1.0</code>. For non-configurable headers, bot detection IDs, and cryptographic verification methods you can use to identify or block Browser Run traffic, refer to <a href="/browser-run/reference/automatic-request-headers/">Automatic request headers</a>.</p>
<p><a href="/ai-search/"><strong>AI Search</strong></a> is a Cloudflare developer product that indexes your website content so it can be searched. The AI Search crawler only crawls a website you own (the domain must exist in the same Cloudflare account) that you select as your data source in AI Search.</p>
<p>The crawler uses a <em>User-Agent</em> of <code>Cloudflare-AI-Search</code>. You can allow or block it with WAF rules using its <a href="/ai-search/configuration/data-source/website/#allow-ai-search-through-waf">bot detection ID</a>.</p>
