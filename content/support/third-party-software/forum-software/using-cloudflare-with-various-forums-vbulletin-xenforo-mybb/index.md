<h2 id="overview">Overview</h2>
<p>Many widely used forum platforms are compatible with Cloudflare.</p>
<p>These include:</p>
<ul>
<li><a href="https://community.cloudflare.com/t/using-discourse-with-cloudflare-best-practices/602890">Discourse</a></li>
<li>vBulletin</li>
<li>Xenforo</li>
<li>MyBB</li>
</ul>
<p>If you have a forum using these platforms, you can increase its speed and safety by adding Cloudflare.</p>
<hr />
<h2 id="steps">Steps</h2>
<p><strong>1</strong>. Cloudflare acts as a reverse proxy, meaning that all visitor IP addresses will become Cloudflare-affiliated IP addresses. If you are using services like <strong>Stopforumspan</strong> or blocking registration by IP address, you need to <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">restore original visitor IPs</a>.</p>
<p><strong>2</strong>. To prevent admin functions from being affected by caching or performance features, create a <a href="/cache/how-to/cache-rules/settings/#bypass-cache">Cache Rule</a> to bypass cache on the admin section of your site.</p>
<p><strong>3</strong>. If you want certain services to access your website (APIs or certain IPs), <a href="/waf/">configure the WAF</a>.</p>
<p><strong>4</strong>. Review your DNS records to make sure all your subdomain records are present. If you cannot find a subdomain, <a href="/dns/manage-dns-records/how-to/create-dns-records/">add the DNS record</a>.</p>
