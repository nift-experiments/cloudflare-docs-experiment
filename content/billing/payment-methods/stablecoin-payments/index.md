---
cp9:
  canonical: https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/
  description: Pay for Cloudflare services with USDC stablecoin at the checkout.
  full_title: Stablecoin payments · Cloudflare Billing docs
  head_html: <title>Stablecoin payments · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Pay for Cloudflare services with USDC stablecoin at the checkout."><link rel="canonical" href="https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/index.md"><meta property="og:title" content="Stablecoin payments · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pay for Cloudflare services with USDC stablecoin at the checkout."><meta property="og:url" content="https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Billing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/#page","headline":"Stablecoin payments \u00b7 Cloudflare Billing docs","description":"Pay for Cloudflare services with USDC stablecoin at the checkout.","url":"https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/payment-methods/stablecoin-payments/
  schema: 1
---
<p>You can pay for Cloudflare services with USDC stablecoin at the checkout. Stablecoin payments support one-time charges and recurring billing, including usage-based products.</p>
<h2 id="how-stablecoin-payments-work">How stablecoin payments work</h2>
<ol>
<li><strong>Checkout</strong>: Select <strong>Crypto</strong> in the payment method picker, alongside card, Apple Pay, and Google Pay.</li>
<li><strong>Wallet connection</strong>: You are redirected to a Stripe-hosted page at <code>crypto.stripe.com</code> to connect your wallet.</li>
<li><strong>Smart contract permit</strong>: Sign a one-time permit to authorize the initial charge and, for recurring subscriptions, future automatic charges.</li>
<li><strong>On-chain confirmation</strong>: Your subscription activates after on-chain confirmation, typically within seconds.</li>
</ol>
<p>For recurring billing, Cloudflare charges your saved wallet each cycle. You only need to act if your wallet balance runs out or you revoke the permit.</p>
<h2 id="supported-stablecoins-and-wallets">Supported stablecoins and wallets</h2>
<table>
<thead>
<tr>
<th>Item</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Stablecoins</td>
<td>USDC on Base and Polygon</td>
</tr>
<tr>
<td>Wallets</td>
<td>MetaMask, Phantom, Coinbase Wallet, and 400+ wallets via WalletConnect</td>
</tr>
<tr>
<td>Invoice currency</td>
<td>US dollars (USD)</td>
</tr>
<tr>
<td>Chargebacks and disputes</td>
<td>Not available. Stablecoin payments are final once confirmed on-chain.</td>
</tr>
</tbody>
</table>
<h2 id="recurring-billing">Recurring billing</h2>
<p>The smart contract permit authorizes future automatic charges for:</p>
<ul>
<li>Monthly or annual subscription renewals for paid plans</li>
<li>Usage-based charges billed at threshold for Workers, R2, and Stream</li>
<li>Prorated charges for plan upgrades</li>
</ul>
<p>Each charge is processed against the saved permit. No action is required between cycles.</p>
<h2 id="payment-failures">Payment failures</h2>
<p>Stablecoin payments fail for a small number of well-defined reasons:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>What happens</th>
<th>How to resolve</th>
</tr>
</thead>
<tbody>
<tr>
<td>Insufficient funds</td>
<td>Your wallet does not have enough USDC</td>
<td>Add USDC to the wallet, then retry. Subscriptions enter dunning until the payment succeeds.</td>
</tr>
<tr>
<td>Approval revoked</td>
<td>You revoked or reduced the permit below the payment amount</td>
<td>Return to the checkout and reconnect your wallet to issue a new permit</td>
</tr>
<tr>
<td>Wallet screening</td>
<td>Pre-transaction screening flagged the wallet</td>
<td>Use a different wallet or payment method</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3398.md")
</aside>
<h2 id="refunds">Refunds</h2>
<p>Refunds for stablecoin payments are returned as USDC to the wallet you paid from. Refunds typically arrive within minutes, compared to 5–10 business days for card refunds.</p>
<h2 id="view-your-payment-history">View your payment history</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Invoices</strong>. Stablecoin payments are listed with payment method <code>crypto</code>.</li>
</ol>
<h2 id="faq">FAQ</h2>
<details class="nb-details"><summary>Network fees and gas</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3399.md")
</div></details>
<details class="nb-details"><summary>Smart contract permit scope</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3400.md")
</div></details>
<details class="nb-details"><summary>Multiple payment methods</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3401.md")
</div></details>
<details class="nb-details"><summary>Pending state during on-chain confirmation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3402.md")
</div></details>
