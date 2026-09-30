---
cp9:
  canonical: https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/
  description: Learn about how Cloudflare decides which certificate and associated SSL/TLS settings to apply to individual hostnames.
  full_title: Certificate and hostname priority · Cloudflare SSL/TLS docs
  head_html: <title>Certificate and hostname priority · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about how Cloudflare decides which certificate and associated SSL/TLS settings to apply to individual hostnames."><link rel="canonical" href="https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/index.md"><meta property="og:title" content="Certificate and hostname priority · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about how Cloudflare decides which certificate and associated SSL/TLS settings to apply to individual hostnames."><meta property="og:url" content="https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/#page","headline":"Certificate and hostname priority \u00b7 Cloudflare SSL/TLS docs","description":"Learn about how Cloudflare decides which certificate and associated SSL/TLS settings to apply to individual hostnames.","url":"https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/reference/certificate-and-hostname-priority/
  schema: 1
---
<p>When a new certificate is created, Cloudflare first deploys the certificate and then serves it.</p>
<hr />
<h2 id="certificate-deployment">Certificate deployment</h2>
<p>For any given hostname, Cloudflare uses the following order to determine which certificate (and associated TLS settings) to apply to that hostname:</p>
<ol>
<li>
<p><strong>Hostname specificity</strong>: A specific subdomain certificate (<code>www.example.com</code>) would take precedence over a wildcard certificate (<code>*.example.com</code>) for requests to <code>www.example.com</code>.</p>
</li>
<li>
<p><strong>Zone specificity</strong>: A specific subdomain certificate (<code>www.example.com</code>) would take precedence over a custom hostname certificate if the domain is active as a zone on Cloudflare.</p>
</li>
<li>
<p><strong>Certificate priority</strong>: If the hostname is the same, certain types of certificates take precedence over others.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Priority</th>
<th>Certificate Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><a href="/ssl/keyless-ssl/">Keyless SSL</a></td>
</tr>
<tr>
<td>2</td>
<td><a href="/ssl/edge-certificates/custom-certificates/">Custom Legacy</a></td>
</tr>
<tr>
<td>3</td>
<td><a href="/ssl/edge-certificates/custom-certificates/">Custom Modern</a></td>
</tr>
<tr>
<td>4</td>
<td><a href="/cloudflare-for-platforms/cloudflare-for-saas/">Custom Hostname (Cloudflare for SaaS)</a></td>
</tr>
<tr>
<td>5</td>
<td><a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced</a></td>
</tr>
<tr>
<td>6</td>
<td><a href="/ssl/edge-certificates/additional-options/total-tls/">Advanced - Total TLS</a></td>
</tr>
<tr>
<td>7</td>
<td><a href="/ssl/edge-certificates/universal-ssl/">Universal</a></td>
</tr>
</tbody>
</table>
<ol start="4">
<li><strong>Certificate expiration</strong>: The most recently ordered certificate takes precedence unless a certificate deletion has occurred. If and when a certificate is deleted, the certificate with the latest expiration date is deployed.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13984.md")
</aside>
<hr />
<h2 id="certificate-presentation">Certificate presentation</h2>
<p>Cloudflare uses the following order to determine the certificate and settings used during a TLS handshake:</p>
<ol>
<li><strong>SNI match</strong>: Certificates and settings that match the SNI hostname <em>exactly</em> take precedence.</li>
<li><strong>SNI wildcard match</strong>: If there is not an exact match between the hostname and SNI hostname, Cloudflare uses certificates and settings that match an SNI wildcard.</li>
<li><strong>IP address</strong>: If no SNI is presented, Cloudflare uses certificate based on the IP address (the hostname can support TLS handshakes made without SNI).</li>
</ol>
<hr />
<h2 id="hostname-priority">Hostname priority</h2>
<p>When multiple <span class="nb-glossary-tooltip" title="proxy status">proxied DNS records</span> exist for a hostname, in multiple <span class="nb-glossary-tooltip" title="zone">zones</span> — usually due to <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> — only one record will control the zone settings and associated origin server.</p>
<p>Cloudflare determines this priority in the following order, assuming each record exists and is proxied (orange-clouded):</p>
<ol>
<li>
<p><strong>Exact hostname match</strong>:</p>
<ol>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">New custom hostname</a> (belonging to a SaaS provider)</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/">Legacy custom hostname</a> (belonging to a SaaS provider)</li>
<li><a href="/dns/proxy-status/">DNS</a> (belonging to the logical DNS zone)</li>
</ol>
</li>
<li>
<p><strong>Wildcard hostname match</strong>:</p>
<ol>
<li>DNS (belonging to the logical DNS zone)</li>
<li>New custom hostname (belonging to a SaaS provider)</li>
</ol>
</li>
</ol>
<p>If a hostname resource record is not proxied (gray-clouded) for a zone on Cloudflare, that zone's settings are not applied and any settings configured at the associated origin are applied instead. This origin could be another zone on Cloudflare or any other server.</p>
<h3 id="example-scenarios">Example scenarios</h3>
<h4 id="scenario-1">Scenario 1</h4>
<p>Customer1 uses Cloudflare as authoritative DNS for the zone <code>shop.example.com</code>. Customer2 is a SaaS provider that creates and successfully <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">verifies the new custom hostname</a> <code>shop.example.com</code>. Afterward, traffic starts routing over Customer2's zone:</p>
<ul>
<li>If Customer1 wants to regain control of their zone, Customer1 contacts Customer2 and requests them to delete the custom hostname record. Customer1 should make sure to have their record target updated to something other than the SaaS provider target, otherwise Customer1 would get a <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/"><code>1014</code> error</a>.</li>
<li>If Customer1 already has a proxied record for <code>www.example.com</code> when Customer2 creates and verifies a new custom hostname <code>www.example.com</code>, <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a> applies.</li>
<li>If Customer1 already has a proxied record for <code>www.example.com</code> in a legacy custom hostname setup (with another SaaS provider, Customer3) and Customer2 creates and verifies a new wildcard custom hostname for <code>*.example.com</code>, legacy custom hostname on Customer3 platform takes precedence due to exact hostname match.</li>
</ul>
<h4 id="scenario-2">Scenario 2</h4>
<p>A customer has a <a href="/dns/proxy-status/">proxied</a> DNS record for their domain. The customer's zone on Cloudflare is using a Free plan.</p>
<p>This customer is also using a SaaS provider that uses Cloudflare for SaaS. The SaaS provider is using a Cloudflare Enterprise plan.</p>
<p>If the provider is using a wildcard custom hostname, then the original customer's plan limits will take precedence over the provider's plan limits (Cloudflare will treat the zone as a Free zone). To apply the Enterprise limits through Cloudflare for SaaS, the original customer's zone would need to either use a <a href="/dns/proxy-status/">DNS-only</a> record or the SaaS provider would need to use an exact hostname match.</p>
