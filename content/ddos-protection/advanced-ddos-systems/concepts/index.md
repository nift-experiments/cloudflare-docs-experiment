<h2 id="prefixes">Prefixes</h2>
<p>Advanced DDoS Protection protects the IP prefixes you select from sophisticated DDoS attacks. A prefix can be an IP address or an IP range in CIDR format. You must add prefixes to Advanced DDoS Protection so that Cloudflare can analyze incoming <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7472.md")
</div> and offer protection against sophisticated TCP DDoS attacks.
<p>Prefixes added to Advanced DDoS Protection must be one of the following:</p>
<ul>
<li>A prefix <a href="/magic-transit/how-to/advertise-prefixes/">onboarded to Magic Transit</a>.</li>
<li>A subset of a prefix <a href="/magic-transit/how-to/advertise-prefixes/">onboarded to Magic Transit</a>.</li>
</ul>
<p>You cannot add a prefix (or a subset of a prefix) that you have not onboarded to Magic Transit or whose status is still <em>Unapproved</em>. Contact your account team to get help with prefix approvals.</p>
<h2 id="allowlist">Allowlist</h2>
<p>The Advanced DDoS Protection allowlist is a list of prefixes that will bypass all configured Advanced DDoS Protection rules.</p>
<p>For example, you could add prefixes used only by partners of your company to the allowlist so that they are exempt from packet inspection and mitigation actions performed by Advanced DDoS Protection.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7471.md")
</aside>
<h2 id="rule">Rule</h2>
<p>A rule configures Advanced DDoS Protection for a given <a href="/ddos-protection/advanced-ddos-systems/concepts/#scope">scope</a>, according to several <a href="/ddos-protection/advanced-ddos-systems/concepts/#rule-settings">settings</a>: execution mode, burst sensitivity, and rate sensitivity.</p>
<p>Each system component (SYN flood protection and out-of-state TCP protection) has its own list of rules, and it should have at least one rule.</p>
<h3 id="rule-settings">Rule settings</h3>
<p>Each rule type has the following settings: scope, mode, burst sensitivity, and rate sensitivity.</p>
<p>You may need to adjust the burst or rate sensitivity of a rule in case of false positives or due to specific traffic patterns.</p>
<h4 id="scope">Scope</h4>
<p>Advanced TCP Protection rules can have one of the following scopes:</p>
<ul>
<li><strong>Global</strong>: The rule will apply to all incoming packets.</li>
<li><strong>Region</strong>: The rule will apply to incoming packets in a selected region.</li>
<li><strong>Data center</strong>: The rule will apply to incoming packets in the selected Cloudflare data center.</li>
</ul>
<p>The rule scope allows you to adjust the system's tolerance for out-of-state packets in locations where you may have more or less traffic than usual, or due to any other networking reasons.</p>
<p>When multiple rules with different scopes apply to a data center, the rule with the most specific scope takes precedence. For example, if you have both a region rule (such as Western Europe) and a data center rule (such as Marseille), traffic through Marseille will be processed according to the data center rule.</p>
<p>Besides defining rules with one of the above scopes, you must also select the <a href="/ddos-protection/advanced-ddos-systems/concepts/#prefixes">prefixes</a> that you wish to protect with Advanced TCP Protection.</p>
<h4 id="mode">Mode</h4>
<p>The Advanced TCP Protection system constantly learns your TCP connections to mitigate DDoS attacks. Advanced TCP Protection rules can have one of the following execution modes: monitoring, mitigation (enabled), or disabled.</p>
<ul>
<li>
<p><strong>Monitoring</strong></p>
<ul>
<li>In this mode, Advanced TCP Protection will not impact any packets. Instead, the protection system will learn your legitimate TCP connections and show you what it would have mitigated. Check Network Analytics to visualize what actions Advanced TCP Protection would have taken on incoming packets, according to the current configuration.
Refer to the <a href="/analytics/network-analytics/configure/displayed-data/#view-logged-or-monitored-traffic">Analytics documentation</a> for more information on how to view logged or monitored traffic.</li>
</ul>
</li>
<li>
<p><strong>​​Mitigation (Enabled)</strong></p>
<ul>
<li>In this mode, Advanced TCP Protection will learn your legitimate TCP connections and perform mitigation actions on incoming TCP DDoS attacks based on the rule configuration (burst and rate sensitivity) and your <a href="/ddos-protection/advanced-ddos-systems/concepts/#allowlist">allowlist</a>.</li>
</ul>
</li>
<li>
<p><strong>Disabled</strong></p>
<ul>
<li>In this mode, a rule will not evaluate any incoming packets.</li>
</ul>
</li>
</ul>
<h4 id="burst-sensitivity">Burst sensitivity</h4>
<p>The burst sensitivity is the rule's sensitivity to short-term bursts in the packet rate:</p>
<ul>
<li>A low sensitivity means that bigger spikes in the packet rate may trigger a mitigation action.</li>
<li>A high sensitivity means that smaller spikes in the packet rate may trigger a mitigation action.</li>
</ul>
<p>The default burst sensitivity is <em>Medium</em>.</p>
<h4 id="rate-sensitivity">Rate sensitivity</h4>
<p>The rate sensitivity is the rule's sensitivity to the sustained packet rate:</p>
<ul>
<li>A low sensitivity means that higher sustained packet rates can trigger a mitigation action.</li>
<li>A high sensitivity means that lower sustained packet rates may trigger a mitigation action. A high sensitivity offers increased protection, but you may get more false positives (that is, mitigated packets that belong to legitimate traffic).</li>
</ul>
<p>The default rate sensitivity is <em>Medium</em>.</p>
<h4 id="profile-sensitivity">Profile sensitivity</h4>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7469.md")
</aside>
<p>The sensitivity to DNS queries that have not been recently seen.</p>
<ul>
<li>A higher sensitivity level means that the mitigation system will begin mitigating faster.</li>
<li>A lower sensitivity provides more tolerance for potentially suspicious DNS queries.</li>
</ul>
<p>The default profile sensitivity and recommended setting is <em>Low</em>. You should only increase sensitivity if it is needed based on observed attacks.</p>
<h2 id="filter">Filter</h2>
<p>A filter modifies Advanced TCP Protection's <a href="/ddos-protection/advanced-ddos-systems/concepts/#mode">execution mode</a> — monitoring, mitigation (enabled), or disabled — for all incoming packets matching an expression.</p>
<p>The filter expression can reference source and destination IP addresses and ports. Each system component (SYN flood protection and out-of-state TCP protection) should have one or more <a href="#rule">rules</a>, but filters are optional.</p>
<p>Each system component has its own filters. You can configure a filter for each execution mode:</p>
<ul>
<li><strong>Mitigation Filter</strong>: The system will drop packets matching the filter expression.</li>
<li><strong>Monitoring Filter</strong>: The system will log packets matching the filter expression.</li>
<li><strong>Off Filter</strong>: The system will ignore packets matching the filter expression.</li>
</ul>
<p>When there is a match, a filter will alter the execution mode for all configured rules in a given system component (SYN flood protection or out-of-state TCP protection), including disabled rules.</p>
<p>For instructions on creating filters in the Cloudflare dashboard, refer to <a href="/ddos-protection/advanced-ddos-systems/how-to/create-filter/">Create a filter</a>. For API examples, refer to <a href="/ddos-protection/advanced-ddos-systems/api/tcp-protection/examples/">Common API calls</a>.</p>
<h3 id="example-use-case">Example use case</h3>
<p>You can create a monitor filter for a new prefix that you are onboarding by using the expression to match against the prefix.</p>
<p>Your already onboarded prefixes can remain protected with one or more configured rules in mitigation mode.</p>
<p>When onboarding a new prefix, you would configure a monitoring filter for this prefix and then add it to Advanced TCP Protection.</p>
<hr />
<h2 id="determining-the-execution-mode">Determining the execution mode</h2>
<p>When you have both rules and filters configured, the execution mode is determined according to the following:</p>
<ol>
<li>If there is a match for one of the configured filters, use the filter's execution mode. The filter evaluation order is based on their mode, in the following order:
<ol>
<li>Mitigation filter (filter with <code>enabled</code> mode)</li>
<li>Monitoring filter (filter with <code>monitoring</code> mode)</li>
<li>Off filter (filter with <code>disabled</code> mode)</li>
</ol>
</li>
<li>If no filter matched, use the execution mode determined by existing rules.</li>
<li>If no rules match, disable Advanced TCP Protection.</li>
</ol>
<hr />
<h2 id="mitigation-reasons">Mitigation reasons</h2>
<p>The Advanced TCP Protection system applies mitigation actions for different reasons based on the connection states. The <strong>Mitigation reason</strong> field shown in the <strong>Advanced TCP Protection</strong> tab of the <a href="/analytics/network-analytics/">Network Analytics</a> dashboard will contain more information on why a given packet was dropped by the system.</p>
<p>The connection states are the following:</p>
<ul>
<li><strong>New</strong>: A SYN or SYN-ACK packet has been sent to attempt to open a new connection.</li>
<li><strong>Open</strong>: The three-way TCP handshake has been completed and the TCP connection is open.</li>
<li><strong>Closing</strong>: A FIN or FIN-ACK packet has been seen attempting to close a connection.</li>
<li><strong>Closed</strong>: The closing three-way handshake has been completed, or an RST packet has closed the connection.</li>
</ul>
<p>The mitigation reasons are the following:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Unexpected</strong></td>
<td>Packet dropped because it was not expected given the current state of the TCP connection it was associated with.</td>
</tr>
<tr>
<td><strong>Challenge needed</strong></td>
<td>Packet challenged because the system determined that the packet is most likely part of a packet flood.</td>
</tr>
<tr>
<td><strong>Challenge passed</strong></td>
<td>Packet dropped because it belongs to a solved challenge.</td>
</tr>
<tr>
<td><strong>Not found</strong></td>
<td>Packet dropped because it is not part of an existing TCP connection and it is not establishing a new connection.</td>
</tr>
<tr>
<td><strong>Out of sequence</strong></td>
<td>Packet dropped because its properties (for example, TCP flags or sequence numbers) do not match the expected values for the existing connection.</td>
</tr>
<tr>
<td><strong>Already closed</strong></td>
<td>Packet dropped because it belongs to a connection that is already closed.</td>
</tr>
</tbody>
</table>
<p>Mitigation will only occur based on your Advanced TCP Protection configuration (rule sensitivities, configured allowlists and prefixes). The protection system will provide some tolerance to out-of-state packets to accommodate for the natural randomness of Internet routing.</p>
