---
cp9:
  canonical: https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/
  description: Advanced nameserver features for Foundation DNS.
  full_title: Advanced nameservers · Cloudflare DNS docs
  head_html: <title>Advanced nameservers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Advanced nameserver features for Foundation DNS."><link rel="canonical" href="https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/index.md"><meta property="og:title" content="Advanced nameservers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Advanced nameserver features for Foundation DNS."><meta property="og:url" content="https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/#page","headline":"Advanced nameservers \u00b7 Cloudflare DNS docs","description":"Advanced nameserver features for Foundation DNS.","url":"https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/foundation-dns/advanced-nameservers/
  schema: 1
---
<p>Advanced nameservers included with <a href="/dns/foundation-dns/">Foundation DNS</a> offer improved resiliency and more consistent nameserver assignment.</p>
<p>Consider the sections below for details about advanced nameservers, and refer to <a href="/dns/foundation-dns/setup/">Set up advanced nameservers</a> to learn how to enable this feature.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7672.md")
</aside>
<h2 id="anycast-network-groups">Anycast network groups</h2>
<p>To increase resiliency, the advertisement of advanced nameserver IPs is organized into three <span class="nb-glossary-tooltip" title="anycast">anycast</span> network groups.</p>
<p>Two groups consist of IPs advertised from geographically distributed data centers, and a third group consists of IPs advertised from all data centers in the Cloudflare network.</p>
<details class="nb-details"><summary>United Kingdom example</summary><div class="nb-details-body">
@input("content/.markup/bodies/7674.md")
</div></details>
<p>In DNS resolution, a resolver eventually acquires a list of all IPs where authoritative nameservers for a domain can be reached, and will then usually prefer the IP with the best resolution performance.</p>
<p>When, instead of advertising all IPs in all data centers, this group logic is applied, resiliency is improved because, if one of the data centers experiences a localized issue, the resolver can fall back to an IP advertised by the next closest data center. The third group adds another layer of redundancy, further enhancing resiliency.</p>
<p>Refer to <a href="https://blog.cloudflare.com/foundation-dns-launch">our blog post</a> for an in-depth explanation of the distributed groups logic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7671.md")
</aside>
<h2 id="dedicated-release-process">Dedicated release process</h2>
<p>Zones using advanced nameservers are less exposed to incidents or software regression.</p>
<p>The dedicated release process means that only changes that have been in production for a while will reach advanced nameservers.</p>
<h2 id="nameservers-hosting-and-assignment">Nameservers hosting and assignment</h2>
<p>While standard Cloudflare nameservers are hosted under <code>ns.cloudflare.com</code> or <code>secondary.cloudflare.com</code>, advanced nameservers use different domains:</p>
<ul>
<li><code>foundationdns.com</code></li>
<li><code>foundationdns.net</code></li>
<li><code>foundationdns.org</code></li>
</ul>
<p>Using the different TLDs (<code>.com</code>, <code>.net</code>, and <code>.org</code>) and making these available only to enterprise accounts allows for better predictability and consistency in nameserver assignment.</p>
<p>There should also be less conflicts when guaranteeing that directly descending zones do not have the same nameserver set.</p>
<details class="nb-details"><summary>Descending zones example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7675.md")
</div></details>
<h3 id="consistent-assignment-across-new-zones">Consistent assignment across new zones</h3>
<p>Advanced nameservers try to keep the same nameserver set (<code>blue</code>, <code>gold</code>, or <code>orange</code>) for new zones added to the same account, but a new zone can still be assigned a different set when:</p>
<ul>
<li>The same domain is (or was recently) active on another Cloudflare account.</li>
<li>A directly descending zone in the same or another account already uses the same set.</li>
<li>The zone was previously deleted from Cloudflare and re-added.</li>
</ul>
<p><a href="/dns/nameservers/nameserver-options/#assignment-method">Assigned nameservers cannot be changed</a> after a zone is created. If your zones must share the same nameservers, <a href="/dns/nameservers/custom-nameservers/account-custom-nameservers/">account custom nameservers</a> provide a single set that every zone in the account can use, and can be configured as the account's <a href="/dns/additional-options/dns-zone-defaults/">DNS zone default</a> so new zones automatically receive them.</p>
<h2 id="custom-nameserver-compatibility">Custom Nameserver compatibility</h2>
<p>Advanced Nameserver features — such as multiple anycast network groups or dedicated release process — are currently available for Cloudflare-branded nameservers. Support of these features for <a href="/dns/nameservers/custom-nameservers/">Custom Nameservers</a> is on the roadmap. Contact your account team for the latest availability.</p>
