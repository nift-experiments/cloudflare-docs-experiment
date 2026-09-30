---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/data-source/
  description: Connect a website, R2 bucket, or upload files directly to your AI Search instance for indexing.
  full_title: Data source · Cloudflare AI Search docs
  head_html: <title>Data source · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect a website, R2 bucket, or upload files directly to your AI Search instance for indexing."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/data-source/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/data-source/index.md"><meta property="og:title" content="Data source · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect a website, R2 bucket, or upload files directly to your AI Search instance for indexing."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/data-source/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/data-source/#page","headline":"Data source \u00b7 Cloudflare AI Search docs","description":"Connect a website, R2 bucket, or upload files directly to your AI Search instance for indexing.","url":"https://developers.cloudflare.com/ai-search/configuration/data-source/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/data-source/
  schema: 1
---
<p>You can upload files directly to an instance or connect an external data source.</p>
<table>
<thead>
<tr>
<th>Data Source</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/ai-search/configuration/data-source/built-in-storage/">Built-in storage</a></td>
<td>Upload files directly to an instance. Available by default on every instance.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/website/">Website</a></td>
<td>Connect a domain you own to index website pages.</td>
</tr>
<tr>
<td><a href="/ai-search/configuration/data-source/r2/">R2 Bucket</a></td>
<td>Connect a Cloudflare R2 bucket to index stored documents.</td>
</tr>
</tbody>
</table>
<p>For website data sources, <a href="/ai-search/configuration/data-source/website/parse-types/">Parse types</a> covers how AI Search finds the pages to index.</p>
<h2 id="supported-file-types">Supported file types</h2>
<p>AI Search can ingest a variety of file types. The following plain text files and rich format files are supported.</p>
<h3 id="plain-text-file-types">Plain text file types</h3>
<table>
<thead>
<tr>
<th>Format</th>
<th>File extensions</th>
<th>Mime Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Text</td>
<td><code>.txt</code>, <code>.rst</code></td>
<td><code>text/plain</code></td>
</tr>
<tr>
<td>Log</td>
<td><code>.log</code>, <code>.log.gz</code></td>
<td><code>text/plain</code></td>
</tr>
<tr>
<td>Config</td>
<td><code>.ini</code>, <code>.conf</code>, <code>.env</code>, <code>.properties</code>, <code>.gitignore</code>, <code>.editorconfig</code>, <code>.toml</code></td>
<td><code>text/plain</code>, <code>text/toml</code></td>
</tr>
<tr>
<td>Markdown</td>
<td><code>.markdown</code>, <code>.md</code>, <code>.mdx</code>, <code>.mdoc</code></td>
<td><code>text/markdown</code></td>
</tr>
<tr>
<td>LaTeX</td>
<td><code>.tex</code>, <code>.latex</code></td>
<td><code>application/x-tex</code>, <code>application/x-latex</code></td>
</tr>
<tr>
<td>Script</td>
<td><code>.sh</code>, <code>.bat</code>, <code>.ps1</code></td>
<td><code>application/x-sh</code>, <code>application/x-msdos-batch</code>, <code>text/x-powershell</code></td>
</tr>
<tr>
<td>SGML</td>
<td><code>.sgml</code></td>
<td><code>text/sgml</code></td>
</tr>
<tr>
<td>JSON</td>
<td><code>.json</code></td>
<td><code>application/json</code></td>
</tr>
<tr>
<td>SQL</td>
<td><code>.sql</code></td>
<td><code>application/sql</code></td>
</tr>
<tr>
<td>YAML</td>
<td><code>.yaml</code>, <code>.yml</code></td>
<td><code>application/x-yaml</code></td>
</tr>
<tr>
<td>CSS</td>
<td><code>.css</code></td>
<td><code>text/css</code></td>
</tr>
<tr>
<td>JavaScript</td>
<td><code>.js</code></td>
<td><code>application/javascript</code></td>
</tr>
<tr>
<td>PHP</td>
<td><code>.php</code></td>
<td><code>application/x-httpd-php</code></td>
</tr>
<tr>
<td>Python</td>
<td><code>.py</code></td>
<td><code>text/x-python</code></td>
</tr>
<tr>
<td>Ruby</td>
<td><code>.rb</code></td>
<td><code>text/x-ruby</code></td>
</tr>
<tr>
<td>Java</td>
<td><code>.java</code></td>
<td><code>text/x-java-source</code></td>
</tr>
<tr>
<td>C</td>
<td><code>.c</code></td>
<td><code>text/x-c</code></td>
</tr>
<tr>
<td>C++</td>
<td><code>.cpp</code>, <code>.cxx</code></td>
<td><code>text/x-c++</code></td>
</tr>
<tr>
<td>C Header</td>
<td><code>.h</code>, <code>.hpp</code></td>
<td><code>text/x-c-header</code></td>
</tr>
<tr>
<td>Go</td>
<td><code>.go</code></td>
<td><code>text/x-go</code></td>
</tr>
<tr>
<td>Rust</td>
<td><code>.rs</code></td>
<td><code>text/rust</code></td>
</tr>
<tr>
<td>Swift</td>
<td><code>.swift</code></td>
<td><code>text/swift</code></td>
</tr>
<tr>
<td>Dart</td>
<td><code>.dart</code></td>
<td><code>text/dart</code></td>
</tr>
<tr>
<td>EMACS Lisp</td>
<td><code>.el</code></td>
<td><code>application/x-elisp</code>, <code>text/x-elisp</code>, <code>text/x-emacs-lisp</code></td>
</tr>
</tbody>
</table>
<h3 id="rich-format-file-types">Rich format file types</h3>
<p>AI Search uses <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> to convert rich format files to markdown. The following table lists the supported formats that will be converted to Markdown:</p>
<table>
<tbody>
<th colspan="5" rowspan="1" style="width:160px">
			Format
