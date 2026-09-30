---
cp9:
  canonical: https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/
  description: Verify bot identity by matching request IP addresses against published bot IP lists.
  full_title: IP validation · Cloudflare bot solutions docs
  head_html: <title>IP validation · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Verify bot identity by matching request IP addresses against published bot IP lists."><link rel="canonical" href="https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/index.md"><meta property="og:title" content="IP validation · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify bot identity by matching request IP addresses against published bot IP lists."><meta property="og:url" content="https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/#page","headline":"IP validation \u00b7 Cloudflare bot solutions docs","description":"Verify bot identity by matching request IP addresses against published bot IP lists.","url":"https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/reference/bot-verification/ip-validation/
  schema: 1
---
<p>The IP validation method aims to identify all of the IP addresses that a bot may use to send requests. IP validation is only used as a verification method for <a href="/bots/concepts/bot/verified-bots/">verified bots</a>.</p>
<p>Cloudflare can achieve this in two ways:</p>
<ul>
<li><strong>Using IP list provided by the bot owner</strong>: The bot owner can host a public list of IP ranges (for example, <a href="https://developers.google.com/static/search/apis/ipranges/googlebot.json">Googlebot's list</a>). Cloudflare fetches and uses this list directly for validation.</li>
<li><strong>Using Domain-based reverse DNS</strong>: The bot owner can provide a domain (or set of domains) that their bot requests originate from. Cloudflare collects the IP addresses observed in the requests with the bot's user agent, and performs reverse DNS lookups. If the reverse DNS of an IP resolves to one of the provided domains, Cloudflare considers it valid and stores it.</li>
</ul>
<h2 id="public-ip-list">Public IP List</h2>
<p>To verify a bot using a public IP list, you need to provide:</p>
<ul>
<li>A fixed and limited set of IP addresses, which can be verified via publicly accessible plain-text, <code>JSON</code>, or <code>CSV</code>.</li>
<li>IP addresses used solely by the bot owner.</li>
<li>A user-agent match pattern.</li>
</ul>
<h2 id="reverse-dns">Reverse DNS</h2>
<p>To verify a bot using reverse DNS, you need to provide:</p>
<ul>
<li>A list of domain suffixes to validate DNS records.</li>
<li>IP addresses should have PTR records set correctly.</li>
<li>A user-agent match pattern.</li>
</ul>
<h2 id="generic-user-agents">Generic user-agents</h2>
<p>User-agent patterns that match generic user-agents will be rejected by the Verified Bots API. When you add a user-agent pattern that is considered very common to the Verified Bot form, you may encounter an error message that will prompt you to correct the user-agent before you can submit again.</p>
<p>Generic user-agents include:</p>
<ul>
<li><code>Dart</code></li>
<li><code>Go-http-client</code></li>
<li><code>GuzzleHttp</code></li>
<li><code>Google Chrome</code></li>
<li><code>Mozilla Firefox</code></li>
<li><code>Safari</code></li>
<li><code>Nessus</code></li>
<li><code>Websocket++</code></li>
<li><code>cloudflare-go</code></li>
<li><code>fasthttp</code></li>
<li><code>got</code></li>
<li><code>nginx-ssl early hints</code></li>
<li><code>node</code></li>
<li><code>node-fetch</code></li>
<li><code>okhttp</code></li>
<li><code>python-requests</code></li>
<li><code>uTorrent</code></li>
</ul>
