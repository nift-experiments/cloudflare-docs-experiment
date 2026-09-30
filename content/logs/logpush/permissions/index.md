<p>Below is a description of the available permissions for tokens and roles as they relate to Logs. For information about how to create an API token, refer to <a href="/fundamentals/api/get-started/create-token/">Creating API tokens</a>.</p>
<h2 id="tokens">Tokens</h2>
<ul>
<li>
<p><strong>Logs: Read</strong> - Grants read access to logs using Logpull or Instant Logs.</p>
</li>
<li>
<p><strong>Logs: Write</strong> - Grants read and write access to Logpull and Logpush, and read access to Instant Logs. Note that all Logpush API operations require <strong>Logs: Write</strong> permission because Logpush jobs contain sensitive information.</p>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10470.md")
</aside>
<h2 id="roles">Roles</h2>
<p><strong>Super Administrator</strong>, <strong>Administrator</strong> and the <strong>Log Share</strong> roles have full access to Logpull, Logpush and Instant Logs.</p>
<p>Only roles with <strong>Log Share</strong> edit permissions can read and configure Logpush jobs because job configurations may contain sensitive information.</p>
<p>The <strong>Administrator Read only</strong> and <strong>Log Share Reader</strong> roles only have access to Instant Logs and Logpull. This role does not have permissions to view the configuration of Logpush jobs.</p>
<h3 id="zero-trust-datasets">Zero Trust datasets</h3>
<p>To view, create, update, or delete Logpush jobs for Zero Trust datasets (Access, Gateway, and DEX) users must have both the <code>Logs Edit</code> and <code>Zero Trust: PII Read</code> permissions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10469.md")
</aside>
<p>If you encounter the error <code>reading job for product '&lt;product&gt;' is not allowed (1004)</code>, this indicates that the API token you are using does not have the required permissions. Ensure your token or user account has both permissions listed above.</p>
<p>For more details, refer to the <a href="https://developers.cloudflare.com/changelog/2025-11-05-logpush-permissions-update/">Logpush Permission Update for Zero Trust Datasets</a>.</p>
<h3 id="assign-or-remove-a-role">Assign or remove a role</h3>
<p>To check the list of members in your account, or to manage roles and permissions:</p>
<ol>
<li>Navigate to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> and select your account.</li>
<li>From your Account Home, go to <strong>Manage Account</strong> &gt; <strong>Members</strong>.</li>
<li>Enter a member’s email address to add them to your account, and select <strong>Invite</strong>.</li>
<li>Alternatively, scroll down to the <strong>Members</strong> card to find a list of members with their status and role.</li>
</ol>
<p>For more information, refer to <a href="/fundamentals/manage-members/">Managing roles within your Cloudflare account</a>.</p>
