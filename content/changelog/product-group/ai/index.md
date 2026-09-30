---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/ai/
  description: '2026-09-17'
  full_title: AI changelog | Cloudflare Docs
  head_html: <title>AI changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-17"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/ai/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-17"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/ai/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/ai/#page","headline":"AI changelog | Cloudflare Docs","description":"2026-09-17","url":"https://developers.cloudflare.com/changelog/product-group/ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/ai/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="reject-busy-synchronous-inference-requests"><a href="/changelog/post/2026-09-17-reject-if-busy/">Reject busy synchronous inference requests</a></h2>
<p><em>2026-09-17</em></p>
<p>The <code>rejectIfBusy</code> option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.</p>
<p>Pass the option as the third argument to the Workers AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17820.md")</div>
<p>For the native REST API, add the option to the request body:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Explain capacity queues.&quot; }],&#10;    &quot;options&quot;: { &quot;rejectIfBusy&quot;: true }&#10;  }&#x27;&#10;</code></pre>
<p>Refer to <a href="/workers-ai/features/reject-if-busy/">Reject busy requests</a> for OpenAI-compatible usage and error behavior.</p>


<h2 id="prevent-unified-billing-fallback-for-byok-third-party-providers"><a href="/changelog/post/2026-09-14-require-provider-credentials/">Prevent Unified Billing fallback for BYOK third-party providers</a></h2>
<p><em>2026-09-14</em></p>
<p>AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.</p>
<p>Turn on <strong>Require provider credentials</strong> in your gateway settings. To use the API, set <code>byok_only</code> to <code>true</code> in the request body of a <a href="/api/resources/ai_gateway/methods/update/"><code>PUT</code> request to update the gateway</a>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;byok_only&quot;: true&#10;}&#10;</code></pre>
<p>To require provider credentials for one third-party request, set the <code>cf-aig-no-wholesale</code> header to <code>true</code>. This header cannot relax the gateway setting.</p>
<p>Requests without applicable credentials then return an HTTP <code>400</code> response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.</p>
<p>For configuration details and request-level controls, refer to <a href="/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</a>.</p>


<h2 id="control-which-hostnames-browser-run-sessions-can-access"><a href="/changelog/post/2026-09-14-guardrails/">Control which hostnames Browser Run sessions can access</a></h2>
<p><em>2026-09-14</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports <a href="/browser-run/features/guardrails/">guardrails</a>, which limit a browser session's HTTP and HTTPS requests to permitted hostnames.</p>
<p>Use guardrails when you need to:</p>
<ul>
<li>Keep a browser workflow limited to a specific website and its subdomains.</li>
<li>Load only known third-party APIs, scripts, images, and fonts.</li>
<li>Generate a screenshot or PDF from HTML you provide while preventing it from loading external content.</li>
</ul>
<p>Set guardrails when starting a session with Puppeteer, Playwright, or the REST API. With a browser binding named <code>MYBROWSER</code>, pass <code>guardrails</code> when launching Puppeteer:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17700.md")</div>
<p>In addition to session guardrails, Browser Run now supports a read-only mode for <a href="/browser-run/features/live-view/">Live View</a>. Live View lets you watch and interact with an active Browser Run session in real time. A read-only link lets someone watch without clicking, typing, navigating, or running JavaScript.</p>
<p>To create a read-only link, set <code>{ mode: &quot;readonly&quot; }</code> when generating the Live View URL. This setting affects only the person using that link. The session's hostname restrictions remain unchanged.</p>
<p>Refer to the <a href="/browser-run/features/guardrails/">guardrails documentation</a> for more information.</p>


