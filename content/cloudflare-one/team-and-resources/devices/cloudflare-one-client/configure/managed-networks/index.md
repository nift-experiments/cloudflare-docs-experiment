<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6168.md")
</div></details>
<p>The Cloudflare One Client (formerly WARP) allows you to selectively apply specific <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a> and device client settings when a device connects to a known network location, such as an office. To detect which network a device is on, the Cloudflare One Client connects to a TLS endpoint that you host on that network and validates its certificate. If the certificate matches, the device is on your managed network and receives the corresponding <a href="#4-configure-device-profile">device profile</a> (if one has been configured for that network).</p>
<p>On this page, you will learn how to:</p>
<ul>
<li>Create a TLS endpoint on your trusted network.</li>
<li>Configure the TLS endpoint in Zero Trust to set up a managed network.</li>
<li>Apply the appropriate device profile to a device when the Cloudflare One Client detects it is on your managed network.</li>
</ul>
<h2 id="requirements">Requirements</h2>
<ul>
<li>The Cloudflare One Client scans for managed networks when the operating system's default route changes, the SSID of the active Wi-Fi connection changes, or the DNS servers of the default interface change. To minimize performance impact, reuse the same TLS endpoint across multiple locations unless you require distinct settings profiles for each location.</li>
<li>Ensure that the device can only reach one managed network at any given time. If multiple managed networks are configured and reachable, there is no way to determine which settings profile the device will receive.</li>
</ul>
<h2 id="managed-network-detection-logic">Managed network detection logic</h2>
<p>When you configure a managed network, the Cloudflare One Client uses the TLS endpoint to determine whether the device is on that network.</p>
<p>The time it takes to apply the correct device profile depends on how quickly the TLS endpoint responds.</p>
<p>If the TLS endpoint times out after 5 seconds, the Cloudflare One Client will determine that the device is not on a managed network and will apply the default device profile. The Cloudflare One Client only retries detection if a non-timeout error occurs. A timeout triggers fallback to the default device profile without further retries.</p>
<h2 id="1-choose-a-tls-endpoint"><ol>
<li>Choose a TLS endpoint</li>
</ol></h2>
<p>A TLS endpoint is a host on your network that serves a TLS certificate. The TLS endpoint acts like a network location beacon — when a device connects to a network, the Cloudflare One Client on the device detects the TLS endpoint and validates the TLS certificate against the SHA-256 fingerprint (if specified) or against the local certificate store to check that it is signed by a public certificate authority.</p>
<p>The TLS certificate can be hosted by any device on your network. However, the endpoint must be inaccessible to users outside of the network location. The Cloudflare One Client will automatically exclude the managed network endpoint from all device profiles to ensure that users cannot connect to this endpoint over Cloudflare Tunnel. We recommend choosing a host that is physically in the office which remote users do not need to access, such as a printer.</p>
<h3 id="create-a-new-tls-endpoint">Create a new TLS endpoint</h3>
<p>If you do not already have a TLS endpoint on your network, you can set one up as follows:</p>
<ol>
<li>Generate a TLS certificate:</li>
</ol>
<pre><code class="language-sh">openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes -keyout key.pem -out cert.pem -subj &quot;/CN=example.com&quot; -addext &quot;subjectAltName=DNS:example.com&quot;&#10;</code></pre>
<pre><code>The command will output a certificate in PEM format and its private key. Store these files in a secure place.&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6167.md")
</aside>
<ol start="2">
<li>
<p>Configure an HTTPS server on your network to use this certificate and key. The example below demonstrates how to serve the TLS certificate from an nginx container in Docker:</p>
<pre><code>a. Create an nginx configuration file called `nginx.conf`:&#10;</code></pre>
</li>
</ol>
<pre><code class="language-txt">events {&#10;worker_connections  1024;&#10;}&#10;&#10;http {&#10;		server {&#10;			listen              443 ssl;&#10;			ssl_certificate     /certs/cert.pem;&#10;			ssl_certificate_key /certs/key.pem;&#10;			location / {&#10;						return 200;&#10;			}&#10;		}&#10;}&#10;</code></pre>
<pre><code>    If needed, replace `/certs/cert.pem` and `/certs/key.pem` with the locations of your certificate and key.&#10;&#10;    b. Add the nginx image to your Docker compose file:&#10;</code></pre>
<pre><code class="language-yml">services:&#10;	nginx:&#10;		image: nginx:latest&#10;		ports:&#10;			&#45; 3333:443&#10;		volumes:&#10;			&#45; ./nginx.conf:/etc/nginx/nginx.conf:ro&#10;			&#45; ./certs:/certs:ro&#10;</code></pre>
<pre><code>    	If needed, replace `./nginx.conf` and `./certs` with the locations of your nginx configuration file and certificate.&#10;&#10;    c. Start the server:&#10;</code></pre>
<pre><code class="language-sh">docker compose up -d&#10;</code></pre>
<ol start="3">
<li>To test that the TLS server is working, run a curl command from the end user's device:</li>
</ol>
<pre><code class="language-sh">curl --verbose --insecure https://&lt;private-server-IP&gt;:3333/&#10;</code></pre>
<pre><code>You need to pass the `--insecure` option because we are using a self-signed certificate. If the device is connected to the network, the request should return a `200` status code.&#10;</code></pre>
<details class="nb-details"><summary>Windows IIS</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6169.md")
</div></details>
<h3 id="supported-cipher-suites">Supported cipher suites</h3>
<p>The Cloudflare One Client establishes a TLS connection using <a href="https://github.com/rustls/rustls">Rustls</a>. Make sure your TLS endpoint accepts one of the <a href="https://docs.rs/rustls/0.21.10/src/rustls/suites.rs.html#125-143">cipher suites supported by Rustls</a>.</p>
<h2 id="2-extract-the-sha-256-fingerprint"><ol start="2">
<li>Extract the SHA-256 fingerprint</li>
</ol></h2>
<p>The SHA-256 fingerprint is only required if your TLS endpoint uses a self-signed certificate.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6172.md")
</div></div>
<h2 id="3-add-managed-network-to-cloudflare-one"><ol start="3">
<li>Add managed network to Cloudflare One</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6175.md")
</div></div>
<p>The Cloudflare One Client will automatically exclude the TLS endpoint from all device profiles if it is specified as a private IP address. This exclusion prevents remote users from accessing the endpoint through the WARP tunnel on any port. If the TLS endpoint is specified as a hostname instead of a private IP, the Cloudflare One Client will not automatically exclude it.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="split-tunnels-in-include-mode">Split Tunnels in Include mode</h3>
@markup("md", "content/.markup/bodies/6165.md")
</aside>
<h2 id="4-configure-device-profile"><ol start="4">
<li>Configure device profile</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6178.md")
</div></div>
<p>Managed networks are now enabled. Every time a device in your organization connects to a network (for example, when waking up the device or changing Wi-Fi networks), the Cloudflare One Client will determine its network location and apply the corresponding settings profile.</p>
<h2 id="5-verify-managed-network"><ol start="5">
<li>Verify managed network</li>
</ol></h2>
<p>To check if the Cloudflare One Client detects the network location:</p>
<ol>
<li>Connect the Cloudflare One Client.</li>
<li>Disconnect and reconnect to the network.</li>
<li>Open a terminal and run <code>warp-cli debug alternate-network</code>.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">Device profiles</a> - How to create and manage the device profiles you apply via managed networks.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/">Device client settings</a> - Defines how the Cloudflare One Client behaves and what users can do.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/">Cloudflare One Client troubleshooting guide</a> - Troubleshoot common Cloudflare One Client issues.</li>
</ul>
