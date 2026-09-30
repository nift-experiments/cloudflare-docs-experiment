<p>If you cannot find your answer here, refer to the <a href="https://community.cloudflare.com/">community page</a> for more resources.</p>
<h2 id="i-am-getting-an-invalid-account-settings-request-body-account-name-format-contains-illegal-characters-or-is-not-supported-error-when-trying-to-create-a-rule">I am getting an &quot;Invalid account settings request body: account name format contains illegal characters or is not supported&quot; error when trying to create a rule.</h2>
<p>This probably means that your account name has unsupported characters. Make sure your account name does not have characters like, for example, <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, <code>'</code>, <code>`</code>.</p>
<p>Refer to <a href="/fundamentals/account/create-account/#account-name">Account name</a> to learn how to change your account name.</p>
<h2 id="can-i-send-netflow-sflow-data-to-cloudflare-in-a-secure-encrypted-way">Can I send NetFlow/sFlow data to Cloudflare in a secure, encrypted way?</h2>
<p>Yes. Both enterprise and free customers can send encrypted network flow data to Cloudflare.</p>
<p>Enterprise customers with Magic Transit or Cloudflare WAN (formerly Magic WAN) can send encrypted network flow data via an IPsec tunnel to Cloudflare's network. You can achieve this by:</p>
<ol>
<li>Configuring your <a href="/network-flow/routers/netflow-ipfix-config/">NetFlow</a> or <a href="/network-flow/routers/sflow-config/">sFlow</a> data to be sent to Cloudflare's network for parsing.</li>
<li>Directing that network flow data to be sent over <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Magic Transit IPsec tunnels</a> or <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Cloudflare WAN IPsec tunnels</a> to Cloudflare's network.</li>
</ol>
<p>Cloudflare identifies the flow traffic by its destination IP address and port, then forwards it to Network Flow for parsing.</p>
<p>Free customers can route their network flow traffic through a device that is running the Cloudflare One Client. Then, network flow traffic can be forwarded from the Cloudflare One Client enabled device to Cloudflare's network flow endpoints. Learn more in the <a href="/network-flow/tutorials/encrypt-network-flow-data/">Encrypt network flow data tutorial</a>.</p>
<h2 id="i-have-auto-advertisement-enabled-and-it-was-triggered-by-an-attack-do-i-have-to-turn-magic-transit-off-manually">I have Auto-Advertisement enabled and it was triggered by an attack. Do I have to turn Magic Transit off manually?</h2>
<p>Yes. After Auto-Advertisement activates for a prefix under attack, Cloudflare continues advertising that prefix even after the attack ends. You must manually withdraw the prefix to stop Magic Transit. Refer to <a href="/byoip/concepts/dynamic-advertisement/best-practices/#configure-dynamic-advertisement">Configure dynamic advertisement</a> to withdraw your prefixes.</p>
<h2 id="if-auto-advertisement-is-enabled-and-the-threshold-has-been-triggered-will-the-ip-prefix-show-as-advertised-in-the-dashboard">If Auto-Advertisement is enabled, and the threshold has been triggered, will the IP prefix show as advertised in the dashboard?</h2>
<p>Yes, the IP prefix will show as advertised under the <a href="/byoip/concepts/dynamic-advertisement/best-practices/#configure-dynamic-advertisement">IP Prefixes tab</a>.</p>
<h2 id="does-auto-advertisement-also-work-with-bgp-controlled-advertisements">Does Auto-advertisement also work with BGP-controlled advertisements?</h2>
<p>No. Auto-advertisement only works with API-controlled advertisement, not BGP-controlled advertisement.</p>
<h2 id="in-the-api-network-flow-rules-have-a-bandwidth-threshold-data-field-does-the-value-for-this-field-refer-to-bytes-transferred-or-current-throughput">In the API, Network Flow rules have a <code>bandwidth_threshold</code> data field. Does the value for this field refer to bytes transferred or current throughput?</h2>
<p>A <a href="/api/resources/magic_network_monitoring/subresources/rules/methods/list/">Network Flow rule</a> threshold has two values:</p>
<ul>
<li><code>bandwidth_threshold</code> — the total ingress throughput on your network at any given moment, measured in bits per second.</li>
<li><code>duration</code> — how long <code>bandwidth_threshold</code> must be exceeded before you receive an alert.</li>
</ul>
<p>For example, you create a Network Flow rule with the following parameters:</p>
<pre><code class="language-txt">&quot;bandwidth_threshold&quot;: 50000000&#10;&quot;duration&quot;: &quot;1m0s&quot;&#10;</code></pre>
<p>With this rule, your network needs to receive a throughput greater than 50,000,000 bits per second (50 Megabits per second or Mbps) for 60 seconds. If both of these conditions are met, then Network Flow will send you an alert.</p>
<h2 id="my-router-s-public-ip-address-is-different-from-the-ip-address-of-my-network-flow-agent-ip-i-cannot-change-my-network-flow-agent-ip-and-i-am-not-seeing-my-router-s-traffic-in-network-flow-analytics">My router's public IP address is different from the IP address of my network flow <code>agent-ip</code>. I cannot change my network flow <code>agent-ip</code>, and I am not seeing my router's traffic in Network Flow analytics</h2>
<p>Set your router's public IP address and network flow <code>agent-ip</code> to the same value. If you cannot change the <code>agent-ip</code>, register both your router's public IP and the <code>agent-ip</code> in the Network Flow <a href="/network-flow/get-started/">router configuration</a>.</p>
<p>Registering both addresses prevents Network Flow from blocking traffic from unrecognized IPs. Your router's flow data appears under the <code>agent-ip</code>.</p>
<h2 id="what-is-the-network-flow-data-retention-policy-for-netflow-sflow-received-from-customer-s-routers">What is the Network Flow data retention policy for NetFlow/sFlow received from customer's routers?</h2>
<p>All flow data is processed on Cloudflare's servers in the US. If you enable data sovereignty in Europe, you cannot use Network Flow.</p>
<p>Cloudflare retains GraphQL analytics data for 90 days for enterprise customers and seven days for non-enterprise customers. Cloudflare also retains flow data for six hours for threshold crossing detection.</p>
