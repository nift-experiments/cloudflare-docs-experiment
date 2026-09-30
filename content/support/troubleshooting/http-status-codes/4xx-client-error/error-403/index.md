<h2 id="403-forbidden">403 Forbidden</h2>
<p>The <code>403 Forbidden</code> status code indicates that the client's request was understood by the server but cannot be fulfilled due to insufficient permissions to access the requested resource.
For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>If you encounter a <code>403</code> error without the Cloudflare branding, this means that the error is being returned directly by the origin web server, not Cloudflare. This is typically related to permission rules set on your server. Common reasons for this error are:</p>
<ul>
<li>Permission rules configured on the origin web server (for example, in an Apache <code>.htaccess</code> file).</li>
<li>Mod_security rules.</li>
<li>IP deny rules, such as blocking traffic from certain IP ranges. Make sure that <a href="https://www.cloudflare.com/ips">Cloudflare's IP ranges</a> are not being blocked.</li>
</ul>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare may serve <code>403</code> responses in the following scenarios:</p>
<ul>
<li>
<p><strong>WAF rules</strong>: The request violated a default WAF managed rule (enabled for all orange-clouded Cloudflare domains) or a custom WAF managed rule specific to your zone. For more information, refer to <a href="/waf/managed-rules/">WAF Managed Rules</a>.</p>
</li>
<li>
<p><strong>Security features</strong>: A <code>403</code> response with Cloudflare branding in the response body may be triggered by:</p>
<ul>
<li><a href="/waf/">WAF Custom or Managed Rules</a> with the challenge or block action.</li>
<li><a href="/waf/tools/security-level/">Security Level</a> settings, which default to Medium.</li>
<li><a href="/ddos-protection/">DDoS Protection</a>, which is enabled by default on zones onboarded to Cloudflare, IP applications onboarded to Spectrum, and IP Prefixes onboarded to Magic Transit.</li>
<li>Most <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">1xxx Cloudflare error codes</a>.</li>
<li>The <a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a>.</li>
<li><a href="/waf/tools/validation-checks/">Validation Checks</a>.</li>
</ul>
</li>
</ul>
<p>Cloudflare may also serve an unstyled <code>403</code> error page in specific cases. These errors are not logged because they occur early in Cloudflare's infrastructure, before domain configuration is loaded. An example is:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/ssl/what-is-sni/">SNI</a>: A <code>403</code> error is returned when the client sends a host that does not match the SNI (Server Name Indication).</li>
</ul>
