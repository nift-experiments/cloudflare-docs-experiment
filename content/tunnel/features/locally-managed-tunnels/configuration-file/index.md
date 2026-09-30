<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14979.md")
</aside>
<p>Locally-managed tunnels run as an instance of <code>cloudflared</code> on your machine. You can configure <code>cloudflared</code> properties by modifying <a href="/tunnel/configuration/#run-parameters">command line parameters</a> or by editing the tunnel <a href="/tunnel/features/locally-managed-tunnels/create-local-tunnel/#4-create-a-configuration-file">configuration file</a>.</p>
<p>The CLI provides a quick way to handle configurations if you are connecting a single service through <code>cloudflared</code>. The tunnel configuration file is useful if you are connecting multiple services and need to configure properties or exceptions for specific origins. In the configuration file, you can define top-level properties for your <code>cloudflared</code> instance as well as <a href="/tunnel/configuration/#origin-parameters">origin-specific properties</a>. For a full list of configuration options, type <code>cloudflared tunnel help</code> in your terminal.</p>
<p>In the absence of a configuration file, <code>cloudflared</code> will proxy outbound traffic through port <code>8080</code>.</p>
<h2 id="file-structure-for-published-applications">File structure for published applications</h2>
<p>If you are exposing local services to the Internet, you can assign a public hostname to each service:</p>
<pre><code class="language-yml">tunnel: 6ff42ae2-765d-4adf-8112-31c55c1551ef&#10;credentials-file: /root/.cloudflared/6ff42ae2-765d-4adf-8112-31c55c1551ef.json&#10;&#10;ingress:&#10;  &#45; hostname: gitlab.widgetcorp.tech&#10;    service: http://localhost:80&#10;  &#45; hostname: gitlab-ssh.widgetcorp.tech&#10;    service: ssh://localhost:22&#10;  &#45; service: http_status:404&#10;</code></pre>
<p>Configuration files that contain ingress rules must always include a catch-all rule that concludes the file. In this example, <code>cloudflared</code> will respond with a <code>404</code> status code when the request does not match any of the previous hostnames.</p>
<h3 id="how-traffic-is-matched">How traffic is matched</h3>
<p>When <code>cloudflared</code> receives an incoming request, it evaluates each ingress rule from top to bottom to find which rule matches the request. Rules can match either the hostname or path of an incoming request, or both. If a rule does not specify a hostname, all hostnames will be matched. If a rule does not specify a path, all paths will be matched.</p>
<p>The last ingress rule must be a catch-all rule that matches all traffic.</p>
<p>Here is an example configuration file that specifies several rules:</p>
<pre><code class="language-yml">tunnel: 6ff42ae2-765d-4adf-8112-31c55c1551ef&#10;credentials-file: /root/.cloudflared/6ff42ae2-765d-4adf-8112-31c55c1551ef.json&#10;&#10;ingress:&#10;  &#35; Rules map traffic from a hostname to a local service:&#10;  &#45; hostname: example.com&#10;    service: https://localhost:8000&#10;  &#35; Rules can match the request&#x27;s path to a regular expression:&#10;  &#45; hostname: static.example.com&#10;    path: \.(jpg|png|css|js)$&#10;    service: https://localhost:8001&#10;  &#35; Rules can match the request&#x27;s hostname to a wildcard character:&#10;  &#45; hostname: &quot;*.example.com&quot;&#10;    service: https://localhost:8002&#10;  &#35; An example of a catch-all rule:&#10;  &#45; service: https://localhost:8003&#10;</code></pre>
<h4 id="wildcards">Wildcards</h4>
<p>You can use wildcards to match traffic to multiple subdomains. For example, if you set the <code>hostname</code> key to <code>*.example.com</code>, both <code>alpha.example.com</code> and <code>beta.example.com</code> will route traffic to your origin. <code>cloudflared</code> does not support wildcards in the middle of the hostname, such as <code>test.*.example.com</code>.</p>
<p>You can also enter regular expressions for the <code>path</code> key. For example, if <code>hostname</code> is <code>static.example.com</code> and <code>path</code> is <code>\.(jpg|png|css|js)$</code>, matching URLs could include <code>https://static.example.com/data.js</code>, <code>http://static.example.com/images/photo.jpg</code>, and so on. Cloudflare parses the path regex using the <a href="https://pkg.go.dev/regexp/syntax">Go <code>syntax</code> package</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-forwarding">Path forwarding</h3>
@markup("md", "content/.markup/bodies/14978.md")
</aside>
<h3 id="services">Services</h3>
<p>In addition to HTTP, <code>cloudflared</code> supports protocols like SSH, RDP, arbitrary TCP services, and Unix sockets. You can also route traffic to the built-in <code>hello_world</code> test server or respond to traffic with an HTTP status. For a full list of supported service types, refer to <a href="/tunnel/concepts/routing/#supported-protocols">Protocols for published applications</a>.</p>
<pre><code class="language-yml">tunnel: 6ff42ae2-765d-4adf-8112-31c55c1551ef&#10;credentials-file: /root/.cloudflared/6ff42ae2-765d-4adf-8112-31c55c1551ef.json&#10;&#10;ingress:&#10;  &#35; Example of a request over TCP:&#10;  &#45; hostname: example.com&#10;    service: tcp://localhost:8000&#10;  &#35; Example of an HTTP request over a Unix socket:&#10;  &#45; hostname: staging.example.com&#10;    service: unix:/home/production/echo.sock&#10;  &#35; Example of a request mapping to the Hello World test server:&#10;  &#45; hostname: test.example.com&#10;    service: hello_world&#10;  &#35; Example of a rule responding to traffic with an HTTP status:&#10;  &#45; service: http_status:404&#10;</code></pre>
<h3 id="origin-configuration">Origin configuration</h3>
<p>If you need to proxy traffic to multiple origins within one instance of <code>cloudflared</code>, you can define the way <code>cloudflared</code> sends requests to each service by specifying <a href="/tunnel/configuration/#origin-parameters">configuration options</a> as part of your ingress rules.</p>
<p>In the following example, the top-level configuration <code>connectTimeout: 30s</code> sets a 30-second connection timeout for all services within that instance of <code>cloudflared</code>. The ingress rule for <code>service: localhost:8002</code> then configures an exception to the top-level configuration by setting <code>connectTimeout</code> for that service at <code>10s</code>. The 30-second connection timeout still applies to all other services.</p>
<pre><code class="language-yml">tunnel: 6ff42ae2-765d-4adf-8112-31c55c1551ef&#10;credentials-file: /root/.cloudflared/6ff42ae2-765d-4adf-8112-31c55c1551ef.json&#10;originRequest: # Top-level configuration&#10;  connectTimeout: 30s&#10;&#10;ingress:&#10;  &#35; The localhost:8000 service inherits all root-level configuration.&#10;  &#35; In other words, it will use a connectTimeout of 30 seconds.&#10;  &#45; hostname: example.com&#10;    service: localhost:8000&#10;  &#45; hostname: example2.com&#10;    service: localhost:8001&#10;  &#35; The localhost:8002 service overrides some root-level config.&#10;  &#45; service: localhost:8002&#10;    originRequest:&#10;      connectTimeout: 10s&#10;      disableChunkedEncoding: true&#10;  &#35; Some built-in services such as `http_status` do not use any configuration.&#10;  &#35; The service below will simply respond with HTTP 404.&#10;  &#45; service: http_status:404&#10;</code></pre>
<h3 id="validate-ingress-rules">Validate ingress rules</h3>
<p>To validate the ingress rules in your configuration file, run:</p>
<pre><code class="language-sh">cloudflared tunnel ingress validate&#10;</code></pre>
<p>This will ensure that the set of ingress rules specified in your config file is valid.</p>
<h3 id="test-ingress-rules">Test ingress rules</h3>
<p>To verify that <code>cloudflared</code> will proxy the right traffic to the right local service, use <code>cloudflared tunnel ingress rule</code>. This checks a URL against every rule, from first to last, and shows the first rule that matches. For example:</p>
<pre><code class="language-sh">cloudflared tunnel ingress rule https://foo.example.com&#10;</code></pre>
<pre><code class="language-sh">Using rules from /usr/local/etc/cloudflared/config.yml&#10;Matched rule #3&#10;	hostname: *.example.com&#10;	service: https://localhost:8000&#10;</code></pre>
<h2 id="update-a-configuration-file">Update a configuration file</h2>
<p>When making changes to the configuration file for a given tunnel, we suggest relying on <a href="/tunnel/configuration/#replicas-and-high-availability"><code>cloudflared</code> replicas</a> to propagate the new configuration with minimal downtime.</p>
<ol>
<li>Have a <code>cloudflared</code> instance running with the original version of the configuration file.</li>
<li>Start a <code>cloudflared</code> replica running with the updated version of the configuration file.</li>
<li>Wait for the replica to be fully running and usable.</li>
<li>Stop the first instance of <code>cloudflared</code>.</li>
</ol>
<p>Your <code>cloudflared</code> will now be running with the updated version of your configuration file.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="traffic-handling">Traffic handling</h3>
@markup("md", "content/.markup/bodies/14977.md")
</aside>
