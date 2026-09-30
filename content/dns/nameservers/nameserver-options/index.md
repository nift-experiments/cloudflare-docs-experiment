---
cp9:
  canonical: https://developers.cloudflare.com/dns/nameservers/nameserver-options/
  description: Available nameserver configuration options.
  full_title: Multi-provider DNS and nameserver options · Cloudflare DNS docs
  head_html: <title>Multi-provider DNS and nameserver options · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Available nameserver configuration options."><link rel="canonical" href="https://developers.cloudflare.com/dns/nameservers/nameserver-options/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/nameservers/nameserver-options/index.md"><meta property="og:title" content="Multi-provider DNS and nameserver options · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available nameserver configuration options."><meta property="og:url" content="https://developers.cloudflare.com/dns/nameservers/nameserver-options/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/nameservers/nameserver-options/#page","headline":"Multi-provider DNS and nameserver options \u00b7 Cloudflare DNS docs","description":"Available nameserver configuration options.","url":"https://developers.cloudflare.com/dns/nameservers/nameserver-options/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/nameservers/nameserver-options/
  schema: 1
---
<p>Refer to the following sections to learn about different Cloudflare nameserver options. The availability of these options depends on your plan. Also, if you acquired your domain from Cloudflare Registrar, your domain already uses and <a href="/registrar/faq/#can-i-use-my-own-third-party-nameservers">must remain</a> on Cloudflare nameservers.</p>
<h2 id="assignment-method">Assignment method</h2>
<p>When you add a domain on a <a href="/dns/zone-setups/full-setup/">primary (full)</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary</a> DNS setup, Cloudflare automatically assigns your nameservers.</p>
<p>The default assignment method is to use <a href="/dns/nameservers/#standard-nameservers">standard nameservers</a> and favor consistent nameserver names across all zones within an account. Nonetheless, in case there are conflicts, you may get different nameserver names, even for domains that are within the same account.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7614.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7613.md")
</aside>
<h3 id="nameserver-consistency">Nameserver consistency</h3>
<p>The level of consistency you can expect when adding new zones depends on the configured nameserver type.</p>
<ul>
<li>
<p>For <a href="/dns/nameservers/#standard-nameservers">standard nameservers</a>, since a conflict can be caused by anyone adding the same zone to any other Cloudflare account, the likelihood of your new zone being assigned different nameserver names than your previously existing zones is higher.</p>
</li>
<li>
<p>If you use <a href="/dns/nameservers/custom-nameservers/account-custom-nameservers/">account custom nameservers</a>, the only conflict would be between a parent and a child zone, which makes consistent assignment across new zones more likely.</p>
</li>
<li>
<p>With <a href="/dns/nameservers/custom-nameservers/tenant-custom-nameservers/">tenant custom nameservers</a> or <a href="/dns/foundation-dns/advanced-nameservers/#nameservers-hosting-and-assignment">Foundation DNS advanced nameservers</a>, there can still be conflicts caused by two zones with the same name being added to different accounts, but, since access to these features is more restricted, the likelihood of your new zone being assigned different nameserver names than your previously existing zones is lower.</p>
</li>
</ul>
<h3 id="dns-zone-defaults">DNS zone defaults</h3>
<p>If you have an Enterprise account, you also have the option to <a href="/dns/additional-options/dns-zone-defaults/">configure your own DNS zone defaults</a> and change how Cloudflare handles nameserver assignment when you add a new zone to your account:</p>
<ul>
<li><strong>Standard nameservers randomized</strong>: instead of attempting consistency, Cloudflare assigns random pairs of nameserver names every time you add a new domain to your account.</li>
<li><strong>Advanced nameservers</strong>: Cloudflare uses the same method as the default - trying to keep nameserver names consistent for different zones within an account - but uses the specific <a href="/dns/foundation-dns/advanced-nameservers/">Foundation DNS nameservers</a>.</li>
<li><strong>Account custom nameservers</strong>: Cloudflare automatically assigns a set of <a href="/dns/nameservers/custom-nameservers/account-custom-nameservers/">account custom nameservers</a> that you have previously configured for your account. In this method, <strong>Set 1</strong> will be attempted first and, in case of any conflicts, Cloudflare will cycle through the other nameserver sets, in ascending order.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7612.md")
</aside>
<h2 id="multi-provider-dns">Multi-provider DNS</h2>
<p>Multi-provider DNS is an optional setting for zones using <a href="/dns/zone-setups/full-setup/">primary setup (full)</a> and is an enforced default behavior for zones using <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary setup</a>.</p>
<p>When you enable multi-provider DNS on a primary zone:</p>
<ul>
<li>Cloudflare will no longer ignore <code>NS</code> records created on the zone apex, as in the example below.</li>
</ul>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7615.md")
</div>
<p>This means that responses to DNS queries made to the zone apex and requesting <code>NS</code> records will contain both Cloudflare's and your other DNS providers' nameservers.</p>
<ul>
<li>Cloudflare will activate a primary zone (full setup) even if its <a href="/dns/nameservers/update-nameservers/">nameservers listed at the registrar</a> include nameservers from other DNS providers.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7611.md")
</aside>
<h2 id="nameserver-ttl">Nameserver TTL</h2>
<p>For both Cloudflare nameservers (standard or advanced) and custom nameservers, the <code>NS</code> record time-to-live (TTL) is controlled by the specific setting on the <strong>DNS Records</strong> page, under <strong>DNS record options</strong>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="foundation-dns">Foundation DNS</h3>
@markup("md", "content/.markup/bodies/7610.md")
</aside>
<p>The default TTL is 24 hours (or 86,400 seconds), but you have the option to lower this value depending on your needs. For example, shorter TTLs can be useful when you are changing nameservers or migrating a zone. Accepted values range from 30 to 86,400 seconds.</p>
<p>This setting can also be configured as a <a href="/dns/additional-options/dns-zone-defaults/">DNS zone default</a>, meaning new zones created in your account will automatically start with the value you define.</p>
