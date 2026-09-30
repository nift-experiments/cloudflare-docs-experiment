<p>To troubleshoot your site, you can pause Cloudflare globally. This will send traffic directly to your origin web server instead of Cloudflare's reverse proxy. Paused domains also cannot use Cloudflare services like <a href="/rules/">Rules</a>, <a href="/waf/">WAF</a>, and <a href="/ssl/edge-certificates/">SSL/TLS certificates</a>. Consider turning on <a href="/fundamentals/manage-domains/pause-cloudflare/#enable-development-mode">Development Mode</a> to bypass caching while preserving protection.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and domain.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Within <strong>Overview</strong>, choose <strong>Advanced Actions</strong> &gt; <strong>Pause Cloudflare on Site</strong>.</li>
</ol>
<p>The process of pausing Cloudflare takes five minutes or less. This approach is preferable to <a href="/dns/zone-setups/full-setup/setup/">changing nameservers</a>, which can cause propagation delays of several hours.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8902.md")
</aside>
<hr />
<h2 id="alternatives-to-global-pause">Alternatives to global pause</h2>
<h3 id="disable-proxy-on-dns-records">Disable proxy on DNS records</h3>
<p>Instead of pausing Cloudflare globally, you can disable the proxy on individual records:</p>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</p>
</li>
<li>
<p>Go to <strong>DNS</strong> &gt; <strong>Records</strong>. Choose the record and select <strong>Edit</strong>.</p>
</li>
<li>
<p>Toggle <strong>Proxy Status</strong> to <strong>Off</strong>.</p>
</li>
</ol>
<p>Adjusting the proxy status will prevent that record from using Cloudflare services like <a href="/rules/">Rules</a>, <a href="/waf/">WAF</a>, and <a href="/ssl/edge-certificates/">SSL/TLS certificates</a>.</p>
<h3 id="enable-development-mode">Enable Development Mode</h3>
<p>To troubleshoot caching issues, you could <a href="/cache/reference/development-mode/">enable Development Mode</a>. This will bypass Cloudflare's cache while still preserving Cloudflare services like <a href="/rules/">Rules</a>, <a href="/waf/">WAF</a>, and <a href="/ssl/edge-certificates/">SSL/TLS certificates</a>.</p>
