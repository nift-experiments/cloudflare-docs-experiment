---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/secrets/
  description: Store sensitive information, like API keys and auth tokens, in your Worker.
  full_title: Secrets · Cloudflare Workers docs
  head_html: <title>Secrets · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Store sensitive information, like API keys and auth tokens, in your Worker."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/secrets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/secrets/index.md"><meta property="og:title" content="Secrets · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store sensitive information, like API keys and auth tokens, in your Worker."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/secrets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/configuration/secrets/#page","headline":"Secrets \u00b7 Cloudflare Workers docs","description":"Store sensitive information, like API keys and auth tokens, in your Worker.","url":"https://developers.cloudflare.com/workers/configuration/secrets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/secrets/
  schema: 1
---
<h2 id="background">Background</h2>
<p>Secrets are a type of binding that allow you to attach encrypted text values to your Worker. Secrets are used for storing sensitive information like API keys and auth tokens.</p>
<p>You can access secrets in your Worker code through:</p>
<ul>
<li>The <a href="/workers/runtime-apis/handlers/fetch/#parameters"><code>env</code> parameter</a> passed to your Worker's <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch</code> event handler</a>.</li>
<li>Importing <code>env</code> from <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global"><code>cloudflare:workers</code></a> to access secrets from anywhere in your code.</li>
<li><a href="/workers/configuration/environment-variables"><code>process.env</code></a> in Workers that have <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> enabled.</li>
</ul>
<h2 id="access-your-secrets-with-workers">Access your secrets with Workers</h2>
<p>Secrets can be accessed from Workers as you would any other <a href="/workers/configuration/environment-variables/">environment variables</a>. For instance, given a <code>DB_CONNECTION_STRING</code> secret, you can access it in your Worker code through the <code>env</code> parameter:</p>
<pre tabindex="0"><code class="language-js">import postgres from &quot;postgres&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		const sql = postgres(env.DB_CONNECTION_STRING);&#10;&#10;		const result = await sql`SELECT * FROM products;`;&#10;&#10;		return new Response(JSON.stringify(result), {&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>You can also import <code>env</code> from <code>cloudflare:workers</code> to access secrets from anywhere in your code, including outside of request handlers:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16602.md")
</div>
<p>For more details on accessing <code>env</code> globally, refer to <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">Importing <code>env</code> as a global</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="secrets-store-beta">Secrets Store (beta)</h3>
@markup("md", "content/.markup/bodies/16601.md")
</aside>
<h2 id="local-development-with-secrets">Local Development with Secrets</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16600.md")
</aside>
<p>Put secrets for use in local development in either a <code>.dev.vars</code> file or a <code>.env</code> file, in the same directory as the Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16599.md")
</aside>
<aside class="nb-aside info">
@markup("md", "content/.markup/bodies/16598.md")
</aside>
<p>These files should be formatted using the <a href="https://hexdocs.pm/dotenvy/dotenv-file-format.html">dotenv</a> syntax. For example:</p>
<pre tabindex="0"><code class="language-bash">SECRET_KEY=&quot;value&quot;&#10;API_TOKEN=&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9&quot;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-commit-secrets-to-git">Do not commit secrets to git</h3>
@markup("md", "content/.markup/bodies/16597.md")
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
@markup("md", "content/.markup/bodies/16596.md")
</aside>
<h2 id="secrets-on-deployed-workers">Secrets on deployed Workers</h2>
<h3 id="validate-secrets-before-deploy">Validate secrets before deploy</h3>
<p>You can declare the secret names your Worker requires using the <a href="/workers/wrangler/configuration/#secrets-configuration-property"><code>secrets</code> configuration property</a> in your Wrangler configuration. When defined, <code>wrangler deploy</code> and <code>wrangler versions upload</code> will fail with a clear error if any required secrets are not configured on the Worker.</p>
<h3 id="adding-secrets-to-your-project">Adding secrets to your project</h3>
<h4 id="via-wrangler">Via Wrangler</h4>
<p>Secrets can be added through <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret put</code></a> or <a href="/workers/wrangler/commands/general/#versions-secret-put"><code>wrangler versions secret put</code></a> commands.</p>
<p><code>wrangler secret put</code> creates a new version of the Worker and deploys it immediately.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put &lt;KEY&gt;&#10;</code></pre>
<p>If using <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a>, instead use the <code>wrangler versions secret put</code> command. This will only create a new version of the Worker, that can then be deploying using <a href="/workers/wrangler/commands/general/#versions-deploy"><code>wrangler versions deploy</code></a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16595.md")
</aside>
<pre tabindex="0"><code class="language-sh">npx wrangler versions secret put &lt;KEY&gt;&#10;</code></pre>
<h4 id="via-the-dashboard">Via the dashboard</h4>
<p>To add a secret via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker &gt; <strong>Settings</strong>.</li>
<li>Under <strong>Variables and Secrets</strong>, select <strong>Add</strong>.</li>
<li>Select the type <strong>Secret</strong>, input a <strong>Variable name</strong>, and input its <strong>Value</strong>. This secret will be made available to your Worker but the value will be hidden in Wrangler and the dashboard.</li>
<li>(Optional) To add more secrets, select <strong>Add variable</strong>.</li>
<li>Select <strong>Deploy</strong> to implement your changes.</li>
</ol>
<h4 id="upload-secrets-alongside-code">Upload secrets alongside code</h4>
<p>You can upload secrets at the same time as your Worker code using the <code>--secrets-file</code> flag on <a href="/workers/wrangler/commands/workers/#deploy"><code>wrangler deploy</code></a> or <a href="/workers/wrangler/commands/workers/#versions-upload"><code>wrangler versions upload</code></a>. This accepts a path to a JSON or <code>.env</code> file — the same formats accepted by <a href="/workers/wrangler/commands/workers/#secret-bulk"><code>wrangler secret bulk</code></a>. You can upload up to 100 secrets per bulk request for a single version.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy --secrets-file .env.production&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler versions upload --secrets-file secrets.json&#10;</code></pre>
<p>Secrets not included in the file are preserved from the previous version. This is useful in CI/CD pipelines where you want to deploy code and update secrets in a single operation.</p>
<h3 id="delete-secrets-from-your-project">Delete secrets from your project</h3>
<h4 id="via-wrangler-1">Via Wrangler</h4>
<p>Secrets can be deleted through <a href="/workers/wrangler/commands/general/#secret-delete"><code>wrangler secret delete</code></a> or <a href="/workers/wrangler/commands/general/#versions-secret-delete"><code>wrangler versions secret delete</code></a> commands.</p>
<p><code>wrangler secret delete</code> creates a new version of the Worker and deploys it immediately.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret delete &lt;KEY&gt;&#10;</code></pre>
<p>If using <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a>, instead use the <code>wrangler versions secret delete</code> command. This will only create a new version of the Worker, that can then be deploying using <a href="/workers/wrangler/commands/general/#versions-deploy"><code>wrangler versions deploy</code></a>.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler versions secret delete &lt;KEY&gt;&#10;</code></pre>
<h4 id="via-the-dashboard-1">Via the dashboard</h4>
<p>To delete a secret from your Worker project via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker &gt; <strong>Settings</strong>.</li>
<li>Under <strong>Variables and Secrets</strong>, select <strong>Edit</strong>.</li>
<li>In the <strong>Edit</strong> drawer, select <strong>X</strong> next to the secret you want to delete.</li>
<li>Select <strong>Deploy</strong> to implement your changes.</li>
<li>(Optional) Instead of using the edit drawer, you can click the delete icon next to the secret.</li>
</ol>
<h2 id="compare-secrets-and-environment-variables">Compare secrets and environment variables</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-secrets-for-sensitive-information">Use secrets for sensitive information</h3>
@markup("md", "content/.markup/bodies/16594.md")
</aside>
<p><a href="/workers/configuration/secrets/">Secrets</a> are <a href="/workers/configuration/environment-variables/">environment variables</a>. The difference is secret values are not visible within Wrangler or Cloudflare dashboard after you define them. This means that sensitive data, including passwords or API tokens, should always be encrypted to prevent data leaks. To your Worker, there is no difference between an environment variable and a secret. The secret's value is passed through as defined.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/wrangler/commands/general/#secret">Wrangler secret commands</a> - Review the Wrangler commands to create, delete and list secrets.</li>
<li><a href="/workers/wrangler/configuration/#secrets-configuration-property"><code>secrets</code> configuration property</a> - Declare required secret names in your Wrangler configuration. Used for validation during local development and deploy, and as the source of truth for type generation.</li>
<li><a href="/secrets-store/">Cloudflare Secrets Store</a> - Encrypt and store sensitive information as secrets that are securely reusable across your account.</li>
</ul>
