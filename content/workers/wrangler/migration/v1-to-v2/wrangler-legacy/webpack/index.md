---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/
  description: Learn how to migrate from Wrangler v1 to v2 using webpack. This guide covers configuration, custom builds, and compatibility for Cloudflare Workers.
  full_title: Webpack · Cloudflare Workers docs
  head_html: <title>Webpack · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to migrate from Wrangler v1 to v2 using webpack. This guide covers configuration, custom builds, and compatibility for Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/webpack/index.md"><meta property="og:title" content="Webpack · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to migrate from Wrangler v1 to v2 using webpack. This guide covers configuration, custom builds, and compatibility for Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/webpack/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/#page","headline":"Webpack \u00b7 Cloudflare Workers docs","description":"Learn how to migrate from Wrangler v1 to v2 using webpack. This guide covers configuration, custom builds, and compatibility for Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/wrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/migration/v1-to-v2/wrangler-legacy/webpack/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17452.md")
</aside>
<p>Wrangler allows you to develop modern ES6 applications with support for modules. This support is possible because of Wrangler's <a href="https://webpack.js.org/">webpack</a> integration. This document describes how Wrangler uses webpack to build your Workers and how you can bring your own configuration.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="configuration-and-webpack-version">Configuration and webpack version</h3>
@markup("md", "content/.markup/bodies/17451.md")
</aside>
<h2 id="sensible-defaults">Sensible defaults</h2>
<p>This is the default webpack configuration that Wrangler uses to build your Worker:</p>
<pre tabindex="0"><code class="language-js">module.exports = {&#10;	target: &quot;webworker&quot;,&#10;	entry: &quot;./index.js&quot;, // inferred from &quot;main&quot; in package.json&#10;};&#10;</code></pre>
<p>The <code>&quot;main&quot;</code> field in the <code>package.json</code> file determines the <code>entry</code> configuration value. When undefined or missing, <code>&quot;main&quot;</code> defaults to <code>index.js</code>, meaning that <code>entry</code> also defaults to <code>index.js</code>.</p>
<p>The default configuration sets <code>target</code> to <code>webworker</code>. This is the correct value because Cloudflare Workers are built to match the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API">Service Worker API</a>. Refer to the <a href="https://webpack.js.org/concepts/targets/">webpack documentation</a> for an explanation of this <code>target</code> value.</p>
<h2 id="bring-your-own-configuration">Bring your own configuration</h2>
<p>You can tell Wrangler to use a custom webpack configuration file by setting <code>webpack_config</code> in your Wrangler file. Always set <code>target</code> to <code>webworker</code>.</p>
<h3 id="example">Example</h3>
<pre tabindex="0"><code class="language-js">module.exports = {&#10;	target: &quot;webworker&quot;,&#10;	entry: &quot;./index.js&quot;,&#10;	mode: &quot;production&quot;,&#10;};&#10;</code></pre>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17453.md")
</div>
<h3 id="example-with-multiple-environments">Example with multiple environments</h3>
<p>It is possible to use different webpack configuration files within different <a href="/workers/wrangler/environments/">Wrangler environments</a>. For example, the <code>&quot;webpack.development.js&quot;</code> configuration file is used during <code>wrangler dev</code> for development, but other, more production-ready configurations are used when building for the staging or production environments:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17454.md")
</div>
<pre tabindex="0"><code class="language-js">module.exports = {&#10;	target: &quot;webworker&quot;,&#10;	devtool: &quot;cheap-module-source-map&quot;, // avoid &quot;eval&quot;: Workers environment doesn’t allow it&#10;	entry: &quot;./index.js&quot;,&#10;	mode: &quot;development&quot;,&#10;};&#10;</code></pre>
<pre tabindex="0"><code class="language-js">module.exports = {&#10;	target: &quot;webworker&quot;,&#10;	entry: &quot;./index.js&quot;,&#10;	mode: &quot;production&quot;,&#10;};&#10;</code></pre>
<h3 id="using-with-workers-sites">Using with Workers Sites</h3>
<p>Wrangler commands are run from the project root. Ensure your <code>entry</code> and <code>context</code> are set appropriately. For a project with structure:</p>
<pre tabindex="0"><code class="language-txt">.&#10;├── public&#10;│   ├── 404.html&#10;│   └── index.html&#10;├── workers-site&#10;│   ├── index.js&#10;│   ├── package-lock.json&#10;│   ├── package.json&#10;│   └── webpack.config.js&#10;└── wrangler.toml&#10;</code></pre>
<p>The corresponding <code>webpack.config.js</code> file should look like this:</p>
<pre tabindex="0"><code class="language-js">module.exports = {&#10;	context: __dirname,&#10;	target: &quot;webworker&quot;,&#10;	entry: &quot;./index.js&quot;,&#10;	mode: &quot;production&quot;,&#10;};&#10;</code></pre>
<h2 id="shimming-globals">Shimming globals</h2>
<p>When you want to bring your own implementation of an existing global API, you may <a href="https://webpack.js.org/guides/shimming/#shimming-globals">shim</a> a third-party module in its place as a webpack plugin.</p>
<p>For example, you may want to replace the <code>URL</code> global class with the <code>url-polyfill</code> npm package. After defining the package as a dependency in your <code>package.json</code> file and installing it, add a plugin entry to your webpack configuration.</p>
<h3 id="example-with-webpack-plugin">Example with webpack plugin</h3>
<pre tabindex="0"><code class="language-js">const webpack = require(&quot;webpack&quot;);&#10;&#10;module.exports = {&#10;	target: &quot;webworker&quot;,&#10;	entry: &quot;./index.js&quot;,&#10;	mode: &quot;production&quot;,&#10;	plugins: [&#10;		new webpack.ProvidePlugin({&#10;			URL: &quot;url-polyfill&quot;,&#10;		}),&#10;	],&#10;};&#10;</code></pre>
<h2 id="backwards-compatibility">Backwards compatibility</h2>
<p>If you are using <code>wrangler@1.6.0</code> or earlier, a <code>webpack.config.js</code> file at the root of your project is loaded automatically. This is not always obvious, which is why versions of Wrangler after <code>wrangler@1.6.0</code> require you to specify a <code>webpack_config</code> value in your Wrangler file.</p>
<p>When <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update/">upgrading from <code>wrangler@1.6.0</code></a>, you may encounter webpack configuration warnings. To resolve this, add <code>webpack_config = &quot;webpack.config.js&quot;</code> to your Wrangler file.</p>
