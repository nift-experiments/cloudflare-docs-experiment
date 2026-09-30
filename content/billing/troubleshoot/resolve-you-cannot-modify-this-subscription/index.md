---
cp9:
  canonical: https://developers.cloudflare.com/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/
  description: Fix errors when modifying a canceled subscription.
  full_title: Resolve "you cannot modify this subscription" · Cloudflare Billing docs
  head_html: <title>Resolve &quot;you cannot modify this subscription&quot; · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Fix errors when modifying a canceled subscription."><link rel="canonical" href="https://developers.cloudflare.com/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/index.md"><meta property="og:title" content="Resolve &quot;you cannot modify this subscription&quot; · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fix errors when modifying a canceled subscription."><meta property="og:url" content="https://developers.cloudflare.com/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/#page","headline":"Resolve \"you cannot modify this subscription\" \u00b7 Cloudflare Billing docs","description":"Fix errors when modifying a canceled subscription.","url":"https://developers.cloudflare.com/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/troubleshoot/resolve-you-cannot-modify-this-subscription/
  schema: 1
---
<p>When attempting to cancel or modify a subscription, you may see the following error message:</p>
<ul>
<li>&quot;This subscription is scheduled to be cancelled at the end of the billing period. To make changes or purchase more, please click 'Cancel Downgrade' on the Subscriptions page.&quot;</li>
</ul>
<h2 id="causes">Causes</h2>
<ul>
<li>You are attempting to cancel a subscription that is already scheduled for cancellation.</li>
<li>You are attempting to upgrade a subscription that is already scheduled for cancellation.</li>
</ul>
<h2 id="solutions">Solutions</h2>
<p>If you intended to cancel a subscription, no further action is required. Your subscription ends at the close of the current billing period. Use the steps below to find the exact date.</p>
<h3 id="find-the-cancellation-date">Find the cancellation date</h3>
<p>After requesting cancellation, the <strong>Subscriptions</strong> page shows the end date under <strong>Ending on</strong>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3386.md")
</div>
<h3 id="refunds-for-canceled-subscriptions">Refunds for canceled subscriptions</h3>
<p>Cloudflare does not issue refunds for canceled subscriptions. Instead, your subscription remains active until the end of the current billing period.</p>
<p>If you do not want to pay for the next billing period, cancel your subscription before the current billing period ends. You can find this date on the <strong>Subscriptions</strong> page by checking the renewal date, for example <strong>Renews on Aug 29, 2025</strong>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3387.md")
</div>
<h3 id="stop-the-cancellation">Stop the cancellation</h3>
<p>If you changed your decision and the cancellation has not taken effect yet, you can select <strong>Cancel Downgrade</strong> next to the appropriate subscription.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3388.md")
</div>
<h2 id="verify-the-fix">Verify the fix</h2>
<p>After you cancel the downgrade, return to the subscription and retry the change you originally attempted.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/cancel-subscription/">Cancel subscriptions</a> — How cancellations work</li>
<li><a href="/billing/understand/billing-policy/">Billing policy</a> — Refund policy and billing terms</li>
<li><a href="/billing/troubleshoot/error-reference/">Error reference</a> — Look up other billing error messages</li>
</ul>
