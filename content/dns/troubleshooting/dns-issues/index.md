---
cp9:
  canonical: https://developers.cloudflare.com/dns/troubleshooting/dns-issues/
  description: Troubleshoot common DNS resolution errors like "This site can't be reached", err_name_not_resolved, and Error 1001 when using Cloudflare.
  full_title: General DNS issues · Cloudflare DNS docs
  head_html: <title>General DNS issues · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot common DNS resolution errors like &quot;This site can&#x27;t be reached&quot;, err_name_not_resolved, and Error 1001 when using Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/dns/troubleshooting/dns-issues/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/troubleshooting/dns-issues/index.md"><meta property="og:title" content="General DNS issues · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot common DNS resolution errors like &quot;This site can&#x27;t be reached&quot;, err_name_not_resolved, and Error 1001 when using Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/dns/troubleshooting/dns-issues/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/troubleshooting/dns-issues/#page","headline":"General DNS issues \u00b7 Cloudflare DNS docs","description":"Troubleshoot common DNS resolution errors like \"This site can't be reached\", errnamenotresolved, and Error 1001 when using Cloudflare.","url":"https://developers.cloudflare.com/dns/troubleshooting/dns-issues/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/troubleshooting/dns-issues/
  schema: 1
---
<p>In web browsers such as Safari or Chrome, there are several commonly observable DNS errors:</p>
<ul>
<li><code>This site can't be reached</code></li>
<li><code>This webpage is not available</code></li>
<li><code>err_name_not_resolved</code></li>
<li><code>Can't find the server</code></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/"><code>Error 1001 DNS resolution error</code></a></li>
</ul>
<h2 id="common-causes-and-resolutions">Common causes and resolutions</h2>
<p>Below are the most common causes for DNS resolution errors along with suggested solutions.</p>
<h3 id="mistyped-domain-or-subdomain">Mistyped domain or subdomain</h3>
<p>Verify that the domain or subdomain was correctly spelled in the request URL.</p>
<h3 id="missing-dns-records">Missing DNS records</h3>
<p>Ensure that you have the necessary DNS records for the domain or subdomain that is presenting the error.</p>
<div class="nb-dash-button"></div>
<p>This includes having the following records:</p>
<ul>
<li>The <a href="/dns/manage-dns-records/how-to/create-zone-apex/">zone apex</a> (e.g., <code>example.com</code>) record.</li>
<li>Existing <a href="/dns/manage-dns-records/how-to/create-subdomain/">subdomains</a> (<code>www.example.com</code>, <code>blog.example.com</code>) records.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7562.md")
</aside>
<h3 id="dnssec-was-not-disabled-before-the-domain-was-added-to-cloudflare">DNSSEC was not disabled before the domain was added to Cloudflare</h3>
<p>DNS resolution failures occur if <a href="/dns/dnssec/#disable-dnssec">DNSSEC is not disabled</a> at your domain provider before you add the domain to Cloudflare.</p>
<h3 id="nameservers-no-longer-point-to-cloudflare">Nameservers no longer point to Cloudflare</h3>
<p>If you manage DNS records via the Cloudflare dashboard and your domain stops pointing to Cloudflare's nameservers, DNS resolution will stop functioning.</p>
<p>This can occur if your domain registrar switches the nameservers for your domain to point to their default nameservers. To confirm if this is the problem, <a href="/dns/zone-setups/full-setup/setup/#35-verify-changes">check whether your domain uses Cloudflare's nameservers</a>.</p>
<h3 id="unresolved-ip-address">Unresolved IP address</h3>
<p>In rare cases, the DNS resolver in the client requesting the URL might fail to resolve a DNS record to a valid IP address.</p>
<p>Reload the page after a short wait to note if the problem disappears. This issue is unrelated to Cloudflare, but using <a href="/1.1.1.1/setup/">Cloudflare's DNS resolver</a> may help. Contact your hosting provider for additional help with your current DNS resolver.</p>
<h3 id="newly-created-record-still-does-not-resolve">Newly created record still does not resolve</h3>
<p>If you recently created a DNS record and resolvers still return <code>NXDOMAIN</code> (Non-Existent Domain) or no answer, it is likely because a negative response is currently stored in the resolver's cache.</p>
<p>When a resolver is queried for a hostname that has no DNS records yet, it caches the empty response so it does not have to ask the authoritative nameserver again immediately. This is known as negative caching.</p>
<p>For newly created records:</p>
<ul>
<li>The resolver might not have cached the new record yet. Instead, it is using a prior <code>NXDOMAIN</code> cache entry that says &quot;this record does not exist,&quot; which was generated if the hostname was queried before you created the record.</li>
<li>The duration of this negative cache is determined by the <code>MINIMUM</code> field in your zone's SOA record (per <a href="https://datatracker.ietf.org/doc/html/rfc2308">RFC 2308</a>), not the TTL of the record you just created. Different resolvers may cache for varying durations.</li>
</ul>
<p>This means:</p>
<ul>
<li>Lowering the TTL on your new record will not speed up resolution if a negative cache entry already exists; the resolver will only see your new TTL after the old negative entry expires.</li>
<li>Flushing your local DNS cache only affects your specific device; the upstream recursive resolver (for example, your ISP or a public provider) still holds the negative result.</li>
<li>Propagation appears uneven because different resolvers may have queried the name at different times, apply different negative cache TTLs, or have no negative cache entry at all.</li>
</ul>
<p>The exact behavior differs per resolver, but to estimate how long you need to wait, query your zone's SOA record and look at the last value (the <code>MINIMUM</code> field). You must wait for that interval to pass since the last <code>NXDOMAIN</code> query before the new record will consistently resolve.</p>
<p>You can check if a negative cache entry is active by querying for the non-existent (or newly created) hostname:</p>
<pre tabindex="0"><code class="language-sh">dig +noall +answer +authority mynewrecord.example.com&#10;</code></pre>
<p>If the record is still negatively cached, the response will include the zone's SOA record in the authority section with a TTL indicating how many seconds remain before the entry expires:</p>
<pre tabindex="0"><code class="language-txt">example.com.		256	IN	SOA	...&#10;</code></pre>
<p>In this example, the negative cache response will continue for 256 more seconds.</p>
<p>To verify the record resolves correctly, you can purge the cache for public resolvers and query the record. If this works, other resolvers will eventually start resolving as well:</p>
<ul>
<li><a href="https://one.one.one.one/purge-cache/">Purge 1.1.1.1 cache</a></li>
<li><a href="https://dns.google/cache">Purge 8.8.8.8 cache</a></li>
<li><a href="https://dns.google/">Query 8.8.8.8</a></li>
<li><a href="https://cachecheck.opendns.com/">Query and refresh OpenDNS cache</a></li>
</ul>
<h4 id="further-debugging">Further debugging</h4>
<p>To verify the record was correctly created, query Cloudflare's authoritative nameservers directly:</p>
<pre tabindex="0"><code class="language-sh">&#35; Find the authoritative nameservers for your zone&#10;dig @1.1.1.1 example.com NS +short&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Query the authoritative nameserver for your new record&#10;dig @hera.ns.cloudflare.com mynewrecord.example.com A&#10;</code></pre>
<p>Querying the authoritative nameserver directly bypasses resolver caching. If the record is returned, resolvers will eventually start returning it as well. If the record does not appear, verify the record exists in the Cloudflare dashboard and that the hostname matches exactly.</p>
<h3 id="account-recovery">Account recovery</h3>
<p>If you are locked out of the Cloudflare account that contains your DNS configuration, refer to <a href="/fundamentals/user-profiles/account-recovery/">Account recovery</a>.</p>
