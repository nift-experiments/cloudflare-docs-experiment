---
cp9:
  canonical: https://developers.cloudflare.com/workers/local-development/environment-variables/
  description: Configuring environment variables and secrets for local development
  full_title: Environment variables and secrets · Cloudflare Workers docs
  head_html: <title>Environment variables and secrets · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Configuring environment variables and secrets for local development"><link rel="canonical" href="https://developers.cloudflare.com/workers/local-development/environment-variables/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/local-development/environment-variables/index.md"><meta property="og:title" content="Environment variables and secrets · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configuring environment variables and secrets for local development"><meta property="og:url" content="https://developers.cloudflare.com/workers/local-development/environment-variables/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/local-development/environment-variables/#page","headline":"Environment variables and secrets \u00b7 Cloudflare Workers docs","description":"Configuring environment variables and secrets for local development","url":"https://developers.cloudflare.com/workers/local-development/environment-variables/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/local-development/environment-variables/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16291.md")
</aside>
<p>Put secrets for use in local development in either a <code>.dev.vars</code> file or a <code>.env</code> file, in the same directory as the Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16290.md")
</aside>
<aside class="nb-aside info">
@markup("md", "content/.markup/bodies/16289.md")
</aside>
<p>These files should be formatted using the <a href="https://hexdocs.pm/dotenvy/dotenv-file-format.html">dotenv</a> syntax. For example:</p>
<pre tabindex="0"><code class="language-bash">SECRET_KEY=&quot;value&quot;&#10;API_TOKEN=&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9&quot;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-commit-secrets-to-git">Do not commit secrets to git</h3>
@markup("md", "content/.markup/bodies/16288.md")
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
@markup("md", "content/.markup/bodies/16287.md")
</aside>
<h3 id="basic-setup">Basic setup</h3>
<p>Here are steps to set up environment variables for local development using either <code>.dev.vars</code> or <code>.env</code> files.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16292.md")
</div>
<h2 id="multiple-local-environments">Multiple local environments</h2>
<p>To simulate different local environments, you can provide environment-specific files.
For example, you might have a <code>staging</code> environment that requires different settings than your development environment.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16293.md")
</div>
<h2 id="learn-more">Learn more</h2>
<ul>
<li>To learn how to configure multiple environments in Wrangler configuration, <a href="/workers/wrangler/environments/#_top">read the documentation</a>.</li>
<li>To learn how to use Wrangler environments and Vite environments together, <a href="/workers/vite-plugin/reference/cloudflare-environments/">read the Vite plugin documentation</a></li>
</ul>
