---
cp9:
  canonical: https://developers.cloudflare.com/security-center/investigate/investigate-threats/
  description: Search for IP, domain, URL, or ASN intelligence in Security Center or Radar.
  full_title: Investigate threats · Cloudflare Security Center docs
  head_html: <title>Investigate threats · Cloudflare Security Center docs</title><meta name="generator" content="Nift"><meta name="description" content="Search for IP, domain, URL, or ASN intelligence in Security Center or Radar."><link rel="canonical" href="https://developers.cloudflare.com/security-center/investigate/investigate-threats/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security-center/investigate/investigate-threats/index.md"><meta property="og:title" content="Investigate threats · Cloudflare Security Center docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Search for IP, domain, URL, or ASN intelligence in Security Center or Radar."><meta property="og:url" content="https://developers.cloudflare.com/security-center/investigate/investigate-threats/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security Center"><meta name="algolia_product_filter" content="Security Center"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security-center/investigate/investigate-threats/#page","headline":"Investigate threats \u00b7 Cloudflare Security Center docs","description":"Search for IP, domain, URL, or ASN intelligence in Security Center or Radar.","url":"https://developers.cloudflare.com/security-center/investigate/investigate-threats/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security-center/investigate/investigate-threats/
  schema: 1
---
<p>Users can investigate the details of an IP address, domain name, URL, or Autonomous System Number (ASN). You can find the Investigate feature in your Cloudflare account's Security Center and in <a href="https://radar.cloudflare.com/scan">Cloudflare Radar</a>.</p>
<p>You can search with Investigate by <a href="/security-center/investigate/investigate-threats/#ip-address">IP address</a>, <a href="/security-center/investigate/investigate-threats/#domain">domain</a>, <a href="/security-center/investigate/investigate-threats/#url">URL</a> and <a href="/security-center/investigate/investigate-threats/#as-number">AS number</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13808.md")
</aside>
<h2 id="ip-address">IP Address</h2>
<p>An <a href="https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/">IP address</a> is a unique address that identifies a server. It stands for <a href="https://www.cloudflare.com/learning/network-layer/internet-protocol/">Internet Protocol</a>, which is the set of rules that allows servers to communicate with each other.</p>
<p>IP address search allows you to search both <a href="https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/">IPv4 and IPv6</a> addresses and retrieve relevant information such as their pointer records, AS numbers and passive DNS records.</p>
<h2 id="domain">Domain</h2>
<p>A <a href="https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/">domain name</a> is a string of text that maps to an IP address. Domain names are used to help people remember where websites are hosted. Domain names are purchased through <a href="/registrar/">registrars</a> and can be acquired easily by anyone.</p>
<p>When you search for a domain name, Cloudflare will provide an overview of the domain's <a href="#domain-categories">category</a> and IP addresses it currently resolves to.</p>
<h3 id="domain-categories">Domain categories</h3>
<p>For a detailed list of categories, refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Domain categories</a>.</p>
<p>A domain can have multiple categories. Cloudflare displays both the parent category and the detailed child category. You can <a href="/security-center/investigate/change-categorization/">request category changes</a> for a domain. Miscategorized domains can also request to have a category added. This request goes through an approval process with the Cloudflare team.</p>
<p>As part of the domain search results, Cloudflare show the WHOIS details and a history of its category changes over time.</p>
<h2 id="as-number">AS Number</h2>
<p>An <a href="https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/">AS number</a> is a group of IP addresses belonging to and controlled by a single organization. The entire group of networks have a single unified routing policy. The <a href="https://www.iana.org/">Internet Assigned Numbers Authority</a> (IANA) is the organization responsible for managing the assignment and distribution of AS numbers. The AS number's routing policies are used by <a href="https://www.cloudflare.com/learning/security/glossary/what-is-bgp/">BGP</a> which is how Cloudflare's <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">anycast network</a> works.</p>
<p>When you search for an AS number, Cloudflare will return registration data such as its country, description and type. It will also display data such as domain count, top 10 domains and subnets.</p>
<p>With sufficient data, AS number search results will also return the geographical distribution of traffic in its network, application level attacks and network level attacks, each broken down by Cloudflare mitigation techniques and network protocols, respectively.</p>
<h2 id="hash">Hash</h2>
<p>When you search for a hash, the Cloudflare dashboard will provide a URL report for that specific hash.</p>
<p>To search using a hash:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Investigate</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enter the hash, then select <strong>Search</strong>.</li>
<li>Select <strong>View report</strong> to view the report for your URL.</li>
</ol>
<h2 id="url">URL</h2>
<p>When you search for a URL, Cloudflare will provide a list of recent scan reports for that specific URL, limited to the past 30 days. You can view previously generated reports or scan again to generate a new report.</p>
<p>Different Cloudflare plans will have different <a href="/security-center/investigate/scan-limits/">scan limitations</a>.</p>
<p>If you want to scan a URL:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Investigate</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enter the URL, then select <strong>Search</strong>.</li>
</ol>
<p>Alternatively, to scan a URL, go to <a href="https://radar.cloudflare.com/">Cloudflare Radar</a> &gt; <strong>URL scanner</strong>. Enter the URL, then select <strong>Publish</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13807.md")
</aside>
<h3 id="visibility">Visibility</h3>
<p>When generating a new scan report, the default visibility is set to <code>Unlisted</code>, but you have the option to set it to <code>Public</code>. By choosing <code>Public</code>, the generated scan will be available to all Cloudflare dashboard and Cloudflare Radar users alike, which will increase awareness of potentially malicious websites for others.</p>
<p>We recommend choosing <code>Unlisted</code> if you are scanning infrastructure that is not intended to be shared with the wider Cloudflare community.</p>
<h3 id="filters">Filters</h3>
<p>While viewing the most recent scans, you can use the filtering options. Selecting <code>All account scans</code> will display both <code>Unlisted</code> or <code>Public</code> scans initiated from your Cloudflare account. However, by selecting <code>All global scans</code>, only <code>Public</code> scans are displayed.</p>
<h3 id="downloads">Downloads</h3>
<p>You can download a report of your scan in HAR or JSON format.</p>
<p>To download a report:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Investigate</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enter your domain and select <strong>Search</strong>.</li>
<li>Once the report has been generated, select <strong>Download</strong> and choose between <strong>Download HAR</strong> or <strong>Download JSON</strong>.</li>
</ol>
