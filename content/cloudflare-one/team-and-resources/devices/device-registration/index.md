---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/
  description: Reference information for Device registration in Zero Trust.
  full_title: Device registration · Cloudflare One docs
  head_html: <title>Device registration · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Device registration in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/index.md"><meta property="og:title" content="Device registration · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Device registration in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/#page","headline":"Device registration \u00b7 Cloudflare One docs","description":"Reference information for Device registration in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/device-registration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/device-registration/
  schema: 1
---
<p>A device registration represents an individual session of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on a physical device, linking a user (or service token) and the device to your <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a>. It is created the first time the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> authenticates on that device.</p>
<p>Each device registration includes a unique public key, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a>, and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">virtual IP addresses</a> (one IPv4 and one IPv6) that identify the device on your network.</p>
<p>A single physical device can have <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multiple device registrations</a>, for example, if multiple users share a single laptop and each enrolls the Cloudflare One Client with their own credentials.</p>
<h2 id="key-concepts">Key concepts</h2>
<table>
<thead>
<tr>
<th>Concept</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/team-and-resources/users/seat-management/#manage-users">User</a></td>
<td>A person whose identity is verified through your identity provider (IdP) and who can enroll devices in your Zero Trust organization.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/users/seat-management/">Seat</a></td>
<td>A billable unit consumed when a user authenticates to your Zero Trust organization. Each user occupies one seat regardless of how many devices they enroll. Service tokens do not consume seats.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service token</a></td>
<td>Credentials used by automated systems to authenticate against your Cloudflare One policies.</td>
</tr>
<tr>
<td>Device registration</td>
<td>An individual session of the Cloudflare One Client on a physical device, with its own public key, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a>, and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">virtual IP addresses</a> (one IPv4 and one IPv6).</td>
</tr>
<tr>
<td><a href="/cloudflare-one/access-controls/access-settings/session-management/">Session</a></td>
<td>A time-limited JSON Web Token (JWT) that controls how long a user can access an Access application before re-authenticating. Unlike sessions, a device registration is persistent — it does not expire and exists until you delete it.</td>
</tr>
</tbody>
</table>
<h2 id="review-device-registration-status">Review device registration status</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5964.md")
</div></div>
<p>A deleted device registration is permanently removed from the account and no longer appears in your device list. Deletion is permanent and requires re-registering the device.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="device-registrations-will-automatically-re-register">Device registrations will automatically re-register</h3>
@markup("md", "content/.markup/bodies/5961.md")
</aside>
<h3 id="registration-status">Registration status</h3>
<p>Registrations can have the following statuses:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Active</strong></td>
<td>Registered and able to connect via the Cloudflare One Client. This is the expected operational state.</td>
</tr>
<tr>
<td><strong>Revoked</strong></td>
<td>The registration's public key is invalidated. Revocation does not release the assigned virtual IP addresses.</td>
</tr>
</tbody>
</table>
<h2 id="manage-device-registrations">Manage device registrations</h2>
<p>The following table summarizes the actions available for managing device registrations and devices. For all actions, if the user or service token can still re-authenticate, a new registration will be created automatically. To permanently remove access, refer to <a href="#device-management">Device management</a>.</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>What it does</th>
<th>Virtual IPs released?</th>
<th>When to use</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#delete-a-device-registration">Delete a registration</a></td>
<td>Permanently removes a single device registration and its configuration.</td>
<td>Yes</td>
<td>You want to fully remove a user's enrollment from a device and free up the virtual IP.</td>
</tr>
<tr>
<td><a href="#revoke-a-device-registration">Revoke a registration</a></td>
<td>Invalidates the registration's public key, blocking it from connecting. The registration record remains.</td>
<td>No</td>
<td>You want to temporarily block a device from connecting but preserve the registration record.</td>
</tr>
<tr>
<td><a href="#delete-a-device">Delete a device</a></td>
<td>Removes the physical device record and all its associated registrations.</td>
<td>Yes</td>
<td>You want to fully remove a device and all associated registrations.</td>
</tr>
</tbody>
</table>
<h3 id="delete-a-device-registration">Delete a device registration</h3>
<p>Devices can have multiple device registrations. Deleting one registration does not affect other registrations on the same device.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5967.md")
</div></div>
<p>The device registration is now permanently deleted, and its virtual IP address is released back into the available pool for reassignment.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="automatic-device-re-registration">Automatic device re-registration</h3>
@markup("md", "content/.markup/bodies/5960.md")
</aside>
<h3 id="revoke-a-device-registration">Revoke a device registration</h3>
<p>Revoking a device registration invalidates its associated public key, which disallows the specific device registration from connecting to Cloudflare's network. Revoking a device registration does not release the virtual IPs that are assigned to the registration. Because virtual IPs are a finite resource, Cloudflare strongly advises deleting a registration rather than revoking it.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="automatic-unrevocation">Automatic unrevocation</h3>
@markup("md", "content/.markup/bodies/5959.md")
</aside>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Teams &amp; Resources</strong> &gt; <strong>Devices</strong>.</li>
<li>Select the device and select <strong>View details</strong>.</li>
<li>To revoke access, select <strong>Revoke access</strong>. This revokes access for all associated registrations on the device.</li>
<li>To unrevoke access, scroll down to the <strong>Users</strong> section and select one or more users using the checkbox. Select <strong>Actions</strong> &gt; <strong>Unrevoke access</strong>.</li>
</ol>
<h3 id="delete-a-device">Delete a device</h3>
<p>Deleting a device removes the physical device from your Cloudflare Zero Trust account. This action automatically deletes all associated device registrations.</p>
<p>Devices that have zero active registrations (because all registrations were deleted) are hidden by default in Cloudflare One &gt; <strong>Teams &amp; Resources</strong> &gt; <strong>Devices</strong> table. You may need to adjust the filter to view devices with zero device registrations.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="automatic-device-re-creation">Automatic device re-creation</h3>
@markup("md", "content/.markup/bodies/5958.md")
</aside>
<p>To delete a device:</p>
<ol>
<li>In Cloudflare One &gt; <strong>Teams &amp; Resources</strong> &gt; <strong>Devices</strong>.</li>
<li>Select the device and select <strong>View details</strong>.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
<h2 id="device-management">Device management</h2>
<p>Seat management (billing) and access management are separate processes. Deleting a device registration does not free up the user's seat or block them from accessing internal resources. To fully remove a user's access, you must take additional steps as described below.</p>
<h3 id="remove-user-access">Remove user access</h3>
<p>Deleting or revoking a registration will not be permanent if the user can re-authenticate. To prevent a user from re-authenticating and creating new device registrations, you must remove them from your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">device enrollment policies</a> or from your Identity Provider (IdP).</p>
<ul>
<li>If your device enrollment policies allow a broad domain (for example, <code>@company.com</code>), remove the user from your IdP. This prevents the user from authenticating through Access, effectively blocking them from enrolling devices.</li>
<li>If your device enrollment policies list specific user emails (for example, <code>sally@company.com</code>), you must remove that specific email from your device enrollment policies. Additionally, you can add an explicit Exclude rule for that user to the policy.</li>
</ul>
<p>After you have removed user access, to fully decommission a device, <a href="/cloudflare-one/team-and-resources/devices/device-registration/#remove-service-token-access">remove service token access</a>, if any exists. Devices with existing registrations will remain connected to Cloudflare until those specific device registrations are manually deleted.</p>
<h3 id="remove-service-token-access">Remove service token access</h3>
<p>If you delete a service token's device registration, a new device registration for the service token will be automatically created without user interaction. For device registration deletion to be permanent, you must update your device enrollment policies to remove the service token.</p>
<p>To block a service token from re-authenticating, you must either:</p>
<ol>
<li>Delete the enrollment policy associated with the token, or modify the enrollment policy to no longer include the token (by removing its specific Include rule).</li>
<li>(Optional) <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Delete the service token</a>.
<br/> You cannot use this service token to create new registrations.
<br/> You cannot delete a service token while it is attached to a device enrollment policy.</li>
<li>Delete the service token <a href="/cloudflare-one/team-and-resources/devices/device-registration/#delete-a-device-registration">device registration</a>.</li>
<li>(Optional) To fully decommission a device, <a href="/cloudflare-one/team-and-resources/devices/device-registration/#remove-user-access">remove user access</a>, if any exists. Devices with existing registrations will remain connected to Cloudflare until those specific device registrations are manually deleted.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="impact-on-existing-registrations">Impact on existing registrations</h3>
@markup("md", "content/.markup/bodies/5957.md")
</aside>
<h3 id="seat-management-billing">Seat management (billing)</h3>
<p>Deleting a device or a device registration does not affect <a href="/cloudflare-one/team-and-resources/users/seat-management/">seat usage</a>. Seats are tied to the user identity, not to individual devices.</p>
<p>To stop a user from consuming a seat, you must remove the user from your Zero Trust Organization.</p>
<p>Removing a user from your Zero Trust Organization will free up the seat the user consumed. The user will still appear in your list of users.</p>
<p>To remove a user from your Zero Trust Organization:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong>.</li>
<li>Select the checkbox next to a user with an <strong>Active</strong> status in the <strong>Seat usage</strong> column.</li>
<li>Select <strong>Action</strong> &gt; <strong>Remove users</strong>.</li>
<li>Select <strong>Remove</strong>.</li>
</ol>
<p>The user will now show as <strong>Inactive</strong> and will no longer occupy a seat. If a user is removed but authenticates later, they will consume a seat again. To prevent a user from authenticating, you must remove them from your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">device enrollment policies</a> or from your Identity Provider (IdP).</p>
<p>To automate the removal of users who have not logged in or triggered a device enrollment in a specific amount of time, turn on <a href="/cloudflare-one/team-and-resources/users/seat-management/#enable-seat-expiration">seat expiration</a> or utilize <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a> to remove users when they are deactivated in your identity provider.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="user-record-persistence">User record persistence</h3>
@markup("md", "content/.markup/bodies/5956.md")
</aside>
