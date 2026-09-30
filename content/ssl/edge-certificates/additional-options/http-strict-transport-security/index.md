<p>HSTS protects HTTPS web servers from downgrade attacks. These attacks redirect web browsers from an HTTPS web server to an attacker-controlled server, allowing bad actors to compromise user data and cookies.</p>
<p>HSTS adds an HTTP header that directs <a href="/ssl/reference/browser-compatibility/">compliant web browsers</a> to:</p>
<ul>
<li>Transform HTTP links to HTTPS links</li>
<li>Prevent users from bypassing SSL browser warnings</li>
</ul>
<p>Before enabling HSTS, review the <a href="#requirements">requirements</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14139.md")
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
<h2 id="requirements">Requirements</h2>
<p>In order for HSTS to work as expected, you need to:</p>
<ul>
<li>Have enabled HTTPS before HSTS so browsers can accept your HSTS settings</li>
<li>Keep HTTPS enabled so visitors can access your site</li>
</ul>
<p>Once you enabled HSTS, avoid the following actions to ensure visitors can still access your site:</p>
<ul>
<li>Changing your DNS records from <a href="/dns/proxy-status/">Proxied to DNS only</a></li>
<li><a href="/fundamentals/manage-domains/pause-cloudflare/">Pausing Cloudflare</a> on your site</li>
<li>Pointing your nameservers away from Cloudflare</li>
<li>Redirecting HTTPS to HTTP</li>
<li>Disabling SSL (invalid or expired certificates or certificates with mismatched hostnames)</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14138.md")
</aside>
<h2 id="enable-hsts">Enable HSTS</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14142.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14137.md")
</aside>
<h2 id="disable-hsts">Disable HSTS</h2>
<p>To disable HSTS on your website:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>For <strong>HTTP Strict Transport Security (HSTS)</strong>, select <strong>Enable HSTS</strong>.</li>
<li>Set the <strong>Max Age Header</strong> to <strong>0 (Disable)</strong>.</li>
<li>If you previously enabled the <strong>No-Sniff</strong> header and want to remove it, set it to <strong>Off</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configuration-settings">Configuration settings</h2>
<table style="width:100%">
<thead>
<tr>
<th>Name</th>
<th>Required</th>
<th>Description</th>
<th>Options</th>
</tr>
</thead>
<tbody>
<tr>
<td>Enable HSTS (Strict-Transport-Security)</td>
<td>Yes</td>
<td>
				Serves HSTS headers to browsers for all HTTPS requests. HTTP
				(non-secure) requests will not contain the header.
</td>
<td>Off / On</td>
</tr>
<tr>
<td>Max Age Header (max-age)</td>
<td>Yes</td>
<td>
				Specifies duration for a browser HSTS policy and requires HTTPS on your
				website.
</td>
<td>Disable, or a range from 1 to 12 months</td>
</tr>
<tr>
<td>Apply HSTS policy to subdomains (includeSubDomains)</td>
<td>No</td>
<td>
				Applies the HSTS policy from a parent domain to subdomains. Subdomains
				are inaccessible if they do not support HTTPS.
</td>
<td>Off / On</td>
</tr>
<tr>
<td>Preload</td>
<td>No</td>
<td>
				Permits browsers to automatically preload HSTS configuration. Prevents
				an attacker from downgrading a first request from HTTPS to HTTP. Preload
				can make a website without HTTPS completely inaccessible.
</td>
<td>Off / On</td>
</tr>
<tr>
<td>No-Sniff Header</td>
<td>No</td>
<td>
				Sends the <code>X-Content-Type-Options: nosniff</code> header to prevent
				Internet Explorer and Chrome from automatically detecting a content type
				other than those explicitly specified by the Content-Type header.
</td>
<td>Off / On</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14136.md")
</aside>
