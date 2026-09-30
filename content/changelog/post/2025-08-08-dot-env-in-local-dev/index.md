<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 8, 2025</time><h2 id="post-title">Wrangler and the Cloudflare Vite plugin support `.env` files in local development</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Now, you can use <code>.env</code> files to provide secrets and override environment variables on the <code>env</code> object during local development with Wrangler and the Cloudflare Vite plugin.</p>
<p>Previously in local development, if you wanted to provide secrets or environment variables during local development, you had to use <code>.dev.vars</code> files.
This is still supported, but you can now also use <code>.env</code> files, which are more familiar to many developers.</p>
<h4 id="using-env-files-in-local-development">Using <code>.env</code> files in local development</h4>
<p>You can create a <code>.env</code> file in your project root to define environment variables that will be used when running <code>wrangler dev</code> or <code>vite dev</code>. The <code>.env</code> file should be formatted like a <code>dotenv</code> file, such as <code>KEY=&quot;VALUE&quot;</code>:</p>
<pre><code class="language-bash">TITLE=&quot;My Worker&quot;&#10;API_TOKEN=&quot;dev-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev</code> or <code>vite dev</code>, the environment variables defined in the <code>.env</code> file will be available in your Worker code via the <code>env</code> object:</p>
<pre><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot;&#10;		const apiToken = env.API_TOKEN; // &quot;dev-token&quot;&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="multiple-environments-with-env-files">Multiple environments with <code>.env</code> files</h4>
<p>If your Worker defines multiple <a href="/workers/wrangler/environments/">environments</a>, you can set different variables for each environment (ex: production or staging) by creating files named <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you use <code>wrangler &lt;command&gt; --env &lt;environment-name&gt;</code> or <code>CLOUDFLARE_ENV=&lt;environment-name&gt; vite dev</code>, the corresponding environment-specific file will also be loaded and merged with the <code>.env</code> file.</p>
<p>For example, if you want to set different environment variables for the <code>staging</code> environment, you can create a file named <code>.env.staging</code>:</p>
<pre><code class="language-bash">API_TOKEN=&quot;staging-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev --env staging</code> or <code>CLOUDFLARE_ENV=staging vite dev</code>, the environment variables from <code>.env.staging</code> will be merged onto those from <code>.env</code>.</p>
<pre><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot; (from `.env`)&#10;		const apiToken = env.API_TOKEN; // &quot;staging-token&quot; (from `.env.staging`, overriding the value from `.env`)&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="find-out-more">Find out more</h4>
<p>For more information on how to use <code>.env</code> files with Wrangler and the Cloudflare Vite plugin, see the following documentation:</p>
<ul>
<li><a href="/workers/local-development/environment-variables">Environment variables and secrets</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler">Wrangler Documentation</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler/vite">Cloudflare Vite Plugin Documentation</a></li>
</ul>
</div></article></div>
