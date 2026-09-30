<p>Emergency disconnect allows organizations and administrators to disconnect and reconnect their fleet of Cloudflare One Clients (formerly WARP) independently from Cloudflare infrastructure. For example, in the event of a <a href="#use-cases">Cloudflare network outage</a> you ensure that you can still manage your devices even if Cloudflare’s systems are down or unreachable.</p>
<p>Two mechanisms are available:</p>
<ul>
<li><strong><a href="#set-up-external-emergency-disconnect">External Emergency Disconnect</a></strong>: Cloudflare One Clients periodically poll a customer-hosted HTTPS endpoint for a disconnect signal. This requires network connectivity to your endpoint but works even when Cloudflare infrastructure is unreachable.</li>
<li><strong><a href="#set-up-local-emergency-disconnect">Local Emergency Disconnect</a></strong>: The Cloudflare One Client monitors a local JSON file on the device for a disconnect signal. This does not require any network connectivity and is useful for disaster recovery scenarios where both Cloudflare and your own infrastructure may be unreachable.</li>
</ul>
<p>Emergency disconnect can also be used in combination with the dashboard-initiated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-the-cloudflare-one-client-on-all-devices">Disconnect the Cloudflare One Client on all devices</a> setting. You can use any mechanism individually or together for multi-layer resilience. A disconnect signal from any source triggers disconnect; all sources must indicate normal operation for the client to reconnect. For details on how these settings interact, refer to <a href="#device-client-settings-precedence">Device client settings precedence</a>.</p>
<h2 id="use-cases">Use cases</h2>
<ul>
<li><strong>Security Incident Response</strong>: Quickly terminate all WARP tunnels across the entire fleet.</li>
<li><strong>Compliance and Auditing</strong>: Fulfill requirements in sensitive or regulated environments that mandate an &quot;emergency stop&quot; capability that is fully isolated, auditable, and controlled by the organization's own infrastructure.</li>
<li><strong>Disaster Recovery</strong>: If devices cannot reach Cloudflare's API (due to a network outage, routing issue, or client-side misconfiguration), administrators retain the ability to force-disconnect the fleet via the customer-hosted endpoint or a local signal file.</li>
<li><strong>Business Continuity Planning (BCP)</strong>: Trigger emergency disconnect from local BCP scripts even when both Cloudflare and your own infrastructure are unreachable.</li>
<li><strong>Local Automation</strong>: Integrate with configuration management tools (Ansible, Puppet, Chef) or monitoring agents to manage the disconnect state without maintaining an HTTPS endpoint.</li>
</ul>
<h2 id="signal-format">Signal format</h2>
<p>Both the external endpoint response payload and the local signal file content must be valid JSON with the following format:</p>
<pre><code class="language-json">{&#10;  &quot;emergency_disconnect&quot;: false | true&#10;}&#10;</code></pre>
<ul>
<li>If <code>emergency_disconnect</code> is set to <code>true</code>, the device will initiate an emergency disconnect.</li>
<li>If <code>emergency_disconnect</code> is set to <code>false</code>, the device will continue normal operation.</li>
</ul>
<h2 id="set-up-external-emergency-disconnect">Set up External Emergency Disconnect</h2>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6249.md")
</div></details>
<p>When External Emergency Disconnect is enabled, Cloudflare One Clients will periodically poll a customer-hosted HTTPS endpoint. A client will only change its connection state if it receives a valid JSON payload with the new state. Any failure to successfully retrieve the state (such as endpoint unreachability, invalid certificate fingerprint, or an improperly structured payload) will not cause a state change on the client.</p>
<h3 id="external-endpoint-requirements">External endpoint requirements</h3>
<p>An external disconnect endpoint is an HTTPS server hosted outside of Cloudflare from which the Cloudflare One Client will fetch the emergency disconnect signal. The customer is fully responsible for managing this endpoint.</p>
<h4 id="endpoint-url">Endpoint URL</h4>
<p>The external endpoint URL should:</p>
<ul>
<li>Use the HTTPS protocol.</li>
<li>Use an IPv4 or IPv6 address as the host, not a domain.</li>
<li>(Recommended) Use a public IP to ensure that devices can fetch the latest state regardless of their network location.</li>
</ul>
<h4 id="cipher-suites">Cipher suites</h4>
<p>The Cloudflare One Client establishes a TLS connection using <a href="https://github.com/rustls/rustls">Rustls</a>. Make sure your HTTPS endpoint accepts one of the <a href="https://docs.rs/rustls/0.21.10/src/rustls/suites.rs.html#125-143">cipher suites supported by Rustls</a>.</p>
<h3 id="1-create-an-external-disconnect-endpoint"><ol>
<li>Create an external disconnect endpoint</li>
</ol></h3>
<p>To configure External Emergency Disconnect, you will need an HTTPS endpoint in your own infrastructure that serves the global disconnect signal. The Cloudflare One Client will poll the external endpoint and validate its TLS/SSL certificate against an SHA-256 fingerprint that you upload to Zero Trust. Refer to <a href="#external-endpoint-requirements">External endpoint requirements</a> for more details.</p>
<p>The following example demonstrates how to deploy an external disconnect endpoint using an nginx container in Docker.</p>
<ol>
<li>Generate a TLS/SSL certificate:</li>
</ol>
<pre><code class="language-sh">openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes -keyout key.pem -out cert.pem&#10;</code></pre>
<pre><code>You will be prompted to fill in Distinguished Name (DN) fields. Fill in your organization's information or press `Enter` to use the default values.&#10;&#10;The command will output a certificate in PEM format and its private key. Store these files in a secure place.&#10;</code></pre>
<ol start="2">
<li>
<p>Configure an HTTPS server on your network to use this certificate and key:</p>
<pre><code>a. Create an nginx configuration file called `nginx.conf`:&#10;</code></pre>
</li>
</ol>
<pre><code class="language-txt">events {&#10;	worker_connections  1024;&#10;}&#10;&#10;http {&#10;		server {&#10;				listen              443 ssl;&#10;				ssl_certificate     /certs/cert.pem;&#10;				ssl_certificate_key /certs/key.pem;&#10;				location /status/disconnect {&#10;						default_type application/json;&#10;						return 200 &#x27;{&quot;emergency_disconnect&quot;: false}&#x27;;&#10;				}&#10;		}&#10;}&#10;</code></pre>
<pre><code>    If needed, replace `/certs/cert.pem` and `/certs/key.pem` with the locations of your certificate and key.&#10;&#10;    b. Add the nginx image to your Docker compose file:&#10;</code></pre>
<pre><code class="language-yml">services:&#10;	nginx:&#10;		image: nginx:latest&#10;		ports:&#10;			&#45; 3333:443&#10;		volumes:&#10;			&#45; ./nginx.conf:/etc/nginx/nginx.conf:ro&#10;			&#45; ./certs:/certs:ro&#10;</code></pre>
<pre><code>    	If needed, replace `./nginx.conf` and `./certs` with the locations of your nginx configuration file and certificate.&#10;&#10;    c. Start the server:&#10;</code></pre>
<pre><code class="language-sh">docker compose up -d&#10;</code></pre>
<ol start="3">
<li>To test that the HTTPS endpoint is working, run a curl command from the end user's device. You need to pass the <code>--insecure</code> option because we are using a self-signed certificate.</li>
</ol>
<pre><code class="language-sh">curl --insecure https://&lt;server-ip&gt;:3333/status/disconnect&#10;</code></pre>
<pre><code class="language-sh">{&quot;emergency_disconnect&quot;: false}&#10;</code></pre>
<h3 id="2-extract-the-sha-256-fingerprint"><ol start="2">
<li>Extract the SHA-256 fingerprint</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6252.md")
</div></div>
<h3 id="3-turn-on-external-emergency-disconnect"><ol start="3">
<li>Turn on External Emergency Disconnect</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6256.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="split-tunnels-in-include-mode">Split Tunnels in Include mode</h3>
@markup("md", "content/.markup/bodies/6248.md")
</aside>
<h3 id="4-test-external-emergency-disconnect"><ol start="4">
<li>Test External Emergency Disconnect</li>
</ol></h3>
<ol>
<li>Ensure that the Cloudflare One Client is connected.</li>
<li>Ensure that the External Emergency Disconnect feature is <a href="#3-turn-on-external-emergency-disconnect">turned on</a>.</li>
<li>In your <a href="#1-create-an-external-disconnect-endpoint">external endpoint</a> configuration, change <code>emergency_disconnect</code> to <code>true</code>:</li>
</ol>
<pre><code class="language-json">{ &quot;emergency_disconnect&quot;: true }&#10;</code></pre>
<ol start="4">
<li>You may need to reload the server to apply changes. To reload the <a href="#1-create-an-external-disconnect-endpoint">example <code>nginx</code> server</a>:</li>
</ol>
<pre><code class="language-sh">docker exec &lt;container-name-or-id&gt; nginx -s reload&#10;</code></pre>
<p>The Cloudflare One Client will automatically disconnect within the configured polling interval, and the Cloudflare One Client GUI will display <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#admin-directed-disconnect"><code>Admin directed disconnect</code></a>. To reconnect all devices, change <code>emergency_disconnect</code> back to <code>false</code>.</p>
<h2 id="set-up-local-emergency-disconnect">Set up Local Emergency Disconnect</h2>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6257.md")
</div></details>
<p>Local Emergency Disconnect allows organizations to trigger an emergency disconnect on the device itself, without requiring network access to any remote infrastructure. The Cloudflare One Client monitors a local JSON file at a fixed, admin-writable path. When the file contains a disconnect signal, the client enters the emergency disconnect state. Local scripts, configuration management tools (such as Ansible, Puppet, or Chef), or monitoring agents can create or modify the signal file directly on the device.</p>
<h3 id="signal-file-path">Signal file path</h3>
<p>The Cloudflare One Client monitors a fixed file path that requires administrative privilege to modify. The path is not configurable.</p>
<table>
<thead>
<tr>
<th>Operating system</th>
<th>File path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Windows</td>
<td><code>%PROGRAMDATA%\Cloudflare\emergency_disconnect.json</code></td>
</tr>
<tr>
<td>macOS</td>
<td><code>/Library/Application Support/Cloudflare/emergency_disconnect.json</code></td>
</tr>
<tr>
<td>Linux</td>
<td><code>/var/lib/cloudflare-warp/emergency_disconnect.json</code></td>
</tr>
</tbody>
</table>
<p>The signal file uses the same <a href="#signal-format">JSON format</a> as the external HTTPS endpoint. If the file does not exist, the client treats it as normal operation (<code>false</code>). If the file contains invalid JSON, the client logs an error and does not change state. The client reacts to file changes within 30 seconds.</p>
<h3 id="1-turn-on-local-emergency-disconnect"><ol>
<li>Turn on Local Emergency Disconnect</li>
</ol></h3>
<p>To enable the feature, deploy the <code>local_emergency_signal_enabled</code> parameter via your MDM. Add the following to your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">MDM file</a>:</p>
<pre><code class="language-xml">&lt;key&gt;local_emergency_signal_enabled&lt;/key&gt;&#10;&lt;true /&gt;&#10;</code></pre>
<p>The Cloudflare One Client will begin monitoring the <a href="#signal-file-path">signal file path</a> once the MDM setting is applied. Configuration changes take effect without requiring a client restart.</p>
<h3 id="2-test-local-emergency-disconnect"><ol start="2">
<li>Test Local Emergency Disconnect</li>
</ol></h3>
<ol>
<li>Ensure that the Cloudflare One Client is connected.</li>
<li>Ensure that Local Emergency Disconnect is <a href="#1-turn-on-local-emergency-disconnect">turned on</a>.</li>
<li>Create the signal file at the <a href="#signal-file-path">appropriate path</a> for your operating system with the following content:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6261.md")
</div></div>
<p>The Cloudflare One Client will automatically disconnect within 30 seconds, and the Cloudflare One Client GUI will display <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#admin-directed-disconnect"><code>Admin directed disconnect</code></a>.</p>
<p>To reconnect, change <code>emergency_disconnect</code> to <code>false</code> or remove the file:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6265.md")
</div></div>
<h2 id="logs">Logs</h2>
<p>Since emergency disconnect signals from external endpoints and local files are independent from Cloudflare's infrastructure, these disconnects are not logged by Cloudflare. Dashboard logs will only report changes to feature settings (such as turning on/off the feature or changing the endpoint URL), not disconnection events.</p>
<p>To get the current emergency disconnect status on a device, run:</p>
<pre><code class="language-sh">warp-cli settings&#10;</code></pre>
<pre><code class="language-sh">Merged configuration:&#10;(override)	Emergency disconnect: true (issued @ 2025-12-09T13:57:42.597864Z)&#10;</code></pre>
<p>The current status is also available in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#macoswindowslinux">client diagnostic logs</a> in <code>warp-settings.txt</code>.</p>
<h2 id="clear-emergency-disconnect-state">Clear emergency disconnect state</h2>
<h3 id="clear-external-emergency-disconnect">Clear External Emergency Disconnect</h3>
<p>If the external endpoint becomes unavailable or serves an invalid configuration, Cloudflare One Clients can get stuck in the emergency disconnect state. You can recover clients by removing their External Emergency Disconnect configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6269.md")
</div></div>
<h3 id="clear-local-emergency-disconnect">Clear Local Emergency Disconnect</h3>
<p>To clear the local emergency disconnect state:</p>
<ol>
<li>Remove or update the <a href="#signal-file-path">signal file</a> so that <code>emergency_disconnect</code> is <code>false</code>.</li>
<li>Alternatively, remove the <code>local_emergency_signal_enabled</code> key from your MDM profile and push the change to devices to turn off the feature. The client will stop monitoring the local file and discard its cached local signal state.</li>
</ol>
<h3 id="local-client-reset">Local client reset</h3>
<p>As a last resort, you can use the CLI to reset emergency disconnect on an individual device:</p>
<pre><code class="language-sh">warp-cli registration delete&#10;</code></pre>
<p>This command will clear the client registration, clear the local policy, and discard the cached emergency state. To reconnect, you will need to <a href="#clear-external-emergency-disconnect">turn off External Emergency Disconnect</a> and then <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">re-enroll the Cloudflare One Client</a> with your Zero Trust organization.</p>
<h2 id="device-client-settings-precedence">Device client settings precedence</h2>
<p>Learn how global disconnect settings interact and how they impact other device client profile settings.</p>
<h3 id="global-disconnection-settings">Global disconnection settings</h3>
<p>The client will honor disconnect signals from the Cloudflare dashboard (via <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-the-cloudflare-one-client-on-all-devices">Disconnect the Cloudflare One Client on all devices</a>), the external endpoint, and the local signal file. A global disconnect is enforced if <strong>any</strong> source triggers it. All sources must indicate normal operation for the client to reconnect.</p>
<p>The following table shows how the three signal sources combine. If <strong>any</strong> source indicates disconnect, the client disconnects.</p>
<table>
<thead>
<tr>
<th>Dashboard (<a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-the-cloudflare-one-client-on-all-devices">Disconnect all devices</a>)</th>
<th>External endpoint</th>
<th>Local file</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td>On</td>
<td><code>true</code></td>
<td><code>true</code></td>
<td>Force disconnected</td>
</tr>
<tr>
<td>On</td>
<td><code>true</code></td>
<td><code>false</code>/absent</td>
<td>Force disconnected</td>
</tr>
<tr>
<td>On</td>
<td><code>false</code></td>
<td><code>true</code></td>
<td>Force disconnected</td>
</tr>
<tr>
<td>On</td>
<td><code>false</code></td>
<td><code>false</code>/absent</td>
<td>Force disconnected</td>
</tr>
<tr>
<td>Off</td>
<td><code>true</code></td>
<td><code>true</code></td>
<td>Force disconnected</td>
</tr>
<tr>
<td>Off</td>
<td><code>true</code></td>
<td><code>false</code>/absent</td>
<td>Force disconnected</td>
</tr>
<tr>
<td>Off</td>
<td><code>false</code></td>
<td><code>true</code></td>
<td>Force disconnected</td>
</tr>
<tr>
<td>Off</td>
<td><code>false</code></td>
<td><code>false</code>/absent</td>
<td>Normal operation</td>
</tr>
</tbody>
</table>
<h3 id="auto-connect">Auto connect</h3>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">Auto connect</a> does not apply while a global disconnect is in effect.</p>
<h3 id="lock-device-client-switch">Lock device client switch</h3>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch">Lock device client switch</a> does not apply while a global disconnect is in effect. Users will be unable to connect the Cloudflare One Client unless they have an <a href="#admin-override">admin override code</a>.</p>
<h3 id="admin-override">Admin override</h3>
<p>A global disconnect will clear any existing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes">admin override codes</a>. The only way for users to reconnect during a global disconnect is by using a new <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes">admin override code</a>. For example, you may want to provide IT staff with a code so that they can test resolution of the incident that led to the global disconnect. The override code will exempt a specific user and device from the global disconnect until the override timeout expires.</p>
