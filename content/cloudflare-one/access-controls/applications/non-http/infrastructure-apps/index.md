---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/
  description: Add an infrastructure application in Access.
  full_title: Add an infrastructure application · Cloudflare One docs
  head_html: <title>Add an infrastructure application · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Add an infrastructure application in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/index.md"><meta property="og:title" content="Add an infrastructure application · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add an infrastructure application in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SSH,Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#page","headline":"Add an infrastructure application \u00b7 Cloudflare One docs","description":"Add an infrastructure application in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SSH","Authentication"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/non-http/infrastructure-apps/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/4802.md")
</div></details>
<p>Access for Infrastructure gives you granular control over how users access individual servers, clusters, or databases. You can configure how users authenticate to the resource and control the ports, protocols, and usernames they can use.</p>
<p>You can also organize targets with tags and define applications that match targets by hostname, tag, or both. Access logs and command logs help you audit access and support compliance workflows.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4801.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Connect your infrastructure</a> to Cloudflare using <code>cloudflared</code> or Cloudflare Mesh.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client</a> on user devices in Traffic and DNS mode.</li>
</ul>
<h2 id="1-add-a-target"><ol>
<li>Add a target</li>
</ol></h2>
<p>A target represents a single resource in your infrastructure (such as a server, Kubernetes cluster, database, or container) that users will connect to through Cloudflare.</p>
<p>Targets are protocol-agnostic, meaning that you do not need to define a new target for each protocol that runs on the server. To create a new target: </p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4808.md")
</div></div>
<p>Next, create an Access application to secure the target.</p>
<h3 id="tag-targets">Tag targets</h3>
<p>You can attach key-value <a href="/resource-tagging/">resource tags</a> to infrastructure targets. Use them to organize targets by environment, team, region, or other metadata.</p>
<p>You can then define infrastructure applications that automatically cover any target with matching values.</p>
<p>You can manage tags inline when you create or edit a target or through the <a href="/resource-tagging/how-to/manage-tags/">Resource Tagging API</a>.</p>
<p>Each tag key can only appear once on a target. For example, a target can have <code>environment:production</code> or <code>environment:staging</code>, but not both.</p>
<h3 id="filter-and-sort-targets-by-tag">Filter and sort targets by tag</h3>
<p>You can filter and sort targets by tag values.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4811.md")
</div></div>
<h2 id="2-add-an-infrastructure-application"><ol start="2">
<li>Add an infrastructure application</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4816.md")
</div></div>
<p>The targets in this application are now secured by your infrastructure policies.</p>
<h2 id="3-recommended-modify-order-of-precedence-in-gateway"><ol start="3">
<li>(Recommended) Modify order of precedence in Gateway</li>
</ol></h2>
<p>By default, Cloudflare will evaluate Access application policies after evaluating all <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>. To evaluate Access applications before or after specific Gateway policies:</p>
<ol>
<li>
In the [Cloudflare dashboard](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall policies**. In **Network**, [create a Network policy](/cloudflare-one/traffic-policies/network-policies/) with the following configuration:
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access Infrastructure Target</td>
<td>is</td>
<td><em>Present</em></td>
<td>Allow</td>
</tr>
</tbody>
</table>
</li>
<li>
	Update the policy's [order of
	precedence](/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence)
	using the dashboard or API.
