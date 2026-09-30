---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/
  description: How Scan for sensitive data works in Cloudflare One.
  full_title: Scan for sensitive data · Cloudflare One docs
  head_html: <title>Scan for sensitive data · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Scan for sensitive data works in Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/index.md"><meta property="og:title" content="Scan for sensitive data · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Scan for sensitive data works in Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/#page","headline":"Scan for sensitive data \u00b7 Cloudflare One docs","description":"How Scan for sensitive data works in Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/cloud-and-saas-findings/casb-dlp/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4533.md")
</aside>
<p>You can use <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a> to discover if files stored in a SaaS application contain sensitive data. To perform DLP scans in a SaaS app, first configure a <a href="#configure-a-dlp-profile">DLP profile</a> (a set of patterns that define what counts as sensitive data) with the data patterns you want to detect, then <a href="#enable-dlp-scans-in-casb">add the profile</a> to a CASB integration.</p>
<h2 id="supported-integrations">Supported integrations</h2>
<ul>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/">Amazon Web Services (AWS) S3</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/box/">Box</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/dropbox/">Dropbox</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/gcp-cloud-storage">Google Cloud Platform (GCP) Cloud Storage</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive/">Google Drive</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/onedrive/">Microsoft OneDrive</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint/">Microsoft SharePoint</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/">Microsoft 365 Copilot</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/openai/">OpenAI</a></li>
<li><a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">Anthropic</a></li>
</ul>
<h2 id="configure-a-dlp-profile">Configure a DLP profile</h2>
<p>You may either use DLP profiles predefined by Cloudflare, or create your own custom profiles based on regex, predefined detection entries, datasets, and document fingerprints.</p>
<h3 id="configure-a-predefined-profile">Configure a predefined profile</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>Choose a <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined profile</a> and select <strong>Edit</strong>.</li>
<li>Enable one or more <strong>Detection entries</strong> according to your preferences.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
<p>Most predefined profiles match when any enabled detection entry matches. The <strong>Personally Identifiable Information (PII) Record</strong> profile is an exception and requires at least three unique detection entries in close proximity before the profile matches.</p>
<p>Your DLP profile is now ready to use with CASB.</p>
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
@markup("md", "content/.markup/bodies/4534.md")
</div></details>
   <details class="nb-details"><summary>Add existing entries</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4535.md")
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
<p>Your DLP profile is now ready to use with CASB.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Configure a DLP profile</a>.</p>
<h2 id="enable-dlp-scans-in-casb">Enable DLP scans in CASB</h2>
<h3 id="add-a-new-integration">Add a new integration</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS</strong>.</li>
<li>Select <strong>Add integration</strong> and choose a <a href="#supported-integrations">supported integration</a>.</li>
<li>During the setup process, you are prompted to select DLP profiles for the integration.</li>
<li>Select <strong>Save integration</strong>.</li>
</ol>
<p>CASB will scan every publicly accessible file in the integration for text that matches the DLP profile. The initial scan may take up to a few hours to complete.</p>
<h3 id="modify-an-existing-integration">Modify an existing integration</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS</strong>.</li>
<li>Choose a <a href="#supported-integrations">supported integration</a> and select <strong>Configure</strong>.</li>
<li>Under <strong>DLP profiles</strong>, select the profiles that you want the integration to scan for.</li>
<li>Select <strong>Save integration</strong>.</li>
</ol>
<p>If you enable a DLP profile from the <strong>Manage integrations</strong> page, CASB will only scan publicly accessible files that have had a modification event since enabling the DLP profile. Modification events include changes to the following attributes:</p>
<ul>
<li>Contents of the file</li>
<li>Name of the file</li>
<li>Visibility of the file (only if changed to publicly accessible)</li>
<li>Owner of the file</li>
<li>Location of the file (for example, moved to a different folder)</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4532.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>DLP in CASB will only scan:</p>
<ul>
<li><a href="/cloudflare-one/data-loss-prevention/#supported-file-types">Text-based files</a> such as documents, spreadsheets, and PDFs. Images are not supported.</li>
<li>Files less than or equal to 100 MB in size.</li>
<li>Java and R source code files that are at least 5 KB. Smaller files in these languages are skipped.</li>
</ul>
