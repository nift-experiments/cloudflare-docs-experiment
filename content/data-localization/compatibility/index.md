<p>The Data Localization Suite (DLS) has three features, each controlling a different aspect of where your data is handled:</p>
<ul>
<li><strong>Geo Key Manager</strong>: Controls where your private TLS keys are stored.</li>
<li><strong>Regional Services</strong>: Controls which Cloudflare data centers can decrypt and process your HTTPS traffic.</li>
<li><strong>Customer Metadata Boundary (CMB)</strong>: Controls which region stores your logs and analytics data.</li>
</ul>
<p>The tables below show whether each Cloudflare product is compatible with each DLS feature. If you see 🚧, check the footnote number for specific restrictions.</p>
<p>✅ Fully compatible — no restrictions <br/>
🚧 Compatible with caveats — check the footnote for details <br/>
✘ Not compatible — this product cannot be used with this DLS feature <br/>
⚫️ Not applicable — this product does not interact with this DLS feature</p>
<h2 id="application-performance">Application Performance</h2>
<table>
<thead>
<tr>
<th>Product</th>
<th>Geo Key Manager</th>
<th>Regional Services</th>
<th>Customer Metadata Boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Caching/CDN</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Cache Reserve</td>
<td>⚫️</td>
<td>🚧</td>
<td>✅ <sup><a href="#footnote-29">29</a></sup></td>
</tr>
<tr>
<td>DNS</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-33">33</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td>HTTP/3 (with QUIC)</td>
<td>⚫️</td>
<td>✘</td>
<td>⚫️</td>
</tr>
<tr>
<td>Image Resizing</td>
<td>✅</td>
<td>✅ <sup><a href="#footnote-6">6</a></sup></td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Load Balancing</td>
<td>✅</td>
<td>✅</td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Network Error Logging (NEL)</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✘</td>
</tr>
<tr>
<td>Onion Routing</td>
<td>✘</td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>O2O</td>
<td>✘</td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>Stream Delivery</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Tiered Caching</td>
<td>✅</td>
<td>🚧 <sup><a href="#footnote-2">2</a></sup></td>
<td>🚧 <sup><a href="#footnote-30">30</a></sup></td>
</tr>
<tr>
<td>Trace</td>
<td>✘</td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>Waiting Room</td>
<td>⚫️</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Web Analytics / Real User Monitoring (RUM)</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✘ <sup><a href="#footnote-43">43</a></sup></td>
</tr>
<tr>
<td>Zaraz</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="application-security">Application Security</h2>
<table>
<thead>
<tr>
<th>Product</th>
<th>Geo Key Manager</th>
<th>Regional Services</th>
<th>Customer Metadata Boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Advanced Certificate Manager</td>
<td>⚫️</td>
<td>⚫️</td>
<td>⚫️</td>
</tr>
<tr>
<td>Advanced DDoS Protection</td>
<td>✅</td>
<td>✅</td>
<td>🚧 <sup><a href="#footnote-3">3</a></sup> <sup><a href="#footnote-50">50</a></sup></td>
</tr>
<tr>
<td>API Shield</td>
<td>✅</td>
<td>✅</td>
<td>🚧 <sup><a href="#footnote-4">4</a></sup></td>
</tr>
<tr>
<td>Bot Management</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Client-side security (formerly Page Shield)</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>DNS Firewall</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✅</td>
</tr>
<tr>
<td>Rate Limiting</td>
<td>✅</td>
<td>✅</td>
<td>✅ <sup><a href="#footnote-37">37</a></sup></td>
</tr>
<tr>
<td>SSL</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Cloudflare for SaaS</td>
<td>✘</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Turnstile</td>
<td>⚫️</td>
<td>✘</td>
<td>✅ <sup><a href="#footnote-38">38</a></sup></td>
</tr>
<tr>
<td>WAF/L7 Firewall</td>
<td>✅</td>
<td>✅</td>
<td>🚧 <sup><a href="#footnote-50">50</a></sup></td>
</tr>
<tr>
<td>DMARC Management</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✅</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="developer-platform">Developer Platform</h2>
<table>
<thead>
<tr>
<th>Product</th>
<th>Geo Key Manager</th>
<th>Regional Services</th>
<th>Customer Metadata Boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Images</td>
<td>⚫️</td>
<td>✅ <sup><a href="#footnote-36">36</a></sup></td>
<td>🚧 <sup><a href="#footnote-35">35</a></sup></td>
</tr>
<tr>
<td>AI Gateway</td>
<td>✘</td>
<td>✘</td>
<td>🚧 <sup><a href="#footnote-39">39</a></sup></td>
</tr>
<tr>
<td>AI Search</td>
<td>✘ <sup><a href="#footnote-46">46</a></sup></td>
<td>✘ <sup><a href="#footnote-47">47</a></sup></td>
<td>🚧 <sup><a href="#footnote-48">48</a></sup></td>
</tr>
<tr>
<td>AI Security for Apps</td>
<td>✘</td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>Cloudflare Pages</td>
<td>✅ <sup><a href="#footnote-11">11</a></sup></td>
<td>✅ <sup><a href="#footnote-11">11</a></sup></td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Cloudflare D1</td>
<td>⚫️</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-40">40</a></sup></td>
</tr>
<tr>
<td>Durable Objects</td>
<td>⚫️</td>
<td>✅ <sup><a href="#footnote-7">7</a></sup></td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Email Routing</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✅</td>
</tr>
<tr>
<td>Remote MCP Server</td>
<td>✅ <sup><a href="#footnote-44">44</a></sup></td>
<td>✅ <sup><a href="#footnote-45">45</a></sup></td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>R2</td>
<td>✅ <sup><a href="#footnote-27">27</a></sup></td>
<td>✅ <sup><a href="#footnote-8">8</a></sup></td>
<td>✅ <sup><a href="#footnote-28">28</a></sup></td>
</tr>
<tr>
<td>Smart Placement</td>
<td>⚫️</td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>Stream</td>
<td>⚫️</td>
<td>✘</td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Vectorize</td>
<td>⚫️</td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>Workers (deployed on a Zone)</td>
<td>✅</td>
<td>✅</td>
<td>🚧 <sup><a href="#footnote-41">41</a></sup></td>
</tr>
<tr>
<td>Workers AI</td>
<td>⚫️</td>
<td>✘</td>
<td>✅</td>
</tr>
<tr>
<td>Workers KV</td>
<td>⚫️</td>
<td>✘</td>
<td>✅ <sup><a href="#footnote-34">34</a></sup></td>
</tr>
<tr>
<td>Workers.dev</td>
<td>✘</td>
<td>✘</td>
<td>✘</td>
</tr>
<tr>
<td>Workers Analytics Engine (WAE)</td>
<td>⚫️</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="network-services">Network Services</h2>
<table>
<thead>
<tr>
<th>Product</th>
<th>Geo Key Manager</th>
<th>Regional Services</th>
<th>Customer Metadata Boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Argo Smart Routing</td>
<td>✅</td>
<td>✘ <sup><a href="#footnote-9">9</a></sup></td>
<td>✘ <sup><a href="#footnote-10">10</a></sup></td>
</tr>
<tr>
<td>Static IP/BYOIP</td>
<td>⚫️</td>
<td>✅ <sup><a href="#footnote-26">26</a></sup></td>
<td>⚫️</td>
</tr>
<tr>
<td>Cloudflare Network Firewall</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✅</td>
</tr>
<tr>
<td>Network Flow</td>
<td>⚫️</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Magic Transit</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✅ <sup><a href="#footnote-3">3</a></sup></td>
</tr>
<tr>
<td>Cloudflare WAN</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✅</td>
</tr>
<tr>
<td>Spectrum</td>
<td>✅</td>
<td>✅ <sup><a href="#footnote-42">42</a></sup></td>
<td>✅</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="platform">Platform</h2>
<table>
<thead>
<tr>
<th>Product</th>
<th>Geo Key Manager</th>
<th>Regional Services</th>
<th>Customer Metadata Boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Logpull</td>
<td>⚫️</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-12">12</a></sup></td>
</tr>
<tr>
<td>Logpush</td>
<td>⚫️</td>
<td>✅</td>
<td>🚧 <sup><a href="#footnote-13">13</a></sup></td>
</tr>
<tr>
<td>Log Explorer</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✘ <sup><a href="#footnote-23">23</a></sup></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="zero-trust">Zero Trust</h2>
<table>
<thead>
<tr>
<th>Product</th>
<th>Geo Key Manager</th>
<th>Regional Services</th>
<th>Customer Metadata Boundary</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access</td>
<td>🚧 <sup><a href="#footnote-14">14</a></sup></td>
<td>🚧 <sup><a href="#footnote-15">15</a></sup></td>
<td>✅ <sup><a href="#footnote-16">16</a></sup></td>
</tr>
<tr>
<td>Browser Isolation</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-17">17</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td>CASB</td>
<td>⚫️</td>
<td>⚫️</td>
<td>✘</td>
</tr>
<tr>
<td>Cloudflare Tunnel</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-18">18</a></sup></td>
<td>⚫️</td>
</tr>
<tr>
<td>Digital Experience</td>
<td>⚫️</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-49">49</a></sup></td>
</tr>
<tr>
<td>DLP</td>
<td>⚫️ <sup><a href="#footnote-19">19</a></sup></td>
<td>⚫️ <sup><a href="#footnote-19">19</a></sup></td>
<td>🚧 <sup><a href="#footnote-31">31</a></sup></td>
</tr>
<tr>
<td>Gateway</td>
<td>🚧 <sup><a href="#footnote-20">20</a></sup></td>
<td>🚧 <sup><a href="#footnote-21">21</a></sup></td>
<td>🚧 <sup><a href="#footnote-22">22</a></sup></td>
</tr>
<tr>
<td>Cloudflare One Client</td>
<td>⚫️</td>
<td>⚫️</td>
<td>🚧 <sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Logs / Analytics not available outside US region when using Customer Metadata Boundary.</li>
<li id="footnote-2">Regular and Custom Tiered Cache (where you define the caching hierarchy) work with Regional Services. Smart Tiered Caching (where Cloudflare automatically selects intermediate cache data centers) is not available with Regional Services.</li>
<li id="footnote-3">[Adaptive DDoS Protection](/ddos-protection/managed-rulesets/adaptive-protection/) (which automatically adjusts DDoS rules based on your traffic patterns) is only supported when Customer Metadata Boundary is set to the US. All other DDoS protection features work with any CMB region.</li>
<li id="footnote-4">The following API Shield sub-features do not work when CMB is set to EU: API Discovery (automatic detection of your API endpoints), Volumetric Abuse Detection (identifying unusually high API call volumes), and [Sequence Analytics and Mitigation](/api-shield/security/sequence-analytics/) (tracking the order of API calls to detect misuse). All other API Shield features work with any CMB region.</li>
<li id="footnote-6">Only when using a Custom Domain set to a region, either through Workers or [Transform Rules](/images/optimization/transformations/rewrite-rules/) within the same zone.</li>
<li id="footnote-7">[Jurisdiction restrictions for Durable Objects](/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction).</li>
<li id="footnote-8">Only when using a [Custom Domain](/r2/buckets/public-buckets/#connect-a-bucket-to-a-custom-domain) set to a region and using [jurisdictions with the S3 API](/r2/reference/data-location/#using-jurisdictions-with-the-s3-api).</li>
<li id="footnote-9">Argo cannot be used with Regional Services.</li>
<li id="footnote-10">Argo cannot be used with Customer Metadata Boundary.</li>
<li id="footnote-11">Only when using [Custom Domain](/pages/configuration/custom-domains/) set to a region.</li>
<li id="footnote-12">Logpull available when using CMB = US only. Logpull is a legacy feature, consider using [Logpush](/data-localization/metadata-boundary/logpush-datasets/) or [Log Explorer](/log-explorer/) instead.</li>
<li id="footnote-13">Logpush available with Customer Metadata Boundary for [these datasets](/data-localization/metadata-boundary/logpush-datasets/). Contact your account team if you need another dataset.</li>
<li id="footnote-14">Access App SSL keys can use Geo Key Manager. [Access JWT](/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/) is not yet localized.</li>
<li id="footnote-15">Can be localized to US FedRAMP Moderate Domestic region only.</li>
<li id="footnote-16">Customer Metadata Boundary can be used to limit data transfer outside region, but Access User Logs will not be available outside US region. EU customers must use Logpush to retain logs.</li>
<li id="footnote-17">Currently may only be used with US FedRAMP region.</li>
<li id="footnote-18">The [`--region` parameter](/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#region) in `cloudflared` controls where the tunnel connector establishes its connection to Cloudflare. This setting is separate from Regional Services. For public hostnames served through a tunnel, Regional Services is configured at the DNS record level and operates independently from the tunnel connector region. For incoming web requests, Regional Services only applies when you have [published applications](/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/) (services exposed to users through the tunnel). In that case, the region associated with the DNS record will apply.</li>
<li id="footnote-19">Uses Gateway HTTP and CASB.</li>
<li id="footnote-20">You can [bring your own certificate](https://blog.cloudflare.com/bring-your-certificates-cloudflare-gateway/) to Gateway but these cannot yet be restricted to a specific region.</li>
<li id="footnote-21">Gateway HTTP (web traffic filtering) supports Regional Services. Gateway DNS (domain name filtering) does not yet support regionalization. <br/> ICMP proxy (forwarding network diagnostic traffic like ping) and Mesh proxy are not available to Regional Services users. [File Sandboxing](/cloudflare-one/traffic-policies/http-policies/file-sandboxing/) (an add-on that quarantines and scans suspicious files in an isolated environment) is incompatible with DLS.</li>
<li id="footnote-22">Dashboard Analytics and Logs are empty when using CMB outside the US region. Use Logpush instead.</li>
<li id="footnote-23">Currently, customers do not have the ability to choose the location of the Cloudflare-managed R2 bucket for Log Explorer.</li>
<li id="footnote-26">You can use Static IP/BYOIP with Regionalized Spectrum Applications. You can also regionalize BYOIP prefixes at the IP layer with [Regionalized IP Bindings](/data-localization/regional-services/ip-bindings/).</li>
<li id="footnote-27">Only when using a Custom Domain and a [Custom Certificate](/r2/reference/data-security/#encryption-in-transit) or [Keyless SSL](/ssl/keyless-ssl/).</li>
<li id="footnote-28">R2 Dashboard [Metrics and Analytics](/r2/platform/metrics-analytics/) are populated. [Jurisdictional Restrictions](/r2/reference/data-location/#jurisdictional-restrictions) guarantee objects in a bucket are stored within a specific jurisdiction.</li>
<li id="footnote-29">You cannot yet specify region location for object storage itself.</li>
<li id="footnote-30">Regular/Generic and Custom Tiered Cache work with Customer Metadata Boundary (CMB). Smart Tiered Caching (where Cloudflare automatically selects intermediate cache data centers) does not work with CMB. <br/> With CMB set to EU, the Zone Dashboard **Caching** > **Tiered Cache** > **Smart Tiered Caching** option will not populate the Dashboard Analytics.</li>
<li id="footnote-31">DLP is part of Gateway HTTP, however, [DLP detection entries](/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/) are not available outside US region when using Customer Metadata Boundary.</li>
<li id="footnote-33">If you use [outgoing zone transfers](/dns/zone-setups/zone-transfers/cloudflare-as-primary/) (where Cloudflare sends your DNS records to non-Cloudflare nameservers), those transfers will include global Cloudflare IP addresses rather than region-specific ones. This means Regional Services will not function correctly when end users receive DNS answers from non-Cloudflare nameservers.</li>
<li id="footnote-34">Jurisdictional Restrictions (storage) for Workers KV pairs is not supported today.</li>
<li id="footnote-35">Logs / Analytics not supported for CMB = EU. Jurisdictional Restrictions ([storage](/images/storage/upload-images/methods/)) options are not supported today. All other features are available to all CMB regions. Note that beta or future features may not be in scope and could be subject to change.</li>
<li id="footnote-36">Only when using a [Custom Domain](/images/optimization/hosted-images/serve-from-custom-domains/) set to a region.</li>
<li id="footnote-37">Legacy Zone Analytics & Logs section not available outside US region when using CMB. Use [Security Analytics](/waf/analytics/security-analytics/) instead.</li>
<li id="footnote-38">[Turnstile Analytics](/turnstile/turnstile-analytics/) are available. However, there are no regionalization guarantees for the Siteverify API yet.</li>
<li id="footnote-39">Jurisdictional Restrictions (storage) options for [Logs](/ai-gateway/observability/logging/) are not supported today. All other features are available to all CMB regions.</li>
<li id="footnote-40">Jurisdictional Restrictions ([data location](/d1/configuration/data-location/) / storage) options are not supported today. All other features are available to all CMB regions. Note that beta or future features may not be in scope and could be subject to change.</li>
<li id="footnote-41">Logs / Analytics not available outside US region when using Customer Metadata Boundary. Use Logpush instead.</li>
<li id="footnote-42">Only applies to HTTP/S Spectrum applications. Spectrum applications use a separate regionalization mechanism from the Regional Hostnames API. Configuring a regional hostname does not regionalize a Spectrum application on the same hostname. Contact your [Account Team](/support/contacting-cloudflare-support/) for Spectrum-specific regionalization.</li>
<li id="footnote-43">Web Analytics collects the [minimum amount of information](/web-analytics/data-metrics/data-origin-and-collection/). Alternatively, you can [exclude EU Visitors from RUM](/speed/observatory/rum-beacon/#rum-excluding-eeaeu).</li>
<li id="footnote-44">Only when using Workers Routes & Domains and Custom Certificate.</li>
<li id="footnote-45">Only when using Workers Routes & Domains.</li>
<li id="footnote-46">Only R2 Custom Domains and Custom Certificate are supported.</li>
<li id="footnote-47">Only R2 Custom Domains are supported.</li>
<li id="footnote-48">The following are exceptions and are supported: AI Gateway Analytics (GraphQL Analytics datasets) and Logs (Logpush), R2 Dashboard Metrics & Analytics, Workers AI GraphQL Analytics datasets like aiInferenceAdaptive.</li>
<li id="footnote-49">Dashboard Analytics are empty when using CMB outside the US region. Use [Logpush](/logs/logpush/) instead.</li>
<li id="footnote-50">Email and webhook notifications for DDoS and WAF events may not fire reliably when Customer Metadata Boundary is set to `eu`. This behavior is intermittent and under investigation. If timely alerts are critical, use [Logpush](/logs/logpush/) as a complementary monitoring mechanism.</li></ol></section>
