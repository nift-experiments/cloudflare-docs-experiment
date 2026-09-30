<p>This guide helps you build business continuity strategies for the Cloudflare One Client by documenting available disconnection mechanisms and providing decision guidance for handling service degradation or infrastructure unavailability.</p>
<h2 id="current-resilience-posture">Current resilience posture</h2>
<p>The Cloudflare One Client operates on Cloudflare's globally distributed network with 300+ points of presence (PoPs) worldwide. Anycast routing automatically directs client connections to the nearest healthy PoP without manual intervention. The client maintains locally cached policies and continues enforcing security controls even when unable to reach Cloudflare's management systems.</p>
<p>For detailed architecture information, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client documentation</a> and the <a href="https://cf-assets.www.cloudflare.com/slt3lc6tev37/7ad0dpR3YyqxMlikPfbBgn/020b7450909f03ccf3c7dcfb0e99fc2e/Resilience_Whitepaper.pdf">Cloudflare Network and Service Resilience Whitepaper</a>.</p>
<h2 id="fail-open-vs-fail-closed-decisions">Fail-open vs. fail-closed decisions</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6056.md")
</aside>
<p>The mechanisms below help you execute fail-open decisions when needed. Document your decision criteria in advance and ensure appropriate stakeholders have authorization to trigger disconnection.</p>
<h2 id="customer-impact-and-decision-guidance">Customer impact and decision guidance</h2>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Mechanism</th>
<th>Guidance</th>
<th>Prerequisites and limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td>
        <p><strong>Complete unavailability during Cloudflare infrastructure outage</strong></p>
        <p>Example: Cloudflare management systems unreachable; Global Disconnection unavailable but users need Internet access to maintain business operations.</p>
</td>
<td>
        <p><strong><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">External Emergency Disconnect</a></strong></p>
        <p>A customer-hosted HTTPS endpoint that clients poll for disconnect signals, operating independently of Cloudflare infrastructure.</p>
</td>
<td>
        <p><strong>Use when:</strong> Cloudflare's management systems are unreachable but you need to disconnect clients to restore Internet access.</p>
        <p><strong>Guidance:</strong> Pre-configure this mechanism before outages occur. During an incident, update your endpoint to return <code>{'{"emergency_disconnect": true}'}</code>.</p>
        <p><strong>Expected outcome:</strong> Clients disconnect within 1–2 polling intervals (configurable, default 60 seconds); users regain direct Internet access without security controls.</p>
</td>
<td>
        <p><strong>Prerequisites:</strong></p>
        <ul>
<pre><code>      &lt;li&gt;Customer-hosted HTTPS endpoint (IPv4/IPv6 address, not domain)&lt;/li&gt;&#10;      &lt;li&gt;SHA-256 fingerprint of TLS certificate&lt;/li&gt;&#10;      &lt;li&gt;MDM deployment for group-differentiated responses&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Limitations:&lt;/strong&gt;&lt;/p&gt;&#10;    &lt;ul&gt;&#10;&#10;      &lt;li&gt;&lt;strong&gt;Not available on iOS, Android, or ChromeOS&lt;/strong&gt;&lt;/li&gt;&#10;      &lt;li&gt;Customer responsible for endpoint maintenance and certificate renewal&lt;/li&gt;&#10;      &lt;li&gt;No Cloudflare logging of disconnect events&lt;/li&gt;&#10;      &lt;li&gt;Split Tunnel configuration must not include the endpoint IP&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Security impact:&lt;/strong&gt; Loss of all Zero Trust controls (same as Global Disconnection).&lt;/p&gt;&#10;</code></pre>
</td>
</tr>
<tr>
<td>
        <p><strong>Complete unavailability of client connectivity</strong></p>
        <p>Example: Client cannot establish secure tunnel; users unable to access protected applications or filtered Internet.</p>
</td>
<td>
        <p><strong>Global Disconnection</strong></p>
        <p>Instantly disconnect all Cloudflare One Clients from the secure tunnel via Dashboard or API.</p>
