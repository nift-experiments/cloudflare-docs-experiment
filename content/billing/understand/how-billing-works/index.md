---
cp9:
  canonical: https://developers.cloudflare.com/billing/understand/how-billing-works/
  description: Billing lifecycle, charge types, and invoice details.
  full_title: How Cloudflare billing works · Cloudflare Billing docs
  head_html: <title>How Cloudflare billing works · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Billing lifecycle, charge types, and invoice details."><link rel="canonical" href="https://developers.cloudflare.com/billing/understand/how-billing-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/understand/how-billing-works/index.md"><meta property="og:title" content="How Cloudflare billing works · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Billing lifecycle, charge types, and invoice details."><meta property="og:url" content="https://developers.cloudflare.com/billing/understand/how-billing-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/understand/how-billing-works/#page","headline":"How Cloudflare billing works \u00b7 Cloudflare Billing docs","description":"Billing lifecycle, charge types, and invoice details.","url":"https://developers.cloudflare.com/billing/understand/how-billing-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/understand/how-billing-works/
  schema: 1
---
<p>Cloudflare billing has a few moving parts. This page explains the full billing lifecycle, the different types of charges on your account, and how to read a typical invoice.</p>
<h2 id="billing-lifecycle">Billing lifecycle</h2>
<p>When you use paid Cloudflare products, billing follows this sequence:</p>
<ol>
<li><strong>You subscribe</strong>: You pick a plan or turn on a paid add-on. Cloudflare records the date as the start of your billing cycle.</li>
<li><strong>Billing period runs</strong>: Your billing period is 30 days for monthly plans or 365 days for annual plans. During this period, Cloudflare tracks any usage-based consumption.</li>
<li><strong>Invoice generated</strong>: At the end of each billing period, Cloudflare generates an invoice that includes both flat-rate charges for the upcoming period and usage-based charges for the period that just ended.</li>
<li><strong>Payment attempted</strong>: Cloudflare automatically charges your primary payment method on file.</li>
<li><strong>Payment succeeds or fails</strong>: If payment succeeds, the invoice is marked as paid and your services continue. If payment fails, the retry process begins.</li>
</ol>
<h3 id="what-happens-when-payment-fails">What happens when payment fails</h3>
<p>When an automatic payment fails, Cloudflare follows this process:</p>
<ol>
<li><strong>Grace period begins</strong>: You have a 5-day grace period to resolve the payment issue.</li>
<li><strong>Retries</strong>: Cloudflare automatically retries the charge up to 5 times during the grace period.</li>
<li><strong>Manual payment</strong>: You can also <a href="/billing/manage/pay-invoices-overdue-balances/">pay the outstanding balance manually</a> at any time during this period.</li>
<li><strong>Account restrictions</strong>: While the balance is unpaid, you cannot purchase new products, upgrade subscriptions, or modify your billing profile.</li>
<li><strong>Downgrade</strong>: If payment is not resolved within the grace period, your account is automatically downgraded to the Free plan. You lose access to paid features, but your websites remain active.</li>
</ol>
<p>To restore paid services after a downgrade, you must pay the outstanding balance and then re-subscribe to each product individually.</p>
<h2 id="types-of-charges">Types of charges</h2>
<p>A Cloudflare invoice can contain up to three types of charges. Understanding these is key to reading your invoice.</p>
<h3 id="plan-charges-flat-rate-billed-in-advance">Plan charges (flat rate, billed in advance)</h3>
<p>Domain plan charges (Free, Pro, Business, Enterprise) are flat-rate and billed at the start of each billing period for the upcoming month or year. Plans are billed <strong>per domain</strong> — if you have 20 domains on the Pro plan at $25/month, you will see a single line item for 20 x $25 = $500.</p>
<p>The line item lists the domain names the plan covers. For example:</p>
<table>
<thead>
<tr>
<th>Description</th>
<th>Qty</th>
<th>Unit price</th>
<th>Amount</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Pro Plan (example1.com, example2.com, example3.com)</td>
<td>3</td>
<td>$25.00</td>
<td>$75.00</td>
</tr>
</tbody>
</table>
<h3 id="subscription-and-add-on-charges-flat-rate-billed-in-advance">Subscription and add-on charges (flat rate, billed in advance)</h3>
<p>Add-on services with flat monthly fees — such as Load Balancing, Argo Smart Routing, Images Stream Bundle, or Cache Reserve — are billed at the start of each billing period. These appear as separate line items, each showing the product name and the period it covers.</p>
<p>For example:</p>
<table>
<thead>
<tr>
<th>Description</th>
<th>Period</th>
<th>Qty</th>
<th>Amount</th>
</tr>
</thead>
<tbody>
<tr>
<td>Basic Load Balancing</td>
<td>Apr 14 - May 13</td>
<td>1</td>
<td>$5.00</td>
</tr>
<tr>
<td>Images Stream Bundle Basic</td>
<td>Apr 14 - May 13</td>
<td>1</td>
<td>$5.00</td>
</tr>
<tr>
<td>Smart Shield Argo Zone Level Plan - Basic</td>
<td>Apr 14 - May 13</td>
<td>1</td>
<td>$5.00</td>
</tr>
</tbody>
</table>
<p>Some add-ons have multiple sub-line items (for example, Load Balancing shows separate lines for pools, origins, health check intervals, and health check regions). Many of these sub-items may show $0.00 if they are within your included allocation.</p>
<h3 id="usage-based-charges-metered-billed-in-arrears">Usage-based charges (metered, billed in arrears)</h3>
<p>Products like Workers, R2, Cache Reserve operations, Stream minutes viewed, and Argo data transfer are billed based on actual usage from the <strong>previous</strong> billing period. These line items show a date range for the prior period and a quantity representing your consumption.</p>
<p>For example:</p>
<table>
<thead>
<tr>
<th>Description</th>
<th>Period</th>
<th>Qty</th>
<th>Unit price</th>
<th>Amount</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cache Reserve Reads</td>
<td>Mar 14 - Apr 13</td>
<td>166,865</td>
<td>$0.36 per 1,000,000</td>
<td>$0.36</td>
</tr>
<tr>
<td>Smart Shield Argo Accelerated Gigabytes (First GB is included)</td>
<td>Mar 14 - Apr 13</td>
<td>34</td>
<td>$0.10</td>
<td>$3.40</td>
</tr>
<tr>
<td>Stream Bundle Basic Minutes of Video Viewed (in thousands)</td>
<td>Mar 14 - Apr 13</td>
<td>198</td>
<td>$1.00 per 1,000</td>
<td>$1.00</td>
</tr>
</tbody>
</table>
<p>Many usage-based products include a free tier (for example, &quot;First 10GB-Month included&quot; for R2 storage). If your usage stays within the free tier, the line item appears with a quantity of 0 and a $0.00 amount.</p>
<p>For more detail on which products use usage-based billing, refer to <a href="/billing/understand/usage-based-billing/">Usage-based billing</a>.</p>
<h2 id="reading-your-invoice">Reading your invoice</h2>
<p>A typical Cloudflare invoice may span several pages and contain 20-30+ line items. Here is how the invoice is organized:</p>
<h3 id="invoice-header">Invoice header</h3>
<p>The top of the invoice shows:</p>
<ul>
<li><strong>Invoice number</strong> (for example, IN-62358374)</li>
<li><strong>Date of issue</strong> and <strong>date due</strong> (usually the same day for automatic payments)</li>
<li><strong>Company name</strong> — the name on your billing profile</li>
<li><strong>Cloudflare address</strong> and your <strong>billing address</strong></li>
<li><strong>Total amount due</strong></li>
</ul>
<h3 id="line-items">Line items</h3>
<p>Line items are grouped by billing period. You will typically see two groups on every invoice:</p>
<table>
<thead>
<tr>
<th>Section</th>
<th>Billing period</th>
<th>What it covers</th>
</tr>
</thead>
<tbody>
<tr>
<td>Usage-based charges</td>
<td>Previous period (for example, Mar 14 - Apr 13)</td>
<td>Metered consumption from the period that just ended</td>
</tr>
<tr>
<td>Flat-rate charges</td>
<td>Upcoming period (for example, Apr 14 - May 13)</td>
<td>Plan fees, subscription fees, and add-on base fees prepaid for the next period</td>
</tr>
</tbody>
</table>
<p>Each line item shows:</p>
<ul>
<li><strong>Description</strong>: Product name and any included free tier</li>
<li><strong>Date range</strong>: The billing period the charge covers</li>
<li><strong>Qty</strong>: Units consumed (for usage) or count (for plans/subscriptions)</li>
<li><strong>Unit price</strong>: Price per unit, sometimes shown as &quot;per 1,000,000&quot; or &quot;per 50,000&quot; for high-volume metrics</li>
<li><strong>Amount</strong>: Total charge for that line item</li>
</ul>
<h3 id="zero-amount-line-items">Zero-amount line items</h3>
<p>Many products have multiple billable dimensions (for example, R2 has separate lines for storage, data retrieval, Class A operations, and Class B operations). Even if you did not use a dimension during the billing period, it appears on the invoice at $0.00. This is expected — it confirms the product is active and shows that no charges were incurred for that specific dimension.</p>
<details class="nb-details"><summary>Example: R2 line items on a typical invoice</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3363.md")
</div></details>
<h3 id="invoice-total">Invoice total</h3>
<p>The bottom of the invoice shows:</p>
<ul>
<li><strong>Subtotal</strong>: Sum of all line items</li>
<li><strong>Sales tax</strong>: If applicable based on your billing address (refer to <a href="/billing/understand/sales-tax/">Sales tax</a>)</li>
<li><strong>Total</strong> and <strong>Amount due</strong>: The final amount charged</li>
</ul>
<h2 id="the-billing-dashboard">The billing dashboard</h2>
<p>The Cloudflare dashboard organizes billing information across four tabs under <strong>Manage Account</strong> &gt; <strong>Billing</strong>:</p>
<ul>
<li><strong>Invoices and documents</strong> — view, download, and pay invoices. Configure your billing email preference and set up billable usage notifications.</li>
<li><strong>Billable Usage</strong> — track daily usage-based costs across all products for the current or previous billing period.</li>
<li><strong>Payment</strong> — manage your primary and additional payment methods, billing address, and tax-exempt status.</li>
<li><strong>Subscriptions</strong> — view all active subscriptions with their renewal dates, pricing, and invoice status. Cancel or modify subscriptions from this tab.</li>
</ul>
<h3 id="billable-usage-dashboard">Billable usage dashboard</h3>
<p>The billable usage dashboard shows a daily cost breakdown chart and a per-product usage table. Each product row shows total usage, billable usage (above the free tier), and the cumulative cost for the billing period.</p>
<p><img src="/assets/upstream/images/billing/billable-usage-dashboard.png" alt="The billable usage dashboard showing a daily cost breakdown chart and per-product usage table" /></p>
<h3 id="budget-alerts">Budget alerts</h3>
<p>Budget alerts notify you by email when your account-wide usage-based spend crosses a dollar threshold. Set these up under <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</p>
<p><img src="/assets/upstream/images/billing/budget-alert-modal.png" alt="The budget alert creation modal showing threshold and notification configuration" /></p>
<p>For more detail on monitoring your costs, refer to <a href="/billing/manage/billable-usage/">Monitor billable usage</a> and <a href="/billing/manage/budget-alerts/">Budget alerts</a>.</p>
<h2 id="billing-cycles">Billing cycles</h2>
<p>Your first paid purchase on a Cloudflare account sets the billing date for all future monthly subscriptions. Annual subscriptions follow their own cycle. You can have two different billing cycles on your account — one for monthly and one for annual subscriptions.</p>
<p>All billing dates use <strong>UTC</strong> (Coordinated Universal Time), not your local time zone. Make any plan changes or cancellations at least 24 hours before your billing date to avoid timing issues.</p>
<p>For example, if you upgrade to the Pro plan on the 10th of a month, all monthly charges bill on the 10th going forward.</p>
<h2 id="upgrades-and-downgrades">Upgrades and downgrades</h2>
<ul>
<li><strong>Upgrades</strong> take effect immediately. You are charged a prorated amount for the remainder of the current billing period, and your account is credited for the unused portion of the lower plan.</li>
<li><strong>Downgrades</strong> take effect at the end of the current billing period. You continue to have access to the higher-tier features until the new period begins.</li>
<li><strong>Cancellations</strong> follow the same timing as downgrades — service continues until the end of the billing period. Cloudflare does not issue refunds for the remaining time.</li>
</ul>
<p>For details, refer to <a href="/billing/understand/billing-policy/">Billing policy</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/invoices/">Invoices</a> — Download and manage your invoices</li>
<li><a href="/billing/understand/usage-based-billing/">Usage-based billing</a> — Products that bill based on consumption</li>
<li><a href="/billing/understand/billing-policy/">Billing policy</a> — Refund policy, payment methods, and terms</li>
<li><a href="/billing/manage/pay-invoices-overdue-balances/">Pay an outstanding balance</a> — Resolve unpaid invoices</li>
</ul>
