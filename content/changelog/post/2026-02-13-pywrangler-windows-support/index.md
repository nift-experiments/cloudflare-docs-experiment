<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2026</time><h2 id="post-title">Better Windows support for Python Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler">Pywrangler</a>, the CLI tool for managing Python Workers and packages,
now supports Windows, allowing you to develop and deploy Python Workers from Windows environments.
Previously, Pywrangler was only available on macOS and Linux.</p>
<p>You can install and use Pywrangler on Windows the same way you would on other platforms.
<a href="/workers/languages/python/packages/">Specify your Worker's Python dependencies</a> in your <code>pyproject.toml</code> file,
then use the following commands to develop and deploy:</p>
<pre><code class="language-bash">uvx --from workers-py pywrangler dev&#10;uvx --from workers-py pywrangler deploy&#10;</code></pre>
<p>All existing Pywrangler functionality, including package management, local development, and deployment, works on Windows without any additional configuration.</p>
<h4 id="requirements">Requirements</h4>
<p>This feature requires the following minimum versions:</p>
<ul>
<li><code>wrangler</code> &gt;= 4.64.0</li>
<li><code>workers-py</code> &gt;= 1.72.0</li>
<li><code>uv</code> &gt;= 0.29.8</li>
</ul>
<p>To upgrade <code>workers-py</code> (which includes Pywrangler) in your project, run:</p>
<pre><code class="language-bash">uv tool upgrade workers-py&#10;</code></pre>
<p>To upgrade <code>wrangler</code>, run:</p>
<pre><code class="language-bash">npm install -g wrangler@latest&#10;</code></pre>
<p>To upgrade <code>uv</code>, run:</p>
<pre><code class="language-bash">uv self update&#10;</code></pre>
<p>To get started with Python Workers on Windows, refer to the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler.</p>
</div></article></div>
