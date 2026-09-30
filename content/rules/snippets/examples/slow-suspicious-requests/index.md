---
cp9:
  canonical: https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/
  description: Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score.
  full_title: Slow down suspicious requests · Cloudflare Rules docs
  head_html: <title>Slow down suspicious requests · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score."><link rel="canonical" href="https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/index.md"><meta property="og:title" content="Slow down suspicious requests · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score."><meta property="og:url" content="https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Snippets"><meta name="pcx_tags" content="Request modification"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/#page","headline":"Slow down suspicious requests \u00b7 Cloudflare Rules docs","description":"Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score.","url":"https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Request modification"]}</script>
  markdown: true
  noindex: false
  route: /rules/snippets/examples/slow-suspicious-requests/
  schema: 1
---
<p class="article-summary">Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score.</p>
<h2 id="snippet-code">Snippet code</h2>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request) {&#10;		// Define delay&#10;		const delay_in_seconds = 5;&#10;		// Introduce a delay&#10;		await new Promise((resolve) =&gt;&#10;			setTimeout(resolve, delay_in_seconds * 1000),&#10;		); // Set delay in milliseconds&#10;&#10;		// Pass the request to the origin&#10;		const response = await fetch(request);&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<h2 id="snippet-rule">Snippet rule</h2>
<p>Configure a custom filter expression:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bot Score</td>
<td>less than</td>
<td><code>10</code></td>
</tr>
</tbody>
</table>
<p>If you are using the Expression Editor, enter the following expression:</p>
<pre tabindex="0"><code class="language-txt">(cf.bot_management.score lt 10)&#10;</code></pre>
