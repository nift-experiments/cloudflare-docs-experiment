<p>Outbound handlers let you intercept and modify HTTP traffic from a sandbox with trusted code.</p>
<p>Use them to:</p>
<ul>
<li>Allow or deny specific origin destinations</li>
<li>Safely inject authorization headers or tokens</li>
<li>Transparently reroute traffic</li>
<li>Add custom policy on outbound traffic (such as denying specific HTTP requests)</li>
<li><a href="/sandbox/guides/workers-connections/">Connect to Workers bindings</a> like KV, R2, and Durable Objects</li>
</ul>
<h2 id="block-outbound-traffic">Block outbound traffic</h2>
<p>Use <code>enableInternet = false</code> to block public internet access by default:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13367.md")
</div>
<p>When <code>enableInternet</code> is <code>false</code>, only traffic you explicitly allow later on this page through <code>allowedHosts</code> or outbound handlers can leave the sandbox. Only ports <code>80</code>, <code>443</code>, and DNS are available, and DNS queries use Cloudflare's DNS servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13366.md")
</aside>
<h2 id="block-or-allow-traffic-by-host">Block or allow traffic by host</h2>
<p>You can filter outbound traffic with the <code>allowedHosts</code> and <code>deniedHosts</code> properties on the Sandbox class.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13365.md")
</aside>
<p>When <code>allowedHosts</code> is set, it becomes a deny-by-default allowlist. Any host or IP not in the list is denied, and only matching destinations can reach <code>outbound</code> or <code>outboundByHost</code> handlers.</p>
<p><code>allowedHosts</code> and <code>deniedHosts</code> also support simple glob patterns where <code>*</code> matches any sequence of characters.</p>
<p>By default, a Sandbox allows internet access, and you can set <code>deniedHosts</code> to disallow specific hosts or IPs:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13368.md")
</div>
<p>You can also disable internet access by default, but allow specific hosts and IPs:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13369.md")
</div>
<h2 id="define-outbound-handlers">Define outbound handlers</h2>
<p>Outbound handlers are programmable egress proxies that run on the same machine as the sandbox. They have access to all Workers bindings.</p>
<p>Use <code>outbound</code> to intercept all outbound HTTP and HTTPS traffic:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13370.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13364.md")
</aside>
<p>Use <code>outboundByHost</code> to map specific domain names or IP addresses to handler functions:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13371.md")
</div>
<p>Calls to <code>http://my.worker</code> from the sandbox invoke the handler, which runs inside the Workers runtime, outside the sandbox.</p>
<p><code>deniedHosts</code> and <code>allowedHosts</code> are evaluated before any outbound handler. If you use <code>allowedHosts</code>, include the hostname there for either <code>outbound</code> or <code>outboundByHost</code> to run. <code>outboundByHost</code> handlers take precedence over catch-all <code>outbound</code> handlers.</p>
<h2 id="securely-inject-credentials">Securely inject credentials</h2>
<p>Because outbound handlers run in the Workers runtime — outside the sandbox — they can hold secrets that the sandbox itself never sees. The sandbox makes a plain HTTP request, and the handler attaches the credential before forwarding it to the upstream service.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13372.md")
</div>
<p>This is especially useful for agentic workloads where you cannot fully trust the code running inside the sandbox. With this pattern:</p>
<ul>
<li><strong>No token is exposed to the sandbox.</strong> The secret lives in the Worker's environment and is never passed into the sandbox.</li>
<li><strong>No token rotation inside the sandbox.</strong> Rotate the secret in your Worker's environment and every request picks it up immediately.</li>
<li><strong>Per-host and per-instance rules.</strong> Combine <code>outboundByHost</code> with <code>ctx.containerId</code> to scope credentials or permissions to a specific sandbox instance.</li>
</ul>
<p>Here, <code>ctx.containerId</code> looks up a per-instance key from KV:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13373.md")
</div>
<h2 id="https-traffic">HTTPS traffic</h2>
<p>Sandboxes intercept HTTPS traffic by default — <code>interceptHttps</code> is set to <code>true</code> on the Sandbox class.</p>
<p>When HTTPS interception is active, an ephemeral CA file is created at <code>/etc/cloudflare/certs/cloudflare-containers-ca.crt</code> once the sandbox starts.</p>
<p>The Sandbox runtime makes a best effort to trust this CA automatically regardless of distro. On startup, it checks common system CA bundle locations across major Linux families and configures common CA environment variables so runtimes like Node.js, <code>curl</code>, Python <code>requests</code>, and Git trust the certificate automatically.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13363.md")
</aside>
<h2 id="non-http-traffic">Non-HTTP traffic</h2>
<p>Outbound handlers only intercept HTTP and HTTPS traffic. Traffic on ports other than <code>80</code> and <code>443</code> is never routed through <code>outbound</code> or <code>outboundByHost</code>.</p>
<p>If you set <code>enableInternet = false</code>, that traffic is denied. DNS queries are the one exception, but they only go to Cloudflare's DNS servers. That prevents using arbitrary DNS destinations for data exfiltration.</p>
<h2 id="change-policies-at-runtime">Change policies at runtime</h2>
<p>Use <code>outboundHandlers</code> to define named handlers, then assign them to specific hosts at runtime using <code>setOutboundByHost()</code>. You can also apply a handler globally with <code>setOutboundHandler()</code>.</p>
<p>You can also manage runtime policy with <code>setOutboundByHosts()</code>, <code>setAllowedHosts()</code>, <code>setDeniedHosts()</code>, <code>allowHost()</code>, <code>denyHost()</code>, <code>removeAllowedHost()</code>, and <code>removeDeniedHost()</code>.</p>
<p>This lets a trusted Worker hold credentials without exposing them to an untrusted sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13374.md")
</div>
<p>Apply handlers to hosts programmatically from your Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13375.md")
</div>
<h2 id="handler-precedence">Handler precedence</h2>
<p>Requests are evaluated in this order:</p>
<ol>
<li><code>deniedHosts</code> is checked first. Matching hosts or IPs are denied immediately.</li>
<li><code>allowedHosts</code> is checked next. When it is set, any host or IP not in the list is denied. Matching hosts continue to outbound handlers, or egress to the public internet if no handler is set.</li>
<li>Instance-level rules set with <code>setOutboundByHost()</code> are checked before class-level <code>outboundByHost</code> rules.</li>
<li>Per-host handlers always take precedence over catch-all handlers, so <code>outboundByHost</code> runs before <code>outbound</code>.</li>
<li>Instance-level handlers set with <code>setOutboundHandler()</code> are checked before the class-level <code>outbound</code> handler.</li>
<li>If no handler matches, the request can still egress to the public internet when it matched <code>allowedHosts</code> or <code>enableInternet = true</code>. Otherwise, it is denied.</li>
</ol>
<h2 id="local-development">Local development</h2>
<p><code>wrangler dev</code> supports outbound interception. A sidecar process is spawned inside the sandbox's network namespace. It applies <code>TPROXY</code> rules to route matching traffic to the local Workerd instance, mirroring production behavior.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/workers-connections/">Connect to Workers bindings</a> — Access KV, R2, Durable Objects, and other bindings from a sandbox</li>
<li><a href="/containers/guides/outbound-traffic/">Handle outbound traffic (Containers)</a> — Container SDK API for outbound handlers</li>
<li><a href="/sandbox/configuration/sandbox-options/">Sandbox options</a> — Configure sandbox behavior</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> — Configure secrets and environment variables</li>
</ul>
