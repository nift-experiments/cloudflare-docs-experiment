---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/
  description: Set up global Authenticated Origin Pulls for all hostnames.
  full_title: Global authenticated origin pulls · Cloudflare SSL/TLS docs
  head_html: <title>Global authenticated origin pulls · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up global Authenticated Origin Pulls for all hostnames."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/index.md"><meta property="og:title" content="Global authenticated origin pulls · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up global Authenticated Origin Pulls for all hostnames."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/#page","headline":"Global authenticated origin pulls \u00b7 Cloudflare SSL/TLS docs","description":"Set up global Authenticated Origin Pulls for all hostnames.","url":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/authenticated-origin-pull/set-up/global/
  schema: 1
---
<p>When you enable global Authenticated Origin Pulls (AOP), Cloudflare uses a Cloudflare-provided client certificate for all proxied traffic to your zone. This certificate is shared across all Cloudflare accounts and guarantees that the request is coming from the Cloudflare network.</p>
<p>Global, <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a>, and <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> AOP are independent configurations. Enabling or disabling one does not affect the others.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>
<p>Make sure your zone is using an <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption mode</a> of <strong>Full</strong> or higher.</p>
</li>
<li>
<p>Consider your security and certificate needs:</p>
<ul>
<li>
<p>The Cloudflare-provided certificate is not exclusive to your account. It only guarantees that a request is coming from the Cloudflare network. If you need stricter security, set up <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a> or <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> AOP with your own certificate instead.</p>
</li>
<li>
<p>Global AOP is applied to all proxied hostnames on your zone, including <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a> configured on a Cloudflare for SaaS zone. If you need a different AOP certificate for different custom hostnames, use <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname AOP</a>.</p>
</li>
</ul>
</li>
</ul>
<h2 id="1-download-the-cloudflare-certificate"><ol>
<li>Download the Cloudflare certificate</li>
</ol></h2>
<p><a href="/ssl/static/authenticated_origin_pull_ca.pem">Download the Cloudflare authenticated origin pull certificate (.PEM)</a> and upload it to your origin server. This certificate is <strong>not</strong> the same as the <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificate</a>.</p>
<h2 id="2-configure-origin-to-accept-client-certificates"><ol start="2">
<li>Configure origin to accept client certificates</li>
</ol></h2>
<p>With the certificate installed, set up your origin web server to accept client certificates.</p>
<p>Check the examples below for Apache and NGINX or refer to your origin web server documentation - for example, <a href="https://www.haproxy.com/documentation/hapee/latest/security/authentication/client-certificate-authentication/">HAProxy</a>, <a href="https://doc.traefik.io/traefik/https/tls/#client-authentication-mtls">Traefik</a>, <a href="https://caddyserver.com/docs/json/apps/http/servers/tls_connection_policies/client_authentication/mode/">Caddy</a>.</p>
<details class="nb-details"><summary>Apache example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14320.md")
</div></details>
<details class="nb-details"><summary>NGINX example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14321.md")
</div></details>
<p>At this point, you may also want to enable logging on your origin so that you can verify the configuration is working.</p>
<h2 id="3-enable-global-authenticated-origin-pulls"><ol start="3">
<li>Enable global Authenticated Origin Pulls</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14324.md")
</div></div>
<h2 id="4-enforce-validation-check-on-your-origin"><ol start="4">
<li>Enforce validation check on your origin</li>
</ol></h2>
<p>Once you can confirm everything is working as expected for your specific origin setup, configure your origin to enforce the authentication.</p>
<details class="nb-details"><summary>Apache example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14325.md")
</div></details>
<details class="nb-details"><summary>NGINX example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14326.md")
</div></details>
<p>After completing the process, you can use <code>curl</code> to send requests directly to your origin IPs, verifying that the requests fail due to certificate validation being enforced.</p>
