---
cp9:
  canonical: https://developers.cloudflare.com/bots/botbase/
  description: Browse Cloudflare's directory of all known bots and agents, with behavior-based classification, directly in the dashboard.
  full_title: BotBase · Cloudflare bot solutions docs
  head_html: <title>BotBase · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Browse Cloudflare&#x27;s directory of all known bots and agents, with behavior-based classification, directly in the dashboard."><link rel="canonical" href="https://developers.cloudflare.com/bots/botbase/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/botbase/index.md"><meta property="og:title" content="BotBase · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Browse Cloudflare&#x27;s directory of all known bots and agents, with behavior-based classification, directly in the dashboard."><meta property="og:url" content="https://developers.cloudflare.com/bots/botbase/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><meta name="pcx_tags" content="AI,Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/botbase/#page","headline":"BotBase \u00b7 Cloudflare bot solutions docs","description":"Browse Cloudflare's directory of all known bots and agents, with behavior-based classification, directly in the dashboard.","url":"https://developers.cloudflare.com/bots/botbase/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","Bots"]}</script>
  markdown: true
  noindex: false
  route: /bots/botbase/
  schema: 1
---
<p>BotBase is Cloudflare's directory of all known bots, including <a href="/bots/concepts/bot/verified-bots/">verified bots and agents</a>. It provides a comprehensive, searchable view of the entire bot directory directly in the Cloudflare dashboard, where you can see how Cloudflare classifies each bot and target individual bots in your security configuration.</p>
<p>BotBase currently serves as a visibility plane for tracked bots. To mitigate these bots, you can use <a href="/security/rules/">Security rules</a> or the <a href="/bots/concepts/bot/#ai-bots">AI traffic options</a>.</p>
<h2 id="availability">Availability</h2>
<p>BotBase is available to <a href="/bots/get-started/bot-management/">Enterprise Bot Management</a> customers.</p>
<h2 id="access">Access</h2>
<p>To view BotBase, go to <strong>Security Analytics</strong> &gt; <strong>Bot analysis</strong> &gt; <strong>BotBase</strong>. You can also access BotBase from <strong>Security Settings</strong> &gt; <strong>Bot Management</strong> &gt; <strong>BotBase</strong>.</p>
<h2 id="what-you-can-do">What you can do</h2>
<ul>
<li>Browse the full catalogue of all verified bots and agents, and see the behavior or behaviors each one is classified under.</li>
<li>Search and filter the directory to find a specific bot or group of bots.</li>
<li>Filter your own traffic to a specific bot to investigate its activity on your zone.</li>
<li>Copy a bot's detection ID to target it in <a href="/security/rules/">Security rules</a>.</li>
</ul>
<h2 id="requests">Requests</h2>
<p>The <strong>Requests</strong> column summarizes requests associated with each bot over the previous 24 hours and shows an hourly sparkline.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Successful</strong></td>
<td>Requests with an edge HTTP response status in the <code>2xx</code> or <code>3xx</code> range.</td>
</tr>
<tr>
<td><strong>Unsuccessful</strong></td>
<td>Requests with any other edge HTTP response status.</td>
</tr>
</tbody>
</table>
<p>These metrics describe HTTP response outcomes, not the mitigation that a website owner configured for a request. Unsuccessful requests can include errors returned by the origin, such as <code>404</code> and <code>5xx</code> responses.</p>
<p>To investigate a bot's traffic, select its row to open Security Analytics in a new tab filtered to that bot's detection ID. Expand a request in the request log to review the <strong>Mitigation</strong>, <strong>Edge status code</strong>, and <strong>Origin status code</strong> fields.</p>
<h2 id="classification">Classification</h2>
<p>BotBase classifies each tracked bot by its behavior — what the bot may do on your site. A single bot can have one or more behaviors. To read more, see <a href="/bots/concepts/bot/verified-bots/">Verified bot classifications</a>.</p>
<h2 id="radar-s-public-facing-botbase">Radar's public-facing BotBase</h2>
<p>Every bot tracked in BotBase, along with select metadata, is available publicly in <a href="https://radar.cloudflare.com/bots/directory">Cloudflare Radar's bots and agents directory</a>.</p>
