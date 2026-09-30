<p>This guide walks you through connecting to Privacy Proxy and verifying that traffic is proxied correctly.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Privacy Proxy is a managed service. Before you can connect, Cloudflare will provision an endpoint and provide you with:</p>
<ul>
<li><strong>Proxy endpoint URL</strong>: The hostname for your Privacy Proxy instance (for example, <code>https://your-proxy.example.com</code>).</li>
<li><strong>Pre-shared key (PSK)</strong>: A secret key for proof-of-concept authentication.</li>
<li><strong>Egress IP ranges</strong>: The IP addresses that destination servers will see for proxied traffic.</li>
</ul>
<p><a href="https://www.cloudflare.com/lp/privacy-edge/">Contact us</a> to request access and receive your configuration details.</p>
<hr />
<h2 id="1-configure-your-client"><ol>
<li>Configure your client</li>
</ol></h2>
<p>Privacy Proxy accepts connections over HTTP/2 and HTTP/3 using the HTTP CONNECT method. Because Privacy Proxy requires authentication headers, you cannot configure browsers to connect directly. Instead, use one of the following approaches:</p>
<h3 id="use-curl-for-testing-locally">Use curl for testing locally</h3>
<p>For quick tests, use curl with the <code>--proxy</code> and <code>--proxy-header</code> flags to pass authentication directly:</p>
<pre><code class="language-sh">curl -v \&#10;  &#45;-proxy https://your-proxy.example.com \&#10;  &#45;-proxy-header &quot;Proxy-Authorization: Preshared &lt;YOUR_PSK&gt;&quot; \&#10;  https://example.com&#10;</code></pre>
<h3 id="use-chaussette">Use Chaussette</h3>
<p><a href="/privacy-proxy/reference/client-libraries/#chaussette">Chaussette</a> is a local SOCKS5 proxy that handles authentication and forwards requests to Privacy Proxy.</p>
<ol>
<li>Start Chaussette with your PSK and proxy endpoint:</li>
</ol>
<pre><code class="language-sh">MASQUE_PRESHARED_KEY=&lt;YOUR_PSK&gt; chaussette \&#10;  &#45;-listen 127.0.0.1:1987 \&#10;  &#45;-proxy https://your-proxy.example.com:443&#10;</code></pre>
<ol start="2">
<li>Configure your browser to use the local SOCKS5 proxy:</li>
</ol>
<pre><code class="language-sh">google-chrome --proxy-server=&quot;socks5://127.0.0.1:1987&quot;&#10;</code></pre>
<hr />
<h2 id="2-verify-the-connection"><ol start="2">
<li>Verify the connection</li>
</ol></h2>
<p>To confirm that traffic is routing through Privacy Proxy, check your apparent IP address:</p>
<pre><code class="language-sh">curl -v \&#10;  &#45;-proxy https://your-proxy.example.com \&#10;  &#45;-proxy-header &quot;Proxy-Authorization: Preshared &lt;YOUR_PSK&gt;&quot; \&#10;  https://cloudflare.com/cdn-cgi/trace&#10;</code></pre>
<p>The response includes connection metadata. Look for the <code>ip</code> field, which should show a Cloudflare egress IP address rather than your real IP.</p>
<pre><code class="language-txt">fl=123f456&#10;h=cloudflare.com&#10;ip=162.159.xxx.xxx&#10;ts=1234567890.123&#10;visit_scheme=https&#10;uag=curl/8.0.0&#10;colo=SJC&#10;http=http/2&#10;loc=US&#10;tls=TLSv1.3&#10;</code></pre>
<p>The <code>ip</code> value confirms the egress IP address used by the proxy.</p>
<hr />
<h2 id="3-optional-test-geolocation"><ol start="3">
<li>(Optional) Test geolocation</li>
</ol></h2>
<p>Privacy Proxy preserves user geolocation by selecting egress IP addresses based on the client's location. You can specify a geohash to test this behavior:</p>
<pre><code class="language-sh">curl -v \&#10;  &#45;-proxy https://your-proxy.example.com \&#10;  &#45;-proxy-header &quot;Proxy-Authorization: Preshared &lt;YOUR_PSK&gt;&quot; \&#10;  &#45;-proxy-header &quot;sec-ch-geohash: xn76c-JP&quot; \&#10;  https://cloudflare.com/cdn-cgi/trace&#10;</code></pre>
<p>The <code>sec-ch-geohash</code> header provides a <a href="https://en.wikipedia.org/wiki/Geohash">geohash</a> that the proxy uses to select an appropriate egress IP. The format is <code>&lt;geohash&gt;-&lt;country_code&gt;</code>.</p>
<p>The response should show a <code>loc</code> value corresponding to the geohash region.</p>
<hr />
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn about <a href="/privacy-proxy/concepts/deployment-models/">deployment models</a> to understand single-hop versus double-hop architectures.</li>
<li>Review <a href="/privacy-proxy/concepts/authentication/">authentication methods</a> for production deployments using Privacy Pass.</li>
<li>Configure <a href="/privacy-proxy/reference/metrics/">observability</a> to monitor proxy traffic with GraphQL Analytics and OpenTelemetry.</li>
</ul>
