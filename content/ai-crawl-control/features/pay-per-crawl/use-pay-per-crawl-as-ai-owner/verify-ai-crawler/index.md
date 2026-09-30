---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/
  description: Verify your AI crawler identity for Pay Per Crawl.
  full_title: Verify your AI crawler · Cloudflare AI Crawl Control docs
  head_html: <title>Verify your AI crawler · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Verify your AI crawler identity for Pay Per Crawl."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/index.md"><meta property="og:title" content="Verify your AI crawler · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify your AI crawler identity for Pay Per Crawl."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/#page","headline":"Verify your AI crawler \u00b7 Cloudflare AI Crawl Control docs","description":"Verify your AI crawler identity for Pay Per Crawl.","url":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/
  schema: 1
---
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;A[Set up your&lt;br&gt;Cloudflare Account] --&gt; B[Verify your&lt;br&gt;AI crawler]:::highlight&#10;B --&gt; C[Discover&lt;br&gt;payable content]&#10;C --&gt; D[Connect to&lt;br&gt;Stripe]&#10;D --&gt; E[Crawl pages]&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>Once you have connected your Stripe account, set up your AI crawler as a <a href="/bots/concepts/bot/verified-bots/">verified bot</a>.</p>
<h2 id="content-access-restriction">Content access restriction</h2>
<p>When an AI crawler tries to access content protected by pay per crawl, it receives a HTTP status code 402. This indicates payment is required. The HTTP header of the response includes the cost of the content.</p>
<p>For example, the response header may look like below:</p>
<pre tabindex="0"><code>HTTP/2 402&#10;date: Fri, 06 Jun 2025 08:42:38 GMT&#10;content-type: text/plain; charset=utf-8&#10;crawler-price: USD 0.01&#10;server: cloudflare&#10;</code></pre>
<p>To access this content, you must verify your AI crawler.</p>
<h2 id="1-follow-web-bot-auth-protocol"><ol>
<li>Follow Web Bot Auth protocol</li>
</ol></h2>
<p>Ensure your AI crawler identifies itself with the required headers for Web Bot Auth.</p>
<p>Follow the steps found in <a href="/bots/reference/bot-verification/web-bot-auth/">Web Both Auth</a>.</p>
<h2 id="2-follow-verified-bot-policy"><ol start="2">
<li>Follow verified bot policy</li>
</ol></h2>
<p>Ensure your AI crawler follows Cloudflare's <a href="/bots/concepts/bot/verified-bots/">verified bots policy</a>.</p>
<h2 id="3-submit-verification-request"><ol start="3">
<li>Submit verification request</li>
</ol></h2>
<p>Submit a form to add your AI crawler to Cloudflare's list of verified bots.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2769.md")
</div>
