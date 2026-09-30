---
cp9:
  canonical: https://developers.cloudflare.com/dns/nameservers/update-nameservers/
  description: Update your domain registrar to use Cloudflare nameservers.
  full_title: Update nameservers · Cloudflare DNS docs
  head_html: <title>Update nameservers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Update your domain registrar to use Cloudflare nameservers."><link rel="canonical" href="https://developers.cloudflare.com/dns/nameservers/update-nameservers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/nameservers/update-nameservers/index.md"><meta property="og:title" content="Update nameservers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update your domain registrar to use Cloudflare nameservers."><meta property="og:url" content="https://developers.cloudflare.com/dns/nameservers/update-nameservers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/nameservers/update-nameservers/#page","headline":"Update nameservers \u00b7 Cloudflare DNS docs","description":"Update your domain registrar to use Cloudflare nameservers.","url":"https://developers.cloudflare.com/dns/nameservers/update-nameservers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/nameservers/update-nameservers/
  schema: 1
---
<p>To use Cloudflare DNS as an authoritative DNS provider - be it in a <a href="/dns/zone-setups/full-setup/">primary (full)</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary</a> setup -, your domain nameservers must point to nameservers that you get from your Cloudflare account. Updating your nameservers is required to activate your domain on Cloudflare and use most of our <a href="/fundamentals/concepts/how-cloudflare-works/">application services</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="cloudflare-registrar">Cloudflare Registrar</h3>
@markup("md", "content/.markup/bodies/7608.md")
</aside>
<hr />
<h2 id="specific-processes">Specific processes</h2>
<p>Although Cloudflare will <a href="/dns/nameservers/#authoritative-nameservers-offering">provide you the nameservers</a> or allow you to create your own <a href="/dns/nameservers/custom-nameservers/">custom nameservers</a>, the final step to make Cloudflare an authoritative DNS provider for your domain may have to be done outside of Cloudflare. If you are not using <a href="/registrar/">Cloudflare Registrar</a>, consider which of the following sections correspond to your use case.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-or-advanced-nameservers">Custom or advanced nameservers</h3>
@markup("md", "content/.markup/bodies/7607.md")
</aside>
<h3 id="your-domain-uses-a-different-registrar">Your domain uses a different registrar</h3>
<p>If you have acquired your domain from a <a href="https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/">registrar</a> other than Cloudflare Registrar - and it has not been <a href="#your-domain-is-delegated">delegated</a> - you need to update your nameservers at your registrar.</p>
<p>If you do not know who your registrar is, you can use a Whois search, such as <a href="https://lookup.icann.org/">ICANN Lookup</a>. If the registrar indicated on your Whois search result is not a service that you have interacted directly with, you may <a href="#you-have-acquired-your-domain-from-a-reseller">have acquired your domain from a reseller</a>.</p>
<details class="nb-details" open><summary>Provider-specific instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7609.md")
</div></details>
<h3 id="you-have-acquired-your-domain-from-a-reseller">You have acquired your domain from a reseller</h3>
<p>Some services, such as website builders (<a href="https://support.squarespace.com/hc/articles/115003671428-Who-s-my-domain-provider">Squarespace</a>, for example), are not registrars but act as a <a href="https://www.icann.org/resources/pages/reseller-2013-05-03-en">reseller</a>, allowing you to buy domains directly from them.</p>
<p>In that case, you may have to update your nameservers in the reseller platform, not at the registrar.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7606.md")
</aside>
<h3 id="your-domain-is-delegated">Your domain is delegated</h3>
<p>If you are onboarding a subdomain <code>shop.example.com</code> as a <a href="/dns/zone-setups/subdomain-setup/">child domain</a>, the parent domain (<code>example.com</code>) must delegate authority to the child domain.</p>
<p>Delegation means that <code>shop.example.com</code> has specific <code>NS</code> records set up for it within the DNS records management of the parent zone (<code>example.com</code>).</p>
<p>If that is the case, when setting up your zone in Cloudflare or opting for a different set of <a href="/dns/nameservers/">nameservers</a>, you have to update the <code>NS</code> records in the parent domain, and not at the registrar.</p>
<hr />
<h2 id="restricted-nameserver-management">Restricted nameserver management</h2>
<p>Some providers act as registrars but do not expose nameserver settings. If you cannot change nameservers at your registrar or hosting platform, you can either:</p>
<ul>
<li>Transfer your domain to a registrar that allows nameserver management.</li>
<li>Transfer your domain to Cloudflare Registrar. All domains on <a href="/registrar/">Cloudflare Registrar</a> automatically use Cloudflare nameservers.</li>
<li>Use a <a href="/dns/zone-setups/partial-setup/">CNAME setup (partial)</a> instead. This option does not require nameserver changes and is available on Business and Enterprise plans.</li>
</ul>
<hr />
<h2 id="further-guidance">Further guidance</h2>
<p>This page covers specific workflows that customers who do not use Cloudflare Registrar<sup><a href="#footnote-1">1</a></sup> might have to follow to update their domain nameservers. For complete tutorials, refer to the pages below. Full setup is the most common option, and the only one available for customers on the Free or Pro plans.</p>
<ul class="directory-listing"><li><a href="/dns/zone-setups/full-setup/">Primary setup (Full)</a></li><li><a href="/dns/zone-setups/partial-setup/">CNAME setup (Partial)</a></li><li><a href="/dns/zone-setups/zone-transfers/">DNS Zone transfers</a></li><li><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a></li><li><a href="/dns/zone-setups/reference/">Reference</a></li><li><a href="/dns/zone-setups/troubleshooting/">Troubleshooting</a></li><li><a href="/dns/zone-setups/conversions/">DNS setup conversions</a></li><li><a href="/dns/zone-setups/removal/">Zone removal</a></li></ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">If you acquired your domain from Cloudflare Registrar, your domain already uses and must remain on Cloudflare nameservers. For details, refer to [Registrar](/registrar/faq/#can-i-use-my-own-third-party-nameservers).</li></ol></section>
