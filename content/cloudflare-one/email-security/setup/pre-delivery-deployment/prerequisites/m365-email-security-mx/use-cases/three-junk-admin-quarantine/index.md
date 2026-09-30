---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/
  description: Integrate 3 - Junk email and administrative quarantine with Email Security.
  full_title: Junk email and administrative quarantine - Microsoft 365 · Cloudflare One docs
  head_html: <title>Junk email and administrative quarantine - Microsoft 365 · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate 3 - Junk email and administrative quarantine with Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/index.md"><meta property="og:title" content="Junk email and administrative quarantine - Microsoft 365 · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate 3 - Junk email and administrative quarantine with Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/#page","headline":"Junk email and administrative quarantine - Microsoft 365 \u00b7 Cloudflare One docs","description":"Integrate 3 - Junk email and administrative quarantine with Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/
  schema: 1
---
<p>In this tutorial, you will learn how to deliver <code>BULK</code> messages to the users's junk email folder, and <code>MALICIOUS</code>, <code>SPAM</code>, and <code>SPOOF</code> messages to the administrative quarantine (this requires an administrator to release the emails).</p>
<h2 id="create-quarantine-policies">Create quarantine policies</h2>
<p>To create <span class="nb-glossary-tooltip" title="Quarantine policies">quarantine policies</span>:</p>
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
<li>
<p>Select <strong>Save</strong>.</p>
</li>
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
<li>
<p>Set the following conditions and actions (you might need to scroll up or down to find them):</p>
</li>
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
<li><strong>Retain spam in quarantine for this many days</strong>: Default is 15 days. Email security recommends 15-30 days.
<ul>
<li>Select the spam actions in the above step.</li>
</ul>
</li>
</ul>
<ol start="8">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="create-transport-rules">Create transport rules</h2>
<p>To create the transport rules that will send emails with certain <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a> to Email security:</p>
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
<li><strong>Name</strong>: <em><code>Email security Deliver to Junk Email folder</code></em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-CFEmailSecurity-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <code>BULK</code> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</li>
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
<p>Select the rule <code>Email security Deliver to Junk Email folder</code> you have just created, and <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Add a Rule</strong> &gt; <strong>Create a new rule</strong>.</p>
</li>
<li>
<p>Set the following rule conditions:</p>
<ul>
<li><strong>Name</strong>: <em><code>Email security User Quarantine Message</code></em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-CFEmailSecurity-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <em><code>MALICIOUS</code>, <code>UCE</code>, <code>SPOOF</code></em> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</li>
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
<p>Select the rule <em><code>Email security User Quarantine Message</code></em> you have just created, and select <strong>Enable</strong>.</p>
</li>
</ol>
