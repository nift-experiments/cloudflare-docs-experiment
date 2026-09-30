---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/
  description: Deploy Email Security as the MX record for Office 365 inline email protection.
  full_title: Deploy and configure Microsoft Office 365 with Email security (formerly Area 1) as the MX Record · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Deploy and configure Microsoft Office 365 with Email security (formerly Area 1) as the MX Record · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Email Security as the MX record for Office 365 inline email protection."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/index.md"><meta property="og:title" content="Deploy and configure Microsoft Office 365 with Email security (formerly Area 1) as the MX Record · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Email Security as the MX record for Office 365 inline email protection."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/inline/setup/office-365-area1-mx/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8536.md")
</aside>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/office365-mx.png" alt="A schematic showing where Email security is in the life cycle of an email received" /></p>
<p>In this tutorial, you will learn how to configure Microsoft Office 365 with Email security as its MX record. This tutorial is broken down into several steps. If at any steps during this tutorial you receive a message saying that you need to run the <code>Enable-OrganizationCustomization</code> cmdlet, <a href="#6-execute-enable-organizationcustomization-if-required">refer to section 6</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8535.md")
</aside>
<p>For the purposes of this guide, Office 365 and Microsoft 365 are equivalent.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/8534.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>To ensure changes made in this tutorial take effect quickly, update the Time to Live (TTL) value of the existing MX records on your domains to five minutes. Do this on all the domains you will be deploying.</p>
<p>Changing the TTL value instructs DNS servers on how long to cache this value before requesting an update from the responsible nameserver. You need to change the TTL value before changing your MX records to Cloudflare Email Security (formerly Area 1). This will ensure that changes take effect quickly and can also be reverted quickly if needed. If your DNS manager does not allow for a TTL of five minutes, set it to the lowest possible setting.</p>
<p>To check your existing TTL, open a terminal window and run the following command against your domain:</p>
<pre tabindex="0"><code class="language-sh">dig mx &lt;YOUR_DOMAIN&gt;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#10;; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; mx &lt;YOUR_DOMAIN&gt;&#10;;; global options: +cmd&#10;;; Got answer:&#10;;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 39938&#10;;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1&#10;&#10;;; OPT PSEUDOSECTION:&#10;; EDNS: version: 0, flags:; udp: 4096&#10;;; QUESTION SECTION:&#10;;domain.		IN	MX&#10;&#10;;; ANSWER SECTION:&#10;&lt;YOUR_DOMAIN&gt;.	300	IN	MX	5 mailstream-central.mxrecord.mx.&#10;&lt;YOUR_DOMAIN&gt;.	300	IN	MX	10 mailstream-east.mxrecord.io.&#10;&lt;YOUR_DOMAIN&gt;.	300	IN	MX	10 mailstream-west.mxrecord.io.&#10;</code></pre>
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
<li>
<p>Go to the <a href="https://security.microsoft.com/homepage">Microsoft Security admin center</a>.</p>
</li>
<li>
<p>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; Rules</strong> &gt; <strong>Threat policies</strong>.</p>
</li>
<li>
<p>Select the <a href="https://security.microsoft.com/antispam">Anti-spam option</a>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step3-anti-spam.png" alt="Select the anti-spam option" /></p>
</div>
<ol start="4">
<li>Select <strong>Connection filter policy (Default)</strong> &gt; <strong>Edit connection filter policy</strong>.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step4-edit-filter-policy.png" alt="Select edit connection filter policy" /></p>
</div>
<ol start="5">
<li>In <strong>Always allow messages from the following IP addresses or address range</strong> add the IP addresses and CIDR blocks mentioned in <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs</a>.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step5-egress-ips.png" alt="Enter the egress IP addresses" /></p>
</div>
<ol start="6">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Microsoft recommends disabling SPF Hard fail when an email solution is placed in front of it. Return to the <a href="https://security.microsoft.com/antispam">Anti-spam option</a>.</p>
</li>
<li>
<p>Select <strong>Anti-spam inbound policy (Default)</strong>.</p>
</li>
<li>
<p>At the end of the <strong>Bulk email threshold &amp; spam properties</strong> section, select <strong>Edit spam threshold and properties</strong>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step9-spam-threshold.png" alt="Select the spam threshold and properties button" /></p>
</div>
<ol start="10">
<li>Scroll to <strong>Mark as spam</strong> &gt; <strong>SPF record: hard fail</strong>, and ensure it is set to <strong>Off</strong>.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step10-spf-record-hard-fail.png" alt="Make sure SPF record: hard fail is set to off" /></p>
</div>
<ol start="11">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="2-enhanced-filtering-configuration"><ol start="2">
<li>Enhanced Filtering configuration</li>
</ol></h2>
<p>This option will allow Office 365 to properly identify the original connecting IP before the message was received by Email security (formerly Area 1). This helps with SPF analysis. This has two steps:</p>
<ul>
<li>Creating an inbound connector.</li>
<li>Enabling the enhanced filtering configuration of the connector.</li>
</ul>
<h3 id="create-an-inbound-connector">Create an inbound connector</h3>
<ol>
<li>
<p>Go to the new <a href="https://admin.exchange.microsoft.com/#/homepage"><strong>Exchange admin center</strong></a>.</p>
</li>
<li>
<p>Select <strong>Mail flow</strong> &gt; <strong>Connectors</strong>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step2-mailflow-conectors.png" alt="Select Connectors from Mail flow" /></p>
</div>
<ol start="3">
<li>
<p>Select <strong>Add a connector</strong>.</p>
</li>
<li>
<p>In <strong>Connection from</strong>, select <strong>Partner organization</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Set the following options:</p>
<ul>
<li><strong>Name</strong> - <code>Email security Inbound Connector</code></li>
<li><strong>Description</strong> - <code>Inbound connector for Enhanced Filtering</code></li>
</ul>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step6-connector-options.png" alt="Enter a name and descriptions for your connector" /></p>
</div>
<ol start="7">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Authenticating sent email</strong>, select <strong>By verifying that the IP address of the sending server matches one of the following IP addresses, which belongs to your partner organization.</strong></p>
</li>
<li>
<p>Enter all of the egress IPs in the <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs</a> page.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step9-egress-ips.png" alt="Enter all of Email security's Egress IPs" /></p>
</div>
<ol start="10">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Security restrictions</strong>, accept the default <strong>Reject email messages if they aren't sent over TLS</strong> setting.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Create connector</strong>.</p>
</li>
</ol>
<h3 id="enable-enhanced-filtering">Enable enhanced filtering</h3>
<p>Now that the inbound connector has been configured, you will need to enable the enhanced filtering configuration of the connector in the <a href="https://security.microsoft.com/homepage">Security admin console</a>.</p>
<ol>
<li>
<p>Go to <a href="https://security.microsoft.com/homepage">Security Admin console</a> &gt; <strong>Email &amp; collaboration</strong> &gt; <strong>Policy &amp; Rules</strong>.</p>
</li>
<li>
<p>Go to <strong>Threat policies</strong> &gt; <strong>Rules</strong>, and select <strong>Enhanced filtering</strong>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step2-enhanced-filtering.png" alt="Go to Enhanced filtering" /></p>
</div>
<ol start="3">
<li>
<p>Select the <code>Email security Inbound Connector</code> that you configured previously to edit its configuration parameters.</p>
</li>
<li>
<p>Select <strong>Automatically detect and skip the last IP address</strong> and <strong>Apply to entire organization</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step3-selectors.png" alt="Select Automatically detect and skip the last IP address, and Apply to entire organization" /></p>
<ol start="5">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-configure-email-security-quarantine-policies"><ol start="3">
<li>Configure Email security quarantine policies</li>
</ol></h2>
<h3 id="select-the-disposition-you-want-to-quarantine">Select the disposition you want to quarantine</h3>
<p>Quarantining messages is a per domain configuration. To modify which domains will have their messages quarantined, access the domain configuration:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon) &gt; <strong>Domains</strong>.</p>
</li>
<li>
<p>Locate the domain you want to edit.</p>
</li>
<li>
<p>Select the <strong>...</strong> &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>Select the additional <span class="nb-glossary-tooltip" title="disposition">dispositions</span> you want to quarantine.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step4-area1-dispositions.png" alt="Manage domain quarantines" /></p>
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8533.md")
</aside>
<h3 id="manage-the-admin-quarantine">Manage the Admin Quarantine</h3>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Email</strong> &gt; <strong>Admin Quarantine</strong>.</p>
</li>
<li>
<p>Locate the message you want to manage, and select the <code>...</code> icon next to it. This will let you preview, download, or release the quarantined message.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step4-manage-admin-quarantine.png" alt="Manage admin quarantines" /></p>
</div>
<h2 id="4-message-handling"><ol start="4">
<li>Message handling</li>
</ol></h2>
<p>There may be scenarios where use of the Office 365 (O365) email quarantine or a combination with Email security is preferred. The following are the best practices for using the O365 quarantine <a href="/email-security/reference/dispositions-and-attributes/">by disposition</a>:</p>
<table>
<thead>
<tr>
<th>Disposition</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>MALICIOUS</code></td>
<td>Should always be quarantined. If the user requires notification, they should require administrator approval to release messages. Users should never have the ability to self remediate <code>MALICIOUS</code> emails without approval from an administrator. Emails should be body and subject tagged.</td>
</tr>
<tr>
<td><code>SUSPICIOUS</code></td>
<td>Should not be quarantined. Emails should be body and subject tagged, and delivered to the user’s inbox or junk mail folder. Advantage customers should use <a href="/email-security/email-configuration/email-policies/link-actions/"><code>URL defang</code></a> with this disposition, while all Enterprise customers should always enable <a href="/email-security/email-configuration/email-policies/link-actions/#email-link-isolation">Email Link Isolation</a>.</td>
</tr>
<tr>
<td><code>SPAM</code></td>
<td>Should always be quarantined. If the user requires notification, they may or may not require administrator approval to release emails. Emails should be subject tagged.</td>
</tr>
<tr>
<td><code>BULK</code></td>
<td>Should not be quarantined. Emails should be subject tagged and delivered to the inbox or junk mail folder.</td>
</tr>
<tr>
<td><code>SPOOF</code></td>
<td>If <code>SPOOF</code> detections are clean and well managed <a href="/email-security/email-configuration/lists/">in the Allow List</a>, emails should always be quarantined. If the <code>SPOOF</code> detections are not clean, they should have the same treatment as <code>SPAM</code> dispositions if you have <a href="/email-security/email-configuration/enhanced-detections/">Enhanced Detections</a> configured. If not, <code>SPOOF</code> detections should be treated as <code>BULK</code>. Emails should be body and subject tagged.</td>
</tr>
</tbody>
</table>
<p>Office 365 (O365) has various options, as well as limitations, as to how quarantine email messages. Refer to <a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/">Office 365 use cases</a> for more information.</p>
<p>The Email security dashboard has an <a href="/email-security/email-configuration/admin-quarantine/">Admin quarantine</a>, and you can also use the Office 365 quarantine for when a user quarantine is needed. While there are many quarantine options, the following are the primary use cases the Office 365 <a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/">example tutorials</a> will cover:</p>
<ul>
<li><strong>Use case 1</strong>: Deliver emails to Office 365 junk email folder and Admin Quarantine in Email security (Recommended)</li>
<li><strong>Use case 2</strong>: Deliver emails to junk email folder and user managed quarantine (this use case requires that <code>MALICIOUS</code> emails be quarantined within the Email security dashboard)</li>
<li><strong>Use case 3</strong>: Deliver emails to junk email and administrative quarantine</li>
<li><strong>Use case 4</strong>: Deliver emails to the user managed quarantine and administrative quarantine</li>
<li><strong>Use case 5</strong>: Deliver emails to the user junk email folder and administrative quarantine</li>
</ul>
<h2 id="5-update-your-domain-mx-records"><ol start="5">
<li>Update your domain MX records</li>
</ol></h2>
<p>Instructions to update your MX records will depend on the DNS provider you are using. You will need to update and replace your existing MX record with the Email security hosts. For example:</p>
<table>
<thead>
<tr>
<th>MX Priority</th>
<th>Host</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>5</code></td>
<td><code>mailstream-eu1.mxrecord.io</code></td>
</tr>
<tr>
<td><code>10</code></td>
<td><code>mailstream-central.mxrecord.mx</code></td>
</tr>
<tr>
<td><code>20</code></td>
<td><code>mailstream-east.mxrecord.io</code></td>
</tr>
<tr>
<td><code>20</code></td>
<td><code>mailstream-west.mxrecord.io</code></td>
</tr>
</tbody>
</table>
<p>When configuring the Email Security (formerly Area 1) MX records, it is important to configure hosts with the correct MX priority. This will allow mail flows to the preferred hosts and fail over as needed.</p>
<p>Choose from the following Email Security MX hosts, and order them by priority. For example, if you are located outside the US and want to prioritize email processing in the EU, add <code>mailstream-eu1.mxrecord.io</code> as your first host, and then the US servers.</p>
<table>
<thead>
<tr>
<th>Host</th>
<th>Location</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr>
<td><un><li><code>mailstream-central.mxrecord.mx</code></li> <li><code>mailstream-east.mxrecord.io</code></li> <li><code>mailstream-west.mxrecord.io</code></li></un></td>
<td>US</td>
<td>Best option to ensure all email traffic processing happens in the US.</td>
</tr>
<tr>
<td><code>mailstream-eu1.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens in Germany, with backup to US data centers.</td>
</tr>
<tr>
<td><code>mailstream-bom.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens within India.</td>
</tr>
<tr>
<td><code>mailstream-india-primary.mxrecord.mx</code></td>
<td>India</td>
<td>Same as <code>mailstream-bom.mxrecord.mx</code>, with backup to US data centers.</td>
</tr>
<tr>
<td><code>mailstream-asia.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens in India, with Australia data centers as backup.</td>
</tr>
<tr>
<td><code>mailstream-syd.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens within Australia.</td>
</tr>
<tr>
<td><code>mailstream-australia-primary.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens in Australia, with India and US data centers as backup.</td>
</tr>
</tbody>
</table>
<p>DNS changes will reach the major DNS servers in about an hour or follow the TTL value as described in the <a href="#prerequisites">Prerequisites section</a>.</p>
<h3 id="secure-office-365-from-mx-records-bypass-recommended">Secure Office 365 from MX records bypass (recommended)</h3>
<p>One method of DNS attacks is to search for old MX records and send <span class="nb-glossary-tooltip" title="phishing">phishing</span> emails directly to the mail server. To secure the email flow, you will want to enforce an email flow where inbound messages are accepted by Office 365 only when they originate from Email security. This can be done by adding a connector to only allow email from Email security with TLS encryption. This step is optional but recommended.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/8532.md")
</aside>
<h4 id="configure-domains">Configure domains</h4>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>In <strong>Email Configuration</strong> &gt; <strong>Domains</strong>, make sure each domain you are onboarding has been added.</p>
</li>
<li>
<p>Set the following options for each domain:</p>
<ul>
<li><strong>Domain</strong>: <code>&lt;YOUR_DOMAIN&gt;</code></li>
<li><strong>Configured as</strong>: <code>MX Records</code></li>
<li><strong>Forwarding to</strong>: This should match the expected MX record for each domain in the <a href="https://admin.microsoft.com/#/Domains/">Domains section</a> of Office 365</li>
<li><strong>IP Restrictions</strong>: Leave empty</li>
<li><strong>Outbound TLS</strong>: <code>Forward all messages over TLS</code></li>
<li><strong>Quarantine Policy</strong>: Varies by deployment.</li>
</ul>
</li>
</ol>
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
<p>Select <strong>Connection from</strong> &gt; <strong>Partner organization</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Set the following options:</p>
<ul>
<li><strong>Name</strong> - <code>Secure O365 Inbound</code></li>
<li><strong>Description</strong> - <code>Only accept inbound email from Email security (formerly Area 1)</code></li>
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
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step9-create-conector.png" alt="Enter an asterisk in the text box, and select the plus button" /></p>
</div>
<ol start="10">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Make sure <strong>Reject email messages if they aren't sent over TLS</strong> is selected.</p>
</li>
<li>
<p>Still in the same screen, select <strong>Reject email messages if they aren’t sent from within this IP address range</strong>, and enter all the egress IPs in the <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs page</a>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step12-egress-ips.png" alt="Enter all the egress IPs for Office 365" /></p>
</div>
<ol start="13">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Create connector</strong>.</p>
</li>
</ol>
<h2 id="6-execute-enable-organizationcustomization-if-required">6 Execute <code>Enable-OrganizationCustomization</code> (if required)</h2>
<p>The following steps are only required if you have not previously customized your Office 365 instance. If you received the message to run this cmdlet in any of the previous steps, you will need to execute it in order to proceed with the configuration. This change may take as long as 24 hours to take effect.</p>
<ol>
<li>Run PowerShell as administrator, and execute the following command. Reply <code>Yes</code> when prompted:</li>
</ol>
<pre tabindex="0"><code class="language-powershell">Install-Module ExchangeOnlineManagement&#10;</code></pre>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step1-install-module.png" alt="Run the install-module command in PowerShell" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8531.md")
</aside>
<ol start="2">
<li>Run the following commands to execute the policy change and connect to the Office 365 instance:</li>
</ol>
<pre tabindex="0"><code class="language-powershell">set-executionpolicy remotesigned&#10;</code></pre>
<p>Confirm that you want to execute the policy change, and then run the following command:</p>
<pre tabindex="0"><code class="language-powershell">Import-Module ExchangeOnlineManagement&#10;</code></pre>
<p>Finally, run the following to authenticate against your Office 365 instance:</p>
<pre tabindex="0"><code class="language-powershell">Connect-ExchangeOnline&#10;</code></pre>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step2-set-executionpolicy.png" alt="Run the commands to execute the policy change" /></p>
<ol start="3">
<li>The <code>Connect-ExchangeOnline</code> cmdlet will prompt you to login. Log in using an Office 365 administrator account. Once authenticated, you will be returned to the PowerShell prompt.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step3-connect-exchange.png" alt="Log in with an Office 365 admin account" /></p>
<ol start="4">
<li>You can verify that the <code>OrganizationCustomization</code> is enabled by running the command:</li>
</ol>
<pre tabindex="0"><code class="language-powershell">Get-OrganizationConfig | FL isDehydrated&#10;</code></pre>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step4-get-organizationconfig.png" alt="Run the get-organizationconfig command" /></p>
<p>If the result is <code>false</code>, <code>OrganizationCustomization</code> is already enabled and no further actions are required. If it is true, you need to enable it:</p>
<pre tabindex="0"><code class="language-powershell">Enable-OrganizationCustomization&#10;</code></pre>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/step4-enable-organizationcustomization.png" alt="If the previous result is true, enable the organization customization mode" /></p>
