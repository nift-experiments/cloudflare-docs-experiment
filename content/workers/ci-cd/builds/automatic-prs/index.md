---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/
  description: Learn about the pull requests Workers Builds creates to configure your project or resolve issues.
  full_title: Automatic pull requests · Cloudflare Workers docs
  head_html: <title>Automatic pull requests · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about the pull requests Workers Builds creates to configure your project or resolve issues."><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/index.md"><meta property="og:title" content="Automatic pull requests · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about the pull requests Workers Builds creates to configure your project or resolve issues."><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/#page","headline":"Automatic pull requests \u00b7 Cloudflare Workers docs","description":"Learn about the pull requests Workers Builds creates to configure your project or resolve issues.","url":"https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/automatic-prs/
  schema: 1
---
<p>Workers Builds can automatically create pull requests in your repository to configure your project or resolve deployment issues.</p>
<h2 id="configuration-pr">Configuration PR</h2>
<p>When you connect a repository that does not have a Wrangler configuration file, Workers Builds runs <code>wrangler deploy</code> which triggers <a href="/workers/framework-guides/automatic-configuration/">automatic project configuration</a>. Instead of failing, it creates a pull request with the necessary configuration for your detected framework.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16784.md")
</aside>
<h3 id="why-you-should-merge-the-pr">Why you should merge the PR</h3>
<p>Without the configuration in your repository, every build has to run autoconfig first, which means your project gets built twice - once during autoconfig to generate the configuration, and again for the actual deployment. Merging the PR commits the configuration to your repository, so future builds skip autoconfig and go straight to building and deploying. This results in faster deployments and version-controlled settings.</p>
<h3 id="what-the-pr-includes">What the PR includes</h3>
<p><img src="/assets/upstream/images/workers/ci-cd/builds/automatic-pr.png" alt="Example of an automatic configuration pull request created by Workers Builds" /></p>
<p>The configuration PR may contain changes to the following files, depending on your framework:</p>
<ul>
<li><strong><code>wrangler.jsonc</code></strong> - Wrangler configuration file with your Worker settings</li>
<li><strong>Framework adapter</strong> - Any required Cloudflare adapter for your framework (for example, <code>@astrojs/cloudflare</code> for Astro)</li>
<li><strong>Framework configuration</strong> - Updates to framework config files (for example, <code>astro.config.mjs</code> for Astro or <code>svelte.config.js</code> for SvelteKit)</li>
<li><strong><code>package.json</code></strong> - New scripts like <code>deploy</code>, <code>preview</code>, and <code>cf-typegen</code>, plus required dependencies</li>
<li><strong><code>package-lock.json</code></strong> / <strong><code>yarn.lock</code></strong> / <strong><code>pnpm-lock.yaml</code></strong> - Updated lock file with new dependencies</li>
<li><strong><code>.gitignore</code></strong> - Entries for <code>.wrangler</code> and <code>.dev.vars*</code> files</li>
<li><strong><code>.assetsignore</code></strong> - For frameworks that generate worker files in the output directory</li>
</ul>
<h3 id="pr-description">PR description</h3>
<p>The PR description includes:</p>
<ul>
<li><strong>Detected settings</strong> - Framework, build command, deploy command, and version command</li>
<li><strong>Preview link</strong> - A working preview generated using the detected settings</li>
<li><strong>Next steps</strong> - Links to documentation for adding bindings, custom domains, and more</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16783.md")
</aside>
<h2 id="name-conflict-pr">Name conflict PR</h2>
<p>If Workers Builds detects a mismatch between your Worker name in the Cloudflare dashboard and the <code>name</code> field in your Wrangler configuration file, it will create a pull request to fix the conflict.</p>
<p>This can happen when:</p>
<ul>
<li>You rename your Worker in the dashboard but not in your config file</li>
<li>You connect a repository that was previously used with a different Worker</li>
<li>The <code>name</code> field in your config does not match the connected Worker</li>
</ul>
<p>The PR will update the <code>name</code> field in your Wrangler configuration to match the Worker name in the dashboard.</p>
<p>For more details, refer to the <a href="/changelog/2025-02-20-builds-name-conflict/">name conflict changelog</a>.</p>
<h2 id="reviewing-prs">Reviewing PRs</h2>
<p>When you receive a PR from Workers Builds:</p>
<ol>
<li><strong>Review the changes</strong> - Check that the configuration matches your project requirements</li>
<li><strong>Test the preview</strong> - Use the preview link in the PR description to verify everything works</li>
<li><strong>Merge when ready</strong> - Once satisfied, merge the PR to enable faster deployments</li>
</ol>
