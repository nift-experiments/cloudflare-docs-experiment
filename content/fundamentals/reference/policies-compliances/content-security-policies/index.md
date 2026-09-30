<p>A <strong>Content Security Policy (CSP)</strong> is an added layer of security that helps detect and mitigate certain types of attacks, including:</p>
<ul>
<li>Content/code injection</li>
<li>Cross-site scripting (XSS)</li>
<li>Embedding malicious resources</li>
<li>Malicious iframes (clickjacking)</li>
</ul>
<p>To learn more about configuring a CSP in general, refer to the <a href="https://developer.mozilla.org/docs/web/http/csp">Mozilla documentation</a>.</p>
<h2 id="using-a-csp-with-cloudflare">Using a CSP with Cloudflare</h2>
<p>Cloudflare's <a href="/cache/">CDN</a> is compatible with CSP.</p>
<p>Cloudflare does not:</p>
<ul>
<li>Modify CSP headers from the origin web server (except when using Zaraz, to ensure the <a href="https://blog.cloudflare.com/cloudflare-zaraz-supports-csp/">Zaraz script is always running</a>).</li>
<li>Require changes to acceptable sources for first or third-party content.</li>
<li>Modify URLs (besides adding the <a href="/fundamentals/reference/cdn-cgi-endpoint/"><code>/cdn-cgi/</code> endpoint</a> and <a href="/speed/optimization/content/fonts/">Cloudflare Fonts</a> that rewrites Google Fonts urls).</li>
<li>Interfere with locations specified in your CSP.</li>
</ul>
<p>If you require the CSP headers to be changed or added, you can change them using some Cloudflare products:</p>
<ul>
<li>If your website is <a href="/dns/proxy-status/">proxied</a> through Cloudflare, you can use a <a href="/rules/transform/response-header-modification/">response header transform rule</a> to replace or add CSP headers.</li>
<li>If your website is hosted using <a href="/pages/">Cloudflare Pages</a>, you can set a <a href="/pages/configuration/headers/"><code>_headers file</code></a> to modify or add CSP headers.</li>
</ul>
<h3 id="product-requirements">Product requirements</h3>
<p>To use certain Cloudflare features, however, you may need to update the headers in your CSP:</p>
<table>
<thead>
<tr>
<th>Feature(s)</th>
<th>Updated headers</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a></td>
<td><code>script-src 'self' ajax.cloudflare.com;</code></td>
</tr>
<tr>
<td><a href="/waf/tools/scrape-shield/">Scrape Shield</a></td>
<td><code>script-src 'self' 'unsafe-inline'</code></td>
</tr>
<tr>
<td><a href="/web-analytics/">Web Analytics</a></td>
<td><code>script-src static.cloudflareinsights.com; connect-src cloudflareinsights.com</code></td>
</tr>
<tr>
<td><a href="/bots/">Bot products</a></td>
<td>Refer to <a href="/cloudflare-challenges/challenge-types/javascript-detections/#if-you-have-a-content-security-policy-csp">JavaScript detections and CSPs</a>.</td>
</tr>
<tr>
<td><a href="/client-side-security/">Client-side security</a> (formerly Page Shield)</td>
<td>Refer to <a href="/client-side-security/reference/csp-header/">CSP header format</a>.</td>
</tr>
<tr>
<td><a href="/zaraz/">Zaraz</a></td>
<td>No updates required (<a href="https://blog.cloudflare.com/cloudflare-zaraz-supports-csp/">details</a>).</td>
</tr>
<tr>
<td><a href="/turnstile/">Turnstile</a></td>
<td>Refer to <a href="/turnstile/reference/content-security-policy/">Turnstile CSP</a>.</td>
</tr>
</tbody>
</table>
