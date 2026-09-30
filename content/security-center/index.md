---
cp9:
  canonical: https://developers.cloudflare.com/security-center/
  description: Review security insights, investigate threats, and protect your brand from impersonation.
  full_title: Overview · Cloudflare Security Center docs
  head_html: <title>Overview · Cloudflare Security Center docs</title><meta name="generator" content="Nift"><meta name="description" content="Review security insights, investigate threats, and protect your brand from impersonation."><link rel="canonical" href="https://developers.cloudflare.com/security-center/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security-center/index.md"><meta property="og:title" content="Overview · Cloudflare Security Center docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review security insights, investigate threats, and protect your brand from impersonation."><meta property="og:url" content="https://developers.cloudflare.com/security-center/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security Center"><meta name="algolia_product_filter" content="Security Center"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/security-center/#page","headline":"Overview \u00b7 Cloudflare Security Center docs","description":"Review security insights, investigate threats, and protect your brand from impersonation.","url":"https://developers.cloudflare.com/security-center/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security-center/
  schema: 1
---
<p>Cloudflare Security Center brings together your Cloudflare security products, threat intelligence from Cloudflare's global network, and configuration analysis into a unified security intelligence solution. Security Center enables you to strengthen your security posture by:</p>
<ul>
<li><strong>Mapping your attack surface</strong> — identifying the Internet-facing assets (domains, DNS records, and IP addresses) associated with your Cloudflare account</li>
<li><strong>Providing asset inventory and discovery</strong> — listing the infrastructure Cloudflare detects across your account so you can review what is exposed</li>
<li><strong>Identifying potential security risks, misconfigurations, and vulnerabilities</strong> — running automated scans that compare your current Cloudflare configuration against ideal settings</li>
<li><strong>Helping you mitigate these risks</strong> — connecting each finding to the relevant Cloudflare product setting so you can resolve issues from the dashboard</li>
</ul>
<h2 id="main-features">Main features</h2>
<ul>
<li><strong><a href="/security/security-insights/">Security Insights</a></strong>: Review and manage potential security risks and vulnerabilities associated with your IT infrastructure. Security Insights scans your Cloudflare account settings — including DNS records, SSL/TLS certificates, WAF configurations, and Access configurations — and reports findings with severity levels.</li>
<li><strong><a href="/security-center/infrastructure/">Infrastructure</a></strong>: Review and manage your IT infrastructure. The Infrastructure tab displays the domains, IP addresses, and other assets associated with your Cloudflare account.</li>
<li><strong><a href="/security-center/investigate/">Investigate</a></strong>: Investigate threats using data from Cloudflare's global network. Look up any IP address, domain, or hostname to view its category, country of origin, and passive DNS records.</li>
<li><strong><a href="/analytics/account-and-zone-analytics/app-security-reports/">Security Reports</a></strong> (beta): Gain visibility into requests blocked or challenged by Cloudflare application security products, including <a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Protection</a>, <a href="/waf/">WAF</a>, and <a href="/bots/">Bot Management</a>.</li>
<li><strong><a href="/security-center/brand-protection/">Brand Protection</a></strong> (beta): Search for newly registered domains that may be attempting to impersonate your brand. Brand Protection monitors for typosquatting, homoglyph attacks, and service concatenation.</li>
</ul>
<p><a class="nb-link-button" href="/security-center/get-started/">Get started</a></p>
<hr />
<h2 id="availability">Availability</h2>
<p>Cloudflare Security Center is available to customers on all plans.</p>
<p>The frequency of automatic security scans depends on your Cloudflare plan, ranging from every 7 days on Free, Pro, and Business plans to every 3 days on Enterprise plans. Refer to <a href="/security/security-insights/how-it-works/#scan-frequency">Scan frequency</a> for more information.</p>
<p>If you have any comments, questions, or bugs to report, create a post in the <a href="https://community.cloudflare.com/c/security/security-center/65">Cloudflare Community forum</a>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Users with an <a href="/fundamentals/manage-members/roles/#account-scoped-roles">Administrator Read Only</a> role cannot access the Cloudflare Security Center.</li>
<li>Only Cloudflare accounts with at least one Business or Enterprise zone (domain on your account), or accounts on the Teams Standard or Teams Enterprise plans, can manually start a new scan.</li>
</ul>
