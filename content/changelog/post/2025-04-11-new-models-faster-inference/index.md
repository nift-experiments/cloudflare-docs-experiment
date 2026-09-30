<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 11, 2025</time><h2 id="post-title">Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Happy Developer Week 2025! Workers AI is excited to announce a couple of new features and improvements available today. Check out our <a href="https://blog.cloudflare.com/workers-ai-improvements">blog</a> for all the announcement details.</p>
<h4 id="faster-inference-new-models">Faster inference + New models</h4>
<p>We’re rolling out some in-place improvements to our models that can help speed up inference by 2-4x! Users of the models below will enjoy an automatic speed boost starting today:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a> gets a speed boost of 2-4x, leveraging techniques like speculative decoding, prefix caching, and an updated inference backend.</li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a>, <a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a>, <a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a> get an updated back end, which should improve inference times by 2x.
<ul>
<li>With the <code>bge</code> models, we’re also announcing a new parameter called <code>pooling</code> which can take <code>cls</code> or <code>mean</code> as options. We highly recommend using <code>pooling: cls</code> which will help generate more accurate embeddings. However, embeddings generated with cls pooling are not backwards compatible with mean pooling. For this to not be a breaking change, the default remains as mean pooling. Please specify <code>pooling: cls</code> to enjoy more accurate embeddings going forward.</li>
</ul>
</li>
</ul>
<p>We’re also excited to launch a few new models in our catalog to help round out your experience with Workers AI. We’ll be deprecating some older models in the future, so stay tuned for a deprecation announcement. Today’s new models include:</p>
<ul>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a>: a 24B parameter model achieving state-of-the-art capabilities comparable to larger models, with support for vision and tool calling.</li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a>: well-suited for a variety of text generation and image understanding tasks, including question answering, summarization and reasoning, with a 128K context window, and multilingual support in over 140 languages.</li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a>: a medium-sized reasoning model, which is capable of achieving competitive performance against state-of-the-art reasoning models, e.g., DeepSeek-R1, o1-mini.</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a>: the current state-of-the-art open-source code LLM, with its coding abilities matching those of GPT-4o.</li>
</ul>
<h4 id="batch-inference">Batch Inference</h4>
<p>Introducing a new batch inference feature that allows you to send us an array of requests, which we will fulfill as fast as possible and send them back as an array. This is really helpful for large workloads such as summarization, embeddings, etc. where you don’t have a human-in-the-loop. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if we don’t have enough capacity at a given time.</p>
<p>Check out the <a href="/workers-ai/features/batch-api/">tutorial</a> to get started! Models that support batch inference today include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-m3/"><code>@cf/baai/bge-m3</code></a></li>
<li><a href="/workers-ai/models/m2m100-1.2b/"><code>@cf/meta/m2m100-1.2b</code></a></li>
</ul>
<h4 id="expanded-lora-support">Expanded LoRA support</h4>
<p>We’ve upgraded our LoRA experience to include 8 newer models, and can support ranks of up to 32 with a 300MB safetensors file limit (previously limited to rank of 8 and 100MB safetensors) Check out our <a href="/workers-ai/features/fine-tunes/loras/">LoRAs page</a> to get started. Models that support LoRAs now include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.2-11b-vision-instruct/"><code>@cf/meta/llama-3.2-11b-vision-instruct</code></a></li>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/llama-guard-3-8b/"><code>@cf/meta/llama-guard-3-8b</code></a></li>
<li><a href="/workers-ai/models/llama-3.1-8b-instruct-fast/"><code>@cf/meta/llama-3.1-8b-instruct-fast</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/deepseek-r1-distill-qwen-32b/"><code>@cf/deepseek-ai/deepseek-r1-distill-qwen-32b</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a></li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a></li>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a></li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a></li>
</ul>
</div></article></div>
