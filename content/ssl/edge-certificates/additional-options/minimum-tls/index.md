---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/
  description: Set the minimum TLS version for connections to your domain.
  full_title: Minimum TLS Version · Cloudflare SSL/TLS docs
  head_html: <title>Minimum TLS Version · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set the minimum TLS version for connections to your domain."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/index.md"><meta property="og:title" content="Minimum TLS Version · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set the minimum TLS version for connections to your domain."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/#page","headline":"Minimum TLS Version \u00b7 Cloudflare SSL/TLS docs","description":"Set the minimum TLS version for connections to your domain.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/minimum-tls/
  schema: 1
---
<p>Minimum TLS Version only allows HTTPS connections from visitors that support the selected TLS protocol version or newer.</p>
<p>For example, if TLS 1.1 is selected, visitors attempting to connect using TLS 1.0 will be rejected. Visitors attempting to connect using TLS 1.1, 1.2, or 1.3 (<a href="/ssl/edge-certificates/additional-options/tls-13/">if enabled</a>) will be allowed to connect.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14132.md")
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
<tr>
<td>Per-hostname</td>
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
<td>Included with <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a></td>
</tr>
</tbody>
</table>
<p>It is not possible to configure minimum TLS version for <a href="/pages/">Cloudflare Pages</a> hostnames.</p>
<h2 id="how-to-disable-tls-1-0">How to disable TLS 1.0</h2>
<p>You can disable TLS 1.0 by choosing a higher minimum TLS version.</p>
<p>All users can apply this configuration to all hostnames in their zones following the steps under <a href="#zone-level">zone-level</a>.</p>
<p>If you have an <a href="/ssl/edge-certificates/advanced-certificate-manager/#advanced-certificate-manager">Advanced Certificate Manager</a> subscription, you also have the option to disable TLS 1.0 (or other versions) with a <a href="#per-hostname">per-hostname</a> setup.</p>
<h2 id="setup">Setup</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14131.md")
</aside>
<h3 id="zone-level">Zone-level</h3>
<p>To manage the TLS version applied to your whole zone when proxied through Cloudflare:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14135.md")
</div></div>
<h3 id="per-hostname">Per-hostname</h3>
<p><a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> users also have the option to specify minimum TLS versions per specific hostnames in their Cloudflare zone.</p>
<p>This is currently only available via the API:</p>
<ul>
<li>Use the <a href="/api/resources/hostnames/subresources/settings/subresources/tls/methods/update/">Edit TLS setting for hostname</a> endpoint to specify different values for <code>min_tls_version</code>.</li>
<li>Use the <a href="/api/resources/hostnames/subresources/settings/subresources/tls/methods/delete/">Delete TLS setting for hostname</a> endpoint to clear previously defined <code>min_tls_version</code> setting.</li>
</ul>
<p>Cloudflare uses the <a href="/ssl/reference/certificate-and-hostname-priority/">hostname priority logic</a> to determine which setting to apply.</p>
<p>In the following example, the minimum TLS version for a specific hostname will be set to <code>1.2</code>. Replace the zone ID, hostname, and authentication placeholders with your information, and adjust the <code>value</code> field with your chosen TLS version.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;value&quot;: &quot;1.2&quot;&#10;}&#x27;</code></pre>
<h3 id="cloudflare-for-saas">Cloudflare for SaaS</h3>
<p>If you are a SaaS provider looking to configure minimum TLS version for your custom hostnames, refer to the Cloudflare for SaaS <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/#minimum-tls-version">TLS management</a>.</p>
<h2 id="test-supported-tls-versions">Test supported TLS versions</h2>
<p>To test supported TLS versions, attempt a request to your website or application while specifying a TLS version.</p>
<p>For example, to test TLS 1.1, use the <code>curl</code> command below. Replace <code>www.example.com</code> with your Cloudflare domain and hostname.</p>
<pre tabindex="0"><code class="language-sh">curl https://www.example.com -svo /dev/null --tls-max 1.1&#10;</code></pre>
<p>If the TLS version you are testing is blocked by Cloudflare, the TLS handshake is not completed and returns an error:</p>
<p><code>* error:1400442E:SSL routines:CONNECT_CR_SRVR_HELLO:tlsv1 alert</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14130.md")
</aside>
