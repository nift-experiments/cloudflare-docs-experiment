---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/
  description: Inspect encrypted traffic with TLS decryption.
  full_title: Enable TLS decryption (optional) · Cloudflare Learning Paths
  head_html: <title>Enable TLS decryption (optional) · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Inspect encrypted traffic with TLS decryption."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/index.md"><meta property="og:title" content="Enable TLS decryption (optional) · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Inspect encrypted traffic with TLS decryption."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/#page","headline":"Enable TLS decryption (optional) \u00b7 Cloudflare Learning Paths","description":"Inspect encrypted traffic with TLS decryption.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/
  schema: 1
---
<p><a href="https://www.cloudflare.com/learning/security/what-is-https-inspection/">TLS decryption</a> allows Cloudflare Gateway to inspect HTTPS requests to your private network applications.</p>
<h2 id="should-i-enable-tls-decryption">Should I enable TLS decryption?</h2>
<p>With TLS decryption turned on, you can apply advanced Gateway policies, such as:</p>
<ul>
<li>Filtering based on the complete URL and path of requests</li>
<li>Scanning for sensitive data with <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a></li>
<li>Starting a remote browser isolation session with <a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a></li>
</ul>
<p>These features can increase the security posture of sensitive systems, but TLS decryption can also break your users' access to certain resources. For instance, if your internal applications use self-signed certificates, you will need to either configure a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policy or an <a href="/cloudflare-one/traffic-policies/http-policies/#untrusted-certificates">Untrusted certificate <em>Pass through</em></a> policy to allow users to connect. To learn more, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#inspection-limitations">TLS decryption limitations</a>.</p>
<p>With TLS decryption turned off, Gateway can only inspect and apply HTTP policies to unencrypted HTTP requests. However, you can still apply network policies to HTTPS traffic based on user identity, device posture, IP, resolved domain, SNI, and other attributes that support a Zero Trust security implementation. For more information, refer to <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>.</p>
<h2 id="enable-tls-decryption">Enable TLS decryption</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9943.md")
</div></div>
<p>Next, choose a <a href="#configure-user-side-certificates">user-side certificate</a> to use for inspection.</p>
<h2 id="configure-user-side-certificates">Configure user-side certificates</h2>
<p>When you enable TLS decryption, Gateway will decrypt all traffic sent over HTTPS, apply your HTTP policies, and then re-encrypt the request with a certificate on the user device. You can either <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">install the certificate provided by Cloudflare</a> (default option) or <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">upload a custom root certificate</a> to Cloudflare (Enterprise-only option).</p>
<h3 id="best-practices">Best practices</h3>
<p>Deploying the Cloudflare root certificate is the simplest way to get started with TLS decryption and is usually appropriate for testing or proof of concept conditions.</p>
<p>If you already have a certificate that you use for other inspection or trust purposes, we recommend uploading your own root certificate for the following reasons:</p>
<ul>
<li>Using a single certificate streamlines IT management.</li>
<li>If other services (such as <code>git</code> workflows, other CLI tools, or thick client applications) rely on an existing certificate store, presenting the same certificate in inspection is far less likely to interrupt their traffic flow.</li>
<li>If you are using Cloudflare Mesh to connect devices to Cloudflare, those devices will not be able to leverage HTTP policies that require decrypting TLS unless they have a certificate that matches either your uploaded certificate or the Cloudflare root certificate. It is more likely that your network infrastructure already has your own device certificates deployed, so using the existing PKI infrastructure for inspection will reduce the number of steps needed to deploy Zero Trust.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="mdm-deployments">MDM deployments</h3>
@markup("md", "content/.markup/bodies/9940.md")
</aside>
