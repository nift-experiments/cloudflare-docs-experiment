<p>You can use version overrides to send a request to a specific version of your Worker in the current deployment, even those set to serve 0% of traffic.</p>
<h2 id="how-to-set-version-overrides">How to set version overrides</h2>
<p>To specify a version override in your request, set the <code>Cloudflare-Workers-Version-Overrides</code> header on the request to your Worker. <code>Cloudflare-Workers-Version-Overrides</code> is a <a href="https://www.rfc-editor.org/rfc/rfc8941#name-dictionaries">Dictionary Structured Header</a> that can contain multiple key-value pairs. Each <strong>key</strong> indicates the name of the Worker the override should be applied to. The <strong>value</strong> indicates the version ID that should be used and must be a <a href="https://www.rfc-editor.org/rfc/rfc8941#name-strings">String</a>. For example:</p>
<pre><code class="language-sh">curl -s https://example.com -H &#x27;Cloudflare-Workers-Version-Overrides: my-worker-name=&quot;dc8dcd28-271b-4367-9840-6c244f84cb40&quot;&#x27;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="version-must-be-in-current-deployment">Version must be in current deployment</h3>
@markup("md", "content/.markup/bodies/16031.md")
</aside>
<h3 id="verify-that-version-overrides-were-applied">Verify that version overrides were applied</h3>
<p>There are a number of reasons why a request's version override may not be applied. For example:</p>
<ul>
<li>The deployment may not contain the specified version. It can take up to a couple of seconds to be available globally after a recent change.</li>
<li>The header value may not be a valid <a href="https://www.rfc-editor.org/rfc/rfc8941#name-dictionaries">Dictionary</a>.</li>
</ul>
<p>In the case that a request's version override is not applied, the request will be routed according to the percentages set in the gradual deployment configuration.</p>
<p>You can observe the version of your Worker that was invoked using <a href="https://developers.cloudflare.com/workers/observability/">Observability</a>, including in features such as <a href="/workers/observability/logs/logpush/">Logpush</a>. Alternatively, if you want to inform clients about the version they ran (e.g. for faster and more transparent debugging), you could use the <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata binding</a> and return the version ID in the Worker's response.</p>
<h2 id="smoke-test-example">Smoke test example</h2>
<p>You may want to test a new version in production before gradually deploying it to an increasing proportion of external traffic. This is commonly referred to as a &quot;smoke test&quot;.</p>
<p>In this example, your deployment is initially configured to route all traffic to a single version:</p>
<table>
<thead>
<tr>
<th align="center">Version ID</th>
<th align="center">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">db7cd8d3-4425-4fe7-8c81-01bf963b6067</td>
<td align="center">100%</td>
</tr>
</tbody>
</table>
<p>Create a new deployment using <a href="/workers/wrangler/commands/general/#versions-deploy"><code>wrangler versions deploy</code></a> and specify 0% for the new version whilst keeping the previous version at 100%.</p>
<table>
<thead>
<tr>
<th align="center">Version ID</th>
<th align="center">Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">dc8dcd28-271b-4367-9840-6c244f84cb40</td>
<td align="center">0%</td>
</tr>
<tr>
<td align="center">db7cd8d3-4425-4fe7-8c81-01bf963b6067</td>
<td align="center">100%</td>
</tr>
</tbody>
</table>
<p>Now test the new version with a version override before gradually progressing the new version to 100%:</p>
<pre><code class="language-sh">curl -s https://example.com -H &#x27;Cloudflare-Workers-Version-Overrides: my-worker-name=&quot;dc8dcd28-271b-4367-9840-6c244f84cb40&quot;&#x27;&#10;</code></pre>
<h2 id="service-bindings">Service bindings</h2>
<p>You can set the <code>Cloudflare-Workers-Version-Overrides</code> header when making a subrequest from one Worker to another using a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a>. This lets you test a specific version of a downstream Worker from an upstream Worker.</p>
<p>If you forward the original request object, the override header carries through automatically:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16032.md")
</div>
<p>Alternatively, you can set an override header explicitly:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16033.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16030.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/versions-and-deployments/gradual-deployments/version-affinity/">Version affinity</a> - Use cookies &amp; headers to pin users to a specific version during a gradual deployment.</li>
<li><a href="/workers/versions-and-deployments/gradual-deployments/">Gradual deployments</a> - Learn how percentage-based traffic splitting works.</li>
<li><a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> - How Workers communicate with each other.</li>
<li><a href="/workers/runtime-apis/bindings/version-metadata/">Version metadata binding</a> - Access version ID and tag from within your Worker.</li>
</ul>
