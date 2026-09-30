---
cp9:
  canonical: https://developers.cloudflare.com/changelog/13/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 13 | Cloudflare Docs
  head_html: <title>Changelog - page 13 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/13/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 13"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/13/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/13/#page","headline":"Changelog - page 13 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/13/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/13/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-06-05">Jun 5, 2026</time><div>
<h2 id="post-2026-06-05-radar-traffic-chart-granularity"><a href="/changelog/post/2026-06-05-radar-traffic-chart-granularity/">Finer-grained chart granularity on Cloudflare Radar for longer time ranges</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now provides finer-grained traffic charts for longer time ranges. Previously, selecting a 1-3 month view on HTTP and NetFlows charts defaulted to weekly aggregation, which was too coarse to surface meaningful trends. Views longer than 3 months defaulted to monthly aggregation, returning as few as 7 data points for a 6-month range.</p>
<p>The new defaults are:</p>
<ul>
<li><strong>1-3 months</strong>: daily granularity (7x more data points)</li>
<li><strong>Longer than 3 months</strong> (HTTP and NetFlows): weekly granularity (4x more data points)</li>
</ul>
<p>For example, a 12-week traffic view previously showed weekly data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-before.png" alt="Traffic trends chart with weekly granularity for a 12-week view" /></p>
<p>The same view now shows daily data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-after.png" alt="Traffic trends chart with daily granularity for a 12-week view" /></p>
<p>Similarly, a 1-year HTTP traffic view that previously showed just 12 monthly data points now provides 52 weekly data points.</p>
<p>Visit <a href="https://radar.cloudflare.com/?dateRange=12w#traffic-trends">Cloudflare Radar</a> to explore the new granular views.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-05">Jun 5, 2026</time><div>
<h2 id="post-2026-06-05-gateway-egress"><a href="/changelog/post/2026-06-05-gateway-egress/">Filter Workers' public Internet traffic using Gateway policies</a></h2>
<div class="changelog-badges"><span>gateway</span><span>mesh</span><span>workers-vpc</span></div><div class="changelog-body"><p>Workers using a <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> binding with <code>network_id: &quot;cf1:network&quot;</code> now egress to public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.</p>
<div class="nb-interactive-component" data-cf-component="WorkersVPCEgressDiagram"></div>
<p>What you get by default:</p>
<ul>
<li><strong>Visibility.</strong> Worker egress shows up in Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> logs alongside your other traffic, so you can audit what your Workers are calling and when.</li>
<li><strong>Enforcement.</strong> Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17825.md")</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17826.md")</div>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>. For policy authoring, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway traffic policies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-04">Jun 4, 2026</time><div>
<h2 id="post-2026-06-04-idp-federation"><a href="/changelog/post/2026-06-04-idp-federation/">Share identity providers across accounts with IdP federation</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which allows organizations to share a single identity provider across multiple Cloudflare accounts.</p>
<p>Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>One IdP, many accounts</strong> — Configure your IdP once and share it with all accounts in your organization.</li>
<li><strong>Lifecycle management</strong> — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.</li>
<li><strong>Immutable recipient connections</strong> — IdP connections in recipient accounts cannot be accidentally modified or deleted.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-04">Jun 4, 2026</time><div>
<h2 id="post-2026-06-04-billable-usage-product-sidebar"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>workers</span><span>d1</span><span>r2</span><span>kv</span><span>queues</span><span>vectorize</span><span>durable-objects</span><span>containers</span></div><div class="changelog-body"><p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-04">Jun 4, 2026</time><div>
<h2 id="post-2026-05-27-pipeline-binding-stream-field"><a href="/changelog/post/2026-05-27-pipeline-binding-stream-field/">Pipeline binding configuration field renamed to stream</a></h2>
<div class="changelog-badges"><span>pipelines</span><span>workers</span></div><div class="changelog-body"><p>The <code>pipeline</code> field inside the <code>pipelines</code> binding configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> has been renamed to <code>stream</code>. The old field is deprecated but still accepted.</p>
<p>Update your configuration to use <code>stream</code> to avoid the deprecation warning.</p>
<p><strong>Before (deprecated):</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17739.md")</div>
<p><strong>After:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17740.md")</div>
<p>No other changes are required. The binding name, TypeScript types, and runtime API (<code>env.MY_PIPELINE.send(...)</code>) remain the same.</p>
<p>For more information on configuring pipeline bindings, refer to <a href="/pipelines/streams/writing-to-streams/#configure-pipeline-binding">Writing to streams</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-03">Jun 3, 2026</time><div>
<h2 id="post-2026-06-03-saml-assertion-encryption"><a href="/changelog/post/2026-06-03-saml-assertion-encryption/">SAML assertion encryption for identity providers</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports SAML assertion encryption for identity provider integrations. When turned on, your identity provider encrypts SAML assertions using a Cloudflare-managed certificate before sending them through the user's browser. Only Access can decrypt these assertions, protecting sensitive identity data even after TLS termination.</p>
<p>Without encryption, SAML assertions are transmitted in plaintext and could be visible to browser extensions or client-side malware.</p>
<p><img src="/assets/upstream/images/changelog/access/saml-encryption.png" alt="SAML encryption toggle in the identity provider configuration" /></p>
<p>SAML encryption includes built-in certificate lifecycle management:</p>
<ul>
<li><strong>Automatic certificate generation</strong>: Access generates an encryption certificate when you turn on SAML encryption for an identity provider.</li>
<li><strong>Certificate rotation</strong>: Rotate certificates without downtime. The previous certificate remains valid until expiration, giving you time to update your IdP.</li>
<li><strong>PEM export</strong>: Copy the certificate in PEM format for manual upload to your IdP, or point your IdP to the SAML metadata endpoint for automatic retrieval.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#encrypt-saml-assertions">Encrypt SAML assertions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-03">Jun 3, 2026</time><div>
<h2 id="post-2026-06-03-public-oauth-clients"><a href="/changelog/post/2026-06-03-public-oauth-clients/">Introducing self-managed OAuth clients</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.</p>
<p>OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.</p>
<h4 id="2026-06-03-public-oauth-clients-what-is-new">What is new</h4>
<p>Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.</p>
<h4 id="2026-06-03-public-oauth-clients-create-an-application">Create an application</h4>
<p>To create an application, go to <strong>Manage account</strong> &gt; <strong>OAuth clients</strong> in your account on the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<h4 id="2026-06-03-public-oauth-clients-select-limited-scopes">Select limited scopes</h4>
<p>If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.</p>
<p>Users can review the requested scopes before they consent.</p>
<h4 id="2026-06-03-public-oauth-clients-apps-for-both-private-and-public-use">Apps for both private and public use</h4>
<p>Applications start with <code>private</code> visibility. Private applications can only be used by members of the account where the application was created.</p>
<p>To make an application available to any Cloudflare user, complete the prerequisites for <code>public</code> visibility.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients">client visibility</a>.</p>
<h4 id="2026-06-03-public-oauth-clients-client-domain-verification">Client domain verification</h4>
<p>Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.</p>
<p>After verification, users see a verified badge on the consent page.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification">domain verification</a>.</p>
<h4 id="2026-06-03-public-oauth-clients-learn-more">Learn more</h4>
<p>For more information, refer to <a href="/fundamentals/oauth/">OAuth clients</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-03">Jun 3, 2026</time><div>
<h2 id="post-2026-06-03-bulk-secrets-api"><a href="/changelog/post/2026-06-03-bulk-secrets-api/">New Workers bulk secrets API endpoint</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create, update, or delete multiple secrets for your Worker in a single request using the <a href="/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/">bulk secrets endpoint</a>.</p>
<ul>
<li>Include a secret with a value to create or update.</li>
<li>Set a secret to <code>null</code> to delete.</li>
<li>Secrets not included in the request are left unchanged.</li>
</ul>
<p>The following example creates <code>API_KEY</code>, updates the already existing <code>DB_PASSWORD</code>, and deletes <code>OLD_SECRET</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;secrets&quot;: {&#10;    &quot;API_KEY&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;API_KEY&quot;, &quot;text&quot;: &quot;my-api-key&quot; },&#10;    &quot;DB_PASSWORD&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;DB_PASSWORD&quot;, &quot;text&quot;: &quot;my-db-password&quot; },&#10;    &quot;OLD_SECRET&quot;: null&#10;  }&#10;}&#10;</code></pre>
<p>You can do the same from the command line using <a href="/workers/wrangler/commands/workers/#secret-bulk"><code>wrangler secret bulk</code></a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret bulk &lt; secrets.json&#10;</code></pre>
<p>To delete a key, set its value to <code>null</code> in the JSON file. Deletion is not supported with <code>.env</code> files.</p>
<p>Each request supports up to <strong>100 total operations</strong> (creates, updates, and deletes combined).</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-03">Jun 3, 2026</time><div>
<h2 id="post-2026-06-03-wrangler-keyring-credential-storage"><a href="/changelog/post/2026-06-03-wrangler-keyring-credential-storage/">Store Wrangler's OAuth credentials in your OS keychain</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/wrangler/">Wrangler</a> can now store the OAuth credentials returned by <code>wrangler login</code> in an <a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">AES-256-GCM</a>-encrypted file, with the encryption key held in your operating system keychain. The default behavior is unchanged — credentials still live in a plaintext TOML file unless you opt in.</p>
<p>To opt in, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --use-keyring&#10;</code></pre>
<p>The choice is persisted across Wrangler invocations. Opt back out with <code>npx wrangler login --no-use-keyring</code>, or override the preference for a single command with the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
<p><code>wrangler whoami</code> now reports where credentials are stored:</p>
<pre tabindex="0"><code class="language-sh">🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)&#10;</code></pre>
<p>Per-platform backends:</p>
<ul>
<li><strong>macOS</strong> uses the built-in Keychain via <code>/usr/bin/security</code>.</li>
<li><strong>Linux</strong> uses <a href="https://wiki.gnome.org/Projects/Libsecret">libsecret</a> via the <code>secret-tool</code> CLI from the <code>libsecret-tools</code> package.</li>
<li><strong>Windows</strong> uses Credential Manager via <a href="https://www.npmjs.com/package/@napi-rs/keyring"><code>@napi-rs/keyring</code></a>, installed on-demand the first time you opt in.</li>
</ul>
<p>Refer to <a href="/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</a> for the full details, including the migration behavior on opt-in/opt-out and the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-02">Jun 2, 2026</time><div>
<h2 id="post-2026-06-02-cron-workflows"><a href="/changelog/post/2026-06-02-cron-workflows/">Schedule Workflow instances directly from your Workflow binding</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>You can now attach cron schedules directly to a Workflow binding in <code>wrangler.jsonc</code>. Each scheduled run creates a new Workflow instance automatically, so you do not need to define a separate Worker with a <code>scheduled</code> handler just to trigger your Workflow on an interval.</p>
<p>For example, you can configure hourly, every-15-minute, or weekday schedules on the same Workflow:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;workflows&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;my-scheduled-workflow&quot;,&#10;			&quot;binding&quot;: &quot;MY_WORKFLOW&quot;,&#10;			&quot;class_name&quot;: &quot;MyScheduledWorkflow&quot;,&#10;			&quot;schedules&quot;: [&quot;0 * * * *&quot;, &quot;*/15 * * * *&quot;, &quot;0 9 * * MON-FRI&quot;],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>Cron workloads get all the same benefits of Workflows with built-in retries, multi-step durable execution, and configurable timeouts of Workflows.</p>
<pre tabindex="0"><code class="language-ts">import {&#10;	WorkflowEntrypoint,&#10;	WorkflowEvent,&#10;	WorkflowStep,&#10;} from &quot;cloudflare:workers&quot;;&#10;&#10;// Runs automatically on each cron schedule defined for the MY_WORKFLOW binding in wrangler.jsonc.&#10;export class MyScheduledWorkflow extends WorkflowEntrypoint&lt;Env&gt; {&#10;	async run(event: WorkflowEvent, step: WorkflowStep) {&#10;		const data = await step.do(&quot;fetch source data&quot;, async () =&gt; {&#10;			return await fetchSourceData();&#10;		});&#10;&#10;		// If this step fails, only this step is retried with the custom logic below&#10;		await step.do(&#10;			&quot;process and store results&quot;,&#10;			{&#10;				retries: { limit: 5, delay: &quot;30 seconds&quot;, backoff: &quot;exponential&quot; },&#10;				timeout: &quot;10 minutes&quot;,&#10;			},&#10;			async () =&gt; {&#10;				await processAndStore(data);&#10;			},&#10;		);&#10;	}&#10;}&#10;</code></pre>
<p>This makes it easier to build recurring, scheduled jobs such as database backups, invoice generation, report aggregation, and cleanup tasks without wiring up a separate Cron Trigger entrypoint.</p>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/">Trigger Workflows</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-02">Jun 2, 2026</time><div>
<h2 id="post-2026-06-02-agents-sdk-v0.14.0"><a href="/changelog/post/2026-06-02-agents-sdk-v0.14.0/">Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds four new ways to build with <code>@cloudflare/think</code>: on-demand Agent Skills, chat messengers (starting with Telegram), declarative scheduled tasks, and durable reasoning steps inside Workflows. This release also significantly hardens durable chat recovery, so turns reliably ride through deploys, evictions, and stalled model streams in production.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-agent-skills-experimental">Agent Skills (experimental)</h4>
<p>Give an agent a catalog of on-demand instructions, resources, and scripts. A skill source adds a catalog to the system prompt, and the model activates a skill only when a task matches — so a large library of capabilities does not bloat every prompt.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17667.md")</div>
<p>The <code>agents:skills</code> import bundles a local <code>./skills</code> directory through the Agents Vite plugin (one directory per skill, each with a <code>SKILL.md</code>). Skills can also load from R2 or a manifest. When skills are available, Think exposes <code>activate_skill</code>, <code>read_skill_resource</code>, and an optional <code>run_skill_script</code> tool. Skill loading is resilient: a duplicate or failing source is skipped with a warning instead of breaking the agent.</p>
<p>Agent Skills are <strong>experimental</strong>, and script execution in particular is early. The API may change in a future release. We would love your feedback — tell us what you are building and what is missing in the <a href="https://github.com/cloudflare/agents/discussions">Agents repository</a>.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-messengers">Messengers</h4>
<p>Connect a Think agent directly to a chat platform. Think owns the webhook route, conversation routing, durable reply fiber, and streamed delivery back to the provider. Telegram ships as the first provider.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17668.md")</div>
<p>Each Chat SDK thread maps to its own Think sub-agent by default, so group chats and direct messages do not share memory. Multiple bots, custom conversation routing, and custom providers are all supported.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-scheduled-tasks">Scheduled tasks</h4>
<p>Declare recurring, timezone-aware prompts and handlers with a typed domain-specific language (DSL). Think reconciles the declarations on startup and re-arms the next occurrence after each run, backed by durable idempotent submissions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17669.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-think-workflows">Think Workflows</h4>
<p>Run a model-driven reasoning step inside a Cloudflare Workflow with <code>ThinkWorkflow</code> and <code>step.prompt()</code>, with durable typed structured output, long waits, and approval gates.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17670.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-production-hardening-for-durable-chat-recovery">Production hardening for durable chat recovery</h4>
<p>Durable chat turns have always been designed to survive a mid-turn deploy or Durable Object eviction. This release is a major hardening pass on that machinery for production.</p>
<ul>
<li><strong>Better recovery during deploys.</strong> Turns now ride through continuous deploys and evictions without losing completed work or re-running tools that already ran.</li>
<li><strong>A live &quot;recovering…&quot; signal.</strong> <code>useAgentChat</code> exposes a new <code>isRecovering</code> flag, so a recovering turn shows progress instead of looking frozen. Most UIs render <code>isStreaming || isRecovering</code> as &quot;busy&quot;.</li>
<li><strong>Stalled streams recover.</strong> Set <code>chatStreamStallTimeoutMs</code> to route a hung provider stream into the same recovery path instead of leaving an infinite spinner.</li>
<li><strong>Sub-agents re-attach.</strong> On parent recovery, an in-flight <code>agentTool()</code> child is re-attached to its result rather than abandoned and re-run, so long-running children no longer lose work under deploys.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-mcp-transport-improvements">MCP transport improvements</h4>
<ul>
<li><strong>Resumable streams</strong> — In-flight tool calls over Server-Sent Events (SSE) survive a dropped connection. Clients reconnect with <code>Last-Event-ID</code> and replay anything they missed.</li>
<li><strong>Readable server IDs</strong> — <code>addMcpServer</code> accepts an optional <code>id</code>, so tools surface as readable keys (for example <code>tool_github_create_pull_request</code>) instead of opaque connection IDs.</li>
<li><strong>Better handling of concurrent requests</strong> — Overlapping JSON-RPC requests are now correctly correlated to their responses across the HTTP and RPC transports.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Compaction</strong> — A <code>Session</code>'s <code>tokenCounter</code> now also drives the compaction boundary decision (&quot;what to compress&quot;), not just the fire/no-fire trigger.</li>
<li><strong><code>@cloudflare/worker-bundler</code></strong> — Adds a <code>virtualModules</code> option to <code>createWorker</code> to provide in-memory module source during bundling.</li>
<li><strong>Client-tool continuations</strong> — Parallel tool results now coalesce into a single continuation, immediate resume requests attach to the pending continuation, and server-side <code>needsApproval</code> continuations resume reliably after approval.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-02">Jun 2, 2026</time><div>
<h2 id="post-2026-06-02-cisco-ios-xe"><a href="/changelog/post/2026-06-02-cisco-ios-xe/">Cisco IOS XE</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span><span>cloudflare-one</span></div><div class="changelog-body"><p>The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:</p>
<ul>
<li>Post Quantum Cryptography (PQC)</li>
<li>Policy-Based Routing (PBR)</li>
<li>IP Service Level Agreement (IP SLA)</li>
</ul>
<p>This link will take you directly to the updated <a href="/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a> guide.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-01">Jun 1, 2026</time><div>
<h2 id="post-2026-06-01-log-fields-updated"><a href="/changelog/post/2026-06-01-log-fields-updated/">New Turnstile Events Logpush dataset in Cloudflare Logs</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-01-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Turnstile Events</strong>: A new dataset with fields including <code>ASN</code>, <code>Action</code>, <code>BrowserMajor</code>, <code>BrowserName</code>, <code>ClientIP</code>, <code>CountryCode</code>, <code>EventType</code>, <code>Hostname</code>, <code>OSMajor</code>, <code>OSName</code>, <code>Sitekey</code>, <code>Timestamp</code>, and <code>UserAgent</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-05-29-sandbox-named-tunnels"><a href="/changelog/post/2026-05-29-sandbox-named-tunnels/">Share sandbox previews through Cloudflare Tunnel</a></h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p><a href="/sandbox/">Sandboxes</a> can expose a service running inside the container on a public preview URL through the <code>sandbox.tunnels</code> namespace. The SDK uses <code>cloudflared</code> inside the sandbox so you can share a running service without configuring <code>exposePort()</code> or a custom domain.</p>
<p>By default, <code>sandbox.tunnels.get(port)</code> creates a <a href="https://try.cloudflare.com/">quick tunnel</a> on a zero-config <code>*.trycloudflare.com</code> URL — no Cloudflare account, DNS record, or custom domain required. This is perfect for quick development and for <code>.workers.dev</code> deployments.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17665.md")</div>
<h4 id="2026-05-29-sandbox-named-tunnels-named-tunnels">Named tunnels</h4>
<p>For more control you can create a named tunnel through <code>sandbox.tunnels.get(port, { name })</code>. A named tunnel binds a hostname (<code>&lt;name&gt;.&lt;your-zone&gt;</code>) backed by a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and a CNAME record on your zone resulting in something like <a href="https://my-app-preview.example.com">https://my-app-preview.example.com</a>.</p>
<p>Unlike quick tunnels, which generate a new random URL each time, a named tunnel produces a persistent URL that survives container restarts. This makes named tunnels suitable for production use cases where you want control over the tunnel and it's origin.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17666.md")</div>
<p>Calling <code>sandbox.destroy()</code> tears down the Cloudflare Tunnel and the associated DNS record alongside the container, so you do not leave dangling tunnels or records behind.</p>
<h4 id="2026-05-29-sandbox-named-tunnels-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For full API details, refer to the <a href="/sandbox/api/tunnels/">Sandbox tunnels reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-06-04-migrations-pattern"><a href="/changelog/post/2026-06-04-migrations-pattern/">D1 migrations support nested layouts via `migrations_pattern`</a></h2>
<div class="changelog-badges"><span>d1</span></div><div class="changelog-body"><p>You can now point <code>wrangler d1 migrations apply</code> at a nested migrations layout — such as the one produced by <a href="https://orm.drizzle.team/">Drizzle</a> (<code>migrations/0001_init/migration.sql</code>) — using the new <code>migrations_pattern</code> D1 binding config:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;d1_databases&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;DB&quot;,&#10;			&quot;database_name&quot;: &quot;my-database&quot;,&#10;			&quot;database_id&quot;: &quot;&lt;UUID&gt;&quot;,&#10;			&quot;migrations_dir&quot;: &quot;migrations&quot;,&#10;			&quot;migrations_pattern&quot;: &quot;migrations/*/migration.sql&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p><code>migrations_pattern</code> is a glob (relative to your Wrangler config file) used to discover migration files. It defaults to <code>${migrations_dir}/*.sql</code>, so existing projects keep working unchanged. Each migration's name is recorded in the migrations table as a path relative to <code>migrations_dir</code>.</p>
<p>To learn more, visit D1's <a href="/d1/reference/migrations/#nested-migration-layouts">migrations documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-05-29-log-fields-updated"><a href="/changelog/post/2026-05-29-log-fields-updated/">Updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-29-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>DEX Device State Events</strong> (added): <code>DeviceRegistrationProfileID</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>AddedHeaders</code>, <code>DeletedHeaders</code>, and <code>SetHeaders</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>MatchedRules</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-05-29-radar-pq-tls-bug-detection"><a href="/changelog/post/2026-05-29-radar-pq-tls-bug-detection/">TLS bug detection in the Cloudflare Radar post-quantum checker</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p>The <a href="/radar/"><strong>Radar</strong></a> <a href="https://radar.cloudflare.com/post-quantum#website-support">post-quantum TLS support checker</a> now also reports TLS bugs detected during the handshake test. When a scanned host exhibits compatibility issues, the results include details on the specific bugs detected, along with guidance on how to investigate and remediate each issue. The bugs section only appears for hosts where issues are found.</p>
<p>The following TLS bugs are detected:</p>
<ul>
<li><strong>Split ClientHello</strong> — The connection fails with a fragmented post-quantum <code>ClientHello</code> but succeeds with classical handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS messages.</li>
<li><strong>HRR Failure</strong> — The server sends a <code>HelloRetryRequest</code> but fails to complete the handshake afterward.</li>
<li><strong>Unknown Keyshare</strong> — The server cannot handle unknown key exchange algorithms and fails instead of responding with a <code>HelloRetryRequest</code> as required by the TLS 1.3 specification.</li>
</ul>
<p><img src="/assets/upstream/images/radar/pq-tls-bug-detection.png" alt="TLS bug detection results in the Radar post-quantum checker" /></p>
<p>Bug detection data is available through the existing <a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> endpoint.</p>
<p>Visit the <a href="https://radar.cloudflare.com/post-quantum#website-support">Post-Quantum Encryption</a> page to test a host.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-05-29-websocket-adapter-auto-reconnect"><a href="/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/">Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media</a></h2>
<div class="changelog-badges"><span>realtime</span></div><div class="changelog-body"><p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC Selective Forwarding Unit that runs on Cloudflare's global network</a>, so you can route live audio, video, and data between WebRTC clients around the world without managing SFU infrastructure or regions.</p>
<p>When you use the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> to stream WebRTC media to a WebSocket endpoint, the adapter now auto-reconnects and buffers audio and video after brief endpoint disconnects or restarts.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-streaming-webrtc-media-to-websocket-endpoints">Streaming WebRTC media to WebSocket endpoints</h4>
<p>Many teams also use Realtime SFU as the media layer for backend applications, such as transcription, recording, note-taking, and agentic media-processing services. These systems often need to consume live WebRTC audio or video from the SFU in backend infrastructure, including <a href="/durable-objects/">Durable Objects</a>, <a href="/workers/">Workers</a>, <a href="/containers/">Containers</a>, or external services, without running a WebRTC client themselves.</p>
<p>The <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> bridges that gap by streaming WebRTC media from the SFU to a standard WebSocket endpoint as application-consumable payloads: <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-formats">PCM audio frames and JPEG video frames</a>.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-what-changed">What changed</h4>
<p>When you use the WebSocket adapter in <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#stream-mode-egress">Stream mode (egress)</a> to send live audio or video from the SFU to your own WebSocket endpoint, the SFU now <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">automatically reconnects</a> after brief endpoint disconnects or restarts. This is especially helpful for long-running media pipelines where the WebSocket endpoint may briefly restart while a recording, transcription, or live analysis job is still in progress.</p>
<p>Previously, a brief disconnect from your WebSocket endpoint could close the adapter and require your application to recreate it before media could resume. Now, the SFU retries the same endpoint for up to 5 seconds with no API change required. If the endpoint comes back within that window, audio and video delivery resumes automatically.</p>
<p>The reconnect behavior also includes <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-buffering-during-reconnect">live-first media buffering</a>, so brief interruptions reduce media loss without replaying stale video.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-reconnect-behavior">Reconnect behavior</h4>
<p>During reconnect:</p>
<ul>
<li>Audio uses a short bounded backlog to reduce audible loss. If the interruption lasts longer than the backlog can cover, older audio may be dropped.</li>
<li>Video resumes from the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#video-jpeg">latest available JPEG frame</a> instead of replaying stale frames.</li>
<li>Recovery is best effort and does not guarantee gapless or exactly-once delivery.</li>
</ul>
<p>If the endpoint remains unavailable after the 5-second reconnect window, the adapter closes and must be recreated.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-learn-more">Learn more</h4>
<ul>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a></li>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">Automatic reconnection for streaming</a></li>
<li><a href="/realtime/sfu/get-started/">Get started with Realtime SFU</a></li>
<li><a href="/realtime/sfu/example-architecture/">Realtime SFU example architecture</a></li>
<li><a href="/realtime/sfu/calls-vs-sfus/">Realtime vs Regular SFUs</a></li>
<li><a href="https://realtime-sfu.dev-demos.workers.dev/">Global SFU Network Visualization</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-05-29-security-insights-default-scans"><a href="/changelog/post/2026-05-29-security-insights-default-scans/">Security scans more frequent</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Security Insights scans now run more often. Cloudflare scans Free accounts <strong>every 7 days</strong>, Pro and Business accounts <strong>every 3 days</strong>, and Enterprise accounts <strong>daily</strong>.</p>
<p>In addition, all accounts and zones now receive scans by default. You no longer need to enable scans before Cloudflare checks your account for misconfigurations, vulnerabilities, and other security risks.</p>
<p>Granular on-demand scans are now available on any plan. You can trigger an on-demand scan for any zone, insight, insight type from the Cloudflare dashboard in order to quickly re-check your security posture after remediating an issue.</p>
<p>To learn more, refer to the <a href="/security/security-insights/">Security Insights documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-05-29-warp-macos-beta"><a href="/changelog/post/2026-05-29-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.5.1155.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Administrators can now control which virtual networks (VNETs) are available to which users via WARP device profile settings in the Zero Trust dashboard. Previously, every VNET in the organization was visible to every device; you can now scope the VNET picker per profile so users only see the networks relevant to them. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#vnet-availability">VNET availability</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field, matching what the documentation has always claimed. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks (United inflight Wi-Fi was the reported case). The browser now reliably loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-29">May 29, 2026</time><div>
<h2 id="post-2026-05-29-warp-windows-beta"><a href="/changelog/post/2026-05-29-warp-windows-beta/">Cloudflare One Client for Windows (version 2026.5.1155.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Administrators can now control which virtual networks (VNETs) are available to which users via WARP device profile settings in the Zero Trust dashboard. Previously, every VNET in the organization was visible to every device; you can now scope the VNET picker per profile so users only see the networks relevant to them. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#vnet-availability">VNET availability</a> for details.</li>
<li>Added mandatory authentication. When enabled via MDM, the Cloudflare One Client blocks all Internet traffic from the moment the machine boots until the user authenticates, closing the visibility gap on newly deployed devices and during re-authentication. See the <a href="https://blog.cloudflare.com/mandatory-authentication-mfa/">announcement blog</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-no-auth-no-internet/">documentation</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field, matching what the documentation has always claimed. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>The UseWebView2 registry value (HKLM\SOFTWARE\Cloudflare\CloudflareWARP\UseWebView2 = y) is once again honored by the new GUI for authentication, so administrators who prefer the embedded WebView2 browser for sign-in can opt back in. This setting was effectively ignored in the previous release; the default browser was always used. This key is now also honored for re-authentications.</li>
<li>Fixed a crash in the authentication browser when navigating to a site that prompts for browser permissions (microphone, camera, notifications, etc.). The same fix had previously landed for the captive-portal browser; this extends it to the auth browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of Split Tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
<li>Windows ARM may prompt the user to close running applications while trying to install this version. Simply click “Ok” with the default highlighted option.</li>
<li>DNS resolution may be broken when the following conditions are all true:
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.<br />
To work around this issue, please reconnect the client by selecting &quot;disconnect&quot; and then &quot;connect&quot; in the client user interface.</li>
</ul>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-28-mcp-portal-tool-prompt-aliases"><a href="/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/">Tool and prompt aliases for MCP server portals</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>When you connect third-party MCP servers through <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a>, you have no control over how the server author named tools or wrote descriptions. Unclear names make it harder for AI agents to select the right tool and harder for users to understand what is available.</p>
<p>You can now <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">rename tools and prompts</a> and rewrite their descriptions directly on the portal, without modifying the upstream server. For example, a tool named <code>super_cool_tool</code> can become <code>search_customer_records</code> with a description tailored to your organization.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-edit-tool-modal.png" alt="Edit tool modal showing name and description fields for an MCP server tool" /></p>
<p>Modified tools display a <strong>Modified</strong> label in the tools list so administrators can see which tools have been customized at a glance.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-tools-authorized-modified.png" alt="Tools authorized list showing a modified label on a renamed tool" /></p>
<p>Aliases override the metadata that MCP clients receive. You can set them at two levels:</p>
<ul>
<li><strong>Per portal</strong>: Applies only within a specific portal. Takes precedence over server-level aliases.</li>
<li><strong>Per server</strong>: Applies across all portals that use the server.</li>
</ul>
<p>You can reset an alias at any time to restore the original upstream name.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">Tool and prompt aliases</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-28-use-browser-run-quick-actions-directly-from-workers"><a href="/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/">Use Browser Run Quick Actions directly from Workers</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>You can now call <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a> directly from a <a href="/workers/">Cloudflare Worker</a> using the <code>quickAction()</code> method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.</p>
<p>With the <code>quickAction()</code> method you can:</p>
<ul>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">Capture screenshots</a> from URLs or HTML</li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">Generate PDFs</a> with custom styling, headers, and footers</li>
<li><a href="/browser-run/quick-actions/content-endpoint/">Extract HTML content</a> from fully rendered pages</li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">Convert pages to Markdown</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">Extract structured JSON</a> using AI</li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">Scrape elements</a> with CSS selectors</li>
<li><a href="/browser-run/quick-actions/links-endpoint/">Get all links</a> from a page</li>
<li><a href="/browser-run/quick-actions/snapshot/">Capture snapshots</a> (HTML + screenshot in one request)</li>
</ul>
<p>To get started, add a browser binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17694.md")</div>
<p>Then call any Quick Action directly from your Worker. For example, to capture a screenshot:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17695.md")</div>
<p>The <code>quickAction()</code> method requires a compatibility date of <code>2026-03-24</code> or later.</p>
<p>For setup instructions and the full list of available actions, refer to <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-28-mesh-ha-replica-ui"><a href="/changelog/post/2026-05-28-mesh-ha-replica-ui/">High availability replica management for Cloudflare Mesh</a></h2>
<div class="changelog-badges"><span>mesh</span><span>cloudflare-one</span></div><div class="changelog-body"><p>The <a href="/mesh/">Cloudflare Mesh</a> dashboard now shows per-replica details for <a href="/mesh/features/high-availability/">high availability</a> nodes. You can see which replica is active, view each replica's Mesh IP and connection details, and manually trigger failover — all from the node detail page.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/mesh-ha-replicas.gif" alt="Mesh HA replica tabs showing active and passive replicas with per-replica Mesh IPs and a manual failover option" /></p>
<h4 id="2026-05-28-mesh-ha-replica-ui-what-s-new">What's new</h4>
<ul>
<li><strong>Replica tabs</strong> on the node detail page — switch between replicas to see each one's Mesh IP, edge data center, origin IP, platform, version, and uptime.</li>
<li><strong>Active/passive badges</strong> identify which replica is currently routing traffic.</li>
<li><strong>Manual failover</strong> — promote a passive replica to active with a single click. The previous active replica switches to standby.</li>
<li><strong>HA badge</strong> in the overview table identifies nodes running multiple replicas.</li>
<li><strong>Active replica IP</strong> shown in the overview table — the dashboard now resolves which replica is active and displays the correct Mesh IP.</li>
</ul>
<h4 id="2026-05-28-mesh-ha-replica-ui-manual-failover">Manual failover</h4>
<p>To manually promote a passive replica:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/?to=/:account/mesh">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
<li>Select an HA-enabled node.</li>
<li>Select the passive replica tab.</li>
<li>Select <strong>Promote to active</strong> and confirm.</li>
</ol>
<p>Traffic reroutes to the promoted replica immediately. Refer to <a href="/mesh/features/high-availability/">High availability</a> for details on failover behavior.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-28-ssh-proxy-command"><a href="/changelog/post/2026-05-28-ssh-proxy-command/">Wrangler supports SSH ProxyCommand for Containers</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/workers/wrangler/">Wrangler</a> supports using <code>wrangler containers ssh</code> as an OpenSSH <code>ProxyCommand</code> for <a href="/containers/">Containers</a>. This lets your local SSH client connect to a running Container through Wrangler.</p>
<pre tabindex="0"><code class="language-sh">ssh -o ProxyCommand=&quot;wrangler containers ssh %h&quot; cloudchamber@&lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>When standard input and output are piped, Wrangler forwards data to the SSH server in the Container. You can also pass <code>--stdio</code> to force this mode.</p>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/12/">Previous</a><span>Page 13 of 50</span><a class="pagination-next" rel="next" href="/changelog/14/">Next</a></nav>
</div>