</td>
<td>
        <p><strong>Use when:</strong> You need immediate fleet-wide disconnection and Cloudflare's management systems are reachable.</p>
        <p><strong>Guidance:</strong> Check the <a href="https://www.cloudflarestatus.com/">Cloudflare status page</a> first. If Cloudflare infrastructure is experiencing issues, this mechanism may be unavailable — use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">External Emergency Disconnect</a> instead.</p>
        <p><strong>Expected outcome:</strong> All clients disconnect within seconds; users have direct Internet access without filtering, threat protection, or private application connectivity.</p>
</td>
<td>
        <p><strong>Prerequisites:</strong></p>
        <ul>
<pre><code>      &lt;li&gt;Dashboard or API access&lt;/li&gt;&#10;      &lt;li&gt;Account administrator permissions&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Limitations:&lt;/strong&gt;&lt;/p&gt;&#10;    &lt;ul&gt;&#10;&#10;      &lt;li&gt;Requires connectivity to Cloudflare's management systems&lt;/li&gt;&#10;      &lt;li&gt;Account-wide only (no group scoping)&lt;/li&gt;&#10;      &lt;li&gt;Unavailable during complete Cloudflare outages&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Security impact:&lt;/strong&gt;&lt;/p&gt;&#10;    &lt;ul&gt;&#10;&#10;      &lt;li&gt;Loss of web filtering and malware protection&lt;/li&gt;&#10;      &lt;li&gt;Loss of data loss prevention (DLP) inspection&lt;/li&gt;&#10;      &lt;li&gt;Loss of access to private applications&lt;/li&gt;&#10;      &lt;li&gt;Unencrypted DNS queries (potential privacy exposure)&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
</tr>
<tr>
<td>
        <p><strong>Individual device issue requiring immediate local override</strong></p>
        <p>Example: Single user locked out due to policy misconfiguration; client switch disabled but user needs emergency access.</p>
</td>
<td>
        <p><strong>Admin Override Codes</strong></p>
        <p>Time-limited, single-use codes allowing IT administrators to temporarily unlock client settings on a specific device.</p>
</td>
<td>
        <p><strong>Use when:</strong> An individual device requires immediate attention. This is the only option for iOS and Android users when External Emergency Disconnect is unavailable.</p>
        <p><strong>Guidance:</strong> Generate the code in the Dashboard, provide it to the user over a secure channel, and have the user enter it locally to temporarily bypass the locked switch.</p>
        <p><strong>Expected outcome:</strong> Temporary local override allowing the user to disconnect the client for one hour.</p>
</td>
<td>
        <p><strong>Prerequisites:</strong></p>
        <ul>
<pre><code>      &lt;li&gt;&lt;strong&gt;Lock client device switch&lt;/strong&gt; policy enabled&lt;/li&gt;&#10;      &lt;li&gt;Dashboard access to generate codes&lt;/li&gt;&#10;      &lt;li&gt;Direct communication with the end user&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Limitations:&lt;/strong&gt;&lt;/p&gt;&#10;    &lt;ul&gt;&#10;&#10;      &lt;li&gt;One code per device per hour&lt;/li&gt;&#10;      &lt;li&gt;Manual IT intervention required&lt;/li&gt;&#10;      &lt;li&gt;Not scalable for fleet-wide scenarios&lt;/li&gt;&#10;      &lt;li&gt;Requires staffed IT during incidents&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Security impact:&lt;/strong&gt; Single device loses Zero Trust controls for one hour.&lt;/p&gt;&#10;</code></pre>
</td>
</tr>
<tr>
<td>
        <p><strong>Degraded performance impacting user productivity</strong></p>
        <p>Example: High latency through client tunnel; intermittent connection drops affecting work quality.</p>
</td>
<td>
        <p><strong>Graduated response strategy</strong></p>
        <p>Use a combination of mechanisms based on scope and severity. Use <a href="/cloudflare-one/insights/dex/">Digital Experience (DEX)</a> to determine scope and severity.</p>
</td>
<td>
        <p><strong>Guidance by scope:</strong></p>
        <ul>
