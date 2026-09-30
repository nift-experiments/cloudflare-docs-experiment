---
cp9:
  canonical: https://developers.cloudflare.com/bots/concepts/bot/
  description: Automated software programs that interact with websites and APIs.
  full_title: Bots · Cloudflare bot solutions docs
  head_html: <title>Bots · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Automated software programs that interact with websites and APIs."><link rel="canonical" href="https://developers.cloudflare.com/bots/concepts/bot/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/concepts/bot/index.md"><meta property="og:title" content="Bots · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Automated software programs that interact with websites and APIs."><meta property="og:url" content="https://developers.cloudflare.com/bots/concepts/bot/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/concepts/bot/#page","headline":"Bots \u00b7 Cloudflare bot solutions docs","description":"Automated software programs that interact with websites and APIs.","url":"https://developers.cloudflare.com/bots/concepts/bot/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /bots/concepts/bot/
  schema: 1
---
<p>A <strong>bot</strong> is a software application programmed to do certain tasks.</p>
<p>Bots can be used for good (chatbots, search engine crawlers) or for evil (inventory hoarding, credential stuffing).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="more-information">More information</h3>
@markup("md", "content/.markup/bodies/3560.md")
</aside>
<h2 id="ai-bots">AI bots</h2>
<p>AI crawlers and agents interact with your site for very different reasons, and you may want to treat those reasons differently. Rather than relying on a single &quot;AI bot&quot; label, Cloudflare classifies bots by <strong>behavior</strong> — what a bot does on your site — so you can allow the behavior that helps your business and block the behavior that harms it. A single bot can have more than one behavior.</p>
<h3 id="classification">Classification</h3>
<p>Cloudflare lets all customers manage three AI-related use cases directly:</p>
<table>
<thead>
<tr>
<th>Behavior</th>
<th>What it does</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Search</strong></td>
<td>Collects or indexes your content so it can answer questions about it later.</td>
</tr>
<tr>
<td><strong>Agent</strong></td>
<td>Automated activity acting in real time on a person's behalf to get something done, such as chat fetch bots and browser-use agents.</td>
</tr>
<tr>
<td><strong>Training</strong></td>
<td>Crawls your content to train or fine-tune a model, permanently absorbing your data into the model.</td>
</tr>
</tbody>
</table>
<p>Cloudflare classifies other behaviors, too — refer to <a href="/bots/concepts/bot/verified-bots/">Verified bots</a>.</p>
