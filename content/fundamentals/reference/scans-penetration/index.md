<p>Customers may conduct scans and penetration tests (with certain restrictions) on application and network-layer aspects of their own assets, such as their <a href="/fundamentals/concepts/accounts-and-zones/#zones">zones</a> within their Cloudflare accounts, provided they adhere to Cloudflare's policy.</p>
<h2 id="permitted-targets">Permitted targets</h2>
<p>All scans or testing must be limited to the following:</p>
<ul>
<li>Customer-owned IPs</li>
<li>Cloudflare's designated public IPs</li>
<li>The customer's registered DNS entries</li>
</ul>
<p>Targets like <code>*.cloudflare.com</code> or other Cloudflare-owned destinations are only allowed as part of Cloudflare's Public Bug Bounty program. Refer to the <a href="#additional-resources">Additional resources</a> section for more information.</p>
<h2 id="scans">Scans</h2>
<ul>
<li><strong>Throttling</strong>: Scans should be throttled to a reasonable rate to prevent disruptions and ensure stable system performance.</li>
<li><strong>Scope and intent</strong>: Scans should identify the presence of vulnerabilities without attempting to actively exploit any detected weaknesses.</li>
<li><strong>Exclusions</strong>: It is recommended to exclude <a href="/fundamentals/reference/cdn-cgi-endpoint/"><code>/cdn-cgi/</code> endpoints</a> from scans to avoid false positives or irrelevant results.</li>
<li><strong>Compliance checks</strong>: Customers may conduct <a href="/fundamentals/security/pci-scans/">PCI compliance scans</a> or verify that <a href="/ssl/reference/compliance-and-vulnerabilities/#known-vulnerabilities-mitigations">known vulnerabilities</a> have been addressed.</li>
</ul>
<h2 id="penetration-tests">Penetration tests</h2>
<p>Before starting a penetration test on your <a href="/fundamentals/concepts/accounts-and-zones/#zones">zones</a>, set the following application security configurations for each zone you will run the test on:</p>
<ol>
<li>
<p><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/#deploy-in-the-dashboard">Deploy the Cloudflare Managed Ruleset</a> and
<a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/#ruleset-level-configuration">enable all rules</a> in the ruleset by setting <strong>Ruleset status</strong> to <strong>Enabled</strong>.</p>
</li>
<li>
<p><a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#deploy-in-the-dashboard">Deploy the Cloudflare OWASP Core Ruleset</a> and set the following <a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#ruleset-level-configuration">ruleset configuration</a>:</p>
<ul>
<li><strong>Paranoia Level</strong>: <em>PL4</em></li>
<li><strong>Score threshold</strong>: <em>High - 25 and higher</em></li>
</ul>
</li>
<li>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> based on the <a href="/waf/detections/attack-score/">WAF attack score</a> to block requests considered as an attack (WAF attack score between 1 and 20). Refer to the <a href="/waf/detections/attack-score/#1-create-a-custom-rule">WAF attack score</a> documentation for an example.</p>
</li>
<li>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> based on <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a> to block requests containing <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/8775.md")
</div> considered malicious. Refer to [Example rules](/waf/detections/malicious-uploads/example-rules/#block-requests-to-uri-path-with-a-malicious-content-object) for examples of custom rules used to mitigate this kind of threat.
<ol start="5">
<li>
<p>On Pro and Business plans without Bot Management, <a href="/bots/get-started/super-bot-fight-mode/#enable-super-bot-fight-mode">enable Super Bot Fight Mode</a>.<br/>
Customers with access to Bot Management should make sure that <a href="/bots/get-started/bot-management/#enable-bot-management-for-enterprise">Bot Management is enabled</a> (it is enabled by default on entitled zones).</p>
</li>
<li>
<p><a href="/waf/rate-limiting-rules/create-zone-dashboard/">Create rate limiting rules</a> to protect key endpoints of the zone being tested. Refer to <a href="/waf/rate-limiting-rules/use-cases/">Rate limiting rule examples</a> and <a href="/waf/rate-limiting-rules/best-practices/">Rate limiting best practices</a> for example configurations.</p>
</li>
</ol>
<p>Be aware that other Cloudflare security and performance features, configurations, and rules active on your account or zone can influence test results.</p>
<p>After completing the test, it is recommended that you review your security posture and make any necessary adjustments based on the findings.</p>
<h3 id="important-remarks">Important remarks</h3>
<ul>
<li>
<p>Cloudflare's <a href="/fundamentals/concepts/how-cloudflare-works/">anycast network</a> will report ports other than <code>80</code> and <code>443</code> as open due to its shared infrastructure and the nature of Cloudflare's proxy. The reporting is expected behavior and does not indicate a vulnerability.</p>
</li>
<li>
<p>Tools like Netcat may list <a href="/fundamentals/reference/network-ports/">non-standard HTTP ports</a> as open; however, these ports are open solely for Cloudflare's routing purposes and do not necessarily indicate that a connection can be established with the customer's origin over those ports.</p>
</li>
<li>
<p><strong>Known false positives</strong>: Any findings related to the <a href="/ssl/reference/compliance-and-vulnerabilities/#return-of-bleichenbachers-oracle-threat-robot">ROBOT vulnerability</a> are false positives when the customer's assets are behind Cloudflare.</p>
</li>
</ul>
<h2 id="denial-of-service-dos-tests">Denial-of-Service (DoS) tests</h2>
<p>For guidelines on required notification and necessary information, refer to <a href="/ddos-protection/reference/simulate-ddos-attack/">Simulating test DDoS attacks</a>. Customers should also familiarize themselves with Cloudflare's <a href="/ddos-protection/best-practices/">DDoS protection best practices</a>.</p>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li>Customers can download the latest Penetration Test Report of Cloudflare via the <a href="/fundamentals/reference/policies-compliances/compliance-docs/">dashboard</a>.</li>
<li>For information about Cloudflare's Public Bug Bounty program, visit <a href="https://hackerone.com/cloudflare">HackerOne</a>.</li>
</ul>
