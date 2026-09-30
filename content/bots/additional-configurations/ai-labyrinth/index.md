---
cp9:
  canonical: https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/
  description: Trap unauthorized AI crawlers with invisible honeypot links to waste their resources.
  full_title: AI Labyrinth · Cloudflare bot solutions docs
  head_html: <title>AI Labyrinth · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Trap unauthorized AI crawlers with invisible honeypot links to waste their resources."><link rel="canonical" href="https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/index.md"><meta property="og:title" content="AI Labyrinth · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Trap unauthorized AI crawlers with invisible honeypot links to waste their resources."><meta property="og:url" content="https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Bots"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/#page","headline":"AI Labyrinth \u00b7 Cloudflare bot solutions docs","description":"Trap unauthorized AI crawlers with invisible honeypot links to waste their resources.","url":"https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /bots/additional-configurations/ai-labyrinth/
  schema: 1
---
<p>The AI Labyrinth adds invisible links on your webpage with specific <code>Nofollow</code> tags to block AI crawlers that do not adhere to the recommended guidelines and crawl without permission. AI crawlers that scrape your website content without permission will be stuck in a maze of never-ending links, and their details are recorded and used by all Cloudflare customers who choose to block <a href="/bots/concepts/bot/#ai-bots">AI bots</a>.</p>
<p>These links do not impact your search engine optimization (SEO) or your website's appearance, and are only seen by bots. AI bots that respect no-crawl instructions will safely ignore this honeypot.</p>
<h2 id="ai-labyrinth-in-security-analytics">AI Labyrinth in Security Analytics</h2>
<p>When AI Labyrinth is enabled, Cloudflare logs security events for AI Labyrinth under the <strong>AI Labyrinth</strong> service. The following actions describe what happened to the request:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AI Labyrinth Served</strong></td>
<td>Cloudflare injected AI Labyrinth honeypot links into the HTML response.</td>
</tr>
<tr>
<td><strong>AI Labyrinth Crawls</strong></td>
<td>A crawler followed one of the injected honeypot links and entered the maze.</td>
</tr>
</tbody>
</table>
<p>AI Labyrinth actions are not mitigations. Cloudflare does not block or challenge the request.</p>
<p>A high volume of <strong>AI Labyrinth Crawls</strong> relative to <strong>AI Labyrinth Served</strong> indicates that non-compliant AI crawlers are actively following the injected links.</p>
<p>You can view these events in <a href="/waf/analytics/security-analytics/">Security Analytics</a> and <a href="/waf/analytics/security-events/">Security Events</a>.</p>
<h3 id="after-you-turn-off-ai-labyrinth">After you turn off AI Labyrinth</h3>
<p>When you turn off AI Labyrinth, Cloudflare immediately stops injecting new honeypot links into your pages. However, links generated while the feature was on remain valid for a limited time. Cloudflare still serves labyrinth content for these links, so you may continue to see AI Labyrinth actions in Security Analytics and Security Events until the links expire. This is expected behavior and does not mean the feature is still on.</p>
<h2 id="enable-ai-labyrinth">Enable AI Labyrinth</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3541.md")
</div>
