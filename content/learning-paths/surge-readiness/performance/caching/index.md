<h2 id="optimize-caching">Optimize caching</h2>
<p>By default, Cloudflare <a href="/cache/concepts/default-cache-behavior/">caches static content</a> such as images, CSS, and JavaScript. However, you can extend Cloudflare caching to work with HTML by creating custom <a href="/cache/how-to/cache-rules/">Cache Rules</a>.</p>
<h3 id="cache-more-requests">Cache more requests</h3>
<ol>
<li>In  the Cloudflare dashboard, go to the <strong>Caching</strong> &gt; <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong>.</li>
<li>For When incoming requests match, enter either your entire website or a specific path on your application, based on the Hostname or URI Path. Refer to the <a href="/cache/how-to/cache-rules/settings/#fields">available fields</a>.</li>
<li>For Cache eligibility, define how these requests should be cached and for how long. Refer to the available <a href="/cache/how-to/cache-rules/settings/#eligible-for-cache-settings">cache eligibility settings</a>.</li>
<li>You can then monitor the effectiveness of your cache settings using <a href="/cache/performance-review/cache-analytics/">Cache Analytics</a> and update your configuration according to our <a href="/cache/performance-review/cache-performance/">Cache performance guide</a>.</li>
</ol>
<h3 id="advanced-cache-optimizations">Advanced cache optimizations</h3>
<ul>
<li><a href="/cache/how-to/cache-keys/">Custom Cache Keys</a> allows you to precisely set the cacheability setting for any resource.</li>
<li><a href="/cache/concepts/cache-control/">Origin Cache Control</a> can be used to let the Cache-Control headers tell Cloudflare how to handle content from the origin server.</li>
</ul>
<h2 id="tiered-cache">Tiered Cache</h2>
<p><a href="/cache/how-to/tiered-cache/">Tiered Cache</a> uses the size of Cloudflare's network to reduce requests to customer origin servers by dramatically increasing cache hit ratios.</p>
<p>It works by dividing Cloudflare's data centers into a hierarchy of lower-tiers and upper-tiers. If content is not cached in lower-tier data centers (generally the ones closest to a visitor), the lower-tier requests an upper-tier for the content. If the upper-tier does not have the content, only the upper-tier will initiate a request to the origin. This practice improves bandwidth efficiency by limiting the number of Cloudflare data centers that can ask the origin for content.</p>
<p>Refer to <a href="/cache/how-to/tiered-cache/#enable-tiered-cache">Enable Tiered Cache</a> to get started.</p>
<h3 id="cache-reserve">Cache Reserve</h3>
<p><a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a> is a large, persistent data store implemented on top of <a href="/r2/">R2</a>.</p>
<p>With a single click in the dashboard, your cacheable content will be written to Cache Reserve. In the same way that Tiered Cache builds a hierarchy of caches between your visitors and your origin, Cache Reserve serves as the ultimate <a href="/cache/how-to/tiered-cache/">upper-tier cache</a> that will reserve storage space for your assets for as long as you want.</p>
<p>This ensures that your content is served from cache longer, shielding your origin from unneeded egress fees.</p>
<h2 id="cloudflare-waiting-room">Cloudflare Waiting Room</h2>
<p><a href="/waiting-room/">Cloudflare Waiting Room</a> allows you to route excess users of your website to a customized waiting room, helping preserve customer experience and protect origin servers from being overwhelmed with requests.</p>
<h2 id="use-cloudflare-ip-addresses">Use Cloudflare IP addresses</h2>
<p>Take action to prevent attacks to your application during peak season by configuring your firewall to only accept traffic from Cloudflare IP addresses. By only allowing <a href="https://www.cloudflare.com/ips">Cloudflare IPs</a>, you can prevent attackers from bypassing Cloudflare and sending requests directly to your origin.</p>
<p>Refer to <a href="/fundamentals/concepts/cloudflare-ip-addresses/">Cloudflare IP addresses</a> for more information.</p>
<h2 id="monitor-traffic">Monitor traffic</h2>
<p>You can use the Cloudflare dashboard to closely monitor the traffic on your domain and fine-tune your cache and security settings accordingly.</p>
<h3 id="zone-and-account-analytics">Zone and Account analytics</h3>
<p><a href="/analytics/account-and-zone-analytics/zone-analytics/">Cloudflare zone analytics</a> gives you access to a wide range of metrics, collected at the website or domain level.</p>
<p><a href="/analytics/account-and-zone-analytics/account-analytics/">Cloudflare account analytics</a> lets you access a wide range of aggregated metrics from all the sites under a specific Cloudflare account.</p>
<h3 id="security-analytics-and-security-events">Security Analytics and Security Events</h3>
<p><a href="/waf/analytics/security-analytics/">Security Analytics</a> displays information about all incoming HTTP requests for your domain, including requests not handled by Cloudflare security products.</p>
<p>You can also use the <a href="/waf/analytics/security-events/">Security Events</a> to review mitigated requests and tailor your security configurations.</p>
<h3 id="cache-analytics">Cache Analytics</h3>
<p>You can use <a href="/cache/performance-review/cache-analytics/">Cache Analytics</a> to improve site performance or reduce origin web server traffic. Cache Analytics helps determine if resources are missing from cache, expired, or ineligible for caching.</p>
