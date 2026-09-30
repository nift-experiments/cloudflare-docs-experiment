<p>The DDoS Attack Protection managed rulesets provide comprehensive protection against a <a href="/ddos-protection/about/attack-coverage/">variety of DDoS attacks</a> across L3/4 (network layer) and L7 (application layer) of the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a>.</p>
<p>The available managed rulesets are:</p>
<ul>
<li>
<p><strong><a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection</a></strong></p>
<ul>
<li>This ruleset includes rules to detect and mitigate DDoS attacks over HTTP and HTTPS.</li>
</ul>
</li>
<li>
<p><strong><a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection</a></strong></p>
<ul>
<li>This ruleset includes rules to detect and mitigate DDoS attacks on L3/4 of the OSI model such as UDP floods, SYN-ACK reflection attacks, SYN Floods, and DNS floods.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="proactive-false-positive-detection-for-new-rules">Proactive false positive detection for new rules</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7459.md")
</aside>
<p>When Cloudflare creates a new managed rule, we check the rule impact against the traffic of Business and Enterprise zones while the rule is not blocking traffic yet.</p>
<p>If a <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-examples/#legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive">false positive</a> is detected, we proactively reach out to the affected customers and help them make configuration changes (for example, to lower the sensitivity level of the new rule) before the rule starts mitigating traffic. This prevents the new rule from causing service disruptions and outages to your Internet properties.</p>
