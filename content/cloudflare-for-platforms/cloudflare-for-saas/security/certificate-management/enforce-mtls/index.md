---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/
  description: Configure mTLS enforcement and minimum TLS version per custom hostname.
  full_title: TLS Settings — Cloudflare for SaaS · Cloudflare for Platforms docs
  head_html: <title>TLS Settings — Cloudflare for SaaS · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure mTLS enforcement and minimum TLS version per custom hostname."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/index.md"><meta property="og:title" content="TLS Settings — Cloudflare for SaaS · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure mTLS enforcement and minimum TLS version per custom hostname."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><meta name="pcx_tags" content="mTLS,TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/#page","headline":"TLS Settings \u2014 Cloudflare for SaaS \u00b7 Cloudflare for Platforms docs","description":"Configure mTLS enforcement and minimum TLS version per custom hostname.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS","TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/
  schema: 1
---
<p><a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">Mutual TLS (mTLS)</a> adds an extra layer of protection to application connections by validating certificates on the server and the client. When building a SaaS application, you may want to enforce mTLS to protect sensitive endpoints related to payment processing, database updates, and more.</p>
<p><a href="#minimum-tls-version">Minimum TLS Version</a> only allows HTTPS connections from visitors that support the selected TLS protocol version or newer. Cloudflare recommends TLS 1.2 to comply with the Payment Card Industry (PCI) Security Standards Council. As a SaaS provider, you can control the Minimum TLS version for your zone as a whole, as well as for individual custom hostnames.</p>
<p><a href="#cipher-suites">Cipher suites</a> are a combination of ciphers used to negotiate security settings during the <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">SSL/TLS handshake</a>. As a SaaS provider, you can specify configurations for cipher suites on your zone as a whole and cipher suites on individual custom hostnames via the API.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4135.md")
</aside>
<h2 id="enable-mtls">Enable mTLS</h2>
<p>Once you have <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">added a custom hostname</a>, you can enable mTLS by using Cloudflare Access. In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> and <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">add mTLS authentication</a> with a few clicks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4134.md")
</aside>
<h2 id="minimum-tls-version">Minimum TLS Version</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4133.md")
</aside>
<h3 id="scope">Scope</h3>
<p>Minimum TLS version exists both as a <a href="/ssl/edge-certificates/additional-options/minimum-tls/">zone-level setting</a> (on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page under <strong>Minimum TLS Version</strong>) and as a custom hostname setting. What this implies is:</p>
<ul>
<li>For custom hostnames created via API, it is possible not to explicitly define a value for <code>min_tls_version</code>. When that is the case, whatever value is defined as your zone's minimum TLS version will be applied. To confirm whether a given custom hostname has a specific minimum TLS version set, use the following API call.</li>
</ul>
<details class="nb-details"><summary>Check custom hostname TLS settings</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4136.md")
</div></details>
<ul>
<li>
<p>Whenever you make changes to a custom hostname via dashboard, the value that is set for Minimum TLS version will apply. If you have a scenario as explained in the bullet above, the dashboard change will override the zone-level configuration that was being applied.</p>
</li>
<li>
<p>For custom hostnames with wildcards enabled, the direct custom hostname you create (for example, <code>saas-customer.test</code>) will use the hostname-specific setting, while the others (<code>sub1.saas-customer.test</code>, <code>sub2.saas-customer.test</code>, etc) will default to the zone-level setting.</p>
</li>
</ul>
<h3 id="setup">Setup</h3>
<details class="nb-details"><summary>Minimum TLS version for your zone</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4137.md")
</div></details>
<details class="nb-details"><summary>Minimum TLS version for custom hostname</summary><div class="nb-details-body">
@input("content/.markup/bodies/4141.md")
</div></details>
<h2 id="cipher-suites">Cipher suites</h2>
<p>For security and regulatory reasons, you may want to only allow connections from certain cipher suites. Cloudflare provides recommended values and full cipher suite reference in our <a href="/ssl/edge-certificates/additional-options/cipher-suites/#resources">Cipher suites documentation</a>.</p>
<details class="nb-details"><summary>Restrict cipher suites for your zone</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4142.md")
</div></details>
<details class="nb-details"><summary>Restrict cipher suites for custom hostname</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4143.md")
</div></details>
<details class="nb-details"><summary>Restrict cipher suites for custom hostname with custom certificate</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4144.md")
</div></details>
<h2 id="alerts-for-mutual-tls-certificates">Alerts for mutual TLS certificates</h2>
<p>You can configure alerts to receive notifications before your mutual TLS certificates expire.</p>
<details><summary>Access mTLS Certificate Expiration Alert</summary><strong>Who is it for?</strong><p><a href="/cloudflare-one/access-controls/policies/">Access</a> customers that use client certificates for mutual TLS authentication. This notification will be sent 30 and 14 days before the expiration of the certificate.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Access</a> and/or <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/">Cloudflare for SaaS</a>.</p>
<strong>What should you do if you receive one?</strong><p>Upload a <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#add-mtls-authentication-to-your-access-configuration">renewed certificate</a>.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
