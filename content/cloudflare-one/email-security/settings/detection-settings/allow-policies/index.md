---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/
  description: Allow policies in Email Security.
  full_title: Allow policies · Cloudflare One docs
  head_html: <title>Allow policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Allow policies in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/index.md"><meta property="og:title" content="Allow policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Allow policies in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/#page","headline":"Allow policies \u00b7 Cloudflare One docs","description":"Allow policies in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/detection-settings/allow-policies/
  schema: 1
---
<p>Email security allows you to configure allow policies. An allow policy exempts messages that match certain patterns from normal detection scanning.</p>
<h2 id="how-allow-policies-work">How allow policies work</h2>
<p>Allow policies are crucial for legitimate messages that may otherwise be blocked due to, for example, an incorrect setup.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-of-allow-policy">Example of allow policy</h3>
@markup("md", "content/.markup/bodies/4936.md")
</div>
<p>Allow policies can be configured to match messages based on specific criteria such as individual email addresses, IP address ranges, or domains. This flexibility allows you to exempt legitimate messages from specific sources, even if those sources have low spam reputation or send bulk messages from their own servers.</p>
<p>Allow policies are used to mitigate false positives. When an email has been marked as malicious or suspicious, but you still want to receive that email, you configure that email as part of an allow policy.</p>
<h3 id="accept-sender">Accept sender</h3>
<p>Allow policies in Email security give you the option to choose <strong>Accept sender</strong>.</p>
<p>Accept sender creates exceptions for messages that would otherwise be marked as spam, bulk, or spoof. However, Email security will continue to scan the message for maliciousness.</p>
<p>It is recommended to choose this option, as it is the safest option to protect your email inbox from malicious or suspicious activities.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-of-a-use-case-where-marketing-emails-that-are-legitimate-have-been-blocked">Example of a use case where marketing emails that are legitimate have been blocked</h3>
@markup("md", "content/.markup/bodies/4937.md")
</div>
<details class="nb-details"><summary>Regular expressions and emails to add as Accept sender</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4938.md")
</div></details>
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
<li><strong>Accept sender</strong>: Messages from this sender will be exempted from Spam, Spoof, and Bulk dispositions. Refer to <a href="#use-case-1">Allow policy configuration use cases</a> for use case examples on how to configure allow policies for accept sender.</li>
</ul>
</li>
</ul>
</li>
<li><strong>Rule type</strong>: Specify the scope of your policy. Choose one of the following:
<ul>
<li><strong>Email addresses</strong>: Must be a valid email. Enter an email address whose emails are going to be exempted.</li>
<li><strong>IP addresses</strong>: This is the IP address of the email server. Any email address sent from this email server is going to be allowed. The IP address can only be IPv4. IPv6 and CIDR are invalid entries.</li>
<li><strong>Domains</strong>: Must be a valid domain.</li>
<li><strong>Regular expressions</strong>: Must be valid Java expressions. Regular expressions are matched with fields related to the sender email address (envelope from, header from, reply-to), the originating IP address, and the server name for the email. For example, you can enter <code>.*@domain\.com</code> to exempt any email address that ends with <code>domain.com</code>.</li>
</ul>
</li>
<li><strong>(Recommended) Sender verification</strong>: This option enforces DMARC, SPF, or DKIM authentication. If you choose to enable this option, Email security will only honor policies that pass authentication.
<ul>
<li><strong>Notes</strong>: Provide additional information about your allow policy.</li>
</ul>
</li>
</ul>
</li>
<li><strong>Uploading an allow policy</strong>: Upload a file no larger than 150 KB. The file can only contain <code>Pattern</code>, <code>Pattern Type</code>, <code>Verify Email</code>, <code>Trusted Sender</code>, <code>Exempt Recipient</code>, <code>Acceptable Sender</code>, <code>Notes</code> fields. The first row must be a header row. Refer to <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/#csv-uploads">CSV uploads</a> for an example file.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<details class="nb-details"><summary>Allow policy configuration use cases</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4942.md")
</div></details>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can upload a file no larger than 150 KB. The file can only contain <code>Pattern</code>, <code>Pattern Type</code>, <code>Verify Email</code>, <code>Trusted Sender</code>, <code>Exempt Recipient</code>, <code>Acceptable Sender</code>, <code>Notes</code>. The first row must be a header row.</p>
<p>An example file would look like this:</p>
<pre tabindex="0"><code class="language-txt">Values, Rule Type, Sender Verification, Trusted Sender, Exempt Recipient, Acceptable Sender, Notes&#10;whale@notaphish.com, EMAIL, true, true, false, true, not a phish&#10;</code></pre>
<h2 id="export-allow-policies">Export allow policies</h2>
<p>To export all allow policies:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select <strong>Value(s)</strong>. Selecting <strong>Value(s)</strong> will select all allow policies.</li>
<li>Select <strong>Export to CSV</strong>.</li>
</ol>
<p>To export specific allow policies:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the allow policies you want to export.</li>
<li>Select <strong>Export to CSV</strong>.</li>
</ol>
<h2 id="edit-allow-policy">Edit allow policy</h2>
<p>To edit an allow policy:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the allow policy you want to edit.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Edit the allow policy.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="delete-allow-policy">Delete allow policy</h2>
<p>To delete an allow policy:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the allow policy you want to delete.</li>
<li>Select the three dots &gt; <strong>Delete</strong>.</li>
<li>On the pop-up message, select <strong>Delete</strong>.</li>
</ol>
<p>To delete multiple allow policies at once:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the allow policies you want to delete.</li>
<li>Select <strong>Action</strong>.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
