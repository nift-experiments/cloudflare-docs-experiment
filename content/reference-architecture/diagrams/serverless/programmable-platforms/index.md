<h2 id="introduction">Introduction</h2>
<p>A programmable platform allows customers to customize a product by writing code. Unlike traditional SaaS with fixed features, it enables users to extend functionality, deploy backend logic, and build full-stack experiences—all within the platform’s infrastructure.</p>
<p>Hosting the infrastructure for these platforms presents several challenges, including security, scalability, cost efficiency, and performance isolation. Allowing customers to run custom code introduces risks such as untrusted execution, potential abuse, and resource contention, all of which must be managed without compromising platform reliability. Running millions of single-tenant applications is inherently costly, making efficient resource utilization critical. The ability to scale workloads to zero when idle is key to ensuring economic viability while maintaining rapid startup times when demand spikes. Additionally, ensuring seamless global execution with low-latency performance requires a resilient, distributed architecture. Robust monitoring, debugging, and governance capabilities are also essential to provide visibility and control over customer-deployed code without restricting innovation.</p>
<p><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> provides the ideal infrastructure for building programmable platforms by offering secure, isolated environments where customers can safely execute custom code at scale, with automatic scaling to zero and a globally distributed runtime that optimizes performance and cost.</p>
<h2 id="core-architecture-components">Core Architecture Components</h2>
<p>The Workers for Platforms architecture consists of several key components that work together to provide a secure, scalable, and efficient solution for multi-tenant applications. In the following core concepts are outlined.</p>
<ol>
<li>
<p><strong>Main Request Flow</strong>: An overview over the a request flow in a programmable platform.</p>
</li>
<li>
<p><strong>Invocation &amp; Metadata Flow</strong>: commonly, incoming requests and enriched with metadata to provide the function invocation with relevant context or perform routing logic.</p>
</li>
<li>
<p><strong>Egress Control</strong>: controlling outbound connections to ensure compliant behaviour.</p>
</li>
<li>
<p><strong>Utilizing Storage &amp; Data Resources</strong>: leveraging databases &amp; storage to build even richer end-user experiences at scale.</p>
</li>
<li>
<p><strong>Observability Tools</strong>: Logging and metrics collection services to monitor platform performance and troubleshoot issues.</p>
</li>
</ol>
<h2 id="main-request-flow">Main Request Flow</h2>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-1.svg" alt="Figure 1: Workers for Platforms: Main Flow" title="Figure 1: Workers for Platforms: Main Flow" /></p>
<ol>
<li>
<p><strong>Client Request</strong>: Send request from a client application to the platform's <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">Dynamic Dispatch Worker</a>.</p>
</li>
<li>
<p><strong>Routing</strong>: Identify the correct workload to execute and route the request to the respective <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">User Worker</a> in the <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace">Dispatch Namespace</a>. Each customer's workload runs in an isolated User Worker with its own resources and security boundaries.</p>
</li>
</ol>
<h2 id="invocation-metadata-flow">Invocation &amp; Metadata Flow</h2>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-2.svg" alt="Figure 2: Workers for Platforms: Main Flow" title="Figure 2: Workers for Platforms: Main Flow" /></p>
<p>For many use cases, it makes sense to retrieve additional metadata, user data, or configuration to process incoming requests and provide the User Worker invocation with additional context.</p>
<ol>
<li>
<p><strong>Incoming Request</strong>: Send requests to custom hostnames or a Worker using a Workers wildcard route.</p>
</li>
<li>
<p><strong>Metadata Lookup</strong>: Retrieve customer-specific configuration data from <a href="/kv/">KV</a> storage. These lookups are typically based on the hostname of the incoming request or custom metadata in the case of custom hostnames.</p>
</li>
<li>
<p><strong>Worker Invocation</strong>: Route requests to the appropriate User Worker in the Dispatch Namespace based on metadata. Optionally, provide additional context during function invocation.</p>
</li>
</ol>
<h2 id="egress-control-pattern">Egress Control Pattern</h2>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-3.svg" alt="Figure 3: Workers for Platforms: Egress Control" title="Figure 3: Workers for Platforms: Egress Control" /></p>
<p>Data observability and control is crucial for security. <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">Outbound Workers</a> allow for interception of all outgoing requests in User Worker scripts.</p>
<ol>
<li>
<p><strong>Worker Invocation</strong>: Route requests to the appropriate User Worker in the Dispatch Namespace. Optionally pass additional parameters to the Outbound Worker during User Worker invocation.</p>
</li>
<li>
<p><strong>External requests</strong>: Send requests via <code>fetch()</code> calls to external services through a controlled Outbound Worker.</p>
</li>
<li>
<p><strong>Request interception</strong>: Evaluate outgoing requests and perform core functions like centralized policy enforcement and audit logging.</p>
</li>
</ol>
<h2 id="metrics-logging-architecture">Metrics &amp; Logging Architecture</h2>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-4.svg" alt="Figure 4: Workers for Platforms: Metrics &amp; Logging" title="Figure 4: Workers for Platforms: Metrics &amp; Logging" /></p>
<ol>
<li>
<p><strong>Logging</strong>: Collect logs throughout all Workers in the request flow via <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/observability/#tail-workers">Tail Worker</a> and <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/observability/#workers-trace-events-logpush">Workers Trace Events Logpush</a> services.</p>
</li>
<li>
<p><strong>Metrics</strong>: Collect custom metrics via <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> and out-of-the-box <a href="/analytics/graphql-api/">Analytics</a> that can readily be queried via GraphQL API.</p>
</li>
<li>
<p><strong>Third-party Integration</strong>: Export logs and metrics to various external monitoring and analytics platforms like Datadog, Splunk, Grafana, and others via <a href="/analytics/analytics-integrations/">Analytics integrations</a>.</p>
</li>
</ol>
<h2 id="resource-isolation-model">Resource Isolation Model</h2>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-5.svg" alt="Figure 5: Workers for Platforms: Resources" title="Figure 5: Workers for Platforms: Resources" /></p>
<ol>
<li>
<p><strong>Incoming Request</strong>: Send requests to custom hostnames or a Worker using a Workers wildcard route.</p>
</li>
<li>
<p><strong>Worker Invocation</strong>: Route requests to the appropriate User Worker in the Dispatch Namespace.</p>
</li>
<li>
<p><strong>Resource Access</strong>: Interact with per-script-specific resources:</p>
<ul>
<li>D1 for relational database storage</li>
<li>Durable Objects for strongly consistent data</li>
<li>KV for high-read, eventually consistent key-value storage</li>
<li>R2 for object storage</li>
</ul>
</li>
</ol>
<h2 id="deployment-management-flow">Deployment &amp; Management Flow</h2>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-6.svg" alt="Figure 6: Workers for Platforms: Deployment &amp; Management Flow" title="Figure 6: Workers for Platforms: Deployment &amp; Management Flow" /></p>
<ol>
<li>
<p><strong>Management Interface</strong>: Interact with the platform through GUI, API, or CLI interfaces.</p>
</li>
<li>
<p><strong>Platform Processing</strong>: Process these interactions to:</p>
<ul>
<li>Transform and bundle code</li>
<li>Perform security checks</li>
<li>Apply configuration</li>
</ul>
</li>
<li>
<p><strong>Change Management</strong>: Deploy changes to Cloudflare using the Cloudflare REST API.</p>
</li>
</ol>
<h2 id="conclusion">Conclusion</h2>
<p>Cloudflare Workers for Platforms provides a robust foundation for building multi-tenant SaaS applications with strong isolation, global distribution, and scalable performance. By leveraging this architecture, platform providers can focus on delivering value to their customers while Cloudflare handles the underlying infrastructure complexity.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/get-started/">Workers for Platforms: Get started</a></li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">Workers for Platforms: Outbound Workers</a></li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/observability/">Workers for Platforms: Observability</a></li>
</ul>
