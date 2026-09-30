<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16800.md")
</aside>
<p>This guide shows how to quickly start a new Workers Sites project from scratch.</p>
<h2 id="getting-started">Getting started</h2>
<ol>
<li>
<p>Ensure you have the latest version of <a href="https://git-scm.com/downloads">git</a> and <a href="https://nodejs.org/en/download/">Node.js</a> installed.</p>
</li>
<li>
<p>In your terminal, clone the <code>worker-sites-template</code> starter repository.
The following example creates a project called <code>my-site</code>:</p>
</li>
</ol>
<pre><code class="language-sh">git clone --depth=1 --branch=wrangler2 https://github.com/cloudflare/worker-sites-template my-site&#10;</code></pre>
<ol start="3">
<li>
<p>Run <code>npm install</code> to install all dependencies.</p>
</li>
<li>
<p>You can preview your site by running the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> command:</p>
</li>
</ol>
<pre><code class="language-sh">wrangler dev&#10;</code></pre>
<ol start="5">
<li>Deploy your site to Cloudflare:</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h2 id="project-layout">Project layout</h2>
<p>The template project contains the following files and directories:</p>
<ul>
<li><code>public</code>: The static assets for your project. By default it contains an <code>index.html</code> and a <code>favicon.ico</code>.</li>
<li><code>src</code>: The Worker configured for serving your assets. You do not need to edit this but if you want to see how it works or add more functionality to your Worker, you can edit <code>src/index.ts</code>.</li>
<li><code>wrangler.jsonc</code>: The file containing project configuration.
The <code>bucket</code> property tells Wrangler where to find the static assets (e.g. <code>site = { bucket = &quot;./public&quot; }</code>).</li>
<li><code>package.json</code>/<code>package-lock.json</code>: define the required Node.js dependencies.</li>
</ul>
<h2 id="customize-the-wrangler-jsonc-file">Customize the <code>wrangler.jsonc</code> file:</h2>
<ul>
<li>Change the <code>name</code> property to the name of your project:</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16801.md")
</div>
<ul>
<li>Consider updating<code>compatibility_date</code> to today's date to get access to the most recent Workers features:</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16802.md")
</div>
<ul>
<li>Deploy your site to a <a href="/workers/configuration/routing/custom-domains/">custom domain</a> that you own and have already attached as a Cloudflare zone:</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16803.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16799.md")
</aside>
<p>Learn more about <a href="/workers/wrangler/configuration/">configuring your project</a>.</p>
