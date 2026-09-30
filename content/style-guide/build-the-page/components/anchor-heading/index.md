---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/anchor-heading/
  description: Create a heading with a custom anchor ID.
  full_title: Anchor heading · Cloudflare Style Guide
  head_html: <title>Anchor heading · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Create a heading with a custom anchor ID."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/anchor-heading/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/anchor-heading/index.md"><meta property="og:title" content="Anchor heading · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a heading with a custom anchor ID."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/anchor-heading/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/anchor-heading/#page","headline":"Anchor heading \u00b7 Cloudflare Style Guide","description":"Create a heading with a custom anchor ID.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/anchor-heading/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/anchor-heading/
  schema: 1
---
<p>The <code>AnchorHeading</code> component defines headings. Specifically, <code>AnchorHeading</code> performs the following:</p>
<ol>
<li>Generates URL fragments corresponding to headings.</li>
<li>Formats URL fragments into compatible syntax. For example, a <code>&amp;</code> is replaced with a <code>-</code>.</li>
<li>Creates a button to copy the URL at each fragment.</li>
<li>Allows heading fragments to be defined separately from the text of the heading itself.</li>
</ol>
<pre tabindex="0"><code class="language-mdx">import { AnchorHeading } from &quot;~/components&quot;;&#10;&#10;&lt;AnchorHeading title=&quot;How to use AnchorHeading&quot; slug=&quot;use-anchorheading&quot; depth={2} /&gt;&#10;</code></pre>
<p>Markdown files (including partials) have this behavior by default, applied via rehype plugins. Therefore, the <code>AnchorHeading</code> component is usually only required when writing headings yourself inside components, or when working on non-markdown files.</p>
<p>To override the ID given to a heading within Markdown, add an MDX comment at the end of the line:</p>
<pre tabindex="0"><code class="language-mdx">&#35;# foo {/*bar*/}&#10;{/* HTML: &lt;h2 id=&quot;bar&quot;&gt;foo&lt;/h2&gt; */}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14659.md")
</aside>
