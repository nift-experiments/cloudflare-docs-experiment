<h2 id="error-1001-dns-resolution-error">Error 1001: DNS resolution error</h2>
<p>This error indicates a DNS resolution failure preventing access to the requested domain.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>A web request was sent to a <a href="https://www.cloudflare.com/ips/">Cloudflare IP address</a> for a non-existent Cloudflare domain.</li>
<li>An external domain that is not on using Cloudflare has a CNAME record to a domain active on Cloudflare</li>
<li>The target of the DNS CNAME record does not resolve.</li>
<li>A CNAME record in your Cloudflare DNS app requires resolution via a DNS provider that is currently offline.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>A non-Cloudflare domain cannot CNAME to a Cloudflare domain, unless the non-Cloudflare domain is added to a Cloudflare account.</p>
<p>Attempting to directly access DNS records used for <a href="/dns/zone-setups/partial-setup">Cloudflare CNAME setups</a> also causes error 1001. For example, <code>www.example.com.cdn.cloudflare.net</code>.</p>
