---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/
  description: Delegate subdomains to external DNS providers.
  full_title: Delegate subdomains · Cloudflare DNS docs
  head_html: <title>Delegate subdomains · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Delegate subdomains to external DNS providers."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/index.md"><meta property="og:title" content="Delegate subdomains · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Delegate subdomains to external DNS providers."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/#page","headline":"Delegate subdomains \u00b7 Cloudflare DNS docs","description":"Delegate subdomains to external DNS providers.","url":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/how-to/subdomains-outside-cloudflare/
  schema: 1
---
<p>Subdomain delegation allows different individuals, teams, or organizations to manage different subdomains of a site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7812.md")
</aside>
<p>For instance, consider <code>example.com</code> as a Cloudflare domain with <code>www.example.com</code> managed in Cloudflare's <strong>DNS</strong> app and <code>blog.example.com</code> delegated to nameservers outside of Cloudflare. In this example, <code>blog.example.com</code> can now be managed by individuals who do not have access to Cloudflare credentials for the <code>example.com</code> domain.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7811.md")
</aside>
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
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="delegate-a-subdomain-outgoing">Delegate a subdomain (outgoing)</h2>
<p>To delegate a subdomain such as <code>blog.example.com</code>, tell DNS resolvers where to find the zone file:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Select the domain that contains the subdomain to be delegated.</li>
<li>Go to the <strong>DNS Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>Create <code>NS</code> records for the subdomain. For example:
<ul>
<li><code>blog.example.com NS ns1.externalhost.com</code></li>
<li><code>blog.example.com NS ns2.externalhost.com</code></li>
<li><code>blog.example.com NS ns3.externalhost.com</code></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7810.md")
</aside>
5. (Optional) If the delegated nameserver has DNSSEC enabled, [add the `DS` record](/dns/dnssec/#1-activate-dnssec-in-cloudflare) in Cloudflare.
<h3 id="limits">Limits</h3>
<p>When creating NS records, there are limits on the number of nameservers that can be associated with a single delegation name.</p>
<p>According to DNS standards defined in <a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>, a delegation should not include more than seven nameserver names for the same delegation name.</p>
<p>To align with these standards and maintain platform stability:</p>
<ul>
<li>Cloudflare supports up to 10 NS records per delegation name, but the best practice is to keep the set at seven or fewer.</li>
<li>Creating more than 10 NS records for the same name is not supported. Requests that exceed this limit may be rejected or fail validation.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@input("content/.markup/bodies/7814.md")
</div></details>
<h2 id="delegate-a-subdomain-incoming">Delegate a subdomain (incoming)</h2>
<p>To delegate a subdomain from an external DNS provider to Cloudflare, refer to <a href="/dns/zone-setups/subdomain-setup/setup/">subdomain setups</a>.</p>
