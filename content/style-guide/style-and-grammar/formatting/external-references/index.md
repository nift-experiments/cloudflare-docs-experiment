---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/external-references/
  description: Format external references and citations.
  full_title: External references · Cloudflare Style Guide
  head_html: <title>External references · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Format external references and citations."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/external-references/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/external-references/index.md"><meta property="og:title" content="External references · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Format external references and citations."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/external-references/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/external-references/#page","headline":"External references \u00b7 Cloudflare Style Guide","description":"Format external references and citations.","url":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/external-references/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/style-and-grammar/formatting/external-references/
  schema: 1
---
<p>When referencing external resources, ensure that you are linking to a trustworthy source that is recognized as an authority.</p>
<p>For general websites, consider the following recommendations about the link text:</p>
<ul>
<li>Use the website name if you are linking to the home page.</li>
<li>Use the page name if you are linking to a specific page.</li>
<li>Authoritative sources for documents such as RFCs can have their own specific format for references, such as the RFC number.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14679.md")
</aside>
<h2 id="referencing-rfcs">Referencing RFCs</h2>
<p>A Request for Comments (RFC) document is a formal document produced by different entities such as the Internet Engineering Task Force (IETF), covering many aspects of computer networking. RFCs describe the Internet's technical foundations, such as addressing, routing, and transport technologies.</p>
<p>Use the following formatting when referencing an RFC:</p>
<p><code>RFC &lt;number&gt;</code></p>
<p>(RFC, space, number up to four digits)</p>
<p>Example: CAA is a new DNS resource record type defined in RFC 6844.</p>
<h2 id="links">Links</h2>
<p>When linking to an RFC (or RFC section), consider using a link to the following website, which is the authoritative source according to IETF:</p>
<p><a href="https://www.rfc-editor.org">https://www.rfc-editor.org</a></p>
<p>To get the link:</p>
<ol>
<li>Go to <a href="https://www.rfc-editor.org/rfc-index.html">RFC Editor</a> and search for the RFC number.</li>
<li>Select <strong>HTML</strong> to open the HTML version. If available, do <strong>not</strong> use <strong>HTML with inline errata</strong> as this version should not be used as reference.</li>
<li>(Optional) Go to a specific section, if necessary.</li>
<li>Use the current URL as the link target in Developer Documentation.</li>
</ol>
<p>URL example:</p>
<p><a href="https://www.rfc-editor.org/rfc/rfc6844.html">https://www.rfc-editor.org/rfc/rfc6844.html</a></p>
