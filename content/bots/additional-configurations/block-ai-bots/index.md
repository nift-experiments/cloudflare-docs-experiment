---
cp9:
  canonical: https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/
  description: Block AI crawlers and scrapers from accessing your website content.
  full_title: Block AI Bots · Cloudflare bot solutions docs
  head_html: <title>Block AI Bots · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Block AI crawlers and scrapers from accessing your website content."><link rel="canonical" href="https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/index.md"><meta property="og:title" content="Block AI Bots · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block AI crawlers and scrapers from accessing your website content."><meta property="og:url" content="https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Bots"><meta name="pcx_tags" content="AI,Scraping"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/#page","headline":"Block AI Bots \u00b7 Cloudflare bot solutions docs","description":"Block AI crawlers and scrapers from accessing your website content.","url":"https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","Scraping"]}</script>
  markdown: true
  noindex: false
  route: /bots/additional-configurations/block-ai-bots/
  schema: 1
---
<h2 id="configure-ai-bot-policies">Configure AI bot policies</h2>
<h3 id="new-defaults-on-september-15-2026">New defaults on September 15, 2026</h3>
<p>On September 15, 2026, Cloudflare will set updated defaults for new domains: bots classified as Training or as Agent will be blocked on pages that display ads, and Search will remain allowed. Mixed-purpose crawlers that combine Search and Training will also be blocked by all configurations to block AI training, including the legacy &quot;Block AI bots&quot; option. Before September 15, all customers can <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/settings">opt out of these new defaults</a>.</p>
<p>All Cloudflare customers can choose to block AI bots and agents based on their behavior. Cloudflare offers presets for the most common AI behaviors to give customers the option to treat different AI use cases distinctly:</p>
<ul>
<li><strong>Search</strong>: crawlers that collect or index your content to answer questions about it later.</li>
<li><strong>Agent</strong>: automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents.</li>
<li><strong>Training</strong>: crawlers taking your content to train or fine-tune a model, including mixed-purpose crawlers that are used both for Training and for Search.</li>
</ul>
<p>Each blocking option will block Verified bots classified with that behavior, plus additional unverified bots that fall under these classifications.</p>
<p>Each setting includes three mitigation options:</p>
<ul>
<li><strong>Block (on all pages)</strong> - Issues the block across the entire zone.</li>
<li><strong>Block on pages with ads</strong> - Uses Cloudflare automated detection for pages that display ads on your zone to block only on those pages.</li>
<li><strong>Allow (do not block)</strong> - Does not add any blocking.</li>
</ul>
<p>To configure these policies, customers can go to <strong>Security Settings</strong> &gt; <strong>Configure AI bot policies</strong>.</p>
<h2 id="block-ai-bots-deprecating-on-september-15-2026">Block AI bots [Deprecating on September 15, 2026]</h2>
<p>This setting blocks verified bots that are classified as crawling for the purpose of AI training, as well as a number of unverified bots that behave similarly.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3540.md")
</aside>
<p>To configure this setting and set their preference for blocking mixed-purpose bots, customers can go to <strong>Security Settings</strong> &gt; <strong>Block AI bots</strong>.</p>
