---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/bindings/
  description: Worker Bindings that allow for interaction with other Cloudflare Resources.
  full_title: Bindings (env) · Cloudflare Workers docs
  head_html: <title>Bindings (env) · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Worker Bindings that allow for interaction with other Cloudflare Resources."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/index.md"><meta property="og:title" content="Bindings (env) · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Worker Bindings that allow for interaction with other Cloudflare Resources."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="Bindings"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/bindings/#page","headline":"Bindings (env) \u00b7 Cloudflare Workers docs","description":"Worker Bindings that allow for interaction with other Cloudflare Resources.","url":"https://developers.cloudflare.com/workers/runtime-apis/bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Bindings"]}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/bindings/
  schema: 1
---
<p>Bindings allow your Worker to interact with resources on the Cloudflare Developer Platform. Bindings provide better performance and less restrictions when accessing resources from Workers than the <a href="/api/">REST APIs</a> which are intended for non-Workers applications.</p>
<p>During local development, bindings connect to locally simulated resources by default. You can also configure them to connect to real, production resources using <a href="/workers/local-development/#remote-bindings">remote bindings</a>.</p>
<p>The following bindings are available today:</p>
<ul class="directory-listing"><li><a href="/workers-ai/get-started/workers-wrangler/#2-connect-your-worker-to-workers-ai">AI</a></li><li><a href="/analytics/analytics-engine/">Analytics Engine</a></li><li><a href="/workers/static-assets/binding/">Assets</a></li><li><a href="/browser-run/">Browser Run</a></li><li><a href="/d1/worker-api/">D1</a></li><li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dispatcher (Workers for Platforms)</a></li><li><a href="/durable-objects/api/">Durable Objects</a></li><li><a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loaders</a></li><li><a href="/workers/configuration/environment-variables/">Environment Variables</a></li><li><a href="/hyperdrive/">Hyperdrive</a></li><li><a href="/images/optimization/binding/">Images</a></li><li><a href="/kv/api/">KV</a></li><li><a href="/stream/transform-videos/bindings/">Media Transformations</a></li><li><a href="/workers/runtime-apis/bindings/mtls/">mTLS</a></li><li><a href="/queues/configuration/javascript-apis/">Queues</a></li><li><a href="/r2/api/workers/workers-api-reference/">R2</a></li><li><a href="/workers/runtime-apis/bindings/rate-limit/">Rate Limiting</a></li><li><a href="/workers/configuration/secrets/">Secrets</a></li><li><a href="/secrets-store/integrations/workers/">Secrets Store</a></li><li><a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a></li><li><a href="/stream/manage-video-library/bindings/">Stream</a></li><li><a href="/vectorize/reference/client-api/">Vectorize</a></li><li><a href="/workers/runtime-apis/bindings/version-metadata/">Version metadata</a></li><li><a href="/workflows/">Workflows</a></li></ul>
<h2 id="what-is-a-binding">What is a binding?</h2>
<p>When you declare a binding on your Worker, you grant it a specific capability, such as being able to read and write files to an <a href="/r2/">R2</a> bucket. For example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17203.md")
</div>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17206.md")
</div></div>
<p>You can think of a binding as a permission and an API in one piece. With bindings, you never have to add secret keys or tokens to your Worker in order to access resources on your Cloudflare account — the permission is embedded within the API itself. The underlying secret is never exposed to your Worker's code, and therefore can't be accidentally leaked.</p>
<h2 id="making-changes-to-bindings">Making changes to bindings</h2>
<p>When you deploy a change to your Worker, and only change its bindings (i.e. you don't change the Worker's code), Cloudflare may reuse existing isolates that are already running your Worker. This improves performance — you can change an environment variable or other binding without unnecessarily reloading your code.</p>
<p>As a result, you must be careful when &quot;polluting&quot; global scope with derivatives of your bindings. Anything you create there might continue to exist despite making changes to any underlying bindings. Consider an external client instance which uses a secret API key accessed from <code>env</code>: if you put this client instance in global scope and then make changes to the secret, a client instance using the original value might continue to exist. The correct approach would be to create a new client instance for each request.</p>
<p>The following is a good approach:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	fetch(request, env) {&#10;		let client = new Client(env.MY_SECRET); // `client` is guaranteed to be up-to-date with the latest value of `env.MY_SECRET` since a new instance is constructed with every incoming request&#10;&#10;		// ... do things with `client`&#10;	},&#10;};&#10;</code></pre>
<p>Compared to this alternative, which might have surprising and unwanted behavior:</p>
<pre tabindex="0"><code class="language-ts">let client = undefined;&#10;&#10;export default {&#10;	fetch(request, env) {&#10;		client ??= new Client(env.MY_SECRET); // `client` here might not be updated when `env.MY_SECRET` changes, since it may already exist in global scope&#10;&#10;		// ... do things with `client`&#10;	},&#10;};&#10;</code></pre>
<p>If you have more advanced needs, explore the <a href="/workers/runtime-apis/nodejs/asynclocalstorage/">AsyncLocalStorage API</a>, which provides a mechanism for exposing values down to child execution handlers.</p>
<h2 id="how-to-access-env">How to access <code>env</code></h2>
<p>Bindings are located on the <code>env</code> object, which can be accessed in several ways:</p>
<ul>
<li>It is an argument to entrypoint handlers such as <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a>:</li>
</ul>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		return new Response(`Hi, ${env.NAME}`);&#10;	},&#10;};&#10;</code></pre>
<ul>
<li>It is a class property on <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#bindings-env">WorkerEntrypoint</a>,
<a href="/durable-objects/">DurableObject</a>, and <a href="/workflows/">Workflow</a>:</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17209.md")
</div></div>
<ul>
<li>It can be imported from <code>cloudflare:workers</code>:</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17212.md")
</div></div>
<h3 id="importing-env-as-a-global">Importing <code>env</code> as a global</h3>
<p>Importing <code>env</code> from <code>cloudflare:workers</code> is useful when you need to access a binding
such as <a href="/workers/configuration/secrets/">secrets</a> or <a href="/workers/configuration/environment-variables/">environment variables</a>
in top-level global scope. For example, to initialize an API client:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17215.md")
</div></div>
<p>Workers do not allow I/O from outside a request context. This means that even
though <code>env</code> is accessible from the top-level scope, you will not be able to access
every binding's methods.</p>
<p>For instance, environment variables and secrets are accessible, and you are able to
call <code>env.NAMESPACE.get</code> to get a <a href="/durable-objects/api/stub/">Durable Object stub</a> in the
top-level context. However, calling methods on the Durable Object stub, making <a href="/kv/api/">calls to a KV store</a>,
and <a href="/workers/runtime-apis/bindings/service-bindings">calling to other Workers</a> will not work.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17218.md")
</div></div>
<p>Additionally, importing <code>env</code> from <code>cloudflare:workers</code> lets you avoid passing <code>env</code>
as an argument through many function calls if you need to access a binding from a deeply-nested
function. This can be helpful in a complex codebase.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17221.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17202.md")
</aside>
<h3 id="overriding-env-values">Overriding <code>env</code> values</h3>
<p>The <code>withEnv</code> function provides a mechanism for overriding values of <code>env</code>.</p>
<p>Imagine a user has defined the <a href="/workers/configuration/environment-variables/">environment variable</a>
&quot;NAME&quot; to be &quot;Alice&quot; in their Wrangler configuration file and deployed a Worker. By default, logging
<code>env.NAME</code> would print &quot;Alice&quot;. Using the <code>withEnv</code> function, you can override the value of
&quot;NAME&quot;.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17224.md")
</div></div>
<p>This can be useful when testing code that relies on an imported <code>env</code> object.</p>
