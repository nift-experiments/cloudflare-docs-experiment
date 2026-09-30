---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/
  description: Learn which methods you should use to validate Cloudflare for SaaS certificates.
  full_title: Validate certificates · Cloudflare for Platforms docs
  head_html: <title>Validate certificates · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn which methods you should use to validate Cloudflare for SaaS certificates."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/index.md"><meta property="og:title" content="Validate certificates · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn which methods you should use to validate Cloudflare for SaaS certificates."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/#page","headline":"Validate certificates \u00b7 Cloudflare for Platforms docs","description":"Learn which methods you should use to validate Cloudflare for SaaS certificates.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/
  schema: 1
---
<p>Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).
<br /></p>
<p>When you <a href="/api/resources/custom_hostnames/methods/create/">create a custom hostname</a>, choose one certificate validation method. The API accepts one <code>ssl.method</code> value: <code>http</code>, <code>txt</code>, or <code>email</code>.</p>
<h2 id="dcv-situations">DCV situations</h2>
<h3 id="non-wildcard-certificates">Non-wildcard certificates</h3>
<p>Specific (non-wildcard) custom hostnames can use <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/">HTTP based DCV</a> for certificate renewals, as long as:</p>
<ul>
<li>The hostname is pointing to the SaaS provider.</li>
<li>The hostname's traffic is proxying through the Cloudflare network.</li>
</ul>
<p>If your custom hostnames do not meet these requirements, use another validation method.</p>
<h3 id="wildcard-certificates">Wildcard certificates</h3>
<p>Wildcard custom hostnames require TXT-based validation. As the SaaS provider, you have two options for wildcard custom hostname certificate renewals:
<br /></p>
<ul>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">DCV Delegation</a> (auto-issuance)</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/">Manual</a></li>
</ul>
<h3 id="minimize-downtime">Minimize downtime</h3>
<p>If you want to minimize downtime, explore one of the following methods to issue and deploy the certificate before onboarding your customers:</p>
<ul>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/">Delegated DCV</a>: Place a one-time record at your authoritative DNS that allows Cloudflare to auto-renew all future certificate orders.</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/">TXT validation</a>: Have your customers add a <code>TXT</code> record to their authoritative DNS.</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-manual">Manual HTTP validation</a>: Add a <code>TXT</code> record at your origin.</li>
</ul>
<h3 id="minimize-customer-effort">Minimize customer effort</h3>
<p>If you value simplicity and your customers can handle a few minutes of downtime, you can rely on Cloudflare <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-automatic">automatic HTTP validation</a>.</p>
<p>Automatic HTTP validation requires the hostname to point to your SaaS target before the CA can fetch the validation token. During that period, the hostname may route to Cloudflare before the certificate reaches <code>ssl.status: active</code>.</p>
<h2 id="potential-issues">Potential issues</h2>
<p>To avoid or solve potential issues, refer to our <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/">troubleshooting guide</a>.</p>
