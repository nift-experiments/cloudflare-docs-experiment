---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/tutorials/openai-agents/
  description: Use the OpenAI Agents SDK with Cloudflare Sandbox to build a Python agent that writes, tests, and delivers code in an isolated environment.
  full_title: Build an AI coding agent with OpenAI Agents SDK · Cloudflare Sandbox SDK docs
  head_html: <title>Build an AI coding agent with OpenAI Agents SDK · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the OpenAI Agents SDK with Cloudflare Sandbox to build a Python agent that writes, tests, and delivers code in an isolated environment."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/tutorials/openai-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/tutorials/openai-agents/index.md"><meta property="og:title" content="Build an AI coding agent with OpenAI Agents SDK · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the OpenAI Agents SDK with Cloudflare Sandbox to build a Python agent that writes, tests, and delivers code in an isolated environment."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/tutorials/openai-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Sandbox SDK"><meta name="pcx_tags" content="Python,OpenAI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/tutorials/openai-agents/#page","headline":"Build an AI coding agent with OpenAI Agents SDK \u00b7 Cloudflare Sandbox SDK docs","description":"Use the OpenAI Agents SDK with Cloudflare Sandbox to build a Python agent that writes, tests, and delivers code in an isolated environment.","url":"https://developers.cloudflare.com/sandbox/tutorials/openai-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Python","OpenAI"]}</script>
  markdown: true
  noindex: false
  route: /sandbox/tutorials/openai-agents/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13308.md")
