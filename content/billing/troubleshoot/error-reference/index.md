---
cp9:
  canonical: https://developers.cloudflare.com/billing/troubleshoot/error-reference/
  description: Common billing error messages and solutions.
  full_title: Billing error reference · Cloudflare Billing docs
  head_html: <title>Billing error reference · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Common billing error messages and solutions."><link rel="canonical" href="https://developers.cloudflare.com/billing/troubleshoot/error-reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/troubleshoot/error-reference/index.md"><meta property="og:title" content="Billing error reference · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Common billing error messages and solutions."><meta property="og:url" content="https://developers.cloudflare.com/billing/troubleshoot/error-reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/troubleshoot/error-reference/#page","headline":"Billing error reference \u00b7 Cloudflare Billing docs","description":"Common billing error messages and solutions.","url":"https://developers.cloudflare.com/billing/troubleshoot/error-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/troubleshoot/error-reference/
  schema: 1
---
<p>Use the tables below to find common billing error messages, understand what they mean, and go to the right solution.</p>
<p>When troubleshooting, start with the exact error message. Then confirm whether the account has an unpaid balance, an active subscription, a pending cancellation, or a pending payment transaction.</p>
<h2 id="error-messages">Error messages</h2>
<table>
<thead>
<tr>
<th>Error message</th>
<th>Cause</th>
<th>What to do first</th>
</tr>
</thead>
<tbody>
<tr>
<td>&quot;You cannot add or modify subscriptions or services until the outstanding balance is paid.&quot;</td>
<td>Your account has an unpaid balance.</td>
<td><a href="/billing/manage/pay-invoices-overdue-balances/">Pay the outstanding balance</a>.</td>
</tr>
<tr>
<td>&quot;The payment has failed. Please contact your bank or use a different payment method.&quot;</td>
<td>Your payment method was declined by your bank.</td>
<td>Check your card details and bank balance, then retry. Refer to <a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a>.</td>
</tr>
<tr>
<td>&quot;Payment error: authorization failed&quot;</td>
<td>Your bank declined the transaction, or 3DS authentication was not completed.</td>
<td>Contact your bank and retry the payment. Refer to <a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a>.</td>
</tr>
<tr>
<td>&quot;This zone cannot be upgraded&quot;</td>
<td>The account or a previous owner of the domain has an outstanding balance.</td>
<td>Pay the balance on all accounts you have access to, wait 24 hours, then retry. Refer to <a href="/billing/troubleshoot/resolve-zone-cannot-be-upgraded/">Resolve the zone cannot be upgraded error</a>.</td>
</tr>
<tr>
<td>&quot;There is a problem with your billing profile&quot;</td>
<td>Same as &quot;this zone cannot be upgraded&quot; — an unpaid balance exists.</td>
<td><a href="/billing/manage/pay-invoices-overdue-balances/">Pay the outstanding balance</a> and wait 24 hours.</td>
</tr>
<tr>
<td>&quot;You cannot modify this subscription since it is currently scheduled to be cancelled&quot;</td>
<td>You are trying to change a subscription that already has a pending cancellation.</td>
<td>Cancel the pending downgrade first, then make your change. Refer to <a href="/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/">Resolve &quot;you cannot modify this subscription&quot;</a>.</td>
</tr>
<tr>
<td>&quot;You can't remove this payment method while it's linked to active subscriptions.&quot;</td>
<td>You are trying to delete a payment method that is still tied to paid services.</td>
<td>Cancel all paid subscriptions first, or add a replacement payment method. Refer to <a href="/billing/troubleshoot/resolve-cannot-remove-payment-method/">Resolve &quot;cannot remove payment method&quot;</a>.</td>
</tr>
<tr>
<td>&quot;You can't remove a payment method while there are transactions in progress.&quot;</td>
<td>A usage-based charge is pending, or a Registrar renewal is scheduled within 24 hours.</td>
<td>Wait for pending transactions to complete, then retry. Refer to <a href="/billing/troubleshoot/resolve-cannot-remove-payment-method/">Resolve &quot;cannot remove payment method&quot;</a>.</td>
</tr>
</tbody>
</table>
<h2 id="email-notifications">Email notifications</h2>
<table>
<thead>
<tr>
<th>Email subject</th>
<th>What it means</th>
<th>What to do first</th>
</tr>
</thead>
<tbody>
<tr>
<td>&quot;We couldn't process your renewal payment&quot;</td>
<td>A recurring subscription charge failed. Cloudflare will retry up to 5 times over 5 days.</td>
<td>Update your payment method or manually pay the invoice before the grace period ends. Refer to <a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a>.</td>
</tr>
</tbody>
</table>
<h2 id="still-stuck">Still stuck?</h2>
<p>If your error message is not listed above or the suggested solution does not resolve the issue, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a>. Include the account ID, invoice number, exact error message, and the action you were trying to complete.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/troubleshoot/troubleshoot-failed-payments/">Resolve a payment failure</a> — Fix payment errors</li>
<li><a href="/billing/manage/pay-invoices-overdue-balances/">Pay an outstanding balance</a> — Resolve unpaid invoices</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — Billing lifecycle and charge types</li>
</ul>
