<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 4, 2026</time><h2 id="post-title">Google Gemma 4 26B A4B now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We are partnering with Google to bring <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> to Workers AI. Gemma 4 26B A4B is a Mixture-of-Experts (MoE) model built from Gemini 3 research, with 26B total parameters and only 4B active per forward pass. By activating a small subset of parameters during inference, the model runs almost as fast as a 4B-parameter model while delivering the quality of a much larger one.</p>
<p>Gemma 4 is Google's most capable family of open models, designed to maximize intelligence-per-parameter.</p>
<h4 id="key-capabilities">Key capabilities</h4>
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
</div></article></div>
