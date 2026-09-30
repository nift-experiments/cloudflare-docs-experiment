<p>Configure your router to export <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10836.md")
</div> data to Cloudflare's network for analysis in Network Flow (formerly Magic Network Monitoring). sFlow is a network monitoring protocol that samples network traffic to provide visibility into your network's performance and traffic patterns.
<h2 id="before-you-begin">Before you begin</h2>
<p>Before configuring sFlow, verify the following:</p>
<ul>
<li>Your router supports sFlow export capabilities. Refer to <a href="/network-flow/routers/supported-routers/">Supported routers</a> for a list of compatible routers.</li>
<li>You have administrative access to your router's configuration interface.</li>
<li>You have <a href="/network-flow/get-started/#2-register-your-router-with-cloudflare">registered your router with Cloudflare</a> and noted the default sampling rate you configured during registration.</li>
</ul>
<h2 id="1-access-your-router-configuration"><ol>
<li>Access your router configuration</li>
</ol></h2>
<p>Log in to your router's configuration application or command-line interface. The exact method varies by router vendor and model.</p>
<h2 id="2-configure-sflow-exporter"><ol start="2">
<li>Configure sFlow exporter</li>
</ol></h2>
<p>Locate your router's sFlow configuration menu and set up the sFlow exporter with the following values:</p>
<ul>
<li><strong>Destination IP address</strong>: <code>162.159.65.1</code></li>
<li><strong>Destination Port</strong>: <code>6343</code></li>
<li><strong>Transport Protocol</strong>: <code>UDP</code></li>
</ul>
<p>These settings direct your router to send sFlow data to Cloudflare's network for analysis.</p>
<h2 id="3-configure-sampling-rate"><ol start="3">
<li>Configure sampling rate</li>
</ol></h2>
<p>Set your router's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10837.md")
</div> rate to match the value you entered when registering your router with Cloudflare. The sampling rate determines how frequently your router samples network traffic to generate sFlow data.
<p>Refer to <a href="/network-flow/routers/recommended-sampling-rate/">Recommended sampling rate</a> for guidance on selecting an appropriate sampling rate based on your network's traffic volume.</p>
<h2 id="4-save-and-apply-configuration"><ol start="4">
<li>Save and apply configuration</li>
</ol></h2>
<p>Save your sFlow configuration changes and apply them to your router. Depending on your router model, you may need to restart the sFlow service or reload the configuration for changes to take effect.</p>
<h2 id="verify-your-configuration">Verify your configuration</h2>
<p>After configuring sFlow, verify that data is being sent to Cloudflare:</p>
<ol>
<li>Wait five to ten minutes for sFlow data to be transmitted and processed.</li>
<li>Check your router status in the Cloudflare dashboard under <strong>Network flow</strong> &gt; <strong>Configure Network flow</strong> &gt; <strong>Check routers</strong> (visible during onboarding) or view analytics in the <strong>Network flow</strong> page.</li>
<li>If data is not appearing, verify your sFlow exporter settings and confirm your router's public IP address matches the IP registered with Cloudflare.</li>
</ol>
