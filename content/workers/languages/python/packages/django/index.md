---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/python/packages/django/
  description: Run Django on Python Workers
  full_title: Django · Cloudflare Workers docs
  head_html: <title>Django · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Run Django on Python Workers"><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/python/packages/django/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/python/packages/django/index.md"><meta property="og:title" content="Django · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run Django on Python Workers"><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/python/packages/django/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/languages/python/packages/django/#page","headline":"Django \u00b7 Cloudflare Workers docs","description":"Run Django on Python Workers","url":"https://developers.cloudflare.com/workers/languages/python/packages/django/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/python/packages/django/
  schema: 1
---
<p><a href="https://www.djangoproject.com/">Django</a> is supported in Python Workers.</p>
<p>Django applications use protocols called the <a href="https://peps.python.org/pep-3333/">Web Server Gateway Interface (WSGI)</a>
or <a href="https://asgi.readthedocs.io/en/latest/">Asynchronous Server Gateway Interface (ASGI)</a>.</p>
<p>This means that Django never reads from or writes to a socket itself. A WSGI/ASGI application expects to be hooked up to a
WSGI/ASGI server, such as <a href="https://uvicorn.dev/">uvicorn</a>.
The WSGI/ASGI server handles all of the raw sockets on the application’s behalf.</p>
<p>Python Workers provide adaptors for both WSGI and ASGI,
so you can choose any based on whether your Django application deploys to WSGI or ASGI.</p>
<h2 id="quick-start">Quick start</h2>
<p>To get started with Django in Python Workers, follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17015.md")
</div>
<h2 id="choose-between-asgi-and-wsgi">Choose between ASGI and WSGI</h2>
<p>Your Django application needs to be served using either ASGI or WSGI.
While Python workers is optimized for ASGI, you can still use WSGI which is compatible with Django.</p>
<h3 id="serve-a-wsgi-application">Serve a WSGI application</h3>
<p>Build the application object with <code>get_wsgi_application()</code> and pass it to <code>workers.wsgi.fetch</code>:</p>
<pre tabindex="0"><code class="language-python">import os&#10;&#10;from django.core.wsgi import get_wsgi_application&#10;from workers import wsgi&#10;&#10;&#35; your Django settings module&#10;os.environ.setdefault(&quot;DJANGO_SETTINGS_MODULE&quot;, &quot;app.settings&quot;)&#10;&#10;app = get_wsgi_application()&#10;&#10;Default = wsgi.entrypoint(app)&#10;</code></pre>
<p><code>wsgi.fetch</code> takes the application object, the incoming request, and the environment.
It exposes your bindings to the application through <code>scope[&quot;env&quot;]</code>.</p>
<h3 id="serve-an-asgi-application">Serve an ASGI application</h3>
<p>Build the application object with <code>get_asgi_application()</code> and pass it to <code>workers.asgi.fetch</code>:</p>
<pre tabindex="0"><code class="language-python">import os&#10;&#10;from django.core.asgi import get_asgi_application&#10;from workers import asgi&#10;&#10;&#35; your Django settings module&#10;os.environ.setdefault(&quot;DJANGO_SETTINGS_MODULE&quot;, &quot;app.settings&quot;)&#10;&#10;app = get_asgi_application()&#10;&#10;Default = asgi.entrypoint(app)&#10;</code></pre>
<p><code>asgi.fetch</code> takes the application object, the incoming request, and the environment.
It exposes your bindings to the application through <code>scope[&quot;env&quot;]</code>.</p>
<h2 id="configure-django-settings">Configure Django settings</h2>
<h3 id="pass-secrets">Pass secrets</h3>
<p>If you need a secret (like <code>SECRET_KEY</code>) in your Django settings, you can read it from a <a href="/workers/configuration/secrets/">Worker secret</a>:</p>
<pre tabindex="0"><code class="language-python">from workers import env&#10;&#10;SECRET_KEY = env.DJANGO_SECRET_KEY&#10;</code></pre>
<p>Create the secret with <code>uv run pywrangler secret put DJANGO_SECRET_KEY</code>.</p>
<h2 id="use-cloudflare-storage-as-django-backends">Use Cloudflare storage as Django backends</h2>
<p>You can use Cloudflare <a href="/d1/">D1</a> and <a href="/durable-objects/">Durable Objects</a> as Django database backends.
To use them, you need to install the <a href="https://github.com/cloudflare/workers-py/tree/main/packages/django-cf"><code>django-cf</code></a> package.</p>
<p>Add <code>django-cf</code> to your dependencies:</p>
<pre tabindex="0"><code class="language-toml">[project]&#10;dependencies = [&#10;    &quot;django&quot;,&#10;    &quot;django-cf&quot;,&#10;]&#10;</code></pre>
<h3 id="database-backends">Database backends</h3>
<p><code>django-cf</code> provides two SQLite-compatible backends using Cloudflare's D1 and Durable Objects.
Both drive the synchronous Django ORM, so serve your application through the WSGI path when you use them.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="transaction-support">Transaction support</h3>
@markup("md", "content/.markup/bodies/17014.md")
</aside>
<h4 id="d1-backend">D1 backend</h4>
<p>To use D1 as a database backend, first setup your D1 database in Wrangler:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17016.md")
</div>
<p>Then, configure the backend in your Django settings:</p>
<pre tabindex="0"><code class="language-python">DATABASES = {&#10;    &quot;default&quot;: {&#10;        &quot;ENGINE&quot;: &quot;django_cf.db.backends.d1&quot;,&#10;        &#35; should match the binding name in your wrangler.jsonc&#10;        &quot;CLOUDFLARE_BINDING&quot;: &quot;DB&quot;,&#10;    }&#10;}&#10;</code></pre>
<p>You are all set. Your Django application now uses D1 as its database backend.</p>
<pre tabindex="0"><code class="language-python">import os&#10;&#10;from django.core.wsgi import get_wsgi_application&#10;from workers import WorkerEntrypoint, wsgi&#10;&#10;&#35; your Django settings module&#10;os.environ.setdefault(&quot;DJANGO_SETTINGS_MODULE&quot;, &quot;app.settings&quot;)&#10;&#10;application = get_wsgi_application()&#10;&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return await wsgi.fetch(application, request, self.env)&#10;</code></pre>
<h4 id="durable-objects-backend">Durable Objects backend</h4>
<p>To use Durable Objects as a database backend, first setup your Durable Objects binding in Wrangler:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17017.md")
</div>
<p>Then, configure the backend in your Django settings:</p>
<pre tabindex="0"><code class="language-python">DATABASES = {&#10;    &quot;default&quot;: {&#10;        &quot;ENGINE&quot;: &quot;django_cf.db.backends.do&quot;,&#10;    }&#10;}&#10;</code></pre>
<p>Then, update your Python worker as follows:</p>
<pre tabindex="0"><code class="language-python">import os&#10;&#10;from django.core.wsgi import get_wsgi_application&#10;from django_cf.db.backends.do.storage import set_storage&#10;from workers import WorkerEntrypoint, DurableObject, wsgi&#10;&#10;&#35; your Django settings module&#10;os.environ.setdefault(&quot;DJANGO_SETTINGS_MODULE&quot;, &quot;app.settings&quot;)&#10;&#10;application = get_wsgi_application()&#10;&#10;&#10;class DjangoDurableObject(DurableObject):&#10;    def __init__(self, ctx, env):&#10;        super().__init__(ctx, env)&#10;&#10;        &#35; Tell Django to use the Durable Object storage&#10;        set_storage(self.ctx.storage.sql)&#10;&#10;    async def fetch(self, request):&#10;        return await wsgi.fetch(application, request, self.env)&#10;&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        id = self.env.DO_STORAGE.idFromName(&quot;my-do-backend&quot;)&#10;        stub = self.env.DO_STORAGE.get(id)&#10;        return await stub.fetch(request)&#10;</code></pre>
<h2 id="more-examples">More examples</h2>
<p>Clone the <code>cloudflare/python-workers-examples</code> repository and run Django examples:</p>
<ul>
<li><a href="https://github.com/cloudflare/python-workers-examples/tree/main/django">django</a></li>
<li><a href="https://github.com/cloudflare/python-workers-examples/tree/main/django-todo-d1">django with D1 backend</a></li>
</ul>
