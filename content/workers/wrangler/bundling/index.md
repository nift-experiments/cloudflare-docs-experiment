---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/bundling/
  description: Review Wrangler's default bundling.
  full_title: Bundling · Cloudflare Workers docs
  head_html: <title>Bundling · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Review Wrangler&#x27;s default bundling."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/bundling/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/bundling/index.md"><meta property="og:title" content="Bundling · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review Wrangler&#x27;s default bundling."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/bundling/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/bundling/#page","headline":"Bundling \u00b7 Cloudflare Workers docs","description":"Review Wrangler's default bundling.","url":"https://developers.cloudflare.com/workers/wrangler/bundling/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/bundling/
  schema: 1
---
<p>By default, Wrangler bundles your Worker code using <a href="https://esbuild.github.io/"><code>esbuild</code></a>. This means that Wrangler has built-in support for importing modules from <a href="https://www.npmjs.com/">npm</a> defined in your <code>package.json</code>. To review the exact code that Wrangler will upload to Cloudflare, run <code>npx wrangler deploy --dry-run --outdir dist</code>, which will show your Worker code after Wrangler's bundling.</p>
<details>
<summary>`esbuild` version</summary>
<p>Wrangler uses <code>esbuild</code>. We periodically update the <code>esbuild</code> version included with Wrangler, and since <code>esbuild</code> is a pre-1.0.0 tool, this may sometimes include breaking changes to how bundling works. In particular, we may bump the <code>esbuild</code> version in a Wrangler minor version.</p>
</details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16000.md")
</aside>
<h2 id="including-non-javascript-modules">Including non-JavaScript modules</h2>
<p>Bundling your Worker code takes multiple modules and bundles them into one file.
Sometimes, you might have modules that cannot be inlined directly into the bundle.
For example, instead of bundling a Wasm file into your JavaScript Worker, you would want to upload the Wasm file as a separate module that can be imported at runtime.
Wrangler supports this by default for the following file types:</p>
<table>
<thead>
<tr>
<th>Module extension</th>
<th>Imported type</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.txt</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.html</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.sql</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.bin</code></td>
<td><code>ArrayBuffer</code></td>
</tr>
<tr>
<td><code>.wasm</code>, <code>.wasm?module</code></td>
<td><code>WebAssembly.Module</code></td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/workers/wrangler/configuration/#bundling">Bundling configuration</a> to customize these file types.</p>
<p>For example, with the following import, <code>text</code> will be a string containing the contents of <code>example.txt</code>:</p>
<pre tabindex="0"><code class="language-js">import text from &quot;./example.txt&quot;;&#10;</code></pre>
<p>This is also the basis for importing Wasm, as in the following example:</p>
<pre tabindex="0"><code class="language-ts">import wasm from &quot;./example.wasm&quot;;&#10;&#10;// Instantiate Wasm modules in the module scope&#10;const instance = await WebAssembly.instantiate(wasm);&#10;&#10;export default {&#10;	fetch() {&#10;		const result = instance.exports.exported_func();&#10;&#10;		return new Response(result);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15999.md")
</aside>
<h2 id="find-additional-modules">Find additional modules</h2>
<p>By setting <code>find_additional_modules</code> to <code>true</code> in your configuration file, Wrangler will traverse the file tree below <code>base_dir</code>.
Any files that match the <code>rules</code> you define will also be included as unbundled, external modules in the deployed Worker.</p>
<p>This approach is useful for supporting lazy loading of large or dynamically imported JavaScript files:</p>
<ul>
<li>Normally, a large lazy-imported file (for example, <code>await import(&quot;./large-dep.mjs&quot;)</code>) would be bundled directly into your entrypoint, reducing the effectiveness of the lazy loading.
If matching rule is added to <code>rules</code>, then this file would only be loaded and executed at runtime when it is actually imported.</li>
<li>Previously, variable based dynamic imports (for example, <code>await import(`./lang/${language}.mjs`)</code>) would always fail at runtime because Wrangler had no way of knowing which modules to include in the upload.
Providing a rule that matches all these files, such as <code>{ &quot;type&quot;: &quot;EsModule&quot;, &quot;globs&quot;: [&quot;./lang/**/*.mjs&quot;], &quot;fallthrough&quot;: true }</code>, will ensure this module is available at runtime.</li>
<li>&quot;Partial bundling&quot; is supported when <code>find_additional_modules</code> is <code>true</code>, and a source file matches one of the configured <code>rules</code>, since Wrangler will then treat it as &quot;external&quot; and not try to bundle it into the entry-point file.</li>
</ul>
<h2 id="node-env"><code>NODE_ENV</code></h2>
<p><code>process.env.NODE_ENV</code> is statically replaced at build time with one of the following values:</p>
<table>
<thead>
<tr>
<th>Context</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler dev</code></td>
<td><code>&quot;development&quot;</code></td>
</tr>
<tr>
<td><code>wrangler deploy</code> or <code>wrangler build</code></td>
<td><code>&quot;production&quot;</code></td>
</tr>
</tbody>
</table>
<p>You can use <code>process.env.NODE_ENV</code> to conditionally run code based on the build context:</p>
<pre tabindex="0"><code class="language-ts">if (process.env.NODE_ENV === &quot;development&quot;) {&#10;	console.log(&quot;Running in development mode&quot;);&#10;}&#10;</code></pre>
<p>Because <code>process.env.NODE_ENV</code> is replaced at build time, development only code can be removed from the production bundle.</p>
<p>You can override the default value by setting the <code>NODE_ENV</code> environment variable when running the command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>NODE_ENV=staging npx wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="NODE_ENV=staging npx wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>NODE_ENV=staging yarn wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="NODE_ENV=staging yarn wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>NODE_ENV=staging pnpm wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="NODE_ENV=staging pnpm wrangler dev" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="conditional-exports">Conditional exports</h2>
<p>Wrangler respects the <a href="https://nodejs.org/api/packages.html#conditional-exports">conditional <code>exports</code> field</a> in <code>package.json</code>. This allows developers to implement isomorphic libraries that have different implementations depending on the JavaScript runtime they are running in. When bundling, Wrangler will try to load the <a href="https://runtime-keys.proposal.wintercg.org/#workerd"><code>workerd</code> key</a>. Refer to the Wrangler repository for <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/isomorphic-random-example">an example isomorphic package</a>.</p>
<h2 id="disable-bundling">Disable bundling</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15998.md")
</aside>
<p>If your build tooling already produces build artifacts suitable for direct deployment to Cloudflare, you can opt out of bundling by using the <code>--no-bundle</code> command line flag: <code>npx wrangler deploy --no-bundle</code>. If you opt out of bundling, Wrangler will not process your code and some features introduced by Wrangler bundling (for example minification, and polyfills injection) will not be available.</p>
<p>Use <a href="/workers/wrangler/custom-builds/">Custom Builds</a> to customize what Wrangler will bundle and upload to the Cloudflare global network when you use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> and <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a>.</p>
<h2 id="generated-wrangler-configuration">Generated Wrangler configuration</h2>
<p>Some framework tools, or custom pre-build processes, generate a modified Wrangler configuration to be used to deploy the Worker code.
It is possible for Wrangler to automatically use this generated configuration rather than the original, user's configuration.</p>
<p>See <a href="/workers/wrangler/configuration/#generated-wrangler-configuration">Generated Wrangler configuration</a> for more information.</p>
