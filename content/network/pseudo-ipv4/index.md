<p>Cloudflare customers can use <strong>Pseudo IPv4</strong> if their origin web server only understands IPv4 formatted IP addresses (meaning it would not support Cloudflare's default <a href="/network/ipv6-compatibility/">IPv6 compatibility</a>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/668.md")
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
<h2 id="background">Background</h2>
<p>Some older origin server analytics and fraud detection software expect IP addresses in an IPv4 format and do not support IPv6 addresses.</p>
<p><strong>Pseudo IPv4</strong> uses the <a href="https://tools.ietf.org/html/rfc1112#section-4">Class E IPv4 address space</a> to provide as many unique IPv4 addresses corresponding to IPv6 addresses as possible.</p>
<ul>
<li>Example Class E IPv4 address: <code>240.16.0.1</code></li>
<li>Example IPv6 address: <code>2400:cb00:f00d:dead:beef:1111:2222:3333</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/667.md")
</aside>
<h2 id="configure-pseudo-ipv4">Configure Pseudo IPv4</h2>
<p>Cloudflare offers three options for configuring <strong>Pseudo IPv4</strong>:</p>
<ul>
<li><strong>Off</strong>: Default value.</li>
<li><strong>Add Header</strong>: Cloudflare automatically adds the <code>Cf-Pseudo-IPv4</code> header with a Class E IPv4 address hashed from the original IPv6 address.</li>
<li><strong>Overwrite Headers</strong>:
If <strong>Pseudo IPv4</strong> is set to <code>Overwrite Headers</code> - Cloudflare overwrites the existing <code>Cf-Connecting-IP</code> and <code>X-Forwarded-For</code> headers with a pseudo IPv4 address while preserving the real IPv6 address in <code>CF-Connecting-IPv6</code> header.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/666.md")
</aside>
<p>To configure <strong>Pseudo IPv4</strong>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/671.md")
</div></div>
