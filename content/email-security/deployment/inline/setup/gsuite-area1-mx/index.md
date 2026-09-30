---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/inline/setup/gsuite-area1-mx/
  description: Deploy Email Security as the MX record for Google Workspace inline email protection.
  full_title: Deploy and configure Google Workspace with Email security (formerly Area 1) as MX Record · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Deploy and configure Google Workspace with Email security (formerly Area 1) as MX Record · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Email Security as the MX record for Google Workspace inline email protection."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/gsuite-area1-mx/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/gsuite-area1-mx/index.md"><meta property="og:title" content="Deploy and configure Google Workspace with Email security (formerly Area 1) as MX Record · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Email Security as the MX record for Google Workspace inline email protection."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/inline/setup/gsuite-area1-mx/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/inline/setup/gsuite-area1-mx/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8525.md")
</aside>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/gsuite-area1-mx.png" alt="A schematic showing where Email security is in the life cycle of an email received" /></p>
<p>In this tutorial, you will learn how to configure Google Workspace with Email security as MX record. This tutorial is broken down into several steps.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/8524.md")
</aside>
<h2 id="requirements">Requirements</h2>
<ul>
<li>Provisioned Email security account.</li>
<li>Access to the Google administrator console (<a href="https://admin.google.com"><strong>Google administrator console</strong></a> &gt; <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong>).</li>
<li>Access to the domain nameserver hosting the MX records for the domains that will be processed by Email security.</li>
</ul>
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
<h2 id="1-add-email-security-ip-addresses-to-the-inbound-gateway-configuration"><ol>
<li>Add Email security IP addresses to the Inbound gateway configuration</li>
</ol></h2>
<p>When Email security is deployed as the MX record for Google Workspace, the Inbound gateway needs to be configured such that Google Workspace is aware that it is no longer the MX record for the domain. This is a critical step as it will allow Google Workspace to accept messages from Email security.</p>
<ol>
<li>
<p>Go to the <a href="https://admin.google.com/">Google Administrative Console</a>.</p>
</li>
<li>
<p>Go to <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step2-gmail.png" alt="Access Gmail" /></p>
<ol start="3">
<li>Select <strong>Spam, Phishing, and Malware</strong> and scroll to <strong>Inbound Gateway configuration</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step3-spam.png" alt="Access the spam, phishing and malware setting" /></p>
<ol start="4">
<li>Enable <strong>Inbound Gateway</strong>, and configure it with the following details:</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step4-inbound-gateway.png" alt="Enable inbound gateway" /></p>
<ul>
<li>In <strong>Gateway IPs</strong>, select the <strong>Add</strong> link, and add the IPs mentioned in <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs</a>.</li>
<li>Select <strong>Automatically detect external IP (recommended)</strong>.</li>
<li>Select <strong>Require TLS for connections from the email gateways listed above</strong>.</li>
</ul>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step4-inbound-gateway-settings.png" alt="Inbound gateway settings" /></p>
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8523.md")
</aside>
<ol start="5">
<li>Select the <strong>Save</strong> button at the bottom of the dialog box to save the configuration once the details have been entered. Once saved, the administrator console will show the Inbound Gateway as <strong>enabled</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step5-inbound-on.png" alt="Inbound gateway on" /></p>
<h2 id="2-quarantine-malicious-detections"><ol start="2">
<li>Quarantine malicious detections</li>
</ol></h2>
<p>This optional step is highly recommended to prevent users from being exposed to malicious messages.</p>
<p>When messages are identified as malicious, Email security will insert the X-header <code>X-Area1Security-Disposition</code> into the message with the corresponding <span class="nb-glossary-tooltip" title="disposition">disposition</span>. Based on the value of the <code>X-Area1Security-Disposition</code>, a content compliance filter can be configured to send malicious detections to an administrative quarantine. This section will outline the steps required to:</p>
<ul>
<li>Create an Email security Malicious quarantine.</li>
<li>Create the content compliance filter to send malicious messages to quarantine.</li>
</ul>
<h3 id="create-email-security-malicious-quarantine">Create Email security Malicious Quarantine</h3>
<p>If you would like to send Email security malicious detection to a separate quarantine other than the default quarantine, you will need to create a new quarantine.</p>
<ol>
<li>In <a href="https://admin.google.com">Google's administrative console</a>, select the <strong>Manage quarantines</strong> panel.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step1-manage-quarantines.png" alt="Select the manage quarantines panel" /></p>
<ol start="2">
<li>Select <strong>ADD QUARANTINE</strong> to configure the new quarantine. This will bring up a pop-up for the configuration details.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step2-add-quarantine.png" alt="Select the add quarantine button" /></p>
<ol start="3">
<li>In the quarantine configuration pop-up, enter the following:
<ul>
<li><strong>Name</strong>: <code>Email security Malicious</code>.</li>
<li><strong>Description</strong>: <code>Email security Malicious</code>.</li>
<li>For the <strong>Inbound denial consequence</strong>, select <strong>Drop Message</strong>.</li>
<li>For the <strong>Outbound denial consequence</strong>, select <strong>Drop Message</strong>.</li>
</ul>
</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step3-configure-quarantine.png" alt="Configure the quarantine settings" /></p>
</div>
<p>When you are finished entering these details, select <strong>SAVE</strong>.</p>
<ol>
<li>To access the newly create quarantine, select <strong>GO TO ADMIN QUARANTINE</strong> or access the quarantine directly by pointing your browser to <a href="https://email-quarantine.google.com/adminreview">https://email-quarantine.google.com/adminreview</a>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step4-access-quarantine.png" alt="Access the quarantine created" /></p>
<p>Once in the Admin quarantine console, you can access the <strong>Email security Malicious</strong> quarantine by selecting <strong>Quarantine:ALL</strong> &gt; <strong>Email security Malicious</strong> in the filter section. Quarantined messages can be released as needed by an administrator.</p>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step4-area1.png" alt="Access Email security" /></p>
<h3 id="create-a-content-compliance-filter-to-send-malicious-messages-to-quarantine">Create a content compliance filter to send malicious messages to quarantine</h3>
<ol>
<li>In <a href="https://admin.google.com">Google's administrative console</a>, select <strong>Compliance</strong> to configure the content compliance filter.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step1-compliance.png" alt="Access the compliance configuration" /></p>
<ol start="2">
<li>Go to the <strong>Content compliance</strong> area and select <strong>CONFIGURE</strong> to open the configuration dialog pop-up.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step2-configure.png" alt="Select the configure button" /></p>
<ol start="3">
<li>In the <strong>Content compliance filter</strong> configuration, enter the following:
<ul>
<li><strong>Name</strong>: <code>Quarantine Email security Malicious</code>.</li>
<li>In <strong>1. Email message to affect</strong>, select <strong>Inbound</strong>.</li>
<li>In <strong>2. Add expression that describe the content you want to search for in each message</strong>:
<ul>
<li>Select <strong>Add</strong> to add the condition.
<ul>
<li>In the <em>Simple content match</em> dropdown, select <strong>Advanced content match</strong>.</li>
<li>In <strong>Location</strong>, select <strong>Full headers</strong>.</li>
<li>In <strong>Match type</strong>, select <strong>Contains text</strong>.</li>
<li>In <strong>Content</strong>, enter <code>X-Area1Security-Disposition: MALICIOUS</code>.</li>
</ul>
</li>
<li>Select <strong>SAVE</strong> to save the condition.</li>
</ul>
</li>
<li>In <strong>3. If the above expression match, do the following</strong>, select the <em>Action</em> dropdown. Then choose <strong>Quarantine message</strong> and the <strong>Email security Malicious</strong> quarantine that was created in the previous step.</li>
</ul>
</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step3-compliance-filter.png" alt="Configure the compliance filter" /></p>
</div>
<p>After you enter this information, select <strong>SAVE</strong>.</p>
<ol start="4">
<li>Once saved, the console will update with the newly configured <strong>content compliance filter</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/gsuite-area1-mx/step4-compliance-filter.png" alt="After configuration, the console shows the content compliance filter" /></p>
<p>If you would like to quarantine the other dispositions, repeat the above steps and use the following strings for the other dispositions:</p>
<ul>
<li><code>X-Area1Security-Disposition: MALICIOUS</code></li>
<li><code>X-Area1Security-Disposition: SUSPICIOUS</code></li>
<li><code>X-Area1Security-Disposition: SPOOF</code></li>
<li><code>X-Area1Security-Disposition: UCE</code> (<code>UCE</code> is the equivalent of <code>SPAM</code>)</li>
</ul>
<p>If desired, you can create a separate quarantine for each of the dispositions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8522.md")
</aside>
<h2 id="3-add-your-domain-to-email-security"><ol start="3">
<li>Add your domain to Email security</li>
</ol></h2>
<p>To avoid email loop errors, add your domain to your Email security dashboard.</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/home">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>In <strong>Email Configuration</strong> &gt; <strong>Domains</strong>, select <strong>New Domain</strong>.</li>
<li>Enter the following settings:
<ol>
<li><strong>Domain</strong>: Enter the domain you want Email security to protect.</li>
<li><strong>Configured as</strong>: Select <strong>MX Records</strong>.</li>
<li><strong>Forwarding to</strong>: Add <code>google.com</code>.</li>
<li><strong>Quarantine policy</strong>: Select <strong>Malicious</strong> and <strong>Spam</strong>.</li>
</ol>
</li>
<li>Select <strong>Publish domain</strong>.</li>
</ol>
<h2 id="4-update-your-domain-mx-records"><ol start="4">
<li>Update your domain MX records</li>
</ol></h2>
<p>Instructions to update your MX records will depend on the DNS provider you are using. You need to replace the existing Google MX records with the Email security hosts. For example:</p>
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
<h2 id="5-secure-your-email-flow"><ol start="5">
<li>Secure your email flow</li>
</ol></h2>
<p>After 36 hours, the MX record DNS update will have sufficiently propagated across the Internet. It is now safe to secure your email flow. This will ensure that Google only accepts messages that are first received by Email security. This step is highly recommended to prevent threat actors from using cached MX entries to bypass Email security by injecting messages directly into Gmail.</p>
<ol>
<li>
<p>Access the <a href="https://admin.google.com/">Google Administrative Console</a>, then select <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong>.</p>
</li>
<li>
<p>Select <strong>Spam, Phishing, and Malware</strong>.</p>
</li>
<li>
<p>Go to <strong>Inbound Gateway configuration</strong> and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Enable <strong>Reject all mail not from gateway IPs</strong> and select <strong>Save</strong>.</p>
</li>
<li>
<p>Select <strong>Save</strong> once more to commit and activate the configuration change in the Gmail advanced configuration console.</p>
</li>
</ol>
<h2 id="6-send-email-security-spam-to-user-spam-folder-optional"><ol start="6">
<li>Send Email security spam to user spam folder (optional)</li>
</ol></h2>
<p>Unlike the configuration in <a href="#2-quarantine-malicious-detections">step 2</a> where the message can be sent to an administrative quarantine, this optional step can be configured to send messages that are identified as spam by Email security to the user’s spam folder.</p>
<ol>
<li>
<p>Access <a href="https://admin.google.com/">Google's Administrative Console</a>, then select <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong>.</p>
</li>
<li>
<p>Select <strong>Spam, Phishing, and Malware</strong>.</p>
</li>
<li>
<p>Go to <strong>Inbound Gateway configuration</strong> and select <strong>Configure</strong>.</p>
</li>
<li>
<p>In the <strong>Message Tagging</strong> section, select <strong>Message is considered spam if the following header regexp matches</strong>.</p>
</li>
<li>
<p>In the <strong>Regexp</strong> section, enter the string <code>X-Area1Security-Disposition: UCE</code> (<code>UCE</code> is the equivalent of <code>SPAM</code>).</p>
</li>
<li>
<p>Select <strong>SAVE</strong> to save the updated configuration.</p>
</li>
</ol>
