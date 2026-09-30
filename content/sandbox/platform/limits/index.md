<p>Since the Sandbox SDK is built on top of the <a href="/containers/">Containers</a> platform, it shares the same underlying platform characteristics. Refer to these pages to understand how pricing and limits work for your sandbox deployments.</p>
<p>Sandbox also inherits current Containers lifecycle, placement, and routing behavior. For more
detail, refer to <a href="/containers/concepts/architecture/">Lifecycle of a Container</a> and
<a href="/containers/configuration/scaling-and-routing/">Scaling and Routing</a>.</p>
<h2 id="container-limits">Container limits</h2>
<p>Refer to <a href="/containers/platform/limits/">Containers limits</a> for complete details on:</p>
<ul>
<li>Memory, vCPU, and disk limits for concurrent container instances</li>
<li>Instance types and their resource allocations</li>
<li>Image size and storage limits</li>
</ul>
<h2 id="workers-and-durable-objects-limits">Workers and Durable Objects limits</h2>
<p>When using the Sandbox SDK from Workers or Durable Objects, you are subject to <a href="/workers/platform/limits/#subrequests">Workers subrequest limits</a>. By default, the SDK uses HTTP transport where each operation (<code>exec()</code>, <code>readFile()</code>, <code>writeFile()</code>, etc.) counts as one subrequest.</p>
<h3 id="subrequest-limits">Subrequest limits</h3>
<ul>
<li><strong>Workers Free</strong>: 50 subrequests per request</li>
<li><strong>Workers Paid</strong>: 1,000 subrequests per request</li>
</ul>
<h3 id="avoid-subrequest-limits-with-rpc-transport">Avoid subrequest limits with RPC transport</h3>
<p>Enable RPC transport to multiplex all SDK calls over a single persistent connection:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13342.md")
</div>
<p>With RPC transport enabled:</p>
<ul>
<li>The persistent connection counts as one subrequest</li>
<li>All subsequent SDK operations use the existing connection (no additional subrequests)</li>
<li>Ideal for workflows with many SDK operations per request</li>
</ul>
<p>See <a href="/sandbox/configuration/transport/">Transport modes</a> for a complete guide.</p>
<h2 id="best-practices">Best practices</h2>
<p>To work within these limits:</p>
<ul>
<li><strong>Right-size your instances</strong> - Choose the appropriate <a href="/containers/platform/limits/#instance-types">instance type</a> based on your workload requirements</li>
<li><strong>Clean up unused sandboxes</strong> - Terminate sandbox sessions when they are no longer needed to free up resources</li>
<li><strong>Optimize images</strong> - Keep your <a href="/sandbox/configuration/dockerfile/">custom Dockerfiles</a> lean to reduce image size</li>
<li><strong>Use RPC transport for high-frequency operations</strong> - Enable <code>SANDBOX_TRANSPORT=rpc</code> to avoid subrequest limits when making many SDK calls per request</li>
</ul>
