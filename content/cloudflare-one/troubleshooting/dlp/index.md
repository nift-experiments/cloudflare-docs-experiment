---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/troubleshooting/dlp/
  description: DLP for Zero Trust.
  full_title: DLP · Cloudflare One docs
  head_html: <title>DLP · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="DLP for Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/troubleshooting/dlp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/troubleshooting/dlp/index.md"><meta property="og:title" content="DLP · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="DLP for Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/troubleshooting/dlp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/troubleshooting/dlp/#page","headline":"DLP \u00b7 Cloudflare One docs","description":"DLP for Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/troubleshooting/dlp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/troubleshooting/dlp/
  schema: 1
---
<p>Use this guide to troubleshoot common issues with Data Loss Prevention (DLP).</p>
<h2 id="dlp-policy-does-not-trigger-or-block-content">DLP policy does not trigger or block content</h2>
<p>DLP not inspecting or blocking content is the most common issue reported. If you have configured a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">DLP policy</a> but it fails to inspect or block traffic, the cause is almost always that the traffic is not being decrypted. To use DLP to scan the content of HTTPS requests, you must turn on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a>.</p>
<p>To turn on TLS decryption:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4370.md")
</div></div>
<p>Once you turn on TLS decryption, you can create a DLP policy to inspect the content of HTTPS requests. For example:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>box.com</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Credit card numbers</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="dlp-scans-trigger-false-positives-or-block-legitimate-sites">DLP scans trigger false positives or block legitimate sites</h2>
<p>If your DLP policy is blocking access to business-critical applications (such as Zoho, Google, or internal domains) or generating a high number of false positives, your DLP policy is likely too broad. Profiles such as <strong>Credentials and Secrets</strong> are powerful but can be overly aggressive if not scoped correctly.</p>
<h3 id="problematic-configuration">Problematic configuration</h3>
<p>Applying a sensitive profile to all traffic causes unnecessary blocks. For example:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Credentials and Secrets</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<h3 id="recommended-solution">Recommended solution</h3>
<p>Make your policies more specific. Instead of a catch-all block, create granular policies that target high-risk destinations or user groups.</p>
<p>This policy only blocks uploads of financial data to file-sharing websites for a specific user group, reducing the risk of false positives on other sites.</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination Domain</td>
<td>in</td>
<td><code>dropbox.com</code>, <code>wetransfer.com</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Financial Information</em></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>User Group Names</td>
<td>in</td>
<td><code>Finance Team</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>You can also create policies that match trusted applications using the <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-scan"><strong>Do Not Scan</strong> action</a>.</p>
<h2 id="dlp-detections-are-inconsistent">DLP detections are inconsistent</h2>
<p>If DLP detects sensitive data in plain text but not within images or certain applications, check for the following issues:</p>
<ul>
<li><strong>OCR is turned on</strong>: For DLP to scan text within images (such as a picture of a credit card), you must turn on <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#optical-character-recognition-ocr">Optical Character Recognition (OCR)</a> in the corresponding DLP profile.</li>
<li><strong>Application-specific behavior</strong>: Some applications, such as WhatsApp Web, use protocols or encryption methods (such as WebSockets) that Gateway may not be able to fully inspect with HTTP policies.</li>
<li><strong>Supported file types</strong>: Content must be in a <a href="/cloudflare-one/data-loss-prevention/#supported-file-types">supported file type</a> for DLP inspection.</li>
</ul>
<h2 id="dlp-options-are-missing-or-you-cannot-create-custom-profiles">DLP options are missing or you cannot create custom profiles</h2>
<p>If you cannot use the <em>DLP Profile</em> selector when creating an HTTP policy or are blocked from creating a custom DLP profile, it typically means one of two things:</p>
<ol>
<li>Incorrect plan. These features require a Zero Trust Enterprise plan. If you believe your account should have this entitlement, contact your account team to confirm your subscription details.</li>
<li>Permissions issue. You may not have the required administrative privileges to configure DLP settings. Check with your Cloudflare account administrator.</li>
</ol>
<hr />
<h2 id="more-dlp-resources">More DLP resources</h2>
<p>For more information, refer to the full DLP documentation.</p>
<p><a class="nb-link-button" href="/cloudflare-one/data-loss-prevention/troubleshoot-dlp/">DLP troubleshooting ❯</a></p>
