<p>If your query returns an error even after configuring and embedding a client SSL certificate, check the following settings.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14012.md")
</aside>
<hr />
<h2 id="check-ssl-tls-handshake">Check SSL/TLS handshake</h2>
<p>On your terminal, use the following command to check whether an SSL/TLS connection can be established successfully between the client and the API endpoint.</p>
<pre><code class="language-sh">curl --verbose --cert /path/to/certificate.pem --key /path/to/key.pem https://your-api-endpoint.com&#10;</code></pre>
<p>If the SSL/TLS handshake cannot be completed, check whether the certificate and the private key are correct.
If the handshake completes but requests are still blocked, confirm that Cloudflare is verifying the client certificate.</p>
<hr />
<h2 id="check-mtls-hosts">Check mTLS hosts</h2>
<p>Check whether <a href="/ssl/client-certificates/enable-mtls/">mTLS has been enabled</a> for the correct host. The host should match the API endpoint that you want to protect.</p>
<hr />
<h2 id="review-mtls-rules">Review mTLS rules</h2>
<p>To review mTLS rules, consider the steps below. For further guidance refer to <a href="/waf/custom-rules/create-dashboard/">Custom rules</a>.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On a specific rule, select <strong>Edit</strong>.</p>
</li>
<li>
<p>On that rule, check whether:</p>
<ul>
<li>The Expression Preview is correct.</li>
<li>The hostname, if defined, matches your API endpoint. For example, for the API endpoint <code>api.trackers.ninja/time</code>, the rule should look like:</li>
</ul>
</li>
</ol>
<pre><code class="language-txt">(http.host in {&quot;api.trackers.ninja&quot;} and not cf.tls_client_auth.cert_verified)&#10;</code></pre>
<ol start="4">
<li>To edit the rule, either use the user interface or select <strong>Edit expression</strong>.</li>
</ol>
<hr />
<h2 id="advanced-debugging">Advanced debugging</h2>
<p>You can use <a href="/workers/">Cloudflare Workers</a> to debug client certificate validation failures.</p>
<ol>
<li>Create a Worker to debug print <a href="/workers/runtime-apis/request/#incomingrequestcfproperties">cf.properties</a>:</li>
</ol>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    console.info({ message: JSON.stringify(request.cf, null, 2) });&#10;    return new Response(JSON.stringify(request.cf, null, 2))&#10;  }&#10;};&#10;</code></pre>
<ol start="2">
<li>
<p>Associate the Worker with the hostname where mTLS is enabled using a <a href="/workers/configuration/routing/routes/">Worker route</a> or a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a>.</p>
</li>
<li>
<p>Make requests to the hostname and/or path configured, with and without sending the mTLS client certificate.</p>
</li>
<li>
<p>View your logs on the <a href="/workers/observability/">Observability</a> dashboard and compare the responses against the expected values listed below.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ul>
<li>Valid certificate</li>
</ul>
<pre><code class="language-json">&quot;tlsClientAuth&quot;: {&#10;  &quot;certPresented&quot;: &quot;1&quot;,&#10;  &quot;certVerified&quot;: &quot;SUCCESS&quot;,&#10;},&#10;</code></pre>
<ul>
<li>Invalid certificate (for example, self-signed certificates)</li>
</ul>
<pre><code class="language-json">&quot;tlsClientAuth&quot;: {&#10;  &quot;certPresented&quot;: &quot;1&quot;,&#10;  &quot;certVerified&quot;: &quot;FAILED:self signed certificate&quot;,&#10;},&#10;</code></pre>
<ul>
<li>No certificate</li>
</ul>
<pre><code class="language-json">&quot;tlsClientAuth&quot;: {&#10;  &quot;certPresented&quot;: &quot;0&quot;,&#10;  &quot;certVerified&quot;: &quot;NONE&quot;,&#10;},&#10;</code></pre>
