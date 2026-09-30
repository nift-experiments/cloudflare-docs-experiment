---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/
  description: Learn how Workers AI pre-processes and converts HTML, images, and other files to Markdown.
  full_title: How it works · Cloudflare Workers AI docs
  head_html: <title>How it works · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Workers AI pre-processes and converts HTML, images, and other files to Markdown."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/index.md"><meta property="og:title" content="How it works · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Workers AI pre-processes and converts HTML, images, and other files to Markdown."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/#page","headline":"How it works \u00b7 Cloudflare Workers AI docs","description":"Learn how Workers AI pre-processes and converts HTML, images, and other files to Markdown.","url":"https://developers.cloudflare.com/workers-ai/features/markdown-conversion/how-it-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/markdown-conversion/how-it-works/
  schema: 1
---
<h2 id="pre-processing">Pre-processing</h2>
<p>When parsing files before converting them to Markdown, there are some cleanup tasks we do depending on the type of file you are trying to convert.</p>
<h3 id="html">HTML</h3>
<p>When we detect an HTML file, a series of things happen to the HTML content before it is converted:</p>
<ul>
<li>Some elements are ignored, including <code>script</code> and <code>style</code> tags.</li>
<li>Meta tags are extracted. These include <code>title</code>, <code>description</code>, <code>og:title</code>, <code>og:description</code> and <code>og:image</code>.</li>
<li><a href="https://json-ld.org/">JSON-LD</a> content is extracted, if it exists. This will be appended at the end of the converted markdown.</li>
<li>The base URL to use for resolving relative links is extracted from the <code>&lt;base&gt;</code> element<sup>1</sup>, if it exists, according to the spec (that is, only the first instance of the base URL is counted).</li>
<li>If the <code>cssSelector</code> option is:
<ul>
<li>present, then only those elements that match the selector are kept for further processing;</li>
<li>missing, then elements such as <code>&lt;header&gt;</code>, <code>&lt;footer&gt;</code> and <code>&lt;head&gt;</code> are removed from the text.</li>
</ul>
</li>
<li>If a base URL was obtained previously, relative links in the remaining HTML are resolved to fully qualified URLs</li>
</ul>
<p><sup>1</sup> The host can also be set per request, using the HTML conversion
options. Refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#html">Conversion
Options</a> for
more details.</p>
<h3 id="images">Images</h3>
<p>Images take a bit more work to prepare for conversion.</p>
<p>For animated GIF files, only the first frame is extracted and analyzed. The remaining frames are discarded.</p>
<p>As a first step, we detect what type the image is. If it is an SVG (Scalable Vector Graphics) file, we need to convert it into a raster format so that using the necessary Workers AI models does not fail. In this case, SVGs are converted into PNGs internally.</p>
<p>Afterwards:</p>
<ul>
<li>We try to determine the image's dimensions. If successful, we determine if the image is considered &quot;too big&quot; or not. An image is &quot;too big&quot; if its width is bigger than 1280px or its height is bigger than 720px.</li>
<li>If the image is too big, we try to resize it to conform with those dimensions. If resizing fails, we simply try to use the original image data</li>
<li>The image is sent to an <strong>object-detection model</strong>. Specifically, we use the <a href="/workers-ai/models/detr-resnet-50/"><code>@cf/facebook/detr-resnet-50</code></a> from Workers AI.</li>
<li>If any objects were detected in the previous step, they are appended to a prompt that is used to instruct an <strong>image-to-text model</strong> on how to describe the image.</li>
<li>If a preferred conversion language is specified in the request's conversion options, the previous prompt is enriched with a directive for the model to output the content in the desired language. Refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#images">Conversion Options</a> for more details.</li>
<li>The final prompt is sent, along with the image data, to the <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> model, also from Workers AI.</li>
</ul>
<h3 id="pdfs">PDFs</h3>
<ul>
<li>Metadata is extracted. This can be removed from the final result. Refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#pdf">Conversion Options</a> for more details.</li>
<li>Each page is parsed in sequence.</li>
<li>We try to obtain a <code>StructTree</code> object from the PDF file. This data structure is a tree of tagged elements that make up the PDF contents, as specified by <a href="https://www.iso.org/standard/64599.html">ISO 14289 (PDF/UA)</a>.</li>
<li>If none is obtained, we extract the text of the page <em>as-is</em> and return it.</li>
<li>If we manage to obtain a <code>StructTree</code>, we traverse its nodes to build a semantic Markdown representation of its contents.</li>
</ul>