<h2 id="inspect-voice-agent-turn-latency-and-outcomes"><a href="/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/">Inspect Voice Agent turn latency and outcomes</a></h2>
<p><em>2026-09-11</em></p>
<p><code>@cloudflare/voice</code> v0.4.0 now lets you inspect where each Voice Agent turn spends time and how it ends.</p>
<pre tabindex="0"><code class="language-ts">client.addEventListener(&quot;turnmetrics&quot;, (turn) =&gt; {&#10;	console.log(turn.outcome, turn.turnTotalMs);&#10;});&#10;</code></pre>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-about-the-voice-package">About the Voice package</h4>
<p>The <code>@cloudflare/voice</code> package lets you build real-time voice agents with Cloudflare Agents. It streams microphone audio to an Agent over WebSocket, transcribes speech, runs your model through <code>onTurn()</code>, converts the response to speech, and streams audio back to the caller.</p>
<p>A turn moves through several stages:</p>
<pre tabindex="0"><code class="language-txt">User speaks -&gt; speech-to-text -&gt; model -&gt; text-to-speech -&gt; audio&#10;</code></pre>
<p>Previously, the package's four aggregate metrics covered successful, non-empty speech turns. They did not show how failed, aborted, empty, or text turns ended.</p>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-turn-metrics">Turn metrics</h4>
<p>Each speech or text turn now produces a typed <code>VoiceTurnMetrics</code> summary with:</p>
<ul>
<li>A <code>turnId</code> for correlating events from the same turn.</li>
<li>A terminal outcome such as <code>completed</code>, <code>no_output</code>, <code>output_limit</code>, <code>content_filtered</code>, <code>model_error</code>, <code>tts_error</code>, or <code>aborted</code>.</li>
<li>Timings for important stages, including speech-to-final-transcript, model-to-first-text, TTS-to-first-audio, and total turn duration.</li>
</ul>
<p>These timings can overlap and are not additive. Timings for stages that a turn did not reach are omitted.</p>
<p>The latest summary is available through <code>VoiceClient</code>, <code>useVoiceAgent()</code>, and <code>useVoiceInput()</code>. Voice input includes only the speech and transcription timings it can measure.</p>
<p>If an agent produces no audio, you can now distinguish between the model returning no output, reaching an output limit, encountering content filtering, or failing.</p>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-additional-diagnostics">Additional diagnostics</h4>
<p>For local debugging, you can forward server lifecycle events to the browser console:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17686.md")</div>
<p>The browser console combines server lifecycle events with local microphone, connection, and playback events, including model start, first model text, first audio, and playback start. Diagnostics are off by default, and their event names and fields can change.</p>
<p><code>VoiceClient</code> also exposes typed events for speech-to-text failures, connection errors, and model outcomes. The SDK removes known content fields and does not read arbitrary provider responses, but custom error messages must not contain sensitive data.</p>
<p>Install the release with a compatible Agents SDK version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/communication-channels/voice/#pipeline-metrics">Voice pipeline metrics</a> and <a href="https://github.com/cloudflare/agents/tree/main/examples/voice-agent">Voice Agent example</a> to get started.</p>


<h2 id="ai-search-supports-extensionless-r2-objects-with-content-type-metadata"><a href="/changelog/post/2026-09-11-extensionless-r2-content-type/">AI Search supports extensionless R2 objects with Content-Type metadata</a></h2>
<p><em>2026-09-11</em></p>
<p>AI Search can index R2 objects without filename extensions when they include supported <code>Content-Type</code> metadata. This supports object keys that do not include file extensions while preserving file-type validation during indexing.</p>
<p>For supported file types and Content-Type requirements, refer to <a href="/ai-search/configuration/data-source/r2/">R2 data sources</a>.</p>


<h2 id="ai-gateway-custom-costs-support-cache-tokens"><a href="/changelog/post/2026-09-09-custom-cache-token-costs/">AI Gateway custom costs support cache tokens</a></h2>
<p><em>2026-09-09</em></p>
<p>AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.</p>
<p>Add <code>per_cache_read_token</code> or <code>per_cache_write_token</code> to the <code>cf-aig-custom-cost</code> header:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;per_token_in&quot;: 0.000001,&#10;	&quot;per_token_out&quot;: 0.000002,&#10;	&quot;per_cache_read_token&quot;: 0.0000001,&#10;	&quot;per_cache_write_token&quot;: 0.0000005&#10;}&#10;</code></pre>
<p>Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to <code>per_token_in</code>. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.</p>
<p>Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/custom-costs/">Custom costs</a>.</p>


<h2 id="run-cursor-cloud-agents-on-cloudflare-via-self-hosted-machines"><a href="/changelog/post/2026-09-02-cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a></h2>
<p><em>2026-09-02</em></p>
<p><a href="https://cursor.com/docs/cloud-agent/self-hosted">Cursor self-hosted machines</a> let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by <a href="/containers/">Cloudflare Containers</a>.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/cursor-cloud-agents-self-hosted-pool.png" alt="Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool" /></p>
<p>Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source <a href="https://github.com/anysphere/cloudflare-workers">Cursor Cloudflare Workers template</a> deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a>.</p>


<h2 id="ai-gateway-consolidates-monthly-usage-invoice-line-items-and-standardizes-model-names"><a href="/changelog/post/2026-09-01-billing-and-model-names/">AI Gateway consolidates monthly usage invoice line items and standardizes model names</a></h2>
<p><em>2026-09-01</em></p>
<p>AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.</p>
<p>For example, an invoice that previously included these separate line items:</p>
<ul>
<li><code>anthropic claude-haiku-4-5-20251001 Input Tokens</code>: 40,000 tokens at $0.000001 ($0.04)</li>
<li><code>anthropic claude-haiku-4-5-20251001 Output Tokens</code>: 24,000 tokens at $0.000005 ($0.12)</li>
</ul>
<p>The updated invoice includes one line item: <code>anthropic/claude-haiku-4.5</code>: $0.16.</p>
<p>AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent <code>provider/model</code> identifier.</p>
<p>For more information, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and <a href="/ai-gateway/observability/logging/">AI Gateway logging documentation</a>.</p>


<h2 id="crawl-endpoint-now-respects-the-content-signals-use-directive"><a href="/changelog/post/2026-08-31-crawl-content-use/">Crawl endpoint now respects the Content Signals `use` directive</a></h2>
<p><em>2026-08-31</em></p>
<p>The <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code></a> endpoint now respects the <code>use</code> directive of the <a href="https://contentsignals.org/">Content Signals</a> standard, letting site owners express the maximum level at which their content may be used.</p>
<p>You can declare your intended level with the new <code>contentUse</code> parameter. Allowed values, from least to most permissive, are <code>reference</code> and <code>full</code>, and the default is <code>full</code>. If a target site's <code>robots.txt</code> sets a <code>use</code> level that is more restrictive than your declared <code>contentUse</code>, the crawl request is rejected with a <code>400</code> error.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;contentUse&quot;: &quot;reference&quot;,&#10;    &quot;formats&quot;: [&quot;markdown&quot;]&#10;  }&#x27;&#10;</code></pre>
<p>For more information, refer to <a href="/browser-run/quick-actions/crawl-endpoint/#content-signals">Content Signals</a> in the <code>/crawl</code> endpoint documentation.</p>


<h2 id="ai-search-now-supports-glm-5-3-flash"><a href="/changelog/post/2026-08-30-glm-5.3-flash/">AI Search now supports GLM-5.3 Flash</a></h2>
<p><em>2026-08-30</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> for text generation. The model has a 1,048,576-token context window and runs on Workers AI.</p>
<p>To configure the model for an AI Search instance, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="z-ai-glm-5-3-now-available-on-workers-ai"><a href="/changelog/post/2026-08-28-glm-5.3-workers-ai/">Z.ai GLM-5.3 now available on Workers AI</a></h2>
<p><em>2026-08-28</em></p>
<p><a href="/workers-ai/models/glm-5.3/"><code>@cf/zai-org/glm-5.3</code></a> is now available on Workers AI. It is Z.ai's flagship agentic coding model, built for long-running, tool-driven development workflows rather than single-turn chat.</p>
<p>GLM-5.3 uses the same base model as GLM-5.2, with every gain coming from post-training. The results are substantial on coding and agentic benchmarks: <a href="https://huggingface.co/zai-org/GLM-5.3">Z.ai reports</a> a 50% improvement over GLM-5.2 on its in-house Z.ai Code Bench, and calls GLM-5.3 the most capable open-weights model for coding. On public benchmarks, it scores 88.2 on Terminal Bench 2.1 (up from 81.0), 28.3 on Terminal Bench 3.0 — open-source state of the art, up from 4.6 — 66.9 on DeepSWE (up from 46.2), 78.1 on FrontierSWE (up from 67.5), and 42.5 on SWE-Marathon (up from 19.4). It is also the top-scoring model in Z.ai's comparisons on CyberGym for vulnerability discovery (84.5) and on long-horizon automation tasks like AutomationBench (48.2).</p>
<p>The price-to-performance ratio is the compelling part. On Workers AI, GLM-5.3 costs the same as GLM-5.2 — $1.40 per M input tokens, $0.26 per M cached input tokens, and $4.40 per M output tokens — while roughly doubling GLM-5.2's scores on long-horizon benchmarks like SWE-Marathon, and improving them by more than 6x on Terminal Bench 3.0.</p>
<p>GLM-5.3 requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3/">GLM-5.3 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="new-workers-ai-text-generation-models-in-ai-search"><a href="/changelog/post/2026-08-26-new-workers-ai-models/">New Workers AI text generation models in AI Search</a></h2>
<p><em>2026-08-26</em></p>
<p><a href="/ai-search/">AI Search</a> now supports six additional <a href="/workers-ai/">Workers AI</a> models for text generation:</p>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></td>
<td>1,048,576</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-120b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/openai/gpt-oss-20b</code></td>
<td>128,000</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3.8-27b</code></td>
<td>262,144</td>
</tr>
<tr>
<td><code>@cf/moonshotai/kimi-k2.7-code</code></td>
<td>262,144</td>
</tr>
</tbody>
</table>
<p>These models run on Workers AI, so they do not require an additional provider key. Select a model when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>


<h2 id="z-ai-glm-5-3-flash-now-available-on-workers-ai"><a href="/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/">Z.ai GLM-5.3 Flash now available on Workers AI</a></h2>
<p><em>2026-08-26</em></p>
<p><a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> is now available on Workers AI. It is the first natively multimodal model in the GLM-5 series, built on a Mixture-of-Experts architecture with 320B total parameters and 18B active per token.</p>
<p>GLM-5.3 Flash is the first GLM-family model on Workers AI to support multimodal inputs. It outperforms GLM-5.2 across benchmarks and real-world workloads at a lower price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.</p>
<p>GLM-5.3 Flash requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3-flash/">GLM-5.3 Flash model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="store-larger-custom-metadata-values-in-ai-search"><a href="/changelog/post/2026-08-25-larger-custom-metadata-values/">Store larger custom metadata values in AI Search</a></h2>
<p><em>2026-08-25</em></p>
<p>AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.</p>
<p>For details, refer to <a href="/ai-search/configuration/indexing/metadata/">Metadata attributes</a>.</p>


<h2 id="choose-oauth-scopes-for-wrangler-and-the-cloudflare-api-mcp-server"><a href="/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/">Choose OAuth scopes for Wrangler and the Cloudflare API MCP server</a></h2>
<p><em>2026-08-22</em></p>
<p>Wrangler and the <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare API MCP server</a> now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.</p>
<p>The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-review.png" alt="OAuth consent dialog with an Edit Permissions button" /></p>
<p>You can then choose which specific permissions to grant:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-edit.png" alt="OAuth permission editor with controls for individual scopes" /></p>
<p>Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.</p>
<p>If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.</p>
<p>For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">Edit optional permissions</a>.</p>


<h2 id="run-more-headless-browsers-concurrently-with-browser-run"><a href="/changelog/post/2026-08-20-limits-increase/">Run more headless browsers concurrently with Browser Run</a></h2>
<p><em>2026-08-20</em></p>
<p><a href="/browser-run/">Browser Run</a> lets you automate headless browsers on Cloudflare's global network. Run full browser sessions for interactive workflows, or use <a href="/browser-run/quick-actions/">Quick Actions</a> for one-request tasks such as screenshots, PDFs, and capturing page content.</p>
<p>If you are on the <a href="/workers/platform/pricing/">Workers Paid plan</a>, your default <a href="/browser-run/limits/#workers-paid">limits</a> are now higher:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent browsers</td>
<td>120</td>
<td><strong>200</strong></td>
</tr>
<tr>
<td>New browser instances / second</td>
<td>1</td>
<td><strong>3</strong></td>
</tr>
<tr>
<td>Quick Actions requests / second</td>
<td>10</td>
<td><strong>30</strong></td>
</tr>
</tbody>
</table>
<p>You can now run hundreds of browser sessions in parallel, launch new browsers faster, and process three times as many <a href="/browser-run/quick-actions/">Quick Actions</a> per second. These published limits are defaults, not maximums. If your workload needs more more concurrent browsers, <a href="https://forms.gle/CdueDKvb26mTaepa9">request higher limits</a>.</p>


<h2 id="get-50-off-gpt-5-6-sol-through-ai-gateway"><a href="/changelog/post/2026-08-19-gpt-5-6-sol-discount/">Get 50% off GPT-5.6 Sol through AI Gateway</a></h2>
<p><em>2026-08-19</em></p>
<p>GPT-5.6 Sol is available through AI Gateway, and for a limited time you can use it at 50% off. If you are already using AI Gateway, point to the <code>openai/gpt-5.6-sol</code> model and the discounted pricing applies automatically — no promo code needed.</p>
<p>The promotion is available for <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> users only (not <a href="/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Keys</a>). Load credits onto AI Gateway and start sending requests to <code>openai/gpt-5.6-sol</code>.</p>
<p>Discounted pricing during the promotion:</p>
<table>
<thead>
<tr>
<th>Usage</th>
<th>Promotional price</th>
<th>Standard price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Input</td>
<td>$2.50 per 1M tokens</td>
<td>$5 per 1M tokens</td>
</tr>
<tr>
<td>Output</td>
<td>$15 per 1M tokens</td>
<td>$30 per 1M tokens</td>
</tr>
<tr>
<td>Cache read</td>
<td>$0.25 per 1M tokens</td>
<td>$0.50 per 1M tokens</td>
</tr>
</tbody>
</table>
<p>The promotion runs through September 18, 2026. After that date, GPT-5.6 Sol requests return to standard pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and the <a href="/ai/models/openai/gpt-5.6-sol/">GPT-5.6 Sol model page</a>.</p>


<h2 id="qwen-3-8-27b-now-available-on-workers-ai"><a href="/changelog/post/2026-08-17-qwen-3.8-27b-workers-ai/">Qwen 3.8 27B now available on Workers AI</a></h2>
<p><em>2026-08-17</em></p>
<p><a href="/workers-ai/models/qwen3.8-27b/"><code>@cf/qwen/qwen3.8-27b</code></a> is now available on Workers AI.</p>
<p>Qwen 3.8 27B is a 27-billion-parameter instruction-tuned vision language model from Alibaba's Qwen family. It processes images and text together, with reasoning and function calling for agentic workflows.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Vision</strong>: Accept image and text inputs and generate text responses.</li>
<li><strong>Reasoning</strong>: Support thinking mode for complex, step-by-step problem-solving.</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns.</li>
<li><strong>262,144 token context window</strong>: Retain long conversations and multimodal inputs across extended agent sessions.</li>
</ul>
<p>Use Qwen 3.8 27B through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>) or the REST API at <code>/ai/run</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/qwen3.8-27b/">Qwen 3.8 27B model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="deepseek-v4-flash-and-pro-now-available-on-workers-ai"><a href="/changelog/post/2026-08-14-deepseek-v4-workers-ai/">DeepSeek V4 Flash and Pro now available on Workers AI</a></h2>
<p><em>2026-08-14</em></p>
<p><a href="/workers-ai/models/deepseek-v4-pro-0813/"><code>@cf/deepseek-ai/deepseek-v4-pro-0813</code></a> and <a href="/workers-ai/models/deepseek-v4-flash-0731/"><code>@cf/deepseek-ai/deepseek-v4-flash-0731</code></a> are now available on Workers AI.</p>
<p>DeepSeek V4 Flash and DeepSeek V4 Pro are the first Workers AI models with a full <strong>one million (1,048,576) token context window</strong>. Use them for long-horizon agentic workflows, large codebases, and multi-step reasoning that exceed the context limits of every other model hosted on the platform.</p>
<p>DeepSeek V4 Flash is the faster, lower-cost sibling. This release supersedes the preview version with substantially enhanced agentic capabilities.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Reasoning</strong>: Both models support thinking mode for complex, step-by-step problem-solving.</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns.</li>
<li><strong>Long context</strong>: Both models support a full 1,048,576 token context window.</li>
</ul>
<p>Both models require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use these models through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/deepseek-v4-pro-0813/">DeepSeek V4 Pro model page</a>, the <a href="/workers-ai/models/deepseek-v4-flash-0731/">DeepSeek V4 Flash model page</a>, and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="workers-ai-and-ai-gateway-unify-model-access-and-billing"><a href="/changelog/post/2026-08-07-workers-ai-unified-billing/">Workers AI and AI Gateway unify model access and billing</a></h2>
<p><em>2026-08-07</em></p>
<p>Workers AI and AI Gateway now provide a unified path for accessing models and managing inference traffic. Use the same AI binding and REST API to call models hosted on Workers AI or by supported third-party providers, with AI Gateway providing observability, logging, caching, security, and billing controls.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-entrypoints-and-observability">Unified entrypoints and observability</h4>
<p>The <a href="/ai-gateway/usage/worker-binding-methods/">AI binding</a> supports both Workers AI and third-party models through <code>env.AI.run()</code>. The <a href="/ai-gateway/usage/rest-api/">REST API</a> provides shared <code>/ai/</code> endpoints with Cloudflare authentication across providers.</p>
<p>Route a Workers AI request through AI Gateway by specifying a gateway ID. Use <code>default</code> to automatically create a gateway on the first authenticated request, or specify an existing gateway to separate applications and workloads:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17687.md")</div>
<p>Requests routed through AI Gateway can be logged and included in analytics for request volume, errors, latency, token usage, and costs. You can also configure controls such as caching, rate limiting, and request retries on the gateway.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-billing-and-higher-rate-limits">Unified billing and higher rate limits</h4>
<p>You can now use prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a> to pay for Workers AI inference. This provides one credit balance for Workers AI and supported third-party model providers. To use credits for Workers AI, set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>. Workers AI requests routed through that gateway deduct from your credit balance in real time.</p>
<p>Prepaid credits also provide access to the following Workers AI frontier models without requiring the Workers Paid plan. Each frontier Workers AI model has a rate limit of 50 requests per minute per account, per model when billed with AI Gateway credits, compared to 20 requests per minute through standard Workers AI billing:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.</p>
<p>For details, refer to <a href="/workers-ai/platform/limits/">Workers AI limits</a>, <a href="/workers-ai/platform/pricing/">Workers AI pricing</a>, <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, and the <a href="/ai/models/">AI Gateway model catalog</a>.</p>


<h2 id="sandbox-sdk-1-0-preview-on-next"><a href="/changelog/post/2026-08-07-sandbox-sdk-1-0-preview/">Sandbox SDK 1.0 preview on @next</a></h2>
<p><em>2026-08-07</em></p>
<p><strong>Sandbox SDK 1.0</strong> is available to preview under the npm <code>@next</code> tag. For existing applications, the current stable package remains published on the 0.12.x line.</p>
<p>Sandbox SDK first shipped to provide a rich library for running untrusted and agent-driven work on <a href="/containers/">Cloudflare Containers</a>. Since then, both Sandbox and Containers have matured. This preview is a thinner SDK built on a richer Cloudflare Containers foundation.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-what-this-preview-is">What this preview is</h4>
<ul>
<li><strong>A single execution interface</strong> — <code>sandbox.exec()</code> takes an argument list, returns when the process <strong>starts</strong>, and gives you a handle for output, logs, waits, and signals. Both short commands and long-running services use the same API.</li>
<li><strong>Removed session execution</strong> — the SDK no longer maintains shell state between executions. Each launch is independent. Pass <code>cwd</code> and <code>env</code> when you need them, or put multi-step shell syntax in one explicit shell command.</li>
<li><strong>RPC as the only transport</strong> — the SDK talks to the container exclusively over RPC. Remove <code>SANDBOX_TRANSPORT</code>, <code>transport</code> on <code>getSandbox()</code>, and <code>setTransport()</code>.</li>
<li><strong>Improved PTY and terminal interface</strong> — interactive PTYs use <code>createTerminal</code> / <code>connect</code>, not the older session-shaped helpers.</li>
<li><strong>Code interpreter as an extension</strong> — configure the code interpreter on your <code>Sandbox</code> subclass so you only ship what you need.</li>
</ul>
<p>Start new projects on <code>@next</code>. Migrate existing apps when you can so you are ready when 1.0 becomes stable. Deploy the Worker package and container image from the <strong>same</strong> <code>@next</code> line.</p>
<p>Coding agents: install <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> (<a href="/agent-setup/">Agent setup</a>). Use <strong><code>sandbox-next</code></strong> for <code>@next</code> (recommended for new projects), <strong><code>sandbox-stable</code></strong> for the current stable package, and <strong><code>sandbox-migrate-to-next</code></strong> when you are ready to port. Stable-package deprecated-API cleanup is in the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation guide</a>.</p>
<p>The main <a href="/sandbox/">Sandbox documentation</a> still describes today's stable package. Preview docs:</p>
<ul>
<li><a href="/sandbox/1-0-preview/">1.0 preview</a></li>
<li><a href="/sandbox/1-0-preview/get-started/">Get started</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Processes</a> · <a href="/sandbox/1-0-preview/terminals/">Terminals</a> · <a href="/sandbox/1-0-preview/errors/">Errors</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
</ul>
<p>The self-deployed Sandbox bridge is not currently part of this preview. We are working on bringing it in line with the latest code. Until then, use the <a href="/sandbox/bridge/">stable bridge</a> with the matching stable package and container image.</p>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-timeline-for-1-0">Timeline for 1.0</h4>
<p>Further Cloudflare Containers features will let us keep reducing the size of the Sandbox SDK. We aim to ship Sandbox SDK 1.0 once those are in. In the meantime we continue to support and maintain the 1.0 preview (<code>@next</code>) alongside the current stable release.</p>


<h2 id="ai-search-makes-it-easier-to-build-a-search-engine-for-your-data"><a href="/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/">AI Search makes it easier to build a search engine for your data</a></h2>
<p><em>2026-08-06</em></p>
<p><a href="/ai-search/">AI Search</a> gets you from a data source to a working search endpoint quickly. This release adds what you need to put that endpoint in front of real users: your own domain, authentication, and one endpoint across several instances. It also adds crawling for sites without a complete sitemap, so your index covers everything you want it to find.</p>
<p>Each of the following is a new option. The previous behavior is still the default, so nothing changes until you change it.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-serve-search-from-your-own-domain">Serve search from your own domain</h4>
<p>A <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> is a URL that a site or app can query directly, with no authentication in front of it. By default that URL is a generated hostname on <code>search.ai.cloudflare.com</code>. You can now serve the same endpoint from a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a>, a hostname in a zone that you own:</p>
<pre tabindex="0"><code class="language-txt">https://search.example.com/search&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-restrict-who-can-query-your-content">Restrict who can query your content</h4>
<p>Once your endpoint is on your own domain, you can put <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> in front of it. For example, you usually want to give <code>/mcp</code> to specific agents rather than to anyone who finds the URL. Agents authenticate with an Access service token, and people who open the endpoint in a browser sign in through your identity provider.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-search-several-instances-from-one-url">Search several instances from one URL</h4>
<p>A namespace can expose its own <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">public endpoint</a> with <code>/search</code>, <code>/chat/completions</code>, and <code>/mcp</code> paths that fan out across the instances you choose:</p>
<pre tabindex="0"><code class="language-bash">curl https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;content&quot;: &quot;How do I configure AI Search?&quot;, &quot;role&quot;: &quot;user&quot; }],&#10;    &quot;ai_search_options&quot;: { &quot;instance_ids&quot;: [&quot;docs&quot;, &quot;support&quot;] }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-index-your-sites-without-a-sitemap">Index your sites without a sitemap</h4>
<p>Website data sources support a new <code>discover</code> <a href="/ai-search/configuration/data-source/website/parse-types/">parse type</a>. It starts at the source URL and collects pages from both your sitemaps and the links it finds while crawling:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source&quot;: &quot;example.com&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_type&quot;: &quot;discover&quot;,&#10;        &quot;discover_options&quot;: { &quot;source&quot;: &quot;links&quot;, &quot;limit&quot;: 5000, &quot;depth&quot;: 3 }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>To learn more, refer to the <a href="/ai-search/">AI Search documentation</a>.</p>


