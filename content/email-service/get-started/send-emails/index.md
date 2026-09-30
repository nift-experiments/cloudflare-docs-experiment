---
cp9:
  canonical: https://developers.cloudflare.com/email-service/get-started/send-emails/
  description: Send your first email using the Cloudflare Email Service Workers binding, REST API, or SMTP.
  full_title: Send emails · Cloudflare Email Service docs
  head_html: <title>Send emails · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Send your first email using the Cloudflare Email Service Workers binding, REST API, or SMTP."><link rel="canonical" href="https://developers.cloudflare.com/email-service/get-started/send-emails/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/get-started/send-emails/index.md"><meta property="og:title" content="Send emails · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send your first email using the Cloudflare Email Service Workers binding, REST API, or SMTP."><meta property="og:url" content="https://developers.cloudflare.com/email-service/get-started/send-emails/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/get-started/send-emails/#page","headline":"Send emails \u00b7 Cloudflare Email Service docs","description":"Send your first email using the Cloudflare Email Service Workers binding, REST API, or SMTP.","url":"https://developers.cloudflare.com/email-service/get-started/send-emails/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/get-started/send-emails/
  schema: 1
---
<p class="article-summary">Send your first email using the Workers binding, the REST API, or SMTP.
</p>
<p>Send emails from your applications using Cloudflare Email Service. You can use the <strong>Workers binding</strong> for applications built on Cloudflare Workers, the <strong>REST API</strong> from any platform, or <strong>SMTP</strong> from any SMTP-capable application or mail client.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8598.md")
</aside>
<h2 id="set-up-your-domain">Set up your domain</h2>
<p>Before using Email Sending, configure your domain.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Sending</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Onboard Domain</strong>.</p>
</li>
<li>
<p>Choose a domain from your Cloudflare account. Optionally review the DNS records that Cloudflare will add to the <code>cf-bounce</code> subdomain of your domain:</p>
<ul>
<li>MX records to route bounce emails to Cloudflare.</li>
<li>TXT record for SPF to authorize sending emails.</li>
<li>TXT record for DKIM to provide authentication for emails sent from your domain.</li>
<li>TXT record for DMARC on <code>_dmarc.yourdomain.com</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Done</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8597.md")
</aside>
<p>Once your domain is onboarded, you can start sending emails.</p>
<h2 id="send-your-first-email">Send your first email</h2>
<p>You can send your first email using the Workers binding, the REST API, or SMTP.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8603.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<p>Now that you can send emails, explore advanced features:</p>
<ul>
<li><strong><a href="/email-service/get-started/route-emails/">Route incoming emails</a></strong> - Process emails sent to your domain</li>
<li><strong><a href="/email-service/api/send-emails/">API reference</a></strong> - Complete API documentation</li>
<li><strong><a href="/email-service/examples/">Examples</a></strong> - Real-world implementation patterns</li>
</ul>
