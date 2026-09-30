<h2 id="using-a-third-party-cdn-in-front-of-cloudflare">Using a third-party CDN in front of Cloudflare</h2>
<p>Some Cloudflare customers choose to use a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7465.md")
</div> in front of Cloudflare to cache and serve their resources.
<p>Cloudflare recommends that you <strong>do not use a third-party CDN in front of Cloudflare</strong>. Some CDN providers may introduce subtleties into HTTP requests that deviate from protocol standards and/or protocol best practices. Additionally, because traffic to Cloudflare will originate from a limited set of IP addresses of the third-party CDN, in rare occasions — such as when using the Akamai CDN in front of Cloudflare — it may appear as if the CDN is launching a DDoS attack against Cloudflare due to the amount of traffic from these limited IP addresses.</p>
<p>Therefore, it is recommended that you <strong>use the <a href="/cache/">Cloudflare CDN</a></strong>, which provides the following benefits:</p>
<ul>
<li>You remove an additional hop between vendor data centers, thus reducing latency for your users.</li>
<li>You perform DDoS filtering in the first point of contact from the Internet, which is a recommended best practice.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="l3-4-ddos-mitigation-accuracy">L3/4 DDoS mitigation accuracy</h3>
@markup("md", "content/.markup/bodies/7464.md")
</aside>
<p>If you require specific architectures involving third-party vendors, refer to our <a href="/reference-architecture/architectures/magic-transit/#deployment-architectures-for-magic-transit">Deployment architectures for Magic Transit</a> for detailed guidance on maintaining security posture in complex environments.</p>
<p>If you are using a third-party CDN in front of Cloudflare and Cloudflare mitigates a DDoS attack, you will still pay your first-hop CDN provider for the attack traffic that they processed before it was mitigated by Cloudflare.</p>
<h3 id="recommended-ddos-configuration-adjustments">Recommended DDoS configuration adjustments</h3>
<p>If you are using a CDN or proxy in front of Cloudflare, it is recommended that you change the action and/or sensitivity level of the following DDoS rules named:</p>
<ul>
<li><code>HTTP requests with unusual HTTP headers or URI path (signature #1)</code> with the rule ID <code class="nb-rule-id" title="0b1e17bd25c74e38834f19043486aee1">3486aee1</code></li>
<li><code>HTTP requests with unusual HTTP headers or URI path (signature #56)</code> with the rule ID <code class="nb-rule-id" title="466d6c2e8ba74459a2670e91e269dfd6">e269dfd6</code></li>
<li><code>HTTP requests with unusual HTTP headers or URI path (signature #57)</code> with the rule ID <code class="nb-rule-id" title="12b9aecf1f6245b29d7e842bf35a42a0">f35a42a0</code></li>
<li><code>Requests coming from known bad sources</code> with the rule ID <code class="nb-rule-id" title="6e3ccc23900c428e8ec0fb8a3a679c52">3a679c52</code></li>
</ul>
<p>You should change the rule's action to <em>Log</em> (only available on Enterprise plans) to view the flagged traffic in the <a href="/ddos-protection/reference/analytics/">analytics dashboard</a>. Alternatively, change the rule's <strong>Sensitivity Level</strong> to <em>Essentially Off</em> to prevent the rule from being triggered.</p>
<p>For more information, refer to <a href="/ddos-protection/managed-rulesets/http/#ruleset-configuration">HTTP DDoS Attack Protection managed ruleset: Ruleset configuration</a>.</p>
<h2 id="using-vpns-nats-and-other-third-party-services">Using VPNs, NATs, and other third-party services</h2>
<p>Some Cloudflare Magic Transit customers operate <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7466.md")
</div> so that their remote employees can connect securely to the organization's services. Additionally, larger organizations have Network Addressing Translation (NAT) systems that manage connections in and out of their network.
<p>Cloudflare Magic Transit customers may also use third-party services such as Zoom, Webex, Microsoft Teams, and others for their internal organization communication. Because traffic to Cloudflare will be originating from a limited set of IP addresses belonging to these third-party services, it may appear as if the services are launching a DDoS attack against Cloudflare due to the amount of traffic from limited IP addresses.</p>
<p>Additionally, since this traffic may also be targeting a limited set of destinations (for example, the same designated service ports, VPN endpoints, or NAT IP addresses), it may appear as if the CDN is launching a DDoS attack against Cloudflare due to the amount of traffic from a limited set of IPs <em>to</em> a limited set of IPs.</p>
<h3 id="recommended-ddos-configuration-adjustments-1">Recommended DDoS configuration adjustments</h3>
<p>If your organization uses VPNs, NATs, or third-party services at high rates of over 100 Mbps, it is recommended that you one of the following:</p>
<ul>
<li>Change the <strong>Sensitivity Level</strong> of the relevant rules to a lower level. Changing the level to <em>Essentially Off</em> will prevent the rules from being triggered. Refer to <a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection managed ruleset</a> and <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a> for more information on the available adjustments per ruleset and how to perform them.</li>
<li>Exclude the desired traffic from the Managed DDoS rule using expression filters. You can exclude a combination of source ports, source IP addresses, destination ports, destination IP addresses, and protocol. For more information, refer to <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-api/">Configure Network-layer DDoS Attack Protection via API</a>.</li>
</ul>
<p>If you are on an Enterprise plan, you can change a rule's action to <em>Log</em> to view the flagged traffic in the <a href="/ddos-protection/reference/analytics/">analytics dashboard</a>. After gathering this information, you can later define rule adjustments as previously described.</p>
