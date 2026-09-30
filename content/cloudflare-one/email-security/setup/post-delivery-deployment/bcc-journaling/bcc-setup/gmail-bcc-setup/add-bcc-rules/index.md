<p>This page will show you how to add BCC rules in the Google Admin Console.</p>
<p>BCC stands for Blind Carbon Copy. A BCC rule is a Google Workspace feature that allows you to create a secure copy of all selected outbound and inbound emails. When you allow Email security to receive a copy of your emails, Cloudflare can perform post-delivery analysis to protect your email inbox.</p>
<p>To add BCC rules:</p>
<ol>
<li>Log in to the <a href="https://admin.google.com/">Google Admin Console</a>.</li>
<li>On the sidebar, go to <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong> &gt; <strong>Compliance</strong>.</li>
<li>Go to <strong>Content Compliance</strong> &gt; Select <strong>Edit</strong>.</li>
<li>Add a <strong>Content Compliance</strong> filter, and name it <code>Email security - BCC</code>.</li>
<li>In <strong>Email messages to affect</strong>, select <strong>Inbound</strong>.</li>
<li>Select the recipients you want to send emails to Email security via BCC. Under <strong>Add expressions that describe the content you want to search for in each message</strong>:
<ul>
<li>Select <strong>If ANY of the following match the message</strong>.</li>
<li>Select <strong>Add</strong> to configure the expression.
<ul>
<li>Select <strong>Advanced content match</strong>.</li>
<li>In <strong>Location</strong>, select <strong>Headers + Body</strong>.</li>
<li>In <strong>Match type</strong>, select <strong>Matches regex</strong>.</li>
<li>In <strong>Regexp</strong>, input <code>.*</code>. You can customize the regex as needed and test within the admin page or on sites like <a href="https://regexr.com/">Regexr</a>.</li>
<li>Select <strong>SAVE</strong>.</li>
</ul>
</li>
</ul>
</li>
<li>In <strong>If the above expressions match, do the following</strong>:
<ul>
<li>Select <strong>Modify message</strong>.
<ul>
<li>Ensure that <strong>Envelope recipient</strong> &gt; <strong>Change envelope recipient</strong> is unselected, so that emails will not be dropped as an unintended consequence. You will select this option at a later stage.</li>
<li>Go to <strong>Also deliver to</strong>, select <strong>Add more recipients</strong> &gt; <strong>ADD</strong> &gt; Choose <strong>Advanced</strong>:
<ul>
<li>Under <strong>Envelope recipient</strong>, select <strong>Change envelope recipient</strong> &gt; <strong>Replace recipient</strong> &gt; Enter the service address. This is the service address you copied and pasted in step 5 when <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/">connecting your domains</a>.
If you did not copy and paste the service address: - In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong>. - Go to <strong>Settings</strong> and locate your domain under <strong>Your domains</strong>. - Select the three dots &gt; <strong>View domain</strong> &gt; <strong>Service address</strong>. Copy and paste the service address.</li>
<li>Under <strong>Spam and delivery options</strong>, ensure <strong>Suppress bounces from this recipient</strong> is not enabled.</li>
<li>Under <strong>Headers</strong>, select <strong>Add X-Gm-Spam and X-Gm-Phishy headers</strong>.</li>
<li>Select <strong>SAVE</strong>.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>In <strong>Account types to affect</strong>, select <strong>Users</strong> and <strong>Groups</strong>.</li>
<li>Select <strong>SAVE</strong>.</li>
</ol>
<p>To verify that BCC rules have been configured successfully:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong> &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Domains</strong> &gt; <strong>View</strong>.</li>
<li>Locate your domain. Under Status, the dashboard should display <strong>Active</strong>. This means that the BCC rules have been configured successfully, and your mail flow is being detected.</li>
</ol>
