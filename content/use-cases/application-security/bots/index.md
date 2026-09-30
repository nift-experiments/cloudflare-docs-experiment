---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/application-security/bots/
  description: Detect and block automated threats while allowing legitimate traffic.
  full_title: Stop malicious bots · Cloudflare use cases
  head_html: <title>Stop malicious bots · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Detect and block automated threats while allowing legitimate traffic."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/application-security/bots/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/application-security/bots/index.md"><meta property="og:title" content="Stop malicious bots · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect and block automated threats while allowing legitimate traffic."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/application-security/bots/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF,Bots,Turnstile"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/application-security/bots/#page","headline":"Stop malicious bots \u00b7 Cloudflare use cases","description":"Detect and block automated threats while allowing legitimate traffic.","url":"https://developers.cloudflare.com/use-cases/application-security/bots/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/application-security/bots/
  schema: 1
---
<p>Malicious bots perform credential stuffing, content scraping, and inventory hoarding. Cloudflare provides multiple tools to detect and block automated threats while allowing legitimate bots like search engine crawlers.</p>
<p>For a step-by-step workflow that combines these tools into a layered defense, refer to <a href="/use-cases/solutions/stop-malicious-bots/">Stop malicious bots while allowing legitimate traffic</a>.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="bot-fight-mode">Bot Fight Mode</h3>
<p>Baseline bot protection available on all plans, including Free. Challenges requests that match known bot patterns. <a href="/bots/get-started/bot-fight-mode/">Learn more about Bot Fight Mode</a>.</p>
<h3 id="super-bot-fight-mode">Super Bot Fight Mode</h3>
<p>Granular bot controls for Pro plans and above. Allows verified bots, configures per-category actions, and extends protection to static resources. <a href="/bots/get-started/super-bot-fight-mode/">Learn more about Super Bot Fight Mode</a>.</p>
<h3 id="bot-management">Bot Management</h3>
<p>Machine learning-powered bot detection for Enterprise with granular signal detections. Assigns a bot score from 1 (bot) to 99 (human) to every request, along with additional signals for more precise and customizable security rules. <a href="/bots/">Learn more about Bot Management</a>.</p>
<h3 id="turnstile">Turnstile</h3>
<p>Privacy-preserving challenge for forms and user interactions. Available on all plans at no cost. <a href="/turnstile/">Learn more about Turnstile</a>.</p>
<h3 id="waf-custom-rules">WAF custom rules</h3>
<p>Targeted rules that act on traffic signals including headers, request patterns, and <a href="/bots/reference/bot-management-variables/">bot management variables</a>. Available on all plans. <a href="/waf/custom-rules/">Learn more about custom rules</a>.</p>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/use-cases/solutions/stop-malicious-bots/">Stop malicious bots while allowing legitimate traffic</a> — layered defense guide covering all products above</li>
<li><a href="/bots/get-started/bot-fight-mode/">Enable Bot Fight Mode</a> — quickest single step (Free plan)</li>
<li><a href="/turnstile/get-started/">Add Turnstile to forms</a> — protect login and signup forms</li>
</ol>
