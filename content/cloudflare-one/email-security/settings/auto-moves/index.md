<p>Auto-moves allow you to automatically move emails out of your inbox based on a <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> that Email security assigns to each message (for example, malicious, spam, or spoof).</p>
<p>Use auto-moves to enforce email security policy without relying on end users to identify and act on threats themselves. After you configure auto-moves, Email security handles flagged messages according to the action you choose for each disposition.</p>
<p>To configure auto-move events:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>Select <strong>Moves</strong>.</li>
<li>Under <strong>Auto-moves</strong>, select <strong>Configure</strong>.</li>
<li>For each disposition (malicious, spam, bulk, suspicious, spoof), choose what happens to matching emails:
<ul>
<li><strong>Soft delete - user recoverable</strong>: Moves the message to the user's <strong>Recoverable Items - Deleted</strong> folder. The user can still find and restore the message. This option is only available for Microsoft 365 customers. Refer to <a href="https://learn.microsoft.com/en-us/compliance/assurance/assurance-exchange-online-data-deletion">Microsoft 365 Exchange data deletion</a> for more information.</li>
<li><strong>Hard delete - admin recoverable</strong>: Removes the message from the user's inbox entirely. Only an administrator can recover it.</li>
<li><strong>Move to trash</strong>: Moves the message to the user's trash or deleted items folder. This option is only available for Google Workspace users.</li>
<li><strong>Move to junk</strong>: Moves the message to the user's junk or spam folder.</li>
<li><strong>No action</strong>: Leaves the message where it is. Email security still records the disposition, but does not move the message.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
