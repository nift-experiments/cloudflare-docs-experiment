---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/
  description: Blocked content rules in Email Security.
  full_title: Blocked content · Cloudflare One docs
  head_html: <title>Blocked content · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Blocked content rules in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/index.md"><meta property="og:title" content="Blocked content · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Blocked content rules in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/#page","headline":"Blocked content \u00b7 Cloudflare One docs","description":"Blocked content rules in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/detection-settings/blocked-content/
  schema: 1
---
<p>Email security allows you to configure blocked content rules that match against the content of incoming messages. When a message matches a rule, Email security marks it with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a>, preventing it from reaching users' inboxes.</p>
<p>Blocked content rules are available for the <strong>Enterprise</strong> and <strong>Enterprise + PhishGuard</strong> Email security packages.</p>
<h2 id="how-blocked-content-works">How blocked content works</h2>
<p>Blocked content rules let you define your own content-based blocking criteria. Each rule specifies a pattern — either a plaintext string or a regular expression — and the part of the message that Email security should scan for it.</p>
<p>You can scan the following fields:</p>
<ul>
<li><strong>Subject</strong>: Match the pattern against the message subject line.</li>
<li><strong>Body</strong>: Match the pattern against the message body.</li>
<li><strong>Subject and body</strong>: Match the pattern against both the subject and the body.</li>
</ul>
<p>If the pattern matches, Email security marks the message as malicious. Blocked content rules only support the block action.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-of-a-blocked-content-rule">Example of a blocked content rule</h3>
@markup("md", "content/.markup/bodies/4934.md")
</div>
<h2 id="configure-a-blocked-content-rule">Configure a blocked content rule</h2>
<p>To create a blocked content rule:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Go to <strong>Policies &amp; rules</strong> &gt; <strong>Blocked content</strong>.</li>
<li>Select <strong>Add a rule</strong>.</li>
<li>Enter the rule information:
<ul>
<li><strong>Name</strong>: A descriptive name for the rule.</li>
<li><strong>Match type</strong>: Choose between:
<ul>
<li><strong>Plaintext</strong>: Email security matches the exact string you enter.</li>
<li><strong>Regular expression</strong>: Email security evaluates the pattern as a regular expression. Regular expressions must be valid Java expressions.</li>
</ul>
</li>
<li><strong>Pattern</strong>: The plaintext string or regular expression to match against.</li>
<li><strong>Search location</strong>: Choose which parts of the message to scan:
<ul>
<li><strong>Subject</strong></li>
<li><strong>Body</strong></li>
<li><strong>Subject and body</strong></li>
</ul>
</li>
<li><strong>Notes</strong> (optional): Provide additional information about the rule.</li>
</ul>
</li>
<li>(Optional) Use the built-in <strong>Regular expression checker</strong> to validate your pattern before saving. The checker lets you test your pattern against sample text to confirm it matches as expected.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="validate-a-regular-expression">Validate a regular expression</h2>
<p>When you choose <strong>Regular expression</strong> as the match type, Email security provides a regular expression checker to help you validate your pattern before saving the rule.</p>
<p>To validate a regular expression:</p>
<ol>
<li>On the <strong>Add a rule</strong> page, select <strong>Regular expression</strong> as the match type.</li>
<li>Enter your regular expression in the <strong>Pattern</strong> field.</li>
<li>In the <strong>Test your expression</strong> field, enter sample text that represents the content you want to match.</li>
<li>Email security displays whether the sample text matches your pattern.</li>
<li>Adjust the pattern as needed and repeat until it behaves as expected.</li>
</ol>
<p>Cloudflare recommends validating every regular expression before saving to avoid false positives and false negatives.</p>
<h2 id="edit-a-blocked-content-rule">Edit a blocked content rule</h2>
<p>To edit a blocked content rule:</p>
<ol>
<li>On the <strong>Blocked content</strong> page, select the rule you want to edit.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Edit the rule.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="delete-a-blocked-content-rule">Delete a blocked content rule</h2>
<p>To delete a blocked content rule:</p>
<ol>
<li>On the <strong>Blocked content</strong> page, select the rule you want to delete.</li>
<li>Select the three dots &gt; <strong>Delete</strong>.</li>
<li>On the pop-up message, select <strong>Delete</strong>.</li>
</ol>
<p>To delete multiple blocked content rules at once:</p>
<ol>
<li>On the <strong>Blocked content</strong> page, select the rules you want to delete.</li>
<li>Select <strong>Action</strong>.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
