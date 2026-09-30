---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/unexpected-dns-records/
  description: Identify and remove unexpected DNS records.
  full_title: Unexpected DNS records · Cloudflare DNS docs
  head_html: <title>Unexpected DNS records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Identify and remove unexpected DNS records."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/unexpected-dns-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/unexpected-dns-records/index.md"><meta property="og:title" content="Unexpected DNS records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Identify and remove unexpected DNS records."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/unexpected-dns-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/unexpected-dns-records/#page","headline":"Unexpected DNS records \u00b7 Cloudflare DNS docs","description":"Identify and remove unexpected DNS records.","url":"https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/unexpected-dns-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/troubleshooting/unexpected-dns-records/
  schema: 1
---
<h2 id="additional-records-after-import">Additional records after import</h2>
<p>You find several unexpected DNS records after adding your domain to Cloudflare.</p>
<h3 id="cause">Cause</h3>
<p>A wildcard (<code>*</code>) record at your previous authoritative DNS provider may have been imported into Cloudflare in a way that creates additional records.</p>
<h3 id="solution">Solution</h3>
<p>To solve this issue, you can do one of the following:</p>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/batch-record-changes/#delete-records-in-bulk">Delete records in bulk</a>.</p>
</li>
<li>
<p>Remove and re-add your domain:</p>
<ol>
<li><a href="/fundamentals/manage-domains/remove-domain/">Remove your domain</a> from Cloudflare.</li>
<li>Delete the wildcard record from your authoritative DNS.</li>
<li><a href="/fundamentals/manage-domains/add-site/">Re-add</a> the domain.</li>
</ol>
</li>
</ul>
<hr />
<h2 id="acme-challenge-txt-records">acme_challenge TXT records</h2>
<p>You might notice TXT records like <code>_acme-challenge.&lt;hostname&gt;</code> are returned by your domain but cannot be found on the Cloudflare dashboard.</p>
<h3 id="cause-1">Cause</h3>
<p>These records are automatically created to allow Cloudflare edge certificates (<a href="/ssl/edge-certificates/universal-ssl/">universal</a>, <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced</a>, and <a href="/ssl/edge-certificates/backup-certificates/">backup</a>) to be provisioned. <code>_acme-challenge</code> records are required by <span class="nb-glossary-tooltip" title="Certificate Authority (CA)">certificate authorities (CAs)</span> so that they can verify your domain ownership before issuing the SSL/TLS certificate. For details, refer to <a href="/ssl/edge-certificates/changing-dcv-method/">Domain control validation (DCV)</a>.</p>
<h3 id="solution-1">Solution</h3>
<p>As these records are tied to the certificates, they cannot be deleted via the Cloudflare dashboard.</p>
<p>If you need more <code>_acme-challenge.&lt;hostname&gt;</code> TXT records in order to provision certificates on your side, you can <a href="/dns/manage-dns-records/how-to/create-dns-records/">manually add them</a> under <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records">DNS records</a>.</p>
<p>If you want to remove these records:</p>
<ul>
<li><a href="/ssl/edge-certificates/universal-ssl/disable-universal-ssl/">Disable Universal SSL</a> to remove the records related to universal and backup certificates.</li>
<li><a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#delete-a-certificate">Delete advanced certificates</a> to remove the records related to advanced certificates.</li>
</ul>
<hr />
<h2 id="dc-mx-and-dc-subdomains">_dc-mx and dc-##### subdomains</h2>
<p>You notice a <code>_dc-mx</code> or <code>dc-#####</code> subdomain that you did not create (for example, <code>_dc-mx.a1b2c3d4e5f6.example.com</code>). This response does not appear in your Cloudflare DNS records table, but will appear in <code>dig</code> responses.</p>
<h3 id="cause-2">Cause</h3>
<p>When your <code>MX</code> or <code>SRV</code> record resolves to a domain configured to <a href="/dns/proxy-status/">proxy</a> through Cloudflare, Cloudflare dynamically inserts a record into DNS responses that resolves to the origin IP address. This record is added at query time to ensure that mail or service traffic bypasses the Cloudflare proxy and reaches your server directly.</p>
<p>The prefix of the auto-generated record depends on the record type that triggered it:</p>
<ul>
<li><strong>MX records:</strong> Cloudflare inserts a record with the <code>_dc-mx</code> prefix (for example, <code>_dc-mx.a1b2c3d4e5f6.example.com</code>).</li>
<li><strong>SRV records:</strong> Cloudflare inserts a record with the <code>dc-</code> prefix (for example, <code>dc-a1b2c3d4e5f6.example.com</code>).</li>
</ul>
<h4 id="how-dc-mx-records-work">How _dc-mx records work</h4>
<p>Before using Cloudflare, suppose your DNS records for mail are as follows:</p>
<p><code>example.com MX example.com</code></p>
<p><code>example.com A 192.0.2.1</code></p>
<p>After using Cloudflare and proxying the <code>A</code> record, Cloudflare provides DNS responses with a <a href="/fundamentals/concepts/cloudflare-ip-addresses/">Cloudflare IP address</a> (<code>203.0.113.1</code> in the example below):</p>
<p><code>example.com MX example.com</code></p>
<p><code>example.com A 203.0.113.1</code></p>
<p>Since proxying mail traffic through Cloudflare would break your mail services, Cloudflare detects this situation and dynamically inserts a <code>_dc-mx</code> record into DNS responses:</p>
<p><code>example.com MX _dc-mx.a1b2c3d4e5f6.example.com</code></p>
<p><code>_dc-mx.a1b2c3d4e5f6.example.com A 192.0.2.1</code></p>
<p><code>example.com A 203.0.113.1</code></p>
<p>You can verify this behavior by querying your domain's MX records (replace <code>example.com</code> with your domain):</p>
<pre tabindex="0"><code class="language-sh">dig example.com mx +short&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">100 _dc-mx.a1b2c3d4e5f6.example.com.&#10;</code></pre>
<p>The <code>_dc-mx</code> record resolves directly to your origin IP:</p>
<pre tabindex="0"><code class="language-sh">dig _dc-mx.a1b2c3d4e5f6.example.com a +short&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">192.0.2.1&#10;</code></pre>
<h3 id="solution-2">Solution</h3>
<p>These records are safe — they ensure your mail traffic reaches your server correctly.</p>
<p>If you want to avoid a <code>_dc-mx</code> or <code>dc-#####</code> response, you must address the underlying proxy conflict:</p>
<ul>
<li>
<p>If no mail is received for the domain, delete the <code>MX</code> record.</p>
</li>
<li>
<p>If mail is received for the domain, update the <code>MX</code> record to resolve to a separate <code>A</code> record for a mail subdomain that is not proxied by Cloudflare:</p>
<p><code>example.com MX mail.example.com</code></p>
<p><code>mail.example.com A 192.0.2.1</code></p>
<p><code>example.com A 203.0.113.1</code></p>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7761.md")
</aside>
<hr />
<h2 id="incorrect-results-for-dns-queries">Incorrect results for DNS queries</h2>
<p>You notice DNS queries returning incorrect results even after you waited for the <a href="/dns/manage-dns-records/reference/ttl/">TTL</a> to expire.</p>
<h3 id="cause-3">Cause</h3>
<p>Third-party tools can sometimes fail to return correct DNS results if a recursive DNS cache fails to refresh.</p>
<h3 id="solution-3">Solution</h3>
<p>In this circumstance, purge your public DNS cache via these methods:</p>
<ul>
<li><a href="http://www.opendns.com/support/cache/">Purge your DNS cache at OpenDNS</a></li>
<li><a href="https://developers.google.com/speed/public-dns/cache">Purge your DNS cache at Google</a></li>
<li><a href="https://docs.cpanel.net/knowledge-base/dns/how-to-clear-your-dns-cache/">Purge your DNS cache locally</a></li>
</ul>
