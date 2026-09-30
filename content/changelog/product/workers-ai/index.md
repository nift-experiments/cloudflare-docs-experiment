<h1 id="changelog">Changelog</h1>

<h2 id="reject-busy-synchronous-inference-requests"><a href="/changelog/post/2026-09-17-reject-if-busy/">Reject busy synchronous inference requests</a></h2>
<p><em>2026-09-17</em></p>
<p>The <code>rejectIfBusy</code> option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.</p>
<p>Pass the option as the third argument to the Workers AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17820.md")</div>
<p>For the native REST API, add the option to the request body:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Explain capacity queues.&quot; }],&#10;    &quot;options&quot;: { &quot;rejectIfBusy&quot;: true }&#10;  }&#x27;&#10;</code></pre>
<p>Refer to <a href="/workers-ai/features/reject-if-busy/">Reject busy requests</a> for OpenAI-compatible usage and error behavior.</p>


<h2 id="z-ai-glm-5-3-now-available-on-workers-ai"><a href="/changelog/post/2026-08-28-glm-5.3-workers-ai/">Z.ai GLM-5.3 now available on Workers AI</a></h2>
<p><em>2026-08-28</em></p>
<p><a href="/workers-ai/models/glm-5.3/"><code>@cf/zai-org/glm-5.3</code></a> is now available on Workers AI. It is Z.ai's flagship agentic coding model, built for long-running, tool-driven development workflows rather than single-turn chat.</p>
<p>GLM-5.3 uses the same base model as GLM-5.2, with every gain coming from post-training. The results are substantial on coding and agentic benchmarks: <a href="https://huggingface.co/zai-org/GLM-5.3">Z.ai reports</a> a 50% improvement over GLM-5.2 on its in-house Z.ai Code Bench, and calls GLM-5.3 the most capable open-weights model for coding. On public benchmarks, it scores 88.2 on Terminal Bench 2.1 (up from 81.0), 28.3 on Terminal Bench 3.0 — open-source state of the art, up from 4.6 — 66.9 on DeepSWE (up from 46.2), 78.1 on FrontierSWE (up from 67.5), and 42.5 on SWE-Marathon (up from 19.4). It is also the top-scoring model in Z.ai's comparisons on CyberGym for vulnerability discovery (84.5) and on long-horizon automation tasks like AutomationBench (48.2).</p>
<p>The price-to-performance ratio is the compelling part. On Workers AI, GLM-5.3 costs the same as GLM-5.2 — $1.40 per M input tokens, $0.26 per M cached input tokens, and $4.40 per M output tokens — while roughly doubling GLM-5.2's scores on long-horizon benchmarks like SWE-Marathon, and improving them by more than 6x on Terminal Bench 3.0.</p>
<p>GLM-5.3 requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3/">GLM-5.3 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="z-ai-glm-5-3-flash-now-available-on-workers-ai"><a href="/changelog/post/2026-08-26-glm-5.3-flash-workers-ai/">Z.ai GLM-5.3 Flash now available on Workers AI</a></h2>
<p><em>2026-08-26</em></p>
<p><a href="/workers-ai/models/glm-5.3-flash/"><code>@cf/zai-org/glm-5.3-flash</code></a> is now available on Workers AI. It is the first natively multimodal model in the GLM-5 series, built on a Mixture-of-Experts architecture with 320B total parameters and 18B active per token.</p>
<p>GLM-5.3 Flash is the first GLM-family model on Workers AI to support multimodal inputs. It outperforms GLM-5.2 across benchmarks and real-world workloads at a lower price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.</p>
<p>GLM-5.3 Flash requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> or prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a>.</p>
<p>Use GLM-5.3 Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API, the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/glm-5.3-flash/">GLM-5.3 Flash model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


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


<h2 id="select-models-now-require-the-workers-paid-plan"><a href="/changelog/post/2026-07-28-models-require-workers-paid/">Select models now require the Workers Paid plan</a></h2>
<p><em>2026-07-28</em></p>
<p>We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer <code>429</code> and <code>3040</code> (Out of Capacity) errors.</p>
<p>The following models now require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>On the Workers Free plan, requests to these models now return a <code>403</code> HTTP error (<a href="/workers-ai/platform/errors/">internal error <code>5035</code></a>) prompting you to upgrade. The Workers Paid plan starts at $5 per month and still includes the 10,000 free Neurons per day allocation, with usage beyond that billed at each <a href="/workers-ai/platform/pricing/">model's pricing</a>.</p>
<p>Many models remain available on the Workers Free plan, including:</p>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a></li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a></li>
<li><a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a></li>
</ul>
<p>For the full list, refer to the <a href="/workers-ai/models/">Workers AI model catalog</a>.</p>


<h2 id="plain-text-output-for-markdown-conversion"><a href="/changelog/post/2026-07-13-markdown-conversion-text-output/">Plain text output for Markdown Conversion</a></h2>
<p><em>2026-07-10</em></p>
<p>The <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service now supports a new <code>output</code> conversion option that controls the format of the converted content.</p>
<p>Set <code>output.format</code> to <code>text</code> to receive plain text with Markdown syntax removed. The default value is <code>markdown</code>, so existing conversions are unchanged.</p>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17819.md")</div>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;output&quot;: {&quot;format&quot;: &quot;text&quot;}}&#x27;&#10;</code></pre>
<p>When you request text output, the <code>format</code> field of each result is set to <code>text</code>. For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#output">Conversion Options</a>.</p>


<h2 id="workers-ai-tomarkdown-and-ai-search-now-supports-gif-and-bmp-image-conversion"><a href="/changelog/post/2026-07-08-gif-bmp-image-support/">Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion</a></h2>
<p><em>2026-07-08</em></p>
<p>Workers AI <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> (<code>toMarkdown</code>) now supports <code>.gif</code> and <code>.bmp</code> image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.</p>
<p>GIF and BMP files run through the same <a href="/workers-ai/features/markdown-conversion/how-it-works/#images">image pipeline</a> as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.</p>
<p><a href="/ai-search/">AI Search</a> uses <code>toMarkdown</code> automatically to process the files it ingests, so any <code>.gif</code> and <code>.bmp</code> files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.</p>
<p>Learn more about <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> and the full list of <a href="/ai-search/configuration/data-source/#supported-file-types">AI Search's supported file types</a>.</p>


