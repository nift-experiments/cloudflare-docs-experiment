---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/
  description: Create and manage detection entries in Cloudflare One.
  full_title: Configure detection entries · Cloudflare One docs
  head_html: <title>Configure detection entries · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage detection entries in Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/index.md"><meta property="og:title" content="Configure detection entries · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage detection entries in Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#page","headline":"Configure detection entries \u00b7 Cloudflare One docs","description":"Create and manage detection entries in Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/
  schema: 1
---
<p>Detection entries are the reusable detection logic that Cloudflare DLP uses to identify sensitive content in your web traffic and SaaS applications. You can create and manage detection entries independently of <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a>, then add the same entry to one or more custom profiles. You can also use detection entries in <a href="/cloudflare-one/data-loss-prevention/data-classification/build-a-data-class/">data classes</a>.</p>
<p>Detection entries include:</p>
<ul>
<li><a href="#pattern-entries">Pattern entries</a> — regular expressions used to detect text patterns</li>
<li><a href="/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/">Predefined detection entries</a> — Cloudflare-managed detections for specific types of sensitive content</li>
<li><a href="#exact-data-match-datasets">Exact Data Match datasets</a> — uploaded datasets of sensitive values to match against, such as customer records or account numbers</li>
<li><a href="#custom-wordlist-datasets">Custom Wordlist datasets</a> — uploaded plaintext datasets used to detect terms such as product names, internal codes, or SKU numbers</li>
<li><a href="#document-entries">Document entries</a> — fingerprints of example documents used to find similar content</li>
<li><a href="#ai-prompt-topics">AI prompt topics</a> — categories of prompts submitted to generative AI tools</li>
</ul>
<h2 id="manage-detection-entries">Manage detection entries</h2>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong> to create, review, and manage detection entries.</p>
<p>The Detection entries section includes dedicated views for different entry types, including <strong>All</strong>, <strong>Pattern</strong>, <strong>Predefined</strong>, <strong>Datasets</strong>, <strong>Documents</strong>, and <strong>AI prompt topics</strong>. You can use search and filters to find specific entries and review details such as type, status, and last updated time.</p>
<p>You can add the same detection entry to multiple custom DLP profiles. When you delete a custom detection entry, Cloudflare lists the profiles that currently use it.</p>
<h2 id="test-a-detection-entry">Test a detection entry</h2>
<p>To test whether a detection entry identifies sample content, add the entry to a <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">DLP profile</a>, then use <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan</a>. Test scan confirms whether the selected profile detects the sample. It does not test a Gateway policy or traffic flowing through Gateway.</p>
<p>If the profile does not match the sample, review the detection entry configuration, the profile <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#match-count">match count</a>, and <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence threshold</a>.</p>
<h2 id="predefined-detection-entries">Predefined detection entries</h2>
<p>Predefined detection entries are Cloudflare-managed detections for specific types of sensitive content. You can review them from the <strong>Predefined</strong> view in <strong>Detection entries</strong> and add them directly to custom DLP profiles.</p>
<p>For a full list, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/">Predefined detection entries</a>.</p>
<h2 id="pattern-entries">Pattern entries</h2>
<p>Pattern entries use regular expressions to detect text patterns in scanned content. You can create pattern entries independently of a DLP profile and reuse them across multiple custom profiles.</p>
<p>Regular expressions are written in Rust. Cloudflare recommends validating your regex with <a href="https://rustexp.lpil.uk/">Rustexp</a>.</p>
<p>DLP detects UTF-8 characters, which can be up to 4 bytes each. Custom text pattern detections are limited to 1024 bytes in length.</p>
<p>DLP does not support regular expressions with <code>+</code> or <code>*</code> operators because they are prone to exceeding the length limit. For example, the regex pattern <code>a+</code> can detect an infinite number of <code>a</code> characters. Cloudflare recommends using <code>a{min,max}</code> instead, such as <code>a{1,1024}</code>.</p>
<h3 id="create-a-pattern-entry">Create a pattern entry</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>From the <strong>Pattern</strong> tab, select <strong>Add Pattern</strong>.</li>
<li>Enter a name. Optionally, add a description.</li>
<li>In <strong>Value</strong>, enter the regular expression you want to detect.</li>
<li>Select <strong>Validate Regex</strong>.</li>
<li>After the regex is validated, select <strong>Save</strong>.</li>
</ol>
<p>To use a pattern entry, add it as an existing entry to one or more <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">custom DLP profiles</a>.</p>
<h2 id="exact-data-match-datasets">Exact Data Match datasets</h2>
<p>Exact Data Match (EDM) datasets protect sensitive information such as names, addresses, phone numbers, and account numbers.</p>
<p>All EDM dataset data is encrypted before reaching Cloudflare. To detect matches, Cloudflare hashes traffic and compares it to hashes from your dataset. Matched data will be redacted in payload logs.</p>
<h3 id="prepare-exact-data-match-datasets">Prepare Exact Data Match datasets</h3>
<h4 id="formatting">Formatting</h4>
<p>To prepare an Exact Data Match dataset for DLP, add your desired data to a multi-column spreadsheet. Each line must be at least six characters long. Entries do not require trailing or final commas.</p>
<p>For compatibility, save your file in either <code>.csv</code> or <code>.txt</code> format with LF (<code>\n</code>) newline characters. DLP does not support CRLF (<code>\r\n</code>) newline characters. For information on dataset limits, refer to <a href="/cloudflare-one/account-limits/#data-loss-prevention-dlp">Account limits</a>.</p>
<h4 id="column-title-cells">Column title cells</h4>
<p>DLP will detect and use title cells as column names for Exact Data Match datasets. If multiple columns have the same name, DLP will append a number sign (<code>#</code>) and number to their names.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="update-edm-datasets">Update EDM datasets</h3>
@markup("md", "content/.markup/bodies/4912.md")
</aside>
<h3 id="upload-a-new-exact-data-match-dataset">Upload a new Exact Data Match dataset</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>From the <strong>Datasets</strong> tab, select <strong>Add a dataset</strong>.</li>
<li>Select <strong>Exact Data Match (EDM)</strong>.</li>
<li>Upload your dataset file. Select <strong>Next</strong>.</li>
<li>Review and choose the detected columns you want to include. Select <strong>Next</strong>.</li>
<li>Name your dataset. Optionally, add a description. Select <strong>Next</strong>.</li>
<li>Review the details for your uploaded dataset. Select <strong>Save dataset</strong>.</li>
</ol>
<p>DLP will encrypt your dataset and save its hash.</p>
<p>The dataset will appear in the list with an <strong>Uploading</strong> status. Once the upload is complete, the status will change to <strong>Complete</strong>. You can then add the dataset as an existing entry to one or more <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">custom DLP profiles</a>.</p>
<h3 id="manage-existing-exact-data-match-datasets">Manage existing Exact Data Match datasets</h3>
<p>Uploaded Exact Data Match datasets are read-only. To update a dataset, you must upload a new file to replace the original.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>From the <strong>Datasets</strong> tab, select the dataset you want to update.</li>
<li>Select <strong>Upload dataset</strong> and choose your updated dataset. Select <strong>Next</strong>.</li>
<li>Review and choose the new columns. Select <strong>Next</strong>.</li>
<li>Select <strong>Save dataset</strong>.</li>
</ol>
<p>Your new dataset will replace the original dataset.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="remove-existing-column-entries">Remove existing column entries</h3>
@markup("md", "content/.markup/bodies/4911.md")
</aside>
<h2 id="custom-wordlist-datasets">Custom Wordlist datasets</h2>
<p>Custom Wordlist (CWL) datasets protect non-sensitive terms such as intellectual property, SKU numbers, and internal project names.</p>
<p>Cloudflare stores data from CWL datasets in plaintext within DLP. Plaintext matches appear in payload logs. Optionally, CWL can detect case-sensitive data.</p>
<h3 id="prepare-custom-wordlist-datasets">Prepare Custom Wordlist datasets</h3>
<p>Column title cells may result in false positives in Custom Wordlist datasets and should be removed.</p>
<h3 id="upload-a-new-custom-wordlist-dataset">Upload a new Custom Wordlist dataset</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>From the <strong>Datasets</strong> tab, select <strong>Add a dataset</strong>.</li>
<li>Select <strong>Custom Wordlist (CWL)</strong>.</li>
<li>Name your dataset. Optionally, add a description.</li>
<li>In <strong>Upload file</strong>, choose your dataset file.</li>
<li>(Optional) In <strong>Settings</strong>, turn on <strong>Enforce case sensitivity</strong> to require matched values to contain exact capitalization.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>DLP will save your dataset in cleartext.</p>
<p>The dataset will appear in the list with an <strong>Uploading</strong> status. Once the upload is complete, the status will change to <strong>Complete</strong>. You can then add the dataset as an existing entry to one or more <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">custom DLP profiles</a>.</p>
<h3 id="manage-existing-custom-wordlist-datasets">Manage existing Custom Wordlist datasets</h3>
<p>Uploaded Custom Wordlist datasets are read-only. To update a dataset, you must upload a new file to replace the original.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>From the <strong>Datasets</strong> tab, select the dataset you want to update.</li>
<li>Select <strong>Upload dataset</strong> and choose your updated dataset. Select <strong>Next</strong>.</li>
<li>Select <strong>Save dataset</strong>.</li>
</ol>
<p>Your new dataset will replace the original dataset.</p>
<h2 id="document-entries">Document entries</h2>
<p>You can upload example documents to detect similar content in your organization's traffic. DLP creates a unique fingerprint of the document and compares traffic against it based on how similar it is to the original. This is useful for detecting specific document types common to your organization, such as contract templates or internal reports, where the content does not reduce to a list of individual values in an uploaded dataset.</p>
<p>DLP stores uploaded documents encrypted at rest in a <a href="/r2/">Cloudflare R2</a> bucket. To upload sensitive data that is only stored in memory, use <a href="#exact-data-match-datasets">Exact Data Match datasets</a>.</p>
<h3 id="prepare-document-entries">Prepare document entries</h3>
<p>DLP supports documents in <code>.docx</code> and <code>.txt</code> format. Documents must be under 10 MB.</p>
<h3 id="upload-a-new-document-entry">Upload a new document entry</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>From the <strong>Documents</strong> tab, select <strong>Add a document entry</strong>.</li>
<li>Name your document. Optionally, add a description.</li>
<li>In <strong>Minimum similarity for matches</strong>, enter a value between 0% and 100%.</li>
<li>In <strong>Upload document</strong>, choose and upload your document file.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The document will appear in the list with a <strong>Pending</strong> status. Once the upload is complete, the status will change to <strong>Complete</strong>. If you created a document entry with Terraform, the status will be <strong>No file</strong> until you upload a file.</p>
<p>To use your uploaded document fingerprint, add it as an existing entry to one or more <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">custom DLP profiles</a>.</p>
<h3 id="manage-existing-document-entries">Manage existing document entries</h3>
<p>Uploaded document entries are read-only. To update a document entry, you must upload a new file to replace the original.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>From the <strong>Documents</strong> tab, choose the document you want to update and select <strong>Edit</strong>.</li>
<li>(Optional) Update the name and minimum similarity for matches for your document entry. You can also open the existing uploaded document.</li>
<li>In <strong>Update document entry</strong>, choose and upload your updated document file.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Your new document entry will replace the original document entry. If your file upload fails, DLP will still use the original document fingerprint to scan traffic until you delete the entry.</p>
<h2 id="ai-prompt-topics">AI prompt topics</h2>
<p>DLP uses <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">Application Granular Controls</a> to detect and categorize prompts submitted to generative AI tools. Application Granular Controls analyzes prompts for both content and user intent. Supported AI prompt protection detections include:</p>
<table>
<thead>
<tr>
<th>Detection entry</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content: PII</td>
<td>Prompt contains personal information such as names, SSNs, or email addresses.</td>
</tr>
<tr>
<td>Content: Credentials and Secrets</td>
<td>Prompt contains API keys, passwords, or other sensitive credentials.</td>
</tr>
<tr>
<td>Content: Source Code</td>
<td>Prompt contains actual source code, code snippets, or proprietary algorithms.</td>
</tr>
<tr>
<td>Content: Customer Data</td>
<td>Prompt contains customer names, projects, business activities, or confidential customer contexts.</td>
</tr>
<tr>
<td>Content: Financial Information</td>
<td>Prompt contains financial numbers or confidential business data.</td>
</tr>
<tr>
<td>Intent: PII</td>
<td>Prompt requests specific personal information about individuals.</td>
</tr>
<tr>
<td>Intent: Code Abuse and Malicious Code</td>
<td>Prompt requests malicious code for attacks, exploits, or harmful activities.</td>
</tr>
<tr>
<td>Intent: Jailbreak</td>
<td>Prompt attempts to circumvent AI security policies.</td>
</tr>
</tbody>
</table>
<p>Each detection entry is categorized as either <strong>Content</strong> or <strong>Intent</strong>:</p>
<ul>
<li><strong>Content</strong> — Detects specific text or data in the prompt itself (for example, a user pasting source code or a credit card number into a chat).</li>
<li><strong>Intent</strong> — Detects the user's goal or objective for the AI's response (for example, a user asking an AI to generate malicious code or extract personal information).</li>
</ul>
<p>Intent detection is useful when AI applications have access to internal data sources containing sensitive information through SaaS connectors or Model Context Protocol (MCP) servers.</p>
<p>To use an AI prompt topic, configure the corresponding <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#ai-prompt">predefined DLP profile</a> or add it as an existing entry to one or more <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">custom DLP profiles</a>. AI prompt protection is available for ChatGPT, Google Gemini, Perplexity, and Claude.</p>
