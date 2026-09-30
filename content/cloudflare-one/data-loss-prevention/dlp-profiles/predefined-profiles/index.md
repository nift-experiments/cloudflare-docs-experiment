---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/
  description: Reference information for Predefined profiles in Cloudflare One.
  full_title: Predefined profiles · Cloudflare One docs
  head_html: <title>Predefined profiles · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Predefined profiles in Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/index.md"><meta property="og:title" content="Predefined profiles · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Predefined profiles in Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#page","headline":"Predefined profiles \u00b7 Cloudflare One docs","description":"Reference information for Predefined profiles in Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/
  schema: 1
---
<p>Cloudflare Zero Trust provides predefined DLP profiles for common types of sensitive data, such as credit card numbers, national identifiers, and credentials. Each predefined profile groups related <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">detection entries</a> which can be turned on or off individually.</p>
<p>To use a predefined profile, <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#configure-a-predefined-profile">enable the detection entries you want</a> and add the profile to a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">DLP policy</a>. You can tune accuracy with <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence thresholds</a> and other <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/">profile settings</a>.</p>
<p>Most profiles match when any enabled detection entry matches. Some add validation checks to improve accuracy, and a few use profile-specific matching logic to reduce false positives — for example, the <a href="#personally-identifiable-information-pii-record">PII Record</a> profile requires multiple entries in close proximity.</p>
<h2 id="ai-prompt">AI Prompt</h2>
<p>DLP provides AI prompt protection profiles that detect sensitive prompts submitted to generative AI tools such as ChatGPT, Google Gemini, Perplexity, and Claude. Each profile evaluates prompts for <strong>Content</strong> (sensitive data within the prompt) and <strong>Intent</strong> (what the user wants the model to do):</p>
<ul>
<li><strong>AI Prompt: AI Security</strong> — Prompts that attempt to circumvent AI security policies or request malicious code.</li>
<li><strong>AI Prompt: Customer</strong> — Prompts that contain customer names, projects, business activities, or confidential customer contexts.</li>
<li><strong>AI Prompt: Financial Information</strong> — Prompts that contain financial numbers or confidential business data.</li>
<li><strong>AI Prompt: PII</strong> — Prompts that contain or request personal information such as names, SSNs, or email addresses.</li>
<li><strong>AI Prompt: Technical</strong> — Prompts that contain source code, code snippets, proprietary algorithms, or credentials such as API keys and passwords.</li>
</ul>
<p>For the full list of underlying topics, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>
<h2 id="credentials-and-secrets">Credentials and Secrets</h2>
<p>The following secrets are validated with regex.</p>
<ul>
<li>Amazon Web Services (AWS) keys</li>
<li>Azure API keys</li>
<li>Google Cloud Platform keys</li>
<li>SSH keys</li>
</ul>
<p>The following Cloudflare API credentials are validated algorithmically using a checksum. Only credentials generated after <a href="/fundamentals/api/get-started/token-formats/">Cloudflare's token format update</a> will be matched by these entries.</p>
<table>
<thead>
<tr>
<th>Detection entry</th>
<th>Format</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare User API Key</td>
<td><code>cfk_</code> followed by 40 alphanumeric characters and an 8-character hex checksum</td>
</tr>
<tr>
<td>Cloudflare User API Token</td>
<td><code>cfut_</code> followed by 40 alphanumeric characters and an 8-character hex checksum</td>
</tr>
<tr>
<td>Cloudflare Account Owned API Token</td>
<td><code>cfat_</code> followed by 40 alphanumeric characters and an 8-character hex checksum</td>
</tr>
</tbody>
</table>
<h2 id="financial-information">Financial Information</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4895.md")
</aside>
<p>Credit card numbers begin with a six or eight-digit Issuer Identification Number (IIN) and are followed by up to 23 additional digits. Card verification values (CVVs) are not validated.</p>
<p>In the table below, entries use one of three validation methods. <a href="https://en.wikipedia.org/wiki/Luhn_algorithm">Luhn's algorithm</a> is a checksum formula used to verify credit card numbers. Entries validated &quot;with checksum&quot; use an arithmetic check specific to that number format. Entries validated &quot;with regex&quot; match a known text pattern without performing a mathematical check.</p>
<table>
<thead>
<tr>
<th>Detection entry</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>American Express Card Number</td>
<td>Validated using <a href="https://en.wikipedia.org/wiki/Luhn_algorithm">Luhn's algorithm</a>.</td>
</tr>
<tr>
<td>American Express Text</td>
<td>Text matching <code>amex</code> or <code>american express</code>.</td>
</tr>
<tr>
<td>Diners Club Card Number</td>
<td>Validated using Luhn's algorithm.</td>
</tr>
<tr>
<td>CVV Card Number (labeled)</td>
<td>Validated with regex.</td>
</tr>
<tr>
<td>Mastercard Card Number</td>
<td>Validated using Luhn's algorithm.</td>
</tr>
<tr>
<td>Mastercard Text</td>
<td>Text matching <code>mastercard</code>.</td>
</tr>
<tr>
<td>Union Pay Card Number</td>
<td>Validated using Luhn's algorithm.</td>
</tr>
<tr>
<td>Union Pay Text</td>
<td>Text matching <code>union pay</code>.</td>
</tr>
<tr>
<td>Visa Card Number</td>
<td>Validated using Luhn's algorithm.</td>
</tr>
<tr>
<td>Visa Text</td>
<td>Text matching <code>visa</code>.</td>
</tr>
<tr>
<td>United States ABA Routing Number</td>
<td>Validated algorithmically with checksum.</td>
</tr>
<tr>
<td>IBAN</td>
<td>Validated with checksum.</td>
</tr>
</tbody>
</table>
<h2 id="health-information">Health Information</h2>
<p>The following diagnosis and medication names are checked for surrounding ASCII characters to prevent false positives.</p>
<ul>
<li>FDA active ingredients</li>
<li>FDA drug names</li>
<li>ICD-10 FY2023 short descriptions</li>
<li>ICD-11 short descriptions</li>
</ul>
<h2 id="http-archive-har-files">HTTP Archive (HAR) files</h2>
<p>The <strong>Unsanitized HAR</strong> predefined profile detects HTTP Archive (HAR) files in traffic that have not been processed by Cloudflare's HAR sanitizer. HAR files frequently contain sensitive data such as session cookies, authorization headers, and other credentials.</p>
<table>
<thead>
<tr>
<th>Detection entry</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Unsanitized HAR file</td>
<td>Detects HAR files that do not carry a Cloudflare sanitized marker. Files processed by the Cloudflare HAR sanitizer and unmodified since will not match this entry.</td>
</tr>
</tbody>
</table>
<p>You can use this profile in a Gateway HTTP policy to block HAR file uploads or redirect users to <code>https://har-sanitizer.pages.dev/</code> to sanitize the file before uploading. For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/common-policies/">common DLP policies</a>.</p>
<h2 id="personally-identifiable-information-pii-record">Personally Identifiable Information (PII) Record</h2>
<p>The <strong>Personally Identifiable Information (PII) Record</strong> predefined profile is designed to detect records that contain multiple types of personal data. Unlike most predefined and custom DLP profiles, this profile matches only when at least three unique detection entries are found in close proximity.</p>
<p>This behavior helps reduce false positives from isolated matches.</p>
<p>The profile includes the following detection entries:</p>
<ul>
<li>Australia Passport Number</li>
<li>American Express Card Number</li>
<li>Diners Club Card Number</li>
<li>US Driver's License Number</li>
<li>Email Address</li>
<li>Full Name</li>
<li>US Mailing Address</li>
<li>Mastercard Card Number</li>
<li>US Individual Tax Identification Number (ITIN)</li>
<li>US Passport Number</li>
<li>US Phone Number</li>
<li>Union Pay Card Number</li>
<li>United States SSN Numeric Detection</li>
<li>Visa Card Number</li>
</ul>
<h2 id="social-security-insurance-tax-and-identifier-numbers">Social Security, Insurance, Tax, and Identifier Numbers</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability-1">Availability</h3>
@markup("md", "content/.markup/bodies/4894.md")
</aside>
<p>The following national identifier detections are validated algorithmically when possible.</p>
<table>
<thead>
<tr>
<th>Detection entry</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>United States SSN Numeric Detection</td>
<td>Matched values must include commonly used separators. For example, <code>000-00-0000</code> matches but <code>000000000</code> does not. Unlike credit card numbers, Social Security numbers have no built-in checksum, so DLP validates the format only.</td>
</tr>
<tr>
<td>Social Security Number Text</td>
<td>Text matching <code>ssn</code> or <code>social security</code>.</td>
</tr>
<tr>
<td>Australia Tax File Number</td>
<td>Validated with checksum.</td>
</tr>
<tr>
<td>Canada Social Insurance Number</td>
<td>Validated using Luhn's algorithm.</td>
</tr>
<tr>
<td>France Social Security Number</td>
<td>Validated with regex.</td>
</tr>
<tr>
<td>Hong Kong Identity Card (HKIC) Number</td>
<td>Validated with checksum.</td>
</tr>
<tr>
<td>Indonesia Identity Card Number</td>
<td>Validated with regex.</td>
</tr>
<tr>
<td>Malaysian National Identity Card Number</td>
<td>Validated with regex.</td>
</tr>
<tr>
<td>Philippines Unified Multi-Purpose ID (UMID) Number</td>
<td>Validated with regex.</td>
</tr>
<tr>
<td>Singapore National Registration Identity Card Number</td>
<td>Validated with checksum.</td>
</tr>
<tr>
<td>Taiwan National Identification Number</td>
<td>Validated with checksum.</td>
</tr>
<tr>
<td>Thai Identity Card Number</td>
<td>Validated with checksum.</td>
</tr>
<tr>
<td>United Kingdom NHS Number</td>
<td>Validated with checksum.</td>
</tr>
<tr>
<td>United Kingdom National Insurance Number</td>
<td>Validated with regex.</td>
</tr>
</tbody>
</table>
<h2 id="source-code">Source Code</h2>
<p>The <strong>Source Code</strong> profile detects source code in common programming languages.</p>
<p>The following programming languages are validated with natural language processing (NLP).</p>
<ul>
<li>C</li>
<li>C++</li>
<li>C#</li>
<li>Go</li>
<li>Haskell</li>
<li>Java</li>
<li>JavaScript</li>
<li>Lua</li>
<li>Python</li>
<li>R</li>
<li>Rust</li>
<li>Swift</li>
</ul>