<h2 id="introducing-kitesurf-an-agent-first-browser-on-browser-run"><a href="/changelog/post/2026-08-06-kitesurf/">Introducing Kitesurf, an agent-first browser on Browser Run</a></h2>
<p><em>2026-08-06</em></p>
<p><a href="/browser-run/kitesurf/">Kitesurf</a> is Cloudflare's new stateless, highly scalable browser that runs entirely on top of <a href="/workers/">Workers</a> and is designed for AI agents. It is available for free while in beta.</p>
<p>Compared to Chromium, Kitesurf uses 3–7× less CPU and memory for common agentic tasks like screenshots and HTML extraction, so you can run more sessions and scale better for bursty, AI-driven workloads.</p>
<p>Your existing clients already work. To opt in, add the <code>browser=kitesurf</code> parameter to any Browser Run <a href="/browser-run/cdp/">CDP</a> or <a href="/browser-run/quick-actions/">Quick Action</a> endpoint:</p>
<pre tabindex="0"><code class="language-sh">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/screenshot?browser=kitesurf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<p>You can also explore Kitesurf without writing any code in the <a href="https://kitesurf.cloudflare.app/">public playground</a>.</p>
<p>For more information, refer to the <a href="/browser-run/kitesurf/">Kitesurf documentation</a> and the <a href="https://blog.cloudflare.com/kitesurf">blog announcement</a>.</p>


