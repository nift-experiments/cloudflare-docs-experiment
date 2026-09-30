---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/
  description: Set up per-hostname Authenticated Origin Pulls with custom certificates.
  full_title: Per-hostname authenticated origin pulls · Cloudflare SSL/TLS docs
  head_html: <title>Per-hostname authenticated origin pulls · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up per-hostname Authenticated Origin Pulls with custom certificates."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/index.md"><meta property="og:title" content="Per-hostname authenticated origin pulls · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up per-hostname Authenticated Origin Pulls with custom certificates."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/#page","headline":"Per-hostname authenticated origin pulls \u00b7 Cloudflare SSL/TLS docs","description":"Set up per-hostname Authenticated Origin Pulls with custom certificates.","url":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/
  schema: 1
---
<p>When you enable per-hostname Authenticated Origin Pulls (AOP), all proxied traffic to the specified hostname is authenticated at the origin web server using a certificate that you upload. You can use client certificates from your Private PKI to authenticate connections from Cloudflare.</p>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/global/">Global</a>, <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a>, and per-hostname AOP are independent configurations. Enabling or disabling one does not affect the others. Per-hostname certificates take precedence over zone-level and global certificates for the specified hostname.</p>
<h2 id="before-you-begin">Before you begin</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/14305.md")
</aside>
<p>Refer to the steps below for an example of how to generate a custom certificate using OpenSSL. The CA root certificate that you use to issue the custom certificate should be the same CA that you will <a href="#2-configure-origin-to-accept-client-certificates">upload to your origin</a>.</p>
<details class="nb-details"><summary>OpenSSL example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14306.md")
</div></details>
<h2 id="1-upload-custom-certificate"><ol>
<li>Upload custom certificate</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14309.md")
</div></div>
<h2 id="2-configure-origin-to-accept-client-certificates"><ol start="2">
<li>Configure origin to accept client certificates</li>
</ol></h2>
<p>With the certificate installed, set up your origin web server to accept client certificates.</p>
<p>Check the examples below for Apache and NGINX or refer to your origin web server documentation - for example, <a href="https://www.haproxy.com/documentation/hapee/latest/security/authentication/client-certificate-authentication/">HAProxy</a>, <a href="https://doc.traefik.io/traefik/https/tls/#client-authentication-mtls">Traefik</a>, <a href="https://caddyserver.com/docs/json/apps/http/servers/tls_connection_policies/client_authentication/mode/">Caddy</a>.</p>
<details class="nb-details"><summary>Apache example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14310.md")
</div></details>
<details class="nb-details"><summary>NGINX example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14311.md")
</div></details>
<p>At this point, you may also want to enable logging on your origin so that you can verify the configuration is working.</p>
<h2 id="3-enable-authenticated-origin-pulls-for-the-hostname"><ol start="3">
<li>Enable Authenticated Origin Pulls for the hostname</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14314.md")
</div></div>
<h2 id="4-enforce-validation-check-on-your-origin"><ol start="4">
<li>Enforce validation check on your origin</li>
</ol></h2>
<p>Once you can confirm everything is working as expected for your specific origin setup, configure your origin to enforce the authentication.</p>
<details class="nb-details"><summary>Apache example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14315.md")
</div></details>
<details class="nb-details"><summary>NGINX example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14316.md")
</div></details>
<p>After completing the process, you can use <code>curl</code> to send requests directly to your origin IPs, verifying that the requests fail due to certificate validation being enforced.</p>
<h2 id="5-optional-set-up-expiration-alerts"><ol start="5">
<li>(Optional) Set up expiration alerts</li>
</ol></h2>
<p>You can configure alerts to receive notifications before your AOP certificates expire.</p>
<details><summary>Hostname-level Authenticated Origin Pulls Certificate Expiration Alert</summary><strong>Who is it for?</strong><p>Customers that upload their own certificate to use with hostname-level Authenticated Origin Pull (AOP) to secure connections from Cloudflare to their origin server.
AOP certificate expiration notifications are sent 30 days and 14 days before the certificate expiry.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Authenticated Origin Pull.</p>
<strong>What should you do if you receive one?</strong><p>Upload a renewed certificate to use for <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">hostname-level AOP</a>.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
<h2 id="further-options">Further options</h2>
<p>Refer to <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/manage-certificates/">Manage certificates</a> for further options.</p>
<p>To learn how to remove the configuration, refer to <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/">Rollback</a>.</p>
