<p>Attackers often try to impersonate executives within an organization when sending malicious emails (with requests about banking information, trade secrets, and more), which is known as a <a href="https://www.cloudflare.com/en-gb/learning/email-security/business-email-compromise-bec/">Business Email Compromise (BEC)</a> attack.</p>
<p>The impersonation registry protects against these attacks by looking for spoofs of known key users in an organization. Information about key users you either synced with your directory or entered manually in the dashboard is used by Email security to run enhanced scan techniques and find these spoofed emails.</p>
<p>To add a user to the impersonation registry:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Impersonation registry</strong>.</li>
<li>Select <strong>Add a user</strong>.</li>
<li>Select <strong>Input method</strong>: Choose between <strong>Manual input</strong>, <strong>Upload manual list</strong>, and <strong>Select from existing directories</strong>:
<ul>
<li><strong>Manual input</strong>: Enter the following information:
<ul>
<li><strong>User info</strong>: enter a valid <strong>Display name</strong>.</li>
<li><strong>User email</strong>: Enter one of the following:
<ul>
<li><strong>Email address</strong>: Enter all known email addresses, separated by a comma.</li>
<li><strong>Regular expressions</strong>: Must be valid Java expressions.</li>
</ul>
</li>
</ul>
</li>
<li><strong>Upload manual list</strong>: You can upload a file no larger than 150 KB containing all variables of potential emails. The file must contain <code>Display_Name</code> and <code>Email</code>, and the first row must be the header row.</li>
<li><strong>Select from existing directories</strong>:
<ul>
<li><strong>Select directory</strong>: Select your directory.</li>
<li><strong>Add users or groups</strong>: Choose the users or groups you want to register.</li>
</ul>
</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>For more information on how to edit and remove users, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/#edit-users">Impersonation Registry</a>.</p>
