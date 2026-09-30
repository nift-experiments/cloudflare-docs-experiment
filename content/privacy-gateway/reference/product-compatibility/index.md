<p>When <a href="/privacy-gateway/get-started/">using Privacy Gateway</a>, the majority of Cloudflare products will be compatible with your application.</p>
<p>However, the following products are not compatible:</p>
<ul>
<li><a href="/api-shield/">API Shield</a>: <a href="/api-shield/security/schema-validation/">Schema Validation</a> and <a href="/api-shield/security/api-discovery/">API discovery</a> are not possible since Cloudflare cannot see the request URLs.</li>
<li><a href="/cache/">Cache</a>: Caching of application content is no longer possible since each between client and gateway is end-to-end encrypted.</li>
<li><a href="/waf/">WAF</a>: Rules implemented based on request content are not supported since Cloudflare cannot see the request or response content.</li>
</ul>