<h2 id="moondream-3-1-now-available-on-workers-ai"><a href="/changelog/post/2026-07-08-moondream3.1-workers-ai/">Moondream 3.1 now available on Workers AI</a></h2>
<p><em>2026-07-08</em></p>
<p>Partnering with <a href="https://moondream.ai/">Moondream</a> to bring their latest model <a href="/workers-ai/models/moondream3.1-9B-A2B/"><code>@cf/moondream/moondream3.1-9B-A2B</code></a> to Workers AI. Moondream 3.1 is a fast vision language model built on a mixture-of-experts architecture with 9B total parameters and 2B active, delivering frontier-level visual reasoning while retaining fast, cost-efficient inference.</p>
<p>Moondream 3.1 is designed for real-world vision tasks, with a 32K token context window for handling complex queries and structured outputs.</p>
<h4 id="2026-07-08-moondream3.1-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Query</strong> — ask open-ended questions about an image, with an optional reasoning parameter</li>
<li><strong>Caption</strong> — generate short, normal, or long descriptions of an image</li>
<li><strong>Point</strong> — return coordinates for objects matching a target phrase</li>
<li><strong>Detect</strong> — return bounding boxes for objects matching a target phrase</li>
</ul>
<h4 id="2026-07-08-moondream3.1-workers-ai-real-time-vision-at-the-edge">Real-time vision at the edge</h4>
<p>Vision workloads like live camera feeds, robotics, content moderation, and interactive agents need answers in milliseconds, not seconds. Moondream 3.1's small active footprint (2B active parameters) pairs well with Workers AI's serverless, globally distributed inference: requests run close to your users, and streaming responses start returning tokens almost immediately.</p>
<p>In our testing, first tokens streamed back in roughly 20–30 ms, and results were fast across every task. The example end-to-end times below (client-observed median, including network round trip) are for a simple, single-subject image. Actual latency depends heavily on the image and how much detail you ask for.</p>
<table>
<thead>
<tr>
<th>Task</th>
<th>End-to-end (p50)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>query</code></td>
<td>~770 ms</td>
</tr>
<tr>
<td><code>caption</code></td>
<td>~480 ms</td>
</tr>
<tr>
<td><code>point</code></td>
<td>~145 ms</td>
</tr>
<tr>
<td><code>detect</code></td>
<td>~160 ms</td>
</tr>
</tbody>
</table>
<p>At these speeds you can call the model inline while handling a request rather than pushing the work to a background queue or a separate service. That opens up use cases where a slow response breaks the experience: moderating user-uploaded images before they are stored, locating an object in a video frame to drive a live overlay, extracting fields from a document during a form submission, or letting an agent inspect a screenshot and decide its next step within a single turn.</p>
<h4 id="2026-07-08-moondream3.1-workers-ai-get-started">Get started</h4>
<p>Use Moondream 3.1 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>) or the REST API at <code>/ai/run</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/moondream3.1-9B-A2B/">Moondream 3.1 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="introducing-glm-5-2-on-workers-ai"><a href="/changelog/post/2026-06-16-glm-5.2-workers-ai/">Introducing GLM-5.2 on Workers AI</a></h2>
<p><em>2026-06-16</em></p>
<p>We are excited to announce <strong>GLM-5.2</strong> on Workers AI, Z.ai's flagship agentic coding model.</p>
<p><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a> is a text generation model built for agentic coding workflows. With function calling and reasoning support, it can handle long codebases, multi-step planning, and tool-augmented agents.</p>
<p><strong>Key features and use cases:</strong></p>
<ul>
<li><strong>Agentic coding</strong>: Designed for autonomous coding tasks, long-horizon planning, and complex software engineering workflows</li>
<li><strong>Large context window</strong>: GLM-5.2 supports up to a 1,048,576 token context window. Workers AI is launching the model with a 262,144 token context window and plans to increase this in the future</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns</li>
<li><strong>Reasoning</strong>: Tackles complex problem-solving and step-by-step reasoning tasks</li>
</ul>
<p>Use GLM-5.2 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-5.2/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>


