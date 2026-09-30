---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/
  description: Set up continuous integration and continuous deployment for your Workers.
  full_title: CI/CD · Cloudflare Workers docs
  head_html: <title>CI/CD · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up continuous integration and continuous deployment for your Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/index.md"><meta property="og:title" content="CI/CD · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up continuous integration and continuous deployment for your Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/#page","headline":"CI/CD \u00b7 Cloudflare Workers docs","description":"Set up continuous integration and continuous deployment for your Workers.","url":"https://developers.cloudflare.com/workers/ci-cd/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/
  schema: 1
---
<p>You can set up continuous integration and continuous deployment (CI/CD) for your Workers by using either the integrated build system, <a href="#workers-builds">Workers Builds</a>, or using <a href="#external-cicd">external providers</a> to optimize your development workflow.</p>
<h2 id="why-use-ci-cd">Why use CI/CD?</h2>
<p>Using a CI/CD pipeline to deploy your Workers is a best practice because it:</p>
<ul>
<li>Automates the build and deployment process, removing the need for manual <code>wrangler deploy</code> commands.</li>
<li>Ensures consistent builds and deployments across your team by using the same source control management (SCM) system.</li>
<li>Reduces variability and errors by deploying in a uniform environment.</li>
<li>Simplifies managing access to production credentials.</li>
</ul>
<h2 id="which-ci-cd-should-i-use">Which CI/CD should I use?</h2>
<p>Choose <a href="/workers/ci-cd/builds">Workers Builds</a> if you want a fully integrated solution within Cloudflare's ecosystem that requires minimal setup and configuration for GitHub or GitLab users.</p>
<p>We recommend using <a href="/workers/ci-cd/external-cicd">external CI/CD providers</a> if:</p>
<ul>
<li>You have a self-hosted instance of GitHub or GitLabs, which is currently not supported in Workers Builds' <a href="/workers/ci-cd/builds/git-integration/">Git integration</a></li>
<li>You are using a Git provider that is not GitHub or GitLab</li>
</ul>
<h2 id="workers-builds">Workers Builds</h2>
<p><a href="/workers/ci-cd/builds">Workers Builds</a> is Cloudflare's native CI/CD system that allows you to integrate with GitHub or GitLab to automatically deploy changes with each new push to a selected branch (e.g. <code>main</code>).</p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/workers-builds-workflow.png" alt="Workers Builds Workflow Diagram" /></p>
<p>Ready to streamline your Workers deployments? Get started with <a href="/workers/ci-cd/builds/#get-started">Workers Builds</a>.</p>
<h2 id="external-ci-cd">External CI/CD</h2>
<p>You can also choose to set up your CI/CD pipeline with an external provider.</p>
<ul>
<li><a href="/workers/ci-cd/external-cicd/github-actions/">GitHub Actions</a></li>
<li><a href="/workers/ci-cd/external-cicd/gitlab-cicd/">GitLab CI/CD</a></li>
</ul>
