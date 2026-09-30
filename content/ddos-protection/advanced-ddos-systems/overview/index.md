<p>The Advanced DDoS Protection system includes <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a>, <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a>, and <a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a>. These systems are configured using the general settings, but also comprise of their own dedicated settings.
Advanced DDoS Protection systems is available to <a href="/magic-transit/">Magic Transit</a> customers.</p>
<p>Protection for simpler TCP or DNS-based DDoS attacks is included as part of the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a>.</p>
<p>General settings enable and control the use of the Advanced TCP Protection and the Advanced DNS Protection systems, and are composed of thresholds, prefixes, rules, and enablement.</p>
<h2 id="thresholds">Thresholds</h2>
<p>Thresholds are based on your network's unique traffic and are configured by Cloudflare. The sensitivity levels manipulate the thresholds. Thresholds apply to Advanced TCP Protection and Advanced DNS protection.</p>
<p>When you get access to Advanced DDoS Protection systems, you are <a href="#automatic-thresholds">automatically provisioned</a> with default settings in monitoring mode.</p>
<p>Thresholds are based on your network's individual behavior, derived from your traffic profile as monitored by Cloudflare. Defining the thresholds will effectively determine what the <em>High</em>, <em>Medium</em>, and <em>Low</em> <a href="/ddos-protection/advanced-ddos-systems/concepts/#burst-sensitivity">sensitivities</a> will be for your specific case.</p>
<p>If needed, you can change the sensitivity levels that will manipulate the thresholds for Advanced TCP Protection and Advanced DNS Protection from the default settings.</p>
<p>Once thresholds are configured, the Advanced DDoS Protection systems have been initialized and enabled in monitoring mode.</p>
<h3 id="automatic-thresholds">Automatic thresholds</h3>
<p>Automatic thresholds for Cloudflare's Advanced DDoS Protection system optimizes the detection and mitigation of DDoS attacks by automatically calculating appropriate traffic thresholds for each system for each customer account. This system applies to Advanced TCP Protection (specifically SYN Flood Protection and Out-of-State TCP Flood Protection) and Advanced DNS Protection.</p>
<p>Make sure that you have properly onboarded to the Advanced DDoS Protection system to benefit from automatic thresholds.</p>
<h4 id="process">Process</h4>
<p>The automatic threshold system calculates thresholds every 10 minutes for both new and existing Magic Transit accounts, provided they meet the requirements outlined in the process below.</p>
<ul>
<li>The <code>flowtrackd</code> account was created within the past 7 to 10 days.</li>
<li>The account has at least one configured global threshold (rate and burst). This can be a threshold that was automatically provisioned by the system or manually provisioned by Cloudflare.</li>
</ul>
<p>These checks are performed independently for SYN Flood Protection, Out-of-State TCP Flood Protection, and Advanced DNS Protection. The criteria does not require the presence of any rules to be configured. Accounts initially provisioned by the automatic system will have default thresholds. Otherwise, thresholds may be unconfigured if they are not set by Cloudflare.</p>
<p>After seven days, the system calculates a rate and burst threshold for each of the protection components. However, they are not applied. Cloudflare must review the draft thresholds produced by the automatic calculation system before creating real thresholds for your traffic.</p>
<p>Thresholds are applied globally per account. There is no minimum packets-per-second (pps) requirement for threshold calculation, but for those under 100 pps, the system will default to a reasonable non-zero rate and burst.</p>
<p>Thresholds are derived using the 95th percentile (P95) of observed traffic over the preceding seven days:</p>
<ul>
<li>SYN Flood Protection: Based on SYN and SYN-ACK traffic.</li>
<li>Out-of-State TCP Flood Protection: Based on all other TCP flag traffic.</li>
<li>Advanced DNS Protection: Based on DNS over UDP traffic.</li>
</ul>
<p>While the calculation typically occurs automatically after seven days, Cloudflare can force an earlier calculation if you want to enable the system in protective mode in advance.</p>
<p>The automatic threshold calculation system does not differentiate between legitimate and attack traffic. If you are onboarded or experience attacks during the seven day observation period, the calculated thresholds may be inaccurate, depending on the attack's size, duration, and frequency relative to legitimate traffic. In such cases, Cloudflare will likely need to trigger a recalculation. Future improvements will allow you to run a recalculation without the assistance of your Cloudflare account team.</p>
<h4 id="implementation">Implementation</h4>
<p>You should enable the automatically provisioned rules. Initially, these rules will have default values and operate in Monitor mode. After seven days, once thresholds are calculated, you can use the Network Analytics dashboard to observe what packets would have been dropped or allowed, then safely enable the rules in mitigation mode. Depending on what is observed in the Network Analytics dashboard (for example, legitimate traffic is being flagged in Monitor mode), you may want to change the sensitivity level and continue observation before enabling in mitigation mode. Rules and Filters, where supported, can also be scoped to allow for additional granularity.</p>
<h4 id="recalculation">Recalculation</h4>
<p>Automatic thresholds are calculated only once. Cloudflare can manually trigger a recalculation. Adding, approving, removing, delegating, advertising, or withdrawing prefixes after initial onboarding does not automatically re-trigger the calculation. It is recommended to move the relevant systems to Monitor mode before making changes that impact traffic levels and requesting a recalculation from Cloudflare. Future improvements will take these events into consideration.</p>
<h4 id="overrides">Overrides</h4>
<p>Automatically calculated thresholds can be overridden. Cloudflare can help manually define thresholds.</p>
<h4 id="considerations">Considerations</h4>
<p>If you are actively under attack and diverting traffic to Cloudflare, the automatic threshold calculation is unlikely to be effective as it will incorporate attack traffic. In these scenarios, Cloudflare will still need to manually configure thresholds. If you are not under attack while diverting traffic, Cloudflare can force a threshold calculation with available data. However, less data, such as fewer days or hours of observation, will result in less accurate thresholds.</p>
<h4 id="limitations">Limitations</h4>
<p>Customers currently do not have visibility into the calculated thresholds or an indication of whether thresholds have been configured. Future improvements aim to indicate when thresholds have been configured and when they were last updated.</p>
<p>The auto-threshold calculation component currently runs only in PDX. Therefore, this feature is not compatible if you have enabled Data Localization Services (DLS) and are located outside of the US, such as EU CMB. Future improvements will address this limitation.</p>
<hr />
<h2 id="prefixes">Prefixes</h2>
<p>The prefixes that you have <a href="/magic-transit/how-to/advertise-prefixes/">onboarded</a> to and approved by Cloudflare instruct the system on which traffic to route through the system. Prefixes apply to Advanced TCP Protection, Advanced DNS Protection, and Programmable Flow Protection.</p>
<p><a href="/ddos-protection/advanced-ddos-systems/how-to/add-prefix/">Add the prefixes</a> you would like to use with Advanced TCP and DNS Protection. You will be able to register prefixes that you previously <a href="/magic-transit/how-to/advertise-prefixes/">onboarded to Magic Transit</a> or a subset of these prefixes.</p>
<p>You cannot add unapproved prefixes to Advanced DDoS Protection systems. Contact your account team to get help with prefix approvals.</p>
<p>Optionally, you can <a href="/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/">add prefixes to the allowlist</a> if your traffic should bypass Advanced DDoS Protection rules.</p>
<p>The <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7491.md")
</div> only applies to source IPs — it does not apply to your own IPs or prefixes. You can also [exclude a subset of an onboarded prefix](/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/) from Advanced TCP Protection.
<p>Refer to <a href="/ddos-protection/advanced-ddos-systems/concepts/">Concepts</a> for more information.</p>
<hr />
<h2 id="rules">Rules</h2>
<p><a href="/ddos-protection/advanced-ddos-systems/how-to/create-rule/">Create a rule</a> for Advanced TCP Protection, Advanced DNS Protection, and Programmable Flow Protection to enable mitigation.</p>
<p>You can create a rule for SYN Flood Protection and another rule for Out-of-state TCP Protection, both with global scope and in monitoring mode. These rules will apply to all received <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7492.md")
</div>.
<p>Optionally, you can create <a href="/ddos-protection/advanced-ddos-systems/concepts/#filter">filters</a> for each protection system component (SYN flood protection and out-of-state TCP protection).
A filter modifies Advanced TCP Protection's <a href="/ddos-protection/advanced-ddos-systems/concepts/#mode">execution mode</a> — monitoring, mitigation (enabled), or disabled — for all incoming packets matching an expression.</p>
<hr />
<h2 id="enablement">Enablement</h2>
<p>Enable the Advanced DDoS system and begin routing traffic through it.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7493.md")
</div>
