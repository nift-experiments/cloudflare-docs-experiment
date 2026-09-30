---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/configuration/health-checks/
  description: Monitor origin server availability and receive notifications when status changes.
  full_title: Health Checks · Cloudflare Smart Shield docs
  head_html: <title>Health Checks · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor origin server availability and receive notifications when status changes."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/configuration/health-checks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/configuration/health-checks/index.md"><meta property="og:title" content="Health Checks · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor origin server availability and receive notifications when status changes."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/configuration/health-checks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Smart Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/smart-shield/configuration/health-checks/#page","headline":"Health Checks \u00b7 Cloudflare Smart Shield docs","description":"Monitor origin server availability and receive notifications when status changes.","url":"https://developers.cloudflare.com/smart-shield/configuration/health-checks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /smart-shield/configuration/health-checks/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/13852.md")
</aside>
<p>A health check is a service that runs on Cloudflare's edge network to monitor whether an origin server is online. This allows you to view the health of your origin servers even if there is only one origin or you do not yet need to balance traffic across your infrastructure.</p>
<p>Health Checks support various configurations to hone in on what you can check, including response codes, protocol types, and intervals. You can specify a particular path if an origin server serves multiple applications or check a larger subset of response codes for your staging environment. All of these options allow you to properly target your Health Check, providing a precise picture of what is wrong with an origin server.</p>
<h2 id="regions">Regions</h2>
<p>Cloudflare has data centers in <a href="https://www.cloudflare.com/network/">hundreds of cities worldwide</a>. Health checks do not run from every single of these data centers as this would result in numerous requests to your servers. Instead, you are able to choose between one and thirteen regions from which to run health checks. Cloudflare will run Health Checks from three data centers in each region that you select.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13851.md")
</aside>
<p>The Internet is not the same everywhere around the world and your users may not have the same experience on your application according to where they are. Running Health Checks from different regions lets you know the health of your application from the point of view of the Cloudflare network in each of these regions.</p>
<p>Analytics are presented at two levels:</p>
<ul>
<li>Regional Aggregates: Combined results from the three data centers within a specific region.</li>
<li>Global Aggregates: Total results across all configured regions and data centers.</li>
</ul>
<p>In the event log, entries are labeled by region or as <strong>Global</strong>. We do not provide granular data for individual data centers.</p>
<p>If you select multiple regions or choose <strong>All Regions</strong> (Business and Enterprise Only), you may increase traffic to your servers. Each region sends individual health checks from three data centers.</p>
<h2 id="further-reading">Further reading</h2>
<ul class="directory-listing"><li><a href="/smart-shield/configuration/health-checks/setup/">Manage Health Checks</a></li><li><a href="/smart-shield/configuration/health-checks/analytics/">Health Checks analytics</a></li><li><a href="/smart-shield/configuration/health-checks/zone-lockdown/">Zone Lockdown</a></li></ul>
