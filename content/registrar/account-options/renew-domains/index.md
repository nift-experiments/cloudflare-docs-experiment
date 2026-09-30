---
cp9:
  canonical: https://developers.cloudflare.com/registrar/account-options/renew-domains/
  description: Manage automatic and manual domain renewals.
  full_title: Renew domains with Cloudflare Registrar · Cloudflare Registrar docs
  head_html: <title>Renew domains with Cloudflare Registrar · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage automatic and manual domain renewals."><link rel="canonical" href="https://developers.cloudflare.com/registrar/account-options/renew-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/account-options/renew-domains/index.md"><meta property="og:title" content="Renew domains with Cloudflare Registrar · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage automatic and manual domain renewals."><meta property="og:url" content="https://developers.cloudflare.com/registrar/account-options/renew-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/account-options/renew-domains/#page","headline":"Renew domains with Cloudflare Registrar \u00b7 Cloudflare Registrar docs","description":"Manage automatic and manual domain renewals.","url":"https://developers.cloudflare.com/registrar/account-options/renew-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/account-options/renew-domains/
  schema: 1
---
<h2 id="automatic-renewal-of-domain">Automatic renewal of domain</h2>
<p>Cloudflare Registrar enrolls your domain to auto-renew by default. Unlike other registrars, your domain will only renew at the list price set by the registry. When a domain has the auto-renew setting turned on, Cloudflare will attempt to automatically renew the domain prior to expiration.</p>
<p>There is no guarantee that the renewal will succeed. Renewals may fail for various reasons, including billing failures and registry downtime. While Cloudflare will make several attempts to renew, it is strongly recommended you frequently review your account to ensure your domains have been renewed.</p>
<p>If you decide you no longer need the domain, <a href="#set-up-automatic-renewals">disable auto-renew for your domain</a>. Once disabled, your domain will not renew upon expiration.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/12759.md")
</aside>
<p>You can continue to keep your domain registered with Cloudflare for the time remaining until the expiration date. If you decide you want to keep the domain, enable auto-renew at any time prior to expiration.</p>
<h2 id="set-up-automatic-renewals">Set up automatic renewals</h2>
<p>If you want your domains to renew automatically, keep the default settings for your domain (<strong>Auto Renew</strong> should be set to <strong>On</strong>). To find this setting:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the domain you want to automatically renew, and make sure the <strong>Auto-renew</strong> toggle is enabled.</li>
</ol>
<p>Cloudflare attempts to renew these domains automatically 30 days before their expiration date. Several more attempts are made if the first attempt fails. The last attempt to renew is made on the day before expiration. You can also <a href="#renew-a-domain-manually">manually renew</a> a domain at any time.</p>
<p>If multiple domains are auto-renewed on the same date, only one charge will be made to the primary payment method.</p>
<p>If the renewal fails, you will receive an email notification and Cloudflare will try to renew the domain three additional times. If these attempts fail, you must manually renew your domain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12758.md")
</aside>
<h2 id="renew-a-domain-manually">Renew a domain manually</h2>
<p>You can renew a domain at any time. To renew a domain registered with Cloudflare:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the domain you want to renew and select <strong>Manage</strong>.</li>
<li>In <strong>Registration</strong> select <strong>Renew/Extend Domain</strong>.</li>
<li>In the <strong>Renew for</strong> drop-down menu, choose a number of years to renew your domain (up to 10 years).</li>
<li>Select <strong>Renew</strong> and then <strong>Purchase</strong>.</li>
</ol>
<p>Once Cloudflare validates your payment, the status of your domain changes to <strong>Renewal Pending</strong>. After the renewal is finished, the status changes back to <strong>Active</strong>.</p>
<h2 id="renewal-notifications">Renewal notifications</h2>
<p>Once a domain is registered, Registrar sends the following expiration notices to the Super Admin of the domain:</p>
<ul>
<li>A monthly email listing all domains set to renew automatically within the next 45 days.</li>
<li>A monthly email listing all domains expiring in the next 60-90 days.</li>
</ul>
<p>In addition to the Super Admin, the following expiration notices are sent to the WHOIS Registrant contact associated with the domain:</p>
<ul>
<li>A weekly email listing all domains expiring within the next month.</li>
<li>A daily email listing all domains expiring in seven days.</li>
<li>An email one day after a domain expires.</li>
<li>An email 20 days after the expiration date.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12757.md")
</aside>
