---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/
  description: Track Pay Per Crawl revenue and crawler activity.
  full_title: Monitor activity · Cloudflare AI Crawl Control docs
  head_html: <title>Monitor activity · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Track Pay Per Crawl revenue and crawler activity."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/index.md"><meta property="og:title" content="Monitor activity · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track Pay Per Crawl revenue and crawler activity."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/#page","headline":"Monitor activity \u00b7 Cloudflare AI Crawl Control docs","description":"Track Pay Per Crawl revenue and crawler activity.","url":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/
  schema: 1
---
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;A[Enable in&lt;br&gt;account settings] --&gt; B[Set a pay per &lt;br/&gt;crawl price ]&#10;B --&gt; C[Select crawlers&lt;br&gt;to charge]&#10;C --&gt; D[Monitor&lt;br&gt;activity]:::highlight&#10;D --&gt; E[Manage&lt;br&gt;payouts]&#10;classDef highlight fill:#F6821F,color:white&#10;&#10;click A &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/&quot;&#10;click B &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/&quot;&#10;click C &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/&quot;&#10;click E &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/&quot;&#10;</code></pre>
<p>After configuring pay per crawl, monitor crawler activity to understand how AI crawlers interact with your content, and track your earnings.</p>
<h2 id="view-crawler-activity">View crawler activity</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2761.md")
</div>
<p>The metrics help you understand:</p>
<ul>
<li>Which crawlers are accessing your content</li>
<li>How often they are being charged</li>
<li>Request patterns and trends</li>
<li>Robots.txt violations</li>
</ul>
<p>For detailed information about available metrics, refer to <a href="/ai-crawl-control/features/analyze-ai-traffic/#view-the-metrics-tab">View AI Crawl Control metrics</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="balance-visibility">Balance visibility</h3>
@markup("md", "content/.markup/bodies/2760.md")
</aside>
<h2 id="additional-considerations">Additional considerations</h2>
<h3 id="robots-txt-management">Robots.txt management</h3>
<p>Consider updating your <code>robots.txt</code> file to clearly indicate which pages should remain off-limits, even if AI crawlers are willing to pay for access.</p>
<h3 id="ongoing-optimization">Ongoing optimization</h3>
<p>Do the following to ensure you are using pay per crawl most effectively:</p>
<ul>
<li>Review crawler activity regularly to identify patterns</li>
<li>Adjust pricing based on demand and content value</li>
<li>Modify crawler actions (charge, allow, block) as needed</li>
<li>Monitor for any unusual or unwanted crawler behavior</li>
</ul>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/faq">Pay Per Crawl FAQs</a></li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a></li>
</ul>
