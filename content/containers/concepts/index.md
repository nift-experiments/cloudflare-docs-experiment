<p>A Cloudflare Container runs your container image in a full Linux environment on Cloudflare's network, alongside a Worker. The Worker handles incoming HTTP requests, while the Container provides the runtime, binaries, and languages your application needs. Together, they let you run Linux workloads without managing the underlying infrastructure.</p>
<h2 id="the-container-runtime">The Container runtime</h2>
<p><em>Run Linux workloads alongside your Worker.</em></p>
<p>A Worker runs code in an isolated JavaScript environment. A Container runs your image in a full Linux environment, so you can bring custom runtimes and binaries when your application needs them. Each Container instance runs inside its own virtual machine, which isolates it from other workloads. The Worker receives inbound HTTP requests and routes them to the Container, so the Container is not exposed directly to end users.</p>
<div class="nb-interactive-component" data-cf-component="ContainerIsolation">
@markup("md", "content/.markup/bodies/7153.md")
</div>
<p>For more information, refer to <a href="/containers/concepts/architecture/">Lifecycle of a Container</a>.</p>
<h2 id="how-requests-reach-a-container">How requests reach a Container</h2>
<p><em>Route every request through your Worker.</em></p>
<p>The request begins at your Worker, which uses the <a href="/durable-objects/">Durable Object</a> layer to identify and reach a Container. This layer coordinates routing and lifecycle behavior, allowing the Container to continue serving requests while it runs. A Container can start when it receives its first request, so the first request may take longer to complete.</p>
<div class="nb-interactive-component" data-cf-component="ContainerRequestPath">
@markup("md", "content/.markup/bodies/7154.md")
</div>
<p>For more information, refer to <a href="/containers/concepts/architecture/">Lifecycle of a Container</a>.</p>
<h2 id="container-lifecycle">Container lifecycle</h2>
<p><em>Start on demand, then stop when idle.</em></p>
<p>A Container starts when your application needs it, so the first request can take longer while its environment starts. Once running, it serves requests until it becomes inactive; after an inactivity period, it can stop and release its running resources. When another request arrives, the Container can start again.</p>
<div class="nb-interactive-component" data-cf-component="ContainerLifecycle">
@markup("md", "content/.markup/bodies/7155.md")
</div>
<p>For more information, refer to <a href="/containers/concepts/architecture/">Lifecycle of a Container</a> and <a href="/containers/platform/pricing/">Pricing</a>.</p>
<h2 id="sizing">Sizing</h2>
<p><em>Choose resources for your workload.</em></p>
<p>Container instance sizes let you match resources to your workload. You can choose a predefined size or configure a custom one, with larger sizes providing more CPU, memory, and disk. When choosing a size, consider the resources your application needs and refer to <a href="/containers/platform/limits/">Limits and instance types</a> for the available options and constraints.</p>
<p>For more information, refer to <a href="/containers/platform/pricing/">Pricing</a>.</p>
<h2 id="placement">Placement</h2>
<p><em>Place instances near users or within constraints.</em></p>
<p>Cloudflare places Container instances across its network, helping applications serve users from suitable locations. You can constrain placement by region or jurisdiction when your workload has location or data residency requirements. You can also run multiple instances when your application needs more capacity.</p>
<div class="nb-interactive-component" data-cf-component="ContainerPlacement">
@markup("md", "content/.markup/bodies/7156.md")
</div>
<p>For more information, refer to <a href="/containers/concepts/placement/">Placement</a>.</p>
<h2 id="storage-and-connectivity">Storage and connectivity</h2>
<p><em>Keep durable data outside the local disk.</em></p>
<p>Treat a Container's local disk as temporary working space, because data on it can be lost when the Container stops or restarts. For data that must persist, use Durable Object storage or Cloudflare storage bindings such as KV, R2, and D1. Configured outbound handlers let the Container access these bindings and external services without requiring an SDK inside the Container.</p>
<div class="nb-interactive-component" data-cf-component="ContainerConnectivity">
@markup("md", "content/.markup/bodies/7157.md")
</div>
<p>For more information, refer to <a href="/containers/configuration/workers-connections/">Connect to Workers and bindings</a> and <a href="/containers/guides/outbound-traffic/">Outbound traffic</a>.</p>
<h2 id="start-building">Start building</h2>
<p>When you are ready to build, start with a deployed Container or explore the available guides.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/7158.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/containers/concepts/architecture/">Lifecycle of a Container</a>: the deep dive on deployment, routing, and shutdown.</li>
<li><a href="/containers/concepts/placement/">Placement</a>: where instances run and how to constrain them.</li>
<li><a href="/containers/configuration/workers-connections/">Connect to Workers and bindings</a>: reaching Cloudflare resources from a container.</li>
<li><a href="/containers/platform/limits/">Limits and instance types</a> and <a href="/containers/platform/pricing/">Pricing</a>: sizes, account limits, and billing.</li>
<li><a href="/containers/configuration/rollouts/">Rollouts</a>: how new versions roll out across instances.</li>
</ul>
