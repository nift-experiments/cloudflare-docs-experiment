---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/
  description: Display inline status badges like Beta or New.
  full_title: Inline badge · Cloudflare Style Guide
  head_html: <title>Inline badge · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display inline status badges like Beta or New."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/index.md"><meta property="og:title" content="Inline badge · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display inline status badges like Beta or New."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/#page","headline":"Inline badge \u00b7 Cloudflare Style Guide","description":"Display inline status badges like Beta or New.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/inline-badge/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/inline-badge/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="recommendation-avoid-inline-badges">Recommendation: Avoid inline badges</h3>
@markup("md", "content/.markup/bodies/14638.md")
</aside>
<h2 id="component">Component</h2>
<p>To adopt this styling in a React component, apply the <code>sl-badge</code> class to a <code>span</code> element.</p>
<pre tabindex="0"><code class="language-mdx">import { InlineBadge } from &#x27;~/components&#x27;;&#10;&#10;&#35;## Alpha &lt;InlineBadge preset=&quot;alpha&quot; /&gt;&#10;&#10;&#35;## Beta &lt;InlineBadge preset=&quot;beta&quot; /&gt;&#10;&#10;&#35;## Deprecated &lt;InlineBadge preset=&quot;deprecated&quot; /&gt;&#10;&#10;&#35;## Early Access &lt;InlineBadge preset=&quot;early-access&quot; /&gt;&#10;&#10;&#35;## Legacy &lt;InlineBadge preset=&quot;legacy&quot; /&gt;&#10;&#10;&#35;## Default &lt;InlineBadge text=&quot;Default&quot; /&gt;&#10;</code></pre>
<h2 id="inputs">Inputs</h2>
<p>Either <code>preset</code> or <code>text</code> and <code>variant</code> must be specified.</p>
<h3 id="presets">Presets</h3>
<ul>
<li>
<p><code>alpha</code></p>
<ul>
<li><strong>Text</strong>: <code>Alpha</code></li>
<li><strong>Variant</strong> <code>success</code></li>
</ul>
</li>
<li>
<p><code>beta</code></p>
<ul>
<li><strong>Text</strong>: <code>Beta</code></li>
<li><strong>Variant</strong> <code>caution</code></li>
</ul>
</li>
<li>
<p><code>deprecated</code></p>
<ul>
<li><strong>Text</strong>: <code>Deprecated</code></li>
<li><strong>Variant</strong> <code>danger</code></li>
</ul>
</li>
<li>
<p><code>early-access</code></p>
<ul>
<li><strong>Text</strong>: <code>Early Access</code></li>
<li><strong>Variant</strong> <code>note</code></li>
</ul>
</li>
<li>
<p><code>legacy</code></p>
<ul>
<li><strong>Text</strong>: <code>Legacy</code></li>
<li><strong>Variant</strong> <code>danger</code></li>
</ul>
</li>
</ul>
<h3 id="text">Text</h3>
<p>Any string.</p>
<h3 id="variant">Variant</h3>
<ul>
<li>
<p><code>note</code></p>
<ul>
<li><strong>Color</strong>: Blue</li>
</ul>
</li>
<li>
<p><code>tip</code></p>
<ul>
<li><strong>Color</strong>: Purple</li>
</ul>
</li>
<li>
<p><code>danger</code></p>
<ul>
<li><strong>Color</strong>: Red</li>
</ul>
</li>
<li>
<p><code>caution</code></p>
<ul>
<li><strong>Color</strong>: Orange</li>
</ul>
</li>
<li>
<p><code>success</code></p>
<ul>
<li><strong>Color</strong>: Green</li>
</ul>
</li>
</ul>
