---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/create-allow-policies/
  description: Configure trusted sender allow policies.
  full_title: Create allow policies · Cloudflare Learning Paths
  head_html: <title>Create allow policies · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Configure trusted sender allow policies."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/create-allow-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/create-allow-policies/index.md"><meta property="og:title" content="Create allow policies · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure trusted sender allow policies."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/create-allow-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/create-allow-policies/#page","headline":"Create allow policies \u00b7 Cloudflare Learning Paths","description":"Configure trusted sender allow policies.","url":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/create-allow-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-your-email/configure-email-security/create-allow-policies/
  schema: 1
---
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
