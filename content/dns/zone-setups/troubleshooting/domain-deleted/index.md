---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/
  description: Learn why a domain may be removed from Cloudflare and how to recover it using audit logs and registrar verification.
  full_title: Domain deleted from Cloudflare · Cloudflare DNS docs
  head_html: <title>Domain deleted from Cloudflare · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn why a domain may be removed from Cloudflare and how to recover it using audit logs and registrar verification."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/index.md"><meta property="og:title" content="Domain deleted from Cloudflare · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn why a domain may be removed from Cloudflare and how to recover it using audit logs and registrar verification."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/#page","headline":"Domain deleted from Cloudflare \u00b7 Cloudflare DNS docs","description":"Learn why a domain may be removed from Cloudflare and how to recover it using audit logs and registrar verification.","url":"https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/troubleshooting/domain-deleted/
  schema: 1
---
<p>Domain deletion commonly occurs for the following reasons:</p>
<ul>
<li>A user with access to the domain removed it.</li>
<li>The nameservers no longer point to Cloudflare. Cloudflare continuously monitors domain registration.</li>
<li>The domain was not authenticated (pending for 28 days).</li>
</ul>
<hr />
<h2 id="check-audit-logs">Check Audit Logs</h2>
<p>Cloudflare <a href="/fundamentals/account/account-security/review-audit-logs/">Audit Logs</a> contain information about domain deletion.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7898.md")
</aside>
<hr />
<h2 id="check-registrar-for-cloudflare-nameservers">Check registrar for Cloudflare nameservers</h2>
<p>If your domain was using a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a>, your registrar needs to use Cloudflare nameservers as the authoritative nameservers for your domain.</p>
<ol>
<li>
<p>Use either the command-line based <code>whois</code> application provided with your operating system or a website such as <a href="https://lookup.icann.org/">ICANN Lookup</a>.</p>
<ul>
<li>If you are unable to find the nameserver details for your domain, reach out to your domain registrar or domain provider to provide the domain registration information.</li>
<li>Ensure Cloudflare's nameservers are the only two nameservers listed in the domain registration details.</li>
<li>Ensure nameservers are spelled correctly in the domain registration.</li>
</ul>
</li>
<li>
<p>Confirm that the nameservers exactly match the nameservers provided within the <strong>Cloudflare Nameservers</strong> card on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page.</p>
</li>
<li>
<p>If you identify incorrect information, log in to your domain provider's portal to make updates or contact your domain provider for assistance.</p>
</li>
</ol>
<hr />
<h2 id="recover-a-deleted-domain">Recover a deleted domain</h2>
<p>To recover a deleted domain, <a href="/fundamentals/manage-domains/add-site/">re-add it in Cloudflare</a> just like you would for a new domain.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7897.md")
</aside>
