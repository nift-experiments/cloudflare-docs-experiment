<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 9, 2025</time><h2 id="post-title">Deploy static sites to Workers without a configuration file</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Deploying static site to Workers is now easier. When you run <code>wrangler deploy [directory]</code> or <code>wrangler deploy --assets [directory]</code> without an existing <a href="/workers/wrangler/configuration/">configuration file</a>, <a href="/workers/wrangler/">Wrangler CLI</a> now guides you through the deployment process with interactive prompts.</p>
<h4 id="before-and-after">Before and after</h4>
<p><strong>Before:</strong> Required remembering multiple flags and parameters</p>
<pre><code class="language-bash">wrangler deploy --assets ./dist --compatibility-date 2025-09-09 --name my-project&#10;</code></pre>
<p><strong>After:</strong> Simple directory deployment with guided setup</p>
<pre><code class="language-bash">wrangler deploy dist&#10;&#35; Interactive prompts handle the rest as shown in the example flow below&#10;</code></pre>
<h4 id="what-s-new">What's new</h4>
<p><strong>Interactive prompts for missing configuration:</strong></p>
<ul>
<li>Wrangler detects when you're trying to deploy a directory of static assets</li>
<li>Prompts you to confirm the deployment type</li>
<li>Asks for a project name (with smart defaults)</li>
<li>Automatically sets the compatibility date to today</li>
</ul>
<p><strong>Automatic configuration generation:</strong></p>
<ul>
<li>Creates a <code>wrangler.jsonc</code> file with your deployment settings</li>
<li>Stores your choices for future deployments</li>
<li>Eliminates the need to remember complex command-line flags</li>
</ul>
<h4 id="example-workflow">Example workflow</h4>
<pre><code class="language-bash">&#35; Deploy your built static site&#10;wrangler deploy dist&#10;&#10;&#35; Wrangler will prompt:&#10;✔ It looks like you are trying to deploy a directory of static assets only. Is this correct? … yes&#10;✔ What do you want to name your project? … my-astro-site&#10;&#10;&#35; Automatically generates a wrangler.jsonc file and adds it to your project:&#10;{&#10;  &quot;name&quot;: &quot;my-astro-site&quot;,&#10;  &quot;compatibility_date&quot;: &quot;2025-09-09&quot;,&#10;  &quot;assets&quot;: {&#10;    &quot;directory&quot;: &quot;dist&quot;&#10;  }&#10;}&#10;&#10;&#35; Next time you run wrangler deploy, this will use the configuration in your newly generated wrangler.jsonc file&#10;wrangler deploy&#10;</code></pre>
<h4 id="requirements">Requirements</h4>
<ul>
<li>You must use Wrangler version 4.24.4 or later in order to use this feature</li>
</ul>
</div></article></div>
