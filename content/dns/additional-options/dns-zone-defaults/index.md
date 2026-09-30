---
cp9:
  canonical: https://developers.cloudflare.com/dns/additional-options/dns-zone-defaults/
  description: Set default DNS settings applied to new zones in your account.
  full_title: Configure DNS zone defaults · Cloudflare DNS docs
  head_html: <title>Configure DNS zone defaults · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set default DNS settings applied to new zones in your account."><link rel="canonical" href="https://developers.cloudflare.com/dns/additional-options/dns-zone-defaults/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/additional-options/dns-zone-defaults/index.md"><meta property="og:title" content="Configure DNS zone defaults · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set default DNS settings applied to new zones in your account."><meta property="og:url" content="https://developers.cloudflare.com/dns/additional-options/dns-zone-defaults/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/additional-options/dns-zone-defaults/#page","headline":"Configure DNS zone defaults \u00b7 Cloudflare DNS docs","description":"Set default DNS settings applied to new zones in your account.","url":"https://developers.cloudflare.com/dns/additional-options/dns-zone-defaults/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/additional-options/dns-zone-defaults/
  schema: 1
---
<p>While there are default values for DNS settings that Cloudflare applies to all new zones, Enterprise accounts have the option to configure their own DNS zone defaults according to their preference.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7730.md")
</aside>
<h2 id="steps">Steps</h2>
<ol>
<li>In the Cloudflare dashboard, go to the account <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>DNS Settings</strong>. If these options are not displayed on your Cloudflare dashboard, you may need to reach out to your account team to have them added.</li>
<li>For <strong>DNS zone defaults</strong>, select <strong>Configure defaults</strong>.</li>
</ol>
<p>The values you select for the listed settings will be automatically applied to new zones as you add them to your Cloudflare account.</p>
<h2 id="available-settings">Available settings</h2>
<ul>
<li><a href="/dns/nameservers/nameserver-options/#assignment-method">Nameserver assignment</a>: Select your preferred nameserver type or assignment method that you want Cloudflare to use for your new zones. This setting applies both to primary zones (<a href="/dns/zone-setups/full-setup/">full setup</a>) and <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary zones</a>.</li>
</ul>
<p>For primary zones:</p>
<ul>
<li><a href="/dns/nameservers/nameserver-options/#multi-provider-dns">Multi-provider DNS</a>: Control whether or not Cloudflare will consider <code>NS</code> records you add on the zone apex and if zones that contain external nameservers listed in the registrar will be activated.</li>
<li><a href="/dns/nameservers/nameserver-options/#nameserver-ttl">Nameserver TTL</a>: Control how long, in seconds, your nameserver (<code>NS</code>) records are cached. The default time-to-live (TTL) is 24 hours. This setting applies both to Cloudflare nameservers and <a href="/dns/nameservers/custom-nameservers/">custom nameservers</a>.</li>
<li><a href="/dns/manage-dns-records/reference/dns-record-types/#soa">SOA record</a>: Adjust values for the start of authority (SOA) record that Cloudflare creates for your zone.</li>
</ul>
<p>For secondary zones:</p>
<ul>
<li>
<p><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS override</a>: Enable the options to use Cloudflare <a href="/dns/proxy-status/">proxy</a> and add <code>CNAME</code> records at your zone apex.</p>
<p>Multi-provider DNS does not apply as a setting for secondary zones, as this is already a required behavior for this setup. <code>SOA</code> record and the <code>NS</code> record TTL are defined on your external DNS provider and only transferred into Cloudflare.</p>
</li>
</ul>
