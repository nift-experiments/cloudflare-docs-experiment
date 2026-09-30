---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/
  description: Follow file naming and organization conventions.
  full_title: File conventions · Cloudflare Style Guide
  head_html: <title>File conventions · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Follow file naming and organization conventions."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/index.md"><meta property="og:title" content="File conventions · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Follow file naming and organization conventions."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/#page","headline":"File conventions \u00b7 Cloudflare Style Guide","description":"Follow file naming and organization conventions.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/file-conventions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/file-conventions/
  schema: 1
---
<p>Our docs have a few conventions around files.</p>
<h2 id="naming">Naming</h2>
<p>When creating new files, follow specific conventions for your naming.</p>
<p>Filenames should:</p>
<ul>
<li>Semantically communicate the purpose of the file</li>
<li>Be lowercased</li>
<li>Use dashes between words</li>
</ul>
<pre tabindex="0"><code class="language-txt">/src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx&#10;//assets/upstream/images/api-shield/api-shield-call-sequence.png&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">/src/content/docs/fundamentals/concepts/What is Cloudflare.mdx&#10;/src/content/docs/fundamentals/concepts/What-is-Cloudflare.mdx&#10;//assets/upstream/images/api-shield/API_Image_1.png&#10;</code></pre>
<p>These conventions are important for user readability, SEO conventions, and making sure our GitHub actions do not break.</p>
<h2 id="folders">Folders</h2>
<p>Each folder should have a file named <code>index.mdx</code>.</p>
<pre tabindex="0"><code class="language-txt">/src/content/docs/fundamentals/concepts/index.mdx&#10;</code></pre>
<p>The content at <code>/src/content/docs/fundamentals/concepts/index.mdx</code> will be rendered at <code>https://developers.cloudflare.com/fundamentals/concepts/</code>.</p>
<h2 id="content-files">Content files</h2>
<p>Add regular content files to the <code>/src/content/docs/{product_folder}/</code> directory.</p>
<pre tabindex="0"><code class="language-txt">/src/content/docs/fundamentals/concepts/what-is-cloudflare.mdx&#10;</code></pre>
<h2 id="image-files">Image files</h2>
<p>Add image files to the <code>//assets/upstream/images/{product_folder}/</code> directory.</p>
<pre tabindex="0"><code class="language-txt">//assets/upstream/images/api-shield/api-shield-call-sequence.png&#10;</code></pre>
