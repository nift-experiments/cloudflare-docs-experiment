---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/
  description: User submissions in Email Security.
  full_title: User submissions · Cloudflare One docs
  head_html: <title>User submissions · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="User submissions in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/index.md"><meta property="og:title" content="User submissions · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="User submissions in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/#page","headline":"User submissions \u00b7 Cloudflare One docs","description":"User submissions in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/submissions/user-submissions/
  schema: 1
---
<p>User submissions are the emails your users submitted for submission. User submissions help enhance our detection model, but can be escalated for human review.</p>
<p>Any email that is reported as <a href="/cloudflare-one/email-security/settings/phish-submissions/#reclassify-an-email">phish</a> will be displayed under <strong>User submissions</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4913.md")
</aside>
<h2 id="view-user-submissions">View user submissions</h2>
<p>To view user submissions:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong> &gt; <strong>Submissions</strong>.</li>
<li>Select <strong>User submissions</strong>.</li>
</ol>
<h2 id="filter-user-submissions">Filter user submissions</h2>
<p>Select among the following filters:</p>
<ul>
<li><strong>Date Range</strong>: Select a date range from the last 7, last 30, and last 90 days.</li>
<li><strong>Original disposition</strong>: Select among the <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#available-values">available values</a>.</li>
<li><strong>Submitted as</strong>: Select among the <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#available-values">available values</a>.</li>
</ul>
<p>Once you have selected all the filters, select <strong>Apply filters</strong>.</p>
<p>The dashboard will populate the table with the list of emails your users submitted for submission, including a <strong>Submission ID</strong>, and the <strong>Email subject</strong>.</p>
<h2 id="view-submission-details">View submission details</h2>
<p>To gain more details on a specific submission:</p>
<ol>
<li>Go to the submission you want to have more details for.</li>
<li>Select the three dots &gt; select among <strong>View more</strong>, <strong>View email message</strong>, <strong>View similar details</strong>, and <strong>Escalate</strong>.</li>
</ol>
<h2 id="escalate-a-submission">Escalate a submission</h2>
<p>To escalate a submission:</p>
<ol>
<li>Go to the submission you want to escalate.</li>
<li>Select the three dots &gt; select <strong>Escalate</strong>.</li>
<li>The dashboard will display a message to authorize escalation. Select <strong>Escalate</strong>.</li>
</ol>
