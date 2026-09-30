---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/environments/
  description: Use environments to create different configurations for the same Worker application.
  full_title: Environments · Cloudflare Workers docs
  head_html: <title>Environments · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use environments to create different configurations for the same Worker application."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/environments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/environments/index.md"><meta property="og:title" content="Environments · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use environments to create different configurations for the same Worker application."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/environments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/environments/#page","headline":"Environments \u00b7 Cloudflare Workers docs","description":"Use environments to create different configurations for the same Worker application.","url":"https://developers.cloudflare.com/workers/wrangler/environments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/environments/
  schema: 1
---
<p>Wrangler allows you to use environments to create different configurations for the same Worker application. Environments are configured in the Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>When you create an environment, Cloudflare effectively creates a new Worker with the name <code>&lt;top-level-name&gt;-&lt;environment-name&gt;</code>. For example, a Worker project named <code>my-worker</code> with an environment <code>dev</code> would deploy as a Worker named <code>my-worker-dev</code>.</p>
<p>Review the following environments flow:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15922.md")
</div>
<h2 id="non-inheritable-keys-and-environments">Non-inheritable keys and environments</h2>
<p><a href="/workers/wrangler/configuration/#non-inheritable-keys">Non-inheritable keys</a> are configurable at the top-level, but cannot be inherited by environments and must be specified for each environment.</p>
<p>For example, <a href="/workers/runtime-apis/bindings/">bindings</a> and <a href="/workers/configuration/environment-variables/">environment variables</a> are non-inheritable, and must be specified per <a href="/workers/wrangler/environments/">environment</a> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>Review the following example Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15923.md")
</div>
<h3 id="service-bindings">Service bindings</h3>
<p>To use a <a href="/workers/wrangler/configuration/#service-bindings">service binding</a> that targets a Worker in a specific environment, you need to append the environment name to the target Worker name in the <code>service</code> field. This should be in the format <code>&lt;worker-name&gt;-&lt;environment-name&gt;</code>.
In the example below, we have two Workers, both with a <code>staging</code> environment. <code>worker-b</code> has a service binding to <code>worker-a</code>. Note how the <code>service</code> field in the <code>staging</code> environment points to <code>worker-a-staging</code>, whereas the top-level service binding points to <code>worker-a</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15924.md")
</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15925.md")
</div>
<h3 id="secrets-for-production">Secrets for production</h3>
<p>You may assign environment-specific <a href="/workers/configuration/secrets/">secrets</a> by running the command <a href="/workers/wrangler/commands/general/#secret-put"><code>wrangler secret put &lt;KEY&gt; -env</code></a>. You can also create <code>dotenv</code> type files named <code>.dev.vars.&lt;environment-name&gt;</code>.</p>
<p>Like other environment variables, secrets are <a href="/workers/wrangler/configuration/#non-inheritable-keys">non-inheritable</a> and must be defined per environment.</p>
<h3 id="secrets-in-local-development">Secrets in local development</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15918.md")
</aside>
<p>Put secrets for use in local development in either a <code>.dev.vars</code> file or a <code>.env</code> file, in the same directory as the Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15917.md")
</aside>
<aside class="nb-aside info">
@markup("md", "content/.markup/bodies/15916.md")
</aside>
<p>These files should be formatted using the <a href="https://hexdocs.pm/dotenvy/dotenv-file-format.html">dotenv</a> syntax. For example:</p>
<pre tabindex="0"><code class="language-bash">SECRET_KEY=&quot;value&quot;&#10;API_TOKEN=&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9&quot;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-commit-secrets-to-git">Do not commit secrets to git</h3>
@markup("md", "content/.markup/bodies/15915.md")
</aside>
<p>To set different secrets for each Cloudflare environment, create files named <code>.dev.vars.&lt;environment-name&gt;</code> or <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you select a Cloudflare environment in your local development, the corresponding environment-specific file will be loaded ahead of the generic <code>.dev.vars</code> (or <code>.env</code>) file.</p>
<ul>
<li>When using <code>.dev.vars.&lt;environment-name&gt;</code> files, all secrets must be defined per environment. If <code>.dev.vars.&lt;environment-name&gt;</code> exists then only this will be loaded; the <code>.dev.vars</code> file will not be loaded.</li>
<li>In contrast, all matching <code>.env</code> files are loaded and the values are merged. For each variable, the value from the most specific file is used, with the following precedence:
<ul>
<li><code>.env.&lt;environment-name&gt;.local</code> (most specific)</li>
<li><code>.env.local</code></li>
<li><code>.env.&lt;environment-name&gt;</code></li>
<li><code>.env</code> (least specific)</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="controlling-env-handling">Controlling `.env` handling</h3>
@markup("md", "content/.markup/bodies/15914.md")
</aside>
<hr />
<h2 id="examples">Examples</h2>
<h3 id="staging-and-production-environments">Staging and production environments</h3>
<p>The following Wrangler file adds two environments, <code>[env.staging]</code> and <code>[env.production]</code>, to the Wrangler file. If you are deploying to a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a> or <a href="/workers/configuration/routing/routes/">route</a>, you must provide a <a href="/workers/wrangler/configuration/"><code>route</code> or <code>routes</code> key</a> for each environment.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15926.md")
</div>
<p>You can pass the name of the environment via the <code>--env</code> flag to run commands in a specific environment.</p>
<p>With this configuration, Wrangler will behave in the following manner:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Uploaded my-worker&#10;Published my-worker&#10;  dev.example.com/*&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy --env staging&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Uploaded my-worker-staging&#10;Published my-worker-staging&#10;  staging.example.com/*&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy --env production&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Uploaded my-worker-production&#10;Published my-worker-production&#10;  example.com/*&#10;</code></pre>
<p>Any defined <a href="/workers/configuration/environment-variables/">environment variables</a> (the <a href="/workers/wrangler/configuration/"><code>vars</code></a> key) are available via the <a href="/workers/runtime-apis/bindings/#accessing-bindings"><code>env</code> object</a> in your Worker.</p>
<p>With this configuration, the <code>env.ENVIRONMENT</code> variable can be used to call specific code depending on the given environment:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		if (env.ENVIRONMENT === &quot;staging&quot;) {&#10;			// staging-specific code&#10;		} else if (env.ENVIRONMENT === &quot;production&quot;) {&#10;			// production-specific code&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h3 id="staging-environment-with-workers-dev">Staging environment with *.workers.dev</h3>
<p>To deploy your code to your <code>*.workers.dev</code> subdomain, include <code>workers_dev = true</code> in the desired environment. Your Wrangler file may look like this:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15927.md")
</div>
<p>With this configuration, Wrangler will behave in the following manner:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Uploaded my-worker&#10;Published my-worker&#10;  example.com/*&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy --env staging&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Uploaded my-worker&#10;Published my-worker&#10;  https://my-worker-staging.&lt;YOUR_SUBDOMAIN&gt;.workers.dev&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15913.md")
</aside>
