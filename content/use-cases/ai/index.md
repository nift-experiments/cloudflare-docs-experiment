<p>Build and deploy AI applications on Cloudflare's global network with inference at the edge, vector databases, and model gateways. Workers AI runs Large Language Models (LLMs), text embeddings, image generation, and other models with pay-per-use pricing. AI Gateway proxies requests to OpenAI, Anthropic, and other providers with caching and unified analytics. Vectorize stores embeddings for Retrieval Augmented Generation (RAG) workflows.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/uv1Cz_BDFmo" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>AI applications can present unique infrastructure challenges, such as unpredictable inference costs, latency-sensitive user experiences, and the need to work with multiple model providers. Cloudflare provides a complete platform for building AI applications that are fast, cost-effective, and globally distributed.</p>
<ul class="directory-listing"><li><a href="/use-cases/ai/build-and-run/">Build and run AI applications</a></li><li><a href="/use-cases/ai/store-and-retrieve-context/">Store and retrieve context</a></li><li><a href="/use-cases/ai/control-costs/">Control costs and improve quality</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="retrieval-augmented-generation-rag">Retrieval Augmented Generation (RAG)</h3>
<p>Combine vector search with Large Language Model (LLM) inference to ground responses in your own data:</p>
<ul>
<li><strong>Vectorize</strong> stores embeddings of your knowledge base</li>
<li><strong>Workers</strong> receives user queries and searches for relevant context</li>
<li><strong>Workers AI</strong> or <strong>AI Gateway</strong> generates responses using retrieved context</li>
</ul>
<h3 id="multi-provider-ai-gateway">Multi-provider AI gateway</h3>
<p>Use AI Gateway to route requests across providers while maintaining a single interface:</p>
<ul>
<li><strong>AI Gateway</strong> proxies requests to OpenAI, Anthropic, or Workers AI</li>
<li>Built-in caching reduces costs for repeated queries</li>
<li>Unified logging and analytics across all providers</li>
</ul>
<h3 id="real-time-ai-features">Real-time AI features</h3>
<p>Deploy low-latency AI features directly at the edge:</p>
<ul>
<li><strong>Workers</strong> handles requests at the nearest Cloudflare location and runs inference via the Workers AI binding — no round-trips to origin servers</li>
<li><strong>KV</strong> caches frequent responses to reduce inference calls and latency</li>
<li><strong>D1</strong> stores session state and conversation history alongside the inference logic</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) installed on your machine.</li>
<li><a href="/workers/wrangler/install-and-update/">Wrangler</a> installed. Wrangler is the command-line interface (CLI) for deploying Workers and managing bindings.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li><a href="/ai-gateway/">AI Gateway</a> does not require a domain added to Cloudflare. You can place it in front of any existing AI provider (OpenAI, Anthropic, and others) by updating your API endpoint to route through AI Gateway.</li>
<li>If you plan to add Workers AI inference or Vectorize to an existing application, you also need <a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) and <a href="/workers/wrangler/install-and-update/">Wrangler</a> installed.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15249.md")
</div>
