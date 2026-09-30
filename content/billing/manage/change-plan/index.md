---
cp9:
  canonical: https://developers.cloudflare.com/billing/manage/change-plan/
  description: Upgrade or downgrade a domain's Cloudflare plan.
  full_title: Change domain plan · Cloudflare Billing docs
  head_html: <title>Change domain plan · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Upgrade or downgrade a domain&#x27;s Cloudflare plan."><link rel="canonical" href="https://developers.cloudflare.com/billing/manage/change-plan/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/manage/change-plan/index.md"><meta property="og:title" content="Change domain plan · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upgrade or downgrade a domain&#x27;s Cloudflare plan."><meta property="og:url" content="https://developers.cloudflare.com/billing/manage/change-plan/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/manage/change-plan/#page","headline":"Change domain plan \u00b7 Cloudflare Billing docs","description":"Upgrade or downgrade a domain's Cloudflare plan.","url":"https://developers.cloudflare.com/billing/manage/change-plan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/manage/change-plan/
  schema: 1
---
<p>Occasionally, you may want to upgrade or downgrade the plan associated with a specific Cloudflare domain.</p>
<h2 id="limitations">Limitations</h2>
<p>Only <a href="/fundamentals/manage-members/roles/#account-scoped-roles">Super Administrators</a> can manage changes to domain plans.</p>
<p>If you decide to downgrade or remove a domain, Cloudflare does not issue refunds. Refer to our <a href="/billing/understand/billing-policy/">billing policy</a> for more information.</p>
<p>Upgrades are processed immediately, but downgrades are not processed until the end of the billing period. You cannot upgrade if you have an unpaid invoice. When downgrading, you can continue using the higher plan's products until the new billing period begins.</p>
<p>If you downgrade your plan, your plan may have access to <a href="/rules/page-rules/">fewer Page Rules</a>. If you continue to use more page rules than is allowed by your plan limit, you may be charged for additional rules. Remove excess rules and <a href="/billing/manage/cancel-subscription/">cancel additional subscriptions</a> if you do not want to be charged.</p>
<p>The Enterprise App Sec Advanced and Enterprise App Sec Core plans cannot be downgraded without <a href="/support/contacting-cloudflare-support/">contacting Cloudflare</a>.</p>
<p>For additional help, refer to <a href="https://community.cloudflare.com/t/communitytip-page-rules-best-practices-when-downgrading-pro-to-free/305725">this Community thread</a>.</p>
<h2 id="change-plan-type">Change plan type</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3430.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3426.md")
</aside>
<h2 id="change-plan-duration">Change plan duration</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3434.md")
</div></div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/cancel-subscription/">Cancel subscriptions</a> — Cancel plans and add-ons</li>
<li><a href="/billing/understand/billing-policy/">Billing policy</a> — Refund policy and subscription terms</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — When upgrades and downgrades take effect</li>
</ul>
