<p>Another way of reducing origin traffic is customizing the Cloudflare WAF and other security features. The fewer malicious requests that reach your application, the fewer that could reach (and overwhelm) your origin.</p>
<p>To reduce incoming malicious requests, you could:</p>
<ul>
<li>Create <a href="/waf/custom-rules/">WAF custom rules</a> for protection based on specific aspects of incoming requests.</li>
<li>Adjust DDoS rules to handle <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-examples/">false negatives and false positives</a>.</li>
<li>Build <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to protect against specific patterns of requests.</li>
<li>Enable <a href="/bots/get-started/">bot protection</a> or set up <a href="/bots/get-started/bot-management/">Bot Management for Enterprise</a> to protect against automated abuse.</li>
<li>Explore <a href="/ddos-protection/managed-rulesets/network/">network-layer DDoS attack protection</a>.</li>
<li>Review the rest of Cloudflare's <a href="/learning-paths/application-security/account-security/">security options</a>.</li>
</ul>
