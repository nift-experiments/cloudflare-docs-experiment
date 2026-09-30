<h2 id="error-1000-dns-points-to-prohibited-ip">Error 1000: DNS points to prohibited IP</h2>
<p>This error indicates that a Cloudflare DNS record points to a prohibited IP, blocking access to the requested domain.</p>
<h3 id="common-causes">Common causes</h3>
<p>Cloudflare halted the request for one of the following reasons:</p>
<ul>
<li>An A record within your Cloudflare DNS app points to a <a href="https://www.cloudflare.com/ips/">Cloudflare IP address</a>, or a Load Balancer Origin points to a proxied record.</li>
<li>Your Cloudflare DNS A or CNAME record references another reverse proxy (such as an nginx web server that uses the proxy_pass function) that then proxies the request to Cloudflare a second time.</li>
<li>The request <code>X-Forwarded-For</code> header is longer than 100 characters.</li>
<li>The request includes two <code>X-Forwarded-For</code> headers.</li>
<li>The request includes a <code>CF-Connecting-IP</code> header.</li>
<li>A Server Name Indication (SNI) issue or mismatch at the origin.</li>
<li>Your DNS record points to a SaaS provider that uses <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> with <a href="/byoip/">BYOIP</a> (Bring Your Own IP). Because the provider's IP addresses are advertised through Cloudflare's network, requests resolve to Cloudflare infrastructure. If the provider has not configured a <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">custom hostname</a> for your domain, this error is returned.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<ul>
<li>If an A record within your Cloudflare DNS app points to a <a href="https://www.cloudflare.com/ips/">Cloudflare IP address</a>, update the IP address to your origin web server IP address. Reach out to your hosting provider if you need help obtaining the origin IP address.</li>
<li>There is a reverse-proxy at your origin that sends the request back through the Cloudflare proxy. Instead of using a reverse-proxy, contact your hosting provider or site administrator to configure an HTTP redirect at your origin.</li>
<li>If your domain points to a SaaS provider that uses Cloudflare, contact the SaaS provider to verify that a custom hostname is properly configured for your domain. The error originates from the provider's Cloudflare account, not yours.</li>
</ul>