<h2 id="moonshot-ai-kimi-k2-7-code-now-available-on-workers-ai"><a href="/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/">Moonshot AI Kimi K2.7 Code now available on Workers AI</a></h2>
<p><em>2026-06-12</em></p>
<p><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a> is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-improved-coding-and-agent-performance">Improved coding and agent performance</h4>
<p>K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:</p>
<ul>
<li><strong>+21.8%</strong> on Kimi Code Bench v2</li>
<li><strong>+11.0%</strong> on Program Bench</li>
<li><strong>+31.5%</strong> on MLS Bench Lite</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-reasoning-efficiency">Reasoning efficiency</h4>
<p>K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with improved instruction following and higher end-to-end coding task success rates</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth via <code>chat_template_kwargs.thinking</code></li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Structured outputs</strong> with JSON schema support</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-differences-from-kimi-k2-6">Differences from Kimi K2.6</h4>
<p>If you are migrating from Kimi K2.6, note the following:</p>
<ul>
<li>K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency</li>
<li>Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)</li>
<li>API usage is identical — no parameter changes required</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.7 Code through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.7-code/">Kimi K2.7 Code model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="planned-model-deprecations-on-workers-ai"><a href="/changelog/post/2026-05-08-planned-model-deprecations/">Planned model deprecations on Workers AI</a></h2>
<p><em>2026-05-08</em></p>
<p>We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date.</p>
<h4 id="2026-05-08-planned-model-deprecations-recommended-replacements">Recommended replacements</h4>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> — fast multilingual model with multi-turn tool calling and coding capabilities.</li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> — efficient open model with vision and tool calling.</li>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> — capable tool-calling and vision model for agentic workloads and coding.</li>
</ul>
<p>For pricing, refer to the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<h4 id="2026-05-08-planned-model-deprecations-kimi-k2-5">Kimi K2.5</h4>
<p>We originally stated Kimi K2.5 would be deprecated on May 10, 2026, however we have extended the deprecation date to May 30, 2026. Requests will be automatically aliased to Kimi K2.6 on May 30, 2026, which has a higher price. Please review the <a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> pricing and model capabilities prior to May 30, 2026 to ensure that the model suits your needs.</p>
<h4 id="2026-05-08-planned-model-deprecations-models-deprecated-on-may-30-2026">Models deprecated on May 30, 2026</h4>
<ul>
<li><code>@cf/moonshotai/kimi-k2.5</code> --&gt; <code>@cf/moonshotai/kimi-k2.6</code></li>
<li><code>@hf/meta-llama/meta-llama-3-8b-instruct</code></li>
<li><code>@cf/meta/llama-3-8b-instruct</code></li>
<li><code>@cf/meta/llama-3-8b-instruct-awq</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct-awq</code></li>
<li><code>@cf/meta/llama-3.1-70b-instruct</code></li>
<li><code>@cf/meta/llama-2-7b-chat-int8</code></li>
<li><code>@cf/meta/llama-2-7b-chat-fp16</code></li>
<li><code>@cf/mistral/mistral-7b-instruct-v0.1</code></li>
<li><code>@hf/mistral/mistral-7b-instruct-v0.2</code></li>
<li><code>@hf/google/gemma-7b-it</code></li>
<li><code>@cf/google/gemma-3-12b-it</code></li>
<li><code>@hf/nousresearch/hermes-2-pro-mistral-7b</code></li>
<li><code>@cf/microsoft/phi-2</code></li>
<li><code>@cf/defog/sqlcoder-7b-2</code></li>
<li><code>@cf/unum/uform-gen2-qwen-500m</code></li>
<li><code>@cf/facebook/bart-large-cnn</code></li>
</ul>
<h4 id="2026-05-08-planned-model-deprecations-variants-that-remain-active">Variants that remain active</h4>
<p>The <code>-fast</code> and <code>-lora</code> variants of models will remain active, including:</p>
<ul>
<li><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct-fast</code></li>
<li><code>@cf/google/gemma-7b-it-lora</code></li>
<li><code>@cf/google/gemma-2b-it-lora</code></li>
<li><code>@cf/mistral/mistral-7b-instruct-v0.2-lora</code></li>
<li><code>@cf/meta-llama/llama-2-7b-chat-hf-lora</code></li>
</ul>
<p>LoRA models may be deprecated in the future. We will be adding more LoRA capabilities to the catalog, and will communicate when new LoRA models come online to give users time to train new LoRAs before we deprecate old ones.</p>
<p>For the full list of available models, refer to the <a href="/workers-ai/models/">Workers AI model catalog</a>.</p>


<h2 id="moonshot-ai-kimi-k2-6-now-available-on-workers-ai"><a href="/changelog/post/2026-04-20-kimi-k2-6-workers-ai/">Moonshot AI Kimi K2.6 now available on Workers AI</a></h2>
<p><em>2026-04-20</em></p>
<p><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.</p>
<p>Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).</p>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python</li>
<li><strong>Coding-driven design</strong> that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows</li>
<li><strong>Agent swarm orchestration</strong> scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-differences-from-kimi-k2-5">Differences from Kimi K2.5</h4>
<p>If you are migrating from Kimi K2.5, note the following API changes:</p>
<ul>
<li>K2.6 uses <code>chat_template_kwargs.thinking</code> to control reasoning, replacing <code>chat_template_kwargs.enable_thinking</code></li>
<li>K2.6 returns reasoning content in the <code>reasoning</code> field, replacing <code>reasoning_content</code></li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.6 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.6/">Kimi K2.6 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="google-gemma-4-26b-a4b-now-available-on-workers-ai"><a href="/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/">Google Gemma 4 26B A4B now available on Workers AI</a></h2>
<p><em>2026-04-04</em></p>
<p>We are partnering with Google to bring <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> to Workers AI. Gemma 4 26B A4B is a Mixture-of-Experts (MoE) model built from Gemini 3 research, with 26B total parameters and only 4B active per forward pass. By activating a small subset of parameters during inference, the model runs almost as fast as a 4B-parameter model while delivering the quality of a much larger one.</p>
<p>Gemma 4 is Google's most capable family of open models, designed to maximize intelligence-per-parameter.</p>
<h4 id="2026-04-04-gemma-4-26b-a4b-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Mixture-of-Experts architecture</strong> with 8 active experts out of 128 total (plus 1 shared expert), delivering frontier-level performance at a fraction of the compute cost of dense models</li>
<li><strong>256,000 token context window</strong> for retaining full conversation history, tool definitions, and long documents across extended sessions</li>
<li><strong>Built-in thinking mode</strong> that lets the model reason step-by-step before answering, improving accuracy on complex tasks</li>
<li><strong>Vision understanding</strong> for object detection, document and PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), and handwriting recognition, with support for variable aspect ratios and resolutions</li>
<li><strong>Function calling</strong> with native support for structured tool use, enabling agentic workflows and multi-step planning</li>
<li><strong>Multilingual</strong> with out-of-the-box support for 35+ languages, pre-trained on 140+ languages</li>
<li><strong>Coding</strong> for code generation, completion, and correction</li>
</ul>
<p>Use Gemma 4 26B A4B through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/gemma-4-26b-a4b-it/">Gemma 4 26B A4B model page</a>.</p>


