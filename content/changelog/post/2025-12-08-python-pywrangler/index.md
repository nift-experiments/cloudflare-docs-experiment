<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 8, 2025</time><h2 id="post-title">Easy Python package management with Pywrangler</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We are introducing a brand new tool called Pywrangler, which simplifies package management in Python Workers by
automatically installing Workers-compatible Python packages into your project.</p>
<p>With Pywrangler, you specify your Worker's Python dependencies in your <code>pyproject.toml</code> file:</p>
<pre><code class="language-toml">[project]&#10;name = &quot;python-beautifulsoup-worker&quot;&#10;version = &quot;0.1.0&quot;&#10;description = &quot;A simple Worker using beautifulsoup4&quot;&#10;requires-python = &quot;&gt;=3.12&quot;&#10;dependencies = [&#10;    &quot;beautifulsoup4&quot;&#10;]&#10;&#10;[dependency-groups]&#10;dev = [&#10;  &quot;workers-py&quot;,&#10;  &quot;workers-runtime-sdk&quot;&#10;]&#10;</code></pre>
<p>You can then develop and deploy your Worker using the following commands:</p>
<pre><code class="language-bash">uv run pywrangler dev&#10;uv run pywrangler deploy&#10;</code></pre>
<p>Pywrangler automatically downloads and vendors the necessary packages for your Worker, and these packages are bundled with the Worker when you deploy.</p>
<p>Consult the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler and Python package management in Workers.</p>
</div></article></div>
