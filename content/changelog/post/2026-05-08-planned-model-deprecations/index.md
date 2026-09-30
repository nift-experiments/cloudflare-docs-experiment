<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 8, 2026</time><h2 id="post-title">Planned model deprecations on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date.</p>
<h4 id="recommended-replacements">Recommended replacements</h4>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> — fast multilingual model with multi-turn tool calling and coding capabilities.</li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> — efficient open model with vision and tool calling.</li>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> — capable tool-calling and vision model for agentic workloads and coding.</li>
</ul>
<p>For pricing, refer to the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<h4 id="kimi-k2-5">Kimi K2.5</h4>
<p>We originally stated Kimi K2.5 would be deprecated on May 10, 2026, however we have extended the deprecation date to May 30, 2026. Requests will be automatically aliased to Kimi K2.6 on May 30, 2026, which has a higher price. Please review the <a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> pricing and model capabilities prior to May 30, 2026 to ensure that the model suits your needs.</p>
<h4 id="models-deprecated-on-may-30-2026">Models deprecated on May 30, 2026</h4>
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
<h4 id="variants-that-remain-active">Variants that remain active</h4>
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
</div></article></div>
