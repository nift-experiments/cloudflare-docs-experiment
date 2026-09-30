---
cp9:
  canonical: https://developers.cloudflare.com/billing/threshold-billing/
  description: Understand threshold-based billing for Cloudflare services.
  full_title: Threshold billing · Cloudflare Billing docs
  head_html: <title>Threshold billing · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand threshold-based billing for Cloudflare services."><link rel="canonical" href="https://developers.cloudflare.com/billing/threshold-billing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/threshold-billing/index.md"><meta property="og:title" content="Threshold billing · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand threshold-based billing for Cloudflare services."><meta property="og:url" content="https://developers.cloudflare.com/billing/threshold-billing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/threshold-billing/#page","headline":"Threshold billing \u00b7 Cloudflare Billing docs","description":"Understand threshold-based billing for Cloudflare services.","url":"https://developers.cloudflare.com/billing/threshold-billing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/threshold-billing/
  schema: 1
---
<p>Threshold billing is an automatic payment collection mechanism for Cloudflare's usage-based products. When your combined usage charges across all usage-based products reach a certain level during a billing cycle, Cloudflare generates a mid-cycle invoice and charges your payment method on file.</p>
<h2 id="how-threshold-billing-works">How threshold billing works</h2>
<ol>
<li><strong>Usage accumulates</strong> - As you use Cloudflare's usage-based products, charges accrue throughout your billing cycle across all these products combined.</li>
<li><strong>Threshold reached</strong> - When your total accumulated usage charges reach the threshold, Cloudflare automatically generates a mid-cycle invoice.</li>
<li><strong>Payment collected</strong> - Your payment method on file is charged for the threshold invoice amount.</li>
<li><strong>One-time trigger</strong> - The threshold fires once per account. After a threshold invoice is generated, your account returns to standard end-of-cycle billing.</li>
<li><strong>End-of-cycle invoice</strong> - At the end of your billing cycle, you receive your regular invoice which includes only the remaining usage charges not already covered by the threshold invoice.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1470.md")
</aside>
<h3 id="example">Example</h3>
<table>
<thead>
<tr>
<th>Event</th>
<th>Charge</th>
</tr>
</thead>
<tbody>
<tr>
<td>Combined usage reaches threshold mid-cycle</td>
<td>Threshold invoice charged (for example, $127.50)</td>
</tr>
<tr>
<td>End of billing cycle (total usage was $180)</td>
<td>End-of-cycle invoice charged (for example, $52.50)</td>
</tr>
<tr>
<td><strong>Total charged</strong></td>
<td><strong>$180</strong></td>
</tr>
</tbody>
</table>
<h2 id="products-subject-to-threshold-billing">Products subject to threshold billing</h2>
<p>Threshold billing applies to all Cloudflare products with usage-based pricing. This includes products such as <a href="/r2/">R2</a>, <a href="/workers/">Workers</a>, <a href="/stream/">Stream</a>, <a href="/images/">Cloudflare Images</a>, and any other product billed based on consumption.</p>
<p>The threshold is based on your total combined usage across all usage-based products, not each product individually.</p>
<h2 id="who-is-affected">Who is affected</h2>
<p>Threshold billing applies to self-serve accounts using any Cloudflare product with usage-based pricing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1469.md")
</aside>
<h2 id="what-happens-if-payment-fails">What happens if payment fails</h2>
<p>If the payment for a threshold invoice fails:</p>
<ol>
<li><strong>Automatic retries</strong> - Cloudflare will automatically retry the payment over a 5-day period.</li>
<li><strong>Email notification</strong> - You will receive an email notifying you of the failed payment with a link to pay the invoice or update your payment method.</li>
<li><strong>Manual payment</strong> - You can pay the invoice directly at any time during the retry period through your Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li><strong>After retries exhausted</strong> - If all payment retries fail, the invoice is marked as uncollectable and your account may be restricted.</li>
</ol>
<p>To avoid service interruption, ensure your payment method on file is current and has sufficient funds.</p>
<h2 id="viewing-your-invoices">Viewing your invoices</h2>
<p>All threshold invoices appear in your billing history alongside your regular invoices.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Invoices</strong> to view your invoice history.</li>
</ol>
<p>Threshold invoices are labeled to distinguish them from regular end-of-cycle invoices.</p>
<h2 id="faq">FAQ</h2>
<h3 id="why-did-i-receive-a-mid-cycle-charge">Why did I receive a mid-cycle charge?</h3>
<p>Your combined usage-based charges across Cloudflare's usage-based products reached the billing threshold before the end of your billing cycle. This is expected behavior for accounts with high usage.</p>
<h3 id="will-i-be-charged-twice-for-the-same-usage">Will I be charged twice for the same usage?</h3>
<p>No. The threshold invoice covers usage up to the point when the threshold was reached. Your end-of-cycle invoice includes only the remaining usage after that point. The two invoices together equal your total usage for the billing period.</p>
<h3 id="can-i-change-the-threshold-amount">Can I change the threshold amount?</h3>
<p>The threshold is automatically set by Cloudflare and cannot be modified.</p>
<h3 id="will-i-get-another-threshold-invoice-next-month">Will I get another threshold invoice next month?</h3>
<p>The threshold can fire once per account. After the first threshold invoice, your account returns to standard end-of-cycle billing for future cycles.</p>
<h3 id="how-do-i-avoid-threshold-invoices">How do I avoid threshold invoices?</h3>
<p>Threshold invoices are triggered by usage. If you prefer not to receive mid-cycle invoices, you can monitor your usage and adjust your product consumption accordingly. However, threshold billing is designed to help you pay as you go rather than receiving a large bill at the end of the month.</p>
<h3 id="what-if-i-think-i-was-charged-incorrectly">What if I think I was charged incorrectly?</h3>
<p>If you believe there is an error with your threshold invoice, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a> with your invoice details.</p>
