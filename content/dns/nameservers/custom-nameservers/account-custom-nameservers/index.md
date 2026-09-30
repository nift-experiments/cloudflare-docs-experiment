---
cp9:
  canonical: https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/
  description: With account-level custom nameservers, you can use the same custom nameservers for different zones in the account. The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare.
  full_title: Account custom nameservers · Cloudflare DNS docs
  head_html: <title>Account custom nameservers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="With account-level custom nameservers, you can use the same custom nameservers for different zones in the account. The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/index.md"><meta property="og:title" content="Account custom nameservers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With account-level custom nameservers, you can use the same custom nameservers for different zones in the account. The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/#page","headline":"Account custom nameservers \u00b7 Cloudflare DNS docs","description":"With account-level custom nameservers, you can use the same custom nameservers for different zones in the account. The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare.","url":"https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/nameservers/custom-nameservers/account-custom-nameservers/
  schema: 1
---
<p>Account custom nameservers (ACNS) allow you to define account-level custom nameservers and use them for different zones within a Cloudflare account.</p>
<p>ACNS are organized in different sets (<code>ns_set</code>) and ACNS names can be provided by any domain, even if the domain does not exist as a zone in Cloudflare.</p>
<p>For instance, if the ACNS are <code>ns1.example.com</code> and <code>ns2.vanity.test</code>, the domains <code>example.com</code> and <code>vanity.test</code> are not required to be zones in Cloudflare.</p>
<h2 id="availability">Availability</h2>
<p>Account custom nameservers are available for customers on Business (after <a href="/support/contacting-cloudflare-support/">contacting Cloudflare Support</a>) or Enterprise plans. Once configured, account custom nameservers can be used by all zones in the account, regardless of the zone plan. Via API or on the dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7874.md")
</aside>
<h2 id="configuration-conditions">Configuration conditions</h2>
<p>For this configuration to be possible, a few conditions apply:</p>
<ul>
<li>You can create up to five different account custom nameserver sets. Each nameserver set must have between two and five different nameserver names (<code>ns_name</code>), and each name cannot belong to more than one set. For example, if <code>ns1.example.com</code> is part of <code>ns_set 1</code> it cannot be part of <code>ns_set 2</code> or vice versa.</li>
<li><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a> or <a href="/dns/additional-options/reverse-zones/">reverse zones</a> can use account custom nameservers as long as they use a different nameserver set (<code>ns_set</code>) than their parent, child, or any other zone in their direct hierarchy tree.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7873.md")
</aside>
<ul>
<li>Choosing a set from <code>ns_set 1</code> through <code>ns_set 5</code> will influence how Cloudflare assigns nameservers to your new zones if you configure <a href="/dns/nameservers/nameserver-options/#dns-zone-defaults">DNS zone defaults</a>.</li>
</ul>
<h2 id="enable-account-custom-nameservers">Enable account custom nameservers</h2>
<h3 id="1-set-up-acns-names-and-sets"><ol>
<li>Set up ACNS names and sets</li>
</ol></h3>
<ol>
<li>Create ACNS names and sets:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7877.md")
</div></div>
<p>Cloudflare will assign an IPv4 and an IPv6 address to each ACNS name, and these nameservers will be listed as options that you can <a href="#2-use-acns-on-existing-zones">use on existing zones</a> or <a href="#3-optional-make-acns-default-for-new-zones">set up as default for new zones in the account</a>.</p>
<ol start="2">
<li>Make sure <code>A/AAAA</code> records with the assigned IPv4 and IPv6 exist at the authoritative DNS of the domain that provides the ACNS names.
<ul>
<li>
<p>If the domain uses Cloudflare DNS, the respective <code>A</code> and <code>AAAA</code> records are automatically created.</p>
</li>
<li>
<p>If the domain or domains that are used for the account custom nameservers do not exist within the same account, you must manually create the <code>A/AAAA</code> records on the configured nameserver names (for example, <code>ns1.example.com</code>) at the authoritative DNS provider.</p>
</li>
</ul>
</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7878.md")
</div>
<ol start="3">
<li>Update the registrar of the domain that provides the ACNS names. This step depends on whether you are using <a href="/registrar/">Cloudflare Registrar</a>:
<ul>
<li>
<p>If you are using Cloudflare Registrar for the domain that provides the ACNS names, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to add the account custom nameservers and IP addresses as glue records to the domain.</p>
</li>
<li>
<p>If you are not using Cloudflare Registrar for the domain that provides the ACNS names, add the account custom nameservers and IP addresses to your domain's registrar as glue records (<a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>). If you do not add these records, DNS lookups for your domain will fail.</p>
</li>
</ul>
</li>
</ol>
<h3 id="2-use-acns-on-existing-zones"><ol start="2">
<li>Use ACNS on existing zones</li>
</ol></h3>
<ol>
<li>Choose an ACNS set as custom nameservers for a zone:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7881.md")
</div></div>
<ol start="2">
<li>Make sure the nameservers are updated:</li>
</ol>
<ul>
<li>If your domain uses <a href="/registrar/">Cloudflare Registrar</a>, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to update your nameservers.</li>
<li>If your domain uses a different registrar, update the nameservers at your registrar to use the account custom nameservers.</li>
<li>If your zone is delegated, update the corresponding <code>NS</code> record at the parent zone.</li>
</ul>
<h3 id="3-optional-make-acns-default-for-new-zones"><ol start="3">
<li>(Optional) Make ACNS default for new zones</li>
</ol></h3>
<p>To make ACNS the default option for all new zones added to your account from now on:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7884.md")
</div></div>
<h2 id="disable-account-custom-nameservers">Disable account custom nameservers</h2>
<h3 id="1-remove-acns-assignment-from-zones"><ol>
<li>Remove ACNS assignment from zones</li>
</ol></h3>
<p>To remove ACNS from a zone, first update your nameservers to stop using ACNS:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7887.md")
</div></div>
<h3 id="2-delete-acns-names-or-sets"><ol start="2">
<li>Delete ACNS names or sets</li>
</ol></h3>
<p>Following the <a href="#configuration-conditions">configuration conditions</a>, each set must have between two and five different nameserver names. When you delete all names or leave a set with only one nameserver name, the set will no longer be listed as an option for the zones in your account.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7890.md")
</div></div>
