---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/billing/
  description: '2026-07-20'
  full_title: billing changelog | Cloudflare Docs
  head_html: <title>billing changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-07-20"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/billing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="billing changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-07-20"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/billing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/billing/#page","headline":"billing changelog | Cloudflare Docs","description":"2026-07-20","url":"https://developers.cloudflare.com/changelog/product/billing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/billing/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="budget-alerts-now-on-by-default-for-pay-as-you-go-accounts"><a href="/changelog/post/2026-06-15-budget-alerts-default-on/">Budget alerts now on by default for Pay-as-you-go accounts</a></h2>
<p><em>2026-07-20</em></p>
<p>We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.</p>
<p>We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.</p>
<p>The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.</p>
<p>Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.</p>
<p>Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.</p>
<p>You can change the threshold, add additional alerts, or remove the default alert entirely from <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>, or from your Notifications settings. If you already configured your own budget alert, nothing changes.</p>
<p>Enterprise contract accounts are not in scope.</p>
<p>For more information, refer to the <a href="/billing/manage/budget-alerts/">Budget alerts documentation</a>.</p>


<h2 id="modernized-billing-profile-with-new-payment-options"><a href="/changelog/post/2026-05-21-modernised-billing-profile/">Modernized Billing Profile with new payment options</a></h2>
<p><em>2026-05-21</em></p>
<p>The <a href="/billing/get-started/update-billing-info/">Billing Profile</a> now has a modern UI and a single space that unifies billing information, payment method management and an enhanced subscriptions view under a single <strong>Subscriptions</strong> tab.</p>
<h4 id="2026-05-21-modernised-billing-profile-what-changed">What changed</h4>
<p>The <strong>Subscriptions</strong> tab brings billing information, payment method management, and your subscriptions together in one place. The payment management and <strong>Pay overdue balances</strong> flows now use the latest checkout as product purchase flows, so you can pay with Apple Pay, Google Pay, Link, and <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link</a> alongside cards and PayPal.</p>
<p>New cards complete 3D Secure authentication when the issuer requires it — for example, the EU under PSD2 and India under RBI.</p>
<p><img src="/assets/upstream/images/changelog/billing/2026-05-21-modernised-billing-profile.png" alt="Modernized Billing Profile with the Subscriptions tab" /></p>
<p>For details, refer to the <a href="/billing/">Billing Home</a> documentation.</p>



