---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/
  description: How wildcard DNS records work on Cloudflare.
  full_title: Wildcard DNS records · Cloudflare DNS docs
  head_html: <title>Wildcard DNS records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="How wildcard DNS records work on Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/index.md"><meta property="og:title" content="Wildcard DNS records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How wildcard DNS records work on Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/#page","headline":"Wildcard DNS records \u00b7 Cloudflare DNS docs","description":"How wildcard DNS records work on Cloudflare.","url":"https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/reference/wildcard-dns-records/
  schema: 1
---
<p>Normal DNS records map a domain name to one or multiple IP addresses or other associated resources to a specific domain name (a one-to-many mapping). Wildcard DNS records allow you to have a many-to-many mapping, for example if you had hundreds or thousands of subdomains you wanted to point to the same resources.</p>
<p>Within Cloudflare, wildcard DNS records can be either <a href="/dns/proxy-status/">proxied or DNS-only</a>.</p>
<h2 id="create-a-wildcard-record">Create a Wildcard record</h2>
<p>To create a wildcard DNS record, <a href="/dns/manage-dns-records/how-to/create-dns-records/">create a DNS record</a> with an <code>*</code> in the <strong>Name</strong> field.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7770.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7769.md")
</aside>
<p>You can also create a wildcard DNS record specifically for a deeper subdomain. For example, if you wanted to create a wildcard record on <code>*.www.example.com</code>, you would create a record with <code>*.www</code> in the name field.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/7771.md")
</div>
<h3 id="aspects-to-consider">Aspects to consider</h3>
<h4 id="wildcards-are-only-supported-on-the-first-label">Wildcards are only supported on the first label</h4>
<p>This means that a hostname such as <code>subdomain.*.example.com</code> is not a wildcard on the level of the asterisk character. If you create a DNS record with that name, the asterisk is interpreted as the literal character <code>*</code> and not as the wildcard operator.</p>
<h4 id="wildcards-are-multi-level-by-default">Wildcards are multi-level by default</h4>
<p>If you create a DNS record on <code>*.*.example.com</code>, only the first asterisk is interpreted as a wildcard while the second one is interpreted as the literal <code>*</code> character. A record <code>*.example.com</code> is already multi-level by default, meaning it would cover <code>abc.example.com</code> as well as <code>123.abc.example.com</code>, as long as there are no <a href="#specific-dns-records-take-precedence-over-wildcard-records">specific DNS records</a> that would take precedence.</p>
<h4 id="specific-dns-records-take-precedence-over-wildcard-records">Specific DNS records take precedence over wildcard records</h4>
<p>A wildcard record applies only when no exact record exists at the queried name. If a record or delegation exists, the wildcard does not apply.</p>
  <details class="nb-details"><summary>Example 1 - specific or below</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7772.md")
</div></details>
<pre tabindex="0"><code>&lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;Example 2 - implicit parent&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
@markup("md", "content/.markup/bodies/7773.md")
</div></details>
<h2 id="availability">Availability</h2>
<p>Customers on all plans can create and proxy wildcard DNS records.</p>
<h2 id="limitations">Limitations</h2>
<p>If you are using a <a href="/dns/zone-setups/partial-setup/">CNAME setup (partial)</a> for your DNS, Cloudflare does not automatically provision SSL/TLS certificates for your wildcard record.</p>
<p>For wildcard hostname certificates, certificate issuance and renewal varies based on the type of certificate you are using:</p>
<ul>
<li><strong>Universal</strong>: Perform DCV using <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT validation method</a>.</li>
<li><strong>Advanced</strong>: In most cases, you can opt for <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>, which greatly simplifies certificate management.</li>
</ul>
<p>If you cannot use Delegated DCV, you need to use <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT based DCV</a> for certificate issuance and renewal. This means you will need to place one TXT DCV token for every hostname on the certificate. If one or more of the hostnames on the certificate fails to validate, the certificate will not be issued or renewed.</p>
<p>This means that a wildcard certificate covering <code>example.com</code> and <code>*.example.com</code> will require two DCV tokens to be placed at the authoritative DNS provider. Similarly, a certificate with five hostnames in the SAN (including a wildcard) will require five DCV tokens to be placed at the authoritative DNS provider.</p>
<h2 id="additional-information">Additional information</h2>
<p>For more information on wildcard records — as well as more details about their limitations — refer to the <a href="https://blog.cloudflare.com/wildcard-proxy-for-everyone/">introductory blog post</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">An opt-in configuration available for Enterprise customers.</li></ol></section>
