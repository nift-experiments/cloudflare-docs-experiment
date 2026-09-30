<h2 id="error-1002-dns-points-to-prohibited-ip">Error 1002: DNS points to Prohibited IP</h2>
<p>This error indicates that a Cloudflare DNS record points to a prohibited IP, preventing proper domain resolution.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>A DNS record in your Cloudflare DNS app points to one of <a href="https://www.cloudflare.com/ips/">Cloudflare's IP addresses</a>.</li>
<li>An incorrect target is specified for a CNAME record in your Cloudflare DNS app.</li>
<li>Your domain is not on Cloudflare but has a CNAME that refers to a Cloudflare domain.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>Update your Cloudflare A or CNAME record to point to your origin IP address instead of a Cloudflare IP address:</p>
<ol>
<li>
<p>Contact your hosting provider to confirm your origin IP address or CNAME record target.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to the <strong>Records</strong> page.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select the domain that generates error 1002.</li>
<li>Select the <strong>DNS</strong> app.</li>
<li>Select <strong>Value</strong> for the A record to update.</li>
<li>Update the A record.</li>
</ol>
<p>To ensure your origin web server does not proxy its own requests through Cloudflare, configure your origin webserver to resolve your Cloudflare domain to:</p>
<ul>
<li>The internal NAT'd IP address, or</li>
<li>The public IP address of the origin web server.</li>
</ul>
<h2 id="error-1002-restricted">Error 1002: Restricted</h2>
<p>This error indicates that the domain resolves to a restricted or disallowed IP address.</p>
<h3 id="common-cause">Common cause</h3>
<p>The Cloudflare domain resolves to a local or disallowed IP address or an IP address not associated with the domain.</p>
<h3 id="resolution-1">Resolution</h3>
<p>If you own the website:</p>
<ol>
<li>Confirm your origin web server IP addresses with your hosting provider,</li>
<li>Log in to your Cloudflare account, and</li>
<li>Update the A records in the Cloudflare DNS app to the IP address confirmed by your hosting provider.</li>
</ol>
