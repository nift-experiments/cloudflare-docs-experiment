---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/
  description: Use admonitions effectively in documentation.
  full_title: Notes/tips/warnings · Cloudflare Style Guide
  head_html: <title>Notes/tips/warnings · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Use admonitions effectively in documentation."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/index.md"><meta property="og:title" content="Notes/tips/warnings · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use admonitions effectively in documentation."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/#page","headline":"Notes/tips/warnings \u00b7 Cloudflare Style Guide","description":"Use admonitions effectively in documentation.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/
  schema: 1
---
<h2 id="definition">Definition</h2>
<p>A colored info box or aside with content (text, images, lists, code blocks) that adds relevant notes that do not fit the text or warns users of specific behavior that can break functionality or impact security.</p>
<h2 id="used-in">Used in</h2>
<p><a href="/style-guide/documentation-content-strategy/content-types/how-to/">How to</a>, <a href="/style-guide/documentation-content-strategy/content-types/configuration/">Configuration</a>, <a href="/style-guide/documentation-content-strategy/content-types/faq/">FAQ</a>, <a href="/style-guide/documentation-content-strategy/content-types/concept/">Concept</a>, <a href="/style-guide/documentation-content-strategy/content-types/reference/">Reference</a>, <a href="/style-guide/documentation-content-strategy/content-types/tutorial/">Tutorial</a></p>
<h2 id="structure">Structure</h2>
<p><strong>Type</strong>: note or warning (defines the background color)</p>
<p><strong>Aside content</strong></p>
<p><strong>(optional) Title/Header</strong></p>
<h2 id="templates">Templates</h2>
<p>To learn how to format notes, refer to <a href="/style-guide/style-and-grammar/formatting/notes-and-other-notation-types/">Notes and other notation types</a>.</p>
<h2 id="rendered-examples">Rendered examples</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="header-text">Header text</h3>
@markup("md", "content/.markup/bodies/14664.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14663.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14662.md")
</aside>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/14661.md")
</aside>
<h2 id="when-should-i-use-a-note-warning">When should I use a note/warning?</h2>
<p>Use a note to alert a reader to additional useful information that you cannot integrate into the text.</p>
<p>Use a warning to alert a reader to behavior that could impact the security of a users network or break functionality.</p>
<h2 id="recommendations">Recommendations</h2>
<ul>
<li><strong>An aside should not contain too much content</strong>, since it breaks the normal text flow. For example, up to 3 paragraphs or bulleted lists up to 3 items. If you need to include more content, consider creating a documentation section &quot;Important notes&quot; or similar.</li>
<li><strong>Use asides sparingly.</strong> Each section should not have more than one aside of the same type. The only exception is a possible availability disclaimer right after the heading.</li>
<li><strong>Asides inside task step instructions should not have a header.</strong> They take too much space and the background color is enough to distinguish the aside content from regular text.</li>
<li><strong>Use a <code>note</code> aside to state the restricted availability of a feature</strong> (for example, &quot;Only available for customers on an Enterprise plan.&quot;) at the beginning of a page, without a header.</li>
</ul>
