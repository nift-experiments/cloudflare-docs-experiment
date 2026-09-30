---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/
  description: Use [Workers Static Assets](/workers/static-assets/) to host full-stack applications instead of Workers Sites. Do not use Workers Sites for new projects.
  full_title: Workers Sites · Cloudflare Workers docs
  head_html: <title>Workers Sites · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use [Workers Static Assets](/workers/static-assets/) to host full-stack applications instead of Workers Sites. Do not use Workers Sites for new projects."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/sites/index.md"><meta property="og:title" content="Workers Sites · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use [Workers Static Assets](/workers/static-assets/) to host full-stack applications instead of Workers Sites. Do not use Workers Sites for new projects."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/sites/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/static-assets/#page","headline":"Workers Sites \u00b7 Cloudflare Workers docs","description":"Use Workers Static Assets to host full-stack applications instead of Workers Sites. Do not use Workers Sites for new projects.","url":"https://developers.cloudflare.com/workers/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/sites/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16813.md")
</aside>
<p>Workers Sites enables developers to deploy static applications directly to Workers. It can be used for deploying applications built with static site generators like <a href="https://gohugo.io">Hugo</a> and <a href="https://www.gatsbyjs.org">Gatsby</a>, or front-end frameworks like <a href="https://vuejs.org">Vue</a> and <a href="https://reactjs.org">React</a>.</p>
<p>To deploy with Workers Sites, select from one of these three approaches depending on the state of your target project:</p>
<hr />
<h2 id="1-start-from-scratch"><ol>
<li>Start from scratch</li>
</ol></h2>
<p>If you are ready to start a brand new project, this quick start guide will help you set up the infrastructure to deploy a HTML website to Workers.</p>
<p><a class="nb-link-button" href="/workers/configuration/sites/start-from-scratch/">Start from scratch</a></p>
<hr />
<h2 id="2-deploy-an-existing-static-site"><ol start="2">
<li>Deploy an existing static site</li>
</ol></h2>
<p>If you have an existing project or static assets that you want to deploy with Workers, this quick start guide will help you install Wrangler and configure Workers Sites for your project.</p>
<p><a class="nb-link-button" href="/workers/configuration/sites/start-from-existing/">Start from an existing static site</a></p>
<hr />
<h2 id="3-add-static-assets-to-an-existing-workers-project"><ol start="3">
<li>Add static assets to an existing Workers project</li>
</ol></h2>
<p>If you already have a Worker deployed to Cloudflare, this quick start guide will show you how to configure the existing codebase to use Workers Sites.</p>
<p><a class="nb-link-button" href="/workers/configuration/sites/start-from-worker/">Start from an existing Worker</a></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16812.md")
</aside>