<pre><code>      &lt;li&gt;&lt;strong&gt;Single device:&lt;/strong&gt; Admin Override Code → manual disconnect&lt;/li&gt;&#10;      &lt;li&gt;&lt;strong&gt;Group or department:&lt;/strong&gt; External Emergency Disconnect with MDM-differentiated endpoints&lt;/li&gt;&#10;      &lt;li&gt;&lt;strong&gt;Organization-wide:&lt;/strong&gt; Global Disconnection (if Cloudflare reachable) or External Emergency Disconnect&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Decision factors:&lt;/strong&gt; Balance user productivity needs against security requirements. For regulated industries, consult your compliance team before disconnecting.&lt;/p&gt;&#10;    &lt;p&gt;&lt;strong&gt;Expected outcome:&lt;/strong&gt; Restored user productivity with a documented security trade-off.&lt;/p&gt;&#10;</code></pre>
</td>
<td>
        <p><strong>Prerequisites:</strong></p>
        <ul>
<pre><code>      &lt;li&gt;Documented decision criteria for fail-open vs. fail-closed&lt;/li&gt;&#10;      &lt;li&gt;Pre-configured mechanisms before incidents occur&lt;/li&gt;&#10;      &lt;li&gt;Clear authorization matrix&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Limitations:&lt;/strong&gt;&lt;/p&gt;&#10;    &lt;ul&gt;&#10;&#10;      &lt;li&gt;Each mechanism has different infrastructure dependencies&lt;/li&gt;&#10;      &lt;li&gt;Mobile platforms have limited options&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Security impact:&lt;/strong&gt; Scope-dependent — refer to individual mechanism entries above.&lt;/p&gt;&#10;</code></pre>
</td>
</tr>
<tr>
<td>
        <p><strong>Management dashboard unavailable, traffic processing normally</strong></p>
        <p>Example: Dashboard and API unreachable; edge services and client connections remain functional with cached policies.</p>
</td>
<td>
        <p><strong>No action required</strong></p>
        <p>Edge services continue operating using cached configurations. New configuration changes will be unavailable until management systems recover.</p>
</td>
<td>
        <p><strong>Use when:</strong> Cloudflare's management systems are unavailable but user traffic continues processing normally.</p>
        <p><strong>Guidance:</strong> Monitor the <a href="https://www.cloudflarestatus.com/">Cloudflare status page</a>. No customer action is typically required — edge services enforce cached policies until management systems recover.</p>
        <p><strong>Expected outcome:</strong> Existing configuration continues to apply; configuration changes resume when management systems recover.</p>
</td>
<td>
        <p><strong>Prerequisites:</strong></p>
        <ul>
