---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/
  description: Add a subdomain as a standalone zone in Cloudflare.
  full_title: Subdomain setup · Cloudflare DNS docs
  head_html: <title>Subdomain setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Add a subdomain as a standalone zone in Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/index.md"><meta property="og:title" content="Subdomain setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add a subdomain as a standalone zone in Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/#page","headline":"Subdomain setup \u00b7 Cloudflare DNS docs","description":"Add a subdomain as a standalone zone in Cloudflare.","url":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/subdomain-setup/
  schema: 1
---
<p>When you use a subdomain setup, you can manage the <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare configurations</a> for one or more subdomains separately from those associated with your <span class="nb-glossary-tooltip" title="apex domain">apex domain</span>. This means that, on your <a href="https://dash.cloudflare.com/?to=/:account/">account homepage</a>, you would find websites like <code>example.com</code> or <code>blog.example.com</code> listed as separate <span class="nb-glossary-tooltip" title="DNS zone">zones</span>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7904.md")
</aside>
<p>You might use this setup when you want to share access to a specific subdomain's settings with different teams, but have stricter controls on your apex domain. For example, a subdomain setup could allow your documentation team to manage the Cloudflare configuration for <code>docs.example.com</code>, while preventing them from adjusting any settings on <code>example.com</code>.</p>
<p>Subdomain setups are also useful when different subdomains require entirely different settings. For example, you may have different requirements for <code>docs.example.com</code>, <code>blog.example.com</code>, and <code>community.example.com</code>.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="setup-combinations">Setup combinations</h3>
@markup("md", "content/.markup/bodies/7903.md")
</aside>
<h3 id="access-applications">Access applications</h3>
<p>To use subdomain setups with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>, note that:</p>
<ul>
<li>
<p>If the child zone is in a pending state when you create the Access application, your configuration will not automatically apply when you activate the zone. You must also re-save the Access application once your subdomain setup is active.</p>
</li>
<li>
<p>If you split out a subdomain which already has an Access application, you will also need to re-save the Access application to associate it with the new child zone.</p>
</li>
</ul>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/dns/zone-setups/subdomain-setup/setup/">Setup</a></li><li><a href="/dns/zone-setups/subdomain-setup/dnssec/">Enable DNSSEC</a></li><li><a href="/dns/zone-setups/subdomain-setup/move-to-new-account/">Migrate to new account</a></li><li><a href="/dns/zone-setups/subdomain-setup/rollback/">Rollback</a></li></ul>
<h2 id="faq">FAQ</h2>
<h3 id="why-does-my-parent-zone-show-dns-queries-for-child-zone-hostnames">Why does my parent zone show DNS queries for child zone hostnames?</h3>
<p>If you have both a parent zone (for example, <code>example.com</code>) and a child subdomain zone (for example, <code>sub.example.com</code>) on Cloudflare, the parent zone's DNS analytics may show queries for hostnames belonging to the child zone.</p>
<p>This is normal DNS behavior — recursive resolvers query the parent zone first to get the referral (NS records) pointing to the child zone's nameservers. These referral queries appear in the parent zone's analytics even though the authoritative answer comes from the child zone.</p>
