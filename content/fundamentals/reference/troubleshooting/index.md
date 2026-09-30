<p>When you <a href="/fundamentals/account/">set up Cloudflare</a>, you may experience the following issues or error messages.</p>
<h2 id="error-messages">Error messages</h2>
<ul>
<li><a href="/ssl/troubleshooting/too-many-redirects/"><code>ERR_TOO_MANY_REDIRECTS</code></a></li>
<li><a href="/ssl/troubleshooting/too-many-redirects/"><code>525</code> or <code>526</code> errors</a></li>
<li><a href="/dns/manage-dns-records/troubleshooting/records-with-same-name/">Cannot add DNS records with the same name</a></li>
<li><a href="/ssl/troubleshooting/version-cipher-mismatch/"><code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code> or <code>SSL_ERROR_NO_CYPHER_OVERLAP</code></a></li>
<li><a href="/dns/troubleshooting/dns-probe-finished-nxdomain/"><code>DNS_PROBE_FINISHED_NXDOMAIN</code></a></li>
<li><a href="/dns/manage-dns-records/troubleshooting/exposed-ip-address/">Record exposing origin server IP address</a></li>
<li><a href="/ssl/troubleshooting/mixed-content-errors/">Mixed content errors</a></li>
<li><a href="/ssl/troubleshooting/general-ssl-errors/">SSL errors in appear in my browser</a></li>
</ul>
<h2 id="behavior">Behavior</h2>
<ul>
<li><a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Why are Cloudflare's IPs in my origin web server logs?</a></li>
<li><a href="#is-cloudflare-attacking-me">Is Cloudflare attacking me?</a></li>
<li><a href="/dns/zone-setups/troubleshooting/cannot-add-domain/">Cannot add domain to Cloudflare</a></li>
<li><a href="/dns/troubleshooting/email-issues/">My domain’s email stopped working</a></li>
<li><a href="/ssl/edge-certificates/encrypt-visitor-traffic/">Why is my site served over HTTP instead of HTTPS?</a></li>
<li><a href="/ssl/troubleshooting/general-ssl-errors/#only-some-of-your-subdomains-return-ssl-errors">SSL is not working for my second-level subdomain, such as <code>dev.www.example.com</code></a></li>
<li><a href="/dns/zone-setups/troubleshooting/domain-deleted/">Why was my domain deleted from Cloudflare?</a></li>
</ul>
<h2 id="cloudflare">Cloudflare</h2>
<ul>
<li><a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">Gather information to troubleshoot site issues</a></li>
<li><a href="/support/contacting-cloudflare-support/">Contact Cloudflare support</a></li>
<li><a href="/fundamentals/user-profiles/customize-account/#notifications">Manage email notifications</a></li>
</ul>
<h2 id="general-resources">General resources</h2>
<ul>
<li><a href="/dns/faq/">DNS FAQ</a></li>
<li><a href="/ssl/faq/">SSL/TLS FAQ</a></li>
</ul>
<h2 id="is-cloudflare-attacking-me">Is Cloudflare attacking me</h2>
<p>Two common scenarios falsely lead to the perception that Cloudflare is attacking your site:</p>
<ul>
<li>Unless you <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">restore the original visitor IP addresses</a>, Cloudflare IP addresses appear in your server logs for all proxied requests.</li>
<li>The attacker is spoofing Cloudflare's IPs. Cloudflare only <a href="/fundamentals/reference/network-ports/">sends traffic to your origin web server over a few specific ports</a> unless you use <a href="/spectrum/">Cloudflare Spectrum</a>.</li>
</ul>
<p>Ideally, because Cloudflare is a reverse proxy, your hosting provider observes attack traffic connecting from <a href="https://www.cloudflare.com/ips/">Cloudflare IP addresses</a>. In contrast, if you notice connections from IP addresses that do not belong to Cloudflare, the attack is direct to your origin web server. Cloudflare cannot stop attacks directly to your origin IP address because the traffic bypasses Cloudflare's network.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8771.md")
</aside>
