<p>After setting up your Magic Transit product, Cloudflare validates:</p>
<ul>
<li>Tunnel connectivity</li>
<li>Tunnel and endpoint <a href="/magic-transit/reference/tunnel-health-checks/#types-of-health-checks">health checks</a></li>
<li>Letter of Agency (LOA)</li>
<li>Internet Routing Registry (IRR)</li>
<li>Maximum segment size (MSS) configurations.</li>
</ul>
<p>Refer to <a href="/learning-paths/data-center-protection/get-started/">Get started</a> for information about the above topics.</p>
<p>Configurations for Cloudflare global network are applied and take around one day to rollout.</p>
<p>On your side, you should do the following:</p>
<ul>
<li>Confirm that your upstream ISPs do not have <a href="/byoip/troubleshooting/#urpf-filtering-and-packet-loss">uRPF</a> strict-mode enabled. If they do, ask them to change this setting to uRPF loose mode. Having strict-mode uRPF will result in packet loss when you advertise your prefix from Cloudflare and withdraw your prefix advertisement from your ISP.</li>
<li>Confirm you have adjusted MSS/MTU value on any IPsec or GRE tunnels with third parties that are configured on your Magic Transit prefix.</li>
<li>If you are using BGP for Magic Transit prefix advertisement, configure your own alerts/logs for the BGP peerings with Cloudflare route reflectors. Cloudflare will not notify you if these peerings go down, so you should enable this on your equipment using syslog or other event-alerting tools.</li>
</ul>
