<p>Build a Worker that takes a repository URL and a task description and uses Sandbox SDK to run Claude Code to implement your task.</p>
<p><strong>Time to complete:</strong> 5 minutes</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13333.md")
</div></details>
<p>You'll also need:</p>
<ul>
<li>An <a href="https://console.anthropic.com/">Anthropic API key</a> for Claude Code</li>
<li><a href="https://www.docker.com/">Docker</a> running locally</li>
</ul>
<h2 id="1-create-your-project"><ol>
<li>Create your project</li>
</ol></h2>
<p>Create a new Sandbox SDK project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- claude-code-sandbox --template=cloudflare/sandbox-sdk/examples/claude-code</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- claude-code-sandbox --template=cloudflare/sandbox-sdk/examples/claude-code" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare claude-code-sandbox --template=cloudflare/sandbox-sdk/examples/claude-code</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare claude-code-sandbox --template=cloudflare/sandbox-sdk/examples/claude-code" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest claude-code-sandbox --template=cloudflare/sandbox-sdk/examples/claude-code</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest claude-code-sandbox --template=cloudflare/sandbox-sdk/examples/claude-code" aria-label="Copy to clipboard">Copy</button></div></div>
<pre><code class="language-sh">cd claude-code-sandbox&#10;</code></pre>
<h2 id="2-set-up-local-environment-variables"><ol start="2">
<li>Set up local environment variables</li>
</ol></h2>
<p>Create a <code>.dev.vars</code> file in your project root for local development:</p>
<pre><code class="language-sh">echo &quot;ANTHROPIC_API_KEY=your_api_key_here&quot; &gt; .dev.vars&#10;</code></pre>
<p>Replace <code>your_api_key_here</code> with your actual API key from the <a href="https://console.anthropic.com/">Anthropic Console</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13332.md")
</aside>
<h2 id="3-test-locally"><ol start="3">
<li>Test locally</li>
</ol></h2>
<p>Start the development server:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13331.md")
</aside>
<p>Test with curl:</p>
<pre><code class="language-sh">curl -X POST http://localhost:8787/ \&#10;  &#45;d &#x27;{&#10;    &quot;repo&quot;: &quot;https://github.com/cloudflare/agents&quot;,&#10;    &quot;task&quot;: &quot;remove the emojis from the readme&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Response:</p>
<pre><code class="language-json">{&#10;	&quot;logs&quot;: &quot;Done! I&#x27;ve removed the brain emoji from the README title. The heading now reads \&quot;# Cloudflare Agents\&quot; instead of \&quot;# 🧠 Cloudflare Agents\&quot;.&quot;,&#10;	&quot;diff&quot;: &quot;diff --git a/README.md b/README.md\nindex 9296ac9..027c218 100644\n--- a/README.md\n+++ b/README.md\n@@ -1,4 +1,4 @@\n-# 🧠 Cloudflare Agents\n+# Cloudflare Agents\n \n ![npm install agents](assets/npm-install-agents.svg)\n &quot;&#10;}&#10;</code></pre>
<h2 id="4-deploy"><ol start="4">
<li>Deploy</li>
</ol></h2>
<p>Deploy your Worker:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Then set your Anthropic API key as a production secret:</p>
<pre><code class="language-sh">npx wrangler secret put ANTHROPIC_API_KEY&#10;</code></pre>
<p>Paste your API key from the <a href="https://console.anthropic.com/">Anthropic Console</a> when prompted.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13330.md")
</aside>
<h2 id="what-you-built">What you built</h2>
<p>You created an API that:</p>
<ul>
<li>Accepts a repository URL and natural language task descriptions</li>
<li>Creates a Sandbox and clones the repository into it</li>
<li>Kicks off Claude Code to implement the given task</li>
<li>Returns Claude's output and changes</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/sandbox/tutorials/analyze-data-with-ai/">Analyze data with AI</a> - Add pandas and matplotlib for data analysis</li>
<li><a href="/sandbox/api/interpreter/">Code Interpreter API</a> - Use the built-in code interpreter instead of exec</li>
<li><a href="/sandbox/guides/streaming-output/">Streaming output</a> - Show real-time execution progress</li>
<li><a href="/sandbox/api/">API reference</a> - Explore all available methods</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://docs.anthropic.com/">Anthropic Claude documentation</a></li>
<li><a href="/workers-ai/">Workers AI</a> - Use Cloudflare's built-in models</li>
</ul>
