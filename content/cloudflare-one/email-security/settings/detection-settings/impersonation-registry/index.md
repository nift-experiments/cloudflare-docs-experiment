<p>The impersonation registry contains combinations of emails of users who are likely to be impersonated. If there is an email that is on the impersonation registry not listed as an alternative email address, that email will be reported as potential <a href="https://www.cloudflare.com/en-gb/learning/email-security/business-email-compromise-bec/">business email compromise (BEC)</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4930.md")
</aside>
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
<li><strong>Upload manual list</strong>: You can upload a file no larger than 150 KB containing all variables of potential emails. The file must contain <code>Display_Name</code> and <code>Email</code>, and the first row must be the header row. Refer to <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/#csv-uploads">CSV uploads</a> for an example file.</li>
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
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can upload a file no larger than 150 KB containing all variables of potential emails. The file must contain <code>Display_Name</code> and <code>Email</code>, and the first row must be the header row.</p>
<p>An example file would look like this:</p>
<pre><code class="language-txt">Display Name, Email&#10;Star Phish, star@nophish.com&#10;Phish Ee, phishee@nophish.com&#10;</code></pre>
<h2 id="edit-users">Edit users</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4929.md")
</aside>
<p>To edit users from the Email security directory:</p>
<ol>
<li>Select the user you want to edit.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Enter the <strong>Display name</strong>, <strong>Email</strong> and <strong>Secondary email</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To edit users from other integrations:</p>
<ol>
<li>Select the user you want to edit.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Enter the <strong>Secondary email</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="remove-users">Remove users</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4928.md")
</aside>
<p>To remove a user from the impersonation registry:</p>
<ol>
<li>Select the user you want to remove.</li>
<li>Select the three dots &gt; <strong>Remove from registry</strong>.</li>
<li>Read the pop-up message, then select <strong>Remove user</strong>.</li>
</ol>
<p>To remove multiple users at once from the impersonation registry:</p>
<ol>
<li>Select all the users you want to remove.</li>
<li>Select <strong>Action</strong> &gt; <strong>Remove from registry</strong>.</li>
<li>Read the pop-up message, then select <strong>Remove users</strong>.</li>
</ol>
