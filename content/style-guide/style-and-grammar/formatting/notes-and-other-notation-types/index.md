---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/notes-and-other-notation-types/
  description: Use notes and admonitions consistently.
  full_title: Notes and other notation types · Cloudflare Style Guide
  head_html: <title>Notes and other notation types · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Use notes and admonitions consistently."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/notes-and-other-notation-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/notes-and-other-notation-types/index.md"><meta property="og:title" content="Notes and other notation types · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use notes and admonitions consistently."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/notes-and-other-notation-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/notes-and-other-notation-types/#page","headline":"Notes and other notation types \u00b7 Cloudflare Style Guide","description":"Use notes and admonitions consistently.","url":"https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/notes-and-other-notation-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/style-and-grammar/formatting/notes-and-other-notation-types/
  schema: 1
---
<p>When adding a note to a page, always use this special note formatting. There are three types of formatted notes: <code>note</code>, <code>caution</code>, and <code>tip</code>.</p>
<p>Here is some additional information about notes:</p>
<ul>
<li>The color of the note depends on the type of note: <code>note</code> is blue, <code>caution</code> is yellow, and <code>tip</code> is purple.</li>
<li>For every note type, the header text is optional.</li>
<li>All note types can contain text and additional formatting like lists, code blocks, and images.</li>
</ul>
<p>To learn how notes fit into our content strategy, refer to <a href="/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/">Notes/tips/warnings</a>.</p>
<h2 id="note">Note</h2>
<p>Use Note for small additions or when you need to provide extra context that is not essential to the main content.</p>
<p>If you do not provide a header, this aside will default to <code>Note</code>.</p>
<pre tabindex="0"><code class="language-mdx">:::note[Header]&#10;Hello, world!&#10;:::&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="header">Header</h3>
@markup("md", "content/.markup/bodies/14677.md")
</aside>
<h2 id="caution-warning">Caution/Warning</h2>
<p>Use Caution to highlight actions that could cause issues for a user.</p>
<p>If you do not provide a header, this aside will default to <code>Warning</code>.</p>
<pre tabindex="0"><code class="language-mdx">:::caution[Feature conflict]&#10;If you use feature A and feature B together, your configuration will not work.&#10;:::&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="feature-conflict">Feature conflict</h3>
@markup("md", "content/.markup/bodies/14676.md")
</aside>
<h2 id="tip">Tip</h2>
<p>Use Tip to share best practices or opinionated use cases that do not fit into the main documentation.</p>
<p>If you do not provide a header, this aside will default to <code>Tip</code>.</p>
<pre tabindex="0"><code class="language-mdx">:::tip[Best practice]&#10;Cloudflare recommends you use [1.1.1.1](/1.1.1.1/) as your DNS resolver.&#10;:::&#10;</code></pre>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/14675.md")
</aside>
