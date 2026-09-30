---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/typescript/
  description: Use TypeScript with fully typed APIs to build Cloudflare Workers.
  full_title: Write Cloudflare Workers in TypeScript · Cloudflare Workers docs
  head_html: <title>Write Cloudflare Workers in TypeScript · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use TypeScript with fully typed APIs to build Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/typescript/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/typescript/index.md"><meta property="og:title" content="Write Cloudflare Workers in TypeScript · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use TypeScript with fully typed APIs to build Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/typescript/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/languages/typescript/#page","headline":"Write Cloudflare Workers in TypeScript \u00b7 Cloudflare Workers docs","description":"Use TypeScript with fully typed APIs to build Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/languages/typescript/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/typescript/
  schema: 1
---
<p>TypeScript is a first-class language on Cloudflare Workers. All APIs provided in Workers are fully typed, and type definitions are generated directly from <a href="https://github.com/cloudflare/workerd">workerd</a>, the open-source Workers runtime.</p>
<p>We recommend you generate types for your Worker by running <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a>. Cloudflare also publishes type definitions to <a href="https://github.com/cloudflare/workers-types">GitHub</a> and <a href="https://www.npmjs.com/package/@cloudflare/workers-types">npm</a> (<code>npm install -D @cloudflare/workers-types</code>).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="version-5-and-later">Version 5 and later</h3>
@markup("md", "content/.markup/bodies/16991.md")
</aside>
<h3 id="generate-types">
	Generate types that match your Worker's configuration
</h3>
<p>Cloudflare continuously improves <a href="https://github.com/cloudflare/workerd">workerd</a>, the open-source Workers runtime.
Changes in workerd can introduce JavaScript API changes, thus changing the respective TypeScript types.</p>
<p>This means the correct types for your Worker depend on:</p>
<ol>
<li>Your Worker's <a href="/workers/configuration/compatibility-dates/">compatibility date</a>.</li>
<li>Your Worker's <a href="/workers/configuration/compatibility-flags/">compatibility flags</a>.</li>
<li>Your Worker's bindings, which are defined in your <a href="/workers/wrangler/configuration">Wrangler configuration file</a>.</li>
<li>Any <a href="/workers/wrangler/configuration/#bundling">module rules</a> you have specified in your Wrangler configuration file under <code>rules</code>.</li>
</ol>
<p>For example, the runtime will only allow you to use the <a href="https://nodejs.org/api/async_context.html#class-asynclocalstorage"><code>AsyncLocalStorage</code></a> class if you have <code>compatibility_flags = [&quot;nodejs_als&quot;]</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. This should be reflected in the type definitions.</p>
<p>To ensure that your type definitions always match your Worker's configuration, you can dynamically generate types by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types" aria-label="Copy to clipboard">Copy</button></div></div>
<p>See <a href="/workers/wrangler/commands/general/#types">the <code>wrangler types</code> command docs</a> for more details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16990.md")
</aside>
<p>This will generate a <code>d.ts</code> file and (by default) save it to <code>worker-configuration.d.ts</code>. This will include <code>Env</code> types based on your Worker bindings <em>and</em> runtime types based on your Worker's compatibility date and flags.</p>
<p>You should then add that file to your <code>tsconfig.json</code>'s <code>compilerOptions.types</code> array. If you have the <code>nodejs_compat</code> compatibility flag, you should also install <code>@types/node</code>.</p>
<p>You can commit your types file to git if you wish.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16989.md")
</aside>
<h3 id="migrating">
	Migrating from `@cloudflare/workers-types` to `wrangler types`
</h3>
<p>We recommend you use <code>wrangler types</code> to generate runtime types, rather than using the <code>@cloudflare/workers-types</code> package, as it generates types based on your Worker's <a href="https://github.com/cloudflare/workerd/tree/main/npm/workers-types#compatibility-dates">compatibility date</a> and <code>compatibility flags</code>, ensuring that types match the exact runtime APIs made available to your Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16988.md")
</aside>
<h4 id="1-uninstall-cloudflare-workers-types"><ol>
<li>Uninstall <code>@cloudflare/workers-types</code></li>
</ol></h4>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm uninstall @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm uninstall @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn remove @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn remove @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm remove @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm remove @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun remove @cloudflare/workers-types</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun remove @cloudflare/workers-types" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2-generate-runtime-types-using-wrangler"><ol start="2">
<li>Generate runtime types using Wrangler</li>
</ol></h4>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler types</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This will generate a <code>.d.ts</code> file, saved to <code>worker-configuration.d.ts</code> by default. This will also generate <code>Env</code> types. If for some reason you do not want to include those, you can set <code>--include-env=false</code>.</p>
<p>You can now remove any imports from <code>@cloudflare/workers-types</code> in your Worker code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16987.md")
</aside>
<h4 id="3-make-sure-your-tsconfig-json-includes-the-generated-types"><ol start="3">
<li>Make sure your <code>tsconfig.json</code> includes the generated types</li>
</ol></h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;types&quot;: [&quot;./worker-configuration.d.ts&quot;]&#10;	}&#10;}&#10;</code></pre>
<p>Note that if you have specified a custom path for the runtime types file, you should use that in your <code>compilerOptions.types</code> array instead of the default path.</p>
<h4 id="4-add-types-node-if-you-are-using-nodejs-compat-workers-runtime-apis-nodejs-optional"><ol start="4">
<li>Add @types/node if you are using <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> (Optional)</li>
</ol></h4>
<p>If you are using the <code>nodejs_compat</code> compatibility flag, you should also install <code>@types/node</code>.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @types/node</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @types/node" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @types/node</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @types/node" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @types/node</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @types/node" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @types/node</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @types/node" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Then add this to your <code>tsconfig.json</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;types&quot;: [&quot;./worker-configuration.d.ts&quot;, &quot;node&quot;]&#10;	}&#10;}&#10;</code></pre>
<h4 id="5-update-your-scripts-and-ci-pipelines"><ol start="5">
<li>Update your scripts and CI pipelines</li>
</ol></h4>
<p>Regardless of your specific framework or build tools, you should run the <code>wrangler types</code> command before any tasks that rely on TypeScript.</p>
<p>Most projects will have existing build and development scripts, as well as some type-checking. In the example below, we're adding the <code>wrangler types</code> before the type-checking script in the project:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;dev&quot;: &quot;existing-dev-command&quot;,&#10;		&quot;build&quot;: &quot;existing-build-command&quot;,&#10;		&quot;generate-types&quot;: &quot;wrangler types&quot;,&#10;		&quot;type-check&quot;: &quot;generate-types &amp;&amp; tsc&quot;&#10;	}&#10;}&#10;</code></pre>
<p>We recommend you commit your generated types file for use in CI. You can run <code>wrangler types</code> before other CI commands, as it should not take more than a few seconds. For example:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16995.md")
</div></div>
<p>Alternatively, if you commit your generated types file and want to verify it stays up-to-date in CI, you can use the <code>--check</code> flag:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16999.md")
</div></div>
<p>This fails the CI job if the committed types file is out-of-date, prompting developers to regenerate and commit the updated types.</p>
<h3 id="resources">Resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare/templates/hello-world/ts">TypeScript template</a></li>
<li><a href="https://github.com/cloudflare/workers-types">@cloudflare/workers-types</a></li>
<li><a href="/workers/runtime-apis/">Runtime APIs</a></li>
<li><a href="/workers/examples/?languages=TypeScript">TypeScript Examples</a></li>
</ul>