</th>
<th colspan="5" rowspan="1">
			File extensions
</th>
<th colspan="5" rowspan="1">
			Mime Types
</th>
<tr>
<td colspan="5" rowspan="1">
				PDF Documents
</td>
<td colspan="5" rowspan="1">
				`.pdf`
</td>
<td colspan="5" rowspan="1">
				`application/pdf`
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				Images <sup>1</sup>
</td>
<td colspan="5" rowspan="1">
				`.jpeg`, `.jpg`, `.png`, `.webp`, `.svg`, `.gif`, `.bmp`
</td>
<td colspan="5" rowspan="1">
				`image/jpeg`, `image/png`, `image/webp`, `image/svg+xml`, `image/gif`, `image/bmp`
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				HTML Documents
</td>
<td colspan="5" rowspan="1">
				`.html`, `.htm`
</td>
<td colspan="5" rowspan="1">
				`text/html`
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				XML Documents
</td>
<td colspan="5" rowspan="1">
				`.xml`
</td>
<td colspan="5" rowspan="1">
				`application/xml`
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				Microsoft Office Documents
</td>
<td colspan="5" rowspan="1">
				`.xlsx`, `.xlsm`, `.xlsb`, `.xls`, `.et`, `.docx`
</td>
<td colspan="5" rowspan="1">
				`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`,
				`application/vnd.ms-excel.sheet.macroenabled.12`,
				`application/vnd.ms-excel.sheet.binary.macroenabled.12`,
				`application/vnd.ms-excel`,
				`application/vnd.openxmlformats-officedocument.wordprocessingml.document`
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				Open Document Format
</td>
<td colspan="5" rowspan="1">
				`.ods`, `.odt`
</td>
<td colspan="5" rowspan="1">
				`application/vnd.oasis.opendocument.spreadsheet`,
				`application/vnd.oasis.opendocument.text`
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				CSV
</td>
<td colspan="5" rowspan="1">
				`.csv`
</td>
<td colspan="5" rowspan="1">
				`text/csv`
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				Apple Documents
</td>
<td colspan="5" rowspan="1">
				`.numbers`
</td>
<td colspan="5" rowspan="1">
				`application/vnd.apple.numbers`
</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> Image conversion uses two Workers AI models for object detection
and summarization. See <a href="/workers-ai/features/markdown-conversion/#pricing">Workers AI
pricing</a> for more details.</p>
<h2 id="file-limits">File limits</h2>
<p>AI Search has a file size limit of <strong>up to 4 MB</strong>.</p>
<p>Files that exceed this limit will not be indexed and will show up in the error logs.</p>
