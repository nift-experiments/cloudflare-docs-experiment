---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/
  description: Deploy recommended network security policies.
  full_title: Recommended network policies · Cloudflare Learning Paths
  head_html: <title>Recommended network policies · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Deploy recommended network security policies."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/index.md"><meta property="og:title" content="Recommended network policies · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy recommended network security policies."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/#page","headline":"Recommended network policies \u00b7 Cloudflare Learning Paths","description":"Deploy recommended network security policies.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/
  schema: 1
---
<p>We recommend you add the following network policies to build an Internet and SaaS app security strategy for your organization.</p>
<p>For additional commonly used network policy examples, refer to <a href="/cloudflare-one/traffic-policies/network-policies/common-policies/">Common network policies</a>. For more information on building network policies, refer to <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>.</p>
<h2 id="quarantined-users-net-restricted-access">Quarantined-Users-NET-Restricted-Access</h2>
<p>Restrict access for users included in an <span class="nb-glossary-tooltip" title="identity provider">identity provider (IdP)</span> user group for risky users. This policy ensures your security team can restrict traffic for users of whom malicious or suspicious activity was detected.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10102.md")
</div></div>
<h2 id="posture-fail-net-restricted-access">Posture-Fail-NET-Restricted-Access</h2>
<p>Restrict access for devices where baseline posture checks have not passed. If posture checks are integrated with service providers such as Crowdstrike or Intune via the API, this policy dynamically blocks access for devices that do not meet predetermined security requirements.</p>
<p>Restrict access for users included in an <span class="nb-glossary-tooltip" title="identity provider">identity provider (IdP)</span> user group for risky users. This policy ensures your security team can restrict traffic for users of whom malicious or suspicious activity was detected.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10107.md")
</div></div>
<p>You can add a number of Cloudflare One Client device posture checks as needed, such as <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/disk-encryption/">Disk encryption</a> and <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/">Domain joined</a>. For more information on device posture checks, refer to <a href="/cloudflare-one/reusable-components/posture-checks/">Enforce device posture</a>.</p>
<h2 id="financeusers-net-https-financeservers-example">FinanceUsers-NET-HTTPS-FinanceServers (example)</h2>
<p>Allow HTTPS access for user groups. For example, the following policy gives finance users access to any known financial applications:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10111.md")
</div></div>
<h2 id="all-net-internet-blocklist">All-NET-Internet-Blocklist</h2>
<p>Block traffic to destination IPs, <span class="nb-glossary-tooltip" title="Server Name Indication (SNI)">SNIs</span>, and SNI domains that are malicious or pose a threat to your organization.</p>
<p>You can implement this policy by either creating custom blocklists or by using blocklists provided by threat intelligence partners or regional Computer Emergency and Response Teams (CERTs). Ideally, your CERTs can update the blocklist with an <a href="/security-center/intel-apis/">API automation</a> to provide real-time threat protection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10116.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10097.md")
</aside>
<h2 id="all-net-ssh-internet-allowlist">All-NET-SSH-Internet-Allowlist</h2>
<p>Allow SSH traffic to specific endpoints on the Internet for specific users. You can create a similar policy for other non-web endpoints that required access.</p>
<p>Optionally, you can include a selector to filter by source IP or IdP group.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10120.md")
</div></div>
<h2 id="all-net-no-http-https-internet-deny">All-NET-NO-HTTP-HTTPS-Internet-Deny</h2>
<p>Block all non-web traffic towards the Internet. By using the <strong>Detected Protocol</strong> selector, you will ensure alternative ports for HTTP and HTTPS are allowed.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10124.md")
</div></div>
<h2 id="all-net-internalnetwork-implicitdeny">All-NET-InternalNetwork-ImplicitDeny</h2>
<p>Implicitly deny all of your internal IP ranges included in a list. We recommend you place this policy at the <a href="/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#order-of-precedence">bottom of your policy list</a> to ensure you explicitly approve traffic defined in the above policies.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10128.md")
</div></div>
<h2 id="all-net-applicationaccess-allow">All-NET-ApplicationAccess-Allow</h2>
<p>Only allow network traffic from known and approved devices.</p>
<p>In the following example, you can use a list of <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/">device serial numbers</a> to ensure users can only access an application if they connect with the Cloudflare One Client from a company device:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10132.md")
</div></div>
