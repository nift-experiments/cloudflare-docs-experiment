---
cp9:
  canonical: https://developers.cloudflare.com/billing/understand/billing-policy/
  description: Review refund policy, payment methods, and billing terms.
  full_title: Billing policy · Cloudflare Billing docs
  head_html: <title>Billing policy · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Review refund policy, payment methods, and billing terms."><link rel="canonical" href="https://developers.cloudflare.com/billing/understand/billing-policy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/understand/billing-policy/index.md"><meta property="og:title" content="Billing policy · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review refund policy, payment methods, and billing terms."><meta property="og:url" content="https://developers.cloudflare.com/billing/understand/billing-policy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/billing/understand/billing-policy/#page","headline":"Billing policy \u00b7 Cloudflare Billing docs","description":"Review refund policy, payment methods, and billing terms.","url":"https://developers.cloudflare.com/billing/understand/billing-policy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/understand/billing-policy/
  schema: 1
---
<p>Cloudflare plans are billed per domain on your account. Monthly plans are billed every 30 days and annual plans are billed yearly. Add-on services (also referred to as subscriptions) are billed monthly only.</p>
<p>Cloudflare also collects sales tax as governed by local laws. Sales taxes are computed based on the nine (9) digit postal code of either the shipping or billing address on file for your Cloudflare account where applicable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3381.md")
</aside>
<p>Cloudflare issues a separate invoice for plans and subscriptions (or add-on services) for every domain added to a Cloudflare account.</p>
<p>Cloudflare issues a monthly or annual invoice based on the plans you purchase. You will receive a $0 invoice even if your domain is on a Free plan.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3380.md")
</aside>
<p>For example, if test1.com and test2.com are added to the same Cloudflare account and upgraded to the Pro plan, you will receive an invoice with two charges. Subdomains such as blog.test1.com or blog.test2.com will not be included as billable domains.</p>
<p>The date you initiate a paid plan or add-on service will be both the start of your billing period and your <a href="/billing/manage/invoices/">invoice date</a>. For example, if you upgrade your plan on January 10, all future plan charges will be billed on the 10th of every month. Both dates are initialized using the UTC (Coordinated Universal Time) time zone, and not your local time zone.</p>
<p>If your account is dunned (downgraded and banned for non payment of dues), the new start date changes to the day of the upgrade and applies to monthly, yearly, and add-on plans.</p>
<p>When ordering a paid plan, subscription, or add-on service, you must agree to the following:</p>
<p><em>By clicking &quot;Enable&quot; you agree that you are purchasing a continuous month-to-month subscription which will automatically renew, and that the price of your selected subscription plan level and/or add on(s) will be billed to your designated payment method monthly as a recurring charge, unless you cancel your subscription(s), through your account dashboard,</em> <strong><em>before</em></strong> <em>the beginning of your next monthly billing period.</em></p>
<p><strong><em>You will be billed for the full monthly period in which you cancel and no refunds will be given. By purchasing a subscription, you agree to a minimum one month purchase obligation.</em></strong></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3379.md")
</aside>
<h2 id="upgrade-or-downgrade-cloudflare-paid-plans">Upgrade or downgrade Cloudflare paid plans</h2>
<p>If your domain is on a paid plan (for example, Pro) and you upgrade to a higher-priced plan (for example, Business),</p>
<ul>
<li>Your invoice will reflect the prorated cost of the higher-tiered plan, until the end of your billing cycle.</li>
<li>Cloudflare credits the prorated cost of the lower-priced plan, until the end of the billing cycle.</li>
<li>At the beginning of the next billing cycle, your invoice will reflect the full cost of the higher-priced plan.</li>
<li>Your bill cycle start and end dates are calculated using the UTC (Coordinated Universal Time) time zone, and not your local time zone.</li>
</ul>
<p>For example, if your billing date is January 1, but you upgrade from Pro to Business, on January 15,</p>
<ul>
<li>Your invoice will reflect the prorated Business plan rate for the period of use January 15 - January 30.</li>
<li>Cloudflare credits the prorated Pro plan cost from January 1 - January 15.</li>
<li>Your invoice for the billing period of January 1 - January 30 will appear in the Cloudflare dashboard on January 31.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3378.md")
</aside>
<p>If your domain is on a paid plan (for example, Business) and you downgrade to a lower-priced plan (for example, Pro),</p>
<ul>
<li>Your plan type and higher-tiered Cloudflare plan features are downgraded at the end of the current billing service period.</li>
<li>You are billed at the lower-tiered plan and feature rate for the next billing service period.</li>
</ul>
<p>For example, if your billing date is February 1, but you downgrade to Pro from the Business plan on February 15,</p>
<ul>
<li>You can access Business plan features and services until March 1.</li>
<li>Your March plan charges will reflect the downgraded cost.</li>
</ul>
<h2 id="billing-and-payment-for-enterprise-plans">Billing and payment for Enterprise plans</h2>
<p>Enterprise customers work with the Cloudflare account team to customize a plan and service contract to best suit their needs. The Cloudflare accounting team receives and processes Enterprise plan charges.</p>
<p>Enterprise account owners receive invoices directly from the Cloudflare accounting team.</p>
<h2 id="approved-payment-methods">Approved payment methods</h2>
<p>Cloudflare accepts the following payment methods:</p>
<ul>
<li>Visa</li>
<li>Mastercard</li>
<li>American Express</li>
<li>Discover</li>
<li>PayPal</li>
<li>Apple Pay</li>
<li>Google Pay</li>
<li>Stripe Link</li>
<li>UnionPay</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3377.md")
</aside>
<p>Ensure that you are using a valid payment method before changing your plan type or enabling subscriptions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3376.md")
</aside>
<h2 id="account-payment-method-preauthorization">Account Payment Method Preauthorization</h2>
<p>For services subject to usage-based billing, Cloudflare may preauthorize your credit card at any point in a billing period to confirm the payment method on file can cover accrued fees. This is a temporary hold and you will not be charged until the end of your billing period. If your payment method is validated, service will continue normally.</p>
<p>If your payment method fails, we may suspend your access to the usage-based billing services for which we conducted the preauthorization. In the case of <a href="/r2/">R2</a>, you will not be able to access your R2 buckets and requests will return errors, but your data will remain secure. If you do not update your payment method within 30 days, the data related to any usage-based billing service(s) may be deleted.</p>
<p>To regain access, you must settle any outstanding balances and pass preauthorization with a valid payment method. To update your primary payment method, go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Payment</strong>. Upon validation of your updated payment details, we will promptly reactivate your subscription(s), which will restore access to the relevant data and services.</p>
<p>For assistance, visit our <a href="https://support.cloudflare.com/hc/en-us">Support Portal</a> and submit a Billing request (category: “Payment issue”) to our Support team. They will assist you in verifying your updated payment information.</p>
<h2 id="non-refundable-occurrences">Non-refundable occurrences</h2>
<p>The following occurrences cannot be refunded:</p>
<ul>
<li>Billing or renewal issues: Often involves charges for renewals, unexpected billing, or issues related to subscription payments.</li>
<li>Accidental purchases of services and subscriptions: Includes instances where users bought the wrong service, made a mistake during the purchase process, or unintentionally upgraded their plan.</li>
<li>Domain issues: Incorrect domain registration, issues with domain transfers, or accidental domain purchases.</li>
<li>Service or plan issues: Issues with a service or plan itself, such as attempts to downgrade, cancel unused services, or problems with specific features.</li>
<li>Support issues: Unresolved support issues.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://www.cloudflare.com/terms/">Cloudflare Self-Serve Subscription Agreement</a></li>
<li><a href="/billing/manage/invoices/">Understanding Cloudflare Invoices</a></li>
<li><a href="/billing/understand/sales-tax/">Understanding Cloudflare sales tax</a></li>
</ul>
