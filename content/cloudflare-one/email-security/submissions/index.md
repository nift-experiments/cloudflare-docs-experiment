---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/submissions/
  description: Submissions in Email Security.
  full_title: Submissions · Cloudflare One docs
  head_html: <title>Submissions · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Submissions in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/submissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/submissions/index.md"><meta property="og:title" content="Submissions · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Submissions in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/submissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/submissions/#page","headline":"Submissions \u00b7 Cloudflare One docs","description":"Submissions in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/submissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/submissions/
  schema: 1
---
<p>Submitting messages allows you to choose the disposition of your messages if the disposition is incorrect. This helps improve Email security's detection accuracy and ensures proper handling of email threats.</p>
<h2 id="submit-messages-for-review">Submit messages for review</h2>
<p>To submit a message for review:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong> and select <strong>Investigation</strong>.</li>
<li>On the <strong>Investigation</strong> page, under <strong>Your matching messages</strong>, select the message you want to reclassify.</li>
<li>Select the three dots, then select <strong>Submit for review</strong>.</li>
<li>Under <strong>New disposition</strong>, select among the following:
<ul>
<li><strong>Malicious</strong>: Traffic invoked multiple phishing verdict triggers, met thresholds for bad behavior, and is associated with active campaigns.</li>
<li><strong>Spoof</strong>: Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies (SPF, DKIM, DMARC) or has mismatching Envelope From and <code>Header From</code> values.</li>
<li><strong>Spam</strong>: Traffic associated with non-malicious, commercial campaigns.</li>
<li><strong>Bulk</strong>: Traffic associated with <a href="https://en.wikipedia.org/wiki/Graymail_%28email%29">Graymail</a>, that falls in between the definitions of <code>SPAM</code> and <code>SUSPICIOUS</code>. For example, a marketing email that intentionally obscures its unsubscribe link.</li>
<li><strong>Clean</strong>: Traffic not associated with any phishing campaigns.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To submit messages in bulk, select <strong>Select all messages</strong> &gt; <strong>Action</strong> &gt; <strong>Request submissions</strong>.</p>
<p>To release messages in bulk, select <strong>Select all messages</strong> &gt; <strong>Action</strong> &gt; <strong>Release</strong>.</p>
<h2 id="upload-eml-files">Upload EML files</h2>
<p>Email security classifies certain emails as &quot;Clean&quot;. If you disagree with the disposition, you can upload an EML file and reclassify the email.</p>
<p>On the <strong>Investigation</strong> page:</p>
<ol>
<li>Go to the email marked as <strong>Clean</strong>.</li>
<li>Select the three dots &gt; <strong>Submit for review</strong>.</li>
<li>Upload the EML file.</li>
<li>Select a new disposition.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="view-submissions">View submissions</h2>
<p>Once you have submitted your messages, you can access those on <strong>Submissions</strong>.</p>
<p>To view submissions:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong> &gt; <strong>Submissions</strong>.</li>
<li>Choose from the following submission types:
<ul>
<li><a href="/cloudflare-one/email-security/submissions/team-submissions/"><strong>Team submissions</strong></a>: View emails your security team submitted for submissions.</li>
<li><a href="/cloudflare-one/email-security/submissions/user-submissions/"><strong>User submissions</strong></a>: View emails your users submitted for submissions.</li>
<li><a href="/cloudflare-one/email-security/submissions/invalid-submissions/"><strong>Invalid submissions</strong></a>: View submissions that could not be processed.</li>
</ul>
</li>
</ol>
