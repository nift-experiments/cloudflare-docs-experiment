<p>Protect your website or application from attacks, bots, and abuse. Cloudflare's application security (also known as Web Application Firewall or WAF) blocks SQL injection, XSS, and OWASP Top 10 vulnerabilities. DDoS Protection mitigates volumetric and application-layer attacks automatically. Bot Security uses machine learning to score every request. API Shield validates API traffic against your OpenAPI specification. Client-side security monitors third-party scripts for malicious behavior.</p>
<ul class="directory-listing"><li><a href="/use-cases/application-security/block-attacks/">Block application attacks</a></li><li><a href="/use-cases/application-security/ddos/">Mitigate DDoS attacks</a></li><li><a href="/use-cases/application-security/bots/">Stop malicious bots</a></li><li><a href="/use-cases/application-security/client-side/">Protect against client-side threats</a></li><li><a href="/use-cases/application-security/api-endpoints/">Secure API endpoints</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="web-application-security">Web application security</h3>
<p>Protect a website or web application from common attacks:</p>
<ul>
<li><strong>SSL/TLS</strong> encrypts all traffic between visitors and Cloudflare</li>
<li><strong>Security rules</strong> managed rulesets block SQL injection, XSS, and OWASP Top 10 vulnerabilities</li>
<li><strong>DDoS Protection</strong> mitigates volumetric and application-layer attacks automatically</li>
<li><strong>Bot Security</strong> scores every request and blocks automated threats</li>
</ul>
<h3 id="api-security">API security</h3>
<p>Secure Application Programming Interface (API) endpoints with schema enforcement and authentication:</p>
<ul>
<li><strong>API Shield</strong> validates requests against your OpenAPI specification</li>
<li><strong>Rate Limiting</strong> prevents abuse with per-endpoint request limits</li>
<li><strong>mTLS</strong> authenticates known clients with mutual TLS certificates</li>
</ul>
<h3 id="client-side-defense">Client-side defense</h3>
<p>Protect visitors from threats that execute in the browser:</p>
<ul>
<li><strong>Client-side security</strong> monitors third-party scripts loading on your pages</li>
<li><strong>Turnstile</strong> replaces CAPTCHAs on forms with a privacy-preserving challenge</li>
<li><strong>Content security rules</strong> block requests from known malicious sources</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a>. All solutions in this use case require your domain's DNS records to be proxied through Cloudflare so that traffic passes through Cloudflare's network before reaching your origin.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15243.md")
</div>
