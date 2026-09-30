<p>Multi-tenant platforms need to store customer data with appropriate isolation — per-tenant databases, separate object storage, or row-level separation. Cloudflare provides serverless storage options that support tenant isolation at the database, bucket, or key-prefix level.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="d1">D1</h3>
<p>Serverless SQL database built on SQLite, with global read replication. <a href="/d1/">Learn more about D1</a>.</p>
<ul>
<li><strong>Database per tenant</strong> - Create isolated D1 databases per customer for complete data separation, or use row-level isolation in a shared database</li>
</ul>
<h3 id="r2">R2</h3>
<p>S3-compatible object storage with zero egress fees. <a href="/r2/">Learn more about R2</a>.</p>
<ul>
<li><strong>Object storage</strong> - Store customer files and assets per tenant using prefix or bucket-level isolation, with no egress fees</li>
</ul>
<h3 id="durable-objects">Durable Objects</h3>
<p>Stateful objects with strongly consistent storage and coordination. <a href="/durable-objects/">Learn more about Durable Objects</a>.</p>
<ul>
<li><strong>Real-time coordination</strong> - Manage stateful workflows and provide strong consistency for multi-tenant operations</li>
</ul>
<h3 id="kv">KV</h3>
<p>Globally distributed key-value storage for low-latency reads. <a href="/kv/">Learn more about KV</a>.</p>
<ul>
<li><strong>Edge configuration</strong> - Store per-tenant settings, feature flags, and session data at the edge for low-latency reads</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/d1/get-started/">D1 get started</a></li>
<li><a href="/r2/get-started/">R2 get started</a></li>
<li><a href="/durable-objects/get-started/">Durable Objects get started</a></li>
</ol>
