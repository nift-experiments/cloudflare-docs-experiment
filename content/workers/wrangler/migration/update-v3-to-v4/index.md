---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4/
  description: Upgrade Wrangler from v3 to v4, including breaking changes, updated Node.js requirements, and new defaults.
  full_title: Migrate from Wrangler v3 to v4 · Cloudflare Workers docs
  head_html: <title>Migrate from Wrangler v3 to v4 · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Upgrade Wrangler from v3 to v4, including breaking changes, updated Node.js requirements, and new defaults."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4/index.md"><meta property="og:title" content="Migrate from Wrangler v3 to v4 · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upgrade Wrangler from v3 to v4, including breaking changes, updated Node.js requirements, and new defaults."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4/#page","headline":"Migrate from Wrangler v3 to v4 \u00b7 Cloudflare Workers docs","description":"Upgrade Wrangler from v3 to v4, including breaking changes, updated Node.js requirements, and new defaults.","url":"https://developers.cloudflare.com/workers/wrangler/migration/update-v3-to-v4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/migration/update-v3-to-v4/
  schema: 1
---
<p>Wrangler v4 is a major release focused on updates to underlying systems and dependencies, along with improvements to keep Wrangler commands consistent and clear. Unlike previous major versions of Wrangler, which were <a href="https://blog.cloudflare.com/wrangler-v2-beta/">foundational rewrites</a> and <a href="https://blog.cloudflare.com/wrangler3/">rearchitectures</a> — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change.</p>
<p>While many users should expect a no-op upgrade, the following sections outline the more significant changes and steps for migrating where necessary.</p>
<h2 id="upgrade-to-wrangler-v4">Upgrade to Wrangler v4</h2>
<p>To upgrade to the latest version of Wrangler v4 within your Worker project, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i wrangler@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add wrangler@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add wrangler@4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add wrangler@4</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add wrangler@4" aria-label="Copy to clipboard">Copy</button></div></div>
<p>After upgrading, you can verify the installation:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler --version</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler --version" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler --version</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler --version" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler --version</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler --version" aria-label="Copy to clipboard">Copy</button></div></div>
<h3 id="summary-of-changes">Summary of changes</h3>
<ul>
<li>
<p><strong>Updated Node.js support policy:</strong>
Node.js v16, which reached End-of-Life in 2022, is no longer supported in Wrangler v4. Wrangler now follows Node.js's <a href="https://nodejs.org/en/about/previous-releases">official support lifecycle</a>.</p>
</li>
<li>
<p><strong>Upgraded esbuild version</strong>: Wrangler uses <a href="https://esbuild.github.io/">esbuild</a> to bundle Worker code before deploying it, and was previously pinned to esbuild v0.17.19. Wrangler v4 uses esbuild v0.24, which could impact dynamic wildcard imports. Going forward, Wrangler will be periodically updating the <code>esbuild</code> version included with Wrangler, and since <code>esbuild</code> is a pre-1.0.0 tool, this may sometimes include breaking changes to how bundling works. In particular, we may bump the <code>esbuild</code> version in a Wrangler minor version.</p>
</li>
<li>
<p><strong>Commands default to local mode</strong>: All commands that can run in either local or remote mode now default to local, requiring a <code>--remote</code> flag for API queries.</p>
</li>
<li>
<p><strong>Deprecated commands and configurations removed:</strong> Legacy commands, flags, and configurations are removed.</p>
</li>
</ul>
<h2 id="detailed-changes">Detailed Changes</h2>
<h3 id="updated-node-js-support-policy">Updated Node.js support policy</h3>
<p>Wrangler now supports only Node.js versions that align with <a href="https://nodejs.org/en/about/previous-releases">Node.js's official lifecycle</a>:</p>
<ul>
<li><strong>Supported</strong>: Current, Active LTS, Maintenance LTS</li>
<li><strong>No longer supported:</strong> Node.js v16 (EOL in 2022)</li>
</ul>
<p>Wrangler tests no longer run on v16, and users still on this version may encounter unsupported behavior. Users still using Node.js v16 must upgrade to a supported version to continue receiving support and compatibility with Wrangler.</p>
<details class="nb-details"><summary>Am I affected?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17404.md")
</div></details>
<h3 id="upgraded-esbuild-version">Upgraded esbuild version</h3>
<p>Wrangler v4 upgrades esbuild from <strong>v0.17.19</strong> to <strong>v0.24</strong>, bringing improvements (such as the ability to use the <code>using</code> keyword with RPC) and changes to bundling behavior:</p>
<ul>
<li><strong>Dynamic imports:</strong> Wildcard imports (for example, <code>import('./data/' + kind + '.json')</code>) now automatically include all matching files in the bundle.</li>
</ul>
<p>Users relying on wildcard dynamic imports may see unwanted files bundled. Prior to esbuild v0.19, <code>import</code> statements with dynamic paths (like <code>import('./data/' + kind + '.json')</code>) did not bundle all files matching the glob pattern (<code>*.json</code>). Only files explicitly referenced or included using <code>find_additional_modules</code> were bundled. With esbuild v0.19, wildcard imports now automatically bundle all files matching the glob pattern. This could result in unwanted files being bundled, so users might want to avoid wildcard dynamic imports and use explicit imports instead.</p>
<h3 id="commands-default-to-local-mode">Commands default to local mode</h3>
<p>All commands now run in <strong>local mode by default.</strong> Wrangler has many commands for accessing resources like KV and R2, but the commands were previously inconsistent in whether they ran in a local or remote environment. For example, D1 defaulted to querying a local datastore, and required the <code>--remote</code> flag to query via the API. KV, on the other hand, previously defaulted to querying via the API (implicitly using the <code>--remote</code> flag) and required a <code>--local</code> flag to query a local datastore. In order to make the behavior consistent across Wrangler, each command now uses the <code>--local</code> flag by default, and requires an explicit <code>--remote</code> flag to query via the API.</p>
<p>For example:</p>
<ul>
<li><strong>Previous Behavior (Wrangler v3):</strong> <code>wrangler kv key get</code> queried remotely by default.</li>
<li><strong>New Behavior (Wrangler v4):</strong> <code>wrangler kv key get</code> queries locally unless <code>--remote</code> is specified.</li>
</ul>
<p>Those using <code>wrangler kv key</code> and/or <code>wrangler r2 object</code> commands to query or write to their data store will need to add the <code>--remote</code> flag in order to replicate previous behavior.</p>
<details class="nb-details"><summary>Am I affected?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17405.md")
</div></details>
<h3 id="deprecated-commands-and-configurations-removed">Deprecated commands and configurations removed</h3>
<p>All previously deprecated features in <a href="/workers/wrangler/deprecations/#wrangler-v2">Wrangler v2</a> and in <a href="/workers/wrangler/deprecations/#wrangler-v3">Wrangler v3</a> are now removed. Additionally, the following features that were deprecated during the Wrangler v3 release are also now removed:</p>
<ul>
<li>Legacy Assets (using <code>wrangler dev/deploy --legacy-assets</code> or the <code>legacy_assets</code> config file property). Instead, we recommend you <a href="/workers/static-assets/">migrate to Workers Static Assets</a>.</li>
<li>Legacy Node.js compatibility (using <code>wrangler dev/deploy --node-compat</code> or the <code>node_compat</code> config file property). Instead, use the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code> compatibility flag</a>. This includes the functionality from legacy <code>node_compat</code> polyfills and natively implemented Node.js APIs.</li>
<li><code>wrangler version</code>. Instead, use <code>wrangler --version</code> to check the current version of Wrangler.</li>
<li><code>getBindingsProxy()</code> (via <code>import { getBindingsProxy } from &quot;wrangler&quot;</code>). Instead, use the <a href="/workers/wrangler/api/#getplatformproxy"><code>getPlatformProxy()</code> API</a>, which takes exactly the same arguments.</li>
<li><code>usage_model</code>. This no longer has any effect, after the <a href="https://blog.cloudflare.com/workers-pricing-scale-to-zero/">rollout of Workers Standard Pricing</a>.</li>
</ul>
<details class="nb-details"><summary>Am I affected?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17406.md")
</div></details>
