---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/
  description: If you initially set up a partial domain on Cloudflare, you can later migrate it to a full setup.
  full_title: Convert partial setup to full setup · Cloudflare DNS docs
  head_html: <title>Convert partial setup to full setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="If you initially set up a partial domain on Cloudflare, you can later migrate it to a full setup."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/index.md"><meta property="og:title" content="Convert partial setup to full setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="If you initially set up a partial domain on Cloudflare, you can later migrate it to a full setup."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/#page","headline":"Convert partial setup to full setup \u00b7 Cloudflare DNS docs","description":"If you initially set up a partial domain on Cloudflare, you can later migrate it to a full setup.","url":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/conversions/convert-partial-to-full/
  schema: 1
---
<p>If you initially set up a partial domain on Cloudflare, you can later migrate it to a <a href="/dns/zone-setups/full-setup/">primary setup</a> (also know as full setup).</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-setup">Subdomain setup</h3>
@markup("md", "content/.markup/bodies/7985.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-conversion-subdomain-setup-callout-mdx-1">Meaning you have one or more subdomains (`sub.example.com`) added to Cloudflare as their own zone, separate from your apex domain (`example.com`).</li></ol></section>
<h2 id="1-prepare-cloudflare-ssl-tls"><ol>
<li>Prepare Cloudflare SSL/TLS</li>
</ol></h2>
<p>In the Cloudflare dashboard, either order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">advanced certificate</a> or <a href="/ssl/edge-certificates/custom-certificates/uploading/">upload a custom SSL certificate</a> for your website or application.</p>
<p>You should also verify that the <a href="/ssl/reference/certificate-statuses/">status</a> of your SSL certificate is <strong>Active</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7984.md")
</aside>
<h2 id="2-update-settings-in-authoritative-dns"><ol start="2">
<li>Update settings in authoritative DNS</li>
</ol></h2>
<p>At least 24 hours prior to converting your zone, disable DNSSEC at your authoritative DNS provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7983.md")
</aside>
<h2 id="3-convert-to-full-setup"><ol start="3">
<li>Convert to full setup</li>
</ol></h2>
<p>In the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, select your partial zone (CNAME setup) and go to the <strong>DNS Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Convert to Primary DNS</strong> (this will not affect how your traffic is proxied).</li>
<li>Import your records into Cloudflare DNS and verify that they have been configured correctly. Usually, you will want to import <a href="/dns/proxy-status/">unproxied records</a>.</li>
</ol>
<h2 id="4-activate-full-setup"><ol start="4">
<li>Activate full setup</li>
</ol></h2>
<p>Get your assigned Cloudflare nameservers from the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page and <a href="/dns/nameservers/update-nameservers/">update your nameservers</a> at your registrar.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7982.md")
</aside>
<p>Cloudflare recommends that you also <a href="/dns/dnssec/">enable DNSSEC</a> from the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page
and add the DS record to your registrar.</p>
<p>Once all the DNS TTLs expire, all your DNS queries will be answered by the Cloudflare global network.</p>
<p>Start proxying additional hostnames by enabling the <a href="/dns/proxy-status/">proxy status</a> (also known as orange-clouding) for specific DNS records. Previously proxied subdomains will continue to be proxied without any interruption.</p>
