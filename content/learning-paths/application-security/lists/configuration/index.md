---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/
  description: Configure rules with advanced settings.
  full_title: Configurations · Cloudflare Learning Paths
  head_html: <title>Configurations · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Configure rules with advanced settings."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/index.md"><meta property="og:title" content="Configurations · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure rules with advanced settings."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="WAF,DDoS Protection,SSL/TLS,DNS,Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/#page","headline":"Configurations \u00b7 Cloudflare Learning Paths","description":"Configure rules with advanced settings.","url":"https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/application-security/lists/configuration/
  schema: 1
---
<p>Both Custom and Managed Lists are located in the account settings. Refer to <a href="/learning-paths/application-security/lists/features/">Features by plan type</a> for more information on plan eligibility.</p>
<h2 id="custom-lists">Custom Lists</h2>
<p>Using a Custom List is an alternative to creating individual Firewall rules with long lists of IP addresses or other types of identifiers. They are easier to read and update, especially when they are used across many security rules. Lists are often used in conjunction with in-house or third party security feeds.</p>
<h2 id="managed-lists">Managed Lists</h2>
<p>The following lists are managed by the Cloudflare team and are regularly updated.</p>
<table>
<thead>
<tr>
<th>Display name</th>
<th>Name in expressions</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Open Proxies</td>
<td><code>cf.open_proxies</code></td>
<td>IP addresses of known open HTTP and SOCKS proxy endpoints, which are frequently used to launch attacks and hide attackers identity.</td>
</tr>
<tr>
<td>Cloudflare Anonymizers</td>
<td><code>cf.anonymizer</code></td>
<td>IP addresses of known anonymizers (Open SOCKS Proxies, VPNs, and TOR nodes).</td>
</tr>
<tr>
<td>Cloudflare VPNs</td>
<td><code>cf.vpn</code></td>
<td>IP addresses of known VPN servers.</td>
</tr>
<tr>
<td>Cloudflare Malware</td>
<td><code>cf.malware</code></td>
<td>IP addresses of known sources of malware.</td>
</tr>
<tr>
<td>Cloudflare Botnets, Command and Control Servers</td>
<td><code>cf.botnetcc</code></td>
<td>IP addresses of known botnet command-and-control servers.</td>
</tr>
</tbody>
</table>
<br />
<h2 id="creating-a-rule">Creating a rule</h2>
<p>Refer to <a href="/waf/tools/lists/use-in-expressions/">Use lists in expressions</a> to learn how to invoke a Managed List.</p>
