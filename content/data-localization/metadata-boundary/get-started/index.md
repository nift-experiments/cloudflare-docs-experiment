---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/metadata-boundary/get-started/
  description: Configure Customer Metadata Boundary to select the region for your logs and analytics.
  full_title: Get started · Cloudflare Data Localization Suite docs
  head_html: <title>Get started · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Customer Metadata Boundary to select the region for your logs and analytics."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/metadata-boundary/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/metadata-boundary/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Customer Metadata Boundary to select the region for your logs and analytics."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/metadata-boundary/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Data Localization Suite"><meta name="pcx_tags" content="Privacy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/metadata-boundary/get-started/#page","headline":"Get started \u00b7 Cloudflare Data Localization Suite docs","description":"Configure Customer Metadata Boundary to select the region for your logs and analytics.","url":"https://developers.cloudflare.com/data-localization/metadata-boundary/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy"]}</script>
  markdown: true
  noindex: false
  route: /data-localization/metadata-boundary/get-started/
  schema: 1
---
<p>You can configure the Customer Metadata Boundary to select the region where your logs and analytics are stored. This setting controls where Cloudflare stores traffic metadata that could identify your end users. You can configure it via API or the dashboard.</p>
<p>Currently, this can only be applied at the account-level. If you only want the Metadata Boundary to be applied on a portion of zones beneath the same account, you will have to <a href="/fundamentals/manage-domains/move-domain/">move the rest of zones to a new account</a>.</p>
<h2 id="configure-customer-metadata-boundary-in-the-dashboard">Configure Customer Metadata Boundary in the dashboard</h2>
<p>To configure Customer Metadata Boundary in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Customer Metadata Boundary</strong>, select the region you want to use: <code>eu</code> or <code>us</code>. Selecting <code>Global</code> applies no metadata boundary — the default — meaning Customer Logs may be stored in Cloudflare's core data centers globally.</li>
</ol>
<h2 id="configure-customer-metadata-boundary-via-api">Configure Customer Metadata Boundary via API</h2>
<p>You can also configure Customer Metadata Boundary via API.</p>
<p>Currently, only SuperAdmins and Admin roles can edit DLS configurations. Use the <strong>Account-level Logs:Read/Write</strong> API permissions for the <code>/logs/control/cmb</code> endpoint to read/write Customer Metadata Boundary configurations.</p>
<p>These are some examples of API requests.</p>
<details class="nb-details"><summary>Get current regions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7429.md")
</div></details>
<details class="nb-details"><summary>Setting regions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7430.md")
</div></details>
<details class="nb-details"><summary>Delete regions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7431.md")
</div></details>
<h2 id="view-or-change-settings">View or change settings</h2>
<p>To view or change your Customer Metadata Boundary setting:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Preferences</strong>.</li>
<li>Locate the <strong>Customer Metadata Boundary</strong> section.</li>
</ol>
