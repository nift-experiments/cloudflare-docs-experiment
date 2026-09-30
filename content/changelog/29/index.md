<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-12-18">Dec 18, 2025</time><div>
<h2 id="post-2025-12-18-waf-release"><a href="/changelog/post/2025-12-18-waf-release/">WAF Release - 2025-12-18</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6429f7386b1546cf9dfce631be5ec20c">be5ec20c</code>
</td>
<td>N/A</td>
<td>Atlassian Confluence - Code Injection - CVE:CVE-2021-26084 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Atlassian Confluence - Code Injection - CVE:CVE-2021-26084" (ID: <code class="nb-rule-id" title="e8c550810618437c953cf3a969e0b97a">69e0b97a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9108ddb347b3497e9f9351640d9206e3">0d9206e3</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - Copy - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "PostgreSQL - SQLi - COPY" (ID: <code class="nb-rule-id" title="705a6b5569d5472596910e3ce7265a4e">e7265a4e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cb687d73cc954092b58b90b00cd00ba7">0cd00ba7</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Body</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="bf30657ffa2a424cbf6570dbcd679ad4">cd679ad4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Header</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6df040f716194070a242967cfd181fb3">fd181fb3</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="39a4fdc37be948709fa7492e7a95bc3a">7a95bc3a</code>
</td>
<td>N/A</td>
<td>SQLi - Tautology - URI - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Tautology - URI" (ID: <code class="nb-rule-id" title="4c580ea1b5174183b7f5e940b3de2e0a">b3de2e0a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="810e0ffe1dd84e67b159129b432ac90d">432ac90d</code>
</td>
<td>N/A</td>
<td>SQLi - WaitFor Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - WaitFor Function" (ID: <code class="nb-rule-id" title="b16fe708799441dea3049a99d5faba59">d5faba59</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="80690005fef342e0ad6bc9af596c741e">596c741e</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - AND/OR Digit Operator Digit" (ID: <code class="nb-rule-id" title="98e7e08ae64247e2801ca4b388d80772">88d80772</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="eaf11ab80b0d491cbb7186f303b2f3fe">03b2f3fe</code>
</td>
<td>N/A</td>
<td>SQLi - Equation 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Equation" (ID: <code class="nb-rule-id" title="133c6f83cdf14509a4ca6b82a72a6b3a">a72a6b3a</code>)</td>
</tr>
</tbody>    
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-18">Dec 18, 2025</time><div>
<h2 id="post-2025-12-01-build-image-policies-dev-plat"><a href="/changelog/post/2025-12-01-build-image-policies-dev-plat/">Build image policies for Workers Builds and Cloudflare Pages</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've published build image policies for <a href="/workers/ci-cd/builds/build-image/#build-image-policy">Workers Builds</a> and <a href="/pages/configuration/build-image/#build-image-policy">Cloudflare Pages</a>, which establish:</p>
<ul>
<li><strong>Minor version updates</strong>: We typically update preinstalled software to the latest available minor version without notice. For tools that don't follow semantic versioning (e.g., Bun or Hugo), we provide 3 months’ notice.</li>
<li><strong>Major version updates</strong>: Before preinstalled software reaches end-of-life, we update to the next stable LTS version with 3 months’ notice.</li>
<li><strong>Build image version deprecation (Pages only)</strong>: We provide 6 months’ notice before deprecation. Projects on v1 or v2 will be automatically moved to v3 on their specified deprecation dates.</li>
</ul>
<p>To prepare for updates, monitor the <a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a>, dashboard notifications, and email. You can also <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">override default versions</a> to maintain specific versions.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-18">Dec 18, 2025</time><div>
<h2 id="post-2025-12-18-wrangler-auth-token"><a href="/changelog/post/2025-12-18-wrangler-auth-token/">Retrieve your authentication token with `wrangler auth token`</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now includes a new <a href="/workers/wrangler/commands/general/#auth-token"><code>wrangler auth token</code></a> command that retrieves your current authentication token or credentials for use with other tools and scripts.</p>
<pre><code class="language-sh">wrangler auth token&#10;</code></pre>
<p>The command returns whichever authentication method is currently configured, in priority order: API token from <code>CLOUDFLARE_API_TOKEN</code>, or OAuth token from <code>wrangler login</code> (automatically refreshed if expired).</p>
<p>Use the <code>--json</code> flag to get structured output including the token type:</p>
<pre><code class="language-sh">wrangler auth token --json&#10;</code></pre>
<p>The JSON output includes the authentication type:</p>
<pre><code class="language-jsonc">// API token&#10;{ &quot;type&quot;: &quot;api_token&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// OAuth token&#10;{ &quot;type&quot;: &quot;oauth&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// API key/email (only available with --json)&#10;{ &quot;type&quot;: &quot;api_key&quot;, &quot;key&quot;: &quot;...&quot;, &quot;email&quot;: &quot;...&quot; }&#10;</code></pre>
<p>API key/email credentials from <code>CLOUDFLARE_API_KEY</code> and <code>CLOUDFLARE_EMAIL</code> require the <code>--json</code> flag since this method uses two values instead of a single token.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-18">Dec 18, 2025</time><div>
<h2 id="post-2025-12-18-dashboard-improvements"><a href="/changelog/post/2025-12-18-dashboard-improvements/">Workers for Platforms - Dashboard Improvements</a></h2>
<div class="changelog-badges"><span>workers-for-platforms</span></div><div class="changelog-body"><p><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> lets you build multi-tenant platforms on <a href="/workers/">Cloudflare Workers</a>, allowing your end users to deploy and run their own code on your platform. It's designed for anyone building an AI vibe coding platform, e-commerce platform, website builder, or any product that needs to securely execute user-generated code at scale.</p>
<p>Previously, setting up Workers for Platforms required using the API. Now, the Workers for Platforms UI supports namespace creation, dispatch worker templates, and tag management, making it easier for Workers for Platforms customers to build and manage multi-tenant platforms directly from the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-for-platforms/dashboard-improvements.png" alt="Workers for Platforms Dashboard Improvements" /></p>
<h4 id="2025-12-18-dashboard-improvements-key-improvements">Key improvements</h4>
<ul>
<li><strong>Namespace Management:</strong> You can now create and configure <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace">dispatch namespaces</a> directly within the dashboard to start a new platform setup.</li>
<li><strong>Dispatch Worker Templates:</strong> New Dispatch Worker templates allow you to quickly define how traffic is routed to individual Workers within your namespace. Refer to the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dynamic Dispatch documentation</a> for more examples.</li>
<li><strong>Tag Management:</strong> You can now set and update <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/tags/">tags</a> on User Workers, making it easier to group and manage your Workers.</li>
<li><strong>Binding Visibility:</strong> <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">Bindings</a> attached to User Workers are now visible directly within the User Worker view.</li>
<li><strong>Deploy Vibe Coding Platform in one-click:</strong> Deploy a <a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">reference implementation</a> of an AI vibe coding platform directly from the dashboard. Powered by the Cloudflare's <a href="https://github.com/cloudflare/vibesdk">VibeSDK</a>, this starter kit integrates with Workers for Platforms to handle the deployment of AI-generated projects at scale.</li>
</ul>
<p>To get started, go to <strong>Workers for Platforms</strong> under <strong>Compute &amp; AI</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-17">Dec 17, 2025</time><div>
<h2 id="post-2025-12-17-shadow-it-domain-analytics"><a href="/changelog/post/2025-12-17-shadow-it-domain-analytics/">Shadow IT - domain level SaaS analytics</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Zero Trust has again upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>With this update, you can review data transfer metrics at the domain level, rather than just the application level, providing more granular insight into your data transfer patterns.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-domain.png" alt="New Domain Level Metrics" /></p>
<p>These metrics can be filtered by all available filters on the dashboard, including user, application, or content category.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-16">Dec 16, 2025</time><div>
<h2 id="post-2025-12-16-new-duplicate-action-for-supported-cloudflare-one-resources"><a href="/changelog/post/2025-12-16-new-duplicate-action-for-supported-cloudflare-one-resources/">New duplicate action for supported Cloudflare One resources</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>You can now duplicate specific Cloudflare One resources with a single click from the dashboard.</p>
<p>Initially supported resources:</p>
<ul>
<li>Access Applications</li>
<li>Access Policies</li>
<li>Gateway Policies</li>
</ul>
<p>To try this out, simply click on the overflow menu (⋮) from the resource table and click <i>Duplicate</i>. We will continue to add the Duplicate action for resources throughout 2026.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-16">Dec 16, 2025</time><div>
<h2 id="post-2025-12-16-vitest-ctx-exports-support"><a href="/changelog/post/2025-12-16-vitest-ctx-exports-support/">Support for ctx.exports in @cloudflare/vitest-pool-workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/testing/vitest-integration/"><code>@cloudflare/vitest-pool-workers</code></a> package now supports the <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code> API</a>, allowing you to access your Worker's top-level exports during tests.</p>
<p>You can access <code>ctx.exports</code> in unit tests by calling <code>createExecutionContext()</code>:</p>
<pre><code class="language-ts">import { createExecutionContext } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;can access ctx.exports&quot;, async () =&gt; {&#10;  const ctx = createExecutionContext();&#10;  const result = await ctx.exports.MyEntryPoint.myMethod();&#10;  expect(result).toBe(&quot;expected value&quot;);&#10;});&#10;</code></pre>
<p>Alternatively, you can import <code>exports</code> directly from <code>cloudflare:workers</code>:</p>
<pre><code class="language-ts">import { exports } from &quot;cloudflare:workers&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;can access imported exports&quot;, async () =&gt; {&#10;  const result = await exports.MyEntryPoint.myMethod();&#10;  expect(result).toBe(&quot;expected value&quot;);&#10;});&#10;</code></pre>
<p>See the <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/context-exports">context-exports fixture</a> for a complete example.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-16">Dec 16, 2025</time><div>
<h2 id="post-2025-12-16-wrangler-autoconfig"><a href="/changelog/post/2025-12-16-wrangler-autoconfig/">Configure your framework for Cloudflare automatically</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports automatic configuration for popular web frameworks in experimental mode, making it even easier to deploy to Cloudflare Workers.</p>
<p>Previously, if you wanted to deploy an application using a popular web framework like Next.js or Astro, you had to follow tutorials to set up your application for deployment to Cloudflare Workers. This usually involved creating a Wrangler file, installing adapters, or changing configuration options.</p>
<p>Now <code>wrangler deploy</code> does this for you. Starting with Wrangler 4.55, you can use <code>npx wrangler deploy --x-autoconfig</code> in the directory of any web application using one of the supported frameworks. Wrangler will then proceed to configure and deploy it to your Cloudflare account.</p>
<p>You can also configure your application without deploying it by using the new <code>npx wrangler setup</code> command. This enables you to easily review what changes we are making so your application is ready for Cloudflare Workers.</p>
<p>The following application frameworks are supported starting today:</p>
<ul>
<li>Next.js</li>
<li>Astro</li>
<li>Nuxt</li>
<li>TanStack Start</li>
<li>SolidStart</li>
<li>React Router</li>
<li>SvelteKit</li>
<li>Docusaurus</li>
<li>Qwik</li>
<li>Analog</li>
</ul>
<p>Automatic configuration also supports static sites by detecting the assets directory and build command. From a single index.html file to the output of a generator like Jekyll or Hugo, you can just run <code>npx wrangler deploy --x-autoconfig</code> to upload to Cloudflare.</p>
<p>We're really excited to bring you automatic configuration so you can do more with Workers. Please let us know if you run into challenges using this experimentally. We’ve opened a <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a> and would love to hear your feedback.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-15">Dec 15, 2025</time><div>
<h2 id="post-2025-12-15-rules-of-durable-objects"><a href="/changelog/post/2025-12-15-rules-of-durable-objects/">New Best Practices guide for Durable Objects</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>A new <a href="/durable-objects/best-practices/rules-of-durable-objects/">Rules of Durable Objects</a> guide is now available, providing opinionated best practices for building effective Durable Objects applications. This guide covers design patterns, storage strategies, concurrency, and common anti-patterns to avoid.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Design around your &quot;atom&quot; of coordination</strong> — Create one Durable Object per logical unit (chat room, game session, user) instead of a global singleton that becomes a bottleneck.</li>
<li><strong>Use SQLite storage with RPC methods</strong> — SQLite-backed Durable Objects with typed RPC methods provide the best developer experience and performance.</li>
<li><strong>Understand input and output gates</strong> — Learn how Cloudflare's runtime prevents data races by default, how write coalescing works, and when to use <code>blockConcurrencyWhile()</code>.</li>
<li><strong>Leverage Hibernatable WebSockets</strong> — Reduce costs for real-time applications by allowing Durable Objects to sleep while maintaining WebSocket connections.</li>
</ul>
<p>The <a href="/durable-objects/examples/testing-with-durable-objects/">testing documentation</a> has also been updated with modern patterns using <code>@cloudflare/vitest-pool-workers</code>, including examples for testing SQLite storage, alarms, and direct instance access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17718.md")</div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-12">Dec 12, 2025</time><div>
<h2 id="post-2025-12-12-durable-objects-sqlite-storage-billing"><a href="/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/">Billing for SQLite Storage</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>Storage billing for SQLite-backed Durable Objects will be enabled in January 2026, with a target date of January 7, 2026 (no earlier).</p>
<p>To view your SQLite storage usage, go to the <strong>Durable Objects</strong> page</p>
<div class="nb-dash-button"></div>
<p>If you do not want to incur costs, please take action such as optimizing queries or deleting unnecessary stored data in order to reduce your SQLite storage usage ahead of the January 7th target. Only usage on and after the billing target date will incur charges.</p>
<p>Developers on the Workers Paid plan with Durable Object's SQLite storage usage beyond included limits will incur charges according to <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">SQLite storage pricing</a> announced in September 2024 with the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">public beta</a>. Developers on the Workers Free plan will not be charged.</p>
<p>Compute billing for SQLite-backed Durable Objects has been enabled since the initial public beta. SQLite-backed Durable Objects currently incur <a href="/durable-objects/platform/pricing/#compute-billing">charges for requests and duration</a>, and no changes are being made to compute billing.</p>
<p>For more information about SQLite storage pricing and limits, refer to the <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">Durable Objects pricing documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-12">Dec 12, 2025</time><div>
<h2 id="post-2025-12-12-aggregation-support-and-more"><a href="/changelog/post/2025-12-12-aggregation-support-and-more/">R2 SQL now supports aggregations and schema discovery</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>R2 SQL now supports aggregation functions, <code>GROUP BY</code>, <code>HAVING</code>, along with schema discovery commands to make it easy to explore your data catalog.</p>
<h4 id="2025-12-12-aggregation-support-and-more-aggregation-functions">Aggregation Functions</h4>
<p>You can now perform aggregations on Apache Iceberg tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> using standard SQL functions including <code>COUNT(*)</code>, <code>SUM()</code>, <code>AVG()</code>, <code>MIN()</code>, and <code>MAX()</code>. Combine these with <code>GROUP BY</code> to analyze data across dimensions, and use <code>HAVING</code> to filter aggregated results.</p>
<pre><code class="language-sql">&#45;- Calculate average transaction amounts by department&#10;SELECT department, COUNT(*), AVG(total_amount)&#10;FROM my_namespace.sales_data&#10;WHERE region = &#x27;North&#x27;&#10;GROUP BY department&#10;HAVING COUNT(*) &gt; 50&#10;ORDER BY AVG(total_amount) DESC&#10;</code></pre>
<pre><code class="language-sql">&#45;- Find high-value departments&#10;SELECT department, SUM(total_amount)&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;HAVING SUM(total_amount) &gt; 50000&#10;</code></pre>
<h4 id="2025-12-12-aggregation-support-and-more-schema-discovery">Schema Discovery</h4>
<p>New metadata commands make it easy to explore your data catalog and understand table structures:</p>
<ul>
<li><code>SHOW DATABASES</code> or <code>SHOW NAMESPACES</code> - List all available namespaces</li>
<li><code>SHOW TABLES IN namespace_name</code> - List tables within a namespace</li>
<li><code>DESCRIBE namespace_name.table_name</code> - View table schema and column types</li>
</ul>
<pre><code class="language-bash">❯ npx wrangler r2 sql query &quot;{ACCOUNT_ID}_{BUCKET_NAME}&quot; &quot;DESCRIBE default.sales_data;&quot;&#10;&#10; ⛅️ wrangler 4.54.0&#10;─────────────────────────────────────────────&#10;&#10;┌──────────────────┬────────────────┬──────────┬─────────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐&#10;│ column_name      │ type           │ required │ initial_default │ write_default │ doc                                                                                               │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_id          │ BIGINT         │ false    │                 │               │ Unique identifier for each sales transaction                                                      │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_timestamp   │ TIMESTAMPTZ    │ false    │                 │               │ Exact date and time when the sale occurred (used for partitioning)                                │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ department       │ TEXT           │ false    │                 │               │ Product department (8 categories: Electronics, Beauty, Home, Toys, Sports, Food, Clothing, Books) │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ category         │ TEXT           │ false    │                 │               │ Product category grouping (4 categories: Premium, Standard, Budget, Clearance)                    │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ region           │ TEXT           │ false    │                 │               │ Geographic sales region (5 regions: North, South, East, West, Central)                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ product_id       │ INT            │ false    │                 │               │ Unique identifier for the product sold                                                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ quantity         │ INT            │ false    │                 │               │ Number of units sold in this transaction (range: 1-50)                                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ unit_price       │ DECIMAL(10, 2) │ false    │                 │               │ Price per unit in dollars (range: $5.00-$500.00)                                                  │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ total_amount     │ DECIMAL(10, 2) │ false    │                 │               │ Total sale amount before tax (quantity × unit_price with discounts applied)                       │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ discount_percent │ INT            │ false    │                 │               │ Discount percentage applied to this sale (0-50%)                                                  │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ tax_amount       │ DECIMAL(10, 2) │ false    │                 │               │ Tax amount collected on this sale                                                                 │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ profit_margin    │ DECIMAL(10, 2) │ false    │                 │               │ Profit margin on this sale as a decimal percentage                                                │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ customer_id      │ INT            │ false    │                 │               │ Unique identifier for the customer who made the purchase                                          │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ is_online_sale   │ BOOLEAN        │ false    │                 │               │ Boolean flag indicating if sale was made online (true) or in-store (false)                        │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_date        │ DATE           │ false    │                 │               │ Calendar date of the sale (extracted from sale_timestamp)                                         │&#10;└──────────────────┴────────────────┴──────────┴─────────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘&#10;Read 0 B across 0 files from R2&#10;On average, 0 B / s&#10;</code></pre>
<p>To learn more about the new aggregation capabilities and schema discovery commands, check out the <a href="/r2-sql/sql-reference/">SQL reference</a>. If you're new to R2 SQL, visit our <a href="/r2-sql/get-started/">getting started guide</a> to begin querying your data.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-11">Dec 11, 2025</time><div>
<h2 id="post-2025-12-11-sentinelone-destination"><a href="/changelog/post/2025-12-11-sentinelone-destination/">SentinelOne as Logpush destination</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare Logpush now supports <strong>SentinelOne</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.sentinelone.com/">SentinelOne AI SIEM</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/sentinelone/">Destination Configuration</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-11">Dec 11, 2025</time><div>
<h2 id="post-2025-12-11-emergency-waf-release"><a href="/changelog/post/2025-12-11-emergency-waf-release/">WAF Release - 2025-12-11 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release introduces rules for CVE-2025-55183 and CVE-2025-55184, targeting server-side function exposure and resource-exhaustion patterns, respectively.</p>
<p><strong>Key Findings</strong></p>
<p>Added coverage for Leaking Server Functions (CVE-2025-55183) and React Function DoS detection (CVE-2025-55184).</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection for server-function abuse techniques (CVE-2025-55183, CVE-2025-55184) that may expose internal logic or disrupt application availability.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>React - DoS - CVE:CVE-2025-55184</td>
<td>N/A</td>
<td>Disabled</td>
<td>This was labeled as Generic – Server Function Resource Exhaustion.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-10">Dec 10, 2025</time><div>
<h2 id="post-2025-12-10-pay-per-crawl-enhancements"><a href="/changelog/post/2025-12-10-pay-per-crawl-enhancements/">Pay Per Crawl (Private beta) - Discovery API, custom pricing, and advanced configuration</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>Pay Per Crawl is introducing enhancements for both AI crawler operators and site owners, focusing on programmatic discovery, flexible pricing models, and granular configuration control.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-ai-crawler-operators">For AI crawler operators</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-discovery-api">Discovery API</h4>
<p>A new authenticated API endpoint allows verified crawlers to programmatically discover domains participating in Pay Per Crawl. Crawlers can use this to build optimized crawl queues, cache domain lists, and identify new participating sites. This eliminates the need to discover payable content through trial requests.</p>
<p>The API endpoint is <code>GET https://crawlers-api.ai-audit.cfdata.org/charged_zones</code> and requires Web Bot Auth authentication. Refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> for authentication steps, request parameters, and response schema.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-payment-header-signature-requirement">Payment header signature requirement</h4>
<p>Payment headers (<code>crawler-exact-price</code> or <code>crawler-max-price</code>) must now be included in the Web Bot Auth <code>signature-input</code> header components. This security enhancement prevents payment header tampering, ensures authenticated payment intent, validates crawler identity with payment commitment, and protects against replay attacks with modified pricing. Crawlers must add their payment header to the list of signed components when <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#22-sign-your-request-with-web-bot-auth">constructing the signature-input header</a>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-new-crawler-error-header">New <code>crawler-error</code> header</h4>
<p>Pay Per Crawl error responses now include a new <code>crawler-error</code> header with 11 specific <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/">error codes</a> for programmatic handling. Error response bodies remain unchanged for compatibility. These codes enable robust error handling, automated retry logic, and accurate spending tracking.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-site-owners">For site owners</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-configure-free-pages">Configure free pages</h4>
<p>Site owners can now offer free access to specific pages like homepages, navigation, or discovery pages while charging for other content. Create a <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/#disable-pay-per-crawl-by-uri-pattern">Configuration Rule</a> in <strong>Rules</strong> &gt; <strong>Configuration Rules</strong>, set your URI pattern using wildcard, exact, or prefix matching on the <strong>URI Full</strong> field, and enable the <strong>Disable Pay Per Crawl</strong> setting. When disabled for a URI pattern, crawler requests pass through without blocking or charging.</p>
<p>Some paths are always free to crawl. These paths are: <code>/robots.txt</code>, <code>/sitemap.xml</code>, <code>/security.txt</code>, <code>/.well-known/security.txt</code>, <code>/crawlers.json</code>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-get-started">Get started</h4>
<p><strong>AI crawler operators</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> | <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/">Crawl pages</a></p>
<p><strong>Site owners</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-10">Dec 10, 2025</time><div>
<h2 id="post-2025-12-10-emergency-waf-release"><a href="/changelog/post/2025-12-10-emergency-waf-release/">WAF Release - 2025-12-10 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This additional week's emergency release introduces improvements to our existing rule for React – Remote Code Execution – CVE-2025-55182 - 2, along with two new generic detections covering server-side function exposure and resource-exhaustion patterns.</p>
<p><strong>Key Findings</strong></p>
<p>Enhanced detection logic for React – RCE – CVE-2025-55182, added Generic – Server Function Source Code Exposure, and added Generic – Server Function Resource Exhaustion.</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection against React RCE exploitation attempts and broaden coverage for common server-function abuse techniques that may expose internal logic or disrupt application availability.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bc1aee59731c488ca8b5314615fce168">15fce168</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="cbdd3f48396e4b7389d6efd174746aff">74746aff</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Resource Exhaustion</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-10">Dec 10, 2025</time><div>
<h2 id="post-2025-12-09-warp-macos-beta"><a href="/changelog/post/2025-12-09-warp-macos-beta/">WARP client for macOS (version 2025.10.118.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-10">Dec 10, 2025</time><div>
<h2 id="post-2025-12-09-warp-windows-beta"><a href="/changelog/post/2025-12-09-warp-windows-beta/">WARP client for Windows (version 2025.10.118.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Fixed an issue where sending large messages to the WARP daemon by Inter-Process Communication (IPC) could cause WARP to crash and result in service interruptions.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while WARP is connected.</li>
</ul>
<p>To work around this issue, reconnect the WARP client by toggling off and back on.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-08">Dec 8, 2025</time><div>
<h2 id="post-2025-12-08-python-cold-start-improvements"><a href="/changelog/post/2025-12-08-python-cold-start-improvements/">Python cold start improvements</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Python Workers now feature improved cold start performance, reducing initialization time for new Worker instances.
This improvement is particularly noticeable for Workers with larger dependency sets or complex initialization logic.</p>
<p>Every time you deploy a Python Worker, a memory snapshot is captured after the top level of the Worker is executed.
This snapshot captures all imports, including package imports that are often costly to load. The memory snapshot is loaded
when the Worker is first started, avoiding the need to reload the Python runtime and all dependencies on each cold start.</p>
<p>We set up a benchmark that imports common packages (<a href="https://www.python-httpx.org/">httpx</a>,
<a href="https://fastapi.tiangolo.com/">fastapi</a> and <a href="https://docs.pydantic.dev/latest/">pydantic</a>)
to see how Python Workers stack up against other platforms:</p>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Mean Cold Start (ms)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Python Workers</td>
<td>1027</td>
</tr>
<tr>
<td>AWS Lambda</td>
<td>2502</td>
</tr>
<tr>
<td>Google Cloud Run</td>
<td>3069</td>
</tr>
</tbody>
</table>
<p>These benchmarks run continuously. You can view the results and the methodology on our <a href="https://cold.edgeworker.net">benchmark page</a>.</p>
<p>In additional testing, we have found that without any memory snapshot, the cold start for this benchmark takes around 10 seconds, so this change improves cold start performance by roughly a factor of 10.</p>
<p>To get started with Python Workers, check out our <a href="/workers/languages/python/">Python Workers overview</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-08">Dec 8, 2025</time><div>
<h2 id="post-2025-12-08-python-pywrangler"><a href="/changelog/post/2025-12-08-python-pywrangler/">Easy Python package management with Pywrangler</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We are introducing a brand new tool called Pywrangler, which simplifies package management in Python Workers by
automatically installing Workers-compatible Python packages into your project.</p>
<p>With Pywrangler, you specify your Worker's Python dependencies in your <code>pyproject.toml</code> file:</p>
<pre><code class="language-toml">[project]&#10;name = &quot;python-beautifulsoup-worker&quot;&#10;version = &quot;0.1.0&quot;&#10;description = &quot;A simple Worker using beautifulsoup4&quot;&#10;requires-python = &quot;&gt;=3.12&quot;&#10;dependencies = [&#10;    &quot;beautifulsoup4&quot;&#10;]&#10;&#10;[dependency-groups]&#10;dev = [&#10;  &quot;workers-py&quot;,&#10;  &quot;workers-runtime-sdk&quot;&#10;]&#10;</code></pre>
<p>You can then develop and deploy your Worker using the following commands:</p>
<pre><code class="language-bash">uv run pywrangler dev&#10;uv run pywrangler deploy&#10;</code></pre>
<p>Pywrangler automatically downloads and vendors the necessary packages for your Worker, and these packages are bundled with the Worker when you deploy.</p>
<p>Consult the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler and Python package management in Workers.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-08">Dec 8, 2025</time><div>
<h2 id="post-2025-12-08-vite-optional-config"><a href="/changelog/post/2025-12-08-vite-optional-config/">Wrangler config is optional when using Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>When using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> to build and deploy Workers, a Wrangler configuration file is now optional for assets-only (static) sites. If no <code>wrangler.toml</code>, <code>wrangler.json</code>, or <code>wrangler.jsonc</code> file is found, the plugin generates sensible defaults for an assets-only site. The <code>name</code> is based on the <code>package.json</code> or the project directory name, and the <code>compatibility_date</code> uses the latest date supported by your installed Miniflare version.</p>
<p>This allows easier setup for static sites using Vite. Note that SPAs will still need to <a href="https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/">set <code>assets.not_found_handling</code> to <code>single-page-application</code></a> in order to function correctly.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-08">Dec 8, 2025</time><div>
<h2 id="post-2025-12-08-vite-programmatic-config"><a href="/changelog/post/2025-12-08-vite-programmatic-config/">Configure Workers programmatically using the Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> now supports programmatic configuration of Workers without a Wrangler configuration file. You can use the <code>config</code> option to define Worker settings directly in your Vite configuration, or to modify existing configuration loaded from a Wrangler config file. This is particularly useful when integrating with other build tools or frameworks, as it allows them to control Worker configuration without needing users to manage a separate config file.</p>
<h4 id="2025-12-08-vite-programmatic-config-the-config-option">The <code>config</code> option</h4>
<p>The Vite plugin's new <code>config</code> option accepts either a partial configuration object or a function that receives the current configuration and returns overrides. This option is applied after any config file is loaded, allowing the plugin to override specific values or define Worker configuration entirely in code.</p>
<h4 id="2025-12-08-vite-programmatic-config-example-usage">Example usage</h4>
<p>Setting <code>config</code> to an object to provide configuration values that merge with defaults and config file settings:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: {&#10;				name: &quot;my-worker&quot;,&#10;				compatibility_flags: [&quot;nodejs_compat&quot;],&#10;				send_email: [&#10;					{&#10;						name: &quot;EMAIL&quot;,&#10;					},&#10;				],&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>Use a function to modify the existing configuration:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: (userConfig) =&gt; {&#10;				delete userConfig.compatibility_flags;&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>Return an object with values to merge:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: (userConfig) =&gt; {&#10;				if (!userConfig.compatibility_flags.includes(&quot;no_nodejs_compat&quot;)) {&#10;					return { compatibility_flags: [&quot;nodejs_compat&quot;] };&#10;				}&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h4 id="2025-12-08-vite-programmatic-config-auxiliary-workers">Auxiliary Workers</h4>
<p>Auxiliary Workers also support the <code>config</code> option, enabling multi-Worker architectures without config files.</p>
<p>Define auxiliary Workers without config files using <code>config</code> inside the <code>auxiliaryWorkers</code> array:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: {&#10;				name: &quot;entry-worker&quot;,&#10;				main: &quot;./src/entry.ts&quot;,&#10;				services: [{ binding: &quot;API&quot;, service: &quot;api-worker&quot; }],&#10;			},&#10;			auxiliaryWorkers: [&#10;				{&#10;					config: {&#10;						name: &quot;api-worker&quot;,&#10;						main: &quot;./src/api.ts&quot;,&#10;					},&#10;				},&#10;			],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>For more details and examples, see <a href="/workers/vite-plugin/reference/programmatic-configuration/">Programmatic configuration</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-05">Dec 5, 2025</time><div>
<h2 id="post-2025-12-05-terraform-v5.14.0-provider"><a href="/changelog/post/2025-12-05-terraform-v5.14.0-provider/">Terraform v5.14.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.14 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2025-12-05-terraform-v5.14.0-provider-deprecation-notice">Deprecation notice</h4>
<p>Resource affected: <code>api_shield_discovery_operation</code></p>
<p>Cloudflare continuously discovers and updates API endpoints and web assets of your web applications. To improve the maintainability of these dynamic resources, we are working on reducing the need to actively engage with discovered operations.</p>
<p>The corresponding public API endpoint of <a href="https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/">discovered operations</a> is not affected and will continue to be supported.</p>
<h4 id="2025-12-05-terraform-v5.14.0-provider-features">Features</h4>
<ul>
<li><strong>pages_project</strong>: Add v4 -&gt; v5 migration tests (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/pull/6506">#6506</a>)</li>
</ul>
<h4 id="2025-12-05-terraform-v5.14.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>account_members</strong>: Makes member policies a set (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6488">#6488</a>)</li>
<li><strong>pages_project</strong>: Ensures non empty refresh plans (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6515">#6515</a>)</li>
<li><strong>R2</strong>: Improves sweeper (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6512">#6512</a>)</li>
<li><strong>workers_kv</strong>: Ignores value import state for verify (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6521">#6521</a>)</li>
<li><strong>workers_script</strong>: No longer treats the migrations attribute as WriteOnly (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6489">#6489</a>)</li>
<li><strong>workers_script</strong>: Resolves resource drift when worker has unmanaged secret (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6504">#6504</a>)</li>
<li><strong>zero_trust_device_posture_rule</strong>: Preserves input.version and other fields (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6500">#6500</a>) and (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6503">#6503</a>)</li>
<li><strong>zero_trust_dlp_custom_profile</strong>: Adds sweepers for <code>dlp_custom_profile</code></li>
<li><strong>zone_subscription|account_subscription</strong>: Adds <code>partners_ent</code> as valid enum for <code>rate_plan.id</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6505">#6505</a>)</li>
<li><strong>zone</strong>: Ensures datasource model schema parity (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6487">#6487</a>)</li>
<li><strong>subscription</strong>: Updates import signature to accept account_id/subscription_id to import account subscription (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6510">#6510</a>)</li>
</ul>
<h4 id="2025-12-05-terraform-v5.14.0-provider-upgrade-to-newer-version">Upgrade to newer version</h4>
We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-12-05-terraform-v5.14.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-05">Dec 5, 2025</time><div>
<h2 id="post-2025-12-05-rcs-vuln"><a href="/changelog/post/2025-12-05-rcs-vuln/">Increased WAF payload limit for all plans</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>Cloudflare WAF now inspects request-payload size of up to 1 MB across all plans to enhance our detection capabilities for React RCE (CVE-2025-55182).</p>
<p><strong>Key Findings</strong></p>
<p>React payloads commonly have a default maximum size of 1 MB. Cloudflare WAF previously inspected up to 128 KB on Enterprise plans, with even lower limits on other plans.</p>
<p><strong>Update:</strong> We later reinstated the maximum request-payload size the Cloudflare WAF inspects. Refer to <a href="/changelog/2025-12-05-waf-max-payload-size-change/">Updating the WAF maximum payload values</a> for details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-05">Dec 5, 2025</time><div>
<h2 id="post-2025-12-05-waf-max-payload-size-change"><a href="/changelog/post/2025-12-05-waf-max-payload-size-change/">Updating the WAF maximum payload values</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>We are reinstating the maximum request-payload size the Cloudflare WAF inspects, with WAF on Enterprise zones inspecting up to 128 KB.</p>
<p><strong>Key Findings</strong></p>
<p>On <a href="/changelog/2025-12-05-rcs-vuln/">December 5, 2025</a>, we initially attempted to increase the maximum WAF payload limit to 1 MB across all plans. However, an automatic rollout for all customers proved impractical because the increase led to a surge in false positives for existing managed rules.</p>
<p>This issue was particularly notable within the Cloudflare Managed Ruleset and the Cloudflare OWASP Core Ruleset, impacting customer traffic.</p>
<p><strong>Impact</strong></p>
<p>Customers on paid plans can increase the limit to 1 MB for any of their zones by contacting Cloudflare Support. Free zones are already protected up to 1 MB and do not require any action.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-12-04">Dec 4, 2025</time><div>
<h2 id="post-2025-12-04-hyperdrive-remote-database-local-dev"><a href="/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/">Connect to remote databases during local development with wrangler dev</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now connect directly to remote databases and databases requiring TLS with <code>wrangler dev</code>.
This lets you run your Worker code locally while connecting to remote databases, without needing to use <code>wrangler dev --remote</code>.</p>
<p>The <code>localConnectionString</code> field and <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code> environment variable can be used to configure the connection string used by <code>wrangler dev</code>.</p>
<pre><code class="language-jsonc">{&#10;  &quot;hyperdrive&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;HYPERDRIVE&quot;,&#10;      &quot;id&quot;: &quot;your-hyperdrive-id&quot;,&#10;      &quot;localConnectionString&quot;: &quot;postgres://user:password@remote-host.example.com:5432/database?sslmode=require&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/local-development/">local development with Hyperdrive</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/28/">Previous</a><span>Page 29 of 50</span><a class="pagination-next" rel="next" href="/changelog/30/">Next</a></nav>
</div>
