<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 2, 2026</time><h2 id="post-title">Python Workers now support WSGI web frameworks like Django and Flask</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Python web frameworks following the <a href="https://peps.python.org/pep-3333/">Web Server Gateway Interface (WSGI)</a> or <a href="https://asgi.readthedocs.io/">Asynchronous Server Gateway Interface (ASGI)</a> specification can now be used in Python Workers.</p>
<h4 id="using-web-frameworks-with-python-workers">Using web frameworks with Python Workers</h4>
<p>Based on the web framework you are using, you can use either <code>wsgi</code> or <code>asgi</code> from the <code>workers</code> module.</p>
<h4 id="wsgi-frameworks">WSGI frameworks</h4>
<p>For WSGI frameworks like Django or Flask:</p>
<pre><code class="language-python">from workers import wsgi&#10;&#10;from django.core.wsgi import get_wsgi_application&#10;&#10;app = get_wsgi_application()&#10;Default = wsgi.entrypoint(app)&#10;</code></pre>
<p>The <code>wsgi.entrypoint</code> is equivalent to creating a <code>WorkerEntrypoint</code> class and using the <code>wsgi.fetch</code> method. If you want more control over the <code>WorkerEntrypoint</code> class, you can do so:</p>
<pre><code class="language-python">from workers import wsgi, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return await wsgi.fetch(app, request, self.env)&#10;</code></pre>
<h4 id="asgi-frameworks">ASGI frameworks</h4>
<p>For ASGI frameworks like FastAPI or Starlette:</p>
<pre><code class="language-python">from workers import asgi&#10;&#10;from fastapi import FastAPI&#10;&#10;app = FastAPI()&#10;Default = asgi.entrypoint(app)&#10;</code></pre>
<p>For more information about using individual web frameworks, refer to the <a href="/workers/languages/python/packages/">packages documentation in Python Workers</a>.</p>
</div></article></div>
