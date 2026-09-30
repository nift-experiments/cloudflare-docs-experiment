---
cp9:
  canonical: https://developers.cloudflare.com/security-center/intel-apis/
  description: Query Cloudflare threat intelligence data for IPs, domains, ASNs, and more.
  full_title: Threat Intelligence APIs · Cloudflare Security Center docs
  head_html: <title>Threat Intelligence APIs · Cloudflare Security Center docs</title><meta name="generator" content="Nift"><meta name="description" content="Query Cloudflare threat intelligence data for IPs, domains, ASNs, and more."><link rel="canonical" href="https://developers.cloudflare.com/security-center/intel-apis/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security-center/intel-apis/index.md"><meta property="og:title" content="Threat Intelligence APIs · Cloudflare Security Center docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query Cloudflare threat intelligence data for IPs, domains, ASNs, and more."><meta property="og:url" content="https://developers.cloudflare.com/security-center/intel-apis/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security Center"><meta name="algolia_product_filter" content="Security Center"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Security Center"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/security-center/intel-apis/#page","headline":"Threat Intelligence APIs \u00b7 Cloudflare Security Center docs","description":"Query Cloudflare threat intelligence data for IPs, domains, ASNs, and more.","url":"https://developers.cloudflare.com/security-center/intel-apis/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /security-center/intel-apis/
  schema: 1
---
<p>Cloudflare provides a series of endpoints covering various areas of internet security and insights. Based on your Cloudflare plan type, the <a href="/security-center/intel-apis/limits/">limit</a> of API calls will vary per month.</p>
<table>
<thead>
<tr>
<th>Intelligence Endpoint</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/intel/subresources/asn/methods/get/">ASN Intelligence</a></td>
<td>Provides an overview of the Autonomous System Number (ASN) and a list of subnets for it.</td>
</tr>
<tr>
<td><a href="/api/resources/intel/subresources/indicator_feeds/subresources/downloads/">Custom Indicator Feed Download</a></td>
<td>Provides the ability to download any custom indicator feeds that users create.</td>
</tr>
<tr>
<td><a href="/api/resources/intel/subresources/domains/methods/get/">Domain Intelligence</a></td>
<td>Provides security details and statistics about a domain.</td>
</tr>
<tr>
<td><a href="/api/resources/intel/subresources/domain_history/methods/get/">Domain History</a></td>
<td>Provides historical security threat and content categories that are currently and previously assigned to a domain.</td>
</tr>
<tr>
<td><a href="/api/resources/intel/subresources/ips/methods/get/">IP Intelligence</a></td>
<td>Provides the geolocation, ASN, infrastructure type of the ASN, and any security threat categories of an IP address.</td>
</tr>
<tr>
<td><a href="/api/resources/intel/subresources/dns/methods/list/">Passive DNS by IP</a></td>
<td>Provides a list of all the domains, including first seen and last seen dates, that have resolved to a specific IP address.</td>
</tr>
<tr>
<td><a href="/api/resources/brand_protection/methods/url_info/">Phishing Intelligence</a></td>
<td>Provides phishing details about a URL.</td>
</tr>
<tr>
<td><a href="/api/resources/intel/subresources/miscategorizations/methods/create/">Miscategorization Intelligence</a></td>
<td>Enables users to submit requests for modifying a domain's category, subsequently undergoing review by the Cloudflare Intelligence team.</td>
</tr>
<tr>
<td><a href="/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/create/">Priority Intelligence Requirements</a></td>
<td>Provides a structured approach to identifying intelligence gaps, formulating precise requirements, and organizing them into categories.</td>
</tr>
<tr>
<td><a href="/api/resources/cloudforce_one/subresources/requests/methods/create/">Request for Information</a></td>
<td>Creates a targeted inquiry for specific intelligence insights to help organizations understand and respond to imminent security threats and vulnerabilities.</td>
</tr>
<tr>
<td><a href="/api/resources/cloudforce_one/subresources/threat_events">Threat Events</a></td>
<td>Allows customers to look into the Cloudflare telemetry and threat actor activity on the Cloudflare network.</td>
</tr>
<tr>
<td><a href="/api/resources/intel/subresources/whois/methods/get/">WHOIS</a></td>
<td>Provides the WHOIS registration information for a specific domain.</td>
</tr>
<tr>
<td><a href="/ddos-protection/botnet-threat-feed/">DDoS Botnet Threat Feed</a><br/>(early access)</td>
<td>Provides information to service providers about their own IP addresses that have participated in HTTP DDoS attacks as observed from Cloudflare's global network.</td>
</tr>
<tr>
<td><a href="/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/create/">Cloudforce One</a></td>
<td>Enable users to list, delete, get, or update a request asset.</td>
</tr>
<tr>
<td><a href="/api/resources/brand_protection/">Brand Protection API</a></td>
<td>Provides the ability to create and delete queries, download matches for logo and string queries, read matches for logo and string queries.</td>
</tr>
</tbody>
</table>
<h2 id="api-examples">API Examples</h2>
<p>Below you can find examples of Threat Intelligence API calls. Make sure you are using an <a href="/fundamentals/api/get-started/create-token/">API Token</a> with the appropriate edit permissions. For comprehensive details, navigate to the respective API documentation using the links above.</p>
<h3 id="asn-intelligence">ASN Intelligence</h3>
<details class="nb-details" open><summary>Get ASN Overview</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13812.md")
</div></details>
<h3 id="custom-indicator-feed-download">Custom Indicator Feed Download</h3>
<details class="nb-details" open><summary>Download Custom Indicator Feed</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13813.md")
</div></details>
<h3 id="domain-intelligence">Domain Intelligence</h3>
<details class="nb-details"><summary>Get Domain Details</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13814.md")
</div></details>
<h3 id="domain-history">Domain History</h3>
<details class="nb-details"><summary>Get Domain History</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13815.md")
</div></details>
<h3 id="ip-intelligence">IP Intelligence</h3>
<details class="nb-details"><summary>Get IP Overview</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13816.md")
</div></details>
<h3 id="passive-dns-by-ip">Passive DNS by IP</h3>
<details class="nb-details"><summary>Get Passive DNS by IP</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13817.md")
</div></details>
<h3 id="phishing-intelligence">Phishing Intelligence</h3>
<details class="nb-details"><summary>Get results for a URL scan</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13818.md")
</div></details>
<h3 id="miscategorization-intelligence">Miscategorization Intelligence</h3>
<details class="nb-details"><summary>Create Miscategorization</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13819.md")
</div></details>
<h3 id="whois">WHOIS</h3>
<details class="nb-details"><summary>Get WHOIS Record</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13820.md")
</div></details>
