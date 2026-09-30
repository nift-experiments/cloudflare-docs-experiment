<p>This section covers best practices for setting up the following Gateway policy types:</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/traffic-policies/get-started/dns/">DNS filtering</a></li><li><a href="/cloudflare-one/traffic-policies/get-started/network/">Network filtering</a></li><li><a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP filtering</a></li></ul>
<p>For each type of policy, we recommend the following workflow:</p>
<ol>
<li>Connect the devices and/or networks that you want to apply policies to.</li>
<li>Verify that Gateway is successfully proxying traffic from your devices.</li>
<li>Set up basic security and compatibility policies (recommended for most use cases).</li>
<li>Customize your configuration to the unique needs of your organization.</li>
</ol>
<h2 id="recommended-deployment-phases">Recommended deployment phases</h2>
<p>Most organizations roll out Gateway in phases, starting with the lowest-effort, highest-impact policy type and adding deeper inspection over time.</p>
<h3 id="phase-1-dns-filtering">Phase 1: DNS filtering</h3>
<p>DNS filtering requires the least deployment effort and provides immediate protection.</p>
<ul>
<li>Point your network DNS to Gateway's resolver addresses, or deploy the Cloudflare One Client in DNS-only mode.</li>
<li>Block all <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security threat categories</a> (malware, phishing, command and control).</li>
<li>Block <a href="/cloudflare-one/traffic-policies/domain-categories/#content-categories">content categories</a> that violate your acceptable use policy.</li>
<li>Review <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">DNS logs</a> to gain visibility into Internet usage across your organization.</li>
</ul>
<p>For setup instructions, refer to <a href="/cloudflare-one/traffic-policies/get-started/dns/">Set up DNS filtering</a>.</p>
<h3 id="phase-2-network-policies">Phase 2: Network policies</h3>
<p>After DNS filtering is in place, add network-level controls for non-HTTP traffic.</p>
<ul>
<li>Deploy the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> and enable the <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a> for TCP.</li>
<li>Block traffic to high-risk IP ranges or restrict which ports and protocols users can access.</li>
<li>Use <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">protocol detection</a> to identify applications by traffic pattern rather than port number.</li>
<li>Enable network session logging for audit trails.</li>
</ul>
<p>For setup instructions, refer to <a href="/cloudflare-one/traffic-policies/get-started/network/">Set up network filtering</a>.</p>
<h3 id="phase-3-http-inspection">Phase 3: HTTP inspection</h3>
<p>HTTP inspection provides the deepest visibility and the most granular controls, but it requires additional setup.</p>
<ul>
<li>Install the <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Cloudflare root certificate</a> on user devices.</li>
<li>Enable <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> to inspect HTTPS traffic.</li>
<li>Create <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policies for applications that use certificate pinning.</li>
<li>Block risky file types, enable <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">anti-virus scanning</a>, and configure <a href="/cloudflare-one/data-loss-prevention/">DLP profiles</a> to detect sensitive data.</li>
<li>Use <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> to render high-risk sites in a remote browser.</li>
</ul>
<p>For setup instructions, refer to <a href="/cloudflare-one/traffic-policies/get-started/http/">Set up HTTP filtering</a>.</p>
<h3 id="phase-4-egress-control-and-full-integration">Phase 4: Egress control and full integration</h3>
<p>With all policy layers active, extend Gateway to cover your full network and integrate with other Cloudflare One services.</p>
<ul>
<li>Connect branch offices and data centers with <a href="/cloudflare-one/networks/">network tunnels</a> (IPsec/GRE via Magic WAN).</li>
<li>Configure <a href="/cloudflare-one/traffic-policies/egress-policies/">dedicated egress IPs</a> so third-party services can identify your organization's traffic.</li>
<li>Set up <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> to route internal DNS queries to your private DNS servers.</li>
<li>Monitor SaaS application usage with <a href="/cloudflare-one/cloud-and-saas-findings/">CASB</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6602.md")
</aside>
