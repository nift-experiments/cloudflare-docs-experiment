---
cp9:
  canonical: https://developers.cloudflare.com/flagship/sdk/
  description: Use the official Flagship OpenFeature SDKs to evaluate feature flags from Workers, Node.js, browsers, Python, and Go applications.
  full_title: OpenFeature SDK · Cloudflare Flagship docs
  head_html: <title>OpenFeature SDK · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the official Flagship OpenFeature SDKs to evaluate feature flags from Workers, Node.js, browsers, Python, and Go applications."><link rel="canonical" href="https://developers.cloudflare.com/flagship/sdk/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/sdk/index.md"><meta property="og:title" content="OpenFeature SDK · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the official Flagship OpenFeature SDKs to evaluate feature flags from Workers, Node.js, browsers, Python, and Go applications."><meta property="og:url" content="https://developers.cloudflare.com/flagship/sdk/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/flagship/sdk/#page","headline":"OpenFeature SDK \u00b7 Cloudflare Flagship docs","description":"Use the official Flagship OpenFeature SDKs to evaluate feature flags from Workers, Node.js, browsers, Python, and Go applications.","url":"https://developers.cloudflare.com/flagship/sdk/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/sdk/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/8720.md")
</div>
<p><a href="https://openfeature.dev/">OpenFeature</a> is the CNCF standard for feature flag interfaces. It provides a vendor-neutral API so you can switch between flag providers without changing evaluation code.</p>
<p>Flagship provides official OpenFeature-compatible SDKs for TypeScript, Python, and Go. The source code is available on <a href="https://github.com/cloudflare/flagship">GitHub</a>.</p>
<table>
<thead>
<tr>
<th>SDK</th>
<th>Package</th>
<th>Runtime</th>
<th>Evaluation modes</th>
</tr>
</thead>
<tbody>
<tr>
<td>TypeScript</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/flagship"><code>@cloudflare/flagship</code></a></td>
<td>Workers, Node.js, browsers</td>
<td>Workers binding, HTTP, browser prefetch cache</td>
</tr>
<tr>
<td>Python</td>
<td><a href="https://pypi.org/project/cloudflare-flagship/"><code>cloudflare-flagship</code></a></td>
<td>Python server applications</td>
<td>HTTP</td>
</tr>
<tr>
<td>Go</td>
<td><a href="https://pkg.go.dev/github.com/cloudflare/flagship/sdks/go"><code>github.com/cloudflare/flagship/sdks/go</code></a></td>
<td>Go server applications</td>
<td>HTTP</td>
</tr>
</tbody>
</table>
<h2 id="sdks">SDKs</h2>
<p>Flagship SDKs are organized by language. The TypeScript SDK has separate setup guides for server-side and browser usage because they use different OpenFeature packages and runtime behavior.</p>
<ul>
<li><a href="/flagship/sdk/server-provider/">TypeScript Server SDK</a> — For Workers, Node.js, and other server-side JavaScript runtimes.</li>
<li><a href="/flagship/sdk/client-provider/">TypeScript Client SDK</a> — For browser applications that need synchronous OpenFeature web SDK evaluation.</li>
<li><a href="/flagship/sdk/python/">Python SDK</a> — For Python server applications.</li>
<li><a href="/flagship/sdk/go/">Go SDK</a> — For Go server applications.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8719.md")
</aside>
<h2 id="installation">Installation</h2>
<p>For TypeScript server-side usage:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For TypeScript browser usage:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For Python:</p>
<pre tabindex="0"><code class="language-sh">uv add cloudflare-flagship&#10;</code></pre>
<p>For Go:</p>
<pre tabindex="0"><code class="language-sh">go get github.com/cloudflare/flagship/sdks/go&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Set up the <a href="/flagship/sdk/server-provider/">server provider</a> for Workers, Node.js, or other server-side runtimes.</li>
<li>Set up the <a href="/flagship/sdk/client-provider/">client provider</a> for browser applications.</li>
<li>Set up the <a href="/flagship/sdk/python/">Python SDK</a> for Python server applications.</li>
<li>Set up the <a href="/flagship/sdk/go/">Go SDK</a> for Go server applications.</li>
</ul>
