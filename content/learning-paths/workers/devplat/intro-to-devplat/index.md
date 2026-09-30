<p>The <a href="https://www.cloudflare.com/developer-platform/products/">Cloudflare Developer Platform</a> offers various services to empower developers to build full-stack applications, including: <a href="https://www.cloudflare.com/developer-platform/products/#compute">compute</a>, <a href="https://www.cloudflare.com/developer-platform/products/#storage">storage</a>, <a href="https://www.cloudflare.com/developer-platform/products/#webdev">web development, image optimization, video streaming</a> and <a href="https://ai.cloudflare.com/">AI</a>.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/FH5-m0aiO5g" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>It is important to note that the developer platform product offering is growing with new releases and features updates. To review a list of product documentation related to Cloudflare Developer Platform:</p>
<ol>
<li>Go to <a href="https://developers.cloudflare.com">Cloudflare Docs</a>.</li>
<li>Select <strong>Product directory</strong> in the top menu.</li>
<li>Select the <strong>Developer platform</strong> filter to view <a href="/directory/?product-group=Developer+platform">product documentation for Cloudflare Developer Platform products</a>.</li>
</ol>
<h2 id="web-development">Web development</h2>
<p><a href="/pages/">Cloudflare Pages</a> allows you to build full-stack applications at scale.</p>
<p>With Pages, you can deploy front-end applications using <a href="/pages/get-started/">C3, Git integration or Direct Upload</a>. Pages supports a large set of frameworks including <a href="/pages/framework-guides/deploy-an-astro-site/">Astro</a>, <a href="/pages/framework-guides/deploy-a-gatsby-site/">Gatsby</a>, <a href="/pages/framework-guides/deploy-a-hugo-site/">Hugo</a>, <a href="/pages/framework-guides/nextjs/">Next.js</a>, <a href="/pages/framework-guides/deploy-a-nuxt-site/">Nuxt</a>, <a href="/pages/framework-guides/deploy-a-react-site/">React</a>, <a href="/pages/framework-guides/deploy-a-remix-site/">Remix</a>, and <a href="/pages/framework-guides/">more</a>.</p>
<h2 id="compute">Compute</h2>
<p><strong>Cloudflare Workers</strong></p>
<p>As you have learned in previous sections, <a href="/workers/">Cloudflare Workers</a> allow you to build and deploy serverless applications instantly across the globe. To explore what you can build with Workers, refer to <a href="/workers/examples/">Examples</a> and <a href="/workers/tutorials/">Tutorials</a>.</p>
<p><strong>Email Routing</strong></p>
<p><a href="/email-service/">Cloudflare Email Routing</a> allows you to create custom email addresses for your domain and route incoming emails to your preferred mailbox. If you already have a website, refer to <a href="/email-service/get-started/route-emails/">Enable Email Routing</a> to set up a custom email address for your site.</p>
<h2 id="storage">Storage</h2>
<p>Cloudflare storage offerings differ per use case.</p>
<table>
<thead>
<tr>
<th>Use-case</th>
<th>Product</th>
<th>Ideal for</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key-value storage</td>
<td><a href="/kv/">Workers KV</a></td>
<td>Configuration data, service routing metadata, personalization (A/B testing)</td>
</tr>
<tr>
<td>Object storage / blob storage</td>
<td><a href="/r2/">R2</a></td>
<td>User-facing web assets, images, machine learning and training datasets, analytics datasets, log and event data.</td>
</tr>
<tr>
<td>Accelerate a Postgres or MySQL database</td>
<td><a href="/hyperdrive/">Hyperdrive</a></td>
<td>Connecting to an existing database in a cloud or on-premise using your existing database drivers &amp; ORMs.</td>
</tr>
<tr>
<td>Global coordination &amp; stateful serverless</td>
<td><a href="/durable-objects/">Durable Objects</a></td>
<td>Building collaborative applications; global coordination across clients; real-time WebSocket applications; strongly consistent, transactional storage.</td>
</tr>
<tr>
<td>Lightweight SQL database</td>
<td><a href="/d1/">D1</a></td>
<td>Relational data, including user profiles, product listings and orders, and/or customer data.</td>
</tr>
<tr>
<td>Task processing, batching and messaging</td>
<td><a href="/queues/">Queues</a></td>
<td>Background job processing (emails, notifications, APIs), message queuing, and deferred tasks.</td>
</tr>
<tr>
<td>Vector search &amp; embeddings queries</td>
<td><a href="/vectorize/">Vectorize</a></td>
<td>Storing <a href="/workers-ai/models/?tasks=Text+Embeddings">embeddings</a> from AI models for semantic search and classification tasks.</td>
</tr>
<tr>
<td>Streaming ingestion</td>
<td><a href="/pipelines/">Pipelines</a></td>
<td>Streaming data ingestion and processing, including clickstream analytics, telemetry/log data, and structured data for querying</td>
</tr>
<tr>
<td>Time-series metrics</td>
<td><a href="/analytics/analytics-engine/">Analytics Engine</a></td>
<td>Write and query high-cardinality time-series data, usage metrics, and service-level telemetry using Workers and/or SQL.</td>
</tr>
</tbody>
</table>
<p>For a detailed guide to choosing the correct storage option, refer to <a href="/workers/platform/storage-options/">Choose a data or storage product</a>.</p>
<h2 id="image-optimization-and-video-streaming">Image optimization and video streaming</h2>
<p><a href="/stream/">Cloudflare Stream</a> and <a href="/images/">Cloudflare Images</a> deliver videos and pictures to your end-users without configuring or maintaining infrastructure.</p>
<h2 id="ai">AI</h2>
<p><a href="/workers-ai/">Workers AI</a> allow you to build and deploy AI applications that run machine learning models powered by serverless GPUs.</p>
<h2 id="summary">Summary</h2>
<p>You have learned:</p>
<ul>
<li>More about what the Cloudflare Developer Platform offers.</li>
<li>The difference between compute, storage, application development, and AI products.</li>
</ul>
<h2 id="feedback">Feedback</h2>
<p>To improve this learning path, <a href="https://github.com/cloudflare/cloudflare-docs/issues/new/choose">file an issue on GitHub</a>.</p>
<h2 id="community">Community</h2>
<p>Connect with the <a href="https://discord.cloudflare.com">Cloudflare Developer Platform community on Discord</a> to ask questions, share what you are building, and discuss the platform with other developers.</p>
