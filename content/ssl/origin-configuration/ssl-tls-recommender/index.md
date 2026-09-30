<p>The SSL/TLS Recommender helps you choose which <a href="/ssl/origin-configuration/ssl-modes/">Encryption mode</a> is best for your application.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13994.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="common-tasks">Common tasks</h2>
<h3 id="enable-ssl-tls-recommendations">Enable SSL/TLS recommendations</h3>
<p>To make sure you do not inadvertently block the <strong>SSL/TLS Recommender</strong>, review your settings to make sure your domain:</p>
<ul>
<li>Is accessible.</li>
<li>Is not blocking requests from our bot (which uses a user agent of <code>Cloudflare-SSLDetector</code>).</li>
<li>Does not have any active, SSL-specific <a href="/rules/page-rules/">Page Rules</a> or <a href="/rules/configuration-rules/">Configuration rules</a>.</li>
</ul>
<p>Then, you can enable the SSL/TLS recommender.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13997.md")
</div></div>
<h3 id="manually-trigger-a-new-scan">Manually trigger a new scan</h3>
<p>Once you enable it, the recommender runs future scans periodically — typically every two days — and sends notifications if new recommendations become available.</p>
<p>To manually re-trigger a new scan, disable and then <a href="#enable-ssltls-recommendations">re-enable SSL/TLS recommendations</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>Once enabled, the SSL/TLS Recommender runs an origin scan using the user agent <code>Cloudflare-SSLDetector</code> and ignores your <code>robots.txt</code> file (except for rules explicitly targeting the user agent).</p>
<p>Based on this initial scan, the Recommender may decide that you could use a stronger <a href="/ssl/origin-configuration/ssl-modes/">SSL encryption mode</a>. It will never recommend a weaker option than what is currently configured.</p>
<p>If so, it will send the application owner an email with the recommended option and add a <em>Recommended by Cloudflare</em> tag to that option on the <strong>SSL/TLS</strong> page. You are not required to use this recommendation.</p>
<p>If you do not receive an email, keep your current <strong>SSL encryption mode</strong>.</p>
