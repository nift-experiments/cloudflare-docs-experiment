<h2 id="introduction">Introduction</h2>
<p>Serverless APIs represent a modern approach to building and deploying scalable and reliable application programming interfaces (APIs) without the need to manage traditional server infrastructure. These APIs are designed to handle incoming requests from users or other systems, execute the necessary logic or operations, and return a response, all without the need for developers to provision or manage underlying servers.</p>
<p>At the heart of serverless APIs is the concept of serverless computing, where developers focus solely on writing code to implement business logic, without concerning themselves with server provisioning, scaling, or maintenance. This allows for greater agility and faster time-to-market for API-based applications.</p>
<p>Developers define the API endpoints and the corresponding logic or functionality using functions or microservices, which are then deployed to the serverless platform. The platform handles the execution of these functions in response to incoming requests.</p>
<p>Additionally, serverless APIs often integrate seamlessly with other cloud services, such as authentication and authorization services, databases, and event-driven architectures, enabling developers to build complex, scalable, and resilient applications with minimal operational overhead.</p>
<p>Most cloud serverless implementations have a single region where your code is executed. This means any request, from anywhere in the world, must traverse the Internet to get to this single location. All responses to the API request must also be sent back over the same Internet route to the user.</p>
<p><img src="/assets/upstream/images/reference-architecture/serverless-global-apis/single-region.png" alt="Figure 1: Traditional single-region architecture" title="Figure 1:  Traditional single-region architecture" /></p>
<p>Cloudflare follows a different, global-first approach. Globally-deployed architectures enable lower latency and high availability for users accessing the API from different parts of the world. In order to realize performance gains, not only the compute needs to be distributed, but ideally the data as well. Different solutions such as a caching as well as global replication can enable this.</p>
<p><img src="/assets/upstream/images/reference-architecture/serverless-global-apis/region-earth.png" alt="Figure 2: Region Earth" title="Figure 2:  Region Earth" /></p>
<p>Overall, serverless globally-deployed APIs offer a cost-effective, scalable, and agile approach to building modern applications and services, allowing organizations to focus on delivering value to their users without being encumbered by the complexities of managing infrastructure.</p>
<h2 id="serverless-global-apis">Serverless global APIs</h2>
<p><img src="/assets/upstream/images/reference-architecture/serverless-global-apis/serverless-global-apis.svg" alt="Figure 3: Serverless global APIs" title="Figure 3: Serverless global APIs" /></p>
<p>This is an example architecture of a serverless API on Cloudflare and aims to illustrate how different compute and data products could interact with each other.</p>
<ol>
<li><strong>Client request</strong>: Send request to API endpoint.</li>
<li><strong>API Shield/Router</strong>: Process incoming request using <a href="/workers/">Workers</a>, check for validity, and perform authentication logic, if needed. Then, forward the (potentially transformed and/or enriched) API call to individual <a href="/workers">Workers</a> using <a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a>. This allows for a separation of concerns.</li>
<li><strong>Read-heavy data</strong>: Read from <a href="/kv/">KV</a> to serve read-heavy, non-dynamic data. This could include configuration data or product information. Perform writes as needed keeping <a href="/kv/platform/limits/">limits</a> in mind.</li>
<li><strong>Relational data</strong>: Query <a href="/d1/">D1</a> to handle relational-data. This could include user data, product data or other data.</li>
<li><strong>External data</strong>: Query external databases using <a href="/hyperdrive/">Hyperdrive</a>. Leverage caching to improve performance where applicable. This can be especially helpful when a data migration is out of scope of the implementation.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/get-started/guide/">Workers: Get started</a></li>
<li><a href="/queues/get-started/">Queues: Get started</a></li>
<li><a href="/r2/get-started/">R2: Get started</a></li>
</ul>
