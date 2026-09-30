<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 20, 2026</time><h2 id="post-title">Moonshot AI Kimi K2.6 now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.</p>
<p>Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).</p>
<h4 id="key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python</li>
<li><strong>Coding-driven design</strong> that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows</li>
<li><strong>Agent swarm orchestration</strong> scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
</ul>
<h4 id="differences-from-kimi-k2-5">Differences from Kimi K2.5</h4>
<p>If you are migrating from Kimi K2.5, note the following API changes:</p>
<ul>
<li>K2.6 uses <code>chat_template_kwargs.thinking</code> to control reasoning, replacing <code>chat_template_kwargs.enable_thinking</code></li>
<li>K2.6 returns reasoning content in the <code>reasoning</code> field, replacing <code>reasoning_content</code></li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Use Kimi K2.6 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.6/">Kimi K2.6 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div></article></div>
