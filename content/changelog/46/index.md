---
cp9:
  canonical: https://developers.cloudflare.com/changelog/46/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 46 | Cloudflare Docs
  head_html: <title>Changelog - page 46 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/46/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 46"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/46/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/46/#page","headline":"Changelog - page 46 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/46/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/46/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-03-17">Mar 17, 2025</time><div>
<h2 id="post-2025-03-17-importable-env"><a href="/changelog/post/2025-03-17-importable-env/">Import `env` to access bindings in your Worker's global scope</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now access <a href="/workers/runtime-apis/bindings/">bindings</a>
from anywhere in your Worker by importing the <code>env</code> object from <code>cloudflare:workers</code>.</p>
<p>Previously, <code>env</code> could only be accessed during a request. This meant that
bindings could not be used in the top-level context of a Worker.</p>
<p>Now, you can import <code>env</code> and access bindings such as <a href="/workers/configuration/secrets/">secrets</a>
or <a href="/workers/configuration/environment-variables/">environment variables</a> in the
initial setup for your Worker:</p>
<pre tabindex="0"><code class="language-js">import { env } from &quot;cloudflare:workers&quot;;&#10;import ApiClient from &quot;example-api-client&quot;;&#10;&#10;// API_KEY and LOG_LEVEL now usable in top-level scope&#10;const apiClient = ApiClient.new({ apiKey: env.API_KEY });&#10;const LOG_LEVEL = env.LOG_LEVEL || &quot;info&quot;;&#10;&#10;export default {&#10;	fetch(req) {&#10;		// you can use apiClient or LOG_LEVEL, configured before any request is handled&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17767.md")</aside>
<p>Additionally, <code>env</code> was normally accessed as a argument to a Worker's entrypoint handler,
such as <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a>.
This meant that if you needed to access a binding from a deeply nested function,
you had to pass <code>env</code> as an argument through many functions to get it to the
right spot. This could be cumbersome in complex codebases.</p>
<p>Now, you can access the bindings from anywhere in your codebase
without passing <code>env</code> as an argument:</p>
<pre tabindex="0"><code class="language-js">// helpers.js&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;// env is *not* an argument to this function&#10;export async function getValue(key) {&#10;	let prefix = env.KV_PREFIX;&#10;	return await env.KV.get(`${prefix}-${key}`);&#10;}&#10;</code></pre>
<p>For more information, see <a href="/workers/runtime-apis/bindings#how-to-access-env">documentation on accessing <code>env</code></a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-17">Mar 17, 2025</time><div>
<h2 id="post-2025-03-17-rerun-build"><a href="/changelog/post/2025-03-17-rerun-build/">Retry Pages &amp; Workers Builds Directly from GitHub</a></h2>
<div class="changelog-badges"><span>workers</span><span>pages</span></div><div class="changelog-body"><p>You can now retry your Cloudflare Pages and Workers builds directly from GitHub. No need to switch to the Cloudflare Dashboard for a simple retry!</p>
<p>Let\u2019s say you push a commit, but your build fails due to a spurious error like a network timeout. Instead of going to the Cloudflare Dashboard to manually retry, you can now rerun the build with just a few clicks inside GitHub, keeping you inside your workflow.</p>
<p>For Pages and Workers projects connected to a GitHub repository:</p>
<ol>
<li>When a build fails, go to your GitHub repository or pull request</li>
<li>Select the failed Check Run for the build</li>
<li>Select &quot;Details&quot; on the Check Run</li>
<li>Select &quot;Rerun&quot; to trigger a retry build for that commit</li>
</ol>
<p>Learn more about <a href="/pages/configuration/git-integration/github-integration/">Pages Builds</a> and <a href="/workers/ci-cd/builds/git-integration/github-integration/">Workers Builds</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-17">Mar 17, 2025</time><div>
<h2 id="post-2025-03-17-new-workers-ai-models"><a href="/changelog/post/2025-03-17-new-workers-ai-models/">New models in Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Workers AI is excited to add 4 new models to the catalog, including 2 brand new classes of models with a text-to-speech and reranker model. Introducing:</p>
<ul>
<li><a href="/workers-ai/models/bge-m3/">@cf/baai/bge-m3</a> - a multi-lingual embeddings model that supports over 100 languages. It can also simultaneously perform dense retrieval, multi-vector retrieval, and sparse retrieval, with the ability to process inputs of different granularities.</li>
<li><a href="/workers-ai/models/bge-reranker-base/">@cf/baai/bge-reranker-base</a> - our first reranker model! Rerankers are a type of text classification model that takes a query and context, and outputs a similarity score between the two. When used in RAG systems, you can use a reranker after the initial vector search to find the most relevant documents to return to a user by reranking the outputs.</li>
<li><a href="/workers-ai/models/whisper-large-v3-turbo/">@cf/openai/whisper-large-v3-turbo</a> - a faster, more accurate speech-to-text model. This model was added earlier but is graduating out of beta with pricing included today.</li>
<li><a href="/workers-ai/models/melotts/">@cf/myshell-ai/melotts</a> - our first text-to-speech model that allows users to generate an MP3 with voice audio from inputted text.</li>
</ul>
<p>Pricing is available for each of these models on the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<p>This docs update includes a few minor bug fixes to the model schema for llama-guard, llama-3.2-1b, which you can review on the <a href="/workers-ai/changelog/">product changelog</a>.</p>
<p>Try it out and let us know what you think! Stay tuned for more models in the coming days.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-13">Mar 13, 2025</time><div>
<h2 id="post-2025-03-13-new-managed-iplist"><a href="/changelog/post/2025-03-13-new-managed-iplist/">Cloudflare IP Ranges List</a></h2>
<div class="changelog-badges"><span>cloudflare-network-firewall</span></div><div class="changelog-body"><p>Magic Firewall now supports a new managed list of Cloudflare IP ranges. This list is available as an option when creating a Magic Firewall policy based on IP source/destination addresses. When selecting &quot;is in list&quot; or &quot;is not in list&quot;, the option &quot;<strong>Cloudflare IP Ranges</strong>&quot; will appear in the dropdown menu.</p>
<p>This list is based on the IPs listed in the Cloudflare <a href="https://www.cloudflare.com/en-gb/ips/">IP ranges</a>.
Updates to this managed list are applied automatically.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-network-firewall/cloudflare-ips.png" alt="Cloudflare IPs Managed List" /></p>
<p>Note: IP Lists require a Cloudflare Advanced Network Firewall subscription. For more details about Cloudflare Network Firewall plans, refer to <a href="/cloudflare-network-firewall/plans">Plans</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-13">Mar 13, 2025</time><div>
<h2 id="post-2025-03-13-wrangler-v4"><a href="/changelog/post/2025-03-13-wrangler-v4/">Use the latest JavaScript features with Wrangler CLI v4</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've released the next major version of <a href="/workers/wrangler/">Wrangler</a>, the CLI for Cloudflare Workers — <code>wrangler@4.0.0</code>. Wrangler v4 is a major release focused on updates to underlying systems and dependencies, along with improvements to keep Wrangler commands consistent and clear.</p>
<p>You can run the following command to install it in your projects:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Unlike previous major versions of Wrangler, which were <a href="https://blog.cloudflare.com/wrangler-v2-beta/">foundational rewrites</a> and <a href="https://blog.cloudflare.com/wrangler3/">rearchitectures</a> — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change.</p>
<p>A <a href="/workers/wrangler/migration/update-v3-to-v4">detailed migration guide</a> is available and if you find a bug or hit a roadblock when upgrading to Wrangler v4, <a href="https://github.com/cloudflare/workers-sdk/issues/new?template=bug-template.yaml">open an issue on the <code>cloudflare/workers-sdk</code> repository on GitHub</a>.</p>
<p>Going forward, we'll continue supporting Wrangler v3 with bug fixes and security updates until Q1 2026, and with critical security updates until Q1 2027, at which point it will be out of support.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-13">Mar 13, 2025</time><div>
<h2 id="post-2025-03-14-breakpoint-debugging-with-vitest"><a href="/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/">Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now debug your Workers tests with our <a href="/workers/testing/vitest-integration/">Vitest integration</a> by running the following command:</p>
<pre tabindex="0"><code class="language-sh">vitest --inspect --no-file-parallelism&#10;</code></pre>
<p>Attach a debugger to the port 9229 and you can start stepping through your Workers tests. This is available with <code>@cloudflare/vitest-pool-workers</code> v0.7.5 or later.</p>
<p>Learn more in our <a href="/workers/testing/vitest-integration/debugging/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-12">Mar 12, 2025</time><div>
<h2 id="post-2025-03-12-reply-limits"><a href="/changelog/post/2025-03-12-reply-limits/">Threaded replies now possible in Email Workers</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>We’re removing some of the restrictions in Email Routing so that AI Agents and task automation can better handle email workflows, including how Workers can <a href="/email-service/api/route-emails/email-handler/#reply-to-emails">reply</a> to incoming emails.</p>
<p>It's now possible to keep a threaded email conversation with an <a href="/email-service/api/route-emails/email-handler/">Email Worker</a> script as long as:</p>
<ul>
<li>The incoming email has to have valid <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>.</li>
<li>The email can only be replied to once in the same <code>EmailMessage</code> event.</li>
<li>The recipient in the reply must match the incoming sender.</li>
<li>The outgoing sender domain must match the same domain that received the email.</li>
<li>Every time an email passes through Email Routing or another MTA, an entry is added to the <code>References</code> list. We stop accepting replies to emails with more than 100 <code>References</code> entries to prevent abuse or accidental loops.</li>
</ul>
<p>Here's an example of a Worker responding to Emails using a Workers AI model:</p>
<pre tabindex="0"><code class="language-ts">import PostalMime from &quot;postal-mime&quot;;&#10;import { createMimeMessage } from &quot;mimetext&quot;;&#10;import { EmailMessage } from &quot;cloudflare:email&quot;;&#10;&#10;export default {&#10;	async email(message, env, ctx) {&#10;		const email = await PostalMime.parse(message.raw);&#10;		const res = await env.AI.run(&quot;@cf/meta/llama-2-7b-chat-fp16&quot;, {&#10;			messages: [&#10;				{&#10;					role: &quot;user&quot;,&#10;					content: email.text ?? &quot;&quot;,&#10;				},&#10;			],&#10;		});&#10;&#10;		// message-id is generated by mimetext&#10;		const response = createMimeMessage();&#10;		response.setHeader(&quot;In-Reply-To&quot;, message.headers.get(&quot;Message-ID&quot;)!);&#10;		response.setSender(&quot;agent@example.com&quot;);&#10;		response.setRecipient(message.from);&#10;		response.setSubject(&quot;Llama response&quot;);&#10;		response.addMessage({&#10;			contentType: &quot;text/plain&quot;,&#10;			data:&#10;				res instanceof ReadableStream&#10;					? await new Response(res).text()&#10;					: res.response!,&#10;		});&#10;&#10;		const replyMessage = new EmailMessage(&#10;			&quot;&lt;email&gt;&quot;,&#10;			message.from,&#10;			response.asRaw(),&#10;		);&#10;		await message.reply(replyMessage);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>See <a href="/email-service/api/route-emails/email-handler/#reply-to-emails">Reply to emails from Workers</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-11">Mar 11, 2025</time><div>
<h2 id="post-2025-03-11-emergency-waf-release"><a href="/changelog/post/2025-03-11-emergency-waf-release/">WAF Release - 2025-03-11 - Emergency</a></h2>
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
				<code class="nb-rule-id" title="0823d16dd8b94cc6b27a9ab173febb31">73febb31</code>
