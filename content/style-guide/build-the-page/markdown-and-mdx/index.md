---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/
  description: Cloudflare docs pages are authored in MDX, Markdown extended with components. Learn the body syntax, importing components, and escaping special characters.
  full_title: Markdown and MDX · Cloudflare Style Guide
  head_html: <title>Markdown and MDX · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare docs pages are authored in MDX, Markdown extended with components. Learn the body syntax, importing components, and escaping special characters."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/index.md"><meta property="og:title" content="Markdown and MDX · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare docs pages are authored in MDX, Markdown extended with components. Learn the body syntax, importing components, and escaping special characters."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/#page","headline":"Markdown and MDX \u00b7 Cloudflare Style Guide","description":"Cloudflare docs pages are authored in MDX, Markdown extended with components. Learn the body syntax, importing components, and escaping special characters.","url":"https://developers.cloudflare.com/style-guide/build-the-page/markdown-and-mdx/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/markdown-and-mdx/
  schema: 1
---
<p>Cloudflare docs pages are authored in MDX, which is Markdown extended with JSX components. Every page is a <code>.mdx</code> file with a <a href="/style-guide/build-the-page/frontmatter/">frontmatter</a> block at the top, followed by the body content.</p>
<h2 id="body-content">Body content</h2>
<p>The body is standard Markdown. Use it for headings, paragraphs, lists, tables, links, and code:</p>
<pre tabindex="0"><code class="language-md">&#35;# A heading&#10;&#10;A paragraph with a [link](/style-guide/) and `inline code`.&#10;&#10;&#45; A list item&#10;&#45; Another list item&#10;</code></pre>
<p>Refer to the <a href="/style-guide/style-and-grammar/formatting/">formatting</a> section for the rules that govern how to write each of these elements.</p>
<h2 id="import-components">Import components</h2>
<p>Components add formatting that plain Markdown cannot, such as tabs, asides, and collapsible sections. Import them from <code>~/components</code> after the frontmatter block, then add them anywhere in the body:</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Example page&#10;&#45;--&#10;&#10;import { Aside } from &quot;~/components&quot;;&#10;&#10;&lt;Aside type=&quot;note&quot;&gt;This is an aside.&lt;/Aside&gt;&#10;</code></pre>
<p>Refer to the <a href="/style-guide/build-the-page/components/">components</a> section for the props and requirements of each component.</p>
<h2 id="escape-special-characters">Escape special characters</h2>
<p>MDX treats <code>{</code>, <code>}</code>, <code>&lt;</code>, and <code>&gt;</code> as syntax. When these characters are part of your content rather than code, wrap them in backticks so they render literally:</p>
<pre tabindex="0"><code class="language-md">Set the value to `{&quot;key&quot;: &quot;value&quot;}`.&#10;</code></pre>
<p>Characters inside a fenced code block are already literal and do not need escaping.</p>
<h2 id="code-blocks">Code blocks</h2>
<p>Open a fenced code block with a lowercase language identifier so the code is highlighted correctly. Use <code>txt</code> for generic output that has no language:</p>
<pre tabindex="0"><code class="language-md">&#10;</code></pre>
<p>const value = 1;</p>
<pre tabindex="0"><code>&#10;</code></pre>
<p>Deployment complete.</p>
<pre tabindex="0"><code>&#10;</code></pre>
