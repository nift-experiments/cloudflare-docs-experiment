<p>When you deploy User Workers through Workers for Platforms, you can attach <a href="/workers/runtime-apis/bindings/">bindings</a> to give them access to resources like <a href="/kv/">KV namespaces</a>, <a href="/d1/">D1 databases</a>, <a href="/r2/">R2 buckets</a>, and more. This enables your end customers to build more powerful applications without you having to build the infrastructure components yourself.</p>
<p>Bindings attached during upload remain available to every invocation of that user Worker. To provide a request-scoped platform capability instead, <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/#pass-data-and-capabilities-per-request">pass an RPC stub through dynamic dispatch props</a>.</p>
<p>With bindings, each User Worker can extend functionality to:</p>
<ul>
<li><strong>Store data</strong> with <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, <a href="/d1/">D1</a>, or <a href="/durable-objects/">Durable Objects</a></li>
<li><strong>Process work asynchronously</strong> with <a href="/queues/">Queues</a> and <a href="/workflows/">Workflows</a></li>
<li><strong>Run containers</strong> with <a href="/containers/">Containers</a> (bound as a <a href="/durable-objects/">Durable Object</a>)</li>
<li><strong>Connect to private networks</strong> with <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a>, <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>, and <a href="/hyperdrive/">Hyperdrive</a></li>
<li><strong>Collect metrics</strong> with <a href="/analytics/analytics-engine/">Analytics Engine</a></li>
</ul>
<h4 id="resource-isolation">Resource isolation</h4>
<p>Each User Worker can only access the bindings that are explicitly attached to it. For complete isolation, you can create and attach a unique resource (like a D1 database or KV namespace) to every User Worker.</p>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-5.svg" alt="Resource Isolation Model" title="Resource Isolation Model" /></p>
<h2 id="adding-a-kv-namespace-to-a-user-worker">Adding a KV Namespace to a User Worker</h2>
This example walks through how to create a [KV namespace](/kv/) and attach it to a User Worker. The same process can be used to attach to other [bindings](/workers/runtime-apis/bindings/).
<h3 id="1-create-a-kv-namespace"><ol>
<li>Create a KV namespace</li>
</ol></h3>
Create a KV namespace using the [Cloudflare API](/api/resources/kv/subresources/namespaces/methods/bulk_update/).
<h3 id="2-attach-the-kv-namespace-to-the-user-worker"><ol start="2">
<li>Attach the KV namespace to the User Worker</li>
</ol></h3>
<p>Use the <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">Upload User Worker API</a> to attach the KV namespace binding to the Worker. You can do this when you're first uploading the Worker script or when updating an existing Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4232.md")
</aside>
<h5 id="example-api-request">Example API request</h5>
<pre><code class="language-bash">curl -X PUT \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account-id&gt;/workers/dispatch/namespaces/&lt;your-namespace&gt;/scripts/&lt;script-name&gt;&quot; \&#10;  &#45;H &quot;Content-Type: multipart/form-data&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;api-token&gt;&quot; \&#10;  &#45;F &#x27;metadata={&#10;    &quot;main_module&quot;: &quot;worker.js&quot;,&#10;    &quot;bindings&quot;: [&#10;      {&#10;        &quot;type&quot;: &quot;kv_namespace&quot;,&#10;        &quot;name&quot;: &quot;USER_KV&quot;,&#10;        &quot;namespace_id&quot;: &quot;&lt;your-namespace-id&gt;&quot;&#10;      }&#10;    ]&#10;  }&#x27; \&#10;  &#45;F &#x27;worker.js=@/path/to/worker.js&#x27;&#10;</code></pre>
<p>Now, the User Worker can access the <code>USER_KV</code> binding through the <code>env</code> argument using <code>env.USER_KV.get()</code>, <code>env.USER_KV.put()</code>, and other KV methods.</p>
<p>Note: If you plan to add new bindings to the Worker, use the <code>keep_bindings</code> parameter to ensure existing bindings are preserved while adding new ones.</p>
<pre><code class="language-bash">curl -X PUT \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account-id&gt;/workers/dispatch/namespaces/&lt;your-namespace&gt;/scripts/&lt;script-name&gt;&quot; \&#10;  &#45;H &quot;Content-Type: multipart/form-data&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;api-token&gt;&quot; \&#10;  &#45;F &#x27;metadata={&#10;    &quot;bindings&quot;: [&#10;      {&#10;        &quot;type&quot;: &quot;r2_bucket&quot;,&#10;        &quot;name&quot;: &quot;STORAGE&quot;,&#10;        &quot;bucket_name&quot;: &quot;&lt;your-bucket-name&gt;&quot;&#10;      }&#10;    ],&#10;    &quot;keep_bindings&quot;: [&quot;kv_namespace&quot;]&#10;  }&#x27;&#10;</code></pre>
