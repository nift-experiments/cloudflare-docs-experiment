---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/
  description: Configure account-level DLP settings.
  full_title: DLP settings · Cloudflare One docs
  head_html: <title>DLP settings · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure account-level DLP settings."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/index.md"><meta property="og:title" content="DLP settings · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure account-level DLP settings."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One,Data Loss Prevention"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/#page","headline":"DLP settings \u00b7 Cloudflare One docs","description":"Configure account-level DLP settings.","url":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/data-loss-prevention/dlp-settings/
  schema: 1
---
<p>DLP settings allow you to configure account-level settings that apply across all DLP profiles and policies. These settings are located in <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<h2 id="optical-character-recognition-ocr">Optical Character Recognition (OCR)</h2>
<p>Optical Character Recognition (OCR) analyzes and interprets text within image files. When turned on, OCR can detect sensitive data within images your users upload.</p>
<p>OCR supports scanning <code>.jpg</code>/<code>.jpeg</code> and <code>.png</code> files between 4 KB and 1 MB in size. Text is encoded in UTF-8 format, including support for non-Latin characters.</p>
<p>To turn on OCR:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong>.</li>
<li>Turn on <strong>Optical Character Recognition (OCR)</strong>.</li>
</ol>
<h2 id="ai-context-analysis">AI context analysis</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4522.md")
</aside>
<p>AI context analysis uses a pretrained model to analyze surrounding context and adjust the confidence level of a detection. For example, a number that matches a credit card pattern may receive a lower confidence score if it appears in a context where credit card numbers are unlikely. DLP will log any matches that are above your confidence threshold.</p>
<p>DLP redacts any matched text, then converts the surrounding context into a vector embedding and submits it to <a href="/workers-ai/">Cloudflare Workers AI</a>. Vector embeddings (not raw text) are stored in user-specific private namespaces for up to six months, along with hit count and the <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#report-false-and-true-positives-to-ai-context-analysis">false positive/negative report</a>.</p>
<p>To turn on AI context analysis:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong>.</li>
<li>Turn on <strong>AI context analysis</strong>.</li>
<li><a href="/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy">Add the profile</a> to a DLP policy.</li>
<li>When configuring the DLP policy, turn on <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">payload logging</a>.</li>
</ol>
<p>AI context analysis results will appear in the payload section of your <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#4-view-dlp-logs">DLP logs</a>. To improve future detections of sensitive data, you need to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#report-false-and-true-positives-to-ai-context-analysis">report false and true positives</a>.</p>
<h2 id="payload-encryption-key">Payload encryption key</h2>
<p>Before you begin logging DLP payloads, you will need to set a DLP payload encryption public key. DLP uses public-key encryption so that matched sensitive data is readable only by you — Cloudflare does not have access to your private key and cannot decrypt your logs.</p>
<h3 id="generate-a-key-pair">Generate a key pair</h3>
<p>You will generate two keys: a public key (uploaded to Cloudflare to encrypt log data) and a private key (kept by you to decrypt log data later).</p>
<p>To generate a public/private key pair in the command line, refer to <a href="/waf/managed-rules/payload-logging/command-line/generate-key-pair/">Generate a key pair</a>.</p>
<h3 id="upload-the-public-key-to-cloudflare">Upload the public key to Cloudflare</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong>.</li>
<li>In the <strong>DLP Payload Encryption public key</strong> field, paste your public key.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4521.md")
</aside>
<h2 id="payload-log-masking">Payload log masking</h2>
<p>You can control how sensitive data appears in your DLP payload logs by selecting a masking level. This determines how much of the matched content is visible after decryption.</p>
<p>To configure payload log masking:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong>.</li>
<li>Go to the <strong>Payload log masking</strong> card.</li>
<li>Choose one of the following masking levels:
<ul>
<li><strong>Full Mask (default):</strong> Masks the match while preserving character count and visual formatting. For example, a Social Security Number appears as <code>***-**-****</code>.</li>
<li><strong>Partial Mask:</strong> Reveals 25% of the matched content while masking the remainder. For example, <code>***-**-6789</code>.</li>
<li><strong>Clear Text:</strong> Stores the full, unmasked match for detailed investigation. For example, <code>123-45-6789</code>.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4520.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4519.md")
</aside>
<h2 id="migrate-from-profile-level-settings">Migrate from profile-level settings</h2>
<p>OCR and AI context analysis are available at both the profile level (<strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>) and the account level (<strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong>) during the migration period. When both are configured, DLP uses OR logic for evaluation. A match occurs if either the profile-level or account-level setting would trigger a detection.</p>
<p>Profile-level OCR and AI context analysis settings will be deprecated in a future release. We recommend migrating to account-level settings in <strong>DLP settings</strong> to ensure consistent behavior across all profiles.</p>
<p>To migrate:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong>.</li>
<li>Turn on <strong>Optical Character Recognition (OCR)</strong> and/or <strong>AI context analysis</strong> as needed.</li>
<li>Go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>For each profile with OCR or AI context analysis enabled, edit the profile and turn off the profile-level settings.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