<h2 id="track-ai-spend-and-catch-anomalous-usage-with-user-insights"><a href="/changelog/post/2026-08-05-user-insights/">Track AI spend and catch anomalous usage with User Insights</a></h2>
<p><em>2026-08-05T12:00:00-08:00</em></p>
<p>AI Gateway now includes User Insights, a dashboard that gives you two things at once: clear visibility into how much your organization spends on AI, and a security signal that surfaces users whose usage suddenly looks abnormal. It works on the traffic already flowing through your gateway, so there is no additional setup.</p>
<p>On the spend side, User Insights shows organization-wide totals for cost, requests, tokens, and adoption, and lets you drill into an individual user to see their spend, top models and providers, cache hit rate, and more. To attribute usage to individual users, add a user identifier with custom metadata or put your gateway behind Cloudflare Access.</p>
<p>On the security side, User Insights baselines each user's normal usage from their 95th percentile (p95) session cost over the last 30 days, then flags sessions that exceed both that baseline and an organization-level threshold. A sudden jump above a user's own pattern is often the first sign of a compromised credential or a misbehaving agent, so you can investigate before it shows up on your bill.</p>
<p>User Insights is available to all AI Gateway customers at no additional cost.</p>


<h2 id="identity-aware-controls-are-now-available-in-ai-gateway"><a href="/changelog/post/2026-08-05-access-user-id-metadata/">Identity-aware controls are now available in AI Gateway</a></h2>
<p><em>2026-08-05</em></p>
<p>AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:</p>
<ul>
<li><strong>Protect your gateway endpoint.</strong> Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.</li>
<li><strong>Identity-aware controls.</strong> When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.</li>
</ul>
<p>With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as <code>cf.user_id</code>.</p>
<p>For setup instructions, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 7</span><a class="pagination-next" rel="next" href="/changelog/product-group/ai/2/">Next</a></nav>
