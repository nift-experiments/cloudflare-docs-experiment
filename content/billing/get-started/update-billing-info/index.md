---
cp9:
  canonical: https://developers.cloudflare.com/billing/get-started/update-billing-info/
  description: Update payment methods, billing address, or tax IDs.
  full_title: Update billing information · Cloudflare Billing docs
  head_html: <title>Update billing information · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Update payment methods, billing address, or tax IDs."><link rel="canonical" href="https://developers.cloudflare.com/billing/get-started/update-billing-info/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/get-started/update-billing-info/index.md"><meta property="og:title" content="Update billing information · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update payment methods, billing address, or tax IDs."><meta property="og:url" content="https://developers.cloudflare.com/billing/get-started/update-billing-info/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/get-started/update-billing-info/#page","headline":"Update billing information \u00b7 Cloudflare Billing docs","description":"Update payment methods, billing address, or tax IDs.","url":"https://developers.cloudflare.com/billing/get-started/update-billing-info/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/get-started/update-billing-info/
  schema: 1
---
<p>To avoid potential disruptions in your Cloudflare services, make sure your billing information is current and accurate.</p>
<p>If Cloudflare is unable to process your payment, refer to <a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a>.</p>
<h2 id="update-payment-methods">Update payment methods</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3448.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3449.md")
</div>
<h3 id="supported-payment-methods">Supported payment methods</h3>
<p>The Billing Profile supports:</p>
<ul>
<li>Cards (Visa, Mastercard, American Express, Discover, UnionPay)</li>
<li>PayPal</li>
<li>Apple Pay</li>
<li>Google Pay</li>
<li>Link</li>
<li><a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link</a> (US-based self-serve accounts)</li>
</ul>
<h3 id="3d-secure-authentication">3D Secure authentication</h3>
<p>Cards issued in regions where 3D Secure is required — for example, the EU under PSD2 or India under RBI — trigger an authentication step with the card issuer. Complete the challenge to save the card.</p>
<h2 id="delete-a-payment-method">Delete a payment method</h2>
<p>Before removing your payment method from file, you must cancel all Cloudflare paid services.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3447.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3450.md")
</div>
<h2 id="update-your-billing-address">Update your billing address</h2>
<p>Two address fields exist on your account:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Where it is used</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Billing profile address</strong></td>
<td>Appears as <strong>Bill to</strong> on every invoice. Used for tax calculation and sanctions screening.</td>
</tr>
<tr>
<td><strong>Payment method billing address</strong></td>
<td>Captured when you add a payment method. Used by the card issuer to authorize each charge. Does not appear on invoices.</td>
</tr>
</tbody>
</table>
<p>Updating the billing profile address applies to invoices issued after the change. Past invoices keep the address that was on file when they were issued. Updating the billing profile address does not change the address stored on existing payment methods.</p>
<p>To update the billing profile address:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3451.md")
</div>
<p>To update the address stored on a specific payment method, edit that payment method from the <strong>Payment methods</strong> panel on the <strong>Subscriptions</strong> page. The address you enter is saved both with the payment method and with the card issuer.</p>
<p>If you pay by PayPal, refer to PayPal's <a href="https://www.paypal.com/ai/smarthelp/article/how-do-i-edit-the-billing-address-linked-to-my-credit-card-faq680">billing address documentation</a>.</p>
<h2 id="update-billing-email-address">Update billing email address</h2>
<p>Your billing email address is particularly important if you have <a href="/billing/manage/invoices/#turn-on-invoice-emails-from-cloudflare">opted in to invoice emails</a>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3452.md")
</div>
<h2 id="add-or-change-a-tax-id-vat-or-gst-number">Add or change a Tax ID, VAT, or GST number</h2>
<p>If you added a payment method but did not include a Tax ID, VAT, or GST number, you can add or change the Tax ID, VAT, or GST number associated with the payment method afterwards.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3446.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3453.md")
</div>
<h2 id="remove-a-tax-id-vat-or-gst-number">Remove a Tax ID, VAT, or GST number</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3445.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3454.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/get-started/create-billing-profile/">Create billing profile</a> — Set up your initial payment method</li>
<li><a href="/billing/manage/invoices/">Invoices</a> — View and download invoices</li>
<li><a href="/billing/understand/sales-tax/">Sales tax</a> — How tax is calculated based on your billing address</li>
</ul>
