---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/
  description: Control which devices can enroll.
  full_title: Define device enrollment permissions · Cloudflare Learning Paths
  head_html: <title>Define device enrollment permissions · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Control which devices can enroll."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/index.md"><meta property="og:title" content="Define device enrollment permissions · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control which devices can enroll."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/#page","headline":"Define device enrollment permissions \u00b7 Cloudflare Learning Paths","description":"Control which devices can enroll.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/
  schema: 1
---
<p>Device enrollment permissions determine which users can connect new devices to your organization's Cloudflare Zero Trust instance. Once the user registers their device, the Cloudflare One Client will store their identity token and use it to authenticate to services in your private network.</p>
<h2 id="set-device-enrollment-permissions">Set device enrollment permissions</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10090.md")
</div></div>
<h2 id="only-allow-corporate-devices">Only allow corporate devices</h2>
<p>Device posture evaluation happens after a device has already enrolled in your Zero Trust organization. If you want only specific devices to be able to enroll, we recommend adding a <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">mutual TLS authentication</a> rule to your device enrollment policy. This rule will check for the presence of a specific client certificate on the enrolling devices.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10086.md")
</aside>
<details class="nb-details"><summary>Certificate requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10092.md")
</div></details>
<p>To check for an mTLS certificate:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10096.md")
</div></div>
<h2 id="best-practices">Best practices</h2>
<p>Most businesses use a single identity provider as the source of truth for their user directory. You should use this source of truth to onboard your corporate users to Zero Trust, for example by requiring company email addresses to login with your primary identity provider. Later on, you can add other login methods or identity providers as necessary for any contractors, vendors, or acquired corporations who may need access to your network.</p>
