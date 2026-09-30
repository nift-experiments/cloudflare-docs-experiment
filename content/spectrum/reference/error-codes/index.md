---
cp9:
  canonical: https://developers.cloudflare.com/spectrum/reference/error-codes/
  description: Error codes returned by the Cloudflare Spectrum API.
  full_title: Error codes · Cloudflare Spectrum docs
  head_html: <title>Error codes · Cloudflare Spectrum docs</title><meta name="generator" content="Nift"><meta name="description" content="Error codes returned by the Cloudflare Spectrum API."><link rel="canonical" href="https://developers.cloudflare.com/spectrum/reference/error-codes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/spectrum/reference/error-codes/index.md"><meta property="og:title" content="Error codes · Cloudflare Spectrum docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Error codes returned by the Cloudflare Spectrum API."><meta property="og:url" content="https://developers.cloudflare.com/spectrum/reference/error-codes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Spectrum"><meta name="algolia_product_filter" content="Spectrum"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Spectrum"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/spectrum/reference/error-codes/#page","headline":"Error codes \u00b7 Cloudflare Spectrum docs","description":"Error codes returned by the Cloudflare Spectrum API.","url":"https://developers.cloudflare.com/spectrum/reference/error-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /spectrum/reference/error-codes/
  schema: 1
---
<p>This page documents error codes returned by the <a href="/api/resources/spectrum/subresources/apps/">Spectrum API</a>, along with recommended fixes to help with troubleshooting.</p>
<h2 id="how-errors-are-returned">How errors are returned</h2>
<p>Spectrum API errors follow the standard Cloudflare v4 error envelope. The response body includes an <code>errors</code> array with <code>code</code> and <code>message</code> fields:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 11044,&#10;      &quot;message&quot;: &quot;No matching routes in the specified virtual network.&quot;&#10;    }&#10;  ],&#10;  &quot;messages&quot;: [],&#10;  &quot;success&quot;: false,&#10;  &quot;result&quot;: null&#10;}&#10;</code></pre>
<h2 id="general-errors-10xxx">General errors (10xxx)</h2>
<h3 id="10002-unexpected-internal-server-error">10002 — Unexpected internal server error</h3>
<p>An unexpected error occurred during request processing. The response does not include diagnostic details. If you contact Cloudflare support, provide the <a href="/fundamentals/reference/cloudflare-ray-id/">Ray ID</a> from the response so the original error can be located.</p>
<p>HTTP <code>503</code> indicates a dependent service (such as DNS or IP address management) is temporarily unavailable. HTTP <code>500</code> indicates any other internal error.</p>
<h3 id="10012-unknown-field-in-request-json">10012 — Unknown field in request JSON</h3>
<p>The request body contains a field the API does not recognize. This error is only returned for applications on Pay-as-you-go accounts. Enterprise applications silently ignore unknown fields.</p>
<p>Pay-as-you-go accounts are limited to <code>protocol</code>, <code>dns</code>, and <code>origin_direct</code> when creating or updating a Spectrum application. A common cause is an account without a Spectrum entitlement sending a full Spectrum configuration — any field outside those three will be rejected.</p>
<p><strong>Resolution:</strong> To use the full Spectrum configuration API, contact your account team to enable Spectrum as a paid add-on. Otherwise, remove any fields other than <code>protocol</code>, <code>dns</code>, and <code>origin_direct</code> from the request.</p>
<h2 id="application-configuration-errors-11xxx">Application configuration errors (11xxx)</h2>
<p>These errors are returned as HTTP <code>400</code>, unless noted otherwise.</p>
<h3 id="11000-invalid-origin-configuration">11000 — Invalid origin configuration</h3>
<p>The request must provide exactly one of <code>origin_direct</code> or <code>origin_dns</code>. Providing both or neither will trigger this error.</p>
<h3 id="11001-invalid-origin-dns-configuration">11001 — Invalid origin DNS configuration</h3>
<p>The <code>origin_dns</code> configuration failed validation. Common causes:</p>
<ul>
<li>The <code>origin_dns.name</code> is not a valid domain name.</li>
<li>A non-SRV <code>origin_dns.type</code> was provided without an <code>origin_port</code>.</li>
<li>The <code>origin_dns.ttl</code> is outside the allowed range.</li>
</ul>
<h3 id="11002-invalid-origin-address">11002 — Invalid origin address</h3>
<p>One or more of the origin addresses provided are invalid.</p>
<p>Common causes:</p>
<ul>
<li><strong>IPv6 origin without brackets:</strong> IPv6 addresses must be wrapped in brackets in <code>origin_direct</code>, for example <code>tcp://[2001:db8::1]:443</code>. Without brackets, the colons in the address make parsing ambiguous.</li>
<li><strong>Origin IP fails access control validation:</strong> The origin IP may fail an internal access control check. Verify the IP is valid and belongs to an allowed range.</li>
</ul>
<h3 id="11004-invalid-dns-configuration">11004 — Invalid DNS configuration</h3>
<p>The DNS type must match the edge IP allocation mode. Dynamic edge IPs require <code>type: &quot;CNAME&quot;</code>. Static (BYOIP) edge IPs require <code>type: &quot;ADDRESS&quot;</code>. This error is also returned if you attempt to change the DNS type when updating an existing application.</p>
<h3 id="11014-ftp-not-enabled">11014 — FTP not enabled</h3>
<p>FTP traffic type is not enabled for the account. Returned as HTTP <code>403</code>.</p>
<p><strong>Resolution:</strong> Contact your account team to enable FTP support.</p>
<h3 id="11018-edge-ips-not-enabled">11018 — <code>edge_ips</code> not enabled</h3>
<p>The <code>edge_ips</code> feature (BYOIP) is not enabled for the account. Returned as HTTP <code>403</code>.</p>
<p><strong>Resolution:</strong> Contact your account team to enable <a href="/spectrum/about/byoip/">BYOIP</a> for the account.</p>
<h3 id="11019-edge-ips-not-authorized">11019 — <code>edge_ips</code> not authorized</h3>
<p>The authenticated account is not authorized to use the provided <code>edge_ips</code>.</p>
<p>Common causes:</p>
<ul>
<li><strong>API token lacks IP prefix permissions:</strong> API tokens scoped to Spectrum may not carry the IP prefix permissions required for BYOIP validation. Use a Global API Key, or add the <strong>Account</strong> &gt; <strong>IP Prefixes</strong> permission to the API token.</li>
<li><strong>BYOIP prefix not allocated to account:</strong> Verify the BYOIP prefix is allocated to the requesting account before assigning it.</li>
</ul>
<h3 id="11026-argo-smart-routing-not-enabled">11026 — Argo Smart Routing not enabled</h3>
<p>The request set <code>argo_smart_routing</code> to <code>true</code>, but Argo Smart Routing is not enabled for the account. Returned as HTTP <code>403</code>.</p>
<p><strong>Resolution:</strong> Contact your account team to enable Argo Smart Routing for the account.</p>
<h3 id="11033-edge-ips-in-use">11033 — <code>edge_ips</code> in use</h3>
<p>One or more of the provided <code>edge_ips</code> is already in use by another zone.</p>
<p>Common cause: The requested edge IP may be held by a legacy Spectrum application on a deleted zone. Contact Cloudflare support to clean up the orphaned application.</p>
<h3 id="11034-cannot-create-more-applications-for-protocol">11034 — Cannot create more applications for protocol</h3>
<p>Pay-as-you-go accounts are limited to one application per protocol. If you need multiple applications on the same protocol, contact your account team to enable Spectrum as a paid add-on.</p>
<h3 id="11050-invalid-cross-zone-origin-dns-configuration">11050 — Invalid cross-zone origin DNS configuration</h3>
<p>The DNS record or Load Balancer used as an origin lives on a different zone or a non-permitted zone.</p>
<p><strong>Resolution:</strong> Move the origin DNS record or Load Balancer to the same zone, or use <code>origin_direct</code> with an IP address instead.</p>
<h2 id="virtual-network-origin-errors">Virtual network origin errors</h2>
<p>The following codes are returned by <code>POST /zones/:zone/spectrum/apps</code> and <code>PATCH /zones/:zone/spectrum/apps/:id</code> when validating an application that uses a <a href="/spectrum/reference/configuration-options/#virtual-network-origin">virtual network origin</a>.</p>
<h3 id="11041-virtual-network-requires-origin-direct">11041 — Virtual network requires origin direct</h3>
<p><code>virtual_network_id</code> was set on a request that uses <code>origin_dns</code>. Virtual network origins are only supported with IP-based origins.</p>
<p><strong>Resolution:</strong> Replace <code>origin_dns</code> with <code>origin_direct</code> and provide the private IP and single port that the virtual network routes to.</p>
<h3 id="11042-virtual-network-requires-single-origin">11042 — Virtual network requires single origin</h3>
<p><code>origin_direct</code> contained more than one address. Virtual network origins must resolve to a single private IP and port.</p>
<p><strong>Resolution:</strong> Reduce <code>origin_direct</code> to a single entry of the form <code>tcp://&lt;IP&gt;:&lt;PORT&gt;</code> or <code>udp://&lt;IP&gt;:&lt;PORT&gt;</code>.</p>
<h3 id="11043-virtual-network-no-port-range">11043 — Virtual network no port range</h3>
<p>The request included a port range, either in <code>origin_port</code> or in the <code>origin_direct</code> address. Virtual network origins do not support port ranges.</p>
<p><strong>Resolution:</strong> Use a single port instead of a range. If you need to expose multiple ports, create a separate Spectrum application per port.</p>
<h3 id="11044-virtual-network-route-not-found">11044 — Virtual network route not found</h3>
<p>The combination of IP and <code>virtual_network_id</code> does not match any route in the specified virtual network. This covers two cases: the virtual network does not exist, or the IP is not routable within the virtual network you specified.</p>
<p><strong>Resolution:</strong></p>
<ul>
<li>Confirm <code>virtual_network_id</code> matches a virtual network on your account. You can list virtual networks with the <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/">List virtual networks</a> endpoint.</li>
<li>Confirm the origin IP is within a route attached to that virtual network. You can list routes with the <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/">List network routes</a> endpoint.</li>
<li>If no matching route exists, add one by following <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">Connect an IP/CIDR</a>.</li>
</ul>
<h3 id="11045-virtual-network-invalid-uuid">11045 — Virtual network invalid UUID</h3>
<p><code>virtual_network_id</code> is not a valid UUID.</p>
<p><strong>Resolution:</strong> Provide a UUID. Virtual network IDs are returned by the <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/">List virtual networks</a> endpoint in the <code>id</code> field of each entry.</p>
<h2 id="addressing-errors-12xxx">Addressing errors (12xxx)</h2>
<h3 id="12005-ipv4-quota-limit">12005 — IPv4 quota limit</h3>
<p>The zone has allocated all available IPv4 addresses in its quota.</p>
<p><strong>Resolution:</strong> Consolidate applications onto fewer IPs (multiple apps can share a hostname on different ports), purchase additional Cloudflare-managed IPs, or onboard <a href="/spectrum/about/byoip/">BYOIP</a>.</p>
<h2 id="protocol-errors-13xxx">Protocol errors (13xxx)</h2>
<h3 id="13002-protocol-not-available">13002 — Protocol not available</h3>
<p>The requested protocol is not available for the zone. The error message includes specific edge ports that are not allowed for the requested protocol.</p>
<h2 id="hostname-errors-16xxx">Hostname errors (16xxx)</h2>
<h3 id="16001-zone-mismatch">16001 — Zone mismatch</h3>
<p>A hostname with the same DNS name already exists but belongs to a different zone. This can occur during application creation or update when the hostname lookup matches a record owned by another zone.</p>
<p><strong>Resolution:</strong></p>
<ul>
<li>Verify you are using the correct zone ID in the API request URL.</li>
<li>Use a different DNS name for the application.</li>
<li>If the DNS name was previously used on another zone you control, delete the application on that zone first.</li>
<li>Contact Cloudflare support if none of these apply — the hostname may need to be cleaned up internally.</li>
</ul>
