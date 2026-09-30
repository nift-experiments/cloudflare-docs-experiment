---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/
  description: View the list of file formats supported by Workers AI Markdown Conversion.
  full_title: Supported Formats · Cloudflare Workers AI docs
  head_html: <title>Supported Formats · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="View the list of file formats supported by Workers AI Markdown Conversion."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/index.md"><meta property="og:title" content="Supported Formats · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View the list of file formats supported by Workers AI Markdown Conversion."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/#page","headline":"Supported Formats \u00b7 Cloudflare Workers AI docs","description":"View the list of file formats supported by Workers AI Markdown Conversion.","url":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/markdown-conversion/supported-formats/
  schema: 1
---
<p>This list shows all rich-content formats that are currently supported for Markdown conversion and is updated frequently:</p>
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
