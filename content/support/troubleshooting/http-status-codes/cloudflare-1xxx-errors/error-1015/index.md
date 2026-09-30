<h2 id="error-1015-you-are-being-rate-limited">Error 1015: You are being rate limited</h2>
<p>The website you are trying to visit has received too many requests and has temporarily blocked you from accessing it.</p>
<h3 id="common-cause">Common cause</h3>
<p>The website owner has configured rate limiting rules that restrict how many requests a visitor can make to their site in a given time period. When you exceed this limit, Cloudflare returns a <code>1015</code> error.</p>
<h3 id="resolution">Resolution</h3>
<p><strong>If you are a site visitor:</strong></p>
<ul>
<li>Wait for a period of time, then try accessing the website again later. Do not repeatedly try to access the website within a short period of time, as this may extend the block.</li>
<li>If you are still blocked or need help, contact the website owner or the website's support team directly for help. Cloudflare does not control which visitors are rate limited, the website owner sets these rules.</li>
</ul>
<p><strong>If you are the site owner:</strong></p>
<ul>
<li>Review your current <a href="/waf/rate-limiting-rules/">rate limiting thresholds</a> and adjust your configuration.</li>
<li>If a rate limiting rule is blocking requests in a short time period (for example, one second), try increasing the time period to 10 seconds.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14736.md")
</aside>