</td>
<td>100731</td>
<td>Apache Camel - Code Injection - CVE:CVE-2025-27636</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-11">Mar 11, 2025</time><div>
<h2 id="post-2025-03-11-process-env-support"><a href="/changelog/post/2025-03-11-process-env-support/">Access your Worker's environment variables from process.env</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now access <a href="/workers/configuration/environment-variables/">environment variables</a> and
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-10">Mar 10, 2025</time><div>
<h2 id="post-2025-03-10-waf-release"><a href="/changelog/post/2025-03-10-waf-release/">WAF Release - 2025-03-10</a></h2>
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
				<code class="nb-rule-id" title="d4f68c1c65c448e58fe4830eb2a51e3d">b2a51e3d</code>
</td>
<td>100722</td>
<td>Ivanti - Information Disclosure - CVE:CVE-2025-0282</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fda130e396224ffc9f0a9e72259073d5">259073d5</code>
</td>
<td>100723</td>
<td>Cisco IOS XE - Information Disclosure - CVE:CVE-2023-20198</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-07">Mar 7, 2025</time><div>
<h2 id="post-2025-03-07-cloudflare-one-device-health-monitoring"><a href="/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/">Cloudflare One Agent now supports Endpoint Monitoring</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment. The latest release of the Cloudflare One agent (v2025.1.861) now includes device endpoint monitoring capabilities
to provide deeper visibility into end-user device performance which can be analyzed directly from the dashboard.</p>
<p>Device health metrics are now automatically collected, allowing administrators to:</p>
<ul>
<li>View the last network a user was connected to</li>
<li>Monitor CPU and RAM utilization on devices</li>
<li>Identify resource-intensive processes running on endpoints</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/cloudflare-one-agent-health-monitoring.gif" alt="Device endpoint monitoring dashboard" /></p>
<p>This feature complements existing DEX features like <a href="/cloudflare-one/insights/dex/tests/">synthetic application monitoring</a> and <a href="/cloudflare-one/insights/dex/tests/traceroute/">network path visualization</a>, creating a comprehensive troubleshooting workflow that connects application performance with device state.</p>
<p>For more details refer to our <a href="/cloudflare-one/insights/dex/">DEX</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-07">Mar 7, 2025</time><div>
<h2 id="post-2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress"><a href="/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/">Hyperdrive reduces query latency by up to 90% and now supports IP access control lists</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-regional-pooling-query-latency-improvement.png" alt="Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling." /></p>
<p>By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.</p>
<p>With this update, Hyperdrive also uses <a href="https://www.cloudflare.com/ips/">Cloudflare's standard IP address ranges</a> to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.</p>
<p>Refer to <a href="/hyperdrive/concepts/how-hyperdrive-works/">documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast</a>.</p>
<p>This improvement is enabled on all Hyperdrive configurations.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-07">Mar 7, 2025</time><div>
<h2 id="post-2025-03-07-updated-leaked-credentials-database"><a href="/changelog/post/2025-03-07-updated-leaked-credentials-database/">Updated leaked credentials database</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>Added new records to the leaked credentials database. The record sources are: Have I Been Pwned (HIBP) database, RockYou 2024 dataset, and another third-party database.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-06">Mar 6, 2025</time><div>
<h2 id="post-2025-03-06-oneclick-logpush"><a href="/changelog/post/2025-03-06-oneclick-logpush/">One-click Logpush Setup with R2 Object Storage</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>We’ve streamlined the <a href="/logs/logpush/">Logpush</a> setup process by integrating R2 bucket creation directly into the Logpush workflow!</p>
<p>Now, you no longer need to navigate multiple pages to manually create an R2 bucket or copy credentials. With this update, you can seamlessly <strong>configure a Logpush job to R2 in just one click</strong>, reducing friction and making setup faster and easier.</p>
<p>This enhancement makes it easier for customers to adopt Logpush and R2.</p>
<p>For more details refer to our <a href="/logs/logpush/logpush-job/enable-destinations/r2/">Logs</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-06">Mar 6, 2025</time><div>
<h2 id="post-2025-03-06-r2-bucket-locks"><a href="/changelog/post/2025-03-06-r2-bucket-locks/">Set retention polices for your R2 bucket with bucket locks</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>You can now use <a href="/r2/buckets/bucket-locks/">bucket locks</a> to set retention policies on your <a href="/r2/buckets/">R2 buckets</a> (or specific prefixes within your buckets) for a specified period — or indefinitely. This can help ensure compliance by protecting important data from accidental or malicious deletion.</p>
<p>Locks give you a few ways to ensure your objects are retained (not deleted or overwritten). You can:</p>
<ul>
<li>Lock objects for a specific duration, for example 90 days.</li>
<li>Lock objects until a certain date, for example January 1, 2030.</li>
<li>Lock objects indefinitely, until the lock is explicitly removed.</li>
</ul>
<p>Buckets can have up to 1,000 <a href="/r2/buckets/">bucket lock rules</a>. Each rule specifies which objects it covers (via prefix) and how long those objects must remain retained.</p>
<p>Here are a couple of examples showing how you can configure bucket lock rules using <a href="/workers/wrangler/">Wrangler</a>:</p>
<h4 id="2025-03-06-r2-bucket-locks-ensure-all-objects-in-a-bucket-are-retained-for-at-least-180-days">Ensure all objects in a bucket are retained for at least 180 days</h4>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name 180-days-all --retention-days 180&#10;</code></pre>
<h4 id="2025-03-06-r2-bucket-locks-prevent-deletion-or-overwriting-of-all-logs-indefinitely-via-prefix">Prevent deletion or overwriting of all logs indefinitely (via prefix)</h4>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name indefinite-logs --prefix logs/ --retention-indefinite&#10;</code></pre>
<p>For more information on bucket locks and how to set retention policies for objects in your R2 buckets, refer to our <a href="/r2/buckets/bucket-locks/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-06">Mar 6, 2025</time><div>
<h2 id="post-2025-03-06-media-transformations"><a href="/changelog/post/2025-03-06-media-transformations/">Introducing Media Transformations from Cloudflare Stream</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>Today, we are thrilled to announce Media Transformations, a new service that
brings the magic of <a href="/images/optimization/transformations/overview/">Image Transformations</a> to
<em>short-form video files,</em> wherever they are stored!</p>
<p>For customers with a huge volume of short video — generative AI output,
e-commerce product videos, social media clips, or short marketing content —
uploading those assets to Stream is not always practical. Sometimes, the
greatest friction to getting started was the thought of all that migrating.
Customers want a simpler solution that retains their current storage strategy to
deliver small, optimized MP4 files. Now you can do that with Media
Transformations.</p>
<p>To transform a video or image,
<a href="/stream/transform-videos/#getting-started">enable transformations</a> for your
zone, then make a simple request with a specially formatted URL. The result is
an MP4 that can be used in an HTML video element without a player library.
If your zone already has Image Transformations enabled, then it is ready to
optimize videos with Media Transformations, too.</p>
<pre tabindex="0"><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;</code></pre>
<p>For example, we have a short video of the mobile in Austin's office. The
original is nearly 30 megabytes and wider than necessary for this layout.
Consider a simple width adjustment:</p>
<video controls>
	<source src="https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4" />
