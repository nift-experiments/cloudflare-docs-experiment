---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/
  description: Delegate domain control validation to Cloudflare.
  full_title: Delegated DCV — Domain Control Validation — SSL/TLS · Cloudflare SSL/TLS docs
  head_html: <title>Delegated DCV — Domain Control Validation — SSL/TLS · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Delegate domain control validation to Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/index.md"><meta property="og:title" content="Delegated DCV — Domain Control Validation — SSL/TLS · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Delegate domain control validation to Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/#page","headline":"Delegated DCV \u2014 Domain Control Validation \u2014 SSL/TLS \u00b7 Cloudflare SSL/TLS docs","description":"Delegate domain control validation to Cloudflare.","url":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/
  schema: 1
---
<p>Delegated DCV allows zones with <a href="/dns/zone-setups/partial-setup/">partial DNS setups</a> - meaning authoritative DNS is not provided by Cloudflare - to delegate the DCV process to Cloudflare.</p>
<p>DCV Delegation requires you to place a one-time record that allows Cloudflare to auto-renew all future certificate orders, so that there’s no manual intervention at the time of the renewal.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14194.md")
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
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
</tr>
</tbody>
</table>
<h2 id="when-to-use">When to use</h2>
<p>You should use Delegated DCV when all of the following conditions are true:</p>
<ul>
<li>Your zone is using a <a href="/dns/zone-setups/partial-setup/">partial DNS setup</a>.</li>
<li>Cloudflare is not already <a href="/ssl/edge-certificates/changing-dcv-method/">performing DCV automatically</a>.</li>
<li>Your zone is using an <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced certificate</a>.</li>
<li>The Certificate Authority is either Google Trust Services, SSL.com, or Let's Encrypt</li>
</ul>
<h3 id="aspects-to-keep-in-mind">Aspects to keep in mind</h3>
<p>As explained in the <a href="https://blog.cloudflare.com/introducing-dcv-delegation/">announcement blog post</a>, currently, you can only delegate DCV to one provider at a time. This means:</p>
<ul>
<li>
<p>If you also issue publicly trusted certificates for the same hostname for your <a href="/ssl/concepts/#origin-certificate">origin server</a>, this will no longer be possible. You can use <a href="/ssl/origin-configuration/origin-ca/">Cloudflare origin CA certificates</a> instead.</p>
</li>
<li>
<p>If your zone is using multiple CDN providers, you might want to use an alternative <a href="/ssl/edge-certificates/changing-dcv-method/methods/">method</a>. This is because, once the DCV delegation is configured for Cloudflare, only Cloudflare will be able to perform DCV on your behalf, blocking your external CDN providers from doing the same.</p>
</li>
</ul>
<h2 id="setup">Setup</h2>
<p>To set up Delegated DCV:</p>
<ol>
<li>Order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">advanced certificate</a> for your zone, choosing <code>TXT</code> as the <strong>Certificate validation method</strong>.</li>
<li>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page, go to <strong>DCV Delegation for Partial Zones</strong>.</li>
<li>Copy the Cloudflare validation URL.</li>
<li>At your authoritative DNS provider, create <code>CNAME</code> record(s) considering the following:</li>
</ol>
<ul>
<li>If your certificate only covers the apex domain and a wildcard, you only need to create a single <code>CNAME</code> record for your apex domain. Any direct subdomains will be covered as well.</li>
</ul>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/14195.md")
</div>
<ul>
<li>If your certificate also covers subdomains specified by their name, you will need to add multiple <code>CNAME</code> records to your authoritative DNS provider, one for each specific subdomain.</li>
</ul>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/14196.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="remove-conflicting-acme-challenge-txt-records">Remove conflicting `_acme-challenge` TXT records</h3>
@markup("md", "content/.markup/bodies/14193.md")
</aside>
<p>Once the <code>CNAME</code> records are in place, Cloudflare will add TXT DCV tokens for every hostname on the Advanced certificate that has a DCV delegation record in place, as long as the zone is <a href="/dns/zone-setups/reference/domain-status/">active</a> on Cloudflare.</p>
<p>Because DCV happens regularly, do not remove the <code>CNAME</code> record(s) at your authoritative DNS provider. Otherwise, Cloudflare will not be able to perform DCV on your behalf and your certificate will not be issued.</p>
<h2 id="further-details">Further details</h2>
<h3 id="testing">Testing</h3>
<p>If you use a <code>dig</code> command to test, you should only be able see the placed tokens if the certificate is up for issuance.</p>
<p>This is because Cloudflare places the tokens when needed and then cleans them up.</p>
<pre tabindex="0"><code class="language-sh">dig TXT +noadditional +noquestion +nocomments +nocmd +nostats _acme-challenge.example.com. @1.1.1.1&#10;&#10;_acme-challenge.example.com. 3600    IN    CNAME    example.com.&lt;COPIED_VALIDATION_URL&gt;&#10;</code></pre>
<h3 id="renewal">Renewal</h3>
<p>If a hostname becomes unreachable during certificate renewal time, the certificate will not be able to be renewed automatically via Delegated DCV. Should you need to renew a certificate for a hostname that is not resolving currently, you can send a PATCH request to <a href="/api/resources/ssl/subresources/verification/methods/edit/">the changing DCV method API endpoint</a> and change the method to TXT to proceed with manual renewal per <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">the TXT DCV method</a>.</p>
<p>Once the hostname becomes resolvable again, <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a> will resume working as expected.</p>
<h3 id="moved-domains">Moved domains</h3>
<p>If you <a href="/fundamentals/manage-domains/move-domain/">move your zone to another account</a>, you will need to update the <code>CNAME</code> record at your authoritative DNS provider with a new validation URL.</p>
