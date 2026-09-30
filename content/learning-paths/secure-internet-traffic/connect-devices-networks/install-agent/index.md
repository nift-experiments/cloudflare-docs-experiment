<p>Most admins test by manually downloading the Cloudflare One Client and enrolling in your organization's Cloudflare Zero Trust instance.</p>
<h2 id="install-the-cloudflare-one-client">Install the Cloudflare One Client</h2>
<ol>
<li>First, uninstall any existing third-party VPN software if possible. Sometimes products placed in a disconnected or disabled state will still interfere with the Cloudflare One Client.</li>
<li>If you are running third-party firewall or TLS decryption software, verify that it does not inspect or block traffic to the following destinations:</li>
</ol>
<ul>
<li>
<p>IPv4 API endpoints: <code>162.159.137.105</code> and <code>162.159.138.105</code></p>
</li>
<li>
<p>IPv6 API endpoints: <code>2606:4700:7::a29f:8969</code> and <code>2606:4700:7::a29f:8a69</code></p>
</li>
<li>
<p>SNIs for Cloudflare One Client version 2026.6.0 and later: <code>api.devices.cloudflare.com</code></p>
</li>
<li>
<p>SNIs for versions earlier than 2026.6.0: <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code></p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">WARP with firewall</a>.</p>
</li>
</ul>
<ol start="3">
<li>
<p>Manually install the Cloudflare One Client on the device.</p>
<pre><code> &lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;Window, macOS, and Linux&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
</li>
</ol>
@markup("md", "content/.markup/bodies/10054.md")
</div></details>
<pre><code>	&lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;iOS, Android, and ChromeOS&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
@markup("md", "content/.markup/bodies/10056.md")
</div></details>
<p>The Cloudflare One Client should show as <strong>Connected</strong>. The device is now connected to your organization and secured with Cloudflare Zero Trust.</p>
