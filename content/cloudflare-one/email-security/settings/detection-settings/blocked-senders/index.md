---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/
  description: Blocked senders in Email Security.
  full_title: Blocked senders · Cloudflare One docs
  head_html: <title>Blocked senders · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Blocked senders in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/index.md"><meta property="og:title" content="Blocked senders · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Blocked senders in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/#page","headline":"Blocked senders \u00b7 Cloudflare One docs","description":"Blocked senders in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/detection-settings/blocked-senders/
  schema: 1
---
<p>Email security marks all messages from these senders with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a>.</p>
<h2 id="how-blocked-senders-work">How blocked senders work</h2>
<p>Blocked senders ensures messages from any sender is automatically marked as malicious, preventing them from reaching users' inbox.</p>
<p>Sometimes, the same email, IP address or domain always sends malicious emails to the company. In this case, you can add an email address, IP address or domain as a blocked sender. You can choose to enter a regular expression by turning <strong>Regular expression</strong> on.</p>
<h2 id="configure-blocked-senders">Configure blocked senders</h2>
<p>To configure blocked senders:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>, go to <strong>Detection settings</strong> &gt; <strong>Blocked senders</strong>.</li>
<li>On the <strong>Detection settings</strong> page, select <strong>Add a sender</strong>.</li>
<li>Select the <strong>Input method</strong>: Choose between <strong>Manual input</strong>, and <strong>Upload blocked sender list</strong>:
<ul>
<li><strong>Manual input</strong>:
<ul>
<li><strong>Sender type</strong>:
<ul>
<li><strong>Email addresses</strong>: Must be a valid email.</li>
<li><strong>IP addresses</strong>: Can only be IPv4. IPv6 and CIDR are invalid entries.</li>
<li><strong>Domains</strong>: Must be a valid domain.</li>
<li><strong>Regular expressions</strong>: Must be valid Java expressions. Regular expressions are matched with fields related to the sender email address (envelope from, header from, reply-to), the originating IP address, and the server name for the email. For example, you can enter <code>.*@domain\.com</code> to exempt any email address that ends with <code>domain.com</code>.</li>
</ul>
</li>
<li><strong>Notes</strong>: Provide additional information about the blocked sender policy.</li>
</ul>
</li>
<li><strong>Upload blocked sender list</strong>: Upload a file no larger than 150 KB. The file cannot can only contain <code>Blocked_Sender</code>, <code>Pattern Type,</code> and <code>Notes</code> fields. The first row must be a header row. Refer to <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/#csv-uploads">CSV uploads</a> for an example file.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can upload a file no larger than 150 KB. The file cannot can only contain <code>Blocked_Sender</code>, <code>Pattern Type,</code> and <code>Notes</code> fields. The first row must be a header row.</p>
<p>An example file would look like this:</p>
<pre tabindex="0"><code class="language-txt">Blocked Sender, Blocked Sender Type, Is Regex, Notes&#10;john.smith@gmail.com, EMAIL, false, John Smith&#10;example.com, DOMAIN, false, Melanie Turner&#10;</code></pre>
<h2 id="export-blocked-senders">Export blocked senders</h2>
<p>To export all blocked senders:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select <strong>Sender</strong>. Selecting <strong>Sender</strong> will select all blocked senders.</li>
<li>Select <strong>Export to CSV</strong>.</li>
</ol>
<p>To export specific blocked senders:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select <strong>Value(s)</strong>. Select the blocked senders you want to export.</li>
<li>Select <strong>Export to CSV</strong>.</li>
</ol>
<h2 id="edit-a-blocked-sender">Edit a blocked sender</h2>
<p>To edit a blocked sender:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the blocked sender you want to edit.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Edit the blocked sender.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="delete-a-blocked-sender">Delete a blocked sender</h2>
<p>To delete a blocked sender:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, select the blocked sender you want to delete.</li>
<li>Select the three dots &gt; <strong>Delete</strong>.</li>
<li>On the pop up message, select <strong>Delete</strong>.</li>
</ol>
<p>To delete multiple blocked senders at once:</p>
<ol>
<li>On the <strong>Detection settings</strong> page, under <strong>Blocked senders</strong>, select the senders you want to delete.</li>
<li>Select <strong>Action</strong></li>
<li>Select <strong>Delete</strong>.</li>
</ol>
