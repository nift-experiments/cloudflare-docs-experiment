<h2 id="onboard-prefixes">Onboard prefixes</h2>
<p>You can bring your own public IP addresses to Cloudflare to use with Magic Transit. This is also known as bring your own IP (BYOIP). This process involves two distinct types of prefixes:</p>
<ol>
<li><strong>IP prefixes</strong>: Each IP address block you bring to Cloudflare requires an IP prefix entry. The IP prefix includes the permission (<div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/10703.md")
</div>) that allows Cloudflare to announce the network or its subnets. You can also define your optional [Autonomous System Number (ASN)](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) to be included in our advertised AS path.
2. **BGP prefixes**: These control which prefixes Cloudflare announces from its global network. By default, each IP prefix has one matching BGP prefix. You can configure additional, more-specific BGP prefixes (subnets of the IP prefix), up to a maximum prefix length of `/24`.
<h3 id="ip-prefixes">IP prefixes</h3>
<p>Cloudflare measures the Magic Transit prefix count based on the number of BGP prefixes you define. Each prefix is billed separately, even if they overlap. For example, both a <code>/16</code> and any <code>/24</code> within it are counted individually. Onboarding a larger aggregate prefix does not automatically include its smaller subnets for announcement or billing purposes.</p>
<p>There is no billing limit on the accepted prefix sizes. However, only prefixes up to <code>/24</code> are accepted for onboarding because longer prefixes (like <code>/25</code>, <code>/26</code>) are not globally routable.</p>
<p>Provide all IP prefixes you plan to onboard, along with the ASNs from which you will advertise them. When specifying prefixes, observe these guidelines:</p>
<ul>
<li>Prefixes must include at least 256 IP addresses (<code>/24</code> in CIDR (<a href="https://www.cloudflare.com/learning/network-layer/what-is-routing/">Classless Inter-Domain Routing</a>) notation). If you do not meet the <code>/24</code> prefix length requirement, refer to <a href="/magic-transit/cloudflare-ips/">Use a Cloudflare IP</a>.</li>
<li>Internet Routing Registry entries and LOA must match the prefixes and originating prefixes you submit to Cloudflare.</li>
<li>When using contiguous prefixes, specify aggregate prefixes where possible.</li>
<li>When using Route Origin Authorizations (ROAs) to sign routes for <a href="https://tools.ietf.org/html/rfc8210">resource public key infrastructure (RPKI)</a>, the prefix and originating ASN must match the onboarding submission.</li>
<li>If you do not own an ASN, you can use the Cloudflare Customer ASN (AS13335).</li>
</ul>
<h4 id="cloudflare-asn-vs-your-own-asn">Cloudflare ASN vs. your own ASN</h4>
<p>As part of your IP prefix onboarding process, you need to decide which ASN Cloudflare will use to announce your prefixes. If you supply your own ASN, Cloudflare prepends the main Cloudflare ASN (AS13335) to the BGP <code>AS_PATH</code>. For example, if your ASN is <code>AS64496</code>, anyone directly peering with Cloudflare sees the path as <code>13335 64496</code>.</p>
<p>If you do not have an ASN or do not want to bring your ASN to Cloudflare, you can use the Cloudflare Customer ASN (AS13335).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10702.md")
</aside>
<h3 id="bgp-prefixes">BGP prefixes</h3>
<p>BGP prefixes represent the prefix that Cloudflare will announce through anycast from Cloudflare's global network. By default, there is always at least one BGP prefix that is identical to the onboarded IP prefix.</p>
<p>For example, if you onboard a <code>/20</code> IP prefix to Magic Transit, it can only be announced as a <code>/20</code> because there is only the default <code>/20</code> BGP prefix. Smaller sub-prefixes (such as <code>/24s</code>) within that <code>/20</code> cannot be announced individually unless they are configured as separate BGP prefixes.</p>
<h3 id="bgp-prefix-advertisement-control-methods">BGP prefix advertisement control methods</h3>
<p>Cloudflare offers multiple mechanisms to control the announcement and withdrawal of on-demand prefixes. Each method serves different deployment scenarios:</p>
<ul>
<li><strong>Addressing API</strong>: Manually control prefix advertisements through API calls. Refer to <a href="#advertise-or-withdraw-a-bgp-prefix">Advertise or withdraw a BGP prefix</a>.</li>
<li><strong>BGP peering with route reflectors</strong>: Control advertisements through BGP sessions to Cloudflare's globally distributed route reflectors, either over the Internet or over a CNI connection with Dataplane v1. Contact your Cloudflare account team if you need this option. Refer to <a href="#bgp-control-with-cloudflare-route-reflectors">BGP control with Cloudflare Route Reflectors</a>.</li>
<li><strong>Network Flow</strong>: Automatically announce prefixes based on user-defined traffic thresholds observed in your network. Refer to <a href="/network-flow/">Network Flow</a> (formerly Magic Network Monitoring).</li>
<li><strong>BGP peering with Magic Transit Virtual Network routing table</strong>: Automatically control prefix advertisements based on BGP routes learned through CNI with Dataplane v2, or GRE and IPsec tunnels (beta, requires <a href="/magic-transit/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a>). Refer to <a href="#bgp-control-to-magic-transit-virtual-network-routing-table">BGP control to Magic Transit Virtual Network routing table</a>.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/10701.md")
</aside>
<h2 id="manage-bgp-prefixes">Manage BGP prefixes</h2>
<h3 id="add-a-bgp-prefix">Add a BGP prefix</h3>
<p>Create a <a href="/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/create/">POST request</a> to add a BGP prefix. For example:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;cidr&quot;: &quot;192.0.2.0/24&quot;&#10;}&#x27;</code></pre>
<h3 id="advertise-or-withdraw-a-bgp-prefix">Advertise or withdraw a BGP prefix</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10706.md")
</div></div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning-isp-route-refresh-delays-may-impact-traffic">Warning: ISP route refresh delays may impact traffic</h3>
@markup("md", "content/.markup/bodies/10699.md")
</aside>
<h3 id="delete-an-ip-prefix">Delete an IP prefix</h3>
<p>You can only delete a prefix with an <em>Unapproved</em> status. To delete prefixes with a different status, contact your administrator or account manager.</p>
<ol>
<li>Go to the <strong>Routes</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>From the <strong>IP Prefixes</strong> tab, locate the prefix you want to modify and select <strong>Delete</strong>.</li>
<li>Confirm your choice from the modal by selecting <strong>Delete</strong>.</li>
</ol>
<h3 id="use-the-api-to-set-as-prepends-on-a-bgp-prefix">Use the API to set AS prepends on a BGP prefix</h3>
<p>Use the <a href="/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/edit/">Addressing API</a> to control the number of times Cloudflare prepends its Autonomous System Number (ASN) to a prefix. You can prepend AS13335 up to three times in the <code>AS_PATH</code> of BGP updates for your prefixes.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10698.md")
</aside>
<p>Refer to the following example for how to prepend AS13335 three times to a BGP prefix:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;asn_prepend_count&quot;: 3&#10;}&#x27;</code></pre>
<p>AS prepending helps you gracefully transition traffic between network providers. By adding prepends to Cloudflare's advertisement, you make the route through Cloudflare less preferred for some Internet network providers. This allows you to simultaneously advertise the same prefix from an alternate provider with a shorter, more desirable <code>AS_PATH</code>. Advertising from both providers at once provides a smoother traffic migration and minimizes packet loss during a change of provider.</p>
<p>The <code>&quot;asn_prepend_count&quot;</code> parameter accepts values from <code>0</code> to <code>3</code>. A higher value makes the route less preferred. You can also change this parameter using BGP. Refer to <a href="#use-communities-to-set-as-prepends-on-an-anycast-prefix">Use communities to set AS prepends on an anycast prefix</a>.</p>
<p>When you use AS prepending to migrate traffic away from Magic Transit, the typical sequence of events is as follows:</p>
<ul>
<li><strong>Initial state</strong>: Cloudflare advertises your prefix with the default priority (<code>&quot;asn_prepend_count&quot;: 0</code>). Cloudflare routes all traffic to your network through the Cloudflare global network.</li>
<li><strong>Deprioritize Cloudflare</strong>: You update the prefix through the API to set an AS prepend count (for example, <code>&quot;asn_prepend_count&quot;: 3</code>). Cloudflare now advertises your prefix with a longer <code>AS_PATH</code>. External networks will update their BGP tables to recognize the Cloudflare path has the new, longer <code>AS_PATH</code>.</li>
<li><strong>Introduce new provider</strong>: You begin advertising the same prefix from your alternate provider with a standard (shorter) <code>AS_PATH</code>.</li>
<li><strong>Final state</strong>: External networks now receive two advertisements: the prepended route through Cloudflare and the non-prepended route through your new provider. The external network will select a path based on its BGP policy rules.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10697.md")
</aside>
<h2 id="safely-withdraw-a-byoip-prefix">Safely withdraw a BYOIP prefix</h2>
<h3 id="mitigating-stuck-bgp-routes">Mitigating stuck BGP routes</h3>
<p>When you prepare to remove traffic for a <a href="/byoip/">Bring Your Own IP (BYOIP)</a> prefix from the Cloudflare edge, a direct BGP withdrawal action carries the risk of a stuck BGP route. This state occurs when a route becomes stuck in the Internet's <a href="https://en.wikipedia.org/wiki/Default-free_zone">Default-Free Zone (DFZ)</a>. Core routers that missed the withdrawal announcement continue forwarding traffic to a now-inactive next-hop (what is known as a blackhole). You can read more about this in our blog post <a href="https://blog.cloudflare.com/going-bgp-zombie-hunting">BGP zombies and excessive path hunting</a>.</p>
<p>This risk is especially evident in the use case where the global routing table relies on more-specific to less-specific prefix routing fallback. Since this fallback mechanism is highly prone to route instability, Cloudflare recommends a multi-step draining process.</p>
<h3 id="multi-step-byoip-withdrawal-process">Multi-step BYOIP withdrawal process</h3>
<p>When draining traffic, use the same prefix length on Cloudflare and on your ISP (Internet Service Provider), since matching prefix lengths gives the most effective and deterministic behavior.</p>
<p>The following steps outline the recommended multi-step draining process to achieve a clean traffic cutover and prevent blackholing.</p>
<ol>
<li><strong>Initiate advertisement from your origin network</strong>: Begin announcing the exact same-length prefix (for example, <code>192.0.2.0/24</code>) from your local infrastructure to your upstream Internet Service Providers (ISPs). This action introduces a competing route of the same length into the global routing table. BGP best path selection will favor your native route based on other metrics (for example, shorter AS path length or local preference), allowing traffic to begin draining away from the Cloudflare edge. Note that some of your traffic may not route as expected, since this depends on how your ISP prefers routes (for example, the Cloudflare route may be treated as a less-preferred path if not fully withdrawn).</li>
<li><strong>Wait for global BGP convergence</strong>: Allow a period of time (typically five to ten minutes) for the new native advertisement to propagate fully across the global routing table, and for routes to converge. This passive waiting period ensures that the majority of traffic has shifted to your local network before the next step.</li>
<li><strong>Signal BGP withdrawal from the Cloudflare edge</strong>: Once you have verified that traffic has successfully drained, use one of the BGP control methods to stop the advertisement of the prefix from the Cloudflare edge.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="isp-route-refresh-delays-may-impact-traffic">ISP route refresh delays may impact traffic</h3>
@markup("md", "content/.markup/bodies/10696.md")
</aside>
<ol start="4">
<li>The draining process is complete.</li>
</ol>
<h2 id="bgp-control-to-magic-transit-virtual-network-routing-table">BGP control to Magic Transit Virtual Network routing table</h2>
<h3 id="automatically-announce-and-withdraw-anycast-based-magic-bgp-routes">Automatically announce and withdraw anycast-based Magic BGP routes</h3>
<p>If you use CNI with Dataplane v2, GRE or IPsec tunnels, you can:</p>
<ul>
<li>Automatically withdraw your prefixes from Cloudflare's global edge infrastructure when you withdraw all matching BGP learned prefixes from the Magic Transit Virtual Network routing table.</li>
<li>Automatically advertise your prefixes through Cloudflare's global edge infrastructure when you have at least one matching BGP learned prefix in the Magic Transit Virtual Network routing table.</li>
</ul>
<p>To enable automatic global announcement and withdrawal, enable this feature on the BGP prefix using the <a href="/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/edit/">Addressing API</a>. For example:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;auto_advertise_withdraw&quot;: true&#10;}&#x27;</code></pre>
<p>Once you configure this for a BGP prefix, Cloudflare applies the following logic:</p>
<ul>
<li>If there are no BGP routes in the Magic Transit Virtual Network routing table exactly matching the BGP prefix, Cloudflare withdraws the BGP prefix.</li>
<li>If there is at least one BGP route in the Magic Transit Virtual Network routing table exactly matching the BGP prefix, Cloudflare announces the BGP prefix.</li>
</ul>
<p>The Addressing API BGP prefix and the Magic Transit Virtual Network routing table BGP route must match exactly (same IP prefix and CIDR prefix length). If there is a valid route to a subnet or supernet, Cloudflare withdraws the BGP prefix when there are no exactly matching Magic Transit Virtual Network BGP routes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10695.md")
</aside>
<h3 id="use-communities-to-set-as-prepends-on-an-anycast-prefix">Use communities to set AS prepends on an anycast prefix</h3>
<p>As an alternative to setting <a href="#use-the-api-to-set-as-prepends-on-a-bgp-prefix">AS prepends on an anycast prefix with the API</a>, you can use BGP communities to control the number of AS prepends that Cloudflare announces from its edge for your prefix. The community values are:</p>
<ul>
<li><code>13335:50101</code>: Prepends one time with the 13335 ASN</li>
<li><code>13335:50102</code>: Prepends two times with the 13335 ASN</li>
<li><code>13335:50103</code>: Prepends three times with the 13335 ASN</li>
</ul>
<p>If you need to switch to your alternate service provider, you can prepend Cloudflare's ASN multiple times. The intent is typically to make the route less preferred and allow for a graceful transition to the new provider. The higher the prepend count, the less preferred Cloudflare's connection will be if there are no other prioritization rules in place.</p>
<p>Refer to the <a href="#use-the-api-to-set-as-prepends-on-a-bgp-prefix">caution about AS prepends</a> for important information about peer behavior with this feature.</p>
<h2 id="bgp-control-with-cloudflare-route-reflectors">BGP control with Cloudflare Route Reflectors</h2>
<p>Optionally, you can use BGP to control the advertisement status of your prefix — advertised or withdrawn — from Cloudflare's global network for on-demand deployment scenarios. BGP control works by establishing BGP sessions to Cloudflare's globally distributed Route Reflectors, which initiate propagation of your prefix advertisement across Cloudflare's global network. You can peer with Cloudflare's Route Reflectors through Internet or CNI. CNI peering is available through your account team.</p>
<p>You can advertise prefixes from Cloudflare's network in a supported on-demand method such as BGP control, or dynamically through the UI, API, or <a href="/magic-transit/network-flow/">Network Flow</a>. During the onboarding of your on-demand prefixes, specify whether you want BGP-controlled advertisement or dynamic advertisement (through dashboard/API/Network Flow).</p>
<p>Our network architecture utilizes multiple, redundant Route Reflectors. The failure of any single reflector does not impact overall network resiliency or traffic forwarding. For maximum resiliency, we recommend peering with all three of Cloudflare's redundant Route Reflectors.</p>
<p>To begin using BGP control, contact your account team with the following information:</p>
<ul>
<li>BGP endpoint IP addresses</li>
<li>Prefixes you want to use with BGP control</li>
<li>Your ASN for the BGP session</li>
</ul>
<p>After receiving your information, Cloudflare will update firewall filters to establish the BGP session and provide you with the BGP endpoints to control your prefixes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10694.md")
</aside>
<h3 id="example-router-configurations">Example router configurations</h3>
<p>The following examples show peering configurations for <a href="https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book.html">Cisco IOS</a> and <a href="https://www.juniper.net/documentation/us/en/software/junos/cli/index.html">Juniper Junos OS</a> for on-demand deployments leveraging BGP control. The IP addresses used are from Cloudflare's route reflectors and should be left as is.</p>
<h4 id="cisco-ios">Cisco IOS</h4>
<pre><code class="language-txt">ip route {{ &lt;YOUR-MAGIC-TRANSIT-PREFIX&gt; }} Null0&#10;ip prefix-list magic-transit-prefix seq 5 permit {{ &lt;YOUR-MAGIC-TRANSIT-PREFIX&gt; }}&#10;&#10;route-map cloudflare-magic-transit-out permit 1&#10;match ip address prefix-list magic-transit-prefix&#10;!&#10;route-map cloudflare-magic-transit-out deny 99&#10;&#10;route-map reject-all deny 99&#10;&#10;router bgp {{ &lt;YOUR-ASN&gt; }}&#10;neighbor 141.101.67.22 remote-as 13335&#10;neighbor 141.101.67.22 ebgp-multihop 64&#10;neighbor 141.101.67.22 timers 60 900&#10;neighbor 162.158.160.22 remote-as 13335&#10;neighbor 162.158.160.22 ebgp-multihop 64&#10;neighbor 162.158.160.22 timers 60 900&#10;neighbor 173.245.63.66  remote-as 13335&#10;neighbor 173.245.63.66  ebgp-multihop 64&#10;neighbor 173.245.63.66  timers 60 900&#10;!&#10;address-family ipv4 unicast&#10;redistribute static&#10;neighbor 141.101.67.22 route-map cloudflare-magic-transit-out out&#10;neighbor 141.101.67.22 route-map reject-all in&#10;neighbor 162.158.160.22 route-map cloudflare-magic-transit-out out&#10;neighbor 162.158.160.22 route-map reject-all in&#10;neighbor 173.245.63.66  route-map cloudflare-magic-transit-out out&#10;neighbor 173.245.63.66  route-map reject-all in&#10;exit-address-family&#10;</code></pre>
<h4 id="juniper-mx-junos-os-set-commands">Juniper MX (Junos OS set commands)</h4>
<pre><code class="language-txt">set protocols bgp group CF_ROUTE_REFLECTORS neighbor 162.158.160.22 description &quot;CF RR#1 SIN&quot;&#10;set protocols bgp group CF_ROUTE_REFLECTORS neighbor 173.245.63.66 description &quot;CF RR#2 IAD&quot;&#10;set protocols bgp group CF_ROUTE_REFLECTORS neighbor 141.101.67.22 description &quot;CF RR#3 CDG&quot;&#10;set protocols bgp group CF_ROUTE_REFLECTORS peer-as 13335&#10;set protocols bgp group CF_ROUTE_REFLECTORS import REJECT-ALL&#10;set protocols bgp group CF_ROUTE_REFLECTORS export BGP-CONTROL-OUT&#10;&#10;set policy-options policy-statement REJECT-ALL then reject&#10;set policy-options policy-statement BGP-CONTROL-OUT term &lt;TERM-NAME&gt; from route-filter 104.245.62.0/24 exact&#10;set policy-options policy-statement BGP-CONTROL-OUT term &lt;TERM-NAME&gt; from protocol static&#10;set policy-options policy-statement BGP-CONTROL-OUT term &lt;TERM-NAME&gt; from route-type internal&#10;set policy-options policy-statement BGP-CONTROL-OUT term &lt;TERM-NAME&gt; then accept&#10;set policy-options policy-statement BGP-CONTROL-OUT then reject&#10;</code></pre>
<h4 id="juniper-mx-junos-os-xml-format">Juniper MX (Junos OS XML format)</h4>
<pre><code class="language-txt">@rtr01&gt; show configuration routing-instances STAGE protocols bgp group CF_ROUTE_REFLECTORS&#10;type external;&#10;multihop {&#10;    ttl 64;&#10;}&#10;local-address {{customer router IP}}&#10;import NONE;&#10;export NONE;&#10;peer-as 13335;&#10;local-as {{customer AS}} loops 2;&#10;neighbor 162.158.160.22 {&#10;    description &quot;CF RR#1 SIN&quot;;&#10;}&#10;neighbor 173.245.63.66 {&#10;    description &quot;CF RR#2 IAD&quot;;&#10;}&#10;neighbor 141.101.67.22 {&#10;    description &quot;CF RR#3 CDG&quot;;&#10;}&#10;</code></pre>
<h2 id="bgp-peering">BGP peering</h2>
<p>If you use CNI with Dataplane v2, GRE or IPsec tunnels to on-ramp your network traffic to Magic Transit, refer to <a href="/magic-transit/reference/traffic-steering/#bgp-information">BGP information</a> to learn how to use BGP to handle traffic routing between Cloudflare and your network. Note that this is a different option to using BGP as a means to control the advertisement status of your prefix.</p>
<h2 id="regional-settings">Regional settings</h2>
<p>Magic Transit supports both static routing and BGP to steer traffic from Cloudflare's network to your configured off-ramps (GRE tunnels, IPsec tunnels, or CNI). Cloudflare does not currently support advertisement of routes for traffic engineering purposes. As a best practice to reduce last-hop latency, consider scoping your routes regionally.</p>
<p>Cloudflare has nine geographic regions:</p>
<table>
<thead>
<tr>
<th>Region code</th>
<th>Region</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AFR</code></td>
<td>Africa</td>
</tr>
<tr>
<td><code>APAC</code></td>
<td>Asia Pacific</td>
</tr>
<tr>
<td><code>EEUR</code></td>
<td>Eastern Europe</td>
</tr>
<tr>
<td><code>ENAM</code></td>
<td>Eastern North America</td>
</tr>
<tr>
<td><code>ME</code></td>
<td>Middle East</td>
</tr>
<tr>
<td><code>OC</code></td>
<td>Oceania</td>
</tr>
<tr>
<td><code>SAM</code></td>
<td>South America</td>
</tr>
<tr>
<td><code>WEUR</code></td>
<td>Western Europe</td>
</tr>
<tr>
<td><code>WNAM</code></td>
<td>Western North America</td>
</tr>
</tbody>
</table>
<p>The default setting for static route regions is <strong>All Regions</strong>. Configure scoping for your traffic in the <strong>Region code</strong> section when <a href="/magic-transit/how-to/configure-routes/#create-a-static-route">adding</a> or <a href="/magic-transit/how-to/configure-routes/#edit-a-static-route">editing</a> a static route.</p>
<p>Refer to <a href="/magic-transit/reference/traffic-steering/#scoping-routes-to-specific-regions">Scoping routes to specific regions</a> for more information.</p>
