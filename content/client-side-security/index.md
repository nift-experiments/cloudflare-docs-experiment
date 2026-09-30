---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/
  description: Cloudflare's client-side security is a comprehensive client-side security and privacy solution that allows you to ensure the safety of your website visitors' browsing environment.
  full_title: Overview · Client-side security docs
  head_html: <title>Overview · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare&#x27;s client-side security is a comprehensive client-side security and privacy solution that allows you to ensure the safety of your website visitors&#x27; browsing environment."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/index.md"><meta property="og:title" content="Overview · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare&#x27;s client-side security is a comprehensive client-side security and privacy solution that allows you to ensure the safety of your website visitors&#x27; browsing environment."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Client-side security"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/client-side-security/#page","headline":"Overview \u00b7 Client-side security docs","description":"Cloudflare's client-side security is a comprehensive client-side security and privacy solution that allows you to ensure the safety of your website visitors' browsing environment.","url":"https://developers.cloudflare.com/client-side-security/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /client-side-security/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1338.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>Websites load third-party scripts for analytics, ads, chat widgets, and payment forms. If an attacker compromises one of these scripts, they can steal visitor data directly from the browser, an attack known as a <a href="https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/">client-side supply chain attack</a>. Client-side security (formerly Page Shield) gives you visibility into these resources and alerts you when something changes or looks malicious.</p>
<p>Client-side security monitors scripts, connections, and cookies loaded by your website visitors. You can set up alert notifications and create content security rules to control which resources are allowed on your pages.</p>
<p>Learn how to <a href="/client-side-security/get-started/">get started</a>.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1339.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1340.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1341.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1342.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1343.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1344.md")
</div>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
<th>Advanced</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Script monitoring</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Connection monitoring</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cookie monitoring</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Page attribution</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>New Resources Alerts and New Domain Alerts</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Malicious script detection and alerting</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Code change detection and alerting</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Malicious connection detection and alerting</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Cookie monitoring advanced fields</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of content security rules (positive blocking)</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td>Number of Logpush jobs</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>4</td>
</tr>
</tbody>
</table>
<p>The Page Shield add-on is now Client-Side Security Advanced. The features and entitlements are unchanged.</p>
