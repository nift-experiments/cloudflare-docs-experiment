<h2 id="automatic-rule-bypasses">Automatic rule bypasses</h2>
<p>Trace does not display rules that are automatically bypassed for operational reasons.</p>
<p>For example, when SSL/TLS certificates are in <code>pending_validation</code> status, security rules are automatically disabled for domain control validation (DCV) paths like <code>/.well-known/pki-validation/</code> and <code>/.well-known/acme-challenge/</code>. These bypasses will not appear in trace results.</p>
<p>For more information, refer to <a href="/waf/troubleshooting/faq/#why-are-some-rules-bypassed-when-i-did-not-create-an-exception">Why are some rules bypassed?</a> in the WAF documentation.</p>
<hr />
<h2 id="unsupported-features">Unsupported features</h2>
<p>Trace currently does not support:</p>
<ul>
<li>Hostnames using <a href="/data-localization/">Data Localization Suite</a></li>
<li><a href="/spectrum/">Spectrum</a> applications</li>
</ul>
<p>Additionally, the following products will not appear in trace results:</p>
<ul>
<li><a href="/firewall/">Firewall rules (deprecated)</a></li>
<li><a href="/load-balancing/">Load Balancing</a> and <a href="/load-balancing/additional-options/load-balancing-rules/">Load Balancer Custom Rules</a></li>
<li><a href="/waf/tools/ip-access-rules/">IP Access rules</a></li>
<li><a href="/waf/reference/legacy/old-rate-limiting/">Rate limiting rules (previous version)</a></li>
<li><a href="/waf/reference/legacy/old-waf-managed-rules/">WAF managed rules (previous version)</a></li>
<li><a href="/client-side-security/rules/">Content security rules</a></li>
</ul>
