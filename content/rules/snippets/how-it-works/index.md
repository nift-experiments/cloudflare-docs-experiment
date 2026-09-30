---
cp9:
  canonical: https://developers.cloudflare.com/rules/snippets/how-it-works/
  description: How Snippets execute JavaScript at the edge for matching requests.
  full_title: How Snippets work · Cloudflare Rules docs
  head_html: <title>How Snippets work · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="How Snippets execute JavaScript at the edge for matching requests."><link rel="canonical" href="https://developers.cloudflare.com/rules/snippets/how-it-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/snippets/how-it-works/index.md"><meta property="og:title" content="How Snippets work · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Snippets execute JavaScript at the edge for matching requests."><meta property="og:url" content="https://developers.cloudflare.com/rules/snippets/how-it-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/snippets/how-it-works/#page","headline":"How Snippets work \u00b7 Cloudflare Rules docs","description":"How Snippets execute JavaScript at the edge for matching requests.","url":"https://developers.cloudflare.com/rules/snippets/how-it-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/snippets/how-it-works/
  schema: 1
---
<p>Cloudflare Snippets are executed based on rules defined within your zone. Here is how the process works:</p>
<p><img src="/assets/upstream/images/rules/snippets/snippets-execution.png" alt="Diagram of the snippets execution workflow" /></p>
<h2 id="1-evaluate-snippet-rules"><ol>
<li>Evaluate snippet rules</li>
</ol></h2>
<p>For each incoming request, Cloudflare evaluates the expression of every snippet rule defined in the zone. The evaluation checks for a match based on various request properties (such as bot score, WAF attack score, country of origin, and cookies).</p>
<h2 id="2-build-snippets-table"><ol start="2">
<li>Build Snippets table</li>
</ol></h2>
<p>For every snippet rule in a zone that matches an incoming request, Cloudflare adds the corresponding unique snippet ID to a Snippets table.</p>
<h2 id="3-execute-snippets-code"><ol start="3">
<li>Execute snippets code</li>
</ol></h2>
<p>Once all the rules have been evaluated and the full table has been compiled, Cloudflare starts processing all the snippet IDs in the table.</p>
<p>The snippets are executed sequentially. Each snippet receives the modified request from the previous snippet and applies new modifications to it.</p>
<h2 id="4-continue-with-the-request-execution-workflow"><ol start="4">
<li>Continue with the request execution workflow</li>
</ol></h2>
<p>After executing the final snippet IDs, the resulting modified request is passed back to the request execution workflow. Refer to <a href="/rules/snippets/#execution-order">Execution order</a> for more information on the Rules features evaluated before and after Cloudflare Snippets.</p>
