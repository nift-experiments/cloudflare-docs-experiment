---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers-ai/2/
  description: '2025-10-02'
  full_title: workers-ai changelog - page 2 | Cloudflare Docs
  head_html: <title>workers-ai changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-10-02"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers-ai/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers-ai changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-10-02"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers-ai/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers-ai/2/#page","headline":"workers-ai changelog - page 2 | Cloudflare Docs","description":"2025-10-02","url":"https://developers.cloudflare.com/changelog/product/workers-ai/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers-ai/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-deepgram-flux-model-available-on-workers-ai"><a href="/changelog/post/2025-10-02-deepgram-flux/">New Deepgram Flux model available on Workers AI</a></h2>
<p><em>2025-10-02</em></p>
<p>Deepgram's newest Flux model <a href="/workers-ai/models/flux/"><code>@cf/deepgram/flux</code></a> is now available on Workers AI, hosted directly on Cloudflare's infrastructure. We're excited to be a launch partner with Deepgram and offer their new Speech Recognition model built specifically for enabling voice agents. Check out <a href="https://deepgram.com/flux">Deepgram's blog</a> for more details on the release.</p>
<p>The Flux model can be used in conjunction with Deepgram's speech-to-text model <a href="/workers-ai/models/nova-3/"><code>@cf/deepgram/nova-3</code></a> and text-to-speech model <a href="/workers-ai/models/aura-1/"><code>@cf/deepgram/aura-1</code></a> to build end-to-end voice agents. Having Deepgram on Workers AI takes advantage of our edge GPU infrastructure, for ultra low latency voice AI applications.</p>
<h4 id="2025-10-02-deepgram-flux-promotional-pricing">Promotional Pricing</h4>
For the month of October 2025, Deepgram's Flux model will be free to use on Workers AI. Official pricing will be announced soon and charged after the promotional pricing period ends on October 31, 2025. Check out the [model page](/workers-ai/models/flux/) for pricing details in the future.
<h4 id="2025-10-02-deepgram-flux-example-usage">Example Usage</h4>
<p>The new Flux model is WebSocket only as it requires live bi-directional streaming in order to recognize speech activity.</p>
<ol>
<li>Create a worker that establishes a websocket connection with <code>@cf/deepgram/flux</code></li>
</ol>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;    const resp = await env.AI.run(&quot;@cf/deepgram/flux&quot;, {&#10;      encoding: &quot;linear16&quot;,&#10;      sample_rate: &quot;16000&quot;&#10;    }, {&#10;      websocket: true&#10;    });&#10;    return resp;&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<ol start="2">
<li>Deploy your worker</li>
</ol>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<ol start="3">
<li>Write a client script to connect to your worker and start sending random audio bytes to it</li>
</ol>
<pre tabindex="0"><code class="language-js">const ws = new WebSocket(&#x27;wss://&lt;your-worker-url.com&gt;&#x27;);&#10;&#10;ws.onopen = () =&gt; {&#10;  console.log(&#x27;Connected to WebSocket&#x27;);&#10;&#10;  // Generate and send random audio bytes&#10;  // You can replace this part with a function&#10;  // that reads from your mic or other audio source&#10;  const audioData = generateRandomAudio();&#10;  ws.send(audioData);&#10;  console.log(&#x27;Audio data sent&#x27;);&#10;};&#10;&#10;ws.onmessage = (event) =&gt; {&#10;  // Transcription will be received here&#10;  // Add your custom logic to parse the data&#10;  console.log(&#x27;Received:&#x27;, event.data);&#10;};&#10;&#10;ws.onerror = (error) =&gt; {&#10;  console.error(&#x27;WebSocket error:&#x27;, error);&#10;};&#10;&#10;ws.onclose = () =&gt; {&#10;  console.log(&#x27;WebSocket closed&#x27;);&#10;};&#10;&#10;// Generate random audio data (1 second of noise at 44.1kHz, mono)&#10;function generateRandomAudio() {&#10;  const sampleRate = 44100;&#10;  const duration = 1;&#10;  const numSamples = sampleRate * duration;&#10;  const buffer = new ArrayBuffer(numSamples * 2);&#10;  const view = new Int16Array(buffer);&#10;&#10;  for (let i = 0; i &lt; numSamples; i++) {&#10;    view[i] = Math.floor(Math.random() * 65536 - 32768);&#10;  }&#10;&#10;  return buffer;&#10;}&#10;</code></pre>


<h2 id="introducing-embeddinggemma-from-google-on-workers-ai"><a href="/changelog/post/2025-09-05-embeddinggemma/">Introducing EmbeddingGemma from Google on Workers AI</a></h2>
<p><em>2025-09-05</em></p>
<p>We're excited to be a launch partner alongside <a href="https://developers.googleblog.com/en/introducing-embeddinggemma/">Google</a> to bring their newest embedding model, <strong>EmbeddingGemma</strong>, to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.</p>
<p><a href="/workers-ai/models/embeddinggemma-300m/"><code>@cf/google/embeddinggemma-300m</code></a> is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.</p>
<p><strong>Using EmbeddingGemma in AI Search:</strong>
Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.</p>
<p>To use EmbeddingGemma for your AI Search projects:</p>
<ol>
<li>Go to <strong>Create</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/ai/ai-search">AI Search dashboard</a></li>
<li>Follow the setup flow for your new RAG instance</li>
<li>In the <strong>Generate Index</strong> step, open up <strong>More embedding models</strong> and select <code>@cf/google/embeddinggemma-300m</code> as your embedding model</li>
<li>Complete the setup to create an AI Search</li>
</ol>
<p>Try it out and let us know what you think!</p>


<h2 id="deepgram-and-leonardo-partner-models-now-available-on-workers-ai"><a href="/changelog/post/2025-08-27-partner-models/">Deepgram and Leonardo partner models now available on Workers AI</a></h2>
<p><em>2025-08-27</em></p>
<p>New state-of-the-art models have landed on Workers AI! This time, we're introducing new <strong>partner models</strong> trained by our friends at <a href="https://deepgram.com">Deepgram</a> and <a href="https://leonardo.ai">Leonardo</a>, hosted on Workers AI infrastructure.</p>
<p>As well, we're introuding a new turn detection model that enables you to detect when someone is done speaking — useful for building voice agents!</p>
<p>Read the <a href="https://blog.cloudflare.com/workers-ai-partner-models">blog</a> for more details and check out some of the new models on our platform:</p>
<ul>
<li><a href="/workers-ai/models/aura-1"><code>@cf/deepgram/aura-1</code></a> is a text-to-speech model that allows you to input text and have it come to life in a customizable voice</li>
<li><a href="/workers-ai/models/nova-3"><code>@cf/deepgram/nova-3</code></a> is speech-to-text model that transcribes multilingual audio at a blazingly fast speed</li>
<li><a href="/workers-ai/models/smart-turn-v2"><code>@cf/pipecat-ai/smart-turn-v2</code></a> helps you detect when someone is done speaking</li>
<li><a href="/workers-ai/models/lucid-origin"><code>@cf/leonardo/lucid-origin</code></a> is a text-to-image model that generates images with sharp graphic design, stunning full-HD renders, or highly specific creative direction</li>
<li><a href="/workers-ai/models/phoenix-1.0"><code>@cf/leonardo/phoenix-1.0</code></a> is a text-to-image model with exceptional prompt adherence and coherent text</li>
</ul>
<p>You can filter out new partner models with the <code>Partner</code> capability on our <a href="/workers-ai/models">Models</a> page.</p>
<p>As well, we're introducing WebSocket support for some of our audio models, which you can filter though the <code>Realtime</code> capability on our <a href="/workers-ai/models">Models</a> page. WebSockets allows you to create a bi-directional connection to our inference server with low latency — perfect for those that are building voice agents.</p>
<p>An example python snippet on how to use WebSockets with our new Aura model:</p>
<pre tabindex="0"><code>import json&#10;import os&#10;import asyncio&#10;import websockets&#10;&#10;uri = f&quot;wss://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/deepgram/aura-1&quot;&#10;&#10;input = [&#10;    &quot;Line one, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line two, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line three, out of three lines that will be provided to the aura model. This is a last line.&quot;,&#10;]&#10;&#10;&#10;async def text_to_speech():&#10;    async with websockets.connect(uri, additional_headers={&quot;Authorization&quot;: os.getenv(&quot;CF_TOKEN&quot;)}) as websocket:&#10;        print(&quot;connection established&quot;)&#10;        for line in input:&#10;            print(f&quot;sending `{line}`&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Speak&quot;, &quot;text&quot;: line}))&#10;&#10;            print(&quot;line was sent, flushing&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Flush&quot;}))&#10;            print(&quot;flushed, recving&quot;)&#10;            resp = await websocket.recv()&#10;            print(f&quot;response received {resp}&quot;)&#10;&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    asyncio.run(text_to_speech())&#10;</code></pre>


<h2 id="openai-open-models-now-available-on-workers-ai"><a href="/changelog/post/2025-08-05-openai-open-models/">OpenAI open models now available on Workers AI</a></h2>
<p><em>2025-08-05</em></p>
<p>We're thrilled to be a Day 0 partner with <a href="http://openai.com/index/introducing-gpt-oss">OpenAI</a> to bring their <a href="https://openai.com/index/gpt-oss-model-card/">latest open models</a> to Workers AI, including support for Responses API, Code Interpreter, and Web Search (coming soon).</p>
<p>Get started with the new models at <code>@cf/openai/gpt-oss-120b</code> and <code>@cf/openai/gpt-oss-20b</code>.
Check out the <a href="https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai">blog</a> for more details about the new models, and the <a href="/workers-ai/models/gpt-oss-120b"><code>gpt-oss-120b</code></a> and <a href="/workers-ai/models/gpt-oss-20b"><code>gpt-oss-20b</code></a> model pages for more information about pricing and context windows.</p>
<h4 id="2025-08-05-openai-open-models-responses-api">Responses API</h4>
If you call the model through:
- Workers Binding, it will accept/return Responses API – `env.AI.run(“@cf/openai/gpt-oss-120b”)`
- REST API on `/run` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/run/@cf/openai/gpt-oss-120b`
- REST API on new `/responses` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses`
- REST API for OpenAI Compatible endpoint, it will return Chat Completions (coming soon) – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/chat/completions`
<pre tabindex="0"><code>curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/ai/v1/responses \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_KEY&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;@cf/openai/gpt-oss-120b&quot;,&#10;    &quot;reasoning&quot;: {&quot;effort&quot;: &quot;medium&quot;},&#10;    &quot;input&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What are the benefits of open-source models?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;&#10;</code></pre>
<h4 id="2025-08-05-openai-open-models-code-interpreter">Code Interpreter</h4>
The model is natively trained to support stateful code execution, and we've implemented support for this feature using our [Sandbox SDK](https://github.com/cloudflare/sandbox-sdk) and [Containers](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Cloudflare's Developer Platform is uniquely positioned to support this feature, so we're very excited to bring our products together to support this new use case.
<h4 id="2025-08-05-openai-open-models-web-search-coming-soon">Web Search (coming soon)</h4>
We are working to implement Web Search for the model, where users can bring their own Exa API Key so the model can browse the Internet.


<h2 id="workers-ai-for-developer-week-faster-inference-new-models-async-batch-api-expanded-lora-support"><a href="/changelog/post/2025-04-11-new-models-faster-inference/">Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support</a></h2>
<p><em>2025-04-11</em></p>
<p>Happy Developer Week 2025! Workers AI is excited to announce a couple of new features and improvements available today. Check out our <a href="https://blog.cloudflare.com/workers-ai-improvements">blog</a> for all the announcement details.</p>
<h4 id="2025-04-11-new-models-faster-inference-faster-inference-new-models">Faster inference + New models</h4>
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
<h4 id="2025-04-11-new-models-faster-inference-batch-inference">Batch Inference</h4>
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
<h4 id="2025-04-11-new-models-faster-inference-expanded-lora-support">Expanded LoRA support</h4>
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


<h2 id="markdown-conversion-in-workers-ai"><a href="/changelog/post/2025-03-20-markdown-conversion/">Markdown conversion in Workers AI</a></h2>
<p><em>2025-03-20</em></p>
<p>Document conversion plays an important role when designing and developing AI applications and agents. Workers AI now provides the <code>toMarkdown</code> utility method that developers can use to for quick, easy, and convenient conversion and summary of documents in multiple formats to Markdown language.</p>
<p>You can call this new tool using a binding by calling <code>env.AI.toMarkdown()</code> or the using the <a href="/api/resources/ai/">REST API</a> endpoint.</p>
<p>In this example, we fetch a PDF document and an image from R2 and feed them both to <code>env.AI.toMarkdown()</code>. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.</p>
<pre tabindex="0"><code class="language-typescript">import { Env } from &quot;./env&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf&#10;		const pdf = await env.R2.get(&quot;somatosensory.pdf&quot;);&#10;&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg&#10;		const cat = await env.R2.get(&quot;cat.jpeg&quot;);&#10;&#10;		return Response.json(&#10;			await env.AI.toMarkdown([&#10;				{&#10;					name: &quot;somatosensory.pdf&quot;,&#10;					blob: new Blob([await pdf.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;				{&#10;					name: &quot;cat.jpeg&quot;,&#10;					blob: new Blob([await cat.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;			]),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>This is the result:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;name&quot;: &quot;somatosensory.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;# somatosensory.pdf\n## Metadata\n- PDFFormatVersion=1.4\n- IsLinearized=false\n- IsAcroFormPresent=false\n- IsXFAPresent=false\n- IsCollectionPresent=false\n- IsSignaturesPresent=false\n- Producer=Prince 20150210 (www.princexml.com)\n- Title=Anatomy of the Somatosensory System\n\n## Contents\n### Page 1\nThis is a sample document to showcase...&quot;&#10;	},&#10;	{&#10;		&quot;name&quot;: &quot;cat.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;The image is a close-up photograph of Grumpy Cat, a cat with a distinctive grumpy expression and piercing blue eyes. The cat has a brown face with a white stripe down its nose, and its ears are pointed upright. Its fur is light brown and darker around the face, with a pink nose and mouth. The cat&#x27;s eyes are blue and slanted downward, giving it a perpetually grumpy appearance. The background is blurred, but it appears to be a dark brown color. Overall, the image is a humorous and iconic representation of the popular internet meme character, Grumpy Cat. The cat&#x27;s facial expression and posture convey a sense of displeasure or annoyance, making it a relatable and entertaining image for many people.&quot;&#10;	}&#10;]&#10;</code></pre>
<p>See <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> for more information on supported formats, REST API and pricing.</p>


<h2 id="new-models-in-workers-ai"><a href="/changelog/post/2025-03-17-new-workers-ai-models/">New models in Workers AI</a></h2>
<p><em>2025-03-17</em></p>
<p>Workers AI is excited to add 4 new models to the catalog, including 2 brand new classes of models with a text-to-speech and reranker model. Introducing:</p>
<ul>
<li><a href="/workers-ai/models/bge-m3/">@cf/baai/bge-m3</a> - a multi-lingual embeddings model that supports over 100 languages. It can also simultaneously perform dense retrieval, multi-vector retrieval, and sparse retrieval, with the ability to process inputs of different granularities.</li>
<li><a href="/workers-ai/models/bge-reranker-base/">@cf/baai/bge-reranker-base</a> - our first reranker model! Rerankers are a type of text classification model that takes a query and context, and outputs a similarity score between the two. When used in RAG systems, you can use a reranker after the initial vector search to find the most relevant documents to return to a user by reranking the outputs.</li>
<li><a href="/workers-ai/models/whisper-large-v3-turbo/">@cf/openai/whisper-large-v3-turbo</a> - a faster, more accurate speech-to-text model. This model was added earlier but is graduating out of beta with pricing included today.</li>
<li><a href="/workers-ai/models/melotts/">@cf/myshell-ai/melotts</a> - our first text-to-speech model that allows users to generate an MP3 with voice audio from inputted text.</li>
</ul>
<p>Pricing is available for each of these models on the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<p>This docs update includes a few minor bug fixes to the model schema for llama-guard, llama-3.2-1b, which you can review on the <a href="/workers-ai/changelog/">product changelog</a>.</p>
<p>Try it out and let us know what you think! Stay tuned for more models in the coming days.</p>


<h2 id="workers-ai-now-supports-structured-json-outputs"><a href="/changelog/post/2025-02-25-json-mode/">Workers AI now supports structured JSON outputs.</a></h2>
<p><em>2025-02-25</em></p>
<p>Workers AI now supports structured JSON outputs with <a href="/workers-ai/features/json-mode/">JSON mode</a>, which allows you to request a structured output response when interacting with AI models.</p>
<p>This makes it much easier to retrieve structured data from your AI models, and avoids the (error prone!) need to parse large unstructured text responses to extract your data.</p>
<p>JSON mode in Workers AI is compatible with the OpenAI SDK's <a href="https://platform.openai.com/docs/guides/structured-outputs">structured outputs</a> <code>response_format</code> API, which can be used directly in a Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17816.md")</div>
<p>To learn more about JSON mode and structured outputs, visit the <a href="/workers-ai/features/json-mode/">Workers AI documentation</a>.</p>


<h2 id="workers-ai-larger-context-windows"><a href="/changelog/post/2025-02-24-context-windows/">Workers AI larger context windows</a></h2>
<p><em>2025-02-24</em></p>
<p>We've updated the Workers AI text generation models to include context windows and limits definitions and changed our APIs to estimate and validate the number of tokens in the input prompt, not the number of characters.</p>
<p>This update allows developers to use larger context windows when interacting with Workers AI models, which can lead to better and more accurate results.</p>
<p>Our <a href="/workers-ai/models/">catalog page</a> provides more information about each model's supported context window.</p>


<h2 id="workers-ai-updated-pricing"><a href="/changelog/post/2025-02-20-updated-pricing-docs/">Workers AI updated pricing</a></h2>
<p><em>2025-02-20</em></p>
<p>We've updated the Workers AI <a href="/workers-ai/platform/pricing/">pricing</a> to include the latest models and how model usage maps to Neurons.</p>
<ul>
<li>Each model's core input format(s) (tokens, audio seconds, images, etc) now include mappings to Neurons, making it easier to understand how your included Neuron volume is consumed and how you are charged at scale</li>
<li>Per-model pricing, instead of the previous bucket approach, allows us to be more flexible on how models are charged based on their size, performance and capabilities. As we optimize each model, we can then pass on savings for that model.</li>
<li>You will still only pay for what you consume: Workers AI inference is serverless, and not billed by the hour.</li>
</ul>
<p>Going forward, models will be launched with their associated Neuron costs, and we'll be updating the Workers AI dashboard and API to reflect consumption in both raw units and Neurons. Visit the <a href="/workers-ai/platform/pricing/">Workers AI pricing</a> page to learn more about Workers AI pricing.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers-ai/">Previous</a><span>Page 2 of 2</span></nav>
