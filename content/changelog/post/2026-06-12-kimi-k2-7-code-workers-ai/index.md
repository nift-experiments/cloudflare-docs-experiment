<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 12, 2026</time><h2 id="post-title">Moonshot AI Kimi K2.7 Code now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a> is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.</p>
<h4 id="improved-coding-and-agent-performance">Improved coding and agent performance</h4>
<p>K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:</p>
<ul>
<li><strong>+21.8%</strong> on Kimi Code Bench v2</li>
<li><strong>+11.0%</strong> on Program Bench</li>
<li><strong>+31.5%</strong> on MLS Bench Lite</li>
</ul>
<h4 id="reasoning-efficiency">Reasoning efficiency</h4>
<p>K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.</p>
<h4 id="key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with improved instruction following and higher end-to-end coding task success rates</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth via <code>chat_template_kwargs.thinking</code></li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Structured outputs</strong> with JSON schema support</li>
</ul>
<h4 id="differences-from-kimi-k2-6">Differences from Kimi K2.6</h4>
<p>If you are migrating from Kimi K2.6, note the following:</p>
<ul>
<li>K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency</li>
<li>Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)</li>
<li>API usage is identical — no parameter changes required</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Use Kimi K2.7 Code through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.7-code/">Kimi K2.7 Code model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div></article></div>
