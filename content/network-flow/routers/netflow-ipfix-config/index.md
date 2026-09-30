<p>Configure your router to export <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10841.md")
</div> to Cloudflare's network for analysis in Network Flow (formerly Magic Network Monitoring). Network Flow supports the NetFlow v5, NetFlow v9, and IPFIX formats.
<h2 id="before-you-begin">Before you begin</h2>
<p>Before configuring NetFlow or IPFIX, verify the following:</p>
<ul>
<li>Your router supports NetFlow or IPFIX export capabilities. Refer to <a href="/network-flow/routers/supported-routers/">Supported routers</a> for a list of compatible routers.</li>
<li>You have administrative access to your router's configuration interface.</li>
<li>You have <a href="/network-flow/get-started/#2-register-your-router-with-cloudflare">registered your router with Cloudflare</a>.</li>
</ul>
<h2 id="1-access-your-router-configuration"><ol>
<li>Access your router configuration</li>
</ol></h2>
<p>Log in to your router's configuration application or command-line interface. The exact method varies by router vendor and model.</p>
<h2 id="2-configure-flow-exporter"><ol start="2">
<li>Configure Flow Exporter</li>
</ol></h2>
<p>Open your router's NetFlow configuration menu and set up the <strong>Flow Exporter</strong> with the following values:</p>
<ul>
<li><strong>Destination IP address</strong>: <code>162.159.65.1</code></li>
<li><strong>Destination Port</strong>: <code>2055</code></li>
<li><strong>Transport Protocol</strong>: <code>UDP</code></li>
</ul>
<p>These settings direct your router to send flow data to Cloudflare's network for analysis.</p>
<h2 id="3-configure-flow-record"><ol start="3">
<li>Configure Flow Record</li>
</ol></h2>
<p>Set up your router's <strong>Flow Record</strong> configuration with the following fields. These fields define what traffic metadata your router collects and exports.</p>
<p>Match fields identify the traffic:</p>
<ul>
<li><code>match ipv4 protocol</code></li>
<li><code>match ipv4 source address</code></li>
<li><code>match ipv4 destination address</code></li>
<li><code>match transport source-port</code></li>
<li><code>match transport destination-port</code></li>
<li><code>match interface input</code></li>
</ul>
<p>Collect fields capture statistics about the traffic:</p>
<ul>
<li><code>collect transport tcp flag</code></li>
<li><code>collect counter packets long</code></li>
<li><code>collect counter bytes long</code></li>
<li><code>collect flow sampler</code></li>
<li><code>collect timestamp sys-uptime first</code></li>
<li><code>collect timestamp sys-uptime last</code></li>
</ul>
<h2 id="4-save-and-apply-configuration"><ol start="4">
<li>Save and apply configuration</li>
</ol></h2>
<p>Save your NetFlow or IPFIX configuration changes and apply them to your router. Verify that your router's NetFlow template does not contain duplicated fields, as duplicates can cause export errors.</p>
<h2 id="5-verify-your-configuration"><ol start="5">
<li>Verify your configuration</li>
</ol></h2>
<p>After configuring NetFlow or IPFIX, verify that data is being sent to Cloudflare:</p>
<ol>
<li>Wait five to ten minutes for flow data to be transmitted and processed.</li>
<li>Check your router status in the Cloudflare dashboard under <strong>Network flow</strong> &gt; <strong>Configure Network flow</strong> &gt; <strong>Check routers</strong> (visible during onboarding) or view analytics in the <strong>Network flow</strong> page.</li>
<li>If data is not appearing, verify your Flow Exporter settings and confirm your router's public IP address matches the IP registered with Cloudflare.</li>
</ol>
