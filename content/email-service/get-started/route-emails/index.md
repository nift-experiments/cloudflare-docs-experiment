---
cp9:
  canonical: https://developers.cloudflare.com/email-service/get-started/route-emails/
  description: Forward incoming emails to existing mailboxes or process them with Workers using Email Service.
  full_title: Route emails · Cloudflare Email Service docs
  head_html: <title>Route emails · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Forward incoming emails to existing mailboxes or process them with Workers using Email Service."><link rel="canonical" href="https://developers.cloudflare.com/email-service/get-started/route-emails/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/get-started/route-emails/index.md"><meta property="og:title" content="Route emails · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Forward incoming emails to existing mailboxes or process them with Workers using Email Service."><meta property="og:url" content="https://developers.cloudflare.com/email-service/get-started/route-emails/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/get-started/route-emails/#page","headline":"Route emails \u00b7 Cloudflare Email Service docs","description":"Forward incoming emails to existing mailboxes or process them with Workers using Email Service.","url":"https://developers.cloudflare.com/email-service/get-started/route-emails/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/get-started/route-emails/
  schema: 1
---
<p class="article-summary">Set up email routing to forward incoming emails to existing mailboxes or process them with Workers.
</p>
<p>Route incoming emails sent to your domain to existing mailboxes, Workers for processing, or other destinations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8606.md")
</aside>
<h2 id="set-up-your-domain">Set up your domain</h2>
<p>Before using Email Routing, configure your domain.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Onboard Domain</strong>.</p>
</li>
<li>
<p>Choose a domain from your Cloudflare account. Optionally review the DNS records that Cloudflare will add to your root domain:</p>
<ul>
<li>MX records to route incoming emails to Cloudflare.</li>
<li>TXT record for SPF to authorize email routing.</li>
<li>TXT record for DKIM to provide authentication for routed emails.</li>
</ul>
</li>
<li>
<p>Select <strong>Done</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8605.md")
</aside>
<p>Once your domain is onboarded, you can start routing emails.</p>
<h2 id="route-your-first-email">Route your first email</h2>
<p>You can route your first email by setting up routing rules in the dashboard, or by processing emails with Workers.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8610.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<p>Now that you can route emails, explore advanced features:</p>
<ul>
<li><strong><a href="/email-service/get-started/send-emails/">Send outbound emails</a></strong> - Send emails from your applications</li>
<li><strong><a href="/email-service/api/route-emails/">API reference</a></strong> - Complete routing API documentation</li>
<li><strong><a href="/email-service/examples/">Examples</a></strong> - Real-world routing patterns</li>
</ul>
