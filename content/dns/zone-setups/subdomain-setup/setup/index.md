---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/
  description: Set up a subdomain zone in Cloudflare.
  full_title: Subdomain delegation and available setups · Cloudflare DNS docs
  head_html: <title>Subdomain delegation and available setups · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up a subdomain zone in Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/index.md"><meta property="og:title" content="Subdomain delegation and available setups · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up a subdomain zone in Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/#page","headline":"Subdomain delegation and available setups \u00b7 Cloudflare DNS docs","description":"Set up a subdomain zone in Cloudflare.","url":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/subdomain-setup/setup/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/8024.md")
</aside>
<p><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a> relies on a process known as delegation. When, in a parent domain such as <code>example.com</code>, an <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/">NS record</a> is created for a subdomain <code>blog.example.com</code>, this means that DNS management for the subdomain can be done separately, in its own <span class="nb-glossary-tooltip" title="DNS zone">DNS zone</span>.</p>
<pre tabindex="0"><code class="language-mermaid">    flowchart TD&#10;      accTitle: Example of parent zone and subdomains&#10;      A[&lt;code&gt;example.com&lt;/code&gt;] --&gt; B[&lt;code&gt;docs.example.com&lt;/code&gt;]&#10;      A[&lt;code&gt;example.com&lt;/code&gt;] --&gt; C[&lt;code&gt;blog.example.com&lt;/code&gt;]&#10;      subgraph Parent domain&#10;        A&#10;      end&#10;      subgraph Subdomains&#10;        B&#10;        C&#10;      end&#10;</code></pre>
<hr />
<h2 id="available-setups">Available setups</h2>
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
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-zones-in-partial-setup-are-not-delegated">Subdomain zones in partial setup are not delegated</h3>
@markup("md", "content/.markup/bodies/8023.md")
</aside>
<p>This table assumes zones that are in an <a href="/dns/zone-setups/reference/domain-status/">active status</a>. For example, if you need to add the parent zone to Cloudflare when its child zone already exists in a CNAME setup (partial), you can <a href="/dns/zone-setups/partial-setup/setup/#1-convert-your-zone-and-review-dns-records">convert the parent zone to a CNAME setup (partial)</a> while it is still in pending status.</p>
<hr />
<h2 id="how-to">How to</h2>
<p>Refer to the following guides to learn how to configure a subdomain setup depending on the setup used for the parent zone:</p>
<ul class="directory-listing"><li><a href="/dns/zone-setups/subdomain-setup/setup/parent-on-full/">Parent zone on full setup</a></li><li><a href="/dns/zone-setups/subdomain-setup/setup/parent-on-partial/">Parent zone on partial setup</a></li></ul>
<p>Although the how-to guides in this documentation are focused on both parent domains and subdomains existing in Cloudflare, it is also possible to achieve a subdomain setup in Cloudflare while the parent domain exists in a different DNS provider.</p>
<hr />
<h2 id="ssl-tls-certificates">SSL/TLS certificates</h2>
<p>When using subdomain setup, you should consider possible interactions between parent zone and child zone configurations that could impact <a href="/ssl/">SSL/TLS certificates</a> provisioning.</p>
<p>If a certificate is already active on the child zone for a specific hostname (<code>subdomain.example.com</code>), any certificate pack containing that exact hostname in the parent zone (<code>example.com</code>) will fail validation.</p>
<h2 id="access-applications">Access applications</h2>
<p>To use subdomain setups with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>, note that:</p>
<ul>
<li>
<p>If the child zone is in a pending state when you create the Access application, your configuration will not automatically apply when you activate the zone. You must also re-save the Access application once your subdomain setup is active.</p>
</li>
<li>
<p>If you split out a subdomain which already has an Access application, you will also need to re-save the Access application to associate it with the new child zone.</p>
</li>
</ul>
