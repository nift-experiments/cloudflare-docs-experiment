---
cp9:
  canonical: https://developers.cloudflare.com/dns/nameservers/
  description: Manage Cloudflare nameservers for your zones.
  full_title: Nameservers · Cloudflare DNS docs
  head_html: <title>Nameservers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage Cloudflare nameservers for your zones."><link rel="canonical" href="https://developers.cloudflare.com/dns/nameservers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/nameservers/index.md"><meta property="og:title" content="Nameservers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage Cloudflare nameservers for your zones."><meta property="og:url" content="https://developers.cloudflare.com/dns/nameservers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/nameservers/#page","headline":"Nameservers \u00b7 Cloudflare DNS docs","description":"Manage Cloudflare nameservers for your zones.","url":"https://developers.cloudflare.com/dns/nameservers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/nameservers/
  schema: 1
---
<p>Nameservers are DNS servers that answer DNS queries about the domains they are authoritative for. When a visitor types your domain into a browser, the <a href="https://www.cloudflare.com/learning/dns/what-is-dns/">DNS resolution process</a> passes through several server types and eventually reaches the authoritative nameservers for the final answer.</p>
<p>In the context of Cloudflare DNS, nameservers refer to authoritative nameservers — the servers that hold the definitive DNS records for your domain and provide the final response in DNS resolution. When a nameserver is authoritative for <code>example.com</code>, DNS resolvers will consider responses from this nameserver when a user tries to access <code>example.com</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7618.md")
</aside>
<h2 id="authoritative-nameservers-offering">Authoritative nameservers offering</h2>
<p>Within Cloudflare, and depending on your plan, you can choose between using Cloudflare-branded nameservers or setting up your own custom nameservers. The names for Cloudflare-branded nameservers are automatically assigned and cannot be changed.</p>
<p>Regardless of the type you choose, for these nameservers to be authoritative for your domain, you need to <a href="/dns/nameservers/update-nameservers/">update your domain nameservers</a>, typically where you registered your domain. Updating your nameservers is required to activate your domain on Cloudflare and use most of Cloudflare's <a href="/fundamentals/concepts/how-cloudflare-works/">application services</a>, such as proxying, caching, and security features.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="cloudflare-registrar">Cloudflare Registrar</h3>
@markup("md", "content/.markup/bodies/7617.md")
</aside>
<h3 id="standard-nameservers">Standard nameservers</h3>
<p>Unless your account has a specific <a href="/dns/additional-options/dns-zone-defaults/">DNS zone defaults</a> configuration, when you add a domain on a <a href="/dns/zone-setups/full-setup/">primary (full)</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary</a> DNS setup, Cloudflare automatically assigns two standard nameservers for your zone.</p>
<p>Standard nameservers are hosted on <code>ns.cloudflare.com</code> and follow the pattern <code>&lt;proper_name&gt;.ns.cloudflare.com</code>.</p>
<p>To know the reason behind these nameserver names, refer to <a href="https://blog.cloudflare.com/whats-the-story-behind-the-names-of-cloudflares-name-servers/">our blog</a>.</p>
<h3 id="advanced-nameservers">Advanced nameservers</h3>
<p>Enterprise accounts on <a href="/dns/foundation-dns/">Foundation DNS</a> have access to advanced nameservers.</p>
<p><a href="/dns/foundation-dns/advanced-nameservers/">Advanced nameservers</a> are hosted on <code>foundationdns.com</code>, <code>foundationdns.net</code>, and <code>foundationdns.org</code>.</p>
<p>Each zone that uses advanced nameservers is assigned a set of three nameservers names: <code>&lt;color&gt;.foundationdns.com</code>, <code>&lt;color&gt;.foundationdns.net</code>, and <code>&lt;color&gt;.foundationdns.org</code>.</p>
<h3 id="custom-nameservers">Custom nameservers</h3>
<p>With <a href="/dns/nameservers/custom-nameservers/">custom nameservers</a>, your nameservers are hosted on your own domain (or domains) and, in this sense, are not Cloudflare branded.</p>
<p>You provide fully qualified domain names — complete domain names like <code>ns1.example.com</code> — for your nameservers, and Cloudflare assigns one IPv4 and one IPv6 address to each.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7616.md")
</aside>
