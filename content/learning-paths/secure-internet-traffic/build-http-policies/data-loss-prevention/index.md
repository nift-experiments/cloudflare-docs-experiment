---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/data-loss-prevention/
  description: Configure DLP profiles and policies.
  full_title: Build Data Loss Prevention (DLP) policies · Cloudflare Learning Paths
  head_html: <title>Build Data Loss Prevention (DLP) policies · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Configure DLP profiles and policies."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/data-loss-prevention/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/data-loss-prevention/index.md"><meta property="og:title" content="Build Data Loss Prevention (DLP) policies · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure DLP profiles and policies."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/data-loss-prevention/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/data-loss-prevention/#page","headline":"Build Data Loss Prevention (DLP) policies \u00b7 Cloudflare Learning Paths","description":"Configure DLP profiles and policies.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-http-policies/data-loss-prevention/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/build-http-policies/data-loss-prevention/
  schema: 1
---
<p>In order to use Data Loss Prevention (DLP) tools within Cloudflare Zero Trust, you first need to define your DLP profiles. <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> are complex objects with dictionaries, pre-built detections, and custom logic that you can reference as selectors within your Gateway policies.</p>
<h2 id="configure-a-dlp-profile">Configure a DLP profile</h2>
<p>You may either use DLP profiles predefined by Cloudflare, or create your own custom profiles based on regular expressions (regex), predefined detection entries, and DLP datasets.</p>
<h3 id="configure-a-predefined-profile">Configure a predefined profile</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>Choose a <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined profile</a> and select <strong>Edit</strong>.</li>
<li>Enable one or more <strong>Detection entries</strong> according to your preferences.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
<p>Most predefined profiles match when any enabled detection entry matches. The <strong>Personally Identifiable Information (PII) Record</strong> profile is an exception and requires at least three unique detection entries in close proximity before the profile matches.</p>
<h3 id="build-a-custom-profile">Build a custom profile</h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</p>
</li>
<li>
<p>Select <strong>Create profile</strong>.</p>
</li>
<li>
<p>Enter a name and optional description for the profile.</p>
</li>
<li>
<p>Add detection entries to the profile.</p>
<details class="nb-details"><summary>Create a custom entry</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/10190.md")
</div></details>
   <details class="nb-details"><summary>Add existing entries</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10191.md")
</div></details>
<ol start="5">
<li>
<p>(Optional) Add data classes to include reusable classification rules.</p>
<ul>
<li>Select <strong>Add data classes</strong></li>
<li>Choose the data classes you want to add, then select <strong>Confirm</strong></li>
</ul>
</li>
<li>
<p>(Optional) Use labels as match criteria for the profile.</p>
<ul>
<li>Select a sensitivity schema and minimum sensitivity level.</li>
<li>Select a data tag group and one or more data tags.</li>
</ul>
<p>For more information on labels, templates, and data classes, refer to <a href="/cloudflare-one/data-loss-prevention/data-classification/">Data Classification</a>.</p>
</li>
<li>
<p>(Optional) Configure <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/"><strong>profile settings</strong></a> for the profile.</p>
</li>
<li>
<p>Select <strong>Save profile</strong>.</p>
</li>
</ol>
<h2 id="build-effective-dlp-profiles">Build effective DLP profiles</h2>
<p>For many Cloudflare users, Zero Trust is often one of the only measures for preventing the loss of sensitive data. For other users, Zero Trust may be the one of the early in-line measures of a complex Internet and SaaS app security strategy. No matter which model you most resemble, developing effective and appropriate DLP policies and practices starts with first-principles definitions.</p>
<h3 id="define-your-sensitive-data">Define your sensitive data</h3>
<h4 id="existing-data-patterns">Existing data patterns</h4>
<p>If your organization is most concerned about general data patterns that fit existing classifications such as personal identifiable information (PII), protected health information (PHI), financial information, or source code, we recommend using the <a href="#configure-a-predefined-profile">default predefined profiles</a>.</p>
<p>To help this better match the needs of your organization, you can also build a complex profile that matches data to both an existing library and a custom string detection or database. For example:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10194.md")
</div></div>
<h4 id="assorted-data-patterns">Assorted data patterns</h4>
<p>If your data patterns take many different forms and contexts, consider building a custom profile using one or multiple regexes.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="rust-regular-expressions">Rust regular expressions</h3>
@markup("md", "content/.markup/bodies/10189.md")
</aside>
<p>For example, you can use a custom expression to detect when your users share product SKUs in the format <code>CF1234-56789</code>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10197.md")
</div></div>
<h4 id="dlp-datasets">DLP datasets</h4>
<p>If your data is a distinct <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#exact-data-match-datasets">dataset</a> you have defined, you can build a profile by uploading a database to use in an Exact Data Match or Custom Wordlist function. Exact Data Match and Custom Wordlist feature some key differences:</p>
<table>
<thead>
<tr>
<th></th>
<th>Exact Data Match</th>
<th>Custom Wordlist</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Encryption</strong></td>
<td>Hashed and compared to encrypted traffic</td>
<td>Stored as plaintext</td>
</tr>
<tr>
<td><strong>Payload logging</strong></td>
<td>Matches redacted in logs</td>
<td>Matches appear in logs</td>
</tr>
<tr>
<td><strong>Usage</strong></td>
<td>PII (such as names, addresses, and credit card numbers)</td>
<td>Non-sensitive data (such as intellectual property and SKU numbers)</td>
</tr>
</tbody>
</table>
<p>We recommend using Exact Data Match for highly sensitive datasets and Custom Wordlists for lists of keywords.</p>
<p>As your datasets change and grow, we recommend building a pipeline to update the data source in Cloudflare Zero Trust. For more information, contact your account team.</p>
<h4 id="microsoft-information-protection-mip-labels">Microsoft Information Protection (MIP) labels</h4>
<p>If your data already contains Microsoft Information Protection (MIP) labeling schema, Cloudflare can detect those values in-transit automatically. To get started, connect your Microsoft 365 account with a <a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/">CASB integration</a>. Cloudflare will automatically pull in your existing MIP definitions into Zero Trust. You can then use the MIP definitions to build DLP profiles for use in Gateway policies.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles/">Integration profiles</a>.</p>
<h2 id="build-dlp-policies">Build DLP policies</h2>
<p>The best way to start applying data loss prevention to your traffic, minimize the chance of false positives, and collect actionable data is to start with the known knowns in your sensitive data policies. Rather than building policies to detect sensitive data like SSNs or financial information across all of your traffic, you should start by building policies that target both sensitive data types and destinations that are known data sources or points of high risk. These sources can be inside or outside your organization.</p>
<h3 id="example">Example</h3>
<p>Many organizations want to detect and log financial information egressing from user devices to critical SaaS applications. To limit the risk of false positives and to filter out logging noise, Cloudflare recommends building your first series of policies to specify both target data and target destination. For example, you can block financial information from being sent to AI chatbots, such as ChatGPT and Gemini:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10200.md")
</div></div>
<p>Once you have analyzed the flow and magnitude of data from the known sources, you can begin focusing on more specialized or explicit datasets for more generalized sources. You may want to allow sources that are known internal locations where sensitive data is intentionally transferred.</p>
<p>After developing a level of confidence from reviewing the logs and evaluating a rate of false positives for both types of policies, you can feel more confident in experimenting more broadly with data loss prevention policies.</p>
