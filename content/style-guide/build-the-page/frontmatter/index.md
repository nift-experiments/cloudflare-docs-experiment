---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/
  description: Set the required and optional frontmatter fields that carry a page's metadata, such as title, description, and pcx_content_type.
  full_title: Frontmatter · Cloudflare Style Guide
  head_html: <title>Frontmatter · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Set the required and optional frontmatter fields that carry a page&#x27;s metadata, such as title, description, and pcx_content_type."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/index.md"><meta property="og:title" content="Frontmatter · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set the required and optional frontmatter fields that carry a page&#x27;s metadata, such as title, description, and pcx_content_type."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/#page","headline":"Frontmatter \u00b7 Cloudflare Style Guide","description":"Set the required and optional frontmatter fields that carry a page's metadata, such as title, description, and pcxcontenttype.","url":"https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/frontmatter/
  schema: 1
---
<p>Frontmatter contains the metadata for a page, such as the <code>title</code>. It is written as YAML, between <code>---</code>, at the top of the page.</p>
<p>For example:</p>
<pre tabindex="0"><code class="language-yaml">&#45;--&#10;title: Create a Cloudflare Tunnel&#10;pcx_content_type: how-to&#10;products:&#10;  &#45; cloudflare-tunnel&#10;description: Set the required and optional frontmatter fields that carry a page&#x27;s metadata, such as title, description, and pcx_content_type.&#10;sidebar:&#10;  order: 2&#10;&#45;--&#10;</code></pre>
<p>For more information on the available fields, refer to <a href="https://nimbus-docs.com/writing/frontmatter/">Nimbus's documentation</a>.</p>
<h2 id="required-fields">Required fields</h2>
<p>Every page with a <code>pcx_content_type</code> must include:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>title</code></td>
<td>The page title. Plain text.</td>
</tr>
<tr>
<td><code>pcx_content_type</code></td>
<td>The content type of the page. Refer to <a href="/style-guide/documentation-content-strategy/content-types/">content types</a>.</td>
</tr>
<tr>
<td><code>description</code></td>
<td>A 1-2 sentence summary used for the <code>&lt;meta name=&quot;description&quot;&gt;</code> tag. Refer to <a href="#writing-a-description">writing a description</a>.</td>
</tr>
</tbody>
</table>
<h2 id="writing-a-description">Writing a description</h2>
<p>The <code>description</code> field populates the <code>&lt;meta name=&quot;description&quot;&gt;</code> tag in the HTML head. This is the single most important metadata field for search engines, AI crawlers, and <code>llms.txt</code> consumers when deciding whether to surface or cite a page.</p>
<p>A strong description:</p>
<ul>
<li>Is 1-2 self-contained sentences (aim for 50-160 characters).</li>
<li>Names the product or feature.</li>
<li>States what the page helps the reader do or understand.</li>
<li>Works as a standalone answer snippet when extracted from the page.</li>
</ul>
<p>Do not start with generic openers like &quot;This page describes...&quot;, &quot;Learn more about...&quot;, or &quot;This document explains...&quot;. These waste the most valuable metadata space without adding information.</p>
<p>The existing <code>summary</code> field remains useful for the on-page experience but is secondary to <code>description</code> for AI and search purposes.</p>
<h3 id="examples">Examples</h3>
<pre tabindex="0"><code class="language-yaml">description: Set the required and optional frontmatter fields that carry a page&#x27;s metadata, such as title, description, and pcx_content_type.&#10;</code></pre>
<pre tabindex="0"><code class="language-yaml">description: Set the required and optional frontmatter fields that carry a page&#x27;s metadata, such as title, description, and pcx_content_type.&#10;</code></pre>
<pre tabindex="0"><code class="language-yaml">description: Set the required and optional frontmatter fields that carry a page&#x27;s metadata, such as title, description, and pcx_content_type.&#10;</code></pre>
<pre tabindex="0"><code class="language-yaml">description: Set the required and optional frontmatter fields that carry a page&#x27;s metadata, such as title, description, and pcx_content_type.&#10;</code></pre>
<h2 id="optional-fields">Optional fields</h2>
<p>For optional fields such as <code>sidebar</code>, <code>tags</code>, <code>products</code>, <code>difficulty</code>, and <code>reviewed</code>, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/">Custom properties</a>.</p>
<p>For more information on the available fields, refer to <a href="https://nimbus-docs.com/writing/frontmatter/">Nimbus's documentation</a>.</p>