</aside>
<p>The <a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a> is a lightweight Python framework for building multi-agent workflows. A Cloudflare Sandbox integration is provided out of the box and ensures that the SDK includes a first-class Cloudflare backend that gives your agents isolated containers for running code, installing packages, and managing files.</p>
<p>In this tutorial, you will deploy a sandbox bridge Worker and build a Python agent that accepts a coding task, executes it inside a Cloudflare Sandbox, and copies the output files to your local machine.</p>
<p><strong>Time to complete</strong>: 20 minutes</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> with the Containers / Sandbox beta enabled.</li>
<li>Install <a href="https://www.python.org/">Python 3.12+</a> and <a href="https://docs.astral.sh/uv/">uv</a>.</li>
<li>Obtain an <a href="https://platform.openai.com/api-keys">OpenAI API key</a>.</li>
</ol>
<h2 id="1-deploy-the-sandbox-bridge"><ol>
<li>Deploy the sandbox bridge</li>
</ol></h2>
<p>The <a href="/sandbox/bridge/">sandbox bridge</a> is a Cloudflare Worker that exposes the Sandbox API over HTTP so non-Worker clients — such as a Python script using the OpenAI Agents SDK — can create and control sandboxes.</p>
<p>The Sandbox environment comes pre-configured for Node.js and Python development, so your agents can start writing and running code immediately.</p>
<p>Deploy the bridge to your Cloudflare account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/sandbox-sdk/tree/main/bridge/worker"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The button deploys the Worker and generates a <code>SANDBOX_API_KEY</code> secret for authentication. When deployment finishes, note your Worker URL and API key — you will need them in the next step.</p>
<details class="nb-details"><summary>Manual deployment</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13309.md")
</div></details>
<h2 id="2-set-up-your-python-project"><ol start="2">
<li>Set up your Python project</li>
</ol></h2>
<p>Create a new directory for the agent:</p>
<pre tabindex="0"><code class="language-sh">mkdir openai-sandbox-agent &amp;&amp; cd openai-sandbox-agent&#10;</code></pre>
<p>Create a <code>.env</code> file with your credentials:</p>
<pre tabindex="0"><code class="language-sh">OPENAI_API_KEY=sk-your-openai-key&#10;CLOUDFLARE_SANDBOX_API_KEY=your-bridge-token&#10;CLOUDFLARE_SANDBOX_WORKER_URL=https://cloudflare-sandbox-bridge.your-subdomain.workers.dev&#10;</code></pre>
<h2 id="3-build-the-agent"><ol start="3">
<li>Build the agent</li>
</ol></h2>
<p>Create <code>main.py</code> with the following content. The inline script metadata tells <code>uv</code> which dependencies to install, so everything is contained in a single file:</p>
<pre tabindex="0"><code class="language-python">&#35; /// script&#10;&#35; requires-python = &quot;&gt;=3.12&quot;&#10;&#35; dependencies = [&quot;openai-agents[cloudflare]&quot;]&#10;&#35; ///&#10;&quot;&quot;&quot;One-shot coding agent backed by a Cloudflare Sandbox.&quot;&quot;&quot;&#10;&#10;from __future__ import annotations&#10;&#10;import asyncio&#10;import os&#10;import sys&#10;from pathlib import Path&#10;&#10;from agents import Runner&#10;from agents.extensions.sandbox.cloudflare import (&#10;    CloudflareSandboxClient,&#10;    CloudflareSandboxClientOptions,&#10;)&#10;from agents.run import RunConfig&#10;from agents.sandbox import SandboxAgent, SandboxRunConfig&#10;from agents.sandbox.capabilities import Shell&#10;&#10;MODEL = &quot;gpt-5.4&quot;&#10;&#10;INSTRUCTIONS = &quot;&quot;&quot;\&#10;You are an expert developer working inside a sandbox.&#10;The sandbox has bun, node, npm, and python available on the PATH.&#10;Implement the user&#x27;s task in /workspace, test it, then copy deliverable files to /workspace/output/.&#10;&quot;&quot;&quot;.strip()&#10;&#10;&#10;async def copy_output(session, dest: Path) -&gt; list[Path]:&#10;    &quot;&quot;&quot;Download files from /workspace/output/ in the sandbox to a local directory.&quot;&quot;&quot;&#10;    dest.mkdir(parents=True, exist_ok=True)&#10;    ls = await session.exec(&quot;find&quot;, &quot;/workspace/output&quot;, &quot;-maxdepth&quot;, &quot;1&quot;, &quot;-type&quot;, &quot;f&quot;, shell=False)&#10;    if not ls.ok():&#10;        return []&#10;    copied: list[Path] = []&#10;    for name in (l.strip() for l in ls.stdout.decode().splitlines() if l.strip()):&#10;        handle = await session.read(Path(name))&#10;        local = dest / Path(name).name&#10;        payload = handle.read(); handle.close()&#10;        local.write_bytes(payload if isinstance(payload, bytes) else payload.encode())&#10;        copied.append(local)&#10;    return copied&#10;&#10;&#10;async def run(prompt: str, output_dir: Path) -&gt; None:&#10;    worker_url = os.environ.get(&quot;CLOUDFLARE_SANDBOX_WORKER_URL&quot;, &quot;&quot;)&#10;    if not worker_url:&#10;        sys.exit(&quot;Error: CLOUDFLARE_SANDBOX_WORKER_URL is not set.&quot;)&#10;&#10;    agent = SandboxAgent(&#10;        name=&quot;Developer&quot;,&#10;        model=MODEL,&#10;        instructions=INSTRUCTIONS,&#10;        capabilities=[Shell()],&#10;    )&#10;&#10;    client = CloudflareSandboxClient()&#10;    options = CloudflareSandboxClientOptions(worker_url=worker_url)&#10;    session = await client.create(manifest=agent.default_manifest, options=options)&#10;&#10;    try:&#10;        async with session:&#10;            run_config = RunConfig(&#10;                sandbox=SandboxRunConfig(session=session),&#10;                tracing_disabled=True,&#10;            )&#10;&#10;            &#35; Stream tool calls so the user can follow progress.&#10;            result = Runner.run_streamed(agent, prompt, run_config=run_config)&#10;            async for ev in result.stream_events():&#10;                if ev.type == &quot;run_item_stream_event&quot; and ev.name == &quot;tool_called&quot;:&#10;                    print(f&quot;  [tool] {getattr(ev.item.raw_item, &#x27;name&#x27;, &#x27;&#x27;)}&quot;)&#10;                elif ev.type == &quot;run_item_stream_event&quot; and ev.name == &quot;tool_output&quot;:&#10;                    print(f&quot;  [output] {str(getattr(ev.item, &#x27;output&#x27;, &#x27;&#x27;))[:200]}&quot;)&#10;&#10;            &#35; Copy output files from the sandbox to the local machine.&#10;            copied = await copy_output(session, output_dir)&#10;            if copied:&#10;                print(f&quot;\nCopied {len(copied)} file(s) to {output_dir}:&quot;)&#10;                for p in copied:&#10;                    print(f&quot;   {p}&quot;)&#10;            else:&#10;                print(&quot;\nAgent did not produce any output files.&quot;)&#10;    finally:&#10;        await client.delete(session)&#10;&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    prompt = sys.argv[1] if len(sys.argv) &gt; 1 else &quot;Create a hello world HTTP server using Bun.serve&quot;&#10;    asyncio.run(run(prompt, Path(&quot;output&quot;)))&#10;</code></pre>
<p>Here is what the key pieces do:</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SandboxAgent</code></td>
<td>An <code>Agent</code> subclass that accepts sandbox-specific configuration, including <code>capabilities</code>.</td>
</tr>
<tr>
<td><code>Shell()</code></td>
<td>A capability that exposes a shell tool to the LLM, allowing it to run commands inside the sandbox.</td>
</tr>
<tr>
<td><code>CloudflareSandboxClient</code></td>
<td>Creates and manages sandbox sessions through the bridge Worker. Reads <code>CLOUDFLARE_SANDBOX_API_KEY</code> from the environment for authentication.</td>
</tr>
<tr>
<td><code>CloudflareSandboxClientOptions</code></td>
<td>Points the client at your bridge Worker URL.</td>
</tr>
<tr>
<td><code>Runner.run_streamed()</code></td>
<td>Executes the agent and yields streaming events for tool calls and text output.</td>
</tr>
<tr>
<td><code>SandboxRunConfig</code></td>
<td>Attaches a live sandbox session to the run so the agent's tools execute inside the container.</td>
</tr>
</tbody>
</table>
<h2 id="4-run-the-agent"><ol start="4">
<li>Run the agent</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">uv run --env-file .env main.py &quot;Create a hello world HTTP server using Bun.serve&quot;&#10;</code></pre>
<p>You should see tool calls and output streaming to the console:</p>
<pre tabindex="0"><code class="language-txt">Sending task to sandbox agent (gpt-5.4)...&#10;  [tool] exec_command&#10;  [output] exit_code=0 stdout: mkdir: created directory &#x27;/workspace/output&#x27;&#10;  [tool] exec_command&#10;  [output] exit_code=0 stdout: Listening on http://localhost:3000&#10;&#10;Copied 1 file(s) to output:&#10;   output/server.ts&#10;</code></pre>
<p>The agent wrote the code, tested it inside the sandbox, and copied the deliverable to your local machine.</p>
<h2 id="what-you-built">What you built</h2>
<p>You built a Python coding agent that:</p>
<ul>
<li>Accepts a natural-language coding task</li>
<li>Executes code in an isolated Cloudflare Sandbox container</li>
<li>Installs packages, runs tests, and iterates until the task is complete</li>
<li>Copies deliverable files back to your local machine</li>
</ul>
<p>The bridge Worker's <code>Dockerfile</code> can be fully customized to suit your needs — install additional languages, system packages, or tools to match your use case.</p>
<p>The Cloudflare Sandbox provides more capabilities you can integrate into your agents:</p>
<ul>
<li><strong>PTY sessions</strong> — Open interactive terminal sessions to sandboxes via WebSocket for real-time I/O.</li>
<li><strong>Bucket mounts</strong> — Mount R2 or S3-compatible buckets as local directories inside the sandbox for persistent data.</li>
<li><strong>Workspace backup and restore</strong> — Persist workspace state with <code>persist_workspace()</code> and <code>hydrate_workspace()</code> to resume work across sandbox lifecycles.</li>
<li><strong>File operations</strong> — Read, write, and manage files programmatically within the sandbox.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="https://github.com/cloudflare/sandbox-sdk/tree/main/bridge/examples/workspace-chat">Workspace chat example</a> — A full-stack chat application with a file browser sidebar, built with the OpenAI Agents SDK and Cloudflare Sandbox.</li>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK documentation</a> — Learn about multi-agent handoffs, guardrails, tracing, and more.</li>
<li><a href="/sandbox/bridge/">Sandbox bridge</a> — Overview of the bridge Worker, usage examples, and configuration.</li>
<li><a href="/sandbox/bridge/http-api/">HTTP API reference</a> — Complete route reference for the bridge API.</li>
<li><a href="/sandbox/tutorials/">Sandbox tutorials</a> — More tutorials covering code execution, data analysis, and CI/CD pipelines.</li>
</ul>