<pre><code>      &lt;li&gt;Monitoring of the Cloudflare status page&lt;/li&gt;&#10;      &lt;li&gt;Understanding that traffic processing and management are separate systems&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Limitations:&lt;/strong&gt;&lt;/p&gt;&#10;    &lt;ul&gt;&#10;&#10;      &lt;li&gt;Cannot modify policies during the outage&lt;/li&gt;&#10;      &lt;li&gt;Cannot trigger Global Disconnection from Dashboard&lt;/li&gt;&#10;      &lt;li&gt;Real-time logs and analytics may be delayed&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;    &lt;p&gt;&lt;strong&gt;Security impact:&lt;/strong&gt; None — security controls remain active.&lt;/p&gt;&#10;</code></pre>
</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6055.md")
</aside>
<h2 id="additional-considerations">Additional considerations</h2>
<h3 id="prerequisites-to-validate-before-incidents">Prerequisites to validate before incidents</h3>
<ul>
<li>Turn on the Global Disconnection feature in the Dashboard.</li>
<li>Configure an External Emergency Disconnect endpoint and upload the certificate fingerprint.</li>
<li>Test all mechanisms in a non-production environment.</li>
<li>Document fail-open vs. fail-closed decision criteria and create an authorization matrix.</li>
<li>Validate that IT and Security staff have backup mechanisms to access critical infrastructure.</li>
<li>Practice using backup mechanisms regularly across departments and geographies.</li>
</ul>
<p><strong>Access and credentials needed during incidents:</strong></p>
<ul>
<li>Cloudflare Dashboard administrator access</li>
<li>API token with device settings permissions (for programmatic control)</li>
<li>MDM administrator credentials (for group-differentiated responses)</li>
</ul>
<h3 id="testing-recommendations">Testing recommendations</h3>
<ul>
<li>Use a dedicated test organization or tenant for initial validation.</li>
<li>Test with a small pilot group before fleet-wide deployment.</li>
<li>Conduct quarterly testing of all three disconnection mechanisms.</li>
<li>Run an annual full business continuity exercise including decision-making scenarios.</li>
</ul>
<p><strong>Common testing issues:</strong></p>
<ul>
<li>External Emergency Disconnect changes take 1–2 polling intervals to take effect (default 60 seconds).</li>
<li>Split Tunnel <strong>Include</strong> mode automatically excludes emergency endpoint IPs.</li>
<li>Certificate fingerprint changes require MDM re-deployment to all affected devices.</li>
</ul>
<h3 id="integration-dependencies">Integration dependencies</h3>
<p>When you disconnect the Cloudflare One Client, the following controls are affected:</p>
<ul>
<li><strong>Web filtering and threat protection:</strong> DNS and HTTP policies stop enforcing; users have direct, unfiltered Internet access.</li>
<li><strong>Data loss prevention (DLP):</strong> Content inspection stops; sensitive data uploads and downloads occur without DLP controls.</li>
<li><strong>Private application access:</strong> Connectivity to applications protected by Cloudflare Tunnel is lost. Consider alternative access methods such as a direct VPN for critical applications.</li>
<li><strong>Gateway logging and analytics:</strong> No visibility into user traffic during disconnection.</li>
</ul>
<h3 id="when-to-contact-cloudflare-support">When to contact Cloudflare support</h3>
<p><strong>Contact support immediately if:</strong></p>
<ul>
<li>A suspected Cloudflare infrastructure issue is affecting multiple customers.</li>
<li>You are unable to access the Dashboard during a critical security incident.</li>
<li>An External Emergency Disconnect misconfiguration has caused a fleet-wide stuck state.</li>
</ul>
<p><strong>Information to provide when opening a ticket:</strong></p>
<ul>
<li>Account ID and organization name</li>
<li>Affected device count and platform distribution</li>
<li>Results of your Cloudflare status page check</li>
<li>Client diagnostic logs (<code>warp-diag</code>)</li>
<li>Timeline and troubleshooting steps already taken</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Link</th>
</tr>
</thead>
<tbody>
<tr>
<td>Product documentation</td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client documentation</a></td>
</tr>
<tr>
<td>API reference</td>
<td><a href="https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/settings/">Zero Trust Devices Settings API</a></td>
</tr>
<tr>
<td>Global Disconnection</td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-the-cloudflare-one-client-on-all-devices">Global Disconnection settings</a></td>
</tr>
<tr>
<td>External Emergency Disconnect</td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">External Emergency Disconnect documentation</a></td>
</tr>
<tr>
<td>Admin Override Codes</td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes">Admin Override Codes</a></td>
</tr>
<tr>
<td>MDM deployment</td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">MDM Deployment Guide</a></td>
</tr>
<tr>
<td>Terraform provider</td>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_device_settings">Cloudflare Terraform Provider – Zero Trust Devices</a></td>
</tr>
<tr>
<td>Status page</td>
<td><a href="https://www.cloudflarestatus.com/">cloudflarestatus.com</a></td>
</tr>
<tr>
<td>Troubleshooting</td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/">Client Troubleshooting Guide</a></td>
</tr>
<tr>
<td>Resilience Whitepaper</td>
<td><a href="https://cf-assets.www.cloudflare.com/slt3lc6tev37/7ad0dpR3YyqxMlikPfbBgn/020b7450909f03ccf3c7dcfb0e99fc2e/Resilience_Whitepaper.pdf">Cloudflare Network and Service Resilience Whitepaper</a></td>
</tr>
</tbody>
</table>
