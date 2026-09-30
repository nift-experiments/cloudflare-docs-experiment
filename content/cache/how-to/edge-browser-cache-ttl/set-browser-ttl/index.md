<p>Specify a time for a visitor’s Browser Cache TTL to accelerate the page load for repeat visitors to your website. To configure cache duration within Cloudflare’s data centers, refer to <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL</a>.</p>
<p>By default, Cloudflare honors the cache expiration set in your <code>Expires</code> and <code>Cache-Control</code> headers. Cloudflare overrides any <code>Cache-Control</code> or <code>Expires</code> headers with values set via the <strong>Browser Cache TTL</strong> option under <strong>Caching</strong> on your dashboard if:</p>
<ul>
<li>The value of the <code>Cache-Control</code> header from the origin web server is less than the <strong>Browser Cache TTL</strong> setting. This means that <strong>Browser cache TTL</strong> value needs to be higher than origin <code>max-age</code>.</li>
<li>The origin web server does not send a <code>Cache-Control</code> or an <code>Expires</code> header.</li>
</ul>
<p>Unless specifically set in a <a href="/cache/how-to/cache-rules/">Cache Rule</a>, Cloudflare does not override or insert <code>Cache-Control</code> headers if you set <strong>Browser Cache TTL</strong> to <strong>Respect Existing Headers</strong>.</p>
<p>Nevertheless, the value you set via Cache Rule will be ignored if <code>Cache-Control: max-age</code> is higher. In other words, you can override to make browsers cache longer than Cloudflare's edge but not less.</p>
<h2 id="set-browser-cache-ttl">Set Browser Cache TTL</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3874.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Caching</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Browser Cache TTL</strong>, select the desired cache expiration time from the drop-down menu.</li>
</ol>
<p>The <strong>Respect Existing Headers</strong> option tells Cloudflare to honor the settings in the <code>Cache-Control</code> headers from your origin web server.</p>