</li>
</ol>
<p> This Gateway policy will apply to all Access for Infrastructure targets, including RDP and SSH. </p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4795.md")
</aside>
<h2 id="4-optional-require-independent-mfa"><ol start="4">
<li>(Optional) Require independent MFA</li>
</ol></h2>
<p>You can require independent MFA before users connect with SSH. The application configuration selects the supported infrastructure authenticators: PIV key (<code>piv_key</code>), FIDO2 key (<code>ssh_fido2_key</code>), or both.</p>
<p>Application-level settings define the default authenticators and session duration. A policy can define custom settings for specific users or usernames.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Enforce MFA for infrastructure applications</a>.</p>
<h2 id="5-configure-the-server"><ol start="5">
<li>Configure the server</li>
</ol></h2>
<p>Certain protocols require configuring the server to trust connections through Access for Infrastructure. For more information, refer to the protocol-specific tutorial:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#7-configure-ssh-server">SSH</a></li>
</ul>
<p>For SSH, this includes trusting the Cloudflare SSH CA and, if your server restricts certificate principals, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#confirm-the-account-authorizes-the-certificate-principal">authorizing the SSH usernames</a> you configured on the target.</p>
<h2 id="6-connect-as-a-user"><ol start="6">
<li>Connect as a user</li>
</ol></h2>
<p>Users connect to the target's IP address using their preferred client software. The user must be logged into the Cloudflare One Client on their device, but no other system configuration is required. You can optionally configure a <a href="/cloudflare-one/traffic-policies/resolver-policies/">private DNS resolver</a> to allow connections to the target's private hostname.</p>
<h3 id="connect-to-different-vnet">Connect to different VNET</h3>
<p>To connect to targets that are in different VNETS, users will need to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/#connect-to-a-virtual-network">switch their connected virtual network</a> in the Cloudflare One Client.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4794.md")
</aside>
<h3 id="display-available-targets">Display available targets</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/4817.md")
</div></details>
<p>Users can use <code>warp-cli</code> to display a list of targets they can access. On the device, open a terminal and run the following command:</p>
<pre tabindex="0"><code class="language-sh">warp-cli target list&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">╭──────────────────────────────────────┬──────────┬───────┬───────────────────────┬──────────────────────┬────────────╮&#10;│ Target ID                            │ Protocol │ Port  │ Attributes            │ IP (Virtual Network) │ Usernames  │&#10;├──────────────────────────────────────┼──────────┼───────┼───────────────────────┼──────────────────────┼────────────┤&#10;│ 0193f22a-9df3-78e3-b5bb-7ab631903306 │ SSH      │ 22    │ hostname: do-target   │ 10.116.0.3 (a1net)   │ alice      │&#10;├──────────────────────────────────────┼──────────┼───────┼───────────────────────┼──────────────────────┼────────────┤&#10;│ 0193f22a-9df3-78e3-b5bb-7ab631903306 │ SSH      │ 23    │ hostname: do-target   │ 10.116.0.3 (a1net)   │ root       │&#10;├──────────────────────────────────────┼──────────┼───────┼───────────────────────┼──────────────────────┼────────────┤&#10;│ 01943cff-6130-7989-8bff-cbc02b59a2b1 │ SSH      │ 80    │ hostname: az-target   │ 172.16.0.0 (b1net)   │ alice, bob │&#10;╰──────────────────────────────────────┴──────────┴───────┴───────────────────────┴──────────────────────┴────────────╯&#10;</code></pre>
<p>You can optionally add flags to filter the output. For example:</p>
<pre tabindex="0"><code class="language-sh">warp-cli target list --attribute hostname=do-target --username root&#10;</code></pre>
<p>To view all available filters, type <code>warp-cli target list --help</code>.</p>
<h2 id="revoke-a-user-s-session">Revoke a user's session</h2>
<p>To revoke a user's access to all infrastructure targets, you can either <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">revoke the user from Zero Trust</a> or revoke their device. Cloudflare does not currently support revoking a user's session for a specific target.</p>
<h2 id="granular-target-permissions">Granular target permissions</h2>
<p>Infrastructure Access supports granular read permissions through <a href="/fundamentals/manage-members/roles/">Cloudflare's role-based access control</a>. Administrators can assign read-only roles scoped to specific targets instead of granting account-wide access. When a user with a scoped role calls the targets list API, the response is automatically filtered to only include the targets they have permission to view.</p>
<p>This is useful for organizations that want to give teams visibility into their own infrastructure targets without exposing the full target inventory.</p>
<h2 id="target-criteria">Target criteria</h2>
<p>Use target criteria to define which targets an infrastructure application covers. Each target criteria entry includes a protocol, a port, and selectors that match targets by hostname, tag, or both.</p>
<p>The <code>target_attributes</code> selector only supports <code>hostname</code> in both the legacy and operator-based formats. Cloudflare rejects any other <code>target_attributes</code> key.</p>
<p>A target can only store one value for each tag key. This limit does not apply to target criteria. For example, an application can match both <code>environment:production</code> and <code>environment:staging</code> in <code>include</code>, <code>require</code>, or <code>exclude</code>.</p>
<h3 id="operators">Operators</h3>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Logic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>include</code></td>
<td>OR</td>
<td>Target must match at least one included selector.</td>
</tr>
<tr>
<td><code>require</code></td>
<td>AND</td>
<td>Target must match all required selectors.</td>
</tr>
<tr>
<td><code>exclude</code></td>
<td>NOT(OR)</td>
<td>Target is rejected if it matches any excluded selector.</td>
</tr>
</tbody>
</table>
<p>Combined evaluation: <strong>(any include) AND (all requires) AND NOT (any excludes)</strong>.</p>
<h3 id="legacy-format">Legacy format</h3>
<p>You can continue to use the flat <code>target_attributes</code> format for existing hostname-only applications. This only matters if you manage applications through the API or Terraform. For each target criteria entry, choose one format: either flat <code>target_attributes</code> or operator-based <code>include</code>, <code>require</code>, and <code>exclude</code>.</p>
<h2 id="infrastructure-policy-selectors">Infrastructure policy selectors</h2>
<p>The following <a href="/cloudflare-one/access-controls/policies/#selectors">Access policy selectors</a> are available for securing infrastructure applications:</p>
<ul>
<li>Email</li>
<li>Emails ending in</li>
<li>SAML group</li>
<li>Country</li>
<li>Authentication method</li>
<li>Device posture</li>
<li>Entra group, GitHub organization, Google Workspace group, Okta group</li>
</ul>
