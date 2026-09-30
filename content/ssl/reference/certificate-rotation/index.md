---
cp9:
  canonical: https://developers.cloudflare.com/ssl/reference/certificate-rotation/
  description: Replace an Advanced Certificate Manager certificate pack with zero downtime by creating the new pack, waiting for it to go Active, then deleting the old one.
  full_title: Rotate ACM certificate packs · Cloudflare SSL/TLS docs
  head_html: <title>Rotate ACM certificate packs · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Replace an Advanced Certificate Manager certificate pack with zero downtime by creating the new pack, waiting for it to go Active, then deleting the old one."><link rel="canonical" href="https://developers.cloudflare.com/ssl/reference/certificate-rotation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/reference/certificate-rotation/index.md"><meta property="og:title" content="Rotate ACM certificate packs · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Replace an Advanced Certificate Manager certificate pack with zero downtime by creating the new pack, waiting for it to go Active, then deleting the old one."><meta property="og:url" content="https://developers.cloudflare.com/ssl/reference/certificate-rotation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/reference/certificate-rotation/#page","headline":"Rotate ACM certificate packs \u00b7 Cloudflare SSL/TLS docs","description":"Replace an Advanced Certificate Manager certificate pack with zero downtime by creating the new pack, waiting for it to go Active, then deleting the old one.","url":"https://developers.cloudflare.com/ssl/reference/certificate-rotation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/reference/certificate-rotation/
  schema: 1
---
<p>Advanced Certificate Manager (ACM) certificate packs cannot be updated in place. To replace an existing pack - for example, to change the certificate authority, add hostnames, or change validation method - you create a new pack, wait for it to reach <strong>Active</strong> status, and then delete the old one.</p>
<p>The key principle is to ensure the new certificate pack reaches <strong>Active</strong> before removing the old one. This avoids any gap in coverage and means there is no downtime for your users.</p>
<hr />
<h2 id="recommended-rotation-process">Recommended rotation process</h2>
<h3 id="1-create-the-new-certificate-pack"><ol>
<li>Create the new certificate pack</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13974.md")
</div></div>
<h3 id="2-wait-for-active-status"><ol start="2">
<li>Wait for Active status</li>
</ol></h3>
<p>After ordering, the new certificate pack moves through several intermediate states before it is ready to serve traffic:</p>
<ol>
<li><strong>Initializing</strong></li>
<li><strong>Pending Validation</strong></li>
<li><strong>Pending Issuance</strong></li>
<li><strong>Pending Deployment</strong></li>
<li><strong>Active</strong></li>
</ol>
<p>Do not delete the old certificate pack until the new one reaches <strong>Active</strong>. Refer to <a href="/ssl/reference/certificate-statuses/">Certificate statuses</a> for a description of each stage.</p>
<p>Monitor progress on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page in the dashboard, or poll the <a href="/api/resources/ssl/subresources/certificate_packs/methods/get/">Get Certificate Pack</a> API endpoint.</p>
<p>For zones using Cloudflare as authoritative DNS (full setup), most validations complete within minutes. For <a href="/dns/zone-setups/partial-setup/">partial (CNAME) setups</a>, you will need to place DCV tokens manually - refer to <a href="/ssl/edge-certificates/changing-dcv-method/">DCV methods</a> for details. DCV tokens expire if not satisfied within their validity window (7 days for Let's Encrypt, 14 days for Google Trust Services and SSL.com).</p>
<h3 id="3-delete-the-old-certificate-pack"><ol start="3">
<li>Delete the old certificate pack</li>
</ol></h3>
<p>Once the new pack is <strong>Active</strong>, it is safe to delete the old one.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13978.md")
</div></div>
<h3 id="4-expect-a-brief-pending-deployment-state"><ol start="4">
<li>Expect a brief Pending Deployment state</li>
</ol></h3>
<p>After the old pack is deleted, the remaining certificate may briefly show <strong>Pending Deployment</strong> before returning to <strong>Active</strong>. This reflects a normal edge re-evaluation cycle as the global network reconciles the change, and typically resolves within a few minutes with no traffic impact.</p>
<p>If the certificate remains in <strong>Pending Deployment</strong> for longer than expected, refer to <a href="/ssl/reference/certificate-statuses/">Certificate statuses</a> and contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<hr />
<h2 id="terraform">Terraform</h2>
<p>Certificate packs cannot be updated in place - every attribute of the <code>cloudflare_certificate_pack</code> resource forces a new resource on change. Plan your rotation around this constraint.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13970.md")
</aside>
<h3 id="wait-for-active-automatically">Wait for Active automatically</h3>
<p>Set <code>wait_for_active_status = true</code> on the new resource to have Terraform block the apply until the certificate pack reaches <strong>Active</strong>. This removes the need to manually poll the dashboard or API between steps 1 and 3.</p>
<h3 id="recommended-pattern">Recommended pattern</h3>
<ol>
<li>Add the new <code>cloudflare_certificate_pack</code> resource with <code>wait_for_active_status = true</code> and run <code>terraform apply</code>. The apply will not complete until the pack is Active.</li>
<li>Remove the old resource from your configuration and run <code>terraform apply</code> to delete it.</li>
</ol>
<p>For zero-downtime rotation of a single resource (where you cannot have both old and new in state simultaneously), use Terraform's <a href="https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#create_before_destroy"><code>create_before_destroy</code></a> lifecycle meta-argument.</p>
<p>Refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/certificate_pack"><code>cloudflare_certificate_pack</code> provider documentation</a> for the full resource schema.</p>
<hr />
<h2 id="common-rotation-issues">Common rotation issues</h2>
<h3 id="let-s-encrypt-rate-limit">Let's Encrypt rate limit</h3>
<p>Let's Encrypt limits new certificates to five per seven-day window for the same exact set of hostnames. Repeated rotations (for example, during testing or automation loops) can exhaust this limit and block further issuance for up to a week.</p>
<p>If you hit this limit, switch the certificate authority to <a href="/ssl/reference/certificate-authorities/">Google Trust Services or SSL.com</a> or wait for the rate limit window to expire. Refer to <a href="https://letsencrypt.org/docs/rate-limits/">Let's Encrypt rate limits</a> for details.</p>
<h3 id="pack-stuck-in-pending-validation">Pack stuck in Pending Validation</h3>
<p>If a new pack remains in <strong>Pending Validation</strong> for more than 15 minutes, check that your DCV method is set up correctly. Refer to <a href="/ssl/edge-certificates/changing-dcv-method/">Domain Control Validation</a> and <a href="/ssl/edge-certificates/changing-dcv-method/troubleshooting/">Troubleshoot domain control validation</a>.</p>
<hr />
<h2 id="distinction-from-custom-certificate-replacement">Distinction from custom certificate replacement</h2>
<p>This page covers <strong>ACM certificate packs</strong> (Cloudflare-managed Domain Validated certificates ordered via Advanced Certificate Manager).</p>
<p>If you are using a <strong>custom certificate</strong> (a certificate you supplied), Cloudflare provides an in-place <strong>Replace SSL certificate and key</strong> flow that handles the rotation without requiring you to manage two packs. Refer to <a href="/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate">Manage custom certificates</a>.</p>
