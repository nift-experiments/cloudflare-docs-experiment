---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/impersonation-registry/
  description: Protect executives from BEC impersonation attacks.
  full_title: Add user to the impersonation registry · Cloudflare Learning Paths
  head_html: <title>Add user to the impersonation registry · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Protect executives from BEC impersonation attacks."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/impersonation-registry/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/impersonation-registry/index.md"><meta property="og:title" content="Add user to the impersonation registry · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect executives from BEC impersonation attacks."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/impersonation-registry/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/impersonation-registry/#page","headline":"Add user to the impersonation registry \u00b7 Cloudflare Learning Paths","description":"Protect executives from BEC impersonation attacks.","url":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/impersonation-registry/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-your-email/configure-email-security/impersonation-registry/
  schema: 1
---
<p>Attackers often try to impersonate executives within an organization when sending malicious emails (with requests about banking information, trade secrets, and more), which is known as a <a href="https://www.cloudflare.com/en-gb/learning/email-security/business-email-compromise-bec/">Business Email Compromise (BEC)</a> attack.</p>
<p>The impersonation registry protects against these attacks by looking for spoofs of known key users in an organization. Information about key users you either synced with your directory or entered manually in the dashboard is used by Email security to run enhanced scan techniques and find these spoofed emails.</p>
<p>To add a user to the impersonation registry:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Impersonation registry</strong>.</li>
<li>Select <strong>Add a user</strong>.</li>
<li>Select <strong>Input method</strong>: Choose between <strong>Manual input</strong>, <strong>Upload manual list</strong>, and <strong>Select from existing directories</strong>:
<ul>
<li><strong>Manual input</strong>: Enter the following information:
<ul>
<li><strong>User info</strong>: enter a valid <strong>Display name</strong>.</li>
<li><strong>User email</strong>: Enter one of the following:
<ul>
<li><strong>Email address</strong>: Enter all known email addresses, separated by a comma.</li>
<li><strong>Regular expressions</strong>: Must be valid Java expressions.</li>
</ul>
</li>
</ul>
</li>
<li><strong>Upload manual list</strong>: You can upload a file no larger than 150 KB containing all variables of potential emails. The file must contain <code>Display_Name</code> and <code>Email</code>, and the first row must be the header row.</li>
<li><strong>Select from existing directories</strong>:
<ul>
<li><strong>Select directory</strong>: Select your directory.</li>
<li><strong>Add users or groups</strong>: Choose the users or groups you want to register.</li>
</ul>
</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>For more information on how to edit and remove users, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/#edit-users">Impersonation Registry</a>.</p>
