<div class="agent-landing">
<header class="agent-hero">
<h1>Agent setup</h1>
<p>Connect your AI coding agent to Cloudflare, then build and deploy straight from your editor or terminal.</p>
<p><a class="primary-action" href="#pick-your-agent">Browse agents</a></p>
</header>
<section class="agent-section" aria-labelledby="pick-your-agent">
<div class="agent-section-heading"><h2 id="pick-your-agent">Pick your agent</h2>
<p>Select an agent to get step-by-step setup instructions.</p></div>
<div class="agent-filters" role="group" aria-label="Filter agents">
<span>Filter by workflow:</span>
<button type="button" data-agent-filter="all" aria-pressed="true">All</button>
<button type="button" data-agent-filter="terminal" aria-pressed="false">Terminal</button>
<button type="button" data-agent-filter="ide" aria-pressed="false">IDE</button>
<button type="button" data-agent-filter="cloud" aria-pressed="false">Cloud</button>
<button type="button" data-agent-filter="extension" aria-pressed="false">Extension</button>
</div>
<div class="agent-grid" data-agent-grid>
<a class="agent-card" href="/agent-setup/claude-code/" data-agent-card data-match="terminal extension cloud">
<div class="agent-card-title">
<img src="/icons/agents/claude/light.svg" alt="" width="24" height="24">
<div>
<span>Anthropic</span>
<h3>Claude Code</h3>
</div></div>
<p>Terminal-based coding agent that understands your codebase, runs commands, edits files, and manages git. Made by Anthropic.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/codex/" data-agent-card data-match="terminal extension cloud open_source">
<div class="agent-card-title">
<img src="/icons/agents/codex/light.svg" alt="" width="24" height="24">
<div>
<span>OpenAI</span>
<h3>Codex</h3>
</div></div>
<p>OpenAI coding agent available as a terminal CLI and desktop app. It reads and writes files, runs commands, and browses the web in a sandbox.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/cursor/" data-agent-card data-match="terminal ide cloud">
<div class="agent-card-title">
<img src="/icons/agents/cursor/light.svg" alt="" width="24" height="24">
<div>
<span>Cursor</span>
<h3>Cursor</h3>
</div></div>
<p>AI-first IDE built on VS Code with multi-file Composer edits and background agents. Made by Cursor.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/github-copilot/" data-agent-card data-match="terminal extension cloud">
<div class="agent-card-title">
<img src="/icons/agents/copilot/light.svg" alt="" width="24" height="24">
<div>
<span>GitHub</span>
<h3>GitHub Copilot</h3>
</div></div>
<p>Editor extension and CLI with agent mode, workspace context, and native PR integration. Made by GitHub.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/opencode/" data-agent-card data-match="terminal extension open_source">
<div class="agent-card-title">
<img src="/icons/agents/opencode/light.svg" alt="" width="24" height="24">
<div>
<span>Anomaly</span>
<h3>OpenCode</h3>
</div></div>
<p>Open-source terminal agent with a rich TUI that works with 75+ LLMs. Made by Anomaly.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/windsurf/" data-agent-card data-match="ide">
<div class="agent-card-title">
<img src="/icons/agents/windsurf/light.svg" alt="" width="24" height="24">
<div>
<span>Cognition</span>
<h3>Windsurf</h3>
</div></div>
<p>Agentic IDE with Cascade context and Flows for multi-step tasks. Made by Cognition.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/visual-studio-code/" data-agent-card data-match="terminal ide extension open_source">
<div class="agent-card-title">
<img src="/icons/agents/visual-studio-code/light.svg" alt="" width="24" height="24">
<div>
<span>Microsoft</span>
<h3>Visual Studio Code</h3>
</div></div>
<p>Free, open-source code editor with native Model Context Protocol (MCP) client support and Copilot Chat integration. Made by Microsoft.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/command-code/" data-agent-card data-match="terminal extension cloud">
<div class="agent-card-title">
<img src="/icons/agents/command-code/light.svg" alt="" width="24" height="24">
<div>
<span>Command Code</span>
<h3>Command Code</h3>
</div></div>
<p>Command Code is one of the most used coding agents for open models. It automatically learns your coding taste and self-improves as you work.</p>
<strong>View guide →</strong>
</a>
<a class="agent-card" href="/agent-setup/bionic/" data-agent-card data-match="cloud">
<div class="agent-card-title">
<img src="/icons/agents/bionic/light.svg" alt="" width="24" height="24">
<div>
<span>LM Studio</span>
<h3>Bionic</h3>
</div></div>
<p>Powerful agent for coding and work. Natively local, with open models in the cloud. By LM Studio.</p>
<strong>View guide →</strong>
</a>
</div></section>
<section class="agent-section" aria-labelledby="compare-agents">
<div class="agent-section-heading"><h2 id="compare-agents">Compare agents</h2>
<p>Capabilities, pricing, and context approaches compared.</p></div>
<div class="table-scroll"><table class="agent-comparison"><thead><tr>
<th>Agent</th><th>Terminal</th><th>IDE</th><th>Extension</th><th>Cloud</th>
<th>Pricing</th><th>Model</th><th>Context</th><th>Open source</th>
</tr></thead><tbody>
<tr>
<th><a href="/agent-setup/bionic/">Bionic</a></th>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Hybrid</td>
<td>Multi-provider</td>
<td>—</td>
<td>No</td></tr>
<tr>
<th><a href="/agent-setup/claude-code/">Claude Code</a></th>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Subscription</td>
<td>Locked</td>
<td>Project memory</td>
<td>No</td></tr>
<tr>
<th><a href="/agent-setup/codex/">Codex</a></th>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Hybrid</td>
<td>Locked</td>
<td>Project memory</td>
<td>Yes</td></tr>
<tr>
<th><a href="/agent-setup/command-code/">Command Code</a></th>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Subscription</td>
<td>Multi-provider</td>
<td>Project memory</td>
<td>No</td></tr>
<tr>
<th><a href="/agent-setup/cursor/">Cursor</a></th>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Subscription</td>
<td>Multi-provider</td>
<td>Indexed codebase</td>
<td>No</td></tr>
<tr>
<th><a href="/agent-setup/github-copilot/">GitHub Copilot</a></th>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Subscription</td>
<td>Multi-provider</td>
<td>Indexed codebase</td>
<td>No</td></tr>
<tr>
<th><a href="/agent-setup/opencode/">OpenCode</a></th>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
<td>BYOK</td>
<td>Multi-provider</td>
<td>Project memory</td>
<td>Yes</td></tr>
<tr>
<th><a href="/agent-setup/visual-studio-code/">Visual Studio Code</a></th>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
<td>BYOK</td>
<td>Multi-provider</td>
<td>Project memory</td>
<td>Yes</td></tr>
<tr>
<th><a href="/agent-setup/windsurf/">Windsurf</a></th>
<td>No</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>Subscription</td>
<td>Multi-provider</td>
<td>Indexed codebase</td>
<td>No</td></tr>
</tbody></table></div><p class="agent-table-note">Every agent listed supports Skills and MCP.</p></section>
<section class="agent-section" aria-labelledby="understanding-agents">
<div class="agent-section-heading"><h2 id="understanding-agents">Understanding agents</h2>
<p>Common types, concepts, and tradeoffs.</p></div>
<h3>Workflow</h3><p>Where the agent runs changes how you interact with it.</p>
<div class="agent-primer-grid">
<article><strong>Terminal</strong><p>Runs in a shell. Best for automation, scripting, and CI pipelines.</p></article>
<article><strong>IDE</strong><p>Full code editor with AI first-class. Visual diffs, multi-file edits.</p></article>
<article><strong>Cloud</strong><p>Hosted infrastructure. Ideal for async, long-running work.</p></article>
<article><strong>Extension</strong><p>Plugs into an existing editor. Lightest install, keeps your setup.</p></article>
</div><h3>Key concepts</h3><p>The vocabulary you will run into when comparing agents.</p>
<div class="agent-primer-grid">
<article><strong>Skills</strong><p>Reusable prompt packages that teach an agent about a specific domain.</p></article>
<article><strong>MCP</strong><p>The Model Context Protocol lets agents call external tools and APIs.</p></article>
<article><strong>Model flexibility</strong><p>Locked agents use one vendor; BYOK and multi-provider agents offer more choice.</p></article>
<article><strong>Context</strong><p>Project memory and codebase indexes retain information beyond one conversation.</p></article>
</div><h3>Common tradeoffs</h3><p>Decisions you will make when picking an agent.</p>
<div class="agent-primer-grid">
<article><strong>Cloud vs. Local</strong><p>Hosted agents offer remote execution; local agents keep code on your machine.</p></article>
<article><strong>Proprietary vs. Open source</strong><p>Open-source agents can be inspected, modified, and forked.</p></article>
<article><strong>Locked model vs. BYOK</strong><p>BYOK agents let you switch providers and models.</p></article>
<article><strong>Session vs. Indexed codebase</strong><p>Persistent indexes retrieve project files beyond one session.</p></article>
</div></section></div>
