---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/
  description: Manage DNS records for your Cloudflare zones.
  full_title: DNS records · Cloudflare DNS docs
  head_html: <title>DNS records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage DNS records for your Cloudflare zones."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/index.md"><meta property="og:title" content="DNS records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage DNS records for your Cloudflare zones."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/dns/manage-dns-records/#page","headline":"DNS records \u00b7 Cloudflare DNS docs","description":"Manage DNS records for your Cloudflare zones.","url":"https://developers.cloudflare.com/dns/manage-dns-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/
  schema: 1
---
<p>DNS records contain information about your domain and are used to make your website or application available to visitors and other web services.</p>
<p>Each DNS record belongs to a different type, and each type serves a different purpose. For background about the different types of DNS records, refer to the <a href="https://www.cloudflare.com/learning/dns/dns-records/">Learning Center</a>. To quickly find reference information about a specific type, refer to <a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a>.</p>
<p>Depending on the providers you used to <a href="/fundamentals/manage-domains/#get-a-domain-name">get your domain name</a> and <a href="/fundamentals/manage-domains/#host-your-domain">host your website or application</a>, it is expected that DNS records were automatically created on your behalf. According to your <a href="/dns/zone-setups/">setup</a>, you can use Cloudflare to manage your DNS records.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/cd8b06dfaf43918ab8d0590f03ec68b7/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F64a4facf-6882-4c95-9001-492fdeae8200%2Fpublic" title="How DNS and nameservers work" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="dns-records-table">DNS records table</h2>
<p>When managing your records at Cloudflare, besides the common record fields described below, you may also find an option for <a href="/dns/proxy-status/">Proxy status</a> and <a href="/dns/cname-flattening/">CNAME flattening</a>. These are specific features offered by Cloudflare.</p>
<details class="nb-details"><summary>Record fields</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7620.md")
</div></details>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@input("content/.markup/bodies/7623.md")
</div></details>
<h2 id="dns-records-quota">DNS records quota</h2>
<p>Cloudflare limits the number of DNS records you can create. Depending on your plan, this limit is enforced either per zone or per account — not both.</p>
<p>DNS records that other Cloudflare services create on your behalf — for example, the <code>TXT</code> and <code>MX</code> records added by <a href="/email-service/">Email Routing</a> — also count toward your quota. To avoid disrupting those services, they are enforced against your record limit with a small buffer, so a zone may occasionally hold slightly more records than its limit would otherwise allow.</p>
<p>To create new records yourself through the dashboard or API, your zone must still be within its record limit.</p>
<h3 id="per-zone-quota">Per-zone quota</h3>
<p>By default, there is a limit to the number of records you can create on a single <span class="nb-glossary-tooltip" title="DNS zone">zone</span>.</p>
<ul>
<li>Free zones created before <code>2024-09-01 00:00:00 UTC</code>: 1,000</li>
<li>Free zones created on or after <code>2024-09-01 00:00:00 UTC</code>: 200</li>
<li>Pro: 3,500</li>
<li>Business: 3,500</li>
<li>Enterprise: falls under the <a href="#per-account-quota">per-account quota</a> (no separate per-zone limit).</li>
</ul>
<p>You can retrieve a zone's current quota (if applicable) and usage <a href="/api/resources/dns/subresources/usage/subresources/zone/methods/get/">via the API</a>.</p>
<h3 id="per-account-quota">Per-account quota</h3>
<p>Enterprise accounts have a quota on the total number of records across all of their zones, instead of the per-zone limit. This lets you distribute records across your zones however you like, regardless of each zone's plan.</p>
<p>Public zones and <a href="/dns/internal-dns/">internal zones</a> are counted separately, each with a default account quota of 1,000,000 records.</p>
<p>You can retrieve your current account quota and usage <a href="/api/resources/dns/subresources/usage/subresources/account/methods/get/">via the API</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="for-more-dns-records">For more DNS records</h3>
@markup("md", "content/.markup/bodies/7619.md")
</aside>
<h2 id="resources">Resources</h2>
<h3 id="how-to">How to</h3>
<ul class="directory-listing"><li><a href="/dns/manage-dns-records/how-to/create-dns-records/">Manage DNS records</a></li><li><a href="/dns/manage-dns-records/how-to/create-zone-apex/">Create zone apex record</a></li><li><a href="/dns/manage-dns-records/how-to/create-subdomain/">Create subdomain records</a></li><li><a href="/dns/manage-dns-records/how-to/email-records/">Set up email records</a></li><li><a href="/dns/manage-dns-records/how-to/set-up-google-workspace/">Set up Google Workspace DNS records</a></li><li><a href="/dns/manage-dns-records/how-to/import-and-export/">Import and export records</a></li><li><a href="/dns/manage-dns-records/how-to/batch-record-changes/">Batch record changes</a></li><li><a href="/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/">Dynamically update DNS records</a></li><li><a href="/dns/manage-dns-records/how-to/round-robin-dns/">Round-robin DNS</a></li><li><a href="/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/">Delegate subdomains</a></li></ul>
<h3 id="reference">Reference</h3>
<ul class="directory-listing"><li><a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a></li><li><a href="/dns/manage-dns-records/reference/ttl/">Time to Live (TTL)</a></li><li><a href="/dns/manage-dns-records/reference/record-attributes/">Record attributes</a></li><li><a href="/dns/manage-dns-records/reference/wildcard-dns-records/">Wildcard DNS records</a></li><li><a href="/dns/manage-dns-records/reference/shadowed-records/">Shadowed records</a></li><li><a href="/dns/manage-dns-records/reference/vendor-specific-records/">Vendor-specific DNS records</a></li></ul>
<h3 id="troubleshooting">Troubleshooting</h3>
<ul class="directory-listing"><li><a href="/dns/manage-dns-records/troubleshooting/records-with-same-name/">Records with the same name</a></li><li><a href="/dns/manage-dns-records/troubleshooting/unexpected-dns-records/">Unexpected DNS records</a></li><li><a href="/dns/manage-dns-records/troubleshooting/exposed-ip-address/">Exposed IP addresses</a></li><li><a href="/dns/manage-dns-records/troubleshooting/cname-domain-verification/">Verify a domain with CNAME</a></li><li><a href="/dns/manage-dns-records/troubleshooting/existing-ns-record/">NS records already exist</a></li><li><a href="/dns/manage-dns-records/troubleshooting/stale-response/">Stale response for upstream DNS resolution</a></li></ul>
