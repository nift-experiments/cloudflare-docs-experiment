---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/
  description: Use AI Crawl Control alongside bot management.
  full_title: AI Crawl Control with Cloudflare Bots · Cloudflare AI Crawl Control docs
  head_html: <title>AI Crawl Control with Cloudflare Bots · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Use AI Crawl Control alongside bot management."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/index.md"><meta property="og:title" content="AI Crawl Control with Cloudflare Bots · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use AI Crawl Control alongside bot management."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/#page","headline":"AI Crawl Control with Cloudflare Bots \u00b7 Cloudflare AI Crawl Control docs","description":"Use AI Crawl Control alongside bot management.","url":"https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/configuration/ai-crawl-control-with-bots/
  schema: 1
---
<p>AI Crawl Control works alongside other Cloudflare products, such as Cloudflare <a href="/bots/">bot solutions</a>. Bot solutions identifies traffic matching patterns of known bots, and can challenge or block the bots as you wish.</p>
<h2 id="order-of-precedence">Order of precedence</h2>
<ul>
<li>AI Crawl Control's AI crawler blocking uses <a href="/waf/custom-rules/">WAF custom rules</a>, which take place before Cloudflare bot solutions.</li>
<li>AI Crawl Control's pay per crawl takes place after Cloudflare bot solutions.</li>
</ul>
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;A[Traffic] --&gt; B[WAF custom rules&lt;br&gt;AI Crawl Control: Crawler blocks]&#10;B --&gt; C[Cloudflare&lt;br&gt;Bot Solutions]&#10;C --&gt; D[AI Crawl Control:&lt;br&gt;Pay Per Crawl]&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>For more information on how Cloudflare classifies bot traffic, refer to <a href="/bots/concepts/bot/#ai-bots">AI bots</a>.</p>
<h2 id="examples">Examples</h2>
<p>Consider the following examples.</p>
<h3 id="bot-rule-which-blocks-all-ai-bots-vs-pay-per-crawl">Bot rule which blocks all AI bots vs pay per crawl</h3>
<p>You may have both of the following enabled:</p>
<ul>
<li>A selection of AI crawlers to be charged through AI Crawl Control's pay per crawl</li>
<li>Bot configuration option to <a href="/bots/get-started/bot-fight-mode/#block-ai-bots">Block AI Bots</a>.</li>
</ul>
<p>Since pay per crawl happens after bot solutions, you need to first turn off <strong>Block AI Bots</strong> to ensure pay per crawl works as intended.</p>
