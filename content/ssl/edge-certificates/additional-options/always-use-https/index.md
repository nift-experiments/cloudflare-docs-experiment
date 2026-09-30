<p>Always Use HTTPS redirects all your visitor requests from <code>http</code> to <code>https</code>, for all subdomains and hosts in your application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14152.md")
</aside>
<p>Cloudflare recommends not performing redirects at your origin web server, as this can cause <a href="/ssl/troubleshooting/too-many-redirects/">redirect loop errors</a>.</p>
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
<h2 id="encrypt-all-visitor-traffic">Encrypt all visitor traffic</h2>
<p>To redirect traffic for all subdomains and hosts in your application, you can enable <strong>Always Use HTTPS</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14151.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14155.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>Forcing HTTPS does not resolve issues with <a href="/ssl/troubleshooting/mixed-content-errors/">mixed content</a>, as browsers check the protocol of included resources before making a request. You will need to use only relative links or HTTPS links on pages that you force to HTTPS. Cloudflare can automatically resolve some mixed-content links using our <a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a> functionality.</p>
