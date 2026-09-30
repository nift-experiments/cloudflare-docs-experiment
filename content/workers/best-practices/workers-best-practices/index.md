---
cp9:
  canonical: https://developers.cloudflare.com/workers/best-practices/workers-best-practices/
  description: Code patterns and configuration guidance for building fast, reliable, observable, and secure Workers.
  full_title: Workers Best Practices · Cloudflare Workers docs
  head_html: <title>Workers Best Practices · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Code patterns and configuration guidance for building fast, reliable, observable, and secure Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/best-practices/workers-best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/best-practices/workers-best-practices/index.md"><meta property="og:title" content="Workers Best Practices · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Code patterns and configuration guidance for building fast, reliable, observable, and secure Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/best-practices/workers-best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/best-practices/workers-best-practices/#page","headline":"Workers Best Practices \u00b7 Cloudflare Workers docs","description":"Code patterns and configuration guidance for building fast, reliable, observable, and secure Workers.","url":"https://developers.cloudflare.com/workers/best-practices/workers-best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/best-practices/workers-best-practices/
  schema: 1
---
<p>Best practices for Workers based on production patterns, Cloudflare's own internal usage, and common issues seen across the developer community.</p>
<h2 id="configuration">Configuration</h2>
<h3 id="keep-your-compatibility-date-current">Keep your compatibility date current</h3>
<p>The <a href="/workers/configuration/compatibility-dates/"><code>compatibility_date</code></a> controls which runtime features and bug fixes are available to your Worker. Setting it to today's date on new projects ensures you get the latest behavior. Periodically updating it on existing projects gives you access to new APIs and fixes without changing your code.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16738.md")
</div>
<p>For more information, refer to <a href="/workers/configuration/compatibility-dates/">Compatibility dates</a>.</p>
<h3 id="enable-nodejs-compat">Enable nodejs_compat</h3>
<p>The <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag gives your Worker access to Node.js built-in modules like <code>node:crypto</code>, <code>node:buffer</code>, <code>node:stream</code>, and others. Many libraries depend on these modules, and enabling this flag avoids cryptic import errors at runtime.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16739.md")
</div>
<p>For more information, refer to <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a>.</p>
<h3 id="generate-binding-types-with-wrangler-types">Generate binding types with wrangler types</h3>
<p>Do not hand-write your <code>Env</code> interface. Run <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a> to generate a type definition file that matches your actual Wrangler configuration. This catches mismatches between your config and code at compile time instead of at deploy time.</p>
<p>Re-run <code>wrangler types</code> whenever you add or rename a binding.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16740.md")
</div>
<p>For more information, refer to <a href="/workers/wrangler/commands/general/#types">wrangler types</a>.</p>
<h3 id="store-secrets-with-wrangler-secret-not-in-source">Store secrets with wrangler secret, not in source</h3>
<p>Secrets (API keys, tokens, database credentials) must never appear in your Wrangler configuration or source code. Use <a href="/workers/configuration/secrets/"><code>wrangler secret put</code></a> to store them securely, and access them through <code>env</code> at runtime. For local development, use a <code>.env</code> file (and make sure it is in your <code>.gitignore</code>). For more information, refer to <a href="/workers/configuration/environment-variables/">Environment variables</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16741.md")
</div>
<p>To add a secret, run the following command and provide the secret interactively when prompted:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler secret put API_KEY</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler secret put API_KEY" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler secret put API_KEY</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler secret put API_KEY" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler secret put API_KEY</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler secret put API_KEY" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You can also pipe secrets from other tools or environment variables:</p>
<pre tabindex="0"><code class="language-bash">&#35; Pipe from another CLI tool&#10;npx some-cli-tool --get-secret | npx wrangler secret put API_KEY&#10;&#35; Pipe from an environment variable or .env file&#10;echo &quot;$API_KEY&quot; | npx wrangler secret put API_KEY&#10;</code></pre>
<p>For more information, refer to <a href="/workers/configuration/secrets/">Secrets</a>.</p>
<h3 id="configure-environments-deliberately">Configure environments deliberately</h3>
<p><a href="/workers/wrangler/environments/">Wrangler environments</a> let you deploy the same code to separate Workers for production, staging, and development. Each environment creates a distinct Worker named <code>{name}-{env}</code> (for example, <code>my-api-production</code> and <code>my-api-staging</code>).</p>
<p>Each environment is treated separately. Bindings and vars need to be declared per environment and are not inherited. Refer to <a href="/workers/wrangler/configuration/#non-inheritable-keys">non-inheritable keys</a>. The root Worker (without an environment suffix) is a separate deployment. If you do not intend to use it, do not deploy without specifying an environment using <code>--env</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16742.md")
</div>
<p>With this configuration file, to deploy to staging:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler deploy --env staging</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy --env staging" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler deploy --env staging</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy --env staging" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler deploy --env staging</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy --env staging" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For more information, refer to <a href="/workers/wrangler/environments/">Environments</a>.</p>
<h3 id="set-up-custom-domains-or-routes-correctly">Set up custom domains or routes correctly</h3>
<p>Workers support two routing mechanisms, and they serve different purposes:</p>
<ul>
<li><strong><a href="/workers/configuration/routing/custom-domains/">Custom domains</a></strong>: The Worker <strong>is</strong> the origin. Cloudflare creates DNS records and SSL certificates automatically. Use this when your Worker handles all traffic for a hostname.</li>
<li><strong><a href="/workers/configuration/routing/routes/">Routes</a></strong>: The Worker runs <strong>in front of</strong> an existing origin server. You must have a Cloudflare proxied (orange-clouded) DNS record for the hostname before adding a route.</li>
</ul>
<p>The most common mistake with routes is missing the DNS record. Without a proxied DNS record, requests to the hostname return <code>ERR_NAME_NOT_RESOLVED</code> and never reach your Worker. If you do not have a real origin, add a proxied <code>AAAA</code> record pointing to <code>100::</code> as a placeholder.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16743.md")
</div>
<p>For more information, refer to <a href="/workers/configuration/routing/">Routing</a>.</p>
<h2 id="request-and-response-handling">Request and response handling</h2>
<h3 id="stream-request-and-response-bodies">Stream request and response bodies</h3>
<p>Regardless of memory limits, streaming large requests and responses is a best practice in any language. It reduces peak memory usage and improves time-to-first-byte. Workers have a <a href="/workers/platform/limits/">128 MB memory limit</a>, so buffering an entire body with <code>await response.text()</code> or <code>await request.arrayBuffer()</code> will crash your Worker on large payloads.</p>
<p>For request bodies you do consume entirely (JSON payloads, file uploads), enforce a maximum size before reading. This prevents clients from sending data you do not want to process.</p>
<p>Stream data through your Worker using <code>TransformStream</code> to pipe from a source to a destination without holding it all in memory.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16744.md")
</div>
<p>When you need to concatenate multiple responses (for example, fetching data from several upstream APIs), pipe each body sequentially into a single writable stream. This avoids buffering any of the responses in memory.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16745.md")
</div>
<p>For more information, refer to <a href="/workers/runtime-apis/streams/">Streams</a>.</p>
<h3 id="use-waituntil-for-work-after-the-response">Use waitUntil for work after the response</h3>
<p><a href="/workers/runtime-apis/context/"><code>ctx.waitUntil()</code></a> lets you perform work after the response is sent to the client, such as analytics, cache writes, logging, or webhook notifications. This keeps your response fast while still completing background tasks.</p>
<p>Use <code>ctx.waitUntil()</code> only for work that does not affect the response. If the response depends on the work, <code>await</code> it before returning the response or stream the response as the work completes. A Worker that is still streaming a response body remains active without <code>ctx.waitUntil()</code>.</p>
<p>There are two common pitfalls: destructuring <code>ctx</code> (which loses the <code>this</code> binding and throws &quot;Illegal invocation&quot;), and exceeding the 30-second <code>waitUntil()</code> time limit after the response is sent or the client disconnects.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16746.md")
</div>
<p>For more information, refer to <a href="/workers/runtime-apis/context/">Context</a>.</p>
<h2 id="architecture">Architecture</h2>
<h3 id="use-bindings-for-cloudflare-services-not-rest-apis">Use bindings for Cloudflare services, not REST APIs</h3>
<p>Some Cloudflare services like R2, KV, D1, Queues, and Workflows are available as <a href="/workers/runtime-apis/bindings/">bindings</a>. Bindings are direct, in-process references that require no network hop, no authentication, and no extra latency. Using the REST API from within a Worker wastes time and adds unnecessary complexity.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16747.md")
</div>
<h3 id="use-queues-and-workflows-for-async-and-background-work">Use Queues and Workflows for async and background work</h3>
<p>Long-running, retryable, or non-urgent tasks should not block a request. Use <a href="/queues/">Queues</a> and <a href="/workflows/">Workflows</a> to move work out of the critical path. They serve different purposes:</p>
<p><strong>Use Queues when</strong> you need to decouple a producer from a consumer. Queues are a message broker: one Worker sends a message, another Worker processes it later. They are the right choice for fan-out (one event triggers many consumers), buffering and batching (aggregate messages before writing to a downstream service), and simple single-step background jobs (send an email, fire a webhook, write a log). Queues provide at-least-once delivery with configurable retries per message.</p>
<p><strong>Use Workflows when</strong> the background work has multiple steps that depend on each other. Workflows are a durable execution engine: each step's return value is persisted, and if a step fails, only that step is retried — not the entire job. They are the right choice for multi-step processes (charge a card, then create a shipment, then send a confirmation), long-running tasks that need to pause and resume (wait hours or days for an external event or human approval via <code>step.waitForEvent()</code>), and complex conditional logic where later steps depend on earlier results. Workflows can run for hours, days, or weeks.</p>
<p><strong>Use both together</strong> when a high-throughput entry point feeds into complex processing. For example, a Queue can buffer incoming orders, and the consumer can create a Workflow instance for each order that requires multi-step fulfillment.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16748.md")
</div>
<p>For more information, refer to <a href="/queues/">Queues</a> and <a href="/workflows/">Workflows</a>.</p>
<h3 id="use-service-bindings-for-worker-to-worker-communication">Use service bindings for Worker-to-Worker communication</h3>
<p>When one Worker needs to call another, use <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a> instead of making an HTTP request to a public URL. Service bindings are zero-cost, bypass the public internet, and support type-safe RPC.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16749.md")
</div>
<h3 id="use-hyperdrive-for-external-database-connections">Use Hyperdrive for external database connections</h3>
<p>Always use <a href="/hyperdrive/">Hyperdrive</a> when connecting to a remote PostgreSQL or MySQL database from a Worker. Hyperdrive maintains a regional connection pool close to your database, eliminating the per-request cost of TCP handshake, TLS negotiation, and connection setup. It also caches query results where possible.</p>
<p>Create a new <code>Client</code> on each request. Hyperdrive manages the underlying pool, so client creation is fast. Requires <code>nodejs_compat</code> for database driver support.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16750.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16751.md")
</div>
<p>For more information, refer to <a href="/hyperdrive/">Hyperdrive</a>.</p>
<h3 id="use-durable-objects-for-websockets">Use Durable Objects for WebSockets</h3>
<p>Plain Workers can upgrade HTTP connections to WebSockets, but they lack persistent state and hibernation. If the isolate is evicted, the connection is lost because there is no persistent actor to hold it. For reliable, long-lived WebSocket connections, use <a href="/durable-objects/">Durable Objects</a> with the <a href="/durable-objects/best-practices/websockets/">Hibernation API</a>. Durable Objects keep WebSocket connections open even while the object is evicted from memory, and automatically wake up when a message arrives.</p>
<p>Use <code>this.ctx.acceptWebSocket()</code> instead of <code>ws.accept()</code> to enable hibernation. Use <code>setWebSocketAutoResponse</code> for ping/pong heartbeats that do not wake the object.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16752.md")
</div>
<p>For more information, refer to <a href="/durable-objects/best-practices/websockets/">Durable Objects WebSocket best practices</a>.</p>
<h3 id="use-workers-static-assets-for-new-projects">Use Workers Static Assets for new projects</h3>
<p><a href="/workers/static-assets/">Workers Static Assets</a> is the recommended way to deploy static sites, single-page applications, and full-stack apps on Cloudflare. If you are starting a new project, use Workers instead of Pages. Pages continues to work, but new features and optimizations are focused on Workers.</p>
<p>For a purely static site, point <code>assets.directory</code> at your build output. No Worker script is needed. For a full-stack app, add a <code>main</code> entry point and an <code>ASSETS</code> binding to serve static files alongside your API.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16753.md")
</div>
<p>For more information, refer to <a href="/workers/static-assets/">Workers Static Assets</a>.</p>
<h2 id="observability">Observability</h2>
<h3 id="enable-workers-logs-and-traces">Enable Workers Logs and Traces</h3>
<p>Production Workers without observability are a black box. Enable logs and traces before you deploy to production. When an intermittent error appears, you need data already being collected to diagnose it.</p>
<p>Enable them in your Wrangler configuration and use <code>head_sampling_rate</code> to control volume and manage costs. A sampling rate of <code>1</code> captures everything; lower it for high-traffic Workers.</p>
<p>Use structured JSON logging with <code>console.log</code> so logs are searchable and filterable. Use <code>console.error</code> for errors and <code>console.warn</code> for warnings. These appear at the correct severity level in the Workers Observability dashboard.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16754.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16755.md")
</div>
<p>For more information, refer to <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> and <a href="/workers/observability/traces/">Traces</a>.</p>
<p>For more information on all available observability tools, refer to <a href="/workers/observability/">Workers Observability</a>.</p>
<h2 id="code-patterns">Code patterns</h2>
<h3 id="do-not-store-request-scoped-state-in-global-scope">Do not store request-scoped state in global scope</h3>
<p>Workers reuse isolates across requests. A variable set during one request is still present during the next. This causes cross-request data leaks, stale state, and &quot;Cannot perform I/O on behalf of a different request&quot; errors.</p>
<p>Pass state through function arguments or store it on <code>env</code> bindings. Never in module-level variables.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16756.md")
</div>
<p>For more information, refer to <a href="/workers/observability/errors/#cannot-perform-io-on-behalf-of-a-different-request">Workers errors</a>.</p>
<h3 id="always-await-or-waituntil-your-promises">Always await or waitUntil your Promises</h3>
<p>A <code>Promise</code> that is not <code>await</code>ed, <code>return</code>ed, or passed to <code>ctx.waitUntil()</code> is a floating promise. Floating promises cause silent bugs: dropped results, swallowed errors, and unfinished work. The Workers runtime may terminate your isolate before a floating promise completes.</p>
<p>Choose based on whether the response depends on the work. Use <code>await</code> or <code>return</code> for work that must complete before the response is correct. Use <code>ctx.waitUntil()</code> for work that can run after the response is sent and can finish within the <code>waitUntil()</code> time limit.</p>
<p>Enable the <code>no-floating-promises</code> lint rule to catch these at development time. If you use ESLint, enable <a href="https://typescript-eslint.io/rules/no-floating-promises/"><code>@typescript-eslint/no-floating-promises</code></a>. If you use oxlint, enable <a href="https://oxc.rs/docs/guide/usage/linter/rules/typescript/no-floating-promises.html"><code>typescript/no-floating-promises</code></a>.</p>
<pre tabindex="0"><code class="language-bash">&#35; ESLint (typescript-eslint)&#10;npx eslint --rule &#x27;{&quot;@typescript-eslint/no-floating-promises&quot;: &quot;error&quot;}&#x27; src/&#10;&#10;&#35; oxlint&#10;npx oxlint --deny typescript/no-floating-promises src/&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16757.md")
</div>
<h2 id="security">Security</h2>
<h3 id="use-web-crypto-for-secure-token-generation">Use Web Crypto for secure token generation</h3>
<p>The Workers runtime provides the <a href="/workers/runtime-apis/web-crypto/">Web Crypto API</a> for cryptographic operations. Use <code>crypto.randomUUID()</code> for unique identifiers and <code>crypto.getRandomValues()</code> for random bytes. Never use <code>Math.random()</code> for anything security-sensitive. It is not cryptographically secure.</p>
<p>Node.js <a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code></a> is also fully supported when <code>nodejs_compat</code> is enabled, so you can use whichever API you or your libraries prefer.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16758.md")
</div>
<p>When comparing secret values (API keys, tokens, HMAC signatures), use <code>crypto.subtle.timingSafeEqual()</code> to prevent timing side-channel attacks. Do not short-circuit on length mismatch. Encode both values to a fixed-size hash first.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16759.md")
</div>
<h3 id="do-not-use-passthroughonexception-as-error-handling">Do not use passThroughOnException as error handling</h3>
<p><code>passThroughOnException()</code> is a fail-open mechanism that sends requests to your origin when your Worker throws an unhandled exception. While it can be useful during migration from an origin server, it hides bugs and makes debugging difficult. Use explicit <code>try...catch</code> blocks with structured error responses instead.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16760.md")
</div>
<h2 id="development-and-testing">Development and testing</h2>
<h3 id="test-with-cloudflare-vitest-plugin">Test with @cloudflare/vitest-plugin</h3>
<p>The <a href="/workers/testing/vitest-integration/"><code>@cloudflare/vitest-plugin</code></a> package runs your tests inside the Workers runtime, giving you access to real bindings (KV, R2, D1, Durable Objects) during tests. This catches issues that Node.js-based tests miss, like unsupported APIs or missing compatibility flags.</p>
<p>One known pitfall: the Vitest plugin automatically injects <code>nodejs_compat</code>, so tests pass even if your Wrangler configuration does not have the flag. Always confirm your <code>wrangler.jsonc</code> includes <code>nodejs_compat</code> if your code depends on Node.js built-in modules.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16761.md")
</div>
<p>For more information, refer to <a href="/workers/testing/vitest-integration/">Testing with Vitest</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/durable-objects/best-practices/rules-of-durable-objects/">Rules of Durable Objects</a>: best practices for stateful, coordinated applications.</li>
<li><a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a>: best practices for durable, multi-step Workflows.</li>
<li><a href="/workers/platform/limits/">Platform limits</a>: CPU time, memory, subrequest, and other limits.</li>
<li><a href="/workers/observability/errors/">Workers errors</a>: error codes and debugging guidance.</li>
</ul>
