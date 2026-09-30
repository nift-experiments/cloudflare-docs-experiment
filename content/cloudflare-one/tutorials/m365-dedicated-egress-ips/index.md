---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/m365-dedicated-egress-ips/
  description: This tutorial covers how to secure access to your Microsoft 365 applications with Cloudflare Gateway dedicated egress IPs.
  full_title: Protect access to Microsoft 365 with dedicated egress IPs · Cloudflare One docs
  head_html: <title>Protect access to Microsoft 365 with dedicated egress IPs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial covers how to secure access to your Microsoft 365 applications with Cloudflare Gateway dedicated egress IPs."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/m365-dedicated-egress-ips/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/m365-dedicated-egress-ips/index.md"><meta property="og:title" content="Protect access to Microsoft 365 with dedicated egress IPs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial covers how to secure access to your Microsoft 365 applications with Cloudflare Gateway dedicated egress IPs."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/m365-dedicated-egress-ips/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft,IPv4,IPv6"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/m365-dedicated-egress-ips/#page","headline":"Protect access to Microsoft 365 with dedicated egress IPs \u00b7 Cloudflare One docs","description":"This tutorial covers how to secure access to your Microsoft 365 applications with Cloudflare Gateway dedicated egress IPs.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/m365-dedicated-egress-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft","IPv4","IPv6"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/m365-dedicated-egress-ips/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4297.md")
</aside>
<p>This tutorial covers how to secure access to your Microsoft 365 applications with Cloudflare Gateway dedicated egress IPs.</p>
<p>You can map a named location in Microsoft Entra ID to a location associated with your dedicated egress IPs. Traffic will egress from Cloudflare with these IP addresses. If users attempt to access your Microsoft applications without these IPs, Entra ID will block access.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you have:</p>
<ul>
<li>In Cloudflare, a Zero Trust Enterprise plan with <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a></li>
<li>In Microsoft 365, an organization managed with <a href="https://learn.microsoft.com/en-us/entra/identity/">Microsoft Entra ID</a></li>
</ul>
<h2 id="create-an-egress-policy-in-cloudflare-gateway">Create an egress policy in Cloudflare Gateway</h2>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Traffic policies</strong> &gt; <strong>Egress policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Name your policy, then add conditions to check users are configured in Microsoft Entra ID. For example, you can check for <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity conditions</a>:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td>in</td>
<td><code>Sales and Marketing</code>, <code>Retail</code>, <code>U.S. Sales</code></td>
</tr>
</tbody>
</table>
<p>Additionally, you can check for <a href="/cloudflare-one/reusable-components/posture-checks/">device posture conditions</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Passed Device Posture Check</td>
<td>is</td>
<td><code>CrowdStrike Overall ZTA score (Crowdstrike s2s)</code></td>
<td>And</td>
</tr>
<tr>
<td>Passed Device Posture Check</td>
<td>is</td>
<td><code>AppCheckMac - Required Software (Application)</code></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Enable <strong>Use dedicated Cloudflare egress IPs</strong>. Select your desired IPv4 and IPv6 addresses. For example:</li>
</ol>
<table>
<thead>
<tr>
<th>Primary IPv4 address</th>
<th>IPv6 address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>203.0.113.0</code></td>
<td><code>2001:db8::/32</code></td>
</tr>
</tbody>
</table>
<h2 id="create-a-named-ip-range-location-in-microsoft-entra-id">Create a named IP range location in Microsoft Entra ID</h2>
<ol>
<li>Log in to the <a href="https://aka.ms/azureportal">Microsoft Azure portal</a>.</li>
<li>In the sidebar, select <strong>Microsoft Entra ID</strong>.</li>
<li>Go to <strong>Security</strong> &gt; <strong>Named locations</strong>.</li>
<li>Select <strong>IP ranges location</strong>.</li>
<li>Name your location, then add the IP addresses used in your Cloudflare dedicated egress IP policy.</li>
<li>Select <strong>Upload</strong>.</li>
</ol>
<p>This named location corresponds with the locations of your dedicated egress IPs.</p>
<h2 id="create-a-conditional-access-policy-in-microsoft-entra-id">Create a conditional access policy in Microsoft Entra ID</h2>
<ol>
<li>In <strong>Protect</strong>, go to <strong>Conditional Access</strong>.</li>
<li>Select <strong>Create new policy</strong>.</li>
<li>Configure which Entra ID users you want to limit access for, and which traffic, applications, or actions you want to protect.</li>
<li>In <strong>Conditions</strong>, select <strong>Locations</strong>. Enable <strong>Configure</strong>.</li>
<li>In <strong>Include</strong>, select <em>Any location</em>. In <strong>Exclude</strong>, select the named location you created.</li>
<li>In <strong>Access controls</strong>, go to <strong>Grant</strong>. Enable <em>Block access</em>.</li>
</ol>
<p>Your policy will block access for your selected users from any location except those using your dedicated egress IPs.</p>
<h2 id="test-your-policies">Test your policies</h2>
<ol>
<li>Using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, sign in to your Zero Trust organization with a user's account.</li>
<li>Go to any Microsoft 365 app within your organization. Entra ID should allow access.</li>
<li>Disconnect the Cloudflare One Client from your Zero Trust organization. Entra ID should block access to any Microsoft 365 applications.</li>
</ol>
