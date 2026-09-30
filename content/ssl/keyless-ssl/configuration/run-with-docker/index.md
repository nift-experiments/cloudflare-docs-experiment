<p>The <code>gokeyless</code> key server is published as a container image, and most settings can be configured with environment variables instead of a <code>gokeyless.yaml</code> file.</p>
<h2 id="pull-the-image">Pull the image</h2>
<pre><code class="language-sh">docker pull ghcr.io/cloudflare/gokeyless:latest&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14207.md")
</aside>
<p>A complete example is available in <a href="https://github.com/cloudflare/gokeyless/blob/master/docker-compose.example.yaml"><code>docker-compose.example.yaml</code></a> in the gokeyless repository.</p>
<h2 id="environment-variables">Environment variables</h2>
<p>Each environment variable maps to the equivalent setting in <code>gokeyless.yaml</code>. When both are present, the environment variable takes precedence (the order is command-line flag, then environment variable, then configuration file).</p>
<table>
<thead>
<tr>
<th>Environment variable</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>KEYLESS_HOSTNAME</code></td>
<td>Hostname of this key server (must match the value configured in Cloudflare).</td>
</tr>
<tr>
<td><code>KEYLESS_ZONE_ID</code></td>
<td>Cloudflare Zone ID.</td>
</tr>
<tr>
<td><code>KEYLESS_ORIGIN_CA_API_KEY</code></td>
<td>Origin CA API key used to enroll the key server and obtain its authentication certificate.</td>
</tr>
<tr>
<td><code>KEYLESS_AUTH_CERT</code></td>
<td>Path to the key server authentication certificate (default <code>server.pem</code>).</td>
</tr>
<tr>
<td><code>KEYLESS_AUTH_KEY</code></td>
<td>Path to the authentication certificate private key (default <code>server-key.pem</code>).</td>
</tr>
<tr>
<td><code>KEYLESS_AUTH_CSR</code></td>
<td>Path to write the CSR generated during initialization (default <code>server.csr</code>).</td>
</tr>
<tr>
<td><code>KEYLESS_CLOUDFLARE_CA_CERT</code></td>
<td>Path to the Cloudflare CA certificate used to authenticate connecting key clients (default <code>keyless_cacert.pem</code>).</td>
</tr>
<tr>
<td><code>KEYLESS_PORT</code></td>
<td>Port the key server listens on (default <code>2407</code>).</td>
</tr>
<tr>
<td><code>KEYLESS_METRICS_PORT</code></td>
<td>Port for the <code>/metrics</code> endpoint (default <code>2406</code>).</td>
</tr>
<tr>
<td><code>KEYLESS_LOGLEVEL</code></td>
<td>Log verbosity, <code>0</code> (most verbose) to <code>5</code>.</td>
</tr>
</tbody>
</table>
<h2 id="configure-private-keys">Configure private keys</h2>
<p>Private key locations <strong>cannot</strong> be set with an environment variable. Configure them with a <code>private_key_stores</code> block in <code>gokeyless.yaml</code> (each entry sets exactly one of <code>dir</code>, <code>file</code>, or <code>uri</code>), or with the <code>--private-key-dirs</code> / <code>--private-key-files</code> flags (comma-separated), passed as arguments after the image name.</p>
<h2 id="run-the-container">Run the container</h2>
<pre><code class="language-sh">docker run -d \&#10;  &#45;e KEYLESS_HOSTNAME=&lt;KEY_SERVER_HOSTNAME&gt; \&#10;  &#45;e KEYLESS_ZONE_ID=&lt;ZONE_ID&gt; \&#10;  &#45;e KEYLESS_AUTH_CERT=/config/server.pem \&#10;  &#45;e KEYLESS_AUTH_KEY=/config/server-key.pem \&#10;  &#45;e KEYLESS_CLOUDFLARE_CA_CERT=/config/keyless_cacert.pem \&#10;  &#45;v /local/config:/config:ro \&#10;  &#45;v /local/keys:/keys:ro \&#10;  &#45;p 2407:2407 \&#10;  ghcr.io/cloudflare/gokeyless:latest \&#10;  &#45;-private-key-dirs /keys&#10;</code></pre>
<p>The image entrypoint is <code>gokeyless</code>, so any command-line flags (such as <code>--private-key-dirs</code>) are appended after the image name.</p>
<h2 id="serve-multiple-private-keys">Serve multiple private keys</h2>
<p>A single key server can hold private keys for multiple certificates. List several directories or files with <code>--private-key-dirs</code> / <code>--private-key-files</code> (comma-separated), or define multiple <code>private_key_stores</code> entries in <code>gokeyless.yaml</code>.</p>
