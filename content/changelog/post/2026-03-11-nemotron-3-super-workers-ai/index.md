<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 11, 2026</time><h2 id="post-title">NVIDIA Nemotron 3 Super now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We're excited to partner with NVIDIA to bring <a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a> to Workers AI. NVIDIA Nemotron 3 Super is a Mixture-of-Experts (MoE) model with a hybrid Mamba-transformer architecture, 120B total parameters, and 12B active parameters per forward pass.</p>
<p>The model is optimized for running many collaborating agents per application. It delivers high accuracy for reasoning, tool calling, and instruction following across complex multi-step tasks.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Hybrid Mamba-transformer architecture</strong> delivers over 50% higher token generation throughput compared to leading open models, reducing latency for real-world applications</li>
<li><strong>Tool calling</strong> support for building AI agents that invoke tools across multiple conversation turns</li>
<li><strong>Multi-Token Prediction (MTP)</strong> accelerates long-form text generation by predicting several future tokens simultaneously in a single forward pass</li>
<li><strong>32,000 token context window</strong> for retaining conversation history and plan states across multi-step agent workflows</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="prompt-caching">Prompt caching</h4>
@markup("md", "content/.markup/bodies/17818.md")</aside>
<p>Use Nemotron 3 Super through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/nemotron-3-120b-a12b/">Nemotron 3 Super model page</a>.</p>
</div></article></div>
