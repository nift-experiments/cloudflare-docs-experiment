---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/
  description: Limits & pricing for Workers Builds
  full_title: Limits & pricing · Cloudflare Workers docs
  head_html: <title>Limits &amp; pricing · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Limits &amp; pricing for Workers Builds"><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/index.md"><meta property="og:title" content="Limits &amp; pricing · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Limits &amp; pricing for Workers Builds"><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/#page","headline":"Limits & pricing \u00b7 Cloudflare Workers docs","description":"Limits & pricing for Workers Builds","url":"https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/limits-and-pricing/
  schema: 1
---
<p>Workers Builds has the following limits.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Free plan</th>
<th>Paid plans</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Build minutes</strong></td>
<td>3,000 per month</td>
<td>6,000 per month (then, +$0.005 per minute)</td>
</tr>
<tr>
<td><strong>Concurrent builds</strong></td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td><strong>Build timeout</strong></td>
<td>20 minutes</td>
<td>20 minutes</td>
</tr>
<tr>
<td><strong>Deploy Hooks</strong></td>
<td>10/min per Worker, 100/min per account</td>
<td>10/min per Worker, 100/min per account</td>
</tr>
<tr>
<td><strong>CPU</strong></td>
<td>2 vCPU</td>
<td>4 vCPU</td>
</tr>
<tr>
<td><strong>Memory</strong></td>
<td>8 GB</td>
<td>8 GB</td>
</tr>
<tr>
<td><strong>Disk space</strong></td>
<td>20 GB</td>
<td>20 GB</td>
</tr>
<tr>
<td><strong>Environment variables</strong></td>
<td>64</td>
<td>64</td>
</tr>
<tr>
<td><strong>Size per environment variable</strong></td>
<td>5 KB</td>
<td>5 KB</td>
</tr>
</tbody>
</table>
<h2 id="definitions">Definitions</h2>
<ul>
<li><strong>Build minutes</strong>: The number of minutes that it takes to build a project.</li>
<li><strong>Concurrent builds</strong>: The number of builds that can run in parallel across an account.</li>
<li><strong>Build timeout</strong>: The amount of time that a build can be run before it is terminated.</li>
<li><strong>Deploy Hooks</strong>: The rate limit for builds triggered by <a href="/workers/ci-cd/builds/deploy-hooks/">Deploy Hooks</a>.</li>
<li><strong>vCPU</strong>: The number of CPU cores available to your build.</li>
<li><strong>Memory</strong>: The amount of memory available to your build.</li>
<li><strong>Disk space</strong>: The amount of disk space available to your build.</li>
<li><strong>Environment variables</strong>: The number of custom environment variables you can configure per Worker.</li>
<li><strong>Size per environment variable</strong>: The maximum size for each individual environment variable.</li>
</ul>
