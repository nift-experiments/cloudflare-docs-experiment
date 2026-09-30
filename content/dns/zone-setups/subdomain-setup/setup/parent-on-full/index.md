---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-full/
  description: Set up subdomain zone when parent uses full setup.
  full_title: Set up a child zone in Cloudflare with parent on full setup · Cloudflare DNS docs
  head_html: <title>Set up a child zone in Cloudflare with parent on full setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up subdomain zone when parent uses full setup."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-full/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-full/index.md"><meta property="og:title" content="Set up a child zone in Cloudflare with parent on full setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up subdomain zone when parent uses full setup."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-full/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-full/#page","headline":"Set up a child zone in Cloudflare with parent on full setup \u00b7 Cloudflare DNS docs","description":"Set up subdomain zone when parent uses full setup.","url":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-full/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/subdomain-setup/setup/parent-on-full/
  schema: 1
---
<p>When the parent zone is using a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a><sup><a href="#footnote-1">1</a></sup>, the steps to set up your child zone depend on whether the subdomain already exists in the parent domain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8022.md")
</aside>
<h2 id="subdomain-does-not-exist">Subdomain does not exist</h2>
<p>If you have not yet created DNS records covering your subdomain in the parent zone:</p>
<ol>
<li>
<p>Add the subdomain to a Cloudflare account as a new zone. It can be the same account where the parent zone exists or a different one.</p>
</li>
<li>
<p>Complete the configuration accordingly for <a href="/dns/zone-setups/full-setup/setup/">full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">secondary</a> setup.</p>
</li>
<li>
<p>Get the nameserver names for the subdomain. These can be found within your newly created child zone on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page, and will <strong>not</strong> be the same nameservers as the ones used in the parent zone.</p>
</li>
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page of the parent zone, <a href="/dns/manage-dns-records/how-to/create-dns-records/">add</a> two <code>NS</code> records for the subdomain you want to delegate.</p>
<p>For example, if you delegated <code>www.example.com</code>, you might add the following records to <code>example.com</code>:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>Content</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>NS</code></td>
<td>www</td>
<td>john.ns.cloudflare.com</td>
</tr>
<tr>
<td><code>NS</code></td>
<td>www</td>
<td>melinda.ns.cloudflare.com</td>
</tr>
</tbody>
</table>
<ol start="5">
<li>
<p>After a few minutes, the child zone will be active.</p>
</li>
<li>
<p>Create the various DNS records needed for your child zone.</p>
</li>
<li>
<p>(Optional) <a href="/dns/zone-setups/subdomain-setup/dnssec/">Enable DNSSEC</a> on the child zone.</p>
</li>
</ol>
<h2 id="subdomain-already-exists">Subdomain already exists</h2>
<p>If you have already created DNS records covering your subdomain in the parent zone:</p>
<ol>
<li>
<p>Add the subdomain to a Cloudflare account as a new zone. It can be the same account where the parent zone exists or a different one.</p>
</li>
<li>
<p>Complete the configuration accordingly for <a href="/dns/zone-setups/full-setup/setup/">full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">secondary</a> setup.</p>
</li>
<li>
<p>In your child zone, make sure you have all DNS records that relate to the subdomain. This includes all DNS records deeper than the delegated subdomain. For example, if you are delegating <code>www.example.com</code>, you should also move over records for <code>api.www.example.com</code>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8021.md")
</aside>
<ol start="4">
<li>
<p>If the parent zone is on Cloudflare, make sure that you migrate over any settings (<a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/">Rules</a>, <a href="/workers/">Workers</a>, and more) that might be needed for the child zone.</p>
</li>
<li>
<p>In the child zone, <a href="/ssl/edge-certificates/advanced-certificate-manager/">order an advanced SSL certificate</a> that covers the child subdomain and any deeper subdomains (if present).</p>
</li>
<li>
<p>Get the nameserver names for the subdomain. These can be found within your newly created child zone on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page, and will <strong>not</strong> be the same nameservers as the ones used in the parent zone.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8020.md")
</aside>
<ol start="7">
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page of the parent zone, update existing address records (<code>A/AAAA</code>) on your subdomain to <code>NS</code> records. If you only have one address record, update the existing one and add a new <code>NS</code> record. If you have multiple address records, update any two of them.</p>
<p>For example, to delegate the subdomain <code>www.example.com</code>, the updated records in the parent zone <code>example.com</code> should contain <code>NS</code> records similar to the following:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>Content</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>NS</code></td>
<td>www</td>
<td>john.ns.cloudflare.com</td>
</tr>
<tr>
<td><code>NS</code></td>
<td>www</td>
<td>adam.ns.cloudflare.com</td>
</tr>
</tbody>
</table>
<p>In this example, <code>john.ns.cloudflare.com</code> and <code>adam.ns.cloudflare.com</code> represent the subdomain nameservers that you got from step 6.</p>
<ol start="8">
<li>
<p>Flush the address records of your subdomain in public resolvers (<a href="https://1.1.1.1/purge-cache/">1.1.1.1</a> and <a href="https://developers.google.com/speed/public-dns/cache">8.8.8.8</a>).</p>
</li>
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page of the parent zone, <a href="/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records">delete</a> all the remaining records on the delegated subdomain, except the <code>NS</code> records that you created in step 7.</p>
<p>Also delete all DNS records deeper than the delegated subdomain. For example, if you are delegating <code>www.example.com</code>, records for <code>api.www.example.com</code> should only exist in the new child zone.</p>
</li>
<li>
<p>Within a short period of time, the child zone should be active.</p>
</li>
<li>
<p>(Optional) <a href="/dns/zone-setups/subdomain-setup/dnssec/">Enable DNSSEC</a> on the child zone.</p>
</li>
</ol>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Meaning that Cloudflare is your Authoritative DNS provider.</li></ol></section>
