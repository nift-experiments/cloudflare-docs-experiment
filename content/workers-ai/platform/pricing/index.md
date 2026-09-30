---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/platform/pricing/
  description: Workers AI pricing is based on Neurons, with a free daily allocation and per-model rates.
  full_title: Pricing · Cloudflare Workers AI docs
  head_html: <title>Pricing · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers AI pricing is based on Neurons, with a free daily allocation and per-model rates."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/platform/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers AI pricing is based on Neurons, with a free daily allocation and per-model rates."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/platform/pricing/#page","headline":"Pricing \u00b7 Cloudflare Workers AI docs","description":"Workers AI pricing is based on Neurons, with a free daily allocation and per-model rates.","url":"https://developers.cloudflare.com/workers-ai/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/platform/pricing/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15805.md")
</aside>
<p>Workers AI is included in both the <a href="/workers/platform/pricing/">Free and Paid Workers plans</a> and is priced at <strong>$0.011 per 1,000 Neurons</strong>.</p>
<p>Our free allocation allows anyone to use a total of <strong>10,000 Neurons per day at no charge</strong>. To use more than 10,000 Neurons per day, you need to sign up for the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>. On Workers Paid, you will be charged at $0.011 / 1,000 Neurons for any usage above the free allocation of 10,000 Neurons per day.</p>
<p>You can monitor your Neuron usage in the <a href="https://dash.cloudflare.com/?to=/:account/ai/workers-ai">Cloudflare Workers AI dashboard</a>.</p>
<p>All limits reset daily at 00:00 UTC. If you exceed any one of the above limits, further operations will fail with an error.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free <br/> allocation</th>
<th>Pricing</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers Free</td>
<td>10,000 Neurons per day</td>
<td>N/A - Upgrade to Workers Paid</td>
</tr>
<tr>
<td>Workers Paid</td>
<td>10,000 Neurons per day</td>
<td>$0.011 / 1,000 Neurons</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15804.md")
</aside>
<h2 id="pay-with-ai-gateway-credits">Pay with AI Gateway credits</h2>
<p>You can use prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a> to pay for Workers AI inference. Set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>, then specify that gateway in the <a href="/ai-gateway/usage/worker-binding-methods/">AI binding</a> or REST API request.</p>
<p>Requests to frontier models that use prepaid credits receive <a href="/workers-ai/platform/limits/#paid-models">higher rate limits</a>.</p>
<h2 id="what-are-neurons">What are Neurons?</h2>
<p>Neurons are our way of measuring AI outputs across different models, representing the GPU compute needed to perform your request. Our serverless model allows you to pay only for what you use without having to worry about renting, managing, or scaling GPUs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15803.md")
</aside>
<h2 id="llm-model-pricing">LLM model pricing</h2>
<table>
<thead>
<tr>
<th>Model</th>
<th>Price in Tokens</th>
<th>Price in Neurons</th>
</tr>
</thead>
<tbody>
<tr>
<td>@cf/meta/llama-3.2-1b-instruct</td>
<td>$0.027 per M input tokens <br/> $0.201 per M output tokens</td>
<td>2457 neurons per M input tokens <br/> 18252 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.2-3b-instruct</td>
<td>$0.051 per M input tokens <br/> $0.335 per M output tokens</td>
<td>4625 neurons per M input tokens <br/> 30475 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.1-8b-instruct-fp8-fast</td>
<td>$0.045 per M input tokens <br/> $0.384 per M output tokens</td>
<td>4119 neurons per M input tokens <br/> 34868 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.2-11b-vision-instruct</td>
<td>$0.049 per M input tokens <br/> $0.676 per M output tokens</td>
<td>4410 neurons per M input tokens <br/> 61493 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.1-70b-instruct-fp8-fast</td>
<td>$0.293 per M input tokens <br/> $2.253 per M output tokens</td>
<td>26668 neurons per M input tokens <br/> 204805 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.3-70b-instruct-fp8-fast</td>
<td>$0.293 per M input tokens <br/> $2.253 per M output tokens</td>
<td>26668 neurons per M input tokens <br/> 204805 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/deepseek-ai/deepseek-r1-distill-qwen-32b</td>
<td>$0.497 per M input tokens <br/> $4.881 per M output tokens</td>
<td>45170 neurons per M input tokens <br/> 443756 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/deepseek-ai/deepseek-v4-flash-0731</td>
<td>$0.440 per M input tokens <br/> $0.014 per M cached input tokens <br/> $1.320 per M output tokens</td>
<td>40000 neurons per M input tokens <br/> 1273 neurons per M cached input tokens <br/> 120000 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/deepseek-ai/deepseek-v4-pro-0813</td>
<td>$1.320 per M input tokens <br/> $0.044 per M cached input tokens <br/> $3.960 per M output tokens</td>
<td>120000 neurons per M input tokens <br/> 4000 neurons per M cached input tokens <br/> 360000 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/mistral/mistral-7b-instruct-v0.1</td>
<td>$0.110 per M input tokens <br/> $0.190 per M output tokens</td>
<td>10000 neurons per M input tokens <br/> 17300 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/mistralai/mistral-small-3.1-24b-instruct</td>
<td>$0.351 per M input tokens <br/> $0.555 per M output tokens</td>
<td>31876 neurons per M input tokens <br/> 50488 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.1-8b-instruct</td>
<td>$0.282 per M input tokens <br/> $0.827 per M output tokens</td>
<td>25608 neurons per M input tokens <br/> 75147 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.1-8b-instruct-fp8</td>
<td>$0.152 per M input tokens <br/> $0.287 per M output tokens</td>
<td>13778 neurons per M input tokens <br/> 26128 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3.1-8b-instruct-awq</td>
<td>$0.123 per M input tokens <br/> $0.266 per M output tokens</td>
<td>11161 neurons per M input tokens <br/> 24215 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3-8b-instruct</td>
<td>$0.282 per M input tokens <br/> $0.827 per M output tokens</td>
<td>25608 neurons per M input tokens <br/> 75147 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-3-8b-instruct-awq</td>
<td>$0.123 per M input tokens <br/> $0.266 per M output tokens</td>
<td>11161 neurons per M input tokens <br/> 24215 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-2-7b-chat-fp16</td>
<td>$0.556 per M input tokens <br/> $6.667 per M output tokens</td>
<td>50505 neurons per M input tokens <br/> 606061 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-guard-3-8b</td>
<td>$0.484 per M input tokens <br/> $0.030 per M output tokens</td>
<td>44003 neurons per M input tokens <br/> 2730 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/meta/llama-4-scout-17b-16e-instruct</td>
<td>$0.270 per M input tokens <br/> $0.850 per M output tokens</td>
<td>24545 neurons per M input tokens <br/> 77273 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/google/gemma-3-12b-it</td>
<td>$0.345 per M input tokens <br/> $0.556 per M output tokens</td>
<td>31371 neurons per M input tokens <br/> 50560 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/qwen/qwq-32b</td>
<td>$0.660 per M input tokens <br/> $1.000 per M output tokens</td>
<td>60000 neurons per M input tokens <br/> 90909 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/qwen/qwen2.5-coder-32b-instruct</td>
<td>$0.660 per M input tokens <br/> $1.000 per M output tokens</td>
<td>60000 neurons per M input tokens <br/> 90909 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/qwen/qwen3-30b-a3b-fp8</td>
<td>$0.051 per M input tokens <br/> $0.335 per M output tokens</td>
<td>4625 neurons per M input tokens <br/> 30475 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/qwen/qwen3.8-27b</td>
<td>$0.450 per M input tokens <br/> $3.200 per M output tokens</td>
<td>40909 neurons per M input tokens <br/> 290909 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/openai/gpt-oss-120b</td>
<td>$0.350 per M input tokens <br/> $0.750 per M output tokens</td>
<td>31818 neurons per M input tokens <br/> 68182 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/openai/gpt-oss-20b</td>
<td>$0.200 per M input tokens <br/> $0.300 per M output tokens</td>
<td>18182 neurons per M input tokens <br/> 27273 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/aisingapore/gemma-sea-lion-v4-27b-it</td>
<td>$0.351 per M input tokens <br/> $0.555 per M output tokens</td>
<td>31876 neurons per M input tokens <br/> 50488 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/ibm-granite/granite-4.0-h-micro</td>
<td>$0.017 per M input tokens <br/> $0.112 per M output tokens</td>
<td>1542 neurons per M input tokens <br/> 10158 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/zai-org/glm-4.7-flash</td>
<td>$0.060 per M input tokens <br/> $0.400 per M output tokens</td>
<td>5500 neurons per M input tokens <br/> 36400 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/zai-org/glm-5.2</td>
<td>$1.400 per M input tokens <br/> $0.260 per M cached input tokens <br/> $4.400 per M output tokens</td>
<td>127273 neurons per M input tokens <br/> 23636 neurons per M cached input tokens <br/> 400000 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/zai-org/glm-5.3</td>
<td>$1.400 per M input tokens <br/> $0.260 per M cached input tokens <br/> $4.400 per M output tokens</td>
<td>127273 neurons per M input tokens <br/> 23636 neurons per M cached input tokens <br/> 400000 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/zai-org/glm-5.3-flash</td>
<td>$0.150 per M input tokens <br/> $0.030 per M cached input tokens <br/> $0.500 per M output tokens</td>
<td>13636 neurons per M input tokens <br/> 2727 neurons per M cached input tokens <br/> 45455 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/nvidia/nemotron-3-120b-a12b</td>
<td>$0.500 per M input tokens <br/> $1.500 per M output tokens</td>
<td>45455 neurons per M input tokens <br/> 136364 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/moonshotai/kimi-k2.5</td>
<td>$0.600 per M input tokens <br/> $0.100 per M cached input tokens <br/> $3.000 per M output tokens</td>
<td>54545 neurons per M input tokens <br/> 9091 neurons per M cached input tokens <br/> 272727 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/moonshotai/kimi-k2.6</td>
<td>$0.950 per M input tokens <br/> $0.160 per M cached input tokens <br/> $4.000 per M output tokens</td>
<td>86364 neurons per M input tokens <br/> 14545 neurons per M cached input tokens <br/> 363636 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/moonshotai/kimi-k2.7-code</td>
<td>$0.950 per M input tokens <br/> $0.190 per M cached input tokens <br/> $4.000 per M output tokens</td>
<td>86364 neurons per M input tokens <br/> 17273 neurons per M cached input tokens <br/> 363636 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/google/gemma-4-26b-a4b-it</td>
<td>$0.100 per M input tokens <br/> $0.300 per M output tokens</td>
<td>9091 neurons per M input tokens <br/> 27273 neurons per M output tokens</td>
</tr>
</tbody>
</table>
<h2 id="embeddings-model-pricing">Embeddings model pricing</h2>
<table>
<thead>
<tr>
<th>Model</th>
<th>Price in Tokens</th>
<th>Price in Neurons</th>
</tr>
</thead>
<tbody>
<tr>
<td>@cf/baai/bge-small-en-v1.5</td>
<td>$0.020 per M input tokens</td>
<td>1841 neurons per M input tokens</td>
</tr>
<tr>
<td>@cf/baai/bge-base-en-v1.5</td>
<td>$0.067 per M input tokens</td>
<td>6058 neurons per M input tokens</td>
</tr>
<tr>
<td>@cf/baai/bge-large-en-v1.5</td>
<td>$0.204 per M input tokens</td>
<td>18582 neurons per M input tokens</td>
</tr>
<tr>
<td>@cf/baai/bge-m3</td>
<td>$0.012 per M input tokens</td>
<td>1075 neurons per M input tokens</td>
</tr>
<tr>
<td>@cf/pfnet/plamo-embedding-1b</td>
<td>$0.019 per M input tokens</td>
<td>1689 neurons per M input tokens</td>
</tr>
<tr>
<td>@cf/qwen/qwen3-embedding-0.6b</td>
<td>$0.012 per M input tokens</td>
<td>1075 neurons per M input tokens</td>
</tr>
</tbody>
</table>
<h2 id="image-model-pricing">Image model pricing</h2>
<table>
<thead>
<tr>
<th>Model</th>
<th>Price in Tokens</th>
<th>Price in Neurons</th>
</tr>
</thead>
<tbody>
<tr>
<td>@cf/black-forest-labs/flux-1-schnell</td>
<td>$0.0000528 per 512x512 tile <br/> $0.0001056 per step</td>
<td>4.80 neurons per 512x512 tile <br/> 9.60 neurons per step</td>
</tr>
<tr>
<td>@cf/leonardo/lucid-origin</td>
<td>$0.006996 per 512x512 tile <br/> $0.000132 per step</td>
<td>636.00 neurons per 512x512 tile <br/> 12.00 neurons per step</td>
</tr>
<tr>
<td>@cf/leonardo/phoenix-1.0</td>
<td>$0.005830 per 512x512 tile <br/> $0.000110 per step</td>
<td>530.00 neurons per 512x512 tile <br/> 10.00 neurons per step</td>
</tr>
<tr>
<td>@cf/black-forest-labs/flux-2-dev</td>
<td>$0.00021 per input 512x512 tile, per step <br/> $0.00041 per output 512x512 tile, per step</td>
<td>18.75 neurons per input 512x512 tile, per step <br/> 37.50 neurons per output 512x512 tile, per step</td>
</tr>
<tr>
<td>@cf/black-forest-labs/flux-2-klein-4b</td>
<td>$0.000059 per input 512x512 tile <br/> $0.000287 per output 512x512 tile</td>
<td>5.37 neurons per input 512x512 tile <br/> 26.05 neurons per output 512x512 tile</td>
</tr>
<tr>
<td>@cf/black-forest-labs/flux-2-klein-9b</td>
<td>$0.015 per first MP (1024x1024) <br/> $0.002 per subsequent MP <br/> $0.002 per input image MP</td>
<td>1363.64 neurons per first MP (1024x1024) <br/> 181.82 neurons per subsequent MP <br/> 181.82 neurons per input image MP</td>
</tr>
</tbody>
</table>
<h2 id="audio-model-pricing">Audio model pricing</h2>
<table>
<thead>
<tr>
<th>Model</th>
<th>Price in Tokens</th>
<th>Price in Neurons</th>
</tr>
</thead>
<tbody>
<tr>
<td>@cf/openai/whisper</td>
<td>$0.0005 per audio minute</td>
<td>41.14 neurons per audio minute</td>
</tr>
<tr>
<td>@cf/openai/whisper-large-v3-turbo</td>
<td>$0.0005 per audio minute</td>
<td>46.63 neurons per audio minute</td>
</tr>
<tr>
<td>@cf/myshell-ai/melotts</td>
<td>$0.0002 per audio minute</td>
<td>18.63 neurons per audio minute</td>
</tr>
<tr>
<td>@cf/deepgram/aura-1</td>
<td>$0.015 per 1k characters input <br/></td>
<td>1,363.64 neurons per 1k characters input <br/></td>
</tr>
<tr>
<td>@cf/deepgram/nova-3</td>
<td>$0.0052 per audio minute input <br/></td>
<td>472.73 neurons per audio minute input <br/></td>
</tr>
<tr>
<td>@cf/deepgram/nova-3 (WebSocket)</td>
<td>$0.0092 per audio minute input <br/></td>
<td>836.36 neurons per audio minute input <br/></td>
</tr>
<tr>
<td>@cf/pipecat-ai/smart-turn-v2</td>
<td>$0.00033795 per audio minute input <br/></td>
<td>0.51 neurons per audio minute input <br/></td>
</tr>
<tr>
<td>@cf/deepgram/aura-2-en</td>
<td>$0.030 per 1k characters input <br/></td>
<td>2727.27 neurons per 1k characters input <br/></td>
</tr>
<tr>
<td>@cf/deepgram/aura-2-es</td>
<td>$0.030 per 1k characters input <br/></td>
<td>2727.27 neurons per 1k characters input <br/></td>
</tr>
<tr>
<td>@cf/deepgram/flux (WebSocket)</td>
<td>$0.0077 per audio minute <br/></td>
<td>700.00 neurons per audio minute <br/></td>
</tr>
</tbody>
</table>
<h2 id="other-model-pricing">Other model pricing</h2>
<table>
<thead>
<tr>
<th>Model</th>
<th>Price in Tokens</th>
<th>Price in Neurons</th>
</tr>
</thead>
<tbody>
<tr>
<td>@cf/huggingface/distilbert-sst-2-int8</td>
<td>$0.026 per M input tokens</td>
<td>2394 neurons per M input tokens</td>
</tr>
<tr>
<td>@cf/baai/bge-reranker-base</td>
<td>$0.003 per M input tokens</td>
<td>283 neurons per M input tokens</td>
</tr>
<tr>
<td>@cf/meta/m2m100-1.2b</td>
<td>$0.342 per M input tokens <br/> $0.342 per M output tokens</td>
<td>31050 neurons per M input tokens <br/> 31050 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/microsoft/resnet-50</td>
<td>$2.51 per M images</td>
<td>228055 neurons per M images</td>
</tr>
<tr>
<td>@cf/ai4bharat/indictrans2-en-indic-1B</td>
<td>$0.342 per M input tokens <br/> $0.342 per M output tokens</td>
<td>31050 neurons per M input tokens <br/> 31050 neurons per M output tokens</td>
</tr>
<tr>
<td>@cf/moondream/moondream3.1-9B-A2B</td>
<td>$0.300 per M input tokens <br/> $1.000 per M output tokens</td>
<td>27273 neurons per M input tokens <br/> 90909 neurons per M output tokens</td>
</tr>
</tbody>
</table>
