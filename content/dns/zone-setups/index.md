---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/
  description: Available DNS zone setup types and how to configure them.
  full_title: DNS setups · Cloudflare DNS docs
  head_html: <title>DNS setups · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Available DNS zone setup types and how to configure them."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/index.md"><meta property="og:title" content="DNS setups · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available DNS zone setup types and how to configure them."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/#page","headline":"DNS setups \u00b7 Cloudflare DNS docs","description":"Available DNS zone setup types and how to configure them.","url":"https://developers.cloudflare.com/dns/zone-setups/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/
  schema: 1
---
<p>When using Cloudflare DNS, you have a few options for your DNS zone setup:</p>
<ul>
<li><a href="/dns/zone-setups/full-setup/">Primary setup (Full)</a> (most common): Use Cloudflare as your primary DNS provider and manage your DNS records on Cloudflare.</li>
<li><a href="/dns/zone-setups/partial-setup/">CNAME setup (Partial)</a>: Keep your primary DNS provider and only use Cloudflare's reverse proxy for individual subdomains.</li>
<li><a href="/dns/zone-setups/zone-transfers/">Zone transfers</a>: Use Cloudflare and another DNS provider together across your entire zone to increase availability and fault tolerance. DNS records will be transferred between providers using <a href="https://datatracker.ietf.org/doc/html/rfc5936">AXFR</a> or <a href="https://datatracker.ietf.org/doc/html/rfc1995">IXFR</a>.</li>
<li><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a>: With your apex domain (<code>example.com</code>) on a CNAME setup (partial) or primary setup (full), independently manage the settings for a delegated subdomain (<code>blog.example.com</code>) within a separate zone and, potentially, a separate account.</li>
</ul>
<p>When configuring a subdomain setup, its availability will depend on both the parent zone setup and the setup used for the child zone. A child zone holds DNS management for a delegated subdomain.</p>
<table>
<thead>
<tr>
<th>Parent zone</th>
<th>Child zone</th>
<th>Available</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td><a href="/dns/zone-setups/full-setup/">Full</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td>No</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td><a href="/dns/zone-setups/full-setup/">Full</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>For details, refer to <a href="/dns/zone-setups/subdomain-setup/setup/">setup</a>.</p>
<hr />
<h2 id="zone-status">Zone status</h2>
<p>The possible statuses for a zone are the following:</p>
<ul>
<li>Initializing</li>
<li>Pending</li>
<li>Active</li>
<li>Moved</li>
<li>Deleted</li>
<li>Purged</li>
</ul>
<p>For details on each status and how a zone can transition from one status to the other, consider the <a href="/dns/zone-setups/reference/domain-status/">Reference page</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-use-pending-zones-in-production">Do not use pending zones in production</h3>
@markup("md", "content/.markup/bodies/7553.md")
</aside>
<hr />
<h2 id="common-use-cases-and-availability">Common use cases and availability</h2>
<p>If you are unsure of which setup to use, consider the questions below for an overview of common use cases and their correspondence to each setup and <a href="https://www.cloudflare.com/plans/#overview">different pricing plans</a>.</p>
<details class="nb-details"><summary>Are you on a Free or Pro plan?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7554.md")
</div></details>
<details class="nb-details"><summary>Will you be using Cloudflare with other DNS providers?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7555.md")
</div></details>
<details class="nb-details"><summary>Do you need to manage subdomains separately?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7556.md")
</div></details>
<h2 id="configure-dns-only-zones-via-api">Configure DNS-only zones via API</h2>
<p>You can configure zones to operate in DNS-only mode (no HTTP proxying) at the account level or per zone using the API.</p>
<p><strong>Account-level default</strong> (applies to zones created after the setting is applied):</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;  https://api.cloudflare.com/client/v4/accounts/{account_id}/dns_settings \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&quot;zone_defaults&quot;:{&quot;zone_mode&quot;:&quot;dns_only&quot;}}&#x27;&#10;</code></pre>
<p><strong>Per-zone</strong> (for existing zones):</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;  https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_settings \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&quot;zone_mode&quot;:&quot;dns_only&quot;}&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7552.md")
</aside>