<h2 id="moonshot-ai-kimi-k2-5-now-available-on-workers-ai"><a href="/changelog/post/2026-03-19-kimi-k2-5-workers-ai/">Moonshot AI Kimi K2.5 now available on Workers AI</a></h2>
<p><em>2026-03-19</em></p>
<p>Workers AI is officially in the big models game. <a href="/workers-ai/models/kimi-k2.5/"><code>@cf/moonshotai/kimi-k2.5</code></a> is the first frontier-scale open-source model on our AI inference platform — a large model with a full 256k context window, multi-turn tool calling, vision inputs, and structured outputs. By bringing a frontier-scale model directly onto the Cloudflare Developer Platform, you can now run the entire agent lifecycle on a single, unified platform.</p>
<p>The model has proven to be a fast, efficient alternative to larger proprietary models without sacrificing quality. As AI adoption increases, the volume of inference is skyrocketing — now you can access frontier intelligence at a fraction of the cost.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>256,000 token context window</strong> for retaining full conversation history, tool definitions, and entire codebases across long-running agent sessions</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Structured outputs</strong> with JSON mode and JSON Schema support for reliable downstream parsing</li>
<li><strong>Function calling</strong> for integrating external tools and APIs into agent workflows</li>
</ul>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-prefix-caching-and-session-affinity">Prefix caching and session affinity</h4>
<p>When an agent sends a new prompt, it resends all previous prompts, tools, and context from the session. The delta between consecutive requests is usually just a few new lines of input. Prefix caching avoids reprocessing the shared context, saving time and compute from the prefill stage. This means faster Time to First Token (TTFT) and higher Tokens Per Second (TPS) throughput.</p>
<p>Workers AI has done prefix caching, but we are now surfacing cached tokens as a usage metric and offering a discount on cached tokens compared to input tokens (pricing is listed on the <a href="/workers-ai/models/kimi-k2.5/">model page</a>).</p>
<pre><code class="language-bash">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/moonshotai/kimi-k2.5&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;x-session-affinity: ses_12345678&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is prefix caching and why does it matter?&quot;&#10;      }&#10;    ],&#10;    &quot;max_tokens&quot;: 2400,&#10;    &quot;stream&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>Some clients like <a href="https://opencode.ai">OpenCode</a> implement session affinity automatically. The <a href="https://github.com/cloudflare/agents">Agents SDK</a> starter also sets up the wiring for you.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-redesigned-asynchronous-api">Redesigned asynchronous API</h4>
<p>For volumes of requests that exceed synchronous rate limits, you can submit batches of inferences to be completed asynchronously. We have revamped the <a href="/workers-ai/features/batch-api/">Asynchronous Batch API</a> with a pull-based system that processes queued requests as soon as capacity is available. With internal testing, async requests usually execute within 5 minutes, but this depends on live traffic.</p>
<p>The async API is the best way to avoid capacity errors in durable workflows. It is ideal for use cases that are not real-time, such as code scanning agents or research agents.</p>
<p>To use the asynchronous API, pass <code>queueRequest: true</code>:</p>
<pre><code class="language-js">// 1. Push a batch of requests into the queue&#10;const res = await env.AI.run(&#10;	&quot;@cf/moonshotai/kimi-k2.5&quot;,&#10;	{&#10;		requests: [&#10;			{&#10;				messages: [{ role: &quot;user&quot;, content: &quot;Tell me a joke&quot; }],&#10;			},&#10;			{&#10;				messages: [{ role: &quot;user&quot;, content: &quot;Explain the Pythagoras theorem&quot; }],&#10;			},&#10;		],&#10;	},&#10;	{ queueRequest: true },&#10;);&#10;&#10;// 2. Grab the request ID&#10;const requestId = res.request_id;&#10;&#10;// 3. Poll for the result&#10;const result = await env.AI.run(&quot;@cf/moonshotai/kimi-k2.5&quot;, {&#10;	request_id: requestId,&#10;});&#10;&#10;if (result.status === &quot;queued&quot; || result.status === &quot;running&quot;) {&#10;	// Retry by polling again&#10;} else {&#10;	return Response.json(result);&#10;}&#10;</code></pre>
<p>You can also set up <a href="/workers-ai/platform/event-subscriptions/">event notifications</a> to know when inference is complete instead of polling.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.5 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.5/">Kimi K2.5 model page</a>, <a href="/workers-ai/platform/pricing/">pricing</a>, and <a href="/workers-ai/features/prompt-caching/">prompt caching</a>.</p>


<h2 id="nvidia-nemotron-3-super-now-available-on-workers-ai"><a href="/changelog/post/2026-03-11-nemotron-3-super-workers-ai/">NVIDIA Nemotron 3 Super now available on Workers AI</a></h2>
<p><em>2026-03-11</em></p>
<p>We're excited to partner with NVIDIA to bring <a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a> to Workers AI. NVIDIA Nemotron 3 Super is a Mixture-of-Experts (MoE) model with a hybrid Mamba-transformer architecture, 120B total parameters, and 12B active parameters per forward pass.</p>
<p>The model is optimized for running many collaborating agents per application. It delivers high accuracy for reasoning, tool calling, and instruction following across complex multi-step tasks.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Hybrid Mamba-transformer architecture</strong> delivers over 50% higher token generation throughput compared to leading open models, reducing latency for real-world applications</li>
<li><strong>Tool calling</strong> support for building AI agents that invoke tools across multiple conversation turns</li>
<li><strong>Multi-Token Prediction (MTP)</strong> accelerates long-form text generation by predicting several future tokens simultaneously in a single forward pass</li>
<li><strong>32,000 token context window</strong> for retaining conversation history and plan states across multi-step agent workflows</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-03-11-nemotron-3-super-workers-ai-prompt-caching">Prompt caching</h4>
@markup("md", "content/.markup/bodies/17818.md")</aside>
<p>Use Nemotron 3 Super through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/nemotron-3-120b-a12b/">Nemotron 3 Super model page</a>.</p>


