<p>Email security allows you to configure allow policies. An allow policy exempts messages that match certain patterns from normal detection scanning.</p>
<p>You can choose how Email security will handle messages that match your criteria:</p>
<ul>
<li><strong>Trusted Sender</strong>: Messages will bypass all <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">detections</a> and link following. Typically, it only applies to phishing simulations from vendors such as KnowBe4. Many emails contain links in them. Some of these could be links to surveys, phishing simulations and other trackable links. By marking a message as a Trusted Sender, Email security will not scan any attachments from the sender and will not attempt to open the links in the emails.</li>
<li><strong>Exempt Recipient</strong>: Messages will be exempt from all Email security <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">detections</a> intended for recipients matching this pattern (email address or regular expression only). Typically, this only applies to submission mailboxes for user reporting to security.</li>
<li><strong>Accept Sender</strong>: Messages will exempt messages from the <code>SPAM</code>, <code>SPOOF</code>, and <code>BULK</code> <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">dispositions</a> (but not <code>MALICIOUS</code> or <code>SUSPICIOUS</code>). Commonly used for external domains and sources that send mail on behalf of your organization, such as marketing emails or internal tools.</li>
</ul>
<h2 id="configure-allow-policies">Configure allow policies</h2>
<p>To configure allow policies:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>, then go to <strong>Detection settings</strong> &gt; <strong>Allow policies</strong>.</li>
<li>On the <strong>Detection settings</strong> page, select <strong>Add a policy</strong>.</li>
<li>On the <strong>Add an allow policy</strong> page, enter the policy information:
<ul>
<li><strong>Input method</strong>: Choose between <strong>Manual input</strong>, and <strong>Uploading an allow policy</strong>:
<ul>
<li><strong>Manual input</strong>:
<ul>
<li><strong>Action</strong>: Select one of the following to choose how Email security will handle messages that match your criteria:
<ul>
<li><strong>Trust sender</strong>: Messages will bypass all detections and link following.</li>
<li><strong>Exempt recipient</strong>: Message to this recipient will bypass all detections.</li>
<li><strong>Accept sender</strong>: Messages from this sender will be exempted from Spam, Spoof, and Bulk dispositions.</li>
</ul>
</li>
</ul>
</li>
<li><strong>Rule type</strong>: Specify the scope of your policy. Choose one of the following:
<ul>
<li><strong>Email addresses</strong>: Must be a valid email.</li>
<li><strong>IP addresses</strong>: Can only be IPv4. IPv6 and CIDR are invalid entries.</li>
<li><strong>Domains</strong>: Must be a valid domain.</li>
<li><strong>Regular expressions</strong>: Must be valid Java expressions. Regular expressions are matched with fields related to the sender email address (envelope from, header from, reply-to), the originating IP address, and the server name for the email.</li>
</ul>
</li>
<li><strong>(Recommended) Sender verification</strong>: This option enforces DMARC, SPF, or DKIM authentication. If you choose to enable this option, Email security will only honor policies that pass authentication.
<ul>
<li><strong>Notes</strong>: Provide additional information about your allow policy.</li>
</ul>
</li>
</ul>
</li>
<li><strong>Uploading an allow policy</strong>: Upload a file no larger than 150 KB. The file can only contain <code>Pattern</code>, <code>Notes</code>, <code>Verify Email</code>, <code>Trusted Sender</code>, <code>Exempt Recipient</code>, and <code>Acceptable Sender</code> fields. The first row must be a header row.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
