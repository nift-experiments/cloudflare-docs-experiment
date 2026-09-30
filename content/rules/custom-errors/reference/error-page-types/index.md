<table>
<thead>
<tr>
<th>Page type</th>
<th>Description</th>
<th>API identifier</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAF block</td>
<td>The page displayed when visitors are blocked by a <a href="/waf/">Web Application Firewall</a> rule. This page returns a <code>403</code> status code.</td>
<td><code>waf_block</code></td>
</tr>
<tr>
<td>IP/Country block</td>
<td>The page displayed when a request originates from a <a href="/waf/tools/ip-access-rules/">blocked IP address or country</a>. This page returns a <code>403</code> status code.</td>
<td><code>ip_block</code></td>
</tr>
<tr>
<td>IP/Country challenge</td>
<td>Presents a challenge to visitors from specified IP addresses or countries. This page returns a <code>403</code> status code. For more information, refer to <a href="/waf/tools/ip-access-rules/">IP Access rules</a>.</td>
<td><code>country_challenge</code></td>
</tr>
<tr>
<td>500 class errors</td>
<td>500 class error pages are displayed when a web server is unable to process a request. For more information, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx errors</a>.</td>
<td><code>500_errors</code></td>
</tr>
<tr>
<td>1000 class errors</td>
<td>1000 class error pages are displayed when a domain’s configuration, security settings, or origin setup prevents Cloudflare from completing a request. For more information, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx errors</a>.</td>
<td><code>1000_errors</code></td>
</tr>
<tr>
<td>Managed challenge / I'm Under Attack Mode</td>
<td>Presents different types of challenges to a visitor depending on the nature of their request and your security settings. This page returns a <code>403</code> status code. For more information, refer to <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a>.</td>
<td><code>managed_challenge</code></td>
</tr>
<tr>
<td>Rate limiting block</td>
<td>Displayed to visitors when they have been blocked by a <a href="/waf/rate-limiting-rules/">rate limiting rule</a>. This page returns a <code>429</code> status code.</td>
<td><code>ratelimit_block</code></td>
</tr>
</tbody>
</table>
