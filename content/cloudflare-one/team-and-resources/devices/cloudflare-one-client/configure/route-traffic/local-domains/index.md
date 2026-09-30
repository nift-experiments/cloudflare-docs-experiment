---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/
  description: Local Domain Fallback in Zero Trust.
  full_title: Local Domain Fallback · Cloudflare One docs
  head_html: <title>Local Domain Fallback · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Local Domain Fallback in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/index.md"><meta property="og:title" content="Local Domain Fallback · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Local Domain Fallback in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#page","headline":"Local Domain Fallback \u00b7 Cloudflare One docs","description":"Local Domain Fallback in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/
  schema: 1
---
<p>By default, Cloudflare Zero Trust excludes common top-level domains, used for local resolution, from being sent to Gateway for processing. These top-level domains are resolved by the local DNS resolver configured for the device on its primary interface.</p>
<p>You can add additional domains to the Local Domain Fallback list and specify a DNS server to use in place of the Gateway resolver. The Cloudflare One Client (formerly WARP) proxies these requests directly to the configured fallback servers.</p>
<h2 id="limitations">Limitations</h2>
<p>Local Domain Fallback only applies to devices running the Cloudflare One Client.</p>
<p>Because DNS requests subject to Local Domain Fallback bypass the Gateway resolver, they are not subject to Gateway DNS policies or DNS logging. If you want to route DNS queries to custom resolvers and apply Gateway filtering, use <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a>. If both Local Domain Fallback and resolver policies are configured for the same device, Cloudflare will apply client-side Local Domain Fallback rules first.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="local-domain-fallback-or-gateway-resolver-policies">Local Domain Fallback or Gateway Resolver policies?</h3>
@markup("md", "content/.markup/bodies/6291.md")
</aside>
<h3 id="aws">AWS</h3>
<p>Avoid configuring your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> or <a href="/cloudflare-one/traffic-policies/resolver-policies/">Resolver Policy</a> to direct all <code>*.amazonaws.com</code> DNS resolution via AWS Route 53 Resolver.</p>
<p>Some AWS endpoints (such as <code>ssm.us-east-1.amazonaws.com</code>) are public AWS endpoints that are not resolvable via internal VPC resolution. This can break AWS Console features for users on the Cloudflare One Client.</p>
<p>Only route specific Route 53 zones, or VPC Endpoints (such as <code>vpce.amazonaws.com</code>), through the internal VPC resolver.</p>
<h2 id="manage-local-domains">Manage local domains</h2>
<h3 id="view-domains">View domains</h3>
<p>To view the domains subject to Local Domain Fallback:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Locate the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> you would like to view or modify and select <strong>Configure</strong>.</li>
<li>Scroll down to <strong>Local Domain Fallback</strong> and select <strong>Manage</strong>.</li>
</ol>
<p>On this page, you will see a list of domains excluded from Gateway. You can <a href="#add-a-domain">add</a> or <a href="#delete-a-domain">remove</a> domains from the list at any time.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6289.md")
</aside>
<p>To view the fallback domains applied to a device, you can:</p>
<ul>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; find the target device and the <strong>Last active device profile</strong> &gt; follow the <a href="#view-domains">steps above</a>.</li>
<li>(Desktop only) Run <code>warp-cli settings</code> in the terminal of the target device and review the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/#fallback-domains">fallback domains</a> section of the output.</li>
<li>(Desktop only) Collect <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/">client diagnostic logs</a> for the device and review the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/#fallback-domains">fallback domain</a> section in <code>warp_settings.txt</code>.</li>
</ul>
<h3 id="add-a-domain">Add a domain</h3>
<p>To add a domain to the Local Domain Fallback list:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6294.md")
</div></div>
<p>The Cloudflare One Client tries all servers and always uses the fastest response, even if that response is <code>no records found</code>. We recommend specifying at least one DNS server for each domain. If a value is not specified, the Cloudflare One Client will try to identify the DNS server (or servers) used on the device before it started, and use that server for each domain in the Local Domain Fallback list.</p>
<h3 id="route-traffic-to-fallback-server">Route traffic to fallback server</h3>
<p>The Cloudflare One Client routes DNS traffic to your <a href="#add-a-domain">Local Domain Fallback server</a> according to your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel configuration</a>. To ensure that queries can reach your private DNS server:</p>
<ul>
<li>
<p>If your DNS server is only reachable inside of the WARP tunnel (for example, via <code>cloudflared</code> or Cloudflare WAN):</p>
<ol>
<li>
<p>Go to <strong>Networking</strong> &gt; <strong>Routes</strong> and verify that the DNS server is connected to Cloudflare. To connect a DNS server, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Private networks</a>.</p>
</li>
<li>
<p>In your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel configuration</a>, verify that the DNS server IP routes through the WARP tunnel.</p>
</li>
</ol>
</li>
<li>
<p>If your DNS server is only reachable outside of the WARP tunnel (for example, via a third-party VPN), verify that the DNS server IP is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">excluded from the WARP tunnel</a>.</p>
</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#how-the-warp-client-handles-dns-requests">How the Cloudflare One Client handles DNS requests</a>.</p>
<h3 id="delete-a-domain">Delete a domain</h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</p>
</li>
<li>
<p>Locate the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> you would like to view or modify and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Scroll down to <strong>Local Domain Fallback</strong> and select <strong>Manage</strong>.</p>
</li>
<li>
<p>Find the domain in the list and select <strong>Delete</strong>.</p>
</li>
</ol>
<p>The domain will no longer be excluded from Gateway DNS policies, effective immediately.</p>
<h2 id="reverse-dns-lookups-for-internal-ips">Reverse DNS lookups for internal IPs</h2>
<p>By default, Warp sends <a href="https://www.cloudflare.com/learning/dns/glossary/reverse-dns/">reverse DNS queries</a> to public DNS servers. To lookup the domain name associated with an internal IP address, <a href="#add-a-domain">add a local domain fallback entry</a> for <code>in-addr.arpa</code> (IPv4) and/or <code>ip6.arpa</code> (IPv6) that points to your internal DNS server IP. <code>in-addr.arpa</code> and <code>ip6.arpa</code> are top-level domains <a href="https://www.iana.org/domains/arpa">reserved</a> for reverse DNS queries. By adding a local domain fallback entry for these domains, all reverse DNS queries (such as <code>dig -x 1.1.1.1</code>) will now resolve through your local DNS server.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> - Control which traffic goes through the Cloudflare One Client by including or excluding specific IPs or domains.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> - Learn which IPs, domains, and ports to allow so users can deploy and connect the Cloudflare One Client successfully behind a firewall.</li>
</ul>
