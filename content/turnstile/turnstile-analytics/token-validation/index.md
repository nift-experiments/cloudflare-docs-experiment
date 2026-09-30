---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/
  description: View token validation metrics for your Turnstile widgets.
  full_title: Token validation · Cloudflare Turnstile docs
  head_html: <title>Token validation · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="View token validation metrics for your Turnstile widgets."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/index.md"><meta property="og:title" content="Token validation · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View token validation metrics for your Turnstile widgets."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/#page","headline":"Token validation \u00b7 Cloudflare Turnstile docs","description":"View token validation metrics for your Turnstile widgets.","url":"https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/turnstile-analytics/token-validation/
  schema: 1
---
<p>After a visitor successfully completes a Turnstile challenge, a token is generated and validated via the Siteverify API. Token validation data shows how many tokens your server validated successfully versus how many failed. A high rate of invalid tokens may indicate bot activity, expired tokens, or implementation issues.</p>
<p>For example, the token validation values in your analytics may look like this:</p>
<p><img src="/assets/upstream/images/turnstile/token-validation.png" alt="Token validation example values" title="Token validation example" /></p>
<h2 id="metrics">Metrics</h2>
<ul>
<li><strong>Siteverify requests</strong>: The total number of requests made to the Siteverify API in the given timeframe.</li>
<li><strong>Valid tokens</strong>: The number of Siteverify requests with <code>success:true</code> responses.</li>
<li><strong>Invalid tokens</strong>: The number of Siteverify requests with <code>success:false</code> responses.</li>
</ul>
<h3 id="call-siteverify">Call Siteverify</h3>
<p>It is important to <a href="/turnstile/get-started/server-side-validation/">call the Siteverify API</a>. Without calling Siteverify API to validate the tokens, your website or application is not protected. Skipping token validation means you cannot confirm the visitor's legitimacy.</p>
<ul>
<li>Tokens can only be redeemed once. Even valid tokens will return <code>success:false</code> if they are reused, preventing token theft and replay attacks.</li>
<li>Tokens expire after five minutes. Validation must occur within this window to be effective.</li>
<li>Tokens can be invalid. Bots might complete challenges, but Cloudflare can detect bot-like signals and mark the token as invalid.</li>
</ul>
