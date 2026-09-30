---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/
  description: Device profiles in Zero Trust.
  full_title: Device profiles · Cloudflare One docs
  head_html: <title>Device profiles · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Device profiles in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/index.md"><meta property="og:title" content="Device profiles · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Device profiles in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/#page","headline":"Device profiles \u00b7 Cloudflare One docs","description":"Device profiles in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/
  schema: 1
---
<p>A device profile defines <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/">Cloudflare One Client settings</a> for a specific set of devices in your organization. You can create multiple profiles and apply different settings based on the user's identity, the device's location, and other criteria.</p>
<p>For example, users in one identity provider group (signifying a specific office location) might have different routes that need to be excluded from their WARP tunnel, or some device types (like Linux) might need different DNS settings to accommodate local development services.</p>
<h2 id="create-a-new-profile">Create a new profile</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6186.md")
</div></div>
<h2 id="edit-profile-settings">Edit profile settings</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Locate the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> you would like to update and select <strong>Configure</strong>.</li>
<li>Use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/#selectors">selectors</a> to add or adjust match rules, and modify <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-settings">device client settings</a> for this profile as needed.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6181.md")
</aside>
<ol start="4">
<li>Select <strong>Save profile</strong>.</li>
</ol>
<p>It may take up to 10 minutes for newly updated settings to propagate to devices.</p>
<h2 id="verify-device-profile">Verify device profile</h2>
<h3 id="via-the-dashboard">Via the dashboard</h3>
<p>To verify the last active device profile for a specific device:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>.</li>
<li>Under devices, find your device.</li>
<li>Review the device profile under <strong>Last active device profile</strong>.</li>
</ol>
<p>To verify the last active device profile for a user's devices:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong>.</li>
<li>Under <strong>User name</strong>, find the user you would like to investigate.</li>
<li>Select <strong>Devices</strong> to see all devices used by the user.</li>
<li>Find the device you want to investigate and verify the last active device profile for that device under the <strong>Device profile</strong> column.</li>
</ol>
<p>Alternatively, you can use <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/">DEX remote captures</a> to collect client diagnostic logs. The device profile UUID is shown in your <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta">detection report</a> under <code>Profile ID</code>.</p>
<h3 id="via-the-cli">Via the CLI</h3>
<p>To check which device profile and profile settings are currently on a device, open a terminal and run:</p>
<pre tabindex="0"><code class="language-sh">warp-cli settings&#10;</code></pre>
<p>The device profile UUID is shown in the <code>Profile ID</code> field.</p>
<h2 id="selectors">Selectors</h2>
<p>You can configure device profiles to match against the following selectors, or criteria. Identity-based selectors are only available if the user <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">enrolled the device</a> by logging in to an identity provider (IdP).</p>
<h3 id="user-email">User email</h3>
<p>Apply a device profile based on the user's email.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User email</td>
<td><code>identity.email == &quot;user-name@company.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-group-emails">User group emails</h3>
<p>Apply a device profile based on an <a href="/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway">IdP group</a> email address of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User group emails</td>
<td><code>identity.groups.email == &quot;contractors@company.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-group-ids">User group IDs</h3>
<p>Apply a device profile based on an <a href="/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway">IdP group</a> ID of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User group IDs</td>
<td><code>identity.groups.id == &quot;12jf495bhjd7893ml09o&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-group-names">User group names</h3>
<p>Apply a device profile based on an <a href="/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway">IdP group</a> name of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User group names</td>
<td><code>identity.groups.name == &quot;\&quot;finance\&quot;&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="operating-system">Operating system</h3>
<p>Apply a device profile based on the operating system of the device.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operating system</td>
<td><code>os.name in {\&quot;windows\&quot; \&quot;mac\&quot;}</code></td>
</tr>
</tbody>
</table>
<h3 id="operating-system-version">Operating system version</h3>
<p>Apply a device profile based on the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/#determine-the-os-version">OS version</a> of the device.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operating system version</td>
<td><code>os.version == \&quot;1.2.0\&quot;</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6180.md")
</aside>
<h3 id="managed-network">Managed network</h3>
<p>Apply a device profile based on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/">managed network</a> that the device is connected to.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Managed network</td>
<td><code>network == \&quot;Austin office\&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="saml-attributes">SAML attributes</h3>
<p>Apply a device profile based on an attribute name and value from a <a href="/cloudflare-one/traffic-policies/identity-selectors/#generic-saml-idp">SAML IdP</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>SAML Attributes</td>
<td><code>identity.saml_attributes == &quot;\&quot;group=finance\&quot;&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="service-token">Service token</h3>
<p>Apply a device profile based on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token">service token</a> used to enroll the device.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Service Token</td>
<td><code>identity.service_token_uuid == \&quot;f174e90a-fafe-4643-bbbc-4a0ed4fc8415\&quot;</code></td>
</tr>
</tbody>
</table>
<h2 id="comparison-operators">Comparison operators</h2>
<p>Comparison operators determine how device profiles match a selector.</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>is</td>
<td>equals the defined value</td>
</tr>
<tr>
<td>in</td>
<td>matches at least one of the defined values</td>
</tr>
</tbody>
</table>
<h2 id="logical-operators">Logical operators</h2>
<p>To evaluate multiple conditions in an expression, select a logical operator:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>And</td>
<td>match all of the conditions in the expression</td>
</tr>
<tr>
<td>Or</td>
<td>match any of the conditions in the expression</td>
</tr>
</tbody>
</table>
<h2 id="order-of-precedence">Order of precedence</h2>
<p>The Cloudflare One Client evaluates device profiles dynamically based on a hierarchy. When a device connects, the client checks the profiles from top to bottom as they appear in the dashboard. The client follows the first match principle — once a device matches a profile, the client stops evaluating and no subsequent profiles can override the decision.</p>
<p>The <strong>Default</strong> profile is always at the bottom of the list. It will only be applied if the device does not meet the criteria of any profile listed above it. If you make another custom profile the default, all settings will be copied over into the <strong>Default</strong> profile.</p>
<p>Administrators can create multiple profiles to apply different settings based on specific criteria such as user identity, location, or operating system. Understanding this top-to-bottom evaluation order is crucial for ensuring that the correct policies are applied to devices.</p>
