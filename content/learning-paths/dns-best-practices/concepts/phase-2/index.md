---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-2/
  description: Prepare for DNS migration with minimal downtime.
  full_title: 'Phase 2: Preparation · Cloudflare Learning Paths'
  head_html: '<title>Phase 2: Preparation · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Prepare for DNS migration with minimal downtime."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-2/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-2/index.md"><meta property="og:title" content="Phase 2: Preparation · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Prepare for DNS migration with minimal downtime."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-2/#page","headline":"Phase 2: Preparation \u00b7 Cloudflare Learning Paths","description":"Prepare for DNS migration with minimal downtime.","url":"https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: true
  noindex: false
  route: /learning-paths/dns-best-practices/concepts/phase-2/
  schema: 1
---
<p>Careful preparation will minimize downtime and issues during the cutover.</p>
<h2 id="1-reduce-dns-record-ttls-time-to-live"><ol>
<li>Reduce DNS record TTLs (Time To Live)</li>
</ol></h2>
<p>At least 24-48 hours (or longer, ideally matching your longest current TTLs) before your planned migration window, lower the TTLs for all critical records in your BIND zone files. A common short TTL for migration is 300 seconds (5 minutes).</p>
<p>This ensures that DNS resolvers worldwide will cache your old records for a shorter period, allowing changes to propagate more quickly when you switch to Cloudflare.</p>
<ul>
<li>SOA Record: Also consider lowering the <code>MINIMUM</code> field in your SOA record, which dictates the TTL to be used for negative responses (<a href="https://www.rfc-editor.org/rfc/rfc2308.html#section-4">RFC 2308</a>).</li>
</ul>
<h2 id="2-export-zone-files-from-bind"><ol start="2">
<li>Export zone files from BIND</li>
</ol></h2>
<p>Obtain a clean and current export of your zone files from your BIND servers in standard BIND format and ensure these files are complete and accurate.</p>
<h2 id="3-add-domains-to-cloudflare"><ol start="3">
<li>Add domains to Cloudflare</li>
</ol></h2>
<ol>
<li>Log in to your Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Add each domain you intend to migrate. Cloudflare will attempt to scan for existing DNS records.</li>
</ol>
<h2 id="4-import-dns-records-into-cloudflare"><ol start="4">
<li>Import DNS Records into Cloudflare</li>
</ol></h2>
<p>Use Cloudflare's <strong>Import and Export</strong> feature (under <strong>DNS</strong> &gt; <strong>Records</strong>) to upload your BIND zone files.</p>
<div class="nb-dash-button"></div>
<ul>
<li>Verification (Crucial):
<ul>
<li>After import, meticulously compare the records in Cloudflare with your BIND zone files or a <code>dig</code> output of your current zone.</li>
<li>Pay close attention to <code>MX</code> records, <code>SRV</code> records, <code>TXT</code> records (especially for <code>SPF</code>, <code>DKIM</code>, <code>DMARC</code>), and any complex <code>CNAME</code> configurations.</li>
<li>Ensure FQDNs (Fully Qualified Domain Names) are correctly formatted (Cloudflare usually handles the trailing dot correctly on import, but verify).</li>
</ul>
</li>
<li>Proxy status (orange vs grey cloud):
<ul>
<li>For <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records that point to HTTP or HTTPS services you want to proxy through Cloudflare (for example, websites and APIs), you can enable the orange cloud to use Cloudflare CDN and security features.</li>
<li>Some services and ports are not supported behind the proxy, and certain record types (for example, <code>MX</code> targets and many non-HTTP services) must remain <strong>DNS only</strong>. For a detailed list, refer to <a href="/dns/proxy-status/limitations/">Proxy status and limitations</a>.</li>
<li>Recommendation for initial migration: To isolate the DNS migration from potential proxy-related issues, consider setting all records to <strong>DNS only</strong> (grey cloud) initially. After you confirm that DNS resolution is working correctly, enable the proxy (orange cloud) for specific HTTP(S) records and test again.</li>
</ul>
</li>
</ul>
<h2 id="5-dnssec-preparation-if-currently-enabled"><ol start="5">
<li>DNSSEC preparation (if currently enabled)</li>
</ol></h2>
<p>Complete this step before you change your nameservers at the registrar.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9758.md")
</aside>
<ul>
<li><strong>Action at registrar:</strong> Log in to your domain registrar and delete the existing DS records associated with your on-prem BIND DNSSEC keys for each domain.</li>
<li><strong>Wait for DS TTL:</strong> Wait at least the full DS record TTL published at the parent zone, and preferably up to 1.5 times that TTL, before you change nameservers. This ensures that validating resolvers stop expecting the old DNSSEC chain. The typical TTL duration for DS records is set to +24 hours (86,400 seconds).</li>
<li><strong>Impact of incorrect timing:</strong> If you change nameservers while resolvers still expect the old DS record, DNSSEC validation will fail and your domain may become unreachable for validating resolvers.</li>
</ul>
