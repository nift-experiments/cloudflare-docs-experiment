---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers/10/
  description: '2025-03-13'
  full_title: workers changelog - page 10 | Cloudflare Docs
  head_html: <title>workers changelog - page 10 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-03-13"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers/10/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers changelog - page 10"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-03-13"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers/10/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers/10/#page","headline":"workers changelog - page 10 | Cloudflare Docs","description":"2025-03-13","url":"https://developers.cloudflare.com/changelog/product/workers/10/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers/10/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="set-breakpoints-and-debug-your-workers-tests-with-cloudflare-vitest-pool-workers"><a href="/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/">Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers</a></h2>
<p><em>2025-03-13</em></p>
<p>You can now debug your Workers tests with our <a href="/workers/testing/vitest-integration/">Vitest integration</a> by running the following command:</p>
<pre tabindex="0"><code class="language-sh">vitest --inspect --no-file-parallelism&#10;</code></pre>
<p>Attach a debugger to the port 9229 and you can start stepping through your Workers tests. This is available with <code>@cloudflare/vitest-pool-workers</code> v0.7.5 or later.</p>
<p>Learn more in our <a href="/workers/testing/vitest-integration/debugging/">documentation</a>.</p>


<h2 id="access-your-worker-s-environment-variables-from-process-env"><a href="/changelog/post/2025-03-11-process-env-support/">Access your Worker's environment variables from process.env</a></h2>
<p><em>2025-03-11</em></p>
<p>You can now access <a href="/workers/configuration/environment-variables/">environment variables</a> and
<a href="/workers/configuration/secrets/">secrets</a> on <a href="/workers/runtime-apis/nodejs/process/#processenv"><code>process.env</code></a>
when using the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code> compatibility flag</a>.</p>
<pre tabindex="0"><code class="language-js">const apiClient = ApiClient.new({ apiKey: process.env.API_KEY });&#10;const LOG_LEVEL = process.env.LOG_LEVEL || &quot;info&quot;;&#10;</code></pre>
<p>In Node.js, environment variables are exposed via the global <code>process.env</code> object. Some libraries
assume that this object will be populated, and many developers may be used to accessing variables
in this way.</p>
<p>Previously, the <code>process.env</code> object was always empty unless written to in Worker code. This could
cause unexpected errors or friction when developing Workers using code previously written for Node.js.</p>
<p>Now, <a href="/workers/configuration/environment-variables/">environment variables</a>,
<a href="/workers/configuration/secrets/">secrets</a>, and <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata</a>
can all be accessed on <code>process.env</code>.</p>
<p>To opt-in to the new <code>process.env</code> behaviour now, add the <a href="/workers/configuration/compatibility-flags/#enable-auto-populating-processenv"><code>nodejs_compat_populate_process_env</code></a> compatibility flag to your
<code>wrangler.json</code> configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17766.md")</div>
<p>After April 1, 2025, populating <code>process.env</code> will become the default behavior when both <code>nodejs_compat</code> is enabled and
your Worker's <code>compatibility_date</code> is after &quot;2025-04-01&quot;.</p>


