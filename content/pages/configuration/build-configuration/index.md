---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/build-configuration/
  description: Set build commands, output directories, and framework presets for Cloudflare Pages projects.
  full_title: Build configuration · Cloudflare Pages docs
  head_html: <title>Build configuration · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Set build commands, output directories, and framework presets for Cloudflare Pages projects."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/build-configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/build-configuration/index.md"><meta property="og:title" content="Build configuration · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set build commands, output directories, and framework presets for Cloudflare Pages projects."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/build-configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/build-configuration/#page","headline":"Build configuration \u00b7 Cloudflare Pages docs","description":"Set build commands, output directories, and framework presets for Cloudflare Pages projects.","url":"https://developers.cloudflare.com/pages/configuration/build-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/build-configuration/
  schema: 1
---
<p>You may tell Cloudflare Pages how your site needs to be built as well as where its output files will be located.</p>
<h2 id="build-commands-and-directories">Build commands and directories</h2>
<p>You should provide a build command to tell Cloudflare Pages how to build your application. For projects not listed here, consider reading the tool's documentation or framework, and submit a pull request to add it here.</p>
<p>Build directories indicates where your project's build command outputs the built version of your Cloudflare Pages site. Often, this defaults to the industry-standard <code>public</code>, but you may find that you need to customize it.</p>
<details class="nb-details"><summary>Understanding your build configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11076.md")
</div></details>
<h2 id="framework-presets">Framework presets</h2>
<p>Cloudflare maintains a list of build configurations for popular frameworks and tools. These are accessible during project creation. Below are some standard build commands and directories for popular frameworks and tools.</p>
<p>If you are not using a preset, use <code>exit 0</code> as your <strong>Build command</strong>.</p>
<div class="nb-data-component" data-cf-component="PagesBuildPresetsTable"></div>
<h2 id="environment-variables">Environment variables</h2>
<p>If your project makes use of environment variables to build your site, you can provide custom environment variables:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Select **Settings** > **Environment variables**.
<p>The following system environment variables are injected by default (but can be overridden):</p>
<table>
<thead>
<tr>
<th>Environment Variable</th>
<th>Injected value</th>
<th>Example use-case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CI</code></td>
<td><code>true</code></td>
<td>Changing build behaviour when run on CI versus locally</td>
</tr>
<tr>
<td><code>CF_PAGES</code></td>
<td><code>1</code></td>
<td>Changing build behaviour when run on Pages versus locally</td>
</tr>
<tr>
<td><code>CF_PAGES_COMMIT_SHA</code></td>
<td><code>&lt;sha1-hash-of-current-commit&gt;</code></td>
<td>Passing current commit ID to error reporting, for example, Sentry</td>
</tr>
<tr>
<td><code>CF_PAGES_BRANCH</code></td>
<td><code>&lt;branch-name-of-current-deployment&gt;</code></td>
<td>Customizing build based on branch, for example, disabling debug logging on <code>production</code></td>
</tr>
<tr>
<td><code>CF_PAGES_URL</code></td>
<td><code>&lt;url-of-current-deployment&gt;</code></td>
<td>Allowing build tools to know the URL the page will be deployed at</td>
</tr>
</tbody>
</table>
