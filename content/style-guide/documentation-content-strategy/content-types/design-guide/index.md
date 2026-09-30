---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/design-guide/
  description: Write design guides that walk a reader through planning and designing a specific Cloudflare solution and the architecture decisions behind it.
  full_title: Design guide · Cloudflare Style Guide
  head_html: <title>Design guide · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Write design guides that walk a reader through planning and designing a specific Cloudflare solution and the architecture decisions behind it."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/design-guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/design-guide/index.md"><meta property="og:title" content="Design guide · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write design guides that walk a reader through planning and designing a specific Cloudflare solution and the architecture decisions behind it."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/design-guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/design-guide/#page","headline":"Design guide \u00b7 Cloudflare Style Guide","description":"Write design guides that walk a reader through planning and designing a specific Cloudflare solution and the architecture decisions behind it.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/design-guide/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/content-types/design-guide/
  schema: 1
---
<p>A design guide helps a reader plan and design a specific solution with Cloudflare, focusing on the architecture decisions behind that solution before any configuration. A design guide is a focused subset of a <a href="/reference-architecture/">reference architecture</a>. The tone is instructional and straightforward.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a design guide when a reader needs to plan the architecture of one specific solution, understanding the decisions and trade-offs before they build it. It is not:</p>
<ul>
<li><strong>A reference architecture.</strong> A reference architecture describes a broad, product-spanning architecture, whereas a design guide narrows to planning one specific solution within it.</li>
<li><strong>A how-to.</strong> A how-to gives the steps to configure a product, whereas a design guide reasons through the architecture decisions and trade-offs before any configuration begins.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: a short verb phrase in the second-person imperative, not a gerund. Prefer &quot;Securely deliver applications with Cloudflare&quot; over &quot;Securely delivering applications&quot;.</li>
<li><strong>Description</strong>: name the solution the reader will plan and design, the Cloudflare products involved, and the architecture decisions covered.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Copy this skeleton and adapt it to your solution:</p>
<pre tabindex="0"><code>&#45;--&#10;title: &lt;Verb phrase naming the solution to plan&gt;&#10;description: Plan and design &lt;solution&gt; with &lt;Cloudflare products&gt;, covering &lt;the architecture decisions&gt;.&#10;pcx_content_type: design-guide&#10;sidebar:&#10;  order: 10&#10;products:&#10;  &#45; product-a&#10;&#45;--&#10;&#10;Open with two or three paragraphs describing the subject matter and the end state of the solution.&#10;&#10;&#35;# Intended audience&#10;&#10;Summarize who the guide is for and what they will learn.&#10;&#10;&#35;# &lt;Architecture decision or design area&gt;&#10;&#10;Describe the design and the decisions and trade-offs behind it, include a diagram of the architecture, and link out to the how-tos and tutorials that implement it.&#10;&#10;&#35;# Related links&#10;&#10;Point to the reference architecture and product documentation the design draws on.&#10;</code></pre>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/introductions/#introduction"><strong>Introduction</strong></a> opens with two to three paragraphs describing the subject matter and the end state of the solution the guide details.</li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/introductions/#intended-audience"><strong>Intended audience</strong></a> summarizes who the guide is for and what they will learn.</li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/#diagrams"><strong>Diagrams</strong></a> show the architecture, which is central to a design guide.</li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/"><strong>Notes and warnings</strong></a> flag caveats and trade-offs that affect how the design applies.</li>
<li><a href="/style-guide/style-and-grammar/formatting/structure/links/"><strong>Related links</strong></a> point to the reference architecture and product documentation the design draws on.</li>
<li><strong>What does not fit:</strong> step-by-step configuration procedures. A design guide plans the solution, so link out to the how-tos and tutorials that implement it.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre tabindex="0"><code class="language-yaml">pcx_content_type: design-guide&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="examples">Examples</h2>
<ul>
<li><a href="/reference-architecture/design-guides/secure-application-delivery/">Securely deliver applications with Cloudflare</a></li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Design, not steps.</strong> Describe the architecture and the decisions behind it, linking out to the how-tos and tutorials that implement them, because a design guide is a plan an agent reasons from, not a procedure it runs.</li>
<li><strong>State the end state.</strong> Describe the finished solution the guide produces up front, so a reader or agent knows the target before following the design.</li>
<li><strong>Name the audience and assumptions.</strong> State who the guide is for and the infrastructure it assumes, because a design guide is only actionable for a reader with the right context.</li>
</ul>