<h2 id="use-the-latest-javascript-features-with-wrangler-cli-v4-0-0-rc-0"><a href="/changelog/post/2025-02-28-wrangler-v4-rc/">Use the latest JavaScript features with Wrangler CLI v4.0.0-rc.0</a></h2>
<p><em>2025-02-28</em></p>
<p>We've released a release candidate of the next major version of <a href="/workers/wrangler/">Wrangler</a>, the CLI for Cloudflare Workers — <code>wrangler@4.0.0-rc.0</code>.</p>
<p>You can run the following command to install it and be one of the first to try it out:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Unlike previous major versions of Wrangler, which were <a href="https://blog.cloudflare.com/wrangler-v2-beta/">foundational rewrites</a> and <a href="https://blog.cloudflare.com/wrangler3/">rearchitectures</a> — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change. Before we release Wrangler v4 and advance past the release candidate stage, we'll share a detailed migration guide in the Workers developer docs. But for the vast majority of cases, you won't need to do anything to migrate — things will just work as they do today. We are sharing this release candidate in advance of the official release of v4, so that you can try it out early and share feedback.</p>
<h4 id="2025-02-28-wrangler-v4-rc-new-javascript-language-features-that-you-can-now-use-with-wrangler-v4">New JavaScript language features that you can now use with Wrangler v4</h4>
<p>Version 4 of Wrangler updates the version of <a href="https://esbuild.github.io/">esbuild</a> that Wrangler uses internally, allowing you to use modern JavaScript language features, including:</p>
<h5 id="2025-02-28-wrangler-v4-rc-the-using-keyword-from-explicit-resource-management">The <code>using</code> keyword from Explicit Resource Management</h5>
<p>The <a href="/workers/runtime-apis/rpc/lifecycle/#explicit-resource-management"><code>using</code> keyword from the Explicit Resource Management standard</a> makes it easier to work with the <a href="/workers/runtime-apis/rpc/">JavaScript-native RPC system built into Workers</a>. This means that when you obtain a stub, you can ensure that it is automatically disposed when you exit scope it was created in:</p>
<pre tabindex="0"><code class="language-js">function sendEmail(id, message) {&#10;  using user = await env.USER_SERVICE.findUser(id);&#10;  await user.sendEmail(message);&#10;&#10;  // user[Symbol.dispose]() is implicitly called at the end of the scope.&#10;}&#10;</code></pre>
<h5 id="2025-02-28-wrangler-v4-rc-import-attributes">Import attributes</h5>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with">Import attributes</a> allow you to denote the type or other attributes of the module that your code imports. For example, you can import a JSON module, using the following syntax:</p>
<pre tabindex="0"><code class="language-js">import data from &quot;./data.json&quot; with { type: &quot;json&quot; };&#10;</code></pre>
<h4 id="2025-02-28-wrangler-v4-rc-other-changes">Other changes</h4>
<h5 id="2025-02-28-wrangler-v4-rc-local-is-now-the-default-for-all-cli-commands"><code>--local</code> is now the default for all CLI commands</h5>
<p>All commands that access resources (for example, <code>wrangler kv</code>, <code>wrangler r2</code>, <code>wrangler d1</code>) now access local datastores by default, ensuring consistent behavior.</p>
<h5 id="2025-02-28-wrangler-v4-rc-clearer-policy-for-the-minimum-required-version-of-node-js-required-to-run-wrangler">Clearer policy for the minimum required version of Node.js required to run Wrangler</h5>
<p>Moving forward, the <a href="https://nodejs.org/en/about/previous-releases">active, maintenance, and current versions of Node.js</a> will be officially supported by Wrangler. This means the minimum officially supported version of Node.js you must have installed for Wrangler v4 will be Node.js v18 or later. This policy mirrors how many other packages and CLIs support older versions of Node.js, and ensures that as long as you are using a version of Node.js that the Node.js project itself supports, this will be supported by Wrangler as well.</p>
<h5 id="2025-02-28-wrangler-v4-rc-features-previously-deprecated-in-wrangler-v3-are-now-removed-in-wrangler-v4">Features previously deprecated in Wrangler v3 are now removed in Wrangler v4</h5>
<p>All previously deprecated features in <a href="https://developers.cloudflare.com/workers/wrangler/deprecations/#wrangler-v2">Wrangler v2</a> and in <a href="https://developers.cloudflare.com/workers/wrangler/deprecations/#wrangler-v3">Wrangler v3</a> have now been removed. Additionally, the following features that were deprecated during the Wrangler v3 release have been removed:</p>
<ul>
<li>Legacy Assets (using <code>wrangler dev/deploy --legacy-assets</code> or the <code>legacy_assets</code> config file property). Instead, we recommend you <a href="https://developers.cloudflare.com/workers/static-assets/">migrate to Workers assets</a>.</li>
<li>Legacy Node.js compatibility (using <code>wrangler dev/deploy --node-compat</code> or the <code>node_compat</code> config file property). Instead, use the <a href="https://developers.cloudflare.com/workers/runtime-apis/nodejs"><code>nodejs_compat</code> compatibility flag</a>. This includes the functionality from legacy <code>node_compat</code> polyfills and natively implemented Node.js APIs.</li>
<li><code>wrangler version</code>. Instead, use <code>wrangler --version</code> to check the current version of Wrangler.</li>
<li><code>getBindingsProxy()</code> (via <code>import { getBindingsProxy } from &quot;wrangler&quot;</code>). Instead, use the <a href="https://developers.cloudflare.com/workers/wrangler/api/#getplatformproxy"><code>getPlatformProxy()</code> API</a>, which takes exactly the same arguments.</li>
<li><code>usage_model</code>. This no longer has any effect, after the <a href="https://blog.cloudflare.com/workers-pricing-scale-to-zero/">rollout of Workers Standard Pricing</a>.</li>
</ul>
<p>We'd love your feedback! If you find a bug or hit a roadblock when upgrading to Wrangler v4, <a href="https://github.com/cloudflare/workers-sdk/issues/new?template=bug-template.yaml">open an issue on the <code>cloudflare/workers-sdk</code> repository on GitHub</a>.</p>


<h2 id="introducing-the-agents-sdk"><a href="/changelog/post/2025-02-25-agents-sdk/">Introducing the Agents SDK</a></h2>
<p><em>2025-02-25</em></p>
<p>We've released the <a href="http://blog.cloudflare.com/build-ai-agents-on-cloudflare/">Agents SDK</a>, a package and set of tools that help you build and ship AI Agents.</p>
<p>You can get up and running with a <a href="https://github.com/cloudflare/agents-starter">chat-based AI Agent</a> (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; open up README.md and follow the instructions&#10;</code></pre>
<p>You can also add an Agent to any existing Workers application by installing the <code>agents</code> package directly</p>
<pre tabindex="0"><code class="language-sh">npm i agents&#10;</code></pre>
<p>... and then define your first Agent:</p>
<pre tabindex="0"><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;export class YourAgent extends Agent&lt;Env&gt; {&#10;	// Build it out&#10;	// Access state on this.state or query the Agent&#x27;s database via this.sql&#10;	// Handle WebSocket events with onConnect and onMessage&#10;	// Run tasks on a schedule with this.schedule&#10;	// Call AI models&#10;	// ... and/or call other Agents.&#10;}&#10;</code></pre>
<p>Head over to the <a href="/agents/">Agents documentation</a> to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.</p>


<h2 id="autofix-worker-name-configuration-errors-at-build-time"><a href="/changelog/post/2025-02-20-builds-name-conflict/">Autofix Worker name configuration errors at build time</a></h2>
<p><em>2025-02-20</em></p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/gh-auto-pr-name.png" alt="Auto-fixing Workers Name in Git Repo" /></p>
<p>Small misconfigurations shouldn’t break your deployments. Cloudflare is introducing automatic error detection and fixes in <a href="/workers/ci-cd/builds/">Workers Builds</a>, identifying common issues in your wrangler.toml or wrangler.jsonc and proactively offering fixes, so you spend less time debugging and more time shipping.</p>
<p>Here's how it works:</p>
<ol>
<li>Before running your build, Cloudflare checks your Worker's Wrangler configuration file (wrangler.toml or wrangler.jsonc) for common errors.</li>
<li>Once you submit a build, if Cloudflare finds an error it can fix, it will submit a pull request to your repository that fixes it.</li>
<li>Once you merge this pull request, Cloudflare will run another build.</li>
</ol>
<p>We're starting with fixing name mismatches between your Wrangler file and the Cloudflare dashboard, a top cause of build failures.</p>
<p>This is just the beginning, we want your feedback on what other errors we should catch and fix next. Let us know in the Cloudflare Developers Discord, <a href="https://discord.com/channels/595317990191398933/1064502845061210152">#workers-and-pages-feature-suggestions</a>.</p>


<h2 id="build-ai-agents-with-example-prompts"><a href="/changelog/post/2025-02-14-example-ai-prompts/">Build AI Agents with Example Prompts</a></h2>
<p><em>2025-02-14</em></p>
<p>We've added an <a href="/workers/get-started/prompting/">example prompt</a> to help you get started with building AI agents and applications on Cloudflare <a href="/workers/">Workers</a>, including <a href="/workflows/">Workflows</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/kv/">Workers KV</a>.</p>
<p>You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the <code>&lt;user_prompt&gt;&lt;/user_prompt&gt;</code> tags.</p>
<pre tabindex="0"><code class="language-sh">{paste_prompt_here}&#10;&lt;user_prompt&gt;&#10;user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label &#x27;help&#x27; or &#x27;bug&#x27;, and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.&#10;&lt;/user_prompt&gt;&#10;</code></pre>
<p>This prompt is still experimental, but we encourage you to try it out and <a href="https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml">provide feedback</a>.</p>


<h2 id="create-and-deploy-workers-from-git-repositories"><a href="/changelog/post/2025-02-07-new-ways-to-get-started-on-workers/">Create and deploy Workers from Git repositories</a></h2>
<p><em>2025-02-07 00:00:00 UTC</em></p>
<p><img src="/assets/upstream/images/workers/choose-template-import-repo.png" alt="Import repo or choose template" /></p>
<p>You can now create a Worker by:</p>
<ul>
<li><strong>Importing a Git repository</strong>: Choose an existing Git repo on your GitHub/GitLab account and set up <a href="/workers/ci-cd/builds/configuration/">Workers Builds</a> to deploy your Worker.</li>
<li><strong>Deploying a template with Git</strong>: Choose from a brand new selection of production ready <a href="https://github.com/cloudflare/templates">examples</a> to help you get started with popular frameworks like <a href="https://astro.build/">Astro</a>, <a href="https://remix.run/">Remix</a> and <a href="https://nextjs.org/">Next</a> or build stateful applications with Cloudflare resources like <a href="/d1/">D1 databases</a>, <a href="/workers-ai/">Workers AI</a> or <a href="/durable-objects/">Durable Objects</a>! When you're ready to deploy, Cloudflare will set up your project by cloning the template to your GitHub/GitLab account, provisioning any required <a href="/workers/runtime-apis/bindings/">resources</a> and deploying your Worker.</li>
</ul>
<p>With every push to your chosen branch, Cloudflare will automatically build and deploy your Worker.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create">Workers dashboard</a>.</p>
<p>These new features are available today in the Cloudflare dashboard to a subset of Cloudflare customers, and will be coming to all customers in the next few weeks. Don't see it in your dashboard, but want early access? Add your Cloudflare Account ID to <a href="https://forms.gle/U1qhkF2snNJDGJJa9">this form</a>.</p>


<h2 id="revamped-workers-metrics"><a href="/changelog/post/2025-02-03-workers-metrics-revamp/">Revamped Workers Metrics</a></h2>
<p><em>2025-02-03</em></p>
<p>We've revamped the <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics/">Workers Metrics dashboard</a>.</p>
<p><img src="/assets/upstream/images/workers/observability/workers-metrics.png" alt="Workers Metrics dashboard" /></p>
<p>Now you can easily compare metrics across Worker versions, understand the current state of a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a>, and review key Workers metrics in a single view. This new interface enables you to:</p>
<ul>
<li>Drag-and-select using a graphical timepicker for precise metric selection.</li>
</ul>
<p><img src="/assets/upstream/images/workers/observability/metrics-graphical-timepicker.png" alt="Workers Metrics graphical timepicker" /></p>
<ul>
<li>Use histograms to visualize cumulative metrics, allowing you to bucket and compare rates over time.</li>
<li>Focus on Worker versions by directly interacting with the version numbers in the legend.</li>
</ul>
<p><img src="/assets/upstream/images/workers/observability/metrics-legend-selector.png" alt="Workers Metrics legend selector" /></p>
<ul>
<li>Monitor and compare active gradual deployments.</li>
<li>Track error rates across versions with grouping both by version and by invocation status.</li>
<li>Measure how <a href="/workers/configuration/placement/">Smart Placement</a> improves request duration.</li>
</ul>
<p>Learn more about <a href="/workers/observability/metrics-and-analytics">metrics</a>.</p>


<h2 id="transform-html-quickly-with-streaming-content"><a href="/changelog/post/2025-01-31-html-rewriter-streaming/">Transform HTML quickly with streaming content</a></h2>
<p><em>2025-01-31</em></p>
<p>You can now transform HTML elements with streamed content using <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code></a>.</p>
<p>Methods like <code>replace</code>, <code>append</code>, and <code>prepend</code> now accept <a href="/workers/runtime-apis/response/"><code>Response</code></a> and <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>
values as <a href="/workers/runtime-apis/html-rewriter/#global-types"><code>Content</code></a>.</p>
<p>This can be helpful in a variety of situations. For instance, you may have a Worker in front of an origin,
and want to replace an element with content from a different source. Prior to this change, you would have to load
all of the content from the upstream URL and convert it into a string before replacing the element. This slowed
down overall response times.</p>
<p>Now, you can pass the <code>Response</code> object directly into the <code>replace</code> method, and HTMLRewriter will immediately
start replacing the content as it is streamed in. This makes responses faster.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17765.md")</div>
<p>For more information, see the <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code> documentation</a>.</p>


<h2 id="increased-browser-rendering-limits"><a href="/changelog/post/2025-01-30-browser-rendering-more-instances/">Increased Browser Rendering limits!</a></h2>
<p><em>2025-01-30</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now supports 10 concurrent browser instances per account <em>and</em> 10 new instances per minute, up from the previous limits of 2.</p>
<p>This allows you to launch more browser tasks from <a href="/workers">Cloudflare Workers</a>.</p>
<p>To manage concurrent browser sessions, you can use <a href="/queues/">Queues</a> or <a href="/workflows/">Workflows</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17693.md")</div>


<h2 id="support-for-node-js-dns-net-and-timer-apis-in-workers"><a href="/changelog/post/2025-01-28-nodejs-compat-improvements/">Support for Node.js DNS, Net, and Timer APIs in Workers</a></h2>
<p><em>2025-01-28</em></p>
<p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled, you can now use the following Node.js APIs:</p>
<ul>
<li><a href="/workers/runtime-apis/nodejs/net/"><code>node:net</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/dns/"><code>node:dns</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/timers/"><code>node:timers</code></a></li>
</ul>
<h4 id="2025-01-28-nodejs-compat-improvements-node-net">node:net</h4>
<p>You can use <a href="https://nodejs.org/api/net.html"><code>node:net</code></a> to create a direct connection to servers via a TCP sockets
with <a href="https://nodejs.org/api/net.html#class-netsocket"><code>net.Socket</code></a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17762.md")</div>
<p>Additionally, you can now use other APIs including <a href="https://nodejs.org/api/net.html#class-netblocklist"><code>net.BlockList</code></a> and
<a href="https://nodejs.org/api/net.html#class-netsocketaddress"><code>net.SocketAddress</code></a>.</p>
<p>Note that <a href="https://nodejs.org/api/net.html#class-netserver"><code>net.Server</code></a> is not supported.</p>
<h4 id="2025-01-28-nodejs-compat-improvements-node-dns">node:dns</h4>
<p>You can use <a href="https://nodejs.org/api/dns.html"><code>node:dns</code></a> for name resolution via <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a> using
<a href="https://www.cloudflare.com/application-services/products/dns/">Cloudflare DNS</a> at 1.1.1.1.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17763.md")</div>
<p>All <code>node:dns</code> functions are available, except <code>lookup</code>, <code>lookupService</code>, and <code>resolve</code> which throw &quot;Not implemented&quot; errors when called.</p>
<h4 id="2025-01-28-nodejs-compat-improvements-node-timers">node:timers</h4>
<p>You can use <a href="https://nodejs.org/api/timers.html"><code>node:timers</code></a> to schedule functions to be called at some future period of time.</p>
<p>This includes <a href="https://nodejs.org/api/timers.html#settimeoutcallback-delay-args"><code>setTimeout</code></a> for calling a function after a delay,
<a href="https://nodejs.org/api/timers.html#setintervalcallback-delay-args"><code>setInterval</code></a> for calling a function repeatedly,
and <a href="https://nodejs.org/api/timers.html#setimmediatecallback-args"><code>setImmediate</code></a> for calling a function in the next iteration of the event loop.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17764.md")</div>


<h2 id="faster-workers-builds-with-build-caching-and-watch-paths"><a href="/changelog/post/2024-12-29-faster-builds/">Faster Workers Builds with Build Caching and Watch Paths</a></h2>
<p><em>2024-12-29</em></p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-caching.png" alt="Build caching settings" />
<img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-watch-paths.png" alt="Build watch path settings" /></p>
<p><a href="/workers/ci-cd/builds/"><strong>Workers Builds</strong></a>, the integrated CI/CD system for Workers (currently in beta), now lets you cache artifacts across builds, speeding up build jobs by eliminating repeated work, such as downloading dependencies at the start of each build.</p>
<ul>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-caching/">Build Caching</a></strong>: Cache dependencies and build outputs between builds with a shared project-wide cache, ensuring faster builds for the entire team.</p>
</li>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-watch-paths/">Build Watch Paths</a></strong>: Define paths to include or exclude from the build process, ideal for <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepos</a> to target only the files that need to be rebuilt per Workers project.</p>
</li>
</ul>
<p>To get started, select your Worker on the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> then go to <strong>Settings</strong> &gt; <strong>Builds</strong>, and connect a GitHub or GitLab repository. Once connected, you'll see options to configure Build Caching and Build Watch Paths.</p>


<h2 id="bypass-caching-for-subrequests-made-from-cloudflare-workers-with-request-cache"><a href="/changelog/post/2024-11-11-cache-no-store/">Bypass caching for subrequests made from Cloudflare Workers, with Request.cache</a></h2>
<p><em>2024-11-11</em></p>
<p>You can now use the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface to bypass <a href="/workers/reference/how-the-cache-works/">Cloudflare's cache</a> when making subrequests from <a href="/workers">Cloudflare Workers</a>, by setting its value to <code>no-store</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17761.md")</div>
<p>When you set the value to <code>no-store</code> on a subrequest made from a Worker, the Cloudflare Workers runtime will not check whether a match exists in the cache, and not add the response to the cache, even if the response includes directives in the <code>Cache-Control</code> HTTP header that otherwise indicate that the response is cacheable.</p>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code> property on <code>Request</code>, the Workers runtime threw an exception.</p>
<p>If you've tried to use <code>@planetscale/database</code>, <code>redis-js</code>, <code>stytch-node</code>, <code>supabase</code>, <code>axiom-js</code> or have seen the error message <code>The cache field on RequestInitializerDict is not implemented in fetch</code> — you should try again, making sure that the <a href="/workers/configuration/compatibility-dates/">Compatibility Date</a> of your Worker is set to on or after <code>2024-11-11</code>, or the <a href="/workers/configuration/compatibility-flags/#enable-cache-no-store-http-standard-api"><code>cache_option_enabled</code> compatibility flag</a> is enabled for your Worker.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>


<h2 id="workflows-is-now-in-open-beta"><a href="/changelog/post/2024-10-24-workflows-beta/">Workflows is now in open beta</a></h2>
<p><em>2024-10-24</em></p>
<p>Workflows is now in open beta, and available to any developer a free or paid Workers plan.</p>
<p>Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.</p>
<h4 id="2024-10-24-workflows-beta-get-started">Get started</h4>
<p>You can get started with Workflows by <a href="/workflows/get-started/guide/">following our get started guide</a> and/or using <code>npm create cloudflare</code> to pull down the starter project:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest workflows-starter -- --template &quot;cloudflare/workflows-starter&quot;&#10;</code></pre>
<p>You can open the <code>src/index.ts</code> file, extend it, and use <code>wrangler deploy</code> to deploy your first Workflow. From there, you can:</p>
<ul>
<li>Learn the <a href="/workflows/build/workers-api/">Workflows API</a></li>
<li><a href="/workflows/build/trigger-workflows/">Trigger Workflows</a> via your Workers apps.</li>
<li>Understand the <a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a> and how to adopt best practices</li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/9/">Previous</a><span>Page 10 of 10</span></nav>
