---
cp9:
  canonical: https://developers.cloudflare.com/registrar/account-options/icloud-domains/
  description: Set up iCloud custom email domains via Cloudflare.
  full_title: iCloud Custom Email Domains · Cloudflare Registrar docs
  head_html: <title>iCloud Custom Email Domains · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up iCloud custom email domains via Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/registrar/account-options/icloud-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/account-options/icloud-domains/index.md"><meta property="og:title" content="iCloud Custom Email Domains · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up iCloud custom email domains via Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/registrar/account-options/icloud-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/account-options/icloud-domains/#page","headline":"iCloud Custom Email Domains \u00b7 Cloudflare Registrar docs","description":"Set up iCloud custom email domains via Cloudflare.","url":"https://developers.cloudflare.com/registrar/account-options/icloud-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/account-options/icloud-domains/
  schema: 1
---
<p>With <a href="https://support.apple.com/kb/HT212514">iCloud Custom Email Domain</a>, you can now purchase a custom domain right from iCloud Settings through Cloudflare and have it automatically set up with your iCloud Mail account. It's great if you want to create a custom email domain for you or your family, such as @examplefamily.com.</p>
<p>You will need an active iCloud+ subscription to add a custom email domain.</p>
<h2 id="purchase-custom-email-domain">Purchase custom email domain</h2>
<p>If you want to buy a custom email domain, go to your <a href="https://www.icloud.com/settings/">iCloud</a> settings and scroll down to <strong>Custom Email Domain</strong>.</p>
<hr />
<h2 id="log-in-to-cloudflare">Log in to Cloudflare</h2>
<p>Once you have bought a custom email domain, you can manage your domain and other options through the <a href="https://dash.cloudflare.com/login">Cloudflare Dashboard</a>.</p>
<h3 id="signing-in-with-apple">Signing in with Apple</h3>
<p>If you had signed up with Apple, signing into Cloudflare is as easy as clicking the “Sign in with Apple” button.</p>
<h3 id="signing-in-with-cloudflare">Signing in with Cloudflare</h3>
<p>If you had signed up with Cloudflare, signing into Cloudflare can be done with your email and password.</p>
<hr />
<h2 id="billing-information">Billing information</h2>
<h3 id="supported-payment-methods">Supported payment methods</h3>
<p>For domain registration, Cloudflare supports the following payment methods:</p>
<ul>
<li>Credit Card</li>
<li>PayPal</li>
<li>Apple Pay (available if you have a wallet with a valid payment method and are using an iOS device or Safari on macOS)</li>
</ul>
<p>For domain renewals, Apple Pay does not currently support recurring payments. You can either add another payment method (Credit Card or PayPal) for automatic renewals or log into <a href="#log-in-to-cloudflare">your account</a> near the renewal date and use Apple Pay.</p>
<h3 id="local-currency-price-estimates">Local currency price estimates</h3>
<p>Users may see a price estimate in both U.S. Dollars and a local currency. This is only an estimate based on the current exchange rate.</p>
<p>The final payment will be charged in US dollars.</p>
<hr />
<h2 id="email-issues">Email issues</h2>
<h3 id="email-issues-1">Email issues</h3>
<p>If you are not receiving emails intended for your new email address, review your DNS records in the Cloudflare dashboard:</p>
<ol>
<li>Log into the <a href="#log-in-to-cloudflare">Cloudflare dashboard</a>.</li>
<li>Go to <strong>DNS</strong>.</li>
<li>Your domain should have records similar to the following:</li>
</ol>
<p><img src="/assets/upstream/images/support/icloud-custom-domain-dns-example.png" alt="Your iCloud custom email domain should have a specific set of records created by default." /></p>
<p>If your domain has records similar to those listed above and you are still experiencing problems with your new email address, contact <a href="https://support.apple.com/">Apple Support</a>.</p>
<hr />
<h2 id="domain-website">Domain website</h2>
<p>If you try to visit your new domain, your browser will show an error or empty page.</p>
<p>That's because there's more to setting up a website than purchasing a domain name (which you just did) and setting up email records (which we just did for you). </p>
<p>If you want your domain to be a fully functioning website, you will need to:</p>
<ol>
<li><strong>Build your website</strong>: Either using <a href="/pages/">Cloudflare Pages</a>, a website builder, or files hosted on a server.</li>
<li><strong>Update your Cloudflare DNS</strong>: To direct visitors looking for your domain name to the actual content on your website (<a href="/dns/manage-dns-records/how-to/create-zone-apex/">detailed guide</a>).</li>
</ol>
<hr />
<h2 id="landing-page">Landing Page</h2>
<p>After you buy a domain through iCloud, Cloudflare Registrar automatically enables a landing page for it. This temporary page informs your visitors that you still do not have a website. This feature is only available to new domain registrations, when you buy a domain through an Apple device.</p>
<h3 id="disable-landing-page">Disable Landing Page</h3>
<p>If you do not want to have Landing Page enabled:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Find the domain you want to disable Landing Page for, and select <strong>Manage</strong> &gt; <strong>Configuration</strong>.</li>
<li>Scroll to Landing Page and select <strong>Disable</strong>.</li>
</ol>
<p>You now have Landing Page disabled. The page can also be re-enabled through the same process.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12761.md")
</aside>
