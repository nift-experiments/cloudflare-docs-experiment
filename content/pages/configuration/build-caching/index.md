---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/build-caching/
  description: Speed up Cloudflare Pages builds by caching dependencies and build output between deployments.
  full_title: Build caching · Cloudflare Pages docs
  head_html: <title>Build caching · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Speed up Cloudflare Pages builds by caching dependencies and build output between deployments."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/build-caching/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/build-caching/index.md"><meta property="og:title" content="Build caching · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Speed up Cloudflare Pages builds by caching dependencies and build output between deployments."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/build-caching/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/build-caching/#page","headline":"Build caching \u00b7 Cloudflare Pages docs","description":"Speed up Cloudflare Pages builds by caching dependencies and build output between deployments.","url":"https://developers.cloudflare.com/pages/configuration/build-caching/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/build-caching/
  schema: 1
---
<p>Improve Pages build times by caching dependencies and build output between builds with a project-wide shared cache.</p>
<p>The first build to occur after enabling build caching on your Pages project will save to cache. Every subsequent build will restore from cache unless configured otherwise.</p>
<h2 id="about-build-cache">About build cache</h2>
<p>When enabled, the build cache will automatically detect and cache data from each build. Refer to <a href="/pages/configuration/build-caching/#frameworks">Frameworks</a> to review what directories are automatically saved and restored from the build cache.</p>
<h3 id="requirements">Requirements</h3>
<p>Build caching requires the <a href="/pages/configuration/build-image/#v2-build-system">V2 build system</a> or later. To update from V1, refer to the <a href="/pages/configuration/build-image/#v1-to-v2-migration">V2 build system migration instructions</a>.</p>
<h3 id="package-managers">Package managers</h3>
<p>Pages will cache the global cache directories of the following package managers:</p>
<table>
<thead>
<tr>
<th>Package Manager</th>
<th>Directories cached</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.npmjs.com/">npm</a></td>
<td><code>.npm</code></td>
</tr>
<tr>
<td><a href="https://yarnpkg.com/">yarn</a></td>
<td><code>.cache/yarn</code></td>
</tr>
<tr>
<td><a href="https://pnpm.io/">pnpm</a></td>
<td><code>.pnpm-store</code></td>
</tr>
<tr>
<td><a href="https://bun.sh/">bun</a></td>
<td><code>.bun/install/cache</code></td>
</tr>
</tbody>
</table>
<h3 id="frameworks">Frameworks</h3>
<p>Some frameworks provide a cache directory that is typically populated by the framework with intermediate build outputs or dependencies during build time. Pages will automatically detect the framework you are using and cache this directory for reuse in subsequent builds.</p>
<p>The following frameworks support build output caching:</p>
<table>
<thead>
<tr>
<th>Framework</th>
<th>Directories cached</th>
</tr>
</thead>
<tbody>
<tr>
<td>Astro</td>
<td><code>node_modules/.astro</code></td>
</tr>
<tr>
<td>Docusaurus</td>
<td><code>node_modules/.cache</code>, <code>.docusaurus</code>, <code>build</code></td>
</tr>
<tr>
<td>Eleventy</td>
<td><code>.cache</code></td>
</tr>
<tr>
<td>Gatsby</td>
<td><code>.cache</code>, <code>public</code></td>
</tr>
<tr>
<td>Hugo</td>
<td><code>.cache</code></td>
</tr>
<tr>
<td>Next.js</td>
<td><code>.next/cache</code></td>
</tr>
<tr>
<td>Nuxt</td>
<td><code>node_modules/.cache/nuxt</code></td>
</tr>
<tr>
<td>SvelteKit</td>
<td><code>node_modules/.cache/imagetools</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="hugo-build-caching">Hugo build caching</h3>
@markup("md", "content/.markup/bodies/11077.md")
</aside>
<h3 id="limits">Limits</h3>
<p>The following limits are imposed for build caching:</p>
<ul>
<li><strong>Retention</strong>: Cache is purged seven days after its last read date. Unread cache artifacts are purged seven days after creation.</li>
<li><strong>Storage</strong>: Every project is allocated 10 GB. If the project cache exceeds this limit, the project will automatically start deleting artifacts that were read least recently.</li>
</ul>
<h2 id="enable-build-cache">Enable build cache</h2>
<p>To enable build caching :</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11078.md")
</div>
<h2 id="clear-build-cache">Clear build cache</h2>
<p>The build cache can be cleared for a project if needed, such as when debugging build issues. To clear the build cache:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11079.md")
</div>
