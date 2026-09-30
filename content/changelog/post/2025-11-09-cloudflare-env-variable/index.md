---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/
  description: New updates and improvements at Cloudflare.
  full_title: Select Wrangler environments using the CLOUDFLARE_ENV environment variable · Changelog
  head_html: <title>Select Wrangler environments using the CLOUDFLARE_ENV environment variable · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Select Wrangler environments using the CLOUDFLARE_ENV environment variable · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/#page","headline":"Select Wrangler environments using the CLOUDFLARE_ENV environment variable \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-09-cloudflare-env-variable/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 9, 2025</time><h2 id="post-title">Select Wrangler environments using the CLOUDFLARE_ENV environment variable</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports using the <code>CLOUDFLARE_ENV</code> <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables">environment variable</a> to select the active <a href="/workers/wrangler/environments/">environment</a> for your Worker commands. This provides a more flexible way to manage environments, especially when working with build tools and CI/CD pipelines.</p>
<h4 id="what-s-new">What's new</h4>
<p><strong>Environment selection via environment variable:</strong></p>
<ul>
<li>Set <code>CLOUDFLARE_ENV</code> to specify which environment to use for Wrangler commands</li>
<li>Works with all Wrangler commands that support the <code>--env</code> flag</li>
<li>The <code>--env</code> command line argument takes precedence over the <code>CLOUDFLARE_ENV</code> environment variable</li>
</ul>
<h4 id="example-usage">Example usage</h4>
<pre tabindex="0"><code class="language-bash">&#35; Deploy to the production environment using CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=production wrangler deploy&#10;&#10;&#35; Upload a version to the staging environment&#10;CLOUDFLARE_ENV=staging wrangler versions upload&#10;&#10;&#35; The --env flag takes precedence over CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=dev wrangler deploy --env production&#10;&#35; This will deploy to production, not dev&#10;</code></pre>
<h4 id="use-with-build-tools">Use with build tools</h4>
<p>The <code>CLOUDFLARE_ENV</code> environment variable is particularly useful when working with build tools like Vite. You can set the environment once during the build process, and it will be used for both building and deploying your Worker:</p>
<pre tabindex="0"><code class="language-bash">&#35; Set the environment for both build and deploy&#10;CLOUDFLARE_ENV=production npm run build &amp; wrangler deploy&#10;</code></pre>
<p>When using <code>@cloudflare/vite-plugin</code>, the build process generates a <a href="/workers/wrangler/configuration/#generated-wrangler-configuration">&quot;redirected deploy config&quot;</a> that is flattened to only contain the active environment. Wrangler will validate that the environment specified matches the environment used during the build to prevent accidentally deploying a Worker built for one environment to a different environment.</p>
<h4 id="learn-more">Learn more</h4>
<ul>
<li><a href="/workers/wrangler/system-environment-variables/">System environment variables</a></li>
<li><a href="/workers/wrangler/environments/">Environments</a></li>
</ul>
</div></article></div>
