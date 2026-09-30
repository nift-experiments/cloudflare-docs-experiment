---
cp9:
  canonical: https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/
  description: Static assets and the Vite plugin
  full_title: Static Assets · Cloudflare Workers docs
  head_html: <title>Static Assets · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Static assets and the Vite plugin"><link rel="canonical" href="https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/index.md"><meta property="og:title" content="Static Assets · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Static assets and the Vite plugin"><meta property="og:url" content="https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/#page","headline":"Static Assets \u00b7 Cloudflare Workers docs","description":"Static assets and the Vite plugin","url":"https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/vite-plugin/reference/static-assets/
  schema: 1
---
<p>This guide focuses on the areas of working with static assets that are unique to the Vite plugin.
For more general documentation, see <a href="/workers/static-assets/">Static Assets</a>.</p>
<h2 id="configuration">Configuration</h2>
<p>The Vite plugin does not require that you provide the <code>assets</code> field in order to enable assets and instead determines whether assets should be included based on whether the <code>client</code> environment has been built. By default, the <code>client</code> environment is built if any of the following conditions are met:</p>
<ul>
<li>There is an <code>index.html</code> file in the root of your project</li>
<li><code>build.rollupOptions.input</code> or <code>environments.client.build.rollupOptions.input</code> is specified in your Vite config</li>
<li>You have a non-empty <a href="https://vite.dev/guide/assets#the-public-directory"><code>public</code> directory</a></li>
<li>Your Worker <a href="https://vite.dev/guide/assets#importing-asset-as-url">imports assets as URLs</a></li>
</ul>
<p>On running <code>vite build</code>, an output <code>wrangler.json</code> configuration file is generated as part of the build output.
The <code>assets.directory</code> field in this file is automatically populated with the path to your <code>client</code> build output.
It is therefore not necessary to provide the <code>assets.directory</code> field in your input Worker configuration.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-access-context">Cloudflare Access context</h3>
@markup("md", "content/.markup/bodies/17384.md")
</aside>
<p>The <code>assets</code> configuration should be used, however, if you wish to set <a href="/workers/static-assets/routing/">routing configuration</a> or enable the <a href="/workers/static-assets/binding/#binding">assets binding</a>.
The following example configures the <code>not_found_handling</code> for a single-page application so that the fallback will always be the root <code>index.html</code> file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17385.md")
</div>
<h2 id="features">Features</h2>
<p>The Vite plugin ensures that all of Vite's <a href="https://vite.dev/guide/assets">static asset handling</a> features are supported in your Worker as well as in your frontend.
These include importing assets as URLs, importing as strings and importing from the <code>public</code> directory as well as inlining assets.</p>
<p>Assets <a href="https://vite.dev/guide/assets#importing-asset-as-url">imported as URLs</a> can be fetched via the <a href="/workers/static-assets/binding/#binding">assets binding</a>.
As the binding's <code>fetch</code> method requires a full URL, we recommend using the request URL as the <code>base</code>.
This is demonstrated in the following example:</p>
<pre tabindex="0"><code class="language-ts">import myImage from &quot;./my-image.png&quot;;&#10;&#10;export default {&#10;	fetch(request, env) {&#10;		return env.ASSETS.fetch(new URL(myImage, request.url));&#10;	},&#10;};&#10;</code></pre>
<p>Assets imported as URLs in your Worker will automatically be moved to the client build output.
When running <code>vite build</code> the paths of any moved assets will be displayed in the console.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17383.md")
</aside>
<h2 id="headers-and-redirects">Headers and redirects</h2>
<p>Custom <a href="/workers/static-assets/headers/">headers</a> and <a href="/workers/static-assets/redirects/">redirects</a> are supported at build, preview and deploy time by adding <code>_headers</code> and <code>_redirects</code> files to your <a href="https://vite.dev/guide/assets#the-public-directory"><code>public</code> directory</a>.
The paths in these files should reflect the structure of your client build output.
For example, generated assets are typically located in an <a href="https://vite.dev/config/build-options#build-assetsdir">assets subdirectory</a>.</p>
