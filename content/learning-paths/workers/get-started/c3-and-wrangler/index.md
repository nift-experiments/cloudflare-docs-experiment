---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/workers/get-started/c3-and-wrangler/
  description: Use C3 and Wrangler CLI for Workers.
  full_title: C3 & Wrangler · Cloudflare Learning Paths
  head_html: <title>C3 &amp; Wrangler · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Use C3 and Wrangler CLI for Workers."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/workers/get-started/c3-and-wrangler/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/workers/get-started/c3-and-wrangler/index.md"><meta property="og:title" content="C3 &amp; Wrangler · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use C3 and Wrangler CLI for Workers."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/workers/get-started/c3-and-wrangler/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/workers/get-started/c3-and-wrangler/#page","headline":"C3 & Wrangler \u00b7 Cloudflare Learning Paths","description":"Use C3 and Wrangler CLI for Workers.","url":"https://developers.cloudflare.com/learning-paths/workers/get-started/c3-and-wrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/workers/get-started/c3-and-wrangler/
  schema: 1
---
<p>Before deploying your first Worker, learn about the CLI tools you will use to build and deploy your Worker project.</p>
<h2 id="cloudflare-dashboard">Cloudflare dashboard</h2>
<p>You can build and develop your Worker on the Cloudflare dashboard, without needing to install and use C3 and Wrangler. Continue to the next page to get started with Workers on the Cloudflare dashboard.</p>
<h2 id="cli">CLI</h2>
<p>The Cloudflare Developer Platform ecosystem has two command-line interfaces (CLI):</p>
<ul>
<li>C3: To create new projects.</li>
<li>Wrangler: To build and deploy your projects.</li>
</ul>
<h2 id="c3">C3</h2>
<p><a href="/pages/get-started/c3/">C3</a> (<code>create-cloudflare</code> CLI) is a command-line tool designed to help you set up and deploy new applications to Cloudflare. In addition to speed, it leverages officially developed templates for Workers and framework-specific setup guides to ensure each new application that you set up follows Cloudflare and any third-party best practices for deployment on the Cloudflare network.</p>
<p>You will use C3 for new project creation.</p>
<h2 id="wrangler">Wrangler</h2>
<p><a href="/workers/wrangler/">Wrangler</a> is a command-line tool for building with Cloudflare developer products.</p>
<p>With Wrangler, you can <a href="/workers/wrangler/commands/general/#dev">develop</a> your Worker locally and remotely, <a href="/workers/wrangler/commands/general/#rollback">roll back</a> to a previous deployment of your Worker, <a href="/workers/wrangler/commands/general/#delete">delete</a> a Worker and its bound Developer Platform resources, and more. Refer to <a href="/workers/wrangler/commands/">Wrangler Commands</a> to view the full reference of Wrangler commands.</p>
<p>When you run C3 to create your project, C3 will install the latest version of Wrangler and you do not need to install Wrangler again. You can <a href="/workers/wrangler/install-and-update/#update-wrangler">update Wrangler</a> to a newer version in your project to access new Wrangler capabilities and features.</p>
<h2 id="source-of-truth">Source of truth</h2>
<p>If you are building your Worker on the Cloudflare dashboard, you will set up your project configuration (such as environment variables, bindings, and routes) through the dashboard. If you are building your project programmatically using C3 and Wrangler, you will rely on a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to configure your Worker.</p>
<p>Cloudflare recommends choosing and using one <a href="/workers/wrangler/configuration/#source-of-truth">source of truth</a>, the dashboard or the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, to avoid errors in your project.</p>
<h2 id="summary">Summary</h2>
<p>By reading this page, you have learned:</p>
<ul>
<li>How to use C3 to create new Workers and Pages projects.</li>
<li>How to use Wrangler to develop, configure, and delete your projects.</li>
</ul>
<p>In the next section, you will learn more about the Cloudflare dashboard before moving on to deploy your first Worker.</p>
