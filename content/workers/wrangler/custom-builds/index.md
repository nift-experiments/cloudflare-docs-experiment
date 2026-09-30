---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/custom-builds/
  description: Customize how your code is compiled, before being processed by Wrangler.
  full_title: Custom builds · Cloudflare Workers docs
  head_html: <title>Custom builds · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize how your code is compiled, before being processed by Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/custom-builds/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/custom-builds/index.md"><meta property="og:title" content="Custom builds · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize how your code is compiled, before being processed by Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/custom-builds/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/custom-builds/#page","headline":"Custom builds \u00b7 Cloudflare Workers docs","description":"Customize how your code is compiled, before being processed by Wrangler.","url":"https://developers.cloudflare.com/workers/wrangler/custom-builds/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/custom-builds/
  schema: 1
---
<p>Custom builds are a way for you to customize how your code is compiled, before being processed by Wrangler.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15928.md")
</aside>
<h2 id="configure-custom-builds">Configure custom builds</h2>
<p>Custom builds are configured by adding a <code>[build]</code> section in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, and using the following options for configuring your custom build.</p>
<ul>
<li>
<p><code>command</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The command used to build your Worker. On Linux and macOS, the command is executed in the <code>sh</code> shell and the <code>cmd</code> shell for Windows. The <code>&amp;&amp;</code> and <code>||</code> shell operators may be used. This command will be run as part of <code>wrangler dev</code> and <code>npx wrangler deploy</code>.</li>
</ul>
</li>
<li>
<p><code>cwd</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The directory in which the command is executed.</li>
</ul>
</li>
<li>
<p><code>watch_dir</code> <span class="nb-type">string | string[]</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The directory to watch for changes while using <code>wrangler dev</code>. Defaults to the current working directory.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15929.md")
</div>
<h2 id="wrangler-command-environment-variable"><code>WRANGLER_COMMAND</code> environment variable</h2>
<p>When Wrangler runs your custom build command, it sets the <code>WRANGLER_COMMAND</code> environment variable so your build script can detect which Wrangler command triggered the build. This allows you to customize the build process based on the deployment context.</p>
<p>The possible values are:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Wrangler command triggered</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dev</code></td>
<td><code>wrangler dev</code></td>
</tr>
<tr>
<td><code>deploy</code></td>
<td><code>wrangler deploy</code></td>
</tr>
<tr>
<td><code>versions upload</code></td>
<td><code>wrangler versions upload</code></td>
</tr>
<tr>
<td><code>types</code></td>
<td><code>wrangler types</code></td>
</tr>
</tbody>
</table>
<p>For example, you can use this to apply different build settings for development and production:</p>
<pre tabindex="0"><code class="language-bash">&#35;!/bin/bash&#10;if [ &quot;$WRANGLER_COMMAND&quot; = &quot;dev&quot; ]; then&#10;  echo &quot;Building for development...&quot;&#10;  &#35; run a development build&#10;else&#10;  echo &quot;Building for production...&quot;&#10;  &#35; run a production build&#10;fi&#10;</code></pre>
