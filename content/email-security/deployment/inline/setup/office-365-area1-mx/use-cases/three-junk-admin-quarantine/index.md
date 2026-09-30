---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/three-junk-admin-quarantine/
  description: Configure Office 365 to deliver suspicious messages to junk and malicious messages to admin quarantine.
  full_title: Junk email and administrative quarantine - Office 365 · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Junk email and administrative quarantine - Office 365 · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Office 365 to deliver suspicious messages to junk and malicious messages to admin quarantine."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/three-junk-admin-quarantine/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/three-junk-admin-quarantine/index.md"><meta property="og:title" content="Junk email and administrative quarantine - Office 365 · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Office 365 to deliver suspicious messages to junk and malicious messages to admin quarantine."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/three-junk-admin-quarantine/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/inline/setup/office-365-area1-mx/use-cases/three-junk-admin-quarantine/
  schema: 1
---
<p>In this tutorial, you will learn how to deliver <code>SUSPICIOUS</code> and <code>BULK</code> messages to the users's junk email folder, and <code>MALICIOUS</code>, <code>SPAM</code>, and <code>SPOOF</code> messages to the administrative quarantine (this requires an administrator to release the emails).</p>
<h2 id="configure-domains">Configure domains</h2>
<p>You first need to configure the domains you are onboarding on the Email Security (formerly Area 1) dashboard. To configure your domains:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email Security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</li>
<li>Make sure each domain you are onboarding has been added.</li>
<li>For each domain you are configuring, select <strong>...</strong> &gt; <strong>Edit</strong>, and set the following options:
<ul>
<li><strong>Domain</strong> - <code>&lt;YOUR_DOMAIN&gt;</code>.</li>
<li><strong>Configured as</strong> - <code>MX Records</code>.</li>
<li><strong>Forwarding to</strong> - This should match the expected MX record for each domain in your <a href="https://admin.microsoft.com/#/Domains/">Office 365 account</a>.</li>
<li><strong>IP Restrictions</strong> - Leave this field empty.</li>
<li><strong>Outbound TLS</strong> - <code>Forward all messages over TLS</code>.</li>
<li><strong>Quarantine Policy</strong> - Do not check any dispositions.</li>
</ul>
</li>
</ol>
<h2 id="create-quarantine-policies">Create quarantine policies</h2>
<p>To create quarantine policies:</p>
<ol>
<li>
<p>Open the <a href="https://security.microsoft.com/">Microsoft 365 Defender console</a></p>
</li>
<li>
<p>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; rules</strong>.</p>
</li>
<li>
<p>Select <strong>Threat policies</strong>.</p>
</li>
<li>
<p>Under <strong>Rules</strong>, select <strong>Quarantine policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add custom policy</strong>.</p>
</li>
<li>
<p>Set the <strong>Policy name</strong> to <code>UserNotifyAdminRelease</code>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Recipient message access</strong>, select <strong>Set specific access (Advanced)</strong>, and then:</p>
<ul>
<li>In <strong>Select release action preference</strong>, choose <em>Allow recipients to request a message to be released from quarantine</em>.</li>
<li>In <strong>Select additional actions recipients can take on quarantined messages</strong>, select the <strong>Delete</strong> and <strong>Preview</strong> checkboxes.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step8-request-message-release.png" alt="Configure the Recipient message access as stated in the step above" /></p>
<ol start="9">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Quarantine notification</strong>, select <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Submit</strong>.</p>
</li>
<li>
<p>Select <strong>Done</strong>.</p>
</li>
</ol>
<h2 id="configure-quarantine-notifications">Configure quarantine notifications</h2>
<p>To configure quarantine notifications:</p>
<ol>
<li>
<p>Open the <a href="https://security.microsoft.com/">Microsoft 365 Defender console</a>.</p>
</li>
<li>
<p>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; rules</strong>.</p>
</li>
<li>
<p>Select <strong>Threat policies</strong>.</p>
</li>
<li>
<p>Under <strong>Rules</strong>, select <strong>Quarantine policies</strong>.</p>
</li>
<li>
<p>Select <strong>Global settings</strong>.</p>
</li>
<li>
<p>Scroll to the bottom and set the desired frequency in <strong>Send end-user spam notifications every (days)</strong>. This value can only be incremented in days.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step6-spam-notifications.png" alt="Configure the desired spam notification frequency" /></p>
</div>
<ol start="7">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-anti-spam-policies">Configure anti-spam policies</h2>
<p>To configure anti-spam policies:</p>
<ol>
<li>
<p>Open the <a href="https://security.microsoft.com/">Microsoft 365 Defender console</a>.</p>
</li>
<li>
<p>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; rules</strong>.</p>
</li>
<li>
<p>Select <strong>Threat policies</strong>.</p>
</li>
<li>
<p>Under <strong>Policies</strong>, select <strong>Anti-spam</strong>.</p>
</li>
<li>
<p>Select the <strong>Anti-spam inbound policy (Default)</strong> text (not the checkbox).</p>
</li>
<li>
<p>In <strong>Actions</strong>, scroll down and select <strong>Edit actions</strong>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step6-edit-actions.png" alt="Go to Actions and find Edit actions" /></p>
</div>
<ol start="7">
<li>Set the following conditions and actions (you might need to scroll up or down to find them):</li>
</ol>
<ul>
<li><strong>Spam</strong>: <em>Move messages to Junk Email folder</em>.</li>
<li><strong>High confidence spam</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>UserNotifyAdminRelease</em>.</li>
</ul>
</li>
<li><strong>Phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>UserNotifyAdminRelease</em>.</li>
</ul>
</li>
<li><strong>High confidence phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>UserNotifyAdminRelease</em>.</li>
</ul>
</li>
<li><strong>Retain spam in quarantine for this many days</strong>: Default is 15 days. Email Security (formerly Area 1) recommends 15-30 days.
<ul>
<li>Select the spam actions in the above step:</li>
</ul>
</li>
</ul>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/case2-step7-spam.png" alt="Select the spam actions in the above step" /></p>
</div>
<ol start="8">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="create-transport-rules">Create transport rules</h2>
<p>To create the transport rules that will send emails with certain <span class="nb-glossary-tooltip" title="disposition">dispositions</span> to Email Security:</p>
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
<li><strong>Name</strong>: <em><code>Area 1 Deliver to Junk Email folder</code></em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-Area1Security-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <code><code>SUSPICIOUS</code>, <code>BULK</code></code> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs page</a>.</li>
<li><strong>Do the following</strong> - <em><em>Modify the message properties</em> &gt; <em>Set the Spam Confidence Level (SCL)</em> &gt; <em>5</em></em>.</li>
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
<p>Select the rule <code>Area 1 Deliver to Junk Email folder</code> you have just created, and <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Add a Rule</strong> &gt; <strong>Create a new rule</strong>.</p>
</li>
<li>
<p>Set the following rule conditions:</p>
<ul>
<li><strong>Name</strong>: <em><code>Area 1 User Quarantine Message</code></em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-Area1Security-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <em><code>MALICIOUS</code>, <code>UCE</code>, <code>SPOOF</code></em> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs page</a>.</li>
<li><strong>Do the following</strong>: <em><em>Modify the message properties</em> &gt; <em>Set the Spam Confidence Level (SCL)</em> &gt; <em>9</em></em>.</li>
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
<p>Select the rule <em><code>Area 1 User Quarantine Message</code></em> you have just created, and select <strong>Enable</strong>.</p>
</li>
</ol>
