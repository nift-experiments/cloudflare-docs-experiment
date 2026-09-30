<p>This page lists the configuration flags for the <code>cloudflared tunnel run</code> command. For a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5353.md")
</div>, add these flags to the [tunnel service](#add-run-parameters-to-tunnel-service). If you are using a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5354.md")
</div>, add these flags to your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a> as key/value pairs.
<h2 id="add-run-parameters-to-tunnel-service">Add run parameters to tunnel service</h2>
<p>Remotely-managed tunnels run as a service on your OS. To add run parameters to the tunnel service file:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5358.md")
</div></div>
<h2 id="parameters">Parameters</h2>
<h3 id="autoupdate-freq"><code>autoupdate-freq</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --autoupdate-freq &lt;FREQ&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>24h</code></td>
</tr>
</tbody>
</table>
<p>Configures the frequency of <code>cloudflared</code> updates.</p>
<p>Built-in automatic updates are enabled when <code>cloudflared</code> is installed as a standalone binary and runs as a service. They are not available on Windows, for package-manager installations, or when <code>cloudflared</code> runs interactively in a terminal. When an update is available, <code>cloudflared</code> restarts to use the new version. The updater does not wait for the replacement process to connect to Cloudflare before shutting down the old process. Active connections may be interrupted. To control when updates occur, use <a href="#no-autoupdate"><code>no-autoupdate</code></a>.</p>
<h3 id="config"><code>config</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5352.md")
</aside>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --config &lt;PATH&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>~/.cloudflared/config.yml</code></td>
</tr>
</tbody>
</table>
<p>Specifies the path to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a> in YAML format.</p>
<h3 id="dns-resolver-addrs"><code>dns-resolver-addrs</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5351.md")
</aside>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel run --dns-resolver-addrs &lt;IP:PORT&gt; &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_DNS_RESOLVER_ADDRS</code></td>
</tr>
</tbody>
</table>
<p>Specifies custom DNS resolver addresses for <code>cloudflared</code> to use instead of the host machine's default resolvers. Each address must be in <code>ip:port</code> format — providing an IP address without a port will cause <code>cloudflared</code> to fail to start. You can specify multiple resolvers by repeating the flag. For example,</p>
<pre><code class="language-sh">cloudflared tunnel run --dns-resolver-addrs 1.1.1.1:53 --dns-resolver-addrs 1.0.0.1:53 &lt;UUID or NAME&gt;&#10;</code></pre>
<p>When multiple resolvers are specified, <code>cloudflared</code> randomly selects one for each DNS request. A maximum of 10 resolver addresses are allowed.</p>
<h3 id="edge-bind-address"><code>edge-bind-address</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --edge-bind-address &lt;IP&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_EDGE_BIND_ADDRESS</code></td>
</tr>
</tbody>
</table>
<p>Specifies the outgoing IP address used to establish a connection between <code>cloudflared</code> and the Cloudflare global network.</p>
<p>By default, <code>cloudflared</code> lets the operating system decide which IP address to use. This option is useful if you have multiple network interfaces available and want to prefer a specific interface.</p>
<p>The IP version of <code>edge-bind-address</code> will override <a href="#edge-ip-version"><code>edge-ip-version</code></a> (if provided). For example, if you enter an IPv6 source address, <code>cloudflared</code> will always connect to an IPv6 destination.</p>
<h3 id="edge-ip-version"><code>edge-ip-version</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --edge-ip-version &lt;VERSION&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>4</code></td>
<td><code>TUNNEL_EDGE_IP_VERSION</code></td>
</tr>
</tbody>
</table>
<p>Specifies the IP address version (IPv4 or IPv6) used to establish a connection between <code>cloudflared</code> and the Cloudflare global network. Available values are <code>auto</code>, <code>4</code>, and <code>6</code>.</p>
<p>The value <code>auto</code> relies on the host operating system to determine which IP version to select. The first IP version returned from the DNS resolution of the region lookup will be used as the primary set. In dual IPv6 and IPv4 network setups, <code>cloudflared</code> will separate the IP versions into two address sets that will be used to fallback in connectivity failure scenarios.</p>
<h3 id="grace-period"><code>grace-period</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --grace-period &lt;PERIOD&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>30s</code></td>
<td><code>TUNNEL_GRACE_PERIOD</code></td>
</tr>
</tbody>
</table>
<p>When <code>cloudflared</code> receives SIGINT/SIGTERM it will stop accepting new requests, wait for in-progress requests to terminate, then shut down. Waiting for in-progress requests will timeout after this grace period, or when a second SIGTERM/SIGINT is received.</p>
<h3 id="log-directory"><code>log-directory</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --log-directory &lt;PATH&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_LOGDIRECTORY</code></td>
</tr>
</tbody>
</table>
<p>Writes logs to a file named <code>cloudflared.log</code> in the specified directory. When the file reaches 1 MB, <code>cloudflared</code> rotates it and keeps up to five backup files. Rotation is based on file size; there is no age-based retention.</p>
<p>Use <code>log-directory</code> for routine persistent logging. If you also specify <a href="#logfile"><code>logfile</code></a>, <code>logfile</code> takes precedence.</p>
<h3 id="logfile"><code>logfile</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --logfile &lt;PATH&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_LOGFILE</code></td>
</tr>
</tbody>
</table>
<p>Saves the application log to this file. <code>cloudflared</code> does not rotate this file. Use <code>logfile</code> for short troubleshooting sessions or when another tool manages log rotation. If you also specify <a href="#log-directory"><code>log-directory</code></a>, <code>logfile</code> takes precedence. For more details on what information you need when contacting Cloudflare support, refer to <a href="/cloudflare-one/faq/cloudflare-tunnels-faq/">this guide</a>.</p>
<h3 id="loglevel"><code>loglevel</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --loglevel &lt;VALUE&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>info</code></td>
<td><code>TUNNEL_LOGLEVEL</code></td>
</tr>
</tbody>
</table>
<p>Specifies the verbosity of logging for the local <code>cloudflared</code> instance. Available values are <code>debug</code>, <code>info</code> (default), <code>warn</code>, <code>error</code>, and <code>fatal</code>. At the <code>debug</code> level, <code>cloudflared</code> will log and display the request URL, method, protocol, content length, as well as all request and response headers. However, note that this can expose sensitive information in your logs.</p>
<h3 id="metrics"><code>metrics</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --metrics &lt;IP:PORT&gt; run &lt;UUID or NAME&gt;</code></td>
<td>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/">Tunnel metrics</a></td>
<td><code>TUNNEL_METRICS</code></td>
</tr>
</tbody>
</table>
<p>Exposes a Prometheus endpoint on the specified IP address and port, which you can then query for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/">usage metrics</a>.</p>
<h3 id="no-autoupdate"><code>no-autoupdate</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5350.md")
</aside>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --no-autoupdate run &lt;UUID or NAME&gt;</code></td>
<td><code>NO_AUTOUPDATE</code></td>
</tr>
</tbody>
</table>
<p>Disables automatic <code>cloudflared</code> updates. To change the automatic update interval instead, refer to <a href="#autoupdate-freq"><code>autoupdate-freq</code></a>. For manual update methods and options to minimize downtime, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/">Update <code>cloudflared</code></a>.</p>
<h3 id="output"><code>output</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5349.md")
</aside>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment variables</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --output &lt;FORMAT&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>default</code></td>
<td><code>TUNNEL_LOG_OUTPUT</code><br/><code>TUNNEL_MANAGEMENT_OUTPUT</code></td>
</tr>
</tbody>
</table>
<p>Specifies the console log format. Available values are <code>default</code> and <code>json</code>.</p>
<p>The <code>json</code> value formats each log line as a JSON object. This format is useful for Kubernetes deployments and log collection systems that consume JSON.</p>
<h3 id="origincert"><code>origincert</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5348.md")
</aside>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --origincert &lt;PATH&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>~/.cloudflared/cert.pem</code></td>
<td><code>TUNNEL_ORIGIN_CERT</code></td>
</tr>
</tbody>
</table>
<p>Specifies the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/tunnel-permissions/">account certificate</a> for one of your zones, authorizing the client to serve as an origin for that zone. You can obtain a certificate by using the <code>cloudflared tunnel login</code> command or by visiting <code>https://dash.cloudflare.com/argotunnel</code>.</p>
<h3 id="pidfile"><code>pidfile</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --pidfile &lt;PATH&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_PIDFILE</code></td>
</tr>
</tbody>
</table>
<p>Writes the application's process identifier (PID) to this file after the first successful connection. Mainly useful for scripting and service integration.</p>
<h3 id="post-quantum"><code>post-quantum</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel run --post-quantum &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_POST_QUANTUM</code></td>
</tr>
</tbody>
</table>
<p>By default, Cloudflare Tunnel connections over <a href="#protocol"><code>quic</code></a> are encrypted using <a href="/ssl/post-quantum-cryptography/">post-quantum cryptography (PQC)</a> but will fall back to non-PQ if there are issues connecting. If the <code>--post-quantum</code> flag is provided, <code>quic</code> connections are only allowed to use PQ key agreements, with no fallback to non-PQ.</p>
<p>Post-quantum key agreements are not supported when using <code>http2</code> protocol.</p>
<h3 id="protocol"><code>protocol</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --protocol &lt;VALUE&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>auto</code></td>
<td><code>TUNNEL_TRANSPORT_PROTOCOL</code></td>
</tr>
</tbody>
</table>
<p>Specifies the protocol used to establish a connection between <code>cloudflared</code> and the Cloudflare global network. Available values are <code>auto</code>, <code>http2</code>, and <code>quic</code>.</p>
<p>The <code>auto</code> value will automatically configure the <code>quic</code> protocol. If <code>cloudflared</code> is unable to establish UDP connections, it will fallback to using the <code>http2</code> protocol.</p>
<h3 id="region"><code>region</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --region &lt;VALUE&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_REGION</code></td>
</tr>
</tbody>
</table>
<p>Allows you to choose the regions to which connections are established. Currently the only available value is <code>us</code>, which routes all connections through data centers in the United States. Omit or leave empty to connect to the global region.</p>
<p>When the region is set to <code>us</code>, <code>cloudflared</code> uses different US-specific hostnames and IPs. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#region-us">Tunnel with firewall</a> for details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5347.md")
</aside>
<h3 id="retries"><code>retries</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Default</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --retries &lt;VALUE&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>5</code></td>
<td><code>TUNNEL_RETRIES</code></td>
</tr>
</tbody>
</table>
<p>Specifies the maximum number of retries for connection/protocol errors. Retries use exponential backoff (retrying at 1, 2, 4, 8, 16 seconds by default), so it is not recommended that you increase this value significantly.</p>
<h3 id="tag"><code>tag</code></h3>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel --tag &lt;KEY=VAL&gt; run &lt;UUID or NAME&gt;</code></td>
<td><code>TUNNEL_TAG</code></td>
</tr>
</tbody>
</table>
<p>Specifies custom tags used to identify this tunnel. Multiple tags may be specified by adding additional <code>--tag &lt;KEY=VAL&gt;</code> flags to the command. If entering multiple tags into a configuration file, delimit with commas: <code>tag: {KEY1=VALUE1, KEY2=VALUE2}</code>.</p>
<h3 id="token"><code>token</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5346.md")
</aside>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel run --token &lt;TUNNEL_TOKEN&gt;</code></td>
<td><code>TUNNEL_TOKEN</code></td>
</tr>
</tbody>
</table>
<p>Associates the <code>cloudflared</code> instance with a specific tunnel. The tunnel's token is shown in the dashboard when you first <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">create the tunnel</a>. You can also retrieve the token using the <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/token/methods/get/">API</a>.</p>
<h3 id="token-file"><code>token-file</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5345.md")
</aside>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Environment Variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel run --token-file &lt;PATH&gt;</code></td>
<td><code>TUNNEL_TOKEN_FILE</code></td>
</tr>
</tbody>
</table>
<p>Associates the <code>cloudflared</code> instance with a specific tunnel using a file which contains the token.</p>
