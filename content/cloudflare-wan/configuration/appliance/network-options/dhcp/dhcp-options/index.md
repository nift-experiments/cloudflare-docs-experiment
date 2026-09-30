---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/
  description: Configure custom DHCP options on the Cloudflare One Appliance DHCP server, including options for PXE, PXELINUX, and iPXE boot.
  full_title: DHCP server options · Cloudflare WAN docs
  head_html: <title>DHCP server options · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure custom DHCP options on the Cloudflare One Appliance DHCP server, including options for PXE, PXELINUX, and iPXE boot."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/index.md"><meta property="og:title" content="DHCP server options · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure custom DHCP options on the Cloudflare One Appliance DHCP server, including options for PXE, PXELINUX, and iPXE boot."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#page","headline":"DHCP server options \u00b7 Cloudflare WAN docs","description":"Configure custom DHCP options on the Cloudflare One Appliance DHCP server, including options for PXE, PXELINUX, and iPXE boot.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/
  schema: 1
---
<p>When the Cloudflare One Appliance is configured as the DHCP server for a LAN, you can attach <strong>custom DHCP options</strong> to the leases it issues. This is commonly used for:</p>
<ul>
<li><strong>Network boot</strong> of workstations or kiosks with PXE, PXELINUX, or iPXE (options 43, 60, 66, 67, 175, 209, and 210).</li>
<li><strong>VoIP phone provisioning</strong> (option 66 — TFTP server).</li>
<li><strong>Vendor-specific client configuration</strong> (option 43 with vendor sub-options).</li>
</ul>
<p>DHCP options can only be configured when the appliance is acting as the DHCP server. They have no effect when the appliance is in <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/">DHCP relay</a> mode.</p>
<h2 id="configure-dhcp-options">Configure DHCP options</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7033.md")
</div></div>
<h2 id="option-format">Option format</h2>
<p>Each option is defined by three fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>code</code></td>
<td>The DHCP option code (1–254).</td>
<td><code>67</code></td>
</tr>
<tr>
<td><code>type</code></td>
<td>The value encoding: <code>text</code>, <code>hex</code>, <code>ip</code>, <code>byte</code>, <code>short</code>, <code>integer</code>.</td>
<td><code>text</code></td>
</tr>
<tr>
<td><code>value</code></td>
<td>The option value, encoded per <code>type</code>.</td>
<td><code>boot/x64/pxelinux.0</code></td>
</tr>
</tbody>
</table>
<h3 id="value-type-encoding">Value type encoding</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Format</th>
<th>Example value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>text</code></td>
<td>A UTF-8 string (max 255 bytes).</td>
<td><code>boot/x64/pxelinux.0</code></td>
</tr>
<tr>
<td><code>hex</code></td>
<td>A colon-separated sequence of hex bytes, used for sub-options (max 255 bytes).</td>
<td><code>01:04:aa:bb:cc</code></td>
</tr>
<tr>
<td><code>ip</code></td>
<td>A dotted-quad IPv4 address.</td>
<td><code>10.20.30.40</code></td>
</tr>
<tr>
<td><code>byte</code></td>
<td>An unsigned 8-bit integer (0–255).</td>
<td><code>1</code></td>
</tr>
<tr>
<td><code>short</code></td>
<td>An unsigned 16-bit integer (0–65535).</td>
<td><code>512</code></td>
</tr>
<tr>
<td><code>integer</code></td>
<td>An unsigned 32-bit integer (0–4294967295).</td>
<td><code>0</code></td>
</tr>
</tbody>
</table>
<h3 id="restricted-option-codes">Restricted option codes</h3>
<ul>
<li>Options <code>0</code> and <code>255</code> are reserved by <a href="https://www.rfc-editor.org/rfc/rfc2132">RFC 2132</a> and cannot be configured.</li>
<li>Options <code>3</code>, <code>6</code>, and <code>51</code> are managed by the Cloudflare One Appliance and cannot be configured, since they conflict with connector-managed configuration (default gateway, DNS servers, and lease time).</li>
<li>Each option code can only be used once per LAN. Duplicate option codes are rejected.</li>
</ul>
<h2 id="common-network-boot-options">Common network boot options</h2>
<p>The most frequently used network boot options are:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>43</td>
<td><code>hex</code></td>
<td>Vendor-specific information. The vendor defines the sub-option layout.</td>
</tr>
<tr>
<td>60</td>
<td><code>text</code></td>
<td>Vendor class identifier, typically <code>PXEClient</code>.</td>
</tr>
<tr>
<td>66</td>
<td><code>text</code></td>
<td>TFTP server name.</td>
</tr>
<tr>
<td>67</td>
<td><code>text</code></td>
<td>Boot file name, for example <code>ipxe.pxe</code> or <code>undionly.kpxe</code>. iPXE also accepts a URI, such as an HTTP URL for an iPXE script.</td>
</tr>
<tr>
<td>175</td>
<td><code>hex</code></td>
<td>Client-specific encapsulated options used by Etherboot and iPXE. IANA lists this option as tentatively assigned and does not define its payload.</td>
</tr>
<tr>
<td>209</td>
<td><code>text</code></td>
<td>PXELINUX configuration filename or path, loaded through TFTP.</td>
</tr>
<tr>
<td>210</td>
<td><code>text</code></td>
<td>PXELINUX TFTP path prefix, prepended to option 209.</td>
</tr>
</tbody>
</table>
<p>For a complete list of standard DHCP option codes, refer to the <a href="https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml">IANA BOOTP/DHCP parameters registry</a>.</p>
<h2 id="validation-and-apply-behavior">Validation and apply behavior</h2>
<p>Before applying a new DHCP options configuration, the appliance:</p>
<ol>
<li>Stages the change to a temporary configuration file.</li>
<li>Validates the syntax with the underlying DHCP server.</li>
<li><strong>On success</strong>, atomically swaps the staged configuration into place and reloads the DHCP server with no service interruption.</li>
<li><strong>On failure</strong>, discards the change and returns the underlying validation error to the caller — shown as a field error in the dashboard, or in the API response for API and Terraform callers. The live DHCP service is never restarted with an unverified configuration.</li>
</ol>
<p>This means a malformed option will be rejected at apply-time rather than disrupting DHCP service for clients on the LAN.</p>
