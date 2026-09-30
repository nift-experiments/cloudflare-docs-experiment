---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/policy-design/
  description: Design Zero Trust access policies.
  full_title: Policy design · Cloudflare Learning Paths
  head_html: <title>Policy design · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Design Zero Trust access policies."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/policy-design/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/policy-design/index.md"><meta property="og:title" content="Policy design · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Design Zero Trust access policies."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/policy-design/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/policy-design/#page","headline":"Policy design \u00b7 Cloudflare Learning Paths","description":"Design Zero Trust access policies.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/policy-design/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/build-policies/policy-design/
  schema: 1
---
<p>Most policy building for private network access happens within the Gateway DNS and Gateway Network policy builders. For the most part, customers use a mixture of DNS resolution, SNI hostname values, and IP address groupings as the baseline for defining policies that pertain to specific applications.</p>
<h2 id="considerations">Considerations</h2>
<p>Before building your policies, it is helpful to ask yourself a few questions:</p>
<ul>
<li>Should all users and services be able to reach all connected subnets? Are there explicit exceptions?</li>
<li>Do all applications live within a primary network range, and are they defined by static or dynamic hosts and IP addresses?</li>
<li>Are there DevOps workflows that rely on completely ephemeral IPs or subdomains?</li>
<li>Do you have sources of truth for identity and device posture that will be used in policies?</li>
<li>Do you plan to immediately implement a default-deny model? In other words, will you block all users except for those who match an explicit Allow policy?</li>
</ul>
<h2 id="prepare-to-build-policies">Prepare to build policies</h2>
<p>We recommend the following approach when planning your Zero Trust Network Access policies.</p>
<h3 id="1-determine-your-sources-of-truth"><ol>
<li>Determine your sources of truth</li>
</ol></h3>
<h4 id="identity">Identity</h4>
<p>Determine which identity provider you will use as the source of truth for user email, user groups, and other <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based attributes</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9969.md")
</aside>
<p>If you plan to grant access to services based on group membership, <a href="/cloudflare-one/team-and-resources/users/users/">view the user registry</a> and verify that the target users have that group value in their User Registry.</p>
<h4 id="device-posture">Device posture</h4>
<p>Most customers will also build policies that are contingent on the use of a corporate device. For example, all users on corporate devices can access <code>*.jira.internal.com</code>, but users on personal devices can only access <code>dev.internal.jira.com</code>. In order for this to be effective, we recommend defining a source of truth for your corporate devices. This is sometimes the presence of a specific <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/">issued certificate</a>, the presence of a <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/">process with a matched hash</a>, or an API integration with a supported <a href="/cloudflare-one/integrations/service-providers/">thirty-party endpoint security provider</a> like Crowdstrike or SentinelOne.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9968.md")
</aside>
<h3 id="2-define-your-networks"><ol start="2">
<li>Define your networks</li>
</ol></h3>
<p>Almost all businesses have a series of interconnected networks, either physical or virtual. Prepare a list of all relevant networks, subnets, or segments within your network that users currently access, either locally or when using the VPN. For example,</p>
<table>
<thead>
<tr>
<th>Network name</th>
<th>Location</th>
<th>IP range</th>
<th>Accessible by VPN?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Corporate DC</td>
<td>AWS US East - VA, USA</td>
<td><code>10.0.0.0/8</code></td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h3 id="3-define-your-applications"><ol start="3">
<li>Define your applications</li>
</ol></h3>
<p>Next, prepare a list of all relevant internal applications on your networks that will have distinct policy requirements (for example, different user identity or device posture requirements). Each application should be defined by an IP list, a hostname/domain list, or sometimes both.</p>
<table>
<thead>
<tr>
<th>Application name</th>
<th>Local IPs</th>
<th>Hostnames</th>
<th>Accessible via IP?</th>
<th>Static or dynamic IP?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Company Wiki</td>
<td><code>10.128.0.10</code></td>
<td><code>wiki.internal.com</code></td>
<td>Yes</td>
<td>Static</td>
</tr>
</tbody>
</table>
<p>For example, you may have an application at <code>a.internal.com</code> which points to a load balancer with a static IP address, balancing a series of dynamic hosts serving the application on <code>a.internal.com</code>. Because the IPs of the application hosts are dynamic, the best practice would be to build two policies: a network policy for the load balancer IP, and a DNS policy for the application hostnames.</p>
<p>On the other hand, if the IPs behind the load balancer are static or only semi-dynamic, it may make sense to directly use the application IPs in your network policy. You can build a workflow to update the application IP list via a Cloudflare API call whenever host changes are made in your infrastructure provider.</p>
<h3 id="4-list-existing-policies"><ol start="4">
<li>List existing policies</li>
</ol></h3>
<p>Gather any existing security policies or block lists that you wish to migrate from your VPN provider to Zero Trust.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="descaler-program">Descaler program</h3>
@markup("md", "content/.markup/bodies/9967.md")
</aside>
