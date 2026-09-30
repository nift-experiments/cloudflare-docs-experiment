---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/
  description: Set up User-side certificates for Zero Trust.
  full_title: User-side certificates · Cloudflare One docs
  head_html: <title>User-side certificates · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up User-side certificates for Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/index.md"><meta property="og:title" content="User-side certificates · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up User-side certificates for Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/#page","headline":"User-side certificates \u00b7 Cloudflare One docs","description":"Set up User-side certificates for Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/user-side-certificates/
  schema: 1
---
<p>Advanced security features such as <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">HTTPS traffic inspection</a>, <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a>, <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">anti-virus scanning</a>, <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a>, and <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> require users to install and trust a root certificate on their device. You can either install the certificate provided by Cloudflare (default option), or generate your own custom certificate and upload it to Cloudflare.</p>
<p>Zero Trust <a href="#generate-a-cloudflare-root-certificate">generates a unique root CA</a> for each account and deploys it across the Cloudflare global network. Alternatively, Enterprise users can upload and deploy their own <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">custom certificate</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="default-certificate-expired-on-2025-02-02">Default certificate expired on 2025-02-02</h3>
@markup("md", "content/.markup/bodies/6030.md")
</aside>
<h2 id="certificate-status">Certificate status</h2>
<p>Zero Trust will indicate if a certificate is ready for use in inspection based on its deployment status:</p>
<table>
<thead>
<tr>
<th>Deployment status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Inactive</td>
<td>The certificate has been generated by or uploaded to Cloudflare but is not deployed across the global network.</td>
</tr>
<tr>
<td>Pending</td>
<td>The certificate is being activated or deactivated for use.</td>
</tr>
<tr>
<td>Available</td>
<td>The certificate is deployed across the Cloudflare global network and ready to be turned on. The Cloudflare One Client will install the certificate on your users' devices.</td>
</tr>
<tr>
<td>Available and In-Use</td>
<td>The certificate is turned on. Gateway will use the certificate for inspection.</td>
</tr>
</tbody>
</table>
<h2 id="generate-a-cloudflare-root-certificate">Generate a Cloudflare root certificate</h2>
<p>To generate a new Cloudflare root certificate for your Zero Trust organization:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6033.md")
</div></div>
<p>The certificate will appear in your list of certificates as <strong>Inactive</strong>. To download a generated certificate, select it, then choose <strong>Download .pem</strong> and/or <strong>Download .crt</strong>. To deploy your certificate and turn it on for inspection, you need to <a href="#activate-a-root-certificate">activate the certificate</a>.</p>
<p>Each Zero Trust account can generate a new root certificate a maximum of three times per day.</p>
<h2 id="activate-a-root-certificate">Activate a root certificate</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6029.md")
</aside>
<p>Once a certificate is generated in or uploaded to Zero Trust, you need to activate it. Activating a certificate deploys it across the Cloudflare network and sets its status to <strong>Available</strong>. You can have up to 10 available certificates at once.</p>
<p>To activate your root certificate:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6036.md")
</div></div>
<p>The status of the certificate will change to <strong>Pending</strong> while it deploys. Once the status of your certificate is <strong>Available</strong>, you can install it on your user's devices either <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">with the Cloudflare One Client</a> or <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/">manually</a>.</p>
<p>Once you deploy and install your certificate, you can turn it on for use in inspection:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6039.md")
</div></div>
<p>You can set multiple certificates to <strong>Available</strong>, but you can only turn on one certificate for use in inspection at a time. Setting a certificate as <strong>In-Use</strong> will set any other in-use certificates as <strong>Available</strong> only and prevent them from being used for inspection until turned on again.</p>