<h2 id="real-time-transcription-in-realtimekit-now-supports-10-languages-with-regional-variants"><a href="/changelog/post/2026-03-06-realtimekit-multilingual-transcription/">Real-time transcription in RealtimeKit now supports 10 languages with regional variants</a></h2>
<p><em>2026-03-06</em></p>
<p><a href="/realtime/realtimekit/ai/transcription/">Real-time transcription</a> in RealtimeKit now supports 10 languages with regional variants, powered by <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> running on <a href="/workers-ai/">Workers AI</a>.</p>
<p>During a meeting, participant audio is routed through <a href="/ai-gateway/">AI Gateway</a> to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.</p>
<p>Set the language when <a href="/realtime/realtimekit/concepts/meeting/">creating a meeting</a> via <code>ai_config.transcription.language</code>:</p>
<pre><code class="language-json">{&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;fr&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like <code>en-AU</code>, <code>en-GB</code>, <code>en-IN</code>, <code>en-NZ</code>, <code>es-419</code>, <code>fr-CA</code>, <code>de-CH</code>, <code>pt-BR</code>, and <code>pt-PT</code>. Use <code>multi</code> for automatic multilingual detection.</p>
<p>If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.</p>
<ul>
<li><a href="/realtime/realtimekit/ai/transcription/">Transcription docs</a></li>
<li><a href="/workers-ai/models/nova-3/">Nova-3 model page</a></li>
<li><a href="/workers-ai/">Workers AI</a></li>
<li><a href="/ai-gateway/">AI Gateway</a></li>
</ul>


<h2 id="new-conversion-options-for-markdown-conversion"><a href="/changelog/post/2026-03-04-new-markdown-conversion-options/">New conversion options for Markdown Conversion</a></h2>
<p><em>2026-03-04</em></p>
<p>You can now customize how the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service processes different file types by passing a <code>conversionOptions</code> object.</p>
<p>Available options:</p>
<ul>
<li><strong>Images</strong>: Set the language for AI-generated image descriptions</li>
<li><strong>HTML</strong>: Use CSS selectors to extract specific content, or provide a hostname to resolve relative links</li>
<li><strong>PDF</strong>: Exclude metadata from the output</li>
</ul>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17817.md")</div>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;html&quot;: {&quot;cssSelector&quot;: &quot;article.content&quot;}}&#x27;&#10;</code></pre>
<p>For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion Options</a>.</p>


<h2 id="ai-dashboard-experience-improvements"><a href="/changelog/post/2026-02-19-ai-dashboard-experience-improvements/">AI dashboard experience improvements</a></h2>
<p><em>2026-02-19</em></p>
<p><a href="/workers-ai/">Workers AI</a> and <a href="/ai-gateway/">AI Gateway</a> have received a series of dashboard improvements to help you get started faster and manage your AI workloads more easily.</p>
<p><strong>Navigation and discoverability</strong></p>
<p>AI now has its own top-level section in the Cloudflare dashboard sidebar, so you can find AI features without digging through menus.</p>
<p><img src="/assets/upstream/images/ai-gateway/sidebar-navigation.png" alt="AI sidebar navigation in the Cloudflare dashboard" />
<em>The new top-level AI section in the dashboard sidebar.</em></p>
<p><strong>Onboarding and getting started</strong></p>
<p><a href="/ai-gateway/get-started/">Getting started</a> with AI Gateway is now simpler. When you create your first gateway, we now show your gateway's OpenAI-compatible endpoint and step-by-step guidance to help you configure it. The Playground also includes helpful prompts, and usage pages have clear next steps if you have not made any requests yet.</p>
<p><img src="/assets/upstream/images/ai-gateway/onboarding-flow.png" alt="AI Gateway onboarding flow" />
<em>The first-run setup experience for new gateways.</em></p>
<p>We've also combined the previously separate code example sections into one view with dropdown selectors for API type, provider, SDK, and authentication method so you can now customize the exact code snippet you need from one place.</p>
<p><strong>Dynamic Routing</strong></p>
<ul>
<li>The <a href="/ai-gateway/features/dynamic-routing/">route builder</a> is now more performant and responsive.</li>
<li>You can now copy route names to your clipboard with a single click.</li>
<li>Code examples use the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> format, making it easier to integrate routes into your application.</li>
</ul>
<p><strong>Observability and analytics</strong></p>
<ul>
<li>Small monetary values now display correctly in <a href="/ai-gateway/observability/costs/">cost analytics</a> charts, so you can accurately track spending at any scale.</li>
</ul>
<p><strong>Accessibility</strong></p>
<ul>
<li>Improvements to keyboard navigation within the AI Gateway, specifically when exploring usage by <a href="/ai-gateway/usage/providers/">provider</a>.</li>
<li>Improvements to sorting and filtering components on the <a href="/workers-ai/models/">Workers AI</a> models page.</li>
</ul>
<p>For more information, refer to the <a href="/ai-gateway/">AI Gateway documentation</a>.</p>


<h2 id="introducing-glm-4-7-flash-on-workers-ai-cloudflare-tanstack-ai-and-workers-ai-provider-v3-1-1"><a href="/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/">Introducing GLM-4.7-Flash on Workers AI, @cloudflare/tanstack-ai, and workers-ai-provider v3.1.1</a></h2>
<p><em>2026-02-13</em></p>
<p>We're excited to announce <strong>GLM-4.7-Flash</strong> on Workers AI, a fast and efficient text generation model optimized for multilingual dialogue and instruction-following tasks, along with the brand-new <a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai"><strong>@cloudflare/tanstack-ai</strong></a> package and <a href="https://www.npmjs.com/package/workers-ai-provider"><strong>workers-ai-provider v3.1.1</strong></a>.</p>
<p>You can now run AI agents entirely on Cloudflare. With GLM-4.7-Flash's multi-turn tool calling support, plus full compatibility with TanStack AI and the Vercel AI SDK, you have everything you need to build agentic applications that run completely at the edge.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-glm-4-7-flash-multilingual-text-generation-model">GLM-4.7-Flash — Multilingual Text Generation Model</h4>
<p><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> is a multilingual model with a 131,072 token context window, making it ideal for long-form content generation, complex reasoning tasks, and multilingual applications.</p>
<p><strong>Key Features and Use Cases:</strong></p>
<ul>
<li><strong>Multi-turn Tool Calling for Agents</strong>: Build AI agents that can call functions and tools across multiple conversation turns</li>
<li><strong>Multilingual Support</strong>: Built to handle content generation in multiple languages effectively</li>
<li><strong>Large Context Window</strong>: 131,072 tokens for long-form writing, complex reasoning, and processing long documents</li>
<li><strong>Fast Inference</strong>: Optimized for low-latency responses in chatbots and virtual assistants</li>
<li><strong>Instruction Following</strong>: Excellent at following complex instructions for code generation and structured tasks</li>
</ul>
<p>Use GLM-4.7-Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via <a href="/workers-ai/configuration/ai-sdk/">workers-ai-provider</a> for the Vercel AI SDK.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-4.7-flash/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-cloudflare-tanstack-ai-v0-1-1-tanstack-ai-adapters-for-workers-ai-and-ai-gateway">@cloudflare/tanstack-ai v0.1.1 — TanStack AI adapters for Workers AI and AI Gateway</h4>
<p>We've released <code>@cloudflare/tanstack-ai</code>, a new package that brings Workers AI and AI Gateway support to <a href="https://tanstack.com/ai">TanStack AI</a>. This provides a framework-agnostic alternative for developers who prefer TanStack's approach to building AI applications.</p>
<p><strong>Workers AI adapters</strong> support four configuration modes — plain binding (<code>env.AI</code>), plain REST, AI Gateway binding (<code>env.AI.gateway(id)</code>), and AI Gateway REST — across all capabilities:</p>
<ul>
<li><strong>Chat</strong> (<code>createWorkersAiChat</code>) — Streaming chat completions with tool calling, structured output, and reasoning text streaming.</li>
<li><strong>Image generation</strong> (<code>createWorkersAiImage</code>) — Text-to-image models.</li>
<li><strong>Transcription</strong> (<code>createWorkersAiTranscription</code>) — Speech-to-text.</li>
<li><strong>Text-to-speech</strong> (<code>createWorkersAiTts</code>) — Audio generation.</li>
<li><strong>Summarization</strong> (<code>createWorkersAiSummarize</code>) — Text summarization.</li>
</ul>
<p><strong>AI Gateway adapters</strong> route requests from third-party providers — OpenAI, Anthropic, Gemini, Grok, and OpenRouter — through Cloudflare AI Gateway for caching, rate limiting, and unified billing.</p>
<p>To get started:</p>
<pre><code class="language-sh">npm install @cloudflare/tanstack-ai @tanstack/ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-workers-ai-provider-v3-1-1-transcription-speech-reranking-and-reliability">workers-ai-provider v3.1.1 — transcription, speech, reranking, and reliability</h4>
<p>The Workers AI provider for the <a href="https://ai-sdk.dev">Vercel AI SDK</a> now supports three new capabilities beyond chat and image generation:</p>
<ul>
<li><strong>Transcription</strong> (<code>provider.transcription(model)</code>) — Speech-to-text with automatic handling of model-specific input formats across binding and REST paths.</li>
<li><strong>Text-to-speech</strong> (<code>provider.speech(model)</code>) — Audio generation with support for voice and speed options.</li>
<li><strong>Reranking</strong> (<code>provider.reranking(model)</code>) — Document reranking for RAG pipelines and search result ordering.</li>
</ul>
<pre><code class="language-typescript">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import {&#10;	experimental_transcribe,&#10;	experimental_generateSpeech,&#10;	rerank,&#10;} from &quot;ai&quot;;&#10;&#10;const workersai = createWorkersAI({ binding: env.AI });&#10;&#10;const transcript = await experimental_transcribe({&#10;	model: workersai.transcription(&quot;@cf/openai/whisper-large-v3-turbo&quot;),&#10;	audio: audioData,&#10;	mediaType: &quot;audio/wav&quot;,&#10;});&#10;&#10;const speech = await experimental_generateSpeech({&#10;	model: workersai.speech(&quot;@cf/deepgram/aura-1&quot;),&#10;	text: &quot;Hello world&quot;,&#10;	voice: &quot;asteria&quot;,&#10;});&#10;&#10;const ranked = await rerank({&#10;	model: workersai.reranking(&quot;@cf/baai/bge-reranker-base&quot;),&#10;	query: &quot;What is machine learning?&quot;,&#10;	documents: [&quot;ML is a branch of AI.&quot;, &quot;The weather is sunny.&quot;],&#10;});&#10;</code></pre>
<p>This release also includes a comprehensive reliability overhaul (v3.0.5):</p>
<ul>
<li><strong>Fixed streaming</strong> — Responses now stream token-by-token instead of buffering all chunks, using a proper <code>TransformStream</code> pipeline with backpressure.</li>
<li><strong>Fixed tool calling</strong> — Resolved issues with tool call ID sanitization, conversation history preservation, and a heuristic that silently fell back to non-streaming mode when tools were defined.</li>
<li><strong>Premature stream termination detection</strong> — Streams that end unexpectedly now report <code>finishReason: &quot;error&quot;</code> instead of silently reporting <code>&quot;stop&quot;</code>.</li>
<li><strong>AI Search support</strong> — Added <code>createAISearch</code> as the canonical export (renamed from AutoRAG). <code>createAutoRAG</code> still works with a deprecation warning.</li>
</ul>
<p>To upgrade:</p>
<pre><code class="language-sh">npm install workers-ai-provider@latest ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-resources">Resources</h4>
<ul>
<li><a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai">@cloudflare/tanstack-ai on npm</a></li>
<li><a href="https://www.npmjs.com/package/workers-ai-provider">workers-ai-provider on npm</a></li>
<li><a href="https://github.com/cloudflare/ai">GitHub repository</a></li>
</ul>


<h2 id="launching-flux-2-klein-9b-on-workers-ai"><a href="/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/">Launching FLUX.2 [klein] 9B on Workers AI</a></h2>
<p><em>2026-01-28</em></p>
<p>We have partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 9B model to Workers AI. This distilled model offers enhanced quality compared to the 4B variant, while maintaining cost-effective pricing. With a fixed 4-step inference process, Klein 9B is ideal for rapid prototyping and real-time applications where both speed and quality matter.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-9b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-workers-ai-platform-specifics">Workers AI platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev] and FLUX.2 [klein] 4B, this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-multi-reference-images">Multi-reference images</h4>
<p>The FLUX.2 klein-9b model supports generating images based on reference images, just like FLUX.2 [dev] and FLUX.2 [klein] 4B. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.</p>
<p>For the prompt, you can reference the images based on the index, like <code>take the subject of image 1 and style it like image 0</code> or even use natural language like <code>place the dog beside the woman</code>.</p>
<p>You must name the input parameter as <code>input_image_0</code>, <code>input_image_1</code>, <code>input_image_2</code>, <code>input_image_3</code> for it to work correctly. All input images must be smaller than 512x512.</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=take the subject of image 1 and style it like image 0&#x27; \&#10;  &#45;-form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \&#10;  &#45;-form input_image_1=@/Users/johndoe/Desktop/me.png \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>Through Workers AI Binding:</p>
<pre><code class="language-javascript">//helper function to convert ReadableStream to Blob&#10;async function streamToBlob(stream: ReadableStream, contentType: string): Promise&lt;Blob&gt; {&#10;  const reader = stream.getReader();&#10;  const chunks = [];&#10;&#10;  while (true) {&#10;    const { done, value } = await reader.read();&#10;    if (done) break;&#10;    chunks.push(value);&#10;  }&#10;&#10;  return new Blob(chunks, { type: contentType });&#10;}&#10;&#10;const image0 = await fetch(&quot;http://image-url&quot;);&#10;const image1 = await fetch(&quot;http://image-url&quot;);&#10;const form = new FormData();&#10;&#10;const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);&#10;const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);&#10;form.append(&#x27;input_image_0&#x27;, image_blob0)&#10;form.append(&#x27;input_image_1&#x27;, image_blob1)&#10;form.append(&#x27;prompt&#x27;, &#x27;take the subject of image 1 and style it like image 0&#x27;)&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;    multipart: {&#10;        body: formStream,&#10;        contentType: formContentType&#10;    }&#10;})&#10;</code></pre>


<h2 id="launching-flux-2-klein-4b-on-workers-ai"><a href="/changelog/post/2026-01-15-flux-2-klein-4b-workers-ai/">Launching FLUX.2 [klein] 4B on Workers AI</a></h2>
<p><em>2026-01-15</em></p>
<p>We've partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 4B model to Workers AI! This distilled model offers faster generation and cost-effective pricing, while maintaining great output quality. With a fixed 4-step inference process, Klein 4B is ideal for rapid prototyping and real-time applications where speed matters.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-4b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-15-flux-2-klein-4b-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev], this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<pre><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 klein-4b model supports generating images based on reference images, just like FLUX.2 [dev]. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-klein-4b">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form width=1024 <br />
--form height=1024</p>
<pre><code>&#10;Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1 and style it like image 0')</p>
<p>// FormData doesn't expose its serialized body or boundary. Passing it to a
// Request (or Response) constructor serializes it and generates the Content-Type
// header with the boundary, which is required for the server to parse the multipart fields.
const formResponse = new Response(form);
const formStream = formResponse.body;
const formContentType = formResponse.headers.get('content-type');</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {
multipart: {
body: formStream,
contentType: formContentType
}
})</p>
<pre><code></code></pre>


<h2 id="launching-flux-2-dev-on-workers-ai"><a href="/changelog/post/2025-11-25-flux-2-dev-workers-ai/">Launching FLUX.2 [dev] on Workers AI</a></h2>
<p><em>2025-11-25</em></p>
<p>We've partnered with Black Forest Labs (BFL) to bring their latest FLUX.2 [dev] model to Workers AI! This model excels in generating high-fidelity images with physical world grounding, multi-language support, and digital asset creation. You can also create specific super images with granular controls like JSON prompting.</p>
<p>Read the <a href="https://bfl.ai/flux2">BFL blog</a> to learn more about the model itself. Read our <a href="https://blog.cloudflare.com/flux-2-workers-ai">Cloudflare blog</a> to see the model in action, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-dev/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>. Note, we expect to drop pricing in the next few days after iterating on the model performance.</p>
<h4 id="2025-11-25-flux-2-dev-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is able to support up to 4 image inputs (512x512 per input image). Note, this image model is one of the most powerful in the catalog and is expected to be slower than the other image models we currently support. One catch to look out for is that this model takes multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form steps=25&#10;  &#45;-form width=1024&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">&#10;const form = new FormData();&#10;form.append(&#x27;prompt&#x27;, &#x27;a sunset with a dog&#x27;);&#10;form.append(&#x27;width&#x27;, &#x27;1024&#x27;);&#10;form.append(&#x27;height&#x27;, &#x27;1024&#x27;);&#10;&#10;//this dummy request is temporary hack&#10;//we&#x27;re pushing a change to address this soon&#10;const formRequest = new Request(&#x27;http://dummy&#x27;, {&#10;  method: &#x27;POST&#x27;,&#10;  body: form&#10;});&#10;const formStream = formRequest.body;&#10;const formContentType = formRequest.headers.get(&#x27;content-type&#x27;) || &#x27;multipart/form-data&#x27;;&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {&#10;  multipart: {&#10;    body: formStream,&#10;    contentType: formContentType&#10;  }&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>steps</code> (integer) - Number of inference steps. Higher values may improve quality but increase generation time</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
</details>
<pre><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 model is great at generating images based on reference images. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generate images. You would use it with the same multipart form data structure, with the input images in binary.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-dev">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form steps=25
--form width=1024
--form height=1024</p>
<pre><code>Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1and style it like image 0')</p>
<p>//this dummy request is temporary hack
//we're pushing a change to address this soon
const formRequest = new Request('<a href="http://dummy">http://dummy</a>', {
method: 'POST',
body: form
});
const formStream = formRequest.body;
const formContentType = formRequest.headers.get('content-type') || 'multipart/form-data';</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {
multipart: {
body: form,
contentType: &quot;multipart/form-data&quot;
}
})</p>
<pre><code>&#10;&#35;# JSON Prompting&#10;&#10;The model supports prompting in JSON to get more granular control over images. You would pass the JSON as the value of the &#x27;prompt&#x27; field in the multipart form data. See the JSON schema below on the base parameters you can pass to the model.&#10;&#10;&lt;details&gt;&#10;  &lt;summary&gt;JSON Prompting Schema&lt;/summary&gt;&#10;</code></pre>
<p>{
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;scene&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Overall scene setting or location&quot;
},
&quot;subjects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;type&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Type of subject (e.g., desert nomad, blacksmith, DJ, falcon)&quot;
},
&quot;description&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Physical attributes, clothing, accessories&quot;
},
&quot;pose&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Action or stance&quot;
},
&quot;position&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;foreground&quot;, &quot;midground&quot;, &quot;background&quot;],
&quot;description&quot;: &quot;Depth placement in scene&quot;
}
},
&quot;required&quot;: [&quot;type&quot;, &quot;description&quot;, &quot;pose&quot;, &quot;position&quot;]
}
},
&quot;style&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Artistic rendering style (e.g., digital painting, photorealistic, pixel art, noir sci-fi, lifestyle photo, wabi-sabi photo)&quot;
},
&quot;color_palette&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;minItems&quot;: 3,
&quot;maxItems&quot;: 3,
&quot;description&quot;: &quot;Exactly 3 main colors for the scene (e.g., ['navy', 'neon yellow', 'magenta'])&quot;
},
&quot;lighting&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Lighting condition and direction (e.g., fog-filtered sun, moonlight with star glints, dappled sunlight)&quot;
},
&quot;mood&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Emotional atmosphere (e.g., harsh and determined, playful and modern, peaceful and dreamy)&quot;
},
&quot;background&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Background environment details&quot;
},
&quot;composition&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [
&quot;rule of thirds&quot;,
&quot;circular arrangement&quot;,
&quot;framed by foreground&quot;,
&quot;minimalist negative space&quot;,
&quot;S-curve&quot;,
&quot;vanishing point center&quot;,
&quot;dynamic off-center&quot;,
&quot;leading leads&quot;,
&quot;golden spiral&quot;,
&quot;diagonal energy&quot;,
&quot;strong verticals&quot;,
&quot;triangular arrangement&quot;
],
&quot;description&quot;: &quot;Compositional technique&quot;
},
&quot;camera&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;angle&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;eye level&quot;, &quot;low angle&quot;, &quot;slightly low&quot;, &quot;bird's-eye&quot;, &quot;worm's-eye&quot;, &quot;over-the-shoulder&quot;, &quot;isometric&quot;],
&quot;description&quot;: &quot;Camera perspective&quot;
},
&quot;distance&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;close-up&quot;, &quot;medium close-up&quot;, &quot;medium shot&quot;, &quot;medium wide&quot;, &quot;wide shot&quot;, &quot;extreme wide&quot;],
&quot;description&quot;: &quot;Framing distance&quot;
},
&quot;focus&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;deep focus&quot;, &quot;macro focus&quot;, &quot;selective focus&quot;, &quot;sharp on subject&quot;, &quot;soft background&quot;],
&quot;description&quot;: &quot;Focus type&quot;
},
&quot;lens&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;14mm&quot;, &quot;24mm&quot;, &quot;35mm&quot;, &quot;50mm&quot;, &quot;70mm&quot;, &quot;85mm&quot;],
&quot;description&quot;: &quot;Focal length (wide to telephoto)&quot;
},
&quot;f-number&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Aperture (e.g., f/2.8, the smaller the number the more blurry the background)&quot;
},
&quot;ISO&quot;: {
&quot;type&quot;: &quot;number&quot;,
&quot;description&quot;: &quot;Light sensitivity value (comfortable range between 100 &amp; 6400, lower = less sensitivity)&quot;
}
}
},
&quot;effects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;description&quot;: &quot;Post-processing effects (e.g., 'lens flare small', 'subtle film grain', 'soft bloom', 'god rays', 'chromatic aberration mild')&quot;
}
},
&quot;required&quot;: [&quot;scene&quot;, &quot;subjects&quot;]
}</p>
<pre><code>&lt;/details&gt;&#10;&#10;&#35;# Other features to try&#10;&#10;&#45; The model also supports the most common latin and non-latin character languages&#10;&#45; You can prompt the model with specific hex codes like `#2ECC71`&#10;&#45; Try creating digital assets like landing pages, comic strips, infographics too!&#10;&#10;&#10;</code></pre>
<h4 id="2025-11-25-flux-2-dev-workers-ai-json-prompting">JSON Prompting</h4><h4 id="2025-11-25-flux-2-dev-workers-ai-other-features-to-try">Other features to try</h4>

<h2 id="workers-ai-markdown-conversion-new-endpoint-to-list-supported-formats"><a href="/changelog/post/2025-10-23-new-markdown-conversion-endpoint/">Workers AI Markdown Conversion: New endpoint to list supported formats</a></h2>
<p><em>2025-10-23</em></p>
<p>Developers can now programmatically retrieve a list of all file formats supported by the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a> in Workers AI.</p>
<p>You can use the <a href="/workers-ai/configuration/bindings/"><code>env.AI</code></a> binding:</p>
<pre><code class="language-typescript">await env.AI.toMarkdown().supported()&#10;</code></pre>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27;&#10;</code></pre>
<p>Both return a list of file formats that users can convert into Markdown:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;extension&quot;: &quot;.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;	},&#10;	{&#10;		&quot;extension&quot;: &quot;.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;	},&#10;	...&#10;]&#10;</code></pre>
<p>Learn more about our <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product/workers-ai/2/">Next</a></nav>
