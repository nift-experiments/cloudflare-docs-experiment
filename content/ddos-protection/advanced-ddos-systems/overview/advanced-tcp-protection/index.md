<p>Cloudflare's Advanced TCP Protection, powered by <a href="https://blog.cloudflare.com/announcing-flowtrackd/"><code>flowtrackd</code></a>, is a stateful TCP inspection engine used to detect and mitigate sophisticated out-of-state TCP attacks such as randomized and spoofed ACK floods or SYN and SYN-ACK floods.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7494.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>Advanced TCP Protection can simultaneously protect against different kinds of attacks:</p>
<ul>
<li>Pinpointed attacks targeting a specific destination IP/port combination.</li>
<li>Broad attacks targeting multiple IP addresses of an IP prefix at the same time.</li>
</ul>
<p>Advanced TCP Protection can track TCP connections even when they move between Cloudflare data centers.</p>
<p>The feature offers two types of protection:</p>
<ul>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/#syn-flood-protection">SYN Flood Protection</a>: Protects against attacks such as fully randomized SYN and SYN-ACK floods.</li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/#out-of-state-tcp-protection">Out-of-state TCP Protection</a>: Protects against out-of-state TCP DDoS attacks such as fully randomized ACK floods and RST floods.</li>
</ul>
<p>Each protection type is configured independently using rules and (optionally) filters. You should configure at least one rule for each type of protection before enabling Advanced TCP Protection.</p>
<h3 id="syn-flood-protection">SYN Flood Protection</h3>
<p>This system protects against attacks such as fully randomized SYN and SYN-ACK floods. You should configure at least one SYN flood rule before enabling Advanced TCP Protection.</p>
<p>In mitigation mode, SYN flood rules will challenge new connection initiation requests (SYN, SYN-ACK) if they exceed the configured packet-per-second thresholds. The threshold should be higher than the normal rate of legitimate SYN and SYN-ACK packets that your network receives. Packets below the threshold will not be challenged. Using the <a href="/ddos-protection/advanced-ddos-systems/concepts/#rate-sensitivity">rate sensitivity</a> and <a href="/ddos-protection/advanced-ddos-systems/concepts/#burst-sensitivity">burst sensitivity</a> settings you can increase or decrease the tolerance of SYN and SYN-ACK packets.</p>
<p>For more information on the configuration settings of SYN flood rules, refer to <a href="/ddos-protection/advanced-ddos-systems/concepts/#rule-settings">Rule settings</a>.</p>
<h3 id="out-of-state-tcp-protection">Out-of-state TCP Protection</h3>
<p>This system protects against out-of-state TCP DDoS attacks such as fully randomized ACK floods and RST floods. You should configure one out-of-state TCP rule before enabling Advanced TCP Protection.</p>
<p>In mitigation mode, out-of-state TCP rules will drop out-of-state packets that do not belong to existing (and tracked) TCP connections if their rates exceed the configured thresholds. The threshold should be higher than the normal rate of non SYN or SYN-ACK TCP packets that your network receives. Packets below the threshold will not be evaluated. Using the <a href="/ddos-protection/advanced-ddos-systems/concepts/#rate-sensitivity">rate sensitivity</a> and <a href="/ddos-protection/advanced-ddos-systems/concepts/#burst-sensitivity">burst sensitivity</a> settings you can increase or decrease the tolerance of out-of-state TCP packets.</p>
<p>For more information on the configuration settings of out-of-state TCP rules, refer to <a href="/ddos-protection/advanced-ddos-systems/concepts/#rule-settings">Rule settings</a>.</p>
<hr />
<h2 id="setup">Setup</h2>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/#rules">Create a global configuration</a> to set up SYN Flood and Out-of-state TCP rules and filters for Advanced TCP Protection.</p>
