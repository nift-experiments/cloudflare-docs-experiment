---
cp9:
  canonical: https://developers.cloudflare.com/changelog/47/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 47 | Cloudflare Docs
  head_html: <title>Changelog - page 47 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/47/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 47"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/47/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/47/#page","headline":"Changelog - page 47 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/47/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/47/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-02-26">Feb 26, 2025</time><div>
<h2 id="post-2025-02-25-dlp-assist-for-m365"><a href="/changelog/post/2025-02-25-dlp-assist-for-m365/">Use DLP Assist for M365</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Cloudflare Email security customers who have Microsoft 365 environments can quickly deploy an Email DLP (Data Loss Prevention) solution for free.</p>
<p>Simply deploy our add-in, create a DLP policy in Cloudflare, and configure Outlook to trigger behaviors like displaying a banner, alerting end users before sending, or preventing delivery entirely.</p>
<p>Refer to <a href="/cloudflare-one/email-security/outbound-dlp/">Outbound Data Loss Prevention</a> to learn more about this feature.</p>
<p>In GUI alert:</p>
<p><img src="/assets/upstream/images/changelog/email-security/DLP-Alert.png" alt="DLP-Alert" /></p>
<p>Alert before sending:</p>
<p><img src="/assets/upstream/images/changelog/email-security/DLP-Pop-up.png" alt="DLP-Pop-up" /></p>
<p>Prevent delivery:</p>
<p><img src="/assets/upstream/images/changelog/email-security/DLP-Blocked.png" alt="DLP-Blocked" /></p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-25">Feb 25, 2025</time><div>
<h2 id="post-2025-02-25-agents-sdk"><a href="/changelog/post/2025-02-25-agents-sdk/">Introducing the Agents SDK</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We've released the <a href="http://blog.cloudflare.com/build-ai-agents-on-cloudflare/">Agents SDK</a>, a package and set of tools that help you build and ship AI Agents.</p>
<p>You can get up and running with a <a href="https://github.com/cloudflare/agents-starter">chat-based AI Agent</a> (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; open up README.md and follow the instructions&#10;</code></pre>
<p>You can also add an Agent to any existing Workers application by installing the <code>agents</code> package directly</p>
<pre tabindex="0"><code class="language-sh">npm i agents&#10;</code></pre>
<p>... and then define your first Agent:</p>
<pre tabindex="0"><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;export class YourAgent extends Agent&lt;Env&gt; {&#10;	// Build it out&#10;	// Access state on this.state or query the Agent&#x27;s database via this.sql&#10;	// Handle WebSocket events with onConnect and onMessage&#10;	// Run tasks on a schedule with this.schedule&#10;	// Call AI models&#10;	// ... and/or call other Agents.&#10;}&#10;</code></pre>
<p>Head over to the <a href="/agents/">Agents documentation</a> to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-25">Feb 25, 2025</time><div>
<h2 id="post-2025-02-25-json-mode"><a href="/changelog/post/2025-02-25-json-mode/">Workers AI now supports structured JSON outputs.</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Workers AI now supports structured JSON outputs with <a href="/workers-ai/features/json-mode/">JSON mode</a>, which allows you to request a structured output response when interacting with AI models.</p>
<p>This makes it much easier to retrieve structured data from your AI models, and avoids the (error prone!) need to parse large unstructured text responses to extract your data.</p>
<p>JSON mode in Workers AI is compatible with the OpenAI SDK's <a href="https://platform.openai.com/docs/guides/structured-outputs">structured outputs</a> <code>response_format</code> API, which can be used directly in a Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17816.md")</div>
<p>To learn more about JSON mode and structured outputs, visit the <a href="/workers-ai/features/json-mode/">Workers AI documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-25">Feb 25, 2025</time><div>
<h2 id="post-2025-02-25-workflows-concurrency-increased"><a href="/changelog/post/2025-02-25-workflows-concurrency-increased/">Concurrent Workflow instances limits increased.</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> now supports up to 4,500 concurrent (running) instances, up from the previous limit of 100. This limit will continue to increase during the Workflows open beta. This increase applies to all users on the Workers Paid plan, and takes effect immediately.</p>
<p>Review the Workflows <a href="/workflows/reference/limits">limits documentation</a> and/or dive into the <a href="/workflows/get-started/guide/">get started guide</a> to start building on Workflows.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-24">Feb 24, 2025</time><div>
<h2 id="post-2025-02-21-images-bindings-in-workers"><a href="/changelog/post/2025-02-21-images-bindings-in-workers/">Bind the Images API to your Worker</a></h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>You can now <a href="/images/optimization/binding/">interact with the Images API</a> directly in your Worker.</p>
<p>This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.</p>
<p>The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17735.md")</div>
<p>Within your Worker code, you can interact with this binding by using <code>env.IMAGES</code>.</p>
<p>Here's how you can rotate, resize, and blur an image, then output the image as AVIF:</p>
<pre tabindex="0"><code class="language-ts">const info = await env.IMAGES.info(stream);&#10;// stream contains a valid image, and width/height is available on the info object&#10;&#10;const response = (&#10;	await env.IMAGES.input(stream)&#10;		.transform({ rotate: 90 })&#10;		.transform({ width: 128 })&#10;		.transform({ blur: 20 })&#10;		.output({ format: &quot;image/avif&quot; })&#10;).response();&#10;&#10;return response;&#10;</code></pre>
<p>For more information, refer to <a href="/images/optimization/binding/">Images Bindings</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-24">Feb 24, 2025</time><div>
<h2 id="post-2025-02-24-r2-super-slurper-s3-compatible-support"><a href="/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/">Super Slurper now supports migrations from all S3-compatible storage providers</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> can now migrate data from any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>. This includes transfers from services like MinIO, Wasabi, Backblaze B2, and DigitalOcean Spaces.</p>
<p><img src="/assets/upstream/images/changelog/r2/super-slurper-s3-compat-screenshot-border.png" alt="Super Slurper S3-Compatible Source" /></p>
<p>For more information on Super Slurper and how to migrate data from your existing S3-compatible storage buckets to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-24">Feb 24, 2025</time><div>
<h2 id="post-2025-02-24-waf-release"><a href="/changelog/post/2025-02-24-waf-release/">WAF Release - 2025-02-24</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
				<code class="nb-rule-id" title="f7b9d265b86f448989fb0f054916911e">4916911e</code>
</td>
<td>100718A</td>
<td>SonicWall SSLVPN 2 - Auth Bypass - CVE:CVE-2024-53704</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="77c13c611d2a4fa3a89c0fafc382fdec">c382fdec</code>
</td>
<td>100720</td>
<td>Palo Alto Networks - Auth Bypass - CVE:CVE-2025-0108</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-24">Feb 24, 2025</time><div>
<h2 id="post-2025-02-24-context-windows"><a href="/changelog/post/2025-02-24-context-windows/">Workers AI larger context windows</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We've updated the Workers AI text generation models to include context windows and limits definitions and changed our APIs to estimate and validate the number of tokens in the input prompt, not the number of characters.</p>
<p>This update allows developers to use larger context windows when interacting with Workers AI models, which can lead to better and more accurate results.</p>
<p>Our <a href="/workers-ai/models/">catalog page</a> provides more information about each model's supported context window.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-24">Feb 24, 2025</time><div>
<h2 id="post-2025-02-24-zaraz-dash-placement"><a href="/changelog/post/2025-02-24-zaraz-dash-placement/">Zaraz moves to the “Tag Management” category in the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>zaraz</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/zaraz/zaraz-account-level.jpg" alt="Zaraz at zone level to Tag management at account level" /></p>
<p>Previously, you could only configure Zaraz by going to each individual zone under your Cloudflare account. Now, if you’d like to get started with Zaraz or manage your existing configuration, you can navigate to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Management</a> section on the Cloudflare dashboard – this will make it easier to compare and configure the same settings across multiple zones.</p>
<p>These changes will not alter any existing configuration or entitlements for zones you already have Zaraz enabled on. If you’d like to edit existing configurations, you can go to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Setup</a> section of the dashboard, and select the zone you'd like to edit.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-21">Feb 21, 2025</time><div>
<h2 id="post-2025-02-20-synchronous-uploads"><a href="/changelog/post/2025-02-20-synchronous-uploads/">Workers for Platforms - Instant dispatch for newly created User Workers</a></h2>
<div class="changelog-badges"><span>workers-for-platforms</span></div><div class="changelog-body"><p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/">Workers for Platforms</a> is an architecture wherein a centralized <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dispatch Worker</a> processes incoming requests and routes them to isolated sub-Workers, called <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">User Workers</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers-for-platforms/wfp-request.png" alt="Workers for Platforms Requests" /></p>
<p>Previously, when a new User Worker was uploaded, there was a short delay before it became available for dispatch. This meant that even though an API request could return a 200 OK response, the script might not yet be ready to handle requests, causing unexpected failures for platforms that immediately dispatch to new Workers.</p>
<p><strong>With this update, first-time uploads of User Workers are now deployed synchronously</strong>. A 200 OK response guarantees the script is fully provisioned and ready to handle traffic immediately, ensuring more predictable deployments and reducing errors.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-20">Feb 20, 2025</time><div>
<h2 id="post-2025-02-20-builds-name-conflict"><a href="/changelog/post/2025-02-20-builds-name-conflict/">Autofix Worker name configuration errors at build time</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/platform/ci-cd/gh-auto-pr-name.png" alt="Auto-fixing Workers Name in Git Repo" /></p>
<p>Small misconfigurations shouldn’t break your deployments. Cloudflare is introducing automatic error detection and fixes in <a href="/workers/ci-cd/builds/">Workers Builds</a>, identifying common issues in your wrangler.toml or wrangler.jsonc and proactively offering fixes, so you spend less time debugging and more time shipping.</p>
<p>Here's how it works:</p>
<ol>
<li>Before running your build, Cloudflare checks your Worker's Wrangler configuration file (wrangler.toml or wrangler.jsonc) for common errors.</li>
<li>Once you submit a build, if Cloudflare finds an error it can fix, it will submit a pull request to your repository that fixes it.</li>
<li>Once you merge this pull request, Cloudflare will run another build.</li>
</ol>
<p>We're starting with fixing name mismatches between your Wrangler file and the Cloudflare dashboard, a top cause of build failures.</p>
<p>This is just the beginning, we want your feedback on what other errors we should catch and fix next. Let us know in the Cloudflare Developers Discord, <a href="https://discord.com/channels/595317990191398933/1064502845061210152">#workers-and-pages-feature-suggestions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-20">Feb 20, 2025</time><div>
<h2 id="post-2025-02-20-updated-pricing-docs"><a href="/changelog/post/2025-02-20-updated-pricing-docs/">Workers AI updated pricing</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We've updated the Workers AI <a href="/workers-ai/platform/pricing/">pricing</a> to include the latest models and how model usage maps to Neurons.</p>
<ul>
<li>Each model's core input format(s) (tokens, audio seconds, images, etc) now include mappings to Neurons, making it easier to understand how your included Neuron volume is consumed and how you are charged at scale</li>
<li>Per-model pricing, instead of the previous bucket approach, allows us to be more flexible on how models are charged based on their size, performance and capabilities. As we optimize each model, we can then pass on savings for that model.</li>
<li>You will still only pay for what you consume: Workers AI inference is serverless, and not billed by the hour.</li>
</ul>
<p>Going forward, models will be launched with their associated Neuron costs, and we'll be updating the Workers AI dashboard and API to reflect consumption in both raw units and Neurons. Visit the <a href="/workers-ai/platform/pricing/">Workers AI pricing</a> page to learn more about Workers AI pricing.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-18">Feb 18, 2025</time><div>
<h2 id="post-2025-02-18-waf-release"><a href="/changelog/post/2025-02-18-waf-release/">WAF Release - 2025-02-18</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
				<code class="nb-rule-id" title="d1d45e4f59014f0fb22e0e6aa2ffa4b8">a2ffa4b8</code>
</td>
<td>100715</td>
<td>FortiOS - Auth Bypass - CVE:CVE-2024-55591</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="14b5cdeb4cde490ba37d83555a883e12">5a883e12</code>
</td>
<td>100716</td>
<td>Ivanti - Auth Bypass - CVE:CVE-2021-44529</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="498fcd81a62a4b5ca943e2de958094d3">958094d3</code>
</td>
<td>100717</td>
<td>SimpleHelp - Auth Bypass - CVE:CVE-2024-57727</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6e0d8afc36ba4ce9836f81e63b66df22">3b66df22</code>
</td>
<td>100718</td>
<td>SonicWall SSLVPN - Auth Bypass - CVE:CVE-2024-53704</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8eb4536dba1a4da58fbf81c79184699f">9184699f</code>
</td>
<td>100719</td>
<td>Yeti Platform - Auth Bypass - CVE:CVE-2024-46507</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-14">Feb 14, 2025</time><div>
<h2 id="post-2025-02-14-customize-queue-retention-period"><a href="/changelog/post/2025-02-14-customize-queue-retention-period/">Customize queue message retention periods</a></h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p>You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.</p>
<p><img src="/assets/upstream/images/queues/customize-retention-period.png" alt="Customize a queue's message retention period" /></p>
<p>You can customize the retention period on the settings page for your queue, or using Wrangler:</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues update my-queue --message-retention-period-secs 600&#10;</code></pre>
<p>This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-14">Feb 14, 2025</time><div>
<h2 id="post-2025-02-14-example-ai-prompts"><a href="/changelog/post/2025-02-14-example-ai-prompts/">Build AI Agents with Example Prompts</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span><span>workflows</span></div><div class="changelog-body"><p>We've added an <a href="/workers/get-started/prompting/">example prompt</a> to help you get started with building AI agents and applications on Cloudflare <a href="/workers/">Workers</a>, including <a href="/workflows/">Workflows</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/kv/">Workers KV</a>.</p>
<p>You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the <code>&lt;user_prompt&gt;&lt;/user_prompt&gt;</code> tags.</p>
<pre tabindex="0"><code class="language-sh">{paste_prompt_here}&#10;&lt;user_prompt&gt;&#10;user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label &#x27;help&#x27; or &#x27;bug&#x27;, and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.&#10;&lt;/user_prompt&gt;&#10;</code></pre>
<p>This prompt is still experimental, but we encourage you to try it out and <a href="https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml">provide feedback</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-14">Feb 14, 2025</time><div>
<h2 id="post-2025-02-14-local-console-access"><a href="/changelog/post/2025-02-14-local-console-access/">Configure your Magic WAN Connector to connect via static IP assignment</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>You can now locally configure your <a href="/cloudflare-wan/configuration/appliance/">Magic WAN Connector</a> to work in a static IP configuration.</p>
<p>This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.</p>
<p>For more details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console">WAN with a static IP address</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-14">Feb 14, 2025</time><div>
<h2 id="post-2025-02-14-r2-super-slurper-faster-migrations"><a href="/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/">Super Slurper now transfers data to R2 up to 5x faster</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to <a href="/r2/">Cloudflare R2</a> up to 5x faster than it did before.</p>
<p>We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using <a href="/workers/">Cloudflare Workers</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/queues/">Queues</a> — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)</p>
<p><img src="/assets/upstream/images/r2/slurper-objects-over-time-border.png" alt="Super Slurper Objects Migrated" /></p>
<p><em>Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)</em></p>
<p>For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-14">Feb 14, 2025</time><div>
<h2 id="post-2025-02-14-cert-bundling-for-custom-hostnames"><a href="/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/">Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname</a></h2>
<div class="changelog-badges"><span>ssl</span></div><div class="changelog-body"><p>Cloudflare has supported both RSA and ECDSA certificates across our platform for a number of years. Both certificates offer the same security, but ECDSA is more performant due to a smaller key size. However, RSA is more widely adopted and ensures compatibility with legacy clients. Instead of choosing between them, you may want both – that way, ECDSA is used when clients support it, but RSA is available if not.</p>
<p>Now, you can upload both an RSA and ECDSA certificate on a custom hostname via the API.</p>
<pre tabindex="0"><code>curl -X POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;d &#x27;{&#10;    &quot;hostname&quot;: &quot;hostname&quot;,&#10;    &quot;ssl&quot;: {&#10;        &quot;custom_cert_bundle&quot;: [&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;RSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;RSA Key&quot;&#10;            },&#10;            {&#10;                &quot;custom_certificate&quot;: &quot;ECDSA Cert&quot;,&#10;                &quot;custom_key&quot;: &quot;ECDSA Key&quot;&#10;            }&#10;        ],&#10;        &quot;bundle_method&quot;: &quot;force&quot;,&#10;        &quot;wildcard&quot;: false,&#10;        &quot;settings&quot;: {&#10;            &quot;min_tls_version&quot;: &quot;1.0&quot;&#10;        }&#10;    }&#10;}’&#10;</code></pre>
<p>You can also:</p>
<ul>
<li>
<p><a href="/api/resources/custom_hostnames/methods/create/">Upload</a> an RSA or ECDSA certificate to a custom hostname with an existing ECDSA or RSA certificate, respectively.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/">Replace</a> the RSA or ECDSA certificate with a certificate of its same type.</p>
</li>
<li>
<p><a href="/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/">Delete</a> the RSA or ECDSA certificate (if the custom hostname has both an RSA and ECDSA uploaded).</p>
</li>
</ul>
<p>This feature is available for Business and Enterprise customers who have purchased custom certificates.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-14">Feb 14, 2025</time><div>
<h2 id="post-2025-02-14-introducing-dvr-for-stream-live"><a href="/changelog/post/2025-02-14-introducing-dvr-for-stream-live/">Rewind, Replay, Resume: Introducing DVR for Stream Live</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>Previously, all viewers watched &quot;the live edge,&quot; or the latest content of the
broadcast, synchronously. If a viewer paused for more than a few seconds,
the player would automatically &quot;catch up&quot; when playback started again. Seeking
through the broadcast was only available once the recording was available after
it concluded.</p>
<p>Starting today, customers can make a small adjustment to the player
embed or manifest URL to enable the DVR experience for their viewers. By
offering this feature as an opt-in adjustment, our customers are empowered to
pick the best experiences for their applications.</p>
<p>When building a player embed code or manifest URL, just add <code>dvrEnabled=true</code> as
a query parameter. There are some things to be aware of when using this option.
For more information, refer to <a href="/stream/stream-live/dvr-for-live/">DVR for Live</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-12">Feb 12, 2025</time><div>
<h2 id="post-2025-02-12-configurable-multiplexing-http2-to-origin"><a href="/changelog/post/2025-02-12-configurable-multiplexing-http2-to-origin/">Configurable multiplexing HTTP/2 to Origin</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now configure HTTP/2 multiplexing settings for origin connections on Enterprise plans. This feature allows you to optimize how Cloudflare manages concurrent requests over HTTP/2 connections to your origin servers, improving cache efficiency and reducing connection overhead.</p>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-how-it-works">How it works</h4>
<p>HTTP/2 multiplexing allows multiple requests to be sent over a single TCP connection. With this configuration option, you can:</p>
<ol>
<li><strong>Control concurrent streams</strong>: Adjust the maximum number of concurrent streams per connection.</li>
<li><strong>Optimize connection reuse</strong>: Fine-tune connection pooling behavior for your origin infrastructure.</li>
<li><strong>Reduce connection overhead</strong>: Minimize the number of TCP connections required between Cloudflare and your origin.</li>
<li><strong>Improve cache performance</strong>: Better connection management can enhance cache fetch efficiency.</li>
</ol>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-benefits">Benefits</h4>
<ul>
<li><strong>Customizable performance</strong>: Tailor multiplexing settings to your origin's capabilities.</li>
<li><strong>Reduced latency</strong>: Fewer connection handshakes improve response times.</li>
<li><strong>Lower origin load</strong>: More efficient connection usage reduces server resource consumption.</li>
<li><strong>Enhanced scalability</strong>: Better connection management supports higher traffic volumes.</li>
</ul>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-get-started">Get started</h4>
<p>Enterprise customers can configure HTTP/2 multiplexing settings in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> or through our <a href="/api/">API</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-configurable-multiplexing-http2-to-origin-important-consideration">Important consideration</h4>
@markup("md", "content/.markup/bodies/17703.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-12">Feb 12, 2025</time><div>
<h2 id="post-2025-02-12-rules-upgraded-limits"><a href="/changelog/post/2025-02-12-rules-upgraded-limits/">Increased Cloudflare Rules limits</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>We have upgraded and streamlined <a href="/rules/">Cloudflare Rules</a> limits across all plans, simplifying rule management and improving scalability for everyone.</p>
<p><strong>New limits by product:</strong></p>
<ul>
<li><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>
<ul>
<li>Free: <strong>20</strong> → <strong>10,000</strong> URL redirects across lists</li>
<li>Pro: <strong>500</strong> → <strong>25,000</strong> URL redirects across lists</li>
<li>Business: <strong>500</strong> → <strong>50,000</strong> URL redirects across lists</li>
<li>Enterprise: <strong>10,000</strong> → <strong>1,000,000</strong> URL redirects across lists</li>
</ul>
</li>
<li><a href="/rules/cloud-connector/">Cloud Connector</a>
<ul>
<li>Free: <strong>5</strong> → <strong>10</strong> connectors</li>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> connectors</li>
</ul>
</li>
<li><a href="/rules/custom-errors/">Custom Errors</a>
<ul>
<li>Pro: <strong>5</strong> → <strong>25</strong> error assets and rules</li>
<li>Business: <strong>20</strong> → <strong>50</strong> error assets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> error assets and rules</li>
</ul>
</li>
<li><a href="/rules/snippets/">Snippets</a>
<ul>
<li>Pro: <strong>10</strong> → <strong>25</strong> code snippets and rules</li>
<li>Business: <strong>25</strong> → <strong>50</strong> code snippets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> code snippets and rules</li>
</ul>
</li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a>, <a href="/rules/configuration-rules/">Configuration Rules</a>, <a href="/rules/compression-rules/">Compression Rules</a>, <a href="/rules/origin-rules/">Origin Rules</a>, <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>, and <a href="/rules/transform/">Transform Rules</a>
<ul>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> rules</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-rules-upgraded-limits-gradual-rollout">Gradual rollout</h4>
@markup("md", "content/.markup/bodies/17745.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-11">Feb 11, 2025</time><div>
<h2 id="post-2025-02-11-custom-errors-beta"><a href="/changelog/post/2025-02-11-custom-errors-beta/">Custom Errors (beta): Stored Assets &amp; Account-level Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>We're introducing <a href="/rules/custom-errors/">Custom Errors</a> (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.</p>
<p>This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.</p>
<p>This brings the following new capabilities:</p>
<ul>
<li><strong>Custom error assets</strong> – Fetch and store external error pages at the edge for use in error responses.</li>
<li><strong>Account-Level custom errors</strong> – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.</li>
</ul>
<p>You can use Cloudflare API to upload your existing assets for use with Custom Errors:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;maintenance&quot;,&#10;  &quot;description&quot;: &quot;Maintenance template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<p>You can then reference the stored asset in a Custom Error rule:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;rules&quot;: [&#10;		{&#10;			&quot;action&quot;: &quot;serve_error&quot;,&#10;			&quot;action_parameters&quot;: {&#10;				&quot;asset_name&quot;: &quot;maintenance&quot;,&#10;				&quot;content_type&quot;: &quot;text/html&quot;,&#10;				&quot;status_code&quot;: 503&#10;			},&#10;			&quot;enabled&quot;: true,&#10;			&quot;expression&quot;: &quot;http.request.uri.path contains \&quot;error\&quot;&quot;&#10;		}&#10;	]&#10;}&#x27;&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-11">Feb 11, 2025</time><div>
<h2 id="post-2025-02-11-waf-release"><a href="/changelog/post/2025-02-11-waf-release/">WAF Release - 2025-02-11</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
				<code class="nb-rule-id" title="742306889c2e4f6087de6646483b4c26">483b4c26</code>
</td>
<td>100708</td>
<td>Aviatrix Network - Remote Code Execution - CVE:CVE-2024-50603</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="042228dffe0a4f1587da0e737e924ca3">7e924ca3</code>
</td>
<td>100709</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2024-46982</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2a12278325464d6682afb53483a7d8ff">83a7d8ff</code>
</td>
<td>100710</td>
<td>
				Progress Software WhatsUp Gold - Directory Traversal -
				CVE:CVE-2024-12105
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="82ce3424fbe84e9e99d77332baa8eb34">baa8eb34</code>
</td>
<td>100711</td>
<td>WordPress - Remote Code Execution - CVE:CVE-2024-56064</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5afacd39dcfd42f89a6c43f787f5d34e">87f5d34e</code>
</td>
<td>100712</td>
<td>WordPress - Remote Code Execution - CVE:CVE-2024-9047</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="05842b06f0a4415880b58f7fbf72cf8a">bf72cf8a</code>
</td>
<td>100713</td>
<td>FortiOS - Auth Bypass - CVE:CVE-2022-40684</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-08">Feb 8, 2025</time><div>
<h2 id="post-2025-02-07-open-links-security-center"><a href="/changelog/post/2025-02-07-open-links-security-center/">Open email links with Security Center</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now investigate links in emails with Cloudflare Security Center to generate a report containing a myriad of technical details: a phishing scan, SSL certificate data, HTTP request and response data, page performance data, DNS records, what technologies and libraries the page uses, and more.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Open-Links-Security-Center.png" alt="Open links in Security Center" /></p>
<p>From <strong>Investigation</strong>, go to <strong>View details</strong>, and look for the <strong>Links identified</strong> section. Select <strong>Open in Security Center</strong> next to each link. <strong>Open in Security Center</strong> allows your team to quickly generate a detailed report about the link with no risk to the analyst or your environment.</p>
<p>For more details, refer to <a href="/cloudflare-one/email-security/investigation/search-email/#open-links">Open links</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-07">Feb 7, 2025</time><div>
<h2 id="post-2025-02-07-new-ways-to-get-started-on-workers"><a href="/changelog/post/2025-02-07-new-ways-to-get-started-on-workers/">Create and deploy Workers from Git repositories</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/choose-template-import-repo.png" alt="Import repo or choose template" /></p>
<p>You can now create a Worker by:</p>
<ul>
<li><strong>Importing a Git repository</strong>: Choose an existing Git repo on your GitHub/GitLab account and set up <a href="/workers/ci-cd/builds/configuration/">Workers Builds</a> to deploy your Worker.</li>
<li><strong>Deploying a template with Git</strong>: Choose from a brand new selection of production ready <a href="https://github.com/cloudflare/templates">examples</a> to help you get started with popular frameworks like <a href="https://astro.build/">Astro</a>, <a href="https://remix.run/">Remix</a> and <a href="https://nextjs.org/">Next</a> or build stateful applications with Cloudflare resources like <a href="/d1/">D1 databases</a>, <a href="/workers-ai/">Workers AI</a> or <a href="/durable-objects/">Durable Objects</a>! When you're ready to deploy, Cloudflare will set up your project by cloning the template to your GitHub/GitLab account, provisioning any required <a href="/workers/runtime-apis/bindings/">resources</a> and deploying your Worker.</li>
</ul>
<p>With every push to your chosen branch, Cloudflare will automatically build and deploy your Worker.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create">Workers dashboard</a>.</p>
<p>These new features are available today in the Cloudflare dashboard to a subset of Cloudflare customers, and will be coming to all customers in the next few weeks. Don't see it in your dashboard, but want early access? Add your Cloudflare Account ID to <a href="https://forms.gle/U1qhkF2snNJDGJJa9">this form</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/46/">Previous</a><span>Page 47 of 50</span><a class="pagination-next" rel="next" href="/changelog/48/">Next</a></nav>
</div>
