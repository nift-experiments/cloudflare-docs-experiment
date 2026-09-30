<h2 id="2026-06-16">2026-06-16</h2><strong>GLM-5.2 now available on Workers AI</strong><ul>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a> is now available on Workers AI. Z.ai's flagship agentic coding model with a 262,144 token context window, function calling, and reasoning support. Read <a href="/changelog/2026-06-16-glm-5.2-workers-ai/">changelog</a> to get started.</li>
</ul><h2 id="2026-06-12">2026-06-12</h2><strong>Moonshot AI Kimi K2.7 Code now available on Workers AI</strong><ul>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a> now available on Workers AI. A frontier-scale 1T parameter MoE model optimized for coding, with a 262.1k context window, vision, multi-turn tool calling, and reasoning. Read <a href="/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/">changelog</a> to get started.</li>
</ul><h2 id="2026-05-08">2026-05-08</h2><strong>Planned model deprecations</strong><ul>
<li>We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date. Refer to the <a href="/changelog/post/2026-05-08-planned-model-deprecations/">changelog</a> for full details.</li>
<li>We recommend migrating to newer models such as <a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> for fast tool-calling, <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> for an efficient open model, or <a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> for a capable tool-calling and vision model.</li>
<li>On May 30, 2026, requests to <a href="/workers-ai/models/kimi-k2.5/"><code>@cf/moonshotai/kimi-k2.5</code></a> will be automatically aliased to <a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a>, which has a higher price. The deprecation date was extended from May 10, 2026. Please review the <a href="/workers-ai/models/kimi-k2.6/">K2.6 pricing and model capabilities</a> prior to May 30, 2026.</li>
<li>On May 30, 2026, the following models will be deprecated:
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
</li>
<li>The <code>-fast</code> and <code>-lora</code> variants of models will remain active. LoRA models may be deprecated in the future, and we will communicate when new LoRA models come online to give users time to train new LoRAs before we deprecate old ones.</li>
</ul><h2 id="2026-04-20">2026-04-20</h2><strong>Moonshot AI Kimi K2.6 now available on Workers AI</strong><ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> now available on Workers AI. The latest frontier-scale model from Moonshot AI with improved reasoning, coding, and agentic capabilities. Read <a href="/changelog/post/2026-04-20-kimi-k2-6-workers-ai/">changelog</a> to get started.</li>
<li>K2.6 uses the <code>chat_template_kwargs.thinking</code> parameter to control reasoning (instead of <code>chat_template_kwargs.enable_thinking</code>) and returns reasoning content in the <code>reasoning</code> field (instead of <code>reasoning_content</code>).</li>
</ul><h2 id="2026-04-04">2026-04-04</h2><strong>Google Gemma 4 26B A4B now available on Workers AI</strong><ul>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> now available on Workers AI. A Mixture-of-Experts model with 26B total parameters and 4B active, featuring a 256K context window, vision, built-in thinking mode, and function calling. Read <a href="/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/">changelog</a> to get started.</li>
</ul><h2 id="2026-03-19">2026-03-19</h2><strong>Moonshot AI Kimi K2.5 now available on Workers AI</strong><ul>
<li><a href="/workers-ai/models/kimi-k2.5/"><code>@cf/moonshotai/kimi-k2.5</code></a> now available on Workers AI. A frontier-scale open-source model with a 256k context window, multi-turn tool calling, vision inputs, and structured outputs for agentic workloads. Read <a href="/changelog/post/2026-03-19-kimi-k2-5-workers-ai/">changelog</a> to get started.</li>
<li>New <a href="/workers-ai/features/prompt-caching/">Prompt caching</a> documentation. Send the <code>x-session-affinity</code> header to route requests to the same model instance and maximize prefix cache hit rates across multi-turn conversations.</li>
<li>Redesigned <a href="/workers-ai/features/batch-api/">Asynchronous Batch API</a> with a pull-based system that processes queued requests as capacity becomes available, avoiding out-of-capacity errors for durable workflows.</li>
</ul><h2 id="2026-03-11">2026-03-11</h2><strong>NVIDIA Nemotron 3 Super now available on Workers AI</strong><ul>
<li><a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a> now available on Workers AI! A hybrid MoE model with 120B total parameters and 12B active, optimized for multi-agent and agentic AI workloads. Read <a href="/changelog/post/2026-03-11-nemotron-3-super-workers-ai/">changelog</a> to get started.</li>
</ul><h2 id="2026-03-06">2026-03-06</h2><strong>Deepgram Nova-3 now supports 10 languages with regional variants</strong><ul>
<li><a href="/workers-ai/models/nova-3/"><code>@cf/deepgram/nova-3</code></a> now supports 10 languages with regional variants for real-time transcription. Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like <code>en-GB</code>, <code>fr-CA</code>, and <code>pt-BR</code>.</li>
</ul><h2 id="2026-02-17">2026-02-17</h2><strong>Chat Completions API support for gpt-oss models and tool calling improvements</strong><ul>
<li><a href="/workers-ai/models/gpt-oss-120b/"><code>@cf/openai/gpt-oss-120b</code></a> and <a href="/workers-ai/models/gpt-oss-20b/"><code>@cf/openai/gpt-oss-20b</code></a> now support Chat Completions API format. Use <code>/v1/chat/completions</code> with a <code>messages</code> array, or use <code>/ai/run</code> which dynamically detects your input format and accepts Chat Completions (<code>messages</code>), legacy Completions (<code>prompt</code>), or Responses API (<code>input</code>).</li>
<li><strong>[Bug fix]</strong> Fixed a bug in the schema for multiple text generation models where the <code>content</code> field in message objects only accepted string values. The field now properly accepts both string content and array content (structured content parts for multi-modal inputs). This fix applies to all affected chat models including GPT-OSS models, Llama 3.x, Mistral, Qwen, and others.</li>
<li><strong>[Bug fix]</strong> Tool call round-trips now work correctly. The binding no longer rejects <code>tool_call_id</code> values that it generated itself, fixing issues with multi-turn tool calling conversations.</li>
<li><strong>[Bug fix]</strong> Assistant messages with <code>content: null</code> and <code>tool_calls</code> are now accepted in both the Workers AI binding and REST API (<code>/v1/chat/completions</code>), fixing tool call round-trip failures.</li>
<li><strong>[Bug fix]</strong> Streaming responses now correctly report <code>finish_reason</code> only on the usage chunk, matching OpenAI's streaming behavior and preventing duplicate finish events.</li>
<li><strong>[Bug fix]</strong> <code>/v1/chat/completions</code> now preserves original tool call IDs from models instead of regenerating them. Previously, the endpoint was generating new IDs which broke multi-turn tool calling because AI SDK clients could not match tool results to their original calls.</li>
<li><strong>[Bug fix]</strong> <code>/v1/chat/completions</code> now correctly reports <code>finish_reason: &quot;tool_calls&quot;</code> in the final usage chunk when tools are used. Previously, it was hardcoding <code>finish_reason: &quot;stop&quot;</code> which caused AI SDK clients to think the conversation was complete instead of executing tool calls.</li>
</ul><h2 id="2026-02-13">2026-02-13</h2><strong>GLM-4.7-Flash, @cloudflare/tanstack-ai, and workers-ai-provider v3.1.1</strong><ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> is now available on Workers AI! A fast and efficient multilingual text generation model optimized for multi-turn tool calling across 100+ languages. Read <a href="/changelog/2026-02-13-glm-4.7-flash-workers-ai/">changelog</a> to get started.</li>
<li>New <a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai"><code>@cloudflare/tanstack-ai</code></a> package for using Workers AI and AI Gateway with TanStack AI.</li>
<li><a href="https://www.npmjs.com/package/workers-ai-provider"><code>workers-ai-provider v3.1.1</code></a> adds transcription, text-to-speech, and reranking capabilities.</li>
</ul><h2 id="2026-01-28">2026-01-28</h2><strong>Black Forest Labs FLUX.2 [klein] 9B now available</strong><ul>
<li><a href="/workers-ai/models/flux-2-klein-9b/"><code>@cf/black-forest-labs/flux-2-klein-9b</code></a> now available on Workers AI! Read <a href="/changelog/2026-01-28-flux-2-klein-9b-workers-ai/">changelog</a> to get started</li>
</ul><h2 id="2026-01-15">2026-01-15</h2><strong>Black Forest Labs FLUX.2 [klein] 4b now available</strong><ul>
<li><a href="/workers-ai/models/flux-2-klein-4b/"><code>@cf/black-forest-labs/flux-2-klein-4b</code></a> now available on Workers AI! Read <a href="/changelog/2026-01-15-flux-2-klein-4b-workers-ai/">changelog</a> to get started</li>
</ul><h2 id="2025-12-03">2025-12-03</h2><strong>Deepgram Flux promotional period over on Dec 8, 2025 - now has pricing</strong><ul>
<li>Check out updated pricing on the <a href="/workers-ai/models/flux/"><code>@cf/deepgram/flux</code></a> model page or <a href="/workers-ai/platform/pricing/">pricing</a> page</li>
<li>Pricing will start Dec 8, 2025</li>
</ul><h2 id="2025-11-25">2025-11-25</h2><strong>Black Forest Labs FLUX.2 dev now available</strong><ul>
<li><a href="/workers-ai/models/flux-2-dev/"><code>@cf/black-forest-labs/flux-2-dev</code></a> now available on Workers AI! Read <a href="/changelog/2025-11-25-flux-2-dev-workers-ai/">changelog</a> to get started</li>
</ul><h2 id="2025-11-13">2025-11-13</h2><strong>Qwen3 LLM and Embeddings available on Workers AI</strong><ul>
<li><a href="/workers-ai/models/qwen3-30b-a3b-fp8/"><code>@cf/qwen/qwen3-30b-a3b-fp8</code></a> and <a href="/workers-ai/models/qwen3-embedding-0.6b"><code>@cf/qwen/qwen3-embedding-0.6b</code></a> now available on Workers AI</li>
</ul><h2 id="2025-10-21">2025-10-21</h2><strong>New voice and LLM models on Workers AI</strong><ul>
<li>Deepgram Aura 2 brings new text-to-speech capabilities to Workers AI. Check out <a href="/workers-ai/models/aura-2-en/"><code>@cf/deepgram/aura-2-en</code></a> and <a href="/workers-ai/models/aura-2-es/"><code>@cf/deepgram/aura-2-es</code></a> on how to use the new models.</li>
<li>IBM Granite model is also up! This new LLM model is small but mighty, take a look at the docs for more <a href="/workers-ai/models/granite-4.0-h-micro/"><code>@cf/ibm-granite/granite-4.0-h-micro</code></a></li>
</ul><h2 id="2025-10-02">2025-10-02</h2><strong>Deepgram Flux now available on Workers AI</strong><ul>
<li>We're excited to be a launch partner with Deepgram and offer their new Speech Recognition model built specifically for enabling voice agents. Check out <a href="https://deepgram.com/flux">Deepgram's blog</a> for more details on the release.</li>
<li>Access the model through <a href="/workers-ai/models/flux/"><code>@cf/deepgram/flux</code></a> and check out the <a href="/changelog/2025-10-02-deepgram-flux/">changelog</a> for in-depth examples.</li>
</ul><h2 id="2025-09-24">2025-09-24</h2><strong>New local models available on Workers AI</strong><ul>
<li>We've added support for some regional models on Workers AI in support of uplifting local AI labs and AI sovereignty. Check out the <a href="https://blog.cloudflare.com/sovereign-ai-and-choice">full blog post here</a>.</li>
<li><a href="/workers-ai/models/plamo-embedding-1b"><code>@cf/pfnet/plamo-embedding-1b</code></a> creates embeddings from Japanese text.</li>
<li><a href="/workers-ai/models/gemma-sea-lion-v4-27b-it"><code>@cf/aisingapore/gemma-sea-lion-v4-27b-it</code></a> is a fine-tuned model that supports multiple South East Asian languages, including Burmese, English, Indonesian, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai, and Vietnamese.</li>
<li><a href="/workers-ai/models/indictrans2-en-indic-1B"><code>@cf/ai4bharat/indictrans2-en-indic-1B</code></a> is a translation model that can translate between 22 indic languages, including Bengali, Gujarati, Hindi, Tamil, Sanskrit and even traditionally low-resourced languages like Kashmiri, Manipuri and Sindhi.</li>
</ul><h2 id="2025-09-23">2025-09-23</h2><strong>New document formats supported by Markdown conversion utility</strong><ul>
<li>Our <a href="/workers-ai/features/markdown-conversion/">Markdown conversion utility</a> now supports converting <code>.docx</code> and <code>.odt</code> files.</li>
</ul><h2 id="2025-09-18">2025-09-18</h2><strong>Model Catalog updates (types, EmbeddingGemma, model deprecation)</strong><ul>
<li>Workers AI types got updated in the upcoming wrangler release, please use <code>npm i -D wrangler@latest</code> to update your packages.</li>
<li>EmbeddingGemma model accuracy has been improved, we recommend re-indexing data to take advantage of the improved accuracy</li>
<li>Some older Workers AI models are being deprecated on October 1st, 2025. We reccommend you use the newer models such as <a href="/workers-ai/models/llama-4-scout-17b-16e-instruct/">Llama 4</a> and <a href="/workers-ai/models/gpt-oss-120b/">gpt-oss</a>. The following models are being deprecated:
<ul>
<li>@hf/thebloke/zephyr-7b-beta-awq</li>
<li>@hf/thebloke/mistral-7b-instruct-v0.1-awq</li>
<li>@hf/thebloke/llama-2-13b-chat-awq</li>
<li>@hf/thebloke/openhermes-2.5-mistral-7b-awq</li>
<li>@hf/thebloke/neural-chat-7b-v3-1-awq</li>
<li>@hf/thebloke/llamaguard-7b-awq</li>
<li>@hf/thebloke/deepseek-coder-6.7b-base-awq</li>
<li>@hf/thebloke/deepseek-coder-6.7b-instruct-awq</li>
<li>@cf/deepseek-ai/deepseek-math-7b-instruct</li>
<li>@cf/openchat/openchat-3.5-0106</li>
<li>@cf/tiiuae/falcon-7b-instruct</li>
<li>@cf/thebloke/discolm-german-7b-v1-awq</li>
<li>@cf/qwen/qwen1.5-0.5b-chat</li>
<li>@cf/qwen/qwen1.5-7b-chat-awq</li>
<li>@cf/qwen/qwen1.5-14b-chat-awq</li>
<li>@cf/tinyllama/tinyllama-1.1b-chat-v1.0</li>
<li>@cf/qwen/qwen1.5-1.8b-chat</li>
<li>@hf/nexusflow/starling-lm-7b-beta</li>
<li>@cf/fblgit/una-cybertron-7b-v2-bf16</li>
</ul>
</li>
</ul><h2 id="2025-09-05">2025-09-05</h2><strong>Introducing EmbeddingGemma from Google</strong><ul>
<li>We’re excited to be a launch partner alongside Google to bring their newest embedding model to Workers AI. We're excited to introduce EmbeddingGemma delivers best-in-class performance for its size, enabling RAG and semantic search use cases. Take a look at <a href="/workers-ai/models/embeddinggemma-300m"><code>@cf/google/embeddinggemma-300m</code></a> for more details. Now available to use for embedding in AI Search too.</li>
</ul><h2 id="2025-08-27">2025-08-27</h2><strong>Introducing Partner models to the Workers AI catalog</strong><ul>
<li>Read the <a href="https://blog.cloudflare.com/workers-ai-partner-models">blog</a> for more details</li>
<li><a href="/workers-ai/models/aura-1"><code>@cf/deepgram/aura-1</code></a> is a text-to-speech model that allows you to input text and have it come to life in a customizable voice</li>
<li><a href="/workers-ai/models/nova-3"><code>@cf/deepgram/nova-3</code></a> is speech-to-text model that transcribes multilingual audio at a blazingly fast speed</li>
<li><a href="/workers-ai/models/smart-turn-v2"><code>@cf/pipecat-ai/smart-turn-v2</code></a> helps you detect when someone is done speaking</li>
<li><a href="/workers-ai/models/lucid-origin"><code>@cf/leonardo/lucid-origin</code></a> is a text-to-image model that generates images with sharp graphic design, stunning full-HD renders, or highly specific creative direction</li>
<li><a href="/workers-ai/models/phoenix-1.0"><code>@cf/leonardo/phoenix-1.0</code></a> is a text-to-image model with exceptional prompt adherence and coherent text</li>
<li>WebSocket support added for audio models like <code>@cf/deepgram/aura-1</code>, <code>@cf/deepgram/nova-3</code>, <code>@cf/pipecat-ai/smart-turn-v2</code></li>
</ul><h2 id="2025-08-05">2025-08-05</h2><strong>Adding gpt-oss models to our catalog</strong><ul>
<li>Check out the <a href="https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai">blog</a> for more details about the new models</li>
<li>Take a look at the <a href="/workers-ai/models/gpt-oss-120b"><code>gpt-oss-120b</code></a> and <a href="/workers-ai/models/gpt-oss-20b"><code>gpt-oss-20b</code></a> model pages for more information about schemas, pricing, and context windows</li>
</ul><h2 id="2025-04-09">2025-04-09</h2><strong>Pricing correction for @cf/myshell-ai/melotts</strong><ul>
<li>We've updated our documentation to reflect the correct pricing for melotts: $0.0002 per audio minute, which is actually cheaper than initially stated. The documented pricing was incorrect, where it said users would be charged based on input tokens.</li>
</ul><h2 id="2025-03-17">2025-03-17</h2><strong>Minor updates to the model schema for llama-3.2-1b-instruct, whisper-large-v3-turbo, llama-guard</strong><ul>
<li><a href="/workers-ai/models/llama-3.2-1b-instruct/">llama-3.2-1b-instruct</a> - updated context window to the accurate 60,000</li>
<li><a href="/workers-ai/models/whisper-large-v3-turbo/">whisper-large-v3-turbo</a> - new hyperparameters available</li>
<li><a href="/workers-ai/models/llama-guard-3-8b/">llama-guard-3-8b</a> - the messages array must alternate between <code>user</code> and <code>assistant</code> to function correctly</li>
</ul><h2 id="2025-02-21">2025-02-21</h2><strong>Workers AI bug fixes</strong><ul>
<li>We fixed a bug where <code>max_tokens</code> defaults were not properly being respected - <code>max_tokens</code> now correctly defaults to <code>256</code> as displayed on the model pages. Users relying on the previous behaviour may observe this as a breaking change. If you want to generate more tokens, please set the <code>max_tokens</code> parameter to what you need.</li>
<li>We updated model pages to show context windows - which is defined as the tokens used in the prompt + tokens used in the response. If your prompt + response tokens exceed the context window, the request will error. Please set <code>max_tokens</code> accordingly depending on your prompt length and the context window length to ensure a successful response.</li>
</ul><h2 id="2024-09-26">2024-09-26</h2><strong>Workers AI Birthday Week 2024 announcements</strong><ul>
<li>Meta Llama 3.2 1B, 3B, and 11B vision is now available on Workers AI</li>
<li><code>@cf/black-forest-labs/flux-1-schnell</code> is now available on Workers AI</li>
<li>Workers AI is fast! Powered by new GPUs and optimizations, you can expect faster inference on Llama 3.1, Llama 3.2, and FLUX models.</li>
<li>No more neurons. Workers AI is moving towards <a href="/workers-ai/platform/pricing">unit-based pricing</a></li>
<li>Model pages get a refresh with better documentation on parameters, pricing, and model capabilities</li>
<li>Closed beta for our Run Any* Model feature, <a href="https://forms.gle/h7FcaTF4Zo5dzNb68">sign up here</a></li>
<li>Check out the <a href="https://blog.cloudflare.com/workers-ai">product announcements blog post</a> for more information</li>
<li>And the <a href="https://blog.cloudflare.com/workers-ai/making-workers-ai-faster">technical blog post</a> if you want to learn about how we made Workers AI fast</li>
</ul><h2 id="2024-07-23">2024-07-23</h2><strong>Meta Llama 3.1 now available on Workers AI</strong><p>Workers AI now suppoorts <a href="/workers-ai/models/llama-3.1-8b-instruct/">Meta Llama 3.1</a>.</p><h2 id="2024-06-27">2024-06-27</h2><strong>Introducing embedded function calling</strong><ul>
<li>A new way to do function calling with <a href="/workers-ai/function-calling/embedded">Embedded function calling</a></li>
<li>Published new <a href="https://www.npmjs.com/package/@cloudflare/ai-utils"><code>@cloudflare/ai-utils</code></a> npm package</li>
<li>Open-sourced <a href="https://github.com/cloudflare/ai-utils"><code>ai-utils on Github</code></a></li>
</ul><h2 id="2024-06-19">2024-06-19</h2><strong>Added support for traditional function calling</strong><ul>
<li><a href="/workers-ai/function-calling/">Function calling</a> is now supported on enabled models</li>
<li>Properties added on <a href="/workers-ai/models/">models</a> page to show which models support function calling</li>
</ul><h2 id="2024-06-18">2024-06-18</h2><strong>Native support for AI Gateways</strong><p>Workers AI now natively supports <a href="/ai-gateway/usage/providers/workersai/#worker">AI Gateway</a>.</p><h2 id="2024-06-11">2024-06-11</h2><strong>Deprecation announcement for `@cf/meta/llama-2-7b-chat-int8`</strong><p>We will be deprecating <code>@cf/meta/llama-2-7b-chat-int8</code> on 2024-06-30.</p>
<p>Replace the model ID in your code with a new model of your choice:</p>
<ul>
<li><a href="/workers-ai/models/llama-3-8b-instruct/"><code>@cf/meta/llama-3-8b-instruct</code></a> is the newest model in the Llama family (and is currently free for a limited time on Workers AI).</li>
<li><a href="/workers-ai/models/llama-3-8b-instruct-awq/"><code>@cf/meta/llama-3-8b-instruct-awq</code></a> is the new Llama 3 in a similar precision to your currently selected model. This model is also currently free for a limited time.</li>
</ul>
<p>If you do not switch to a different model by June 30th, we will automatically start returning inference from <code>@cf/meta/llama-3-8b-instruct-awq</code>.</p><h2 id="2024-05-29">2024-05-29</h2><strong>Add new public LoRAs and note on LoRA routing</strong><ul>
<li>Added documentation on <a href="/workers-ai/fine-tunes/public-loras/">new public LoRAs</a>.</li>
<li>Noted that you can now run LoRA inference with the base model rather than explicitly calling the <code>-lora</code> version</li>
</ul><h2 id="2024-05-17">2024-05-17</h2><strong>Add OpenAI compatible API endpoints</strong><p>Added OpenAI compatible API endpoints for <code>/v1/chat/completions</code> and <code>/v1/embeddings</code>. For more details, refer to <a href="/workers-ai/configuration/open-ai-compatibility/">Configurations</a>.</p><h2 id="2024-04-11">2024-04-11</h2><strong>Add AI native binding</strong><ul>
<li>Added new AI native binding, you can now run models with <code>const resp = await env.AI.run(modelName, inputs)</code></li>
<li>Deprecated <code>@cloudflare/ai</code> npm package. While existing solutions using the @cloudflare/ai package will continue to work, no new Workers AI features will be supported.
Moving to native AI bindings is highly recommended</li>
</ul>
