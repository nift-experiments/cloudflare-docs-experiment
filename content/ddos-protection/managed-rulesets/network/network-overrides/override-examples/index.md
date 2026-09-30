<h2 id="use-cases">Use cases</h2>
<p>The following scenarios detail how you can make use of override rules as a solution to common Network DDoS Protection issues.</p>
<h3 id="vpn-traffic-is-blocked-by-a-udp-rule">VPN traffic is blocked by a UDP rule</h3>
<p>If you have VPN traffic concentrated to a single or a few single destination IP addresses and the traffic is being blocked by a UDP rule, you can create an override rule for the UDP rule to the destination IPs or ranges.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7542.md")
</aside>
<h3 id="attack-traffic-is-flagged-by-the-adaptive-rule-based-on-udp-and-destination-port">Attack traffic is flagged by the adaptive rule based on UDP and destination port</h3>
<p>If you recognize that the traffic flagged by the adaptive rule based on UDP and destination port is an attack, you create an override rule to enable the adaptive rule in mitigation mode, setting the action to block the traffic.</p>
<h3 id="minimize-the-risk-of-false-positives-impacting-production-traffic">Minimize the risk of false positives impacting production traffic</h3>
<p>To avoid disruptions during initial deployment, you can create a <em>Log</em> only – <em>Essentially Off</em> ruleset override that allows all traffic while logging detection results. This lets you safely observe and analyze DDoS activity before enabling enforcement.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to the **DDoS protection** tab.
3. On **HTTP DDoS attack protection**, select **Create override**.
4. Set the **Scope** to _Apply to all incoming requests_.
5. Under **Ruleset configuration**:
    - Set the **Ruleset action** to _Log_.
    - Set the **Ruleset sensitivity** to _Essentially Off_. 
6. Select **Save**.
