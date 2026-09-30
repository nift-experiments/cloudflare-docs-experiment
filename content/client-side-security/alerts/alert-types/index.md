---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/alerts/alert-types/
  description: Available alert types for client-side resource detection, including new and malicious scripts.
  full_title: Alert types · Client-side security docs
  head_html: <title>Alert types · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Available alert types for client-side resource detection, including new and malicious scripts."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/alerts/alert-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/alerts/alert-types/index.md"><meta property="og:title" content="Alert types · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available alert types for client-side resource detection, including new and malicious scripts."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/alerts/alert-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Client-side security"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/alerts/alert-types/#page","headline":"Alert types \u00b7 Client-side security docs","description":"Available alert types for client-side resource detection, including new and malicious scripts.","url":"https://developers.cloudflare.com/client-side-security/alerts/alert-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /client-side-security/alerts/alert-types/
  schema: 1
---
<p>You can configure alerts for resources detected in your domain. Refer to <a href="/client-side-security/alerts/">Alerts</a> for more information.</p>
<h2 id="new-resource-alerts">New resource alerts</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4020.md")
</aside>
<p>New resource alerts notify you about new resources detected on your domain, resources detected from new host domains, or issues with the URL length of newly detected resources.</p>
<details><summary>Client-side security New Resources Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when new resources appear in their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered daily. If configured with a zone filter, the alert is triggered immediately.</p>
</details>
<details><summary>Client-side security New Domain Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from new host domains appear in their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered hourly. If configured with a zone filter, the alert is triggered immediately.</p>
</details>
<details><summary>Client-side security New Resource Exceeds Max URL Length Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when a resource's URL exceeds the maximum allowed length.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Manually check the resource.</p>
</details>
<h2 id="code-change-alert">Code change alert</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4019.md")
</aside>
<p>This alert notifies you about <a href="/client-side-security/detection/review-changed-scripts/">code changes</a> in previously detected scripts.</p>
<details><summary>Client-side security New Code Change Detection Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when JavaScript dependencies change in the pages of their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered daily. If configured with a zone filter, the alert is triggered immediately.</p>
</details>
<h2 id="malicious-resource-alerts">Malicious resource alerts</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4018.md")
</aside>
<p>Malicious resource alerts notify you about <a href="/client-side-security/how-it-works/malicious-script-detection/">resources considered malicious</a>, based on their <a href="/client-side-security/how-it-works/malicious-script-detection/#malicious-domain-checks">domain</a>, <a href="/client-side-security/how-it-works/malicious-script-detection/#malicious-url-checks">URL</a>, or <a href="/client-side-security/how-it-works/malicious-script-detection/#malicious-script-detection">script content</a>.</p>
<details><summary>Client-side security New Malicious Domain Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from a known malicious domain appear in their domain. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details>
<details><summary>Client-side security New Malicious URL Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from a known malicious URL appear in their domain. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details>
<details><summary>Client-side security New Malicious Script Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when Cloudflare classifies JavaScript dependencies in their domain as malicious. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details>
<p>Malicious resource alerts will only include resources with an <em>Active</em> status. Refer to <a href="/client-side-security/reference/script-statuses/">Script and connection statuses</a> for more information.</p>
