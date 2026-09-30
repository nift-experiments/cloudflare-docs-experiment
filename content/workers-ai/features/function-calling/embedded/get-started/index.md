<p>This guide will instruct you through setting up and deploying your first Workers AI project with embedded function calling. You will use Workers, a Workers AI binding, the <a href="https://github.com/cloudflare/ai-utils"><code>ai-utils package</code></a>, and a large language model (LLM) to deploy your first AI-powered application on the Cloudflare global network with embedded function calling.</p>
<h2 id="1-create-a-worker-project-with-workers-ai"><ol>
<li>Create a Worker project with Workers AI</li>
</ol></h2>
<p>Follow the <a href="/workers-ai/get-started/workers-wrangler/">Workers AI Get Started Guide</a> until step 2.</p>
<h2 id="2-install-additional-npm-package"><ol start="2">
<li>Install additional npm package</li>
</ol></h2>
<p>Next, run the following command in your project repository to install the Worker AI utilities package.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/ai-utils</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/ai-utils" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-add-workers-ai-embedded-function-calling"><ol start="3">
<li>Add Workers AI Embedded function calling</li>
</ol></h2>
<p>Update the <code>index.ts</code> file in your application directory with the following code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15831.md")
</div>
<p>This example imports the utils with <code>import { runWithTools} from &quot;@cloudflare/ai-utils&quot;</code> and follows the API reference below.</p>
<p>Moreover, in this example we define and describe a list of tools that the LLM can leverage to respond to the user query. Here, the list contains of only one tool, the <code>sum</code> function.</p>
<p>Abstracted by the <code>runWithTools</code> function, the following steps occur:</p>
<pre><code class="language-mermaid">sequenceDiagram&#10;    participant Worker as Worker&#10;    participant WorkersAI as Workers AI&#10;&#10;    Worker-&gt;&gt;+WorkersAI: Send messages, function calling prompt, and available tools&#10;    WorkersAI-&gt;&gt;+Worker: Select tools and arguments for function calling&#10;    Worker--&gt;&gt;-Worker: Execute function&#10;    Worker--&gt;&gt;+WorkersAI: Send messages, function calling prompt and function result&#10;    WorkersAI--&gt;&gt;-Worker: Send response incorporating function output&#10;</code></pre>
<p>The <code>ai-utils package</code> is also open-sourced on <a href="https://github.com/cloudflare/ai-utils">Github</a>.</p>
<h2 id="4-local-development-deployment"><ol start="4">
<li>Local development &amp; deployment</li>
</ol></h2>
<p>Follow steps 4 and 5 of the <a href="/workers-ai/get-started/workers-wrangler/">Workers AI Get Started Guide</a> for local development and deployment.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-embedded-function-calling-charges">Workers AI Embedded Function Calling charges</h3>
@markup("md", "content/.markup/bodies/15830.md")
</aside>
<h2 id="api-reference">API reference</h2>
<p>For more details, refer to <a href="/workers-ai/features/function-calling/embedded/api-reference/">API reference</a>.</p>
