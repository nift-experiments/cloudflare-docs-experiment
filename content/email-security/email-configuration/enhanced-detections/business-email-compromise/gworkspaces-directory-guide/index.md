<p>Email security can integrate with Google to retrieve user and group information. This can be used to enforce the Business Email Compromise configuration to prevent user impersonation.</p>
<h2 id="1-create-a-service-account-in-google-for-email-security-directory-integration"><ol>
<li>Create a service account in Google for Email security Directory Integration</li>
</ol></h2>
<p>You need to authorize Email security to make connections into your Google tenant to retrieve your directory details. Cloudflare recommends that you create a service account for this purpose. This account will require the following following privileges:</p>
<ul>
<li>View group subscriptions on your domain.</li>
<li>View organization units on your domain.</li>
<li>View groups on your domain.</li>
<li>See info about users on your domain.</li>
</ul>
<p>Start by creating a service account. If you already have one, you can skip this step.</p>
<ol>
<li>Access your <a href="https://admin.google.com/">Google admin console</a>, and go to <strong>Account</strong> &gt; <strong>Admin roles</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/gmail/step1-access-gadmin.png" alt="Access the admin console in your Google account" /></p>
<ol start="2">
<li>
<p>Select <strong>Create new role</strong>, and give it a descriptive name and description. When you are finished, select <strong>Continue</strong>.</p>
</li>
<li>
<p>In <strong>Admin console privileges</strong>, select the following privileges:</p>
<ul>
<li><em>Organizational Units &gt; Read</em></li>
<li><em>Users &gt; Read</em></li>
<li><em>Directory Settings &gt; Settings &gt;Google Support Settings</em></li>
<li><em>Directory Sync &gt; Manage Directory Sync Settings &gt; Read Directory Sync Settings</em></li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/gmail/step3-console-privileges.png" alt="Select only the privileges mentioned here" /></p>
<ol start="4">
<li>When you specify Admin console privileges, you also grant the corresponding Admin API privileges. In any case, make sure the following privileges are selected for <strong>Admin API privileges</strong>:
<ul>
<li><em>Organizational Units &gt; Read</em></li>
<li><em>Users &gt; Read</em></li>
<li><em>Groups &gt; Read</em></li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/gmail/step4-api-privileges.png" alt="Select only the privileges mentioned here" /></p>
<ol start="5">
<li>
<p>Select <strong>Continue</strong>.</p>
</li>
<li>
<p>Review your information and select <strong>Create Role</strong>.</p>
</li>
</ol>
<h2 id="2-authorize-email-security-for-directory-access-with-google"><ol start="2">
<li>Authorize Email security for Directory Access with Google</li>
</ol></h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>, and select <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Directories</strong>, and select <strong>Add Directory</strong> to start the authorization process.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/gmail/step2-directories.png" alt="Go to Directories in the dashboard of Email security, and then select Add Directory to start the authorization process" /></p>
<ol start="3">
<li>
<p>In the Add Directory configuration panel, enter the following details:</p>
<ul>
<li><strong>Directory Type</strong>: Open the drop-down menu and select <strong>Google</strong>.</li>
<li><strong>Directory Name</strong>: Enter a string that represents the directory. This value will be referenced in the Business Email Compromise List configuration section. For example, <code>Gmail</code>.</li>
<li><strong>Sync Frequency</strong>: Update the value to your preference.</li>
</ul>
<p>Select <strong>Authorize</strong> when you are done.</p>
</li>
<li>
<p>The Email security dashboard will redirect you to a Google login page. Select or enter the appropriate account to initiate the authentication process.</p>
</li>
<li>
<p>Once authenticated, the system will show a dialog box with a list of the required permissions. Check all the checkboxes, and select <strong>Continue</strong> to authorize the change.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/gmail/step5-authorize-google.png" alt="Select all the settings to authorize Google" /></p>
<ol start="6">
<li>Upon authorization, you will be automatically redirected back to the Add Directory configuration panel. Select <strong>Save</strong> to complete the authorization process.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/gmail/step6-save.png" alt="Select Save to complete the authorization process" /></p>
<ol start="7">
<li>Once saved, your newly configured directory will appear in the configured directories table.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/bec/gmail/step7-directories.png" alt="Your directory will appear in the configured directories table" /></p>
<h2 id="3-configure-the-business-email-compromise-list"><ol start="3">
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
<h2 id="4-configure-secondary-email-address-if-required"><ol start="4">
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
