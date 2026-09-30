<p><img src="/assets/upstream/email-security/Email_security_M365_MX_Inline.png" alt="A schematic showing where Email security is in the life cycle of an email received" /></p>
<p>In this tutorial, you will learn how to configure Microsoft 365 with Email security as its MX record.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To ensure changes made in this tutorial take effect quickly, update the Time to Live (TTL) value of the existing MX records on your domains to five minutes. Do this on all the domains you will be deploying.</p>
<p>Changing the TTL value instructs DNS servers on how long to cache this value before requesting an update from the responsible nameserver. You need to change the TTL value before changing your MX records to Email security. This will ensure that changes take effect quickly and can also be reverted quickly if needed. If your DNS manager does not allow for a TTL of five minutes, set it to the lowest possible setting.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4962.md")
</aside>
<p>To check your existing TTL, open a terminal window and run the following command against your domain:</p>
<pre><code class="language-sh">dig mx &lt;YOUR_DOMAIN&gt;&#10;</code></pre>
<pre><code class="language-txt">; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; mx &lt;YOUR_DOMAIN&gt;&#10;;; global options: +cmd&#10;;; Got answer:&#10;;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 39938&#10;;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1&#10;&#10;;; OPT PSEUDOSECTION:&#10;; EDNS: version: 0, flags:; udp: 4096&#10;;; QUESTION SECTION:&#10;;&lt;YOUR_DOMAIN&gt;.		IN	MX&#10;&#10;;; ANSWER SECTION:&#10;&lt;YOUR_DOMAIN&gt;.    300    IN    MX    10 mxa.global.inbound.cf-emailsecurity.net.&#10;&lt;YOUR_DOMAIN&gt;.    300    IN    MX    10 mxb.global.inbound.cf-emailsecurity.net.&#10;</code></pre>
<p>In the above example, TTL is shown in seconds as <code>300</code> (or five minutes).</p>
<p>If you are using Cloudflare for DNS, you can leave the <a href="/dns/manage-dns-records/reference/ttl/">TTL setting as <strong>Auto</strong></a>.</p>
<p>Below is a list with instructions on how to edit MX records for some popular services:</p>
<ul>
<li><strong>Cloudflare</strong>: <a href="/dns/manage-dns-records/how-to/email-records/">Set up email records</a></li>
<li><strong>GoDaddy</strong>: <a href="https://www.godaddy.com/help/edit-an-mx-record-19235">Edit an MX Record</a></li>
<li><strong>AWS</strong>: <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html">Creating records by using the Amazon Route 53 console</a></li>
<li><strong>Azure</strong>: <a href="https://learn.microsoft.com/en-us/azure/dns/dns-web-sites-custom-domain">Create DNS records in a custom domain for a web app</a></li>
</ul>
<h2 id="1-add-email-security-ip-addresses-to-allow-list"><ol>
<li>Add Email security IP addresses to Allow List</li>
</ol></h2>
<ol>
<li>Go to the <a href="https://security.microsoft.com/antispam">Anti-spam policies page</a> &gt; Select <strong>Edit connection filter policy</strong>.</li>
<li>In <strong>Always allow messages from the following IP addresses or address range</strong>, add IP addresses and CIDR blocks mentioned in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</li>
<li>Select <strong>Save</strong>.</li>
<li>Microsoft recommends disabling SPF Hard fail when an email solution is placed in front of it:
<ul>
<li>Return to the <a href="https://security.microsoft.com/antispam">Anti-spam option</a>.</li>
<li>Select <strong>Default anti-spam policy</strong>.</li>
<li>Select <strong><a href="https://learn.microsoft.com/en-us/defender-office-365/anti-spam-bulk-complaint-level-bcl-about">Edit spam threshold and properties</a></strong> &gt; <strong>Mark as spam</strong> &gt; <strong>SPF record: hard fail</strong>, and ensure it is set to <strong>Off</strong>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="2-configure-enhanced-filtering"><ol start="2">
<li>Configure Enhanced Filtering</li>
</ol></h2>
<h3 id="create-an-inbound-connector">Create an inbound connector</h3>
<ol>
<li><a href="https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-to-route-mail#1-set-up-a-connector-from-your-email-server-to-microsoft-365-or-office-365">Set up a connector</a>.</li>
<li>Select <strong>Partner organization</strong> under <strong>Connection from</strong>.
<ul>
<li>Provide a name for the connector:
<ul>
<li><strong>Name</strong>: <code>Email security Inbound Connector</code></li>
<li><strong>Description</strong>: <code>Inbound connector for Enhanced Filtering</code></li>
</ul>
</li>
</ul>
</li>
<li>In <strong>Authenticating sent email</strong>, select <strong>By verifying that the IP address of the sending server matches one of the following IP addresses, which belongs to your partner organization.</strong></li>
<li>Enter all of the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</li>
<li>In <strong>Security restrictions</strong>, accept the default <strong>Reject email messages if they aren't sent over TLS</strong> setting.</li>
</ol>
<h3 id="enable-enhanced-filtering">Enable enhanced filtering</h3>
<p>Now that the inbound connector has been configured, you will need to enable the enhanced filtering configuration of the connector.</p>
<ol>
<li>Go to the <a href="https://security.microsoft.com/homepage">Security admin console</a>, and <a href="https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/enhanced-filtering-for-connectors#use-the-microsoft-defender-portal-to-configure-enhanced-filtering-for-connectors-on-an-inbound-connector">enable enhanced filtering</a>.</li>
<li>Select <strong>Automatically detect and skip the last IP address</strong> and <strong>Apply to entire organization</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-configure-anti-spam-policies"><ol start="3">
<li>Configure anti-spam policies</li>
</ol></h2>
<p>To configure anti-spam policies:</p>
<ol>
<li>Open the <a href="https://security.microsoft.com/">Microsoft 365 Defender console</a>.</li>
<li>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; rules</strong>.</li>
<li>Select <strong>Threat policies</strong>.</li>
<li>Under <strong>Policies</strong>, select <strong>Anti-spam</strong>.</li>
<li>Select the <strong>Anti-spam inbound policy (Default)</strong> text (not the checkbox).</li>
<li>In <strong>Actions</strong>, scroll down and select <strong>Edit actions</strong>.</li>
<li>Set the following conditions and actions (you might need to scroll up or down to find them):</li>
</ol>
<ul>
<li><strong>Spam</strong>: <em>Move messages to Junk Email folder</em>.</li>
<li><strong>High confidence spam</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>AdminOnlyAccessPolicy</em>.</li>
</ul>
</li>
<li><strong>Phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>AdminOnlyAccessPolicy</em>.</li>
</ul>
</li>
<li><strong>High confidence phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>AdminOnlyAccessPolicy</em>.</li>
</ul>
</li>
<li><strong>Retain spam in quarantine for this many days</strong>: Default is 15 days. Email security recommends 15-30 days.
<ul>
<li>Select the spam actions in the above step:</li>
</ul>
</li>
</ul>
<ol start="8">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="4-create-transport-rules"><ol start="4">
<li>Create transport rules</li>
</ol></h2>
<p>To create the transport rules that will send emails with certain <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">dispositions</a> to Email security:</p>
<ol>
<li>
<p>Open the new <a href="https://admin.exchange.microsoft.com/#/homepage">Exchange admin center</a>.</p>
</li>
<li>
<p>Go to <strong>Mail flow</strong> &gt; <strong>Rules</strong>.</p>
</li>
<li>
<p>Select <strong>Add a Rule</strong> &gt; <strong>Create a new rule</strong>.</p>
</li>
<li>
<p>Set the following rule conditions:</p>
<ul>
<li><strong>Name</strong>: <em>Email Security Deliver to Junk Email folder</em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-CFEmailSecurity-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <code>BULK</code> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs mentioned in <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/" target="_blank">Egress IPs</a>.</li>
<li><strong>Do the following</strong> - <em>Modify the message properties</em> &gt; <em>Set the Spam Confidence Level (SCL)</em> &gt; <em>5</em>.</li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>You can use the default values on this screen. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Finish</strong> &gt; <strong>Done</strong>.</p>
</li>
<li>
<p>Select the rule <strong>Email security Deliver to Junk Email folder</strong> you have just created, and <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Add a Rule</strong> &gt; <strong>Create a new rule</strong>.</p>
</li>
<li>
<p>Set the following rule conditions:</p>
<ul>
<li><strong>Name</strong>: <code>Email security Deliver to Junk Email folder</code>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-CFEmailSecurity-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <code>MALICIOUS</code>, <code>UCE</code>, <code>SPOOF</code> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/" target="_blank">Egress IPs</a>.</li>
<li><strong>Do the following</strong>: <em>Redirect the message to</em> &gt; <em>hosted quarantine</em>.</li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>You can use the default values on this screen. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Finish</strong> &gt; <strong>Done</strong>.</p>
</li>
<li>
<p>Select the rule you have just created, and select <strong>Enable</strong>.</p>
</li>
</ol>
<h2 id="5-set-up-mx-inline"><ol start="5">
<li>Set up MX/Inline</li>
</ol></h2>
<p>Now that you have completed the prerequisite steps, set up MX/Inline on the Cloudflare dashboard. Refer to <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/">Set up MX/Inline deployment</a> for the next steps.</p>
<h2 id="6-recommended-secure-microsoft-365-from-mx-records-bypass"><ol start="6">
<li>(Recommended) Secure Microsoft 365 from MX records bypass</li>
</ol></h2>
<p>One method of a DNS attack is to search for old MX records and send <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4963.md")
</div> emails directly to the mail server. To secure the email flow, you should enforce an email flow where inbound messages are accepted by Microsoft 365 only when they originate from Email security. This can be done by adding a connector to only allow email from Email security with TLS encryption. This step is optional but recommended.
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4961.md")
</aside>
<h4 id="create-connector">Create Connector</h4>
<ol>
<li>
<p>Go to the new <a href="https://admin.exchange.microsoft.com/#/homepage">Exchange admin center</a>.</p>
</li>
<li>
<p>Go to <strong>Mail flow</strong> &gt; <strong>Connectors</strong>.</p>
</li>
<li>
<p>Select <strong>Add a connector</strong>.</p>
</li>
<li>
<p>Go to <strong>Connection from</strong> &gt; <strong>Partner organization</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Set the following options:</p>
<ul>
<li><strong>Name</strong> - <code>Secure M365 Inbound</code></li>
<li><strong>Description</strong> - <code>Only accept inbound email from Email security</code></li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Make sure <strong>By Verifying that the sender domain matches one of the following domains</strong> is selected.</p>
</li>
<li>
<p>Enter <code>*</code> in the text field, and select <strong>+</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Make sure <strong>Reject email messages if they aren't sent over TLS</strong> is selected.</p>
</li>
<li>
<p>Still in the same screen, select <strong>Reject email messages if they aren't sent from within this IP address range</strong>, and enter all the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Create connector</strong>.</p>
</li>
</ol>