</video>
<pre tabindex="0"><code class="language-text">https://example.com/cdn-cgi/media/width=640/&lt;SOURCE-VIDEO&gt;&#10;https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4&#10;</code></pre>
<p>The result is less than 3 megabytes, properly sized, and delivered dynamically
so that customers do not have to manage the creation and storage of these
transformed assets.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-04">Mar 4, 2025</time><div>
<h2 id="post-2025-03-03-user-action-logging"><a href="/changelog/post/2025-03-03-user-action-logging/">Gain visibility into user actions in Zero Trust Browser Isolation sessions</a></h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>We're excited to announce that new logging capabilities for <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> through <a href="/logs/logpush/logpush-job/datasets/account/">Logpush</a> are available in Beta starting today!</p>
<p>With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;AccountID&quot;: &quot;$ACCOUNT_ID&quot;,&#10;	&quot;Decision&quot;: &quot;block&quot;,&#10;	&quot;DomainName&quot;: &quot;www.example.com&quot;,&#10;	&quot;Timestamp&quot;: &quot;2025-02-27T23:15:06Z&quot;,&#10;	&quot;Type&quot;: &quot;copy&quot;,&#10;	&quot;UserID&quot;: &quot;$USER_ID&quot;&#10;}&#10;</code></pre>
<p>User Actions available:</p>
<ul>
<li><strong>Copy &amp; Paste</strong></li>
<li><strong>Downloads &amp; Uploads</strong></li>
<li><strong>Printing</strong></li>
</ul>
<p>Learn more about how to get started with Logpush in our <a href="/logs/logpush/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-03">Mar 3, 2025</time><div>
<h2 id="post-2025-03-03-saml-oidc-fields-saml-transformations"><a href="/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/">New SAML and OIDC Fields and SAML transforms for Access for SaaS</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS applications</a> now include more configuration options to support a wider array of SaaS applications.</p>
<p><strong>SAML and OIDC Field Additions</strong></p>
<p>OIDC apps now include:</p>
<ul>
<li>Group Filtering via RegEx</li>
<li>OIDC Claim mapping from an IdP</li>
<li>OIDC token lifetime control</li>
<li>Advanced OIDC auth flows including hybrid and implicit flows</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/oidc-claims.png" alt="OIDC field additions" /></p>
<p>SAML apps now include improved SAML attribute mapping from an IdP.</p>
<p><img src="/assets/upstream/images/changelog/access/saml-attribute-statements.png" alt="SAML field additions" /></p>
<p><strong>SAML transformations</strong></p>
<p>SAML identities sent to Access applications can be fully customized using JSONata expressions. This allows admins to configure the precise identity SAML statement sent to a SaaS application.</p>
<p><img src="/assets/upstream/images/changelog/access/transformation-box.png" alt="Configured SAML statement sent to application" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-03">Mar 3, 2025</time><div>
<h2 id="post-2025-03-03-waf-release"><a href="/changelog/post/2025-03-03-waf-release/">WAF Release - 2025-03-03</a></h2>
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
				<code class="nb-rule-id" title="90356ececae3444b9accb3d393e63099">93e63099</code>
