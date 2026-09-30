---
cp9:
  canonical: https://developers.cloudflare.com/agents/platform/limits/
  description: Understand the concurrency, storage, and compute time limits that apply to Cloudflare Agents.
  full_title: Limits · Cloudflare Agents docs
  head_html: <title>Limits · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand the concurrency, storage, and compute time limits that apply to Cloudflare Agents."><link rel="canonical" href="https://developers.cloudflare.com/agents/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the concurrency, storage, and compute time limits that apply to Cloudflare Agents."><meta property="og:url" content="https://developers.cloudflare.com/agents/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Agents docs","description":"Understand the concurrency, storage, and compute time limits that apply to Cloudflare Agents.","url":"https://developers.cloudflare.com/agents/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/platform/limits/
  schema: 1
---
<p>Limits that apply to authoring, deploying, and running Agents are detailed below.</p>
<p>Many limits are inherited from those applied to Workers scripts and/or Durable Objects, and are detailed in the <a href="/workers/platform/limits/">Workers limits</a> documentation.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Max concurrent (running) Agents per account</td>
<td>Tens of millions+ <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Max definitions per account</td>
<td>~250,000+ <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Max state stored per unique Agent</td>
<td>1 GB</td>
</tr>
<tr>
<td>Max compute time per Agent</td>
<td>30 seconds (refreshed per HTTP request / incoming WebSocket message) <sup><a href="#footnote-3">3</a></sup></td>
</tr>
<tr>
<td>Duration (wall clock) per step <sup><a href="#footnote-3">3</a></sup></td>
<td>Unlimited (for example, waiting on a database call or an LLM response)</td>
</tr>
</tbody>
</table>
<hr />
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/1860.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Yes, really. You can have tens of millions of Agents running concurrently, as each Agent is mapped to a [unique Durable Object](/durable-objects/concepts/what-are-durable-objects/) (actor).</li>
<li id="footnote-2">You can deploy up to [500 scripts per account](/workers/platform/limits/), but each script (project) can define multiple Agents. Each deployed script can be up to 10 MB on the [Workers Paid Plan](/workers/platform/pricing/#workers)</li>
<li id="footnote-3">Compute (CPU) time per Agent is limited to 30 seconds, but this is refreshed when an Agent receives a new HTTP request, runs a [scheduled task](/agents/runtime/execution/schedule-tasks/), or an incoming WebSocket message.</li></ol></section>
