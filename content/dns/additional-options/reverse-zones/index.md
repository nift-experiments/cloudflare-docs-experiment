---
cp9:
  canonical: https://developers.cloudflare.com/dns/additional-options/reverse-zones/
  description: Set up reverse DNS zones and PTR records.
  full_title: Reverse zones and PTR records · Cloudflare DNS docs
  head_html: <title>Reverse zones and PTR records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up reverse DNS zones and PTR records."><link rel="canonical" href="https://developers.cloudflare.com/dns/additional-options/reverse-zones/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/additional-options/reverse-zones/index.md"><meta property="og:title" content="Reverse zones and PTR records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up reverse DNS zones and PTR records."><meta property="og:url" content="https://developers.cloudflare.com/dns/additional-options/reverse-zones/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="IPv4,IPv6"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/additional-options/reverse-zones/#page","headline":"Reverse zones and PTR records \u00b7 Cloudflare DNS docs","description":"Set up reverse DNS zones and PTR records.","url":"https://developers.cloudflare.com/dns/additional-options/reverse-zones/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPv4","IPv6"]}</script>
  markdown: true
  noindex: false
  route: /dns/additional-options/reverse-zones/
  schema: 1
---
<p>If you control your own IP prefix(es), you can set up reverse zones with PTR records to allow reverse DNS lookups.</p>
<h2 id="ptr-records">PTR records</h2>
<p>PTR records specify the allowed hosts for a given IP address. They are the opposite of <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-a-record">A records</a> and used for reverse DNS lookups.</p>
<p>Historically, PTR records prevented outbound SMTP servers from being blocked by spam filters. However, more modern DNS records — <a href="/dns/manage-dns-records/how-to/email-records/#prevent-domain-spoofing">SPF, DKIM, and DMARC</a> — provide better verifications of domain ownership.</p>
<p>Now, PTR records are primarily useful for those who own a dedicated IP space. They can help populate trace routes and security tools with human-readable domain names.</p>
<p>As PTR records are mainly used for reverse DNS lookups, they should preferably be added to reverse zones.</p>
<h2 id="availability">Availability</h2>
<p>The following Cloudflare customers can create reverse zones.</p>
<ul>
<li>Customers with an IPv4 or IPv6 address space can add the IPv4 or IPv6 reverse zone for their IP space to their account, and create the required PTR records for forward resolution.</li>
<li>DNS Firewall customers need to contact their account team to add PTR records for the IPs used for their DNS Firewall clusters.</li>
</ul>
<p>If your account does not meet these qualifications and you do not own the IP prefix you want to add PTR records on, contact the owner of the IP address based on a <a href="https://lookup.icann.org/">whois lookup</a>.</p>
<h2 id="set-up-a-reverse-zone">Set up a reverse zone</h2>
<p>To set up a reverse zone, you need to create a reverse DNS zone and add PTR records for forward resolution.</p>
<h3 id="1-create-a-reverse-dns-zone"><ol>
<li>Create a reverse DNS zone</li>
</ol></h3>
<ol>
<li>
<p>Within your account, click <strong>Add</strong> &gt; <strong>Connect a domain</strong>.</p>
</li>
<li>
<p>For your site name, use the reverse IP address:</p>
<ul>
<li>
<p>For IPv4 /24 prefixes, the pattern is:</p>
<ul>
<li><strong>IP prefix</strong>: <code>&lt;octet_1&gt;.&lt;octet_2&gt;.&lt;octet_3&gt;.0/24</code></li>
<li><strong>Reverse zone address</strong>: <code>&lt;octet_3&gt;.&lt;octet_2&gt;.&lt;octet_1&gt;.in-addr.arpa</code></li>
</ul>
</li>
<li>
<p>For IPv4 /16 prefixes, the pattern is:</p>
<ul>
<li><strong>IP prefix</strong>: <code>&lt;octet_1&gt;.&lt;octet_2&gt;.0.0/16</code></li>
<li><strong>Reverse zone address</strong>: <code>&lt;octet_2&gt;.&lt;octet_1&gt;.in-addr.arpa</code></li>
</ul>
</li>
</ul>
 <details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/7723.md")
</div></details>
<pre tabindex="0"><code>* For IPv6, consider the following examples:&#10;</code></pre>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/7724.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/7725.md")
</div>
<ol start="3">
<li>
<p>If you are adding less than 200 PTR records, select the <strong>Free</strong> plan. If you are adding more, select a paid plan.</p>
</li>
<li>
<p>Skip the rest of the onboarding process.</p>
</li>
</ol>
<h3 id="2-add-ptr-records"><ol start="2">
<li>Add PTR records</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>DNS Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>For each IP within the prefix, add a PTR record using the least significant octet(s) as the subdomain.</li>
</ol>
  <details class="nb-details"><summary>IPv4 example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7727.md")
</div></details>
  <details class="nb-details"><summary>IPv6 example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7729.md")
</div></details>
<h3 id="3-set-cloudflare-nameservers"><ol start="3">
<li>Set Cloudflare nameservers</li>
</ol></h3>
<p>Add the two Cloudflare nameservers provided for the zone at your Regional Internet Registry (RIR). The exact steps to update your nameservers will depend on the registry you are using.</p>
<p>After this process, your reverse zone will be activated and you can perform reverse DNS lookups.</p>
<h2 id="other-resources">Other resources</h2>
<p>While setting up reverse zones, the following third-party tools may be useful:</p>
<ul>
<li><a href="https://www.whatsmydns.net/reverse-dns-generator">Reverse DNS record generator</a></li>
<li><a href="https://www.internex.at/de/toolbox/ipv6">IPv6 subnet calculator</a></li>
</ul>