</td>
<td>100721</td>
<td>
				Ivanti - Remote Code Execution - CVE:CVE-2024-13159, CVE:CVE-2024-13160,
				CVE:CVE-2024-13161
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6cf09ce2fa73482abb7f677ecac42ce2">cac42ce2</code>
</td>
<td>100596</td>
<td>
				Citrix Content Collaboration ShareFile - Remote Code Execution -
				CVE:CVE-2023-24489
</td>
<td>N/A</td>
<td>Block</td>
<td></td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-03-02">Mar 2, 2025</time><div>
<h2 id="post-2025-03-01-logpush-detections"><a href="/changelog/post/2025-03-01-logpush-detections/">Use Logpush for Email security detections</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now send detection logs to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set and select from over 25 fields you want to send. When creating a new Logpush job, remember to select <strong>Email security alerts</strong> as the dataset.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-Detections.png" alt="logpush-detections" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs">Enable detection logs</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-28">Feb 28, 2025</time><div>
<h2 id="post-2025-02-28-wrangler-v4-rc"><a href="/changelog/post/2025-02-28-wrangler-v4-rc/">Use the latest JavaScript features with Wrangler CLI v4.0.0-rc.0</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've released a release candidate of the next major version of <a href="/workers/wrangler/">Wrangler</a>, the CLI for Cloudflare Workers — <code>wrangler@4.0.0-rc.0</code>.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-28">Feb 28, 2025</time><div>
<h2 id="post-2025-02-07-check-status"><a href="/changelog/post/2025-02-07-check-status/">Check status of Email security or Area 1</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Concerns about performance for Email security or Area 1? You can now check the operational status of both on the <a href="https://www.cloudflarestatus.com/">Cloudflare Status page</a>.</p>
<p>For Email security, look under <strong>Cloudflare Sites and Services</strong>.</p>
<ul>
<li><strong>Dashboard</strong> is the dashboard for Cloudflare, including Email security</li>
<li><strong>Email security (Zero Trust)</strong> is the processing of email</li>
<li><strong>API</strong> are the Cloudflare endpoints, including the ones for Email security</li>
</ul>
<p>For Area 1, under <strong>Cloudflare Sites and Services</strong>:</p>
<ul>
<li><strong>Area 1 - Dash</strong> is the dashboard for Cloudflare, including Email security</li>
<li><strong>Email security (Area1)</strong> is the processing of email</li>
<li><strong>Area 1 - API</strong> are the Area 1 endpoints</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/Status-Page.png" alt="Status-page" /></p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-27">Feb 27, 2025</time><div>
<h2 id="post-2025-02-27-br-rest-api-beta"><a href="/changelog/post/2025-02-27-br-rest-api-beta/">New REST API is in open beta!</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We've released a new REST API for <a href="/browser-run/">Browser Rendering</a> in open beta, making interacting with browsers easier than ever. This new API provides endpoints for common browser actions, with more to be added in the future.</p>
<p>With the <strong>REST API</strong> you can:</p>
<ul>
<li><strong>Capture screenshots</strong> – Use <code>/screenshot</code> to take a screenshot of a webpage from provided URL or HTML.</li>
<li><strong>Generate PDFs</strong> – Use <code>/pdf</code> to convert web pages into PDFs.</li>
<li><strong>Extract HTML content</strong> – Use <code>/content</code> to retrieve the full HTML from a page.
<strong>Snapshot (HTML + Screenshot)</strong> – Use <code>/snapshot</code> to capture both the page's HTML and a screenshot in one request</li>
<li><strong>Scrape Web Elements</strong> – Use <code>/scrape</code> to extract specific elements from a page.</li>
</ul>
<p>For example, to capture a screenshot:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;Hello World!&quot;,&#10;    &quot;screenshotOptions&quot;: {&#10;      &quot;type&quot;: &quot;webp&quot;,&#10;      &quot;omitBackground&quot;: true&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.webp&quot;&#10;</code></pre>
<p>Learn more in our <a href="/browser-run/quick-actions/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-27">Feb 27, 2025</time><div>
<h2 id="post-2025-02-27-radar-dns-insights"><a href="/changelog/post/2025-02-27-radar-dns-insights/">DNS Insights in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its DNS insights, providing visibility into aggregated traffic and usage trends observed by our <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.
In addition to global, location, and ASN traffic trends, we are also providing perspectives on protocol usage, query/response characteristics, and DNSSEC usage.</p>
<p>Previously limited to the <a href="/api/resources/radar/subresources/dns/subresources/top/"><code>top</code></a> locations and ASes endpoints, we have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/dns/methods/timeseries/"><code>/dns/timeseries</code></a>: Retrieves DNS query volume over time.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/summary/"><code>/dns/summary/{dimension}</code></a>: Retrieves summaries of DNS query distribution across ten different dimensions.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/timeseries_groups/"><code>/dns/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for DNS query distribution across ten different dimensions.</li>
</ul>
<p>For the <code>summary</code> and <code>timeseries_groups</code> endpoints, the following dimensions are available, displaying the distribution of DNS queries based on:</p>
<ul>
<li><code>cache_hit</code>: Cache status (hit vs. miss).</li>
<li><code>dnsssec</code>: DNSSEC support status (secure, insecure, invalid or other).</li>
<li><code>dnsssec_aware</code>: DNSSEC client awareness (aware vs. not-aware).</li>
<li><code>dnsssec_e2e</code>: End-to-end security (secure vs. insecure).</li>
<li><code>ip_version</code>: IP version (IPv4 vs. IPv6).</li>
<li><code>matching_answer</code>: Matching answer status (match vs. no-match).</li>
<li><code>protocol</code>: Transport protocol (UDP, TLS, HTTPS or TCP).</li>
<li><code>query_type</code>: Query type (<code>A</code>, <code>AAAA</code>, <code>PTR</code>, etc.).</li>
<li><code>response_code</code>: Response code (<code>NOERROR</code>, <code>NXDOMAIN</code>, <code>REFUSED</code>, etc.).</li>
<li><code>response_ttl</code>: Response TTL.</li>
</ul>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/dns">new Radar page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-26">Feb 26, 2025</time><div>
<h2 id="post-2025-02-26-guardrails"><a href="/changelog/post/2025-02-26-guardrails/">Introducing Guardrails in AI Gateway</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p><a href="/ai-gateway/">AI Gateway</a> now includes <a href="/ai-gateway/features/guardrails/">Guardrails</a>, to help you monitor your AI apps for harmful or inappropriate content and deploy safely.</p>
<p>Within the AI Gateway settings, you can configure:</p>
<ul>
<li><strong>Guardrails</strong>: Enable or disable content moderation as needed.</li>
<li><strong>Evaluation scope</strong>: Select whether to moderate user prompts, model responses, or both.</li>
<li><strong>Hazard categories</strong>: Specify which categories to monitor and determine whether detected inappropriate content should be blocked or flagged.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/Guardrails.png" alt="Guardrails in AI Gateway" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/guardrails-in-ai-gateway/">blog</a> or our <a href="/ai-gateway/features/guardrails/">documentation</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/45/">Previous</a><span>Page 46 of 50</span><a class="pagination-next" rel="next" href="/changelog/47/">Next</a></nav>
</div>
