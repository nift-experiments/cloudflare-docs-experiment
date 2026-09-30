<p>This tutorial covers how to use a <a href="/workers/">Cloudflare Worker</a> to add custom HTTP headers to traffic, and how to send those custom headers to your origin services protected by <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>.</p>
<p>Some applications and networking implementations require specific custom headers to be passed to the origin, which can be difficult to implement for traffic moving through a Zero Trust proxy. You can configure a Worker to send the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/">user authorization headers</a> required by Access.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Secure your origin server with Cloudflare Access</li>
</ul>
<h2 id="before-you-begin-1">Before you begin</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>If this is your first Worker, select <strong>Create Worker</strong>. Otherwise, select <strong>Create application</strong>, then select <strong>Create Worker</strong>.</p>
</li>
<li>
<p>Enter an identifiable name for the Worker, then select <strong>Deploy</strong>.</p>
</li>
<li>
<p>Select <strong>Edit code</strong>.</p>
</li>
<li>
<p>Input the following Worker:</p>
</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4332.md")
</div>
<ol start="6">
<li>Select <strong>Save and deploy</strong>.</li>
</ol>
<p>Your Worker is now ready to send custom headers to your Access-protected origin services.</p>
<h2 id="apply-the-worker-to-your-hostname">Apply the Worker to your hostname</h2>
<ol>
<li>Select the Worker you created, then go to <strong>Triggers</strong>.</li>
<li>In <strong>Routes</strong>, select <strong>Add route</strong>.</li>
<li>Enter the hostname and zone for your origin, then select <strong>Add route</strong>.</li>
</ol>
<p>The Worker will now insert a custom header into requests that match the defined route. For example:</p>
<pre><code class="language-http">&quot;Accept&quot;: &quot;text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7&quot;,&#10;    &quot;Accept-Encoding&quot;: &quot;gzip&quot;,&#10;    &quot;Accept-Language&quot;: &quot;en-US,en;q=0.9&quot;,&#10;    &quot;Cf-Access-Authenticated-User-Email&quot;: &quot;user@example.com&quot;,&#10;    &quot;Company-User-Id&quot;: &quot;user@example.com&quot;,&#10;    &quot;Connection&quot;: &quot;keep-alive&quot;&#10;</code></pre>
