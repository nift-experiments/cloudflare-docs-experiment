<p>Enable conversational search on your website with NLWeb and Cloudflare AI Search. This template crawls your site, indexes the content, and deploys NLWeb-standard endpoints to serve both people and AI agents.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/Az6NKLjSZMM" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3018.md")
</aside>
<h2 id="what-is-nlweb">What is NLWeb</h2>
<p><a href="https://github.com/nlweb-ai/NLWeb">NLWeb</a> is an open project developed by Microsoft that defines a standard protocol for natural language queries on websites. Its goal is to make every website as accessible and interactive as a conversational AI app, so both people and AI agents can reliably query site content. It does this by exposing two key endpoints:</p>
<ul>
<li><code>/ask</code>: Conversational endpoint for user queries</li>
<li><code>/mcp</code>: Structured Model Context Protocol (MCP) endpoint for AI agents</li>
</ul>
<h2 id="how-to-use-it">How to use it</h2>
<p>You can deploy NLWeb on your website directly through the AI Search dashboard:</p>
<ol>
<li>Log in to your <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Go to <strong>AI</strong> &gt; <strong>AI Search</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Create AI Search</strong>.</li>
<li>Select <strong>Website</strong> as a data source.</li>
<li>Follow the instructions to create an AI Search instance.</li>
<li>Go to the <strong>Settings</strong> for the instance</li>
<li>Find <strong>NLWeb Worker</strong> and select &quot;Enable AI Search for your website&quot;.</li>
</ol>
<p>Once complete, AI Search will deploy an NLWeb Worker for you that enables you to use the NLWeb API endpoints.</p>
<h2 id="what-this-template-includes">What this template includes</h2>
<p>Choosing the NLWeb Website option extends a normal AI Search by tailoring it for content‑heavy websites and giving you everything that is required to adopt NLWeb as the standard for conversational search on your site. Specifically, the template provides:</p>
<ul>
<li><strong>Website as a data source:</strong> Uses <a href="/ai-search/configuration/data-source/website/">Website</a> as data source option to crawl and ingest pages with the Rendered Sites option.</li>
<li><strong>Defaults for content-heavy websites:</strong> Applies tuned embedding and retrieval configurations ideal for publishing and content‑rich websites.</li>
<li><strong>NLWeb Worker deployment:</strong> Automatically spins up a Cloudflare Worker from the <a href="https://github.com/cloudflare/templates">NLWeb Worker template</a>.</li>
</ul>
<h2 id="what-the-worker-includes">What the Worker includes</h2>
<p>Your deployed Worker provides two endpoints:</p>
<ul>
<li><code>/ask</code>: NLWeb’s standard conversational endpoint
<ul>
<li>Powers the conversational UI at the root (<code>/</code>)</li>
<li>Powers the embeddable preview widget (<code>/snippet.html</code>)</li>
</ul>
</li>
<li><code>/mcp</code>: NLWeb’s MCP server endpoint for trusted AI agents</li>
</ul>
<p>These endpoints give both people and agents structured access to your content.</p>
<h2 id="using-it-on-your-website">Using it on your website</h2>
<p>You can use the embeddable snippet to add a search UI directly into your website. For example:</p>
<pre><code class="language-html">&lt;!-- Add css on head --&gt;&#10;&lt;link rel=&quot;stylesheet&quot; href=&quot;https://ask.example.com/nlweb-dropdown-chat.css&quot; /&gt;&#10;&lt;link rel=&quot;stylesheet&quot; href=&quot;https://ask.example.com/common-chat-styles.css&quot; /&gt;&#10;&#10;&lt;!-- Add container on body --&gt;&#10;&lt;div id=&quot;docs-search-container&quot;&gt;&lt;/div&gt;&#10;&#10;&lt;!-- Include JavaScript --&gt;&#10;&lt;script type=&quot;module&quot;&gt;&#10;	import { NLWebDropdownChat } from &quot;https://ask.example.com/nlweb-dropdown-chat.js&quot;;&#10;&#10;	const chat = new NLWebDropdownChat({&#10;		containerId: &quot;docs-search-container&quot;,&#10;		site: &quot;https://ask.example.com&quot;,&#10;		placeholder: &quot;Search for docs...&quot;,&#10;		endpoint: &quot;https://ask.example.com&quot;,&#10;	});&#10;&lt;/script&gt;&#10;</code></pre>
<p>This lets you serve conversational AI search directly from your own domain, with control over how people and agents access your content.</p>
<h2 id="modifying-or-updating-the-worker">Modifying or updating the Worker</h2>
<p>You may want to customize your Worker, for example, to adjust the UI for the embeddable snippet. In those cases, we recommend calling the <code>/ask</code> endpoint for queries, and building your own UI on top of it. However, you may also choose to modify the Worker's code for the embeddable UI.</p>
<p>If the NLWeb standard is updated, you can update your Worker to stay compatible and receive the latest updates.</p>
<p>The simplest way to apply changes or updates is to redeploy the Worker template:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/nlweb-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<ol>
<li>Use the <strong>Deploy to Cloudflare</strong> button from above to deploy the Worker template to your Cloudflare account.</li>
<li>Enter the name of your AI Search in the <code>RAG_ID</code> environment variable field.</li>
<li>Click <strong>Deploy</strong>.</li>
<li>Select the <strong>GitHub/GitLab</strong> icon on the Workers Dashboard.</li>
<li>Clone the repository that is created for your Worker.</li>
<li>Make your modifications, then commit and push changes to the repository to update your Worker.</li>
</ol>
<p>Now you can use this Worker as the new NLWeb endpoint for your website.</p>
