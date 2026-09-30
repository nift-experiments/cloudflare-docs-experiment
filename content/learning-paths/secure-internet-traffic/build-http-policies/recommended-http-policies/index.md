---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/
  description: Deploy recommended HTTP security policies.
  full_title: Recommended HTTP policies · Cloudflare Learning Paths
  head_html: <title>Recommended HTTP policies · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Deploy recommended HTTP security policies."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/index.md"><meta property="og:title" content="Recommended HTTP policies · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy recommended HTTP security policies."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/#page","headline":"Recommended HTTP policies \u00b7 Cloudflare Learning Paths","description":"Deploy recommended HTTP security policies.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/
  schema: 1
---
<p>We recommend you add the following HTTP policies to build an Internet and SaaS app security strategy for your organization.</p>
<p>For additional commonly used HTTP policy examples, refer to <a href="/cloudflare-one/traffic-policies/http-policies/common-policies/">Common HTTP policies</a>. For more information on building HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>
<h2 id="all-http-application-inspectbypass">All-HTTP-Application-InspectBypass</h2>
<p>Bypass HTTP inspection for applications that use embedded certificates. This will help avoid any certificate pinning errors that may arise from an initial rollout.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10150.md")
</div></div>
<h2 id="android-http-application-inspectionbypass">Android-HTTP-Application-InspectionBypass</h2>
<p>Bypass HTTPS inspection for Android applications (such as Google Drive) that use certificate pinning, which is incompatible with Gateway inspection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10154.md")
</div></div>
<h2 id="all-http-domain-inspection-bypass">All-HTTP-Domain-Inspection-Bypass</h2>
<p>Bypass HTTP inspection for a custom list of domains identified as incompatible with TLS inspection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10158.md")
</div></div>
<h2 id="all-http-securityrisks-blocklist">All-HTTP-SecurityRisks-Blocklist</h2>
<p>Block <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security categories</a>, such as <strong>Command and Control &amp; Botnet</strong> and <strong>Malware</strong>, based on Cloudflare's threat intelligence.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10162.md")
</div></div>
<h2 id="all-http-contentcategories-blocklist">All-HTTP-ContentCategories-Blocklist</h2>
<p>Entries in the <a href="/cloudflare-one/traffic-policies/domain-categories/#security-risk-subcategories">security risk content subcategory</a>, such as <strong>New Domains</strong>, do not always pose a security threat. We recommend you first create an Allow policy to track policy matching and identify any false positives. You can add false positives to your <strong>Trusted Domains</strong> list used in <strong>All-HTTP-Domain-Allowlist</strong>.</p>
<p>After your test is complete, we recommend you change the action to Block to minimize risk to your organization.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10166.md")
</div></div>
<h2 id="all-http-domainhost-blocklist">All-HTTP-DomainHost-Blocklist</h2>
<p>Block specific domains or hosts that are malicious or pose a threat to your organization. Like <strong>All-HTTP-ResolvedIP-Blocklist</strong>, this blocklist can be updated manually or via API automation.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10170.md")
</div></div>
<h2 id="all-http-application-blocklist">All-HTTP-Application-Blocklist</h2>
<p>Block unauthorized applications to limit your users' access to certain web-based tools and minimize the risk of <span class="nb-glossary-tooltip" title="shadow IT">shadow IT</span>. For example, the following policy blocks known AI tools:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10175.md")
</div></div>
<h2 id="privilegedusers-http-any-isolate">PrivilegedUsers-HTTP-Any-Isolate</h2>
<p>Isolate traffic for privileged users who regularly access critical systems or execute actions such as threat analysis and malware testing.</p>
<p>Security teams often need to perform threat analysis or malware testing that could trigger malware detection. Likewise, privileged users could be the target of attackers trying to gain access to critical systems.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10179.md")
</div></div>
<h2 id="quarantined-users-http-restricted-access">Quarantined-Users-HTTP-Restricted-Access</h2>
<p>Restrict access for users included in an <span class="nb-glossary-tooltip" title="identity provider">identity provider (IdP)</span> user group for risky users. This policy ensures your security team can restrict traffic for users of whom malicious or suspicious activity was detected.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10184.md")
</div></div>
<h2 id="all-http-domain-isolate">All-HTTP-Domain-Isolate</h2>
<p>Isolate high risk domains or create a custom list of known risky domains to avoid data exfiltration or malware infection. Ideally, your incident response teams can update the blocklist with an <a href="/security-center/intel-apis/">API automation</a> to provide real-time threat protection.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10188.md")
</div></div>
