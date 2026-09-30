<h3 id="untrusted-mode-default">Untrusted Mode (Default)</h3>
<p>By default, Workers inside of a dispatch namespace are considered &quot;untrusted.&quot; This provides the strongest isolation between Workers and is best in cases where your customers have control over the code that's being deployed.</p>
<p>In untrusted mode:</p>
<ul>
<li>The <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>request.cf</code></a> object is not available in Workers (see <a href="/cloudflare-for-platforms/workers-for-platforms/reference/limits/#cf-object">limits</a> for more information)</li>
<li>Each Worker has an isolated cache, when using the <a href="/workers/runtime-apis/cache/">Cache API</a> or when making subrequests using <code>fetch()</code>, which egress via <a href="/cache/">Cloudflare's cache</a></li>
<li><a href="/workers/reference/how-the-cache-works/#cache-api"><code>caches.default</code></a> is disabled for all Workers in the namespace</li>
</ul>
<p>This mode ensures complete isolation between customer Workers, preventing any potential cross-tenant data access.</p>
<h3 id="trusted-mode">Trusted Mode</h3>
<p>If you control the Worker code and want to disable isolation mode, you can configure the namespace as &quot;trusted&quot;. This is useful when building internal platforms where your company controls all Worker code.</p>
<p>In trusted mode:</p>
<ul>
<li>The <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>request.cf</code></a> object becomes available, providing access to request metadata</li>
<li>All Workers in the namespace share the same cache space when using the Cache API</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4188.md")
</aside>
<p>To convert a namespace from untrusted to trusted:</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{namespace_name}&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;name&quot;: &quot;{namespace_name}&quot;,&#10;    &quot;trusted_workers&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>If you enable trusted mode for a namespace that already has deployed Workers, you'll need to redeploy those Workers for the <code>request.cf</code> object to become available. Any new Workers you deploy after enabling trusted mode will automatically have access to it.</p>
<h3 id="maintaining-cache-isolation-in-trusted-mode">Maintaining cache isolation in trusted mode</h3>
If you need access to `request.cf` but want to maintain cache isolation between customers, use customer-specific [cache keys](/workers/examples/cache-using-fetch/#custom-cache-keys) or the [Cache API](/workers/examples/cache-api/) with isolated keys. 
<h2 id="related-resources">Related Resources</h2>
* [Platform Limits](/cloudflare-for-platforms/workers-for-platforms/reference/limits) - Understanding script and API limits
* [Cache API Documentation](/workers/runtime-apis/cache/) - Learn about cache behavior in Workers
* [Request cf object](/workers/runtime-apis/request/#the-cf-property-requestcf) - Details on the cf object properties
