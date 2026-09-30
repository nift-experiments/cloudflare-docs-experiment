<h2 id="wordpress-plugin-is-undetected-on-cloudflare-dashboard">WordPress plugin is undetected on Cloudflare dashboard</h2>
<p>The WordPress plugin may go undetected on your Cloudflare dashboard for a few reasons.</p>
<ul>
<li>Versions older than 3.8.2 of the WordPress plugin are installed.
<ul>
<li><strong>Solution:</strong> Install version 4.4.0 of the WordPress plugin.</li>
</ul>
</li>
<li>Version 3.8.2 of the plugin is installed but existing cache plugins return stale responses, for example, without <code>cf-edge-cache</code> header.
<ul>
<li><strong>Solution:</strong> Enable APO from the WordPress plugin and purge the cache in the existing cache plugins.</li>
</ul>
</li>
<li>WordPress only runs on a subdomain, but WordPress and the WordPress plugin check against the apex domain.
<ul>
<li><strong>Solution:</strong> For additional information, see <a href="/automatic-platform-optimization/reference/subdomain-subdirectories/">Subdomains and subdirectories</a></li>
</ul>
</li>
</ul>
<p>If your Cloudflare dashboard cannot detect the WordPress plugin after trying the solutions above, ensure you completed all of the steps listed in <a href="/automatic-platform-optimization/get-started/activate-cf-wp-plugin/">Activate the Cloudflare WordPress plugin</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3340.md")
</aside>
<h2 id="wordpress-returns-stale-content">WordPress returns stale content</h2>
<p>If WordPress is returning stale content, <a href="/cache/how-to/purge-cache/">purge the cache</a> when APO is enabled.</p>
