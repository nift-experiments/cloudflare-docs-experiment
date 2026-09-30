<aside class="nb-aside note">
<h3 class="nb-aside-title" id="compatibility">Compatibility</h3>
@markup("md", "content/.markup/bodies/4505.md")
</aside>
<p>Outbound Data Loss Prevention ensures the protection of sensitive information in outbound emails with <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a>. Outbound Data Loss Prevention integrates with your inbox, and it proactively monitors your email to prevent unauthorized data leaks.</p>
<p>To enable Outbound DLP:</p>
<ol>
<li><a href="/cloudflare-one/email-security/outbound-dlp/#1-create-an-outbound-policy">Create an outbound policy</a>.</li>
<li><a href="/cloudflare-one/email-security/outbound-dlp/#2-dlp-assist-add-in">Set up DLP Assist add-in</a>.</li>
</ol>
<h2 id="1-create-an-outbound-policy"><ol>
<li>Create an outbound policy</li>
</ol></h2>
<p>An outbound policy allows you to control outbound email flow.</p>
<p>To create an outbound DLP policy:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Email security</strong> &gt; <strong>Outbound DLP</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Name your policy.</li>
<li>Build an expression to match specific email traffic. For example, you can create a policy that blocks outbound emails containing identifying numbers:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Recipient email</td>
<td>not in</td>
<td><code>example.com</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Matched DLP profile</td>
<td>in</td>
<td><em>Social Security, Insurance, Tax, and Identifier Numbers</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>(Optional) Choose whether to use the default block message or a custom message.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>After creating your policy, you can modify or reorder your policies in <strong>Email security</strong> &gt; <strong>Outbound DLP</strong>.</p>
<h3 id="selectors">Selectors</h3>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Recipient email</td>
<td>The intended recipient of an outbound email.</td>
</tr>
<tr>
<td>Email sender</td>
<td>The user in your organization sending an email.</td>
</tr>
<tr>
<td>Matched DLP profile</td>
<td>The <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profile</a> that content of an email matches upon scan.</td>
</tr>
</tbody>
</table>
<h2 id="2-dlp-assist-add-in"><ol start="2">
<li>DLP Assist add-in</li>
</ol></h2>
<p>The Data Loss Prevention (DLP) Assist add-in allows Microsoft 365 users to deploy a DLP solution for free using Cloudflare's Email security. DLP Assist add-in protects your data egress from Outlook web and desktop client.</p>
<p>To set up DLP Assist add-in:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Email security</strong> &gt; <strong>Outbound DLP</strong>.</li>
<li>Select <strong>View Microsoft add-in instructions</strong> &gt; Select <strong>Download add-in</strong>. This downloads a <code>.xml</code> file necessary to install the add-in on the client side.</li>
<li>Set up the add-in in Microsoft 365:
<ul>
<li>Log in to the <a href="https://security.microsoft.com/homepage">Microsoft admin panel</a> and go to <strong>Microsoft 365 Admin Center</strong> &gt; <strong>Settings</strong> &gt; <strong>Integrated Apps</strong>.</li>
<li>Choose <strong>Upload custom apps</strong> and select <strong>Office Add-in</strong> for the application type.</li>
<li>Select <strong>Upload manifest file (.xml) from device</strong>.</li>
<li>Upload the Cloudflare add-in file you downloaded in step three. Then, verify and complete the wizard. It can take up to 24 hours for an add-in to propagate.</li>
</ul>
</li>
</ol>
<p>The add-in works by inserting headers into the <a href="https://en.wikipedia.org/wiki/EML">EML</a> on the client side before the message is sent out.</p>
<p>To block, encrypt, or send approval, you can configure rules within Microsoft Purview DLP:</p>
<ol>
<li>Go to <a href="https://purview.microsoft.com/datalossprevention/overview?tid=11648e1c-3d60-40e2-bf07-f8d481e48e2d">Microsoft Purview</a>.</li>
<li>Select <strong>Policies</strong> &gt; <strong>Create policy</strong>.</li>
<li>Do not choose any templates or custom policy. Select <strong>Next</strong>.</li>
<li>Choose a name and description for the policy: You can choose any name. However, this guide will use <code>Cloudflare Assist Block</code>.</li>
<li>Select <strong>Next</strong> on <strong>Admin Units</strong>:
<ul>
<li>Choose to only apply to <strong>Exchange Email</strong>.</li>
<li>Choose <strong>Create or customize advanced DLP Rules</strong>.</li>
</ul>
</li>
<li>Select <strong>Create rule</strong>:
<ul>
<li>Create a policy name.</li>
<li>Add the following conditions:
<ul>
<li><strong>Header contains words or phrases</strong>: <code>Key: cf_outbound_dlp with Value: BLOCK</code></li>
<li>Select <strong>AND</strong>.</li>
<li><strong>Content is shared from Microsoft 365</strong>: Select <strong>with people from outside my organization</strong>.</li>
</ul>
</li>
</ul>
</li>
<li>Under <strong>Actions</strong>, the admin can choose what to do with the message. You can use the <strong>Restrict access or encrypt the content in Microsoft 365 locations</strong> to block the message or encrypt it.</li>
<li>Under <strong>User notifications</strong>, turn on notifications. Admins can also edit the message if they want to. You can also configure if the admin wants to receive a notification under <strong>Incident reports</strong> &gt; <strong>Use this severity level in admin alerts and reports</strong>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Select <strong>Turn the Policy On Immediately</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4504.md")
</aside>
<h3 id="limitations">Limitations</h3>
<p>Outbound DLP presents its limitations:</p>
<ul>
<li>Outbound DLP only protects user-managed inboxes.</li>
<li>Outbound DLP offers the most consistent experience on Outlook Web App and Outlook desktop, due to limitations imposed by Microsoft.</li>
</ul>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Web client</td>
<td>Stable</td>
</tr>
<tr>
<td>New Outlook desktop client - Windows</td>
<td>Stable</td>
</tr>
<tr>
<td>Desktop client - macOS</td>
<td>Can cause scanning to be delayed due to Apple limitation</td>
</tr>
<tr>
<td>Old Outlook desktop client</td>
<td>Does not work due to Microsoft limitation</td>
</tr>
<tr>
<td>Mobile client - iOS</td>
<td>Unstable due to Apple limitation</td>
</tr>
<tr>
<td>Mobile client - Android</td>
<td>Unstable due to Microsoft limitation</td>
</tr>
</tbody>
</table>
