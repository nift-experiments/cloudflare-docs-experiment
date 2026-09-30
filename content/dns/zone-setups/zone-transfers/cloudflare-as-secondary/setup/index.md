---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/
  description: With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider.
  full_title: Set up incoming zone transfers (Cloudflare as Secondary) · Cloudflare DNS docs
  head_html: <title>Set up incoming zone transfers (Cloudflare as Secondary) · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/index.md"><meta property="og:title" content="Set up incoming zone transfers (Cloudflare as Secondary) · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/#page","headline":"Set up incoming zone transfers (Cloudflare as Secondary) \u00b7 Cloudflare DNS docs","description":"With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider.","url":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/
  schema: 1
---
<p>With <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">incoming zone transfers</a>, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider.</p>
<p>Normal incoming zone transfers only provide DNS resolution. If you also want your traffic to benefit from Cloudflare's performance and security features, you need to <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">set up Secondary DNS Override</a>.
<br /></p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>You should already have a registered domain, set up with your primary DNS provider.</li>
<li>Review the available options and plan for how you will use <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/">DNSSEC with Cloudflare as secondary</a>.</li>
<li>Make sure you have completed the following tasks at your primary DNS provider and at Cloudflare.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8031.md")
</aside>
<h2 id="at-your-primary-dns-provider">At your primary DNS provider</h2>
<p>Your primary DNS provider should allow traffic from the IP address and port specified in your <a href="#2-create-peer-server">peer server configuration</a>.</p>
<p>It should also have updated <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/#cloudflare-as-secondary">Access Control Lists (ACLs)</a> to prevent zone transfers from being blocked.</p>
<p>We strongly recommend configuring <a href="https://datatracker.ietf.org/doc/html/rfc1996">DNS NOTIFY</a> at your primary DNS provider to ensure your secondary zone on Cloudflare is updated with the most recent changes as quickly as possible. In order to do so, set up <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/#notify-ips">Cloudflare NOTIFY IPs</a> at your primary DNS provider.</p>
<p>You will also need the following information from your Primary DNS provider:</p>
<ul>
<li><strong>Primary IP address</strong>: The IP address that Cloudflare sends zone transfer requests to (via AXFR or IXFR).</li>
<li><strong>Zone transfer type</strong>: Will zone transfers be full (AXFR) or incremental (IXFR)?</li>
<li><strong>TSIG name</strong> (optional): A descriptive name of the TSIG following domain name syntax (<a href="https://datatracker.ietf.org/doc/html/rfc8945#section-4.2">RFC 8945 section 4.2</a>).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8030.md")
</aside>
<ul>
<li><strong>TSIG secret</strong> (optional): The secret string used to authenticate zone transfers.</li>
<li><strong>TSIG algorithm</strong> (optional): The algorithm used to authenticate zone transfers.</li>
</ul>
<h3 id="at-cloudflare">At Cloudflare</h3>
<p>Make sure your account team has enabled your zone for Secondary DNS.</p>
<p>Get the following values from your Cloudflare account:</p>
<ul>
<li><a href="/fundamentals/account/find-account-and-zone-ids/">Account ID</a></li>
<li><a href="/fundamentals/account/find-account-and-zone-ids/">Zone ID</a></li>
<li><a href="/dns/zone-setups/full-setup/setup/#31-get-nameserver-names">Nameserver names</a>, which should have <strong>secondary</strong> in the name.</li>
</ul>
<hr />
<h2 id="1-create-tsig-optional"><ol>
<li>Create TSIG (optional)</li>
</ol></h2>
<p>A Transaction Signature (TSIG) authenticates communication between a primary and secondary DNS server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8029.md")
</aside>
<p>While optional, this step is highly recommended.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8034.md")
</div></div>
<h2 id="2-create-peer-server"><ol start="2">
<li>Create Peer Server</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8037.md")
</div></div>
<h2 id="3-create-the-secondary-zone"><ol start="3">
<li>Create the Secondary Zone</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8040.md")
</div></div>
<h2 id="4-update-registrar"><ol start="4">
<li>Update registrar</li>
</ol></h2>
<p>At your registrar, add the secondary nameservers <a href="/dns/zone-setups/full-setup/setup/#31-get-nameserver-names">specified in the Cloudflare dashboard</a>. Do not remove your primary DNS provider's nameservers.</p>
<p>When you have added the Cloudflare nameservers, go into your new secondary zone and select <strong>Done, check nameservers</strong>.</p>
<h2 id="5-create-notifications-optional"><ol start="5">
<li>Create notifications (optional)</li>
</ol></h2>
<p>To increase the reliability of your incoming zone transfers, <a href="/notifications/get-started/#create-a-notification">set up notifications</a> to be notified when your primaries are failing, when records are updated, <a href="/notifications/notification-available/#dns">and more</a>.</p>
<h2 id="6-proxy-traffic-through-cloudflare-optional"><ol start="6">
<li>Proxy traffic through Cloudflare (optional)</li>
</ol></h2>
<p>Normal incoming zone transfers only provide DNS resolution. If you also want your traffic to benefit from Cloudflare's performance and security features, you need to <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">set up Secondary DNS Override</a>.</p>
