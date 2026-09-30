---
cp9:
  canonical: https://developers.cloudflare.com/email-service/configuration/suppressions/
  description: Manage account-wide Email Sending suppression entries.
  full_title: Manage suppressions · Cloudflare Email Service docs
  head_html: <title>Manage suppressions · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage account-wide Email Sending suppression entries."><link rel="canonical" href="https://developers.cloudflare.com/email-service/configuration/suppressions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/configuration/suppressions/index.md"><meta property="og:title" content="Manage suppressions · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage account-wide Email Sending suppression entries."><meta property="og:url" content="https://developers.cloudflare.com/email-service/configuration/suppressions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/configuration/suppressions/#page","headline":"Manage suppressions \u00b7 Cloudflare Email Service docs","description":"Manage account-wide Email Sending suppression entries.","url":"https://developers.cloudflare.com/email-service/configuration/suppressions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/configuration/suppressions/
  schema: 1
---
<p>Manage recipients that Email Service must not contact. For suppression triggers and expiration rules, refer to <a href="/email-service/concepts/suppressions/">Suppression lists</a>.</p>
<p>The dashboard and API are account-scoped. Entries apply to every sending domain and subdomain in the account.</p>
<h2 id="view-suppressions">View suppressions</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8612.md")
</div>
<p>The table displays each recipient, reason, creation time, and expiration. <strong>Never</strong> means the entry has no scheduled expiration.</p>
<h2 id="add-a-suppression">Add a suppression</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8613.md")
</div>
<p>Entries created in the dashboard have the <code>manual</code> reason. They apply to every sending domain in the account.</p>
<h2 id="import-suppressions">Import suppressions</h2>
<p>You can paste addresses or upload <code>.csv</code>, <code>.json</code>, or <code>.txt</code> files. Supported file contents are:</p>
<ul>
<li><code>.csv</code> or <code>.txt</code>: Put one entry on each line as <code>&lt;EMAIL_ADDRESS&gt;</code> or <code>&lt;EMAIL_ADDRESS&gt;,&lt;EXPIRATION_TIMESTAMP&gt;</code>. Use an <a href="https://datatracker.ietf.org/doc/html/rfc3339">RFC 3339</a> timestamp and omit the header row.</li>
<li><code>.json</code>: Use an array of address strings or objects. Each object requires <code>email</code> and can include an RFC 3339 <code>expires_at</code> timestamp.</li>
</ul>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8614.md")
</div>
<h2 id="remove-a-suppression">Remove a suppression</h2>
<p>To remove a mutable entry, select <strong>Delete</strong> for that recipient. Read-only entries do not provide a delete action.</p>
<p>Deleting an entry permits future delivery attempts. Verify that the recipient should receive mail before deleting an automatic suppression.</p>
<h2 id="use-the-api">Use the API</h2>
<p>The <a href="/api/resources/email_sending/subresources/suppressions/">account Email Sending suppression management REST API</a> supports listing, adding, importing, updating, and deleting entries. Requests require an <a href="/fundamentals/api/get-started/create-token/">API token</a> with the <strong>Email Sending: Edit</strong> permission.</p>
<p>API clients must use <code>read_only</code> to determine whether an entry is mutable. Do not infer mutability from the <code>reason</code> value.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8611.md")
</aside>
<h2 id="limits">Limits</h2>
<p>Each account can have one active entry per address. For page size, import, and rate limits, refer to <a href="/email-service/platform/limits/#suppression-list-limits">Suppression list limits</a>.</p>
