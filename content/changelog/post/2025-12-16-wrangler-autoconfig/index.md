---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/
  description: New updates and improvements at Cloudflare.
  full_title: Configure your framework for Cloudflare automatically · Changelog
  head_html: <title>Configure your framework for Cloudflare automatically · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Configure your framework for Cloudflare automatically · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/#page","headline":"Configure your framework for Cloudflare automatically \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-12-16-wrangler-autoconfig/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 16, 2025</time><h2 id="post-title">Configure your framework for Cloudflare automatically</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports automatic configuration for popular web frameworks in experimental mode, making it even easier to deploy to Cloudflare Workers.</p>
<p>Previously, if you wanted to deploy an application using a popular web framework like Next.js or Astro, you had to follow tutorials to set up your application for deployment to Cloudflare Workers. This usually involved creating a Wrangler file, installing adapters, or changing configuration options.</p>
<p>Now <code>wrangler deploy</code> does this for you. Starting with Wrangler 4.55, you can use <code>npx wrangler deploy --x-autoconfig</code> in the directory of any web application using one of the supported frameworks. Wrangler will then proceed to configure and deploy it to your Cloudflare account.</p>
<p>You can also configure your application without deploying it by using the new <code>npx wrangler setup</code> command. This enables you to easily review what changes we are making so your application is ready for Cloudflare Workers.</p>
<p>The following application frameworks are supported starting today:</p>
<ul>
<li>Next.js</li>
<li>Astro</li>
<li>Nuxt</li>
<li>TanStack Start</li>
<li>SolidStart</li>
<li>React Router</li>
<li>SvelteKit</li>
<li>Docusaurus</li>
<li>Qwik</li>
<li>Analog</li>
</ul>
<p>Automatic configuration also supports static sites by detecting the assets directory and build command. From a single index.html file to the output of a generator like Jekyll or Hugo, you can just run <code>npx wrangler deploy --x-autoconfig</code> to upload to Cloudflare.</p>
<p>We're really excited to bring you automatic configuration so you can do more with Workers. Please let us know if you run into challenges using this experimentally. We’ve opened a <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a> and would love to hear your feedback.</p>
</div></article></div>
