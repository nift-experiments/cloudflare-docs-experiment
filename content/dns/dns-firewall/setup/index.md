---
cp9:
  canonical: https://developers.cloudflare.com/dns/dns-firewall/setup/
  description: Set up DNS Firewall to protect upstream nameservers from DDoS attacks and reduce load by caching DNS responses.
  full_title: Set up DNS Firewall · Cloudflare DNS docs
  head_html: <title>Set up DNS Firewall · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up DNS Firewall to protect upstream nameservers from DDoS attacks and reduce load by caching DNS responses."><link rel="canonical" href="https://developers.cloudflare.com/dns/dns-firewall/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dns-firewall/setup/index.md"><meta property="og:title" content="Set up DNS Firewall · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up DNS Firewall to protect upstream nameservers from DDoS attacks and reduce load by caching DNS responses."><meta property="og:url" content="https://developers.cloudflare.com/dns/dns-firewall/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS Firewall"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dns-firewall/setup/#page","headline":"Set up DNS Firewall \u00b7 Cloudflare DNS docs","description":"Set up DNS Firewall to protect upstream nameservers from DDoS attacks and reduce load by caching DNS responses.","url":"https://developers.cloudflare.com/dns/dns-firewall/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/dns-firewall/setup/
  schema: 1
---
<h2 id="prerequisites">Prerequisites</h2>
<p>Prior to setting up DNS Firewall, you need:</p>
<ul>
<li>Account access to DNS Firewall (provided by your Enterprise account team).</li>
<li>Access to <strong>DNS Administrator</strong> or <strong>Super Administrator</strong> privileges on your account.</li>
<li>Newly updated IP addresses for your nameservers (protects against previously compromised IP addresses).</li>
</ul>
<h2 id="configure-dns-firewall">Configure DNS Firewall</h2>
<h3 id="create-a-dns-firewall-cluster">Create a DNS Firewall cluster</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7701.md")
</div></div>
<h3 id="update-registrar-settings">Update registrar settings</h3>
<p>Update the <code>A/AAAA</code> glue records for your nameserver hostnames at your registrar with your DNS Firewall cluster IP addresses.</p>
<h3 id="update-dns-servers">Update DNS servers</h3>
<p>At your DNS servers, update the <code>A/AAAA</code> records for your nameserver hostnames in your DNS zone file with your DNS Firewall cluster IP addresses.</p>
<h3 id="test-dns-resolution">Test DNS resolution</h3>
<p>Confirm that your nameservers are functioning correctly by running a <code>dig</code> command.</p>
<h3 id="update-security-policies">Update security policies</h3>
<p>Configure security policy in your DNS servers and Firewall to allow only <a href="https://cloudflare.com/ips">Cloudflare IPs</a> and TCP/UDP port 53.</p>
<h2 id="additional-options">Additional options</h2>
<p>Beyond the required fields, you can configure the following settings on your DNS Firewall cluster — in the Cloudflare dashboard when you create or edit a cluster, or via the API:</p>
<ul>
<li><strong>Rate limit</strong> (queries per second per data center).</li>
<li><strong>Negative cache TTL</strong> for <code>REFUSED</code>, <code>NXDOMAIN</code>, and <code>SERVFAIL</code> responses.</li>
<li><strong>EDNS Client Subnet (ECS) fallback</strong> — forward the resolver's IP subnet when the incoming query does not include ECS data. Refer to the <a href="/dns/dns-firewall/faq/#does-dns-firewall-support-edns-client-subnet-ecs">FAQ</a> for details.</li>
<li><strong>Attack mitigation</strong> for <a href="/dns/dns-firewall/random-prefix-attacks/">random prefix attacks</a>.</li>
</ul>
<p>For the full parameter reference, refer to the <a href="/api/resources/dns_firewall/methods/create/">Create</a> and <a href="/api/resources/dns_firewall/methods/edit/">Update</a> DNS Firewall Cluster API endpoints.</p>
