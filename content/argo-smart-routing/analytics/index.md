<p>Cloudflare provides analytics to show the performance benefits of Argo Smart Routing.</p>
<p>You can access Argo analytics for your domain in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> at <strong>Analytics</strong> &gt; <strong>Performance</strong>. For information on all analytics in the dashboard, refer to <a href="/analytics/">Analytics</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>Analytics collects data based on the time-to-first-byte (TTFB) from your origin to the Cloudflare network. TTFB is the delay between when Cloudflare sends a request to your server and when it receives the first byte in response. Argo Smart Routing optimizes your server's network transit time to minimize this delay.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1527.md")
</aside>
<h2 id="types-of-analytics">Types of analytics</h2>
<p>The dashboard displays two different views for performance data:</p>
<ul>
<li>
<p><strong>Origin Response Time</strong>: A histogram shows response time from your origin to the Cloudflare network. The blue bars show time-to-first-byte (TTFB) without Argo, while the orange bars show TTFB where Argo found a Smart Route.</p>
</li>
<li>
<p><strong>Geography</strong>: A map shows the improvement in response time at each Cloudflare data center.</p>
<ul>
<li>A negative value indicates that requests from that location would not have benefited from Argo Smart Routing, so instead would have been routed directly.</li>
</ul>
</li>
</ul>
