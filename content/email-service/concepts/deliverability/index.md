---
cp9:
  canonical: https://developers.cloudflare.com/email-service/concepts/deliverability/
  description: Understand bounce handling and reputation management for optimal email delivery with Email Service.
  full_title: Email deliverability · Cloudflare Email Service docs
  head_html: <title>Email deliverability · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand bounce handling and reputation management for optimal email delivery with Email Service."><link rel="canonical" href="https://developers.cloudflare.com/email-service/concepts/deliverability/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/concepts/deliverability/index.md"><meta property="og:title" content="Email deliverability · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand bounce handling and reputation management for optimal email delivery with Email Service."><meta property="og:url" content="https://developers.cloudflare.com/email-service/concepts/deliverability/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/concepts/deliverability/#page","headline":"Email deliverability \u00b7 Cloudflare Email Service docs","description":"Understand bounce handling and reputation management for optimal email delivery with Email Service.","url":"https://developers.cloudflare.com/email-service/concepts/deliverability/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/concepts/deliverability/
  schema: 1
---
<p class="article-summary">Understand bounce handling and reputation management for optimal email delivery.</p>
<p>When you send an email, there is no guarantee it reaches the recipient's inbox. Inbox providers like Gmail, Yahoo, Outlook, and iCloud invest heavily in filtering out unwanted email. If you send poorly targeted emails, have high bounce rates, or trigger spam complaints, these providers may flag your domain as untrustworthy. Once that happens, even your legitimate emails can end up in spam or be blocked outright.</p>
<p>This concept is referred to as email deliverability: maintaining a healthy sending reputation so that inbox providers trust your emails. Cloudflare Email Service helps with this by automatically handling bounces, managing suppression lists, and authenticating your emails through SPF, DKIM, and DMARC.</p>
<h2 id="bounces">Bounces</h2>
<p>Bounces occur when emails cannot be delivered to recipients. There are two types of bounces: <strong>hard bounces</strong> and <strong>soft bounces</strong>.</p>
<h3 id="hard-bounces">Hard bounces</h3>
<p>Hard bounces are permanent delivery failures that occur when:</p>
<ul>
<li>The recipient address does not exist.</li>
<li>The recipient domain does not exist.</li>
<li>The receiving server permanently rejects the recipient.</li>
</ul>
<p><strong>Hard bounces are never retried</strong> because the failure is permanent. Emails that hard bounce will generate a bounce notification to the sender address and can be monitored through <a href="/email-service/observability/metrics-analytics/">analytics</a>.</p>
<p>Email Service adds eligible recipient-side hard bounces to your <a href="/email-service/concepts/suppressions/">suppression list</a>. Suppressions have no expiration when the mailbox or domain does not exist.</p>
<p>They also have no expiration when the recipient remains unavailable across repeated delivery attempts. Other eligible hard-bounce suppressions last seven days.</p>
<h3 id="soft-bounces">Soft bounces</h3>
<p>Soft bounces are temporary failures that may succeed if retried:</p>
<ul>
<li>Recipient mailbox is full</li>
<li>Email server temporarily down</li>
<li>Rate limiting or greylisting</li>
</ul>
<p>Cloudflare automatically retries soft bounces with exponential backoff. Eligible recipient-side failures create a 24-hour suppression.</p>
<h2 id="reputation-management">Reputation management</h2>
<p>Cloudflare automatically manages:</p>
<ul>
<li><strong>IP reputation</strong>: Managed sending infrastructure optimized for deliverability</li>
<li><strong>Domain authentication</strong>: DKIM signing, SPF alignment, DMARC compliance</li>
<li><strong>Feedback processing</strong>: ISP complaint handling and suppression list management</li>
</ul>
<h3 id="best-practices">Best practices</h3>
<h4 id="content-and-list-hygiene">Content and list hygiene</h4>
<p>Avoid content that can trigger spam-detection or can be perceived as unwanted content:</p>
<ul>
<li>Avoid spam trigger words (FREE, URGENT, GUARANTEED)</li>
<li>Include both HTML and plain text versions</li>
<li>Use legitimate URLs and clear sender identification</li>
</ul>
<p>Ensure that your email lists are clean and contain intended recipients:</p>
<ul>
<li>Validate emails before sending</li>
<li>Implement double opt-in for subscriptions</li>
<li>Remove hard bounced addresses immediately</li>
</ul>
<p>Ensure that your deliverability stays above key metrics to avoid affecting your email sending reputation:</p>
<ul>
<li>Delivery rate &gt;95%</li>
<li>Hard bounce rate &lt; 2%</li>
<li>Complaint rate &lt; 0.1%</li>
</ul>
<h4 id="use-separate-domains-for-separate-purposes">Use separate domains for separate purposes</h4>
<p>Each domain builds its own deliverability reputation with inbox providers. Use separate domains or subdomains for different types of email so that one category does not affect the reputation of another. For example:</p>
<ul>
<li><code>notifications.yourdomain.com</code> for transactional emails (order confirmations, password resets)</li>
<li><code>marketing.yourdomain.com</code> for marketing and promotional emails</li>
<li><code>yourdomain.com</code> for important account-related communications</li>
</ul>
<p>This way, if marketing emails generate higher complaint rates, your transactional email deliverability is not impacted. Each domain can be onboarded separately through <a href="/email-service/configuration/domains/">domain configuration</a>.</p>
