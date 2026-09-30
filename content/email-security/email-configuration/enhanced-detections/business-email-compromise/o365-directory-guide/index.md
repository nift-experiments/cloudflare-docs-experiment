---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/o365-directory-guide/
  description: Integrate Email security with Office 365 directories to enforce BEC protection against user impersonation.
  full_title: Office 365 directory integration · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Office 365 directory integration · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Email security with Office 365 directories to enforce BEC protection against user impersonation."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/o365-directory-guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/o365-directory-guide/index.md"><meta property="og:title" content="Office 365 directory integration · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Email security with Office 365 directories to enforce BEC protection against user impersonation."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/enhanced-detections/business-email-compromise/o365-directory-guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/enhanced-detections/business-email-compromise/o365-directory-guide/
  schema: 1
---
<p>Email security (formerly Area 1) can integrate with Office 365 to retrieve user and group information. This can be used to enforce the Business Email Compromise configuration to prevent user impersonation.</p>
<h2 id="1-authorize-email-security-with-office-365-for-directory-access"><ol>
<li>Authorize Email security with Office 365 for Directory Access</li>
</ol></h2>
<p>You need to authorize Email security to make connections into your <a href="https://learn.microsoft.com/en-us/microsoft-365/solutions/tenant-management-overview">Office 365 tenant</a> to retrieve your directory details. The account used to authorize will require the <strong>Privileged authentication admin</strong> and <strong>Privileged role admin</strong> roles.</p>
<h3 id="how-does-the-authorization-work">How does the authorization work?</h3>
<p>The authorization process grants Email security access to the Azure environment with the least applicable privileges required to function. The Enterprise Application that Email security registers is not tied to any administrator account. Inside of the Azure Active Directory admin center you can review the permissions granted to the application in the Enterprise Application section.</p>
<p>When assigning user roles in the Office 365 console, you will find these roles in <strong>User permissions</strong> &gt; <strong>Roles configuration</strong> &gt; <strong>Identity admin roles</strong>.</p>
<p><img src="/assets/upstream/images/email-security/bec/o365/permissions.png" alt="A list of permissions for Email security" /></p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>, and select <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Directories</strong>, and select <strong>Add Directory</strong> to start the authorization process.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step2-directories.png" alt="Go to Directories in the dashboard of Email security, and then select Add Directory to start the authorization process" /></p>
<ol start="3">
<li>
<p>In the Add Directory configuration panel, enter the following details:</p>
<ul>
<li><strong>Directory Type</strong>: Open the drop-down menu and select <strong>Office 365</strong>.</li>
<li><strong>Directory Name</strong>: Enter a string that represents the directory. This value will be referenced in the Business Email Compromise List configuration section. For example, <code>Office 365</code>.</li>
<li><strong>Sync Frequency</strong>: Update the value to your preference.</li>
</ul>
<p>Select <strong>Authorize</strong> when you are done.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step3-directory-config-panel.png" alt="Add the appropriate details to the configuration panel" /></p>
<ol start="4">
<li>The Email security dashboard will redirect you to a Microsoft login page. Select or enter the appropriate account to initiate the authentication process.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/bec/o365/step4-login.png" alt="Select the appropriate Microsoft account to continue" /></p>
</div>
<ol start="5">
<li>Once authenticated, the system will show a dialog box with a list of the requested permissions. Select <strong>Accept</strong> to authorize the change.</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/bec/o365/step5-permissions.png" alt="Accept the permissions to continue" /></p>
</div>
<ol start="6">
<li>Upon authorization, you will be automatically redirected back to the Add Directory configuration panel. Select <strong>Save</strong> to complete the authorization process.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step6-save.png" alt="Select Save to complete the authorization process" /></p>
<ol start="7">
<li>Once saved, your newly configured directory will appear in the configured directories table.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step7-directories.png" alt="Your directory will appear in the configured directories table" /></p>
<h2 id="2-configure-the-business-email-compromise-list"><ol start="2">
<li>Configure the Business Email Compromise list</li>
</ol></h2>
<p>Now that Email Security (formerly Area 1) has been authorized to access and retrieve directory information, you will need to configure the Business Email Compromise list.</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email Security (formerly Area 1) dashboard</a>, and select <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Email Configuration</strong> &gt; <strong>Enhanced Detections</strong> &gt; <strong>Business Email Compromise</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step2-business-email-compromise.png" alt="Access Business Email Compromise in Email Security (formerly Area 1) dashboard to start setting up this feature" /></p>
<ol start="3">
<li>Open the drop-down menu and select the directory you have created in the previous step 3.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step3-office365.png" alt="Select the directory you have created in the previous step 3" /></p>
<ol start="4">
<li>If the initial directory synchronization has completed, the page will refresh and list groups and users. If you do not see any information, wait a few minutes as the system completes processing the initial synchronization.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step4-business-list.png" alt="The screen should refresh and show a list of users and groups" /></p>
<ol start="5">
<li>Select the arrow next to a group to expand it and show its members.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step5-show-members.png" alt="Select the arrow to expand it and show a list of its members" /></p>
<ol start="6">
<li>To protect an entire group, select the three-dots button next to it, and then select <strong>Protect</strong>. When you protect a group, all of its members will be automatically protected. The protection markers will turn green to indicate that protection is active.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step6-protect-group.png" alt="You can protect an entire group of users. The protection markers will turn green to show that protection is active" /></p>
<ol start="7">
<li>You can also protect individual users. Select the three-dots button next to each user you want to protect, and then select <strong>Protect</strong>.</li>
</ol>
<h2 id="3-configure-secondary-email-address-if-required"><ol start="3">
<li>Configure secondary email address (if required)</li>
</ol></h2>
<p>When the Business Email Compromise list is configured, Email Security (formerly Area 1) will enforce the proper match of the sender’s display name and email address. Any variation from this strict requirement will raise a detection event. The reason of detection will be <code>Protected Name &lt;NAME&gt; should not appear as &lt;non-configured email address&gt;</code>.</p>
<p>In some instances, you may want to allow your protected users to send emails from an alternate email address (like their personal email address). To configure this alternate address, you will have to add it to their directory entry.</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email Security (formerly Area 1) dashboard</a>, and select <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Email Configuration</strong> &gt; <strong>Enhanced Detections</strong> &gt; <strong>Business Email Compromise</strong>.</p>
</li>
<li>
<p>Search for the user you want to allow an alternate email address.</p>
</li>
<li>
<p>Select the three-dots button &gt; <strong>Edit</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step4-edit-user.png" alt="Select edit to add alternate email addresses to your user" /></p>
<ol start="5">
<li>In <strong>Secondary Emails</strong> add the additional email addresses. Place each entry on a new line.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/o365/step5-new-email.png" alt="Add each new email address to the Secondary Emails field. Place each address on a separate line" /></p>
<ol start="6">
<li>Select <strong>Save</strong> to finish.</li>
</ol>
