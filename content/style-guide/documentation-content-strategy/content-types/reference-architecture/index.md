---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/
  description: Write reference architecture documentation that shows how Cloudflare products fit a customer's infrastructure and maps use cases to solutions.
  full_title: Reference architecture · Cloudflare Style Guide
  head_html: <title>Reference architecture · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Write reference architecture documentation that shows how Cloudflare products fit a customer&#x27;s infrastructure and maps use cases to solutions."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/index.md"><meta property="og:title" content="Reference architecture · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write reference architecture documentation that shows how Cloudflare products fit a customer&#x27;s infrastructure and maps use cases to solutions."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/#page","headline":"Reference architecture \u00b7 Cloudflare Style Guide","description":"Write reference architecture documentation that shows how Cloudflare products fit a customer's infrastructure and maps use cases to solutions.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/content-types/reference-architecture/
  schema: 1
---
<p>A reference architecture is a high-level design document that shows how Cloudflare products fit into a customer's existing infrastructure and maps their use cases to Cloudflare solutions. The tone is guiding and straightforward.</p>
<p>This page covers how to write one. For the published architectures themselves, refer to <a href="/reference-architecture/">Reference architectures</a>.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a reference architecture when you need to show, at the design level, how several Cloudflare products combine to fit a customer's environment and use cases. These documents are typically detailed. It is not:</p>
<ul>
<li><strong>A concept.</strong> A concept explains one idea in depth, whereas a reference architecture shows how multiple products fit together in a real environment.</li>
<li><strong>A how-to.</strong> A reference architecture describes and designs rather than giving procedural steps.</li>
</ul>
<p>For a single architecture that needs little written explanation, use a <a href="#reference-architecture-diagrams">reference architecture diagram</a> instead. For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>. For live examples, refer to <a href="/reference-architecture/architectures/load-balancing/">Cloudflare Load Balancing Reference Architecture</a>, <a href="/reference-architecture/architectures/magic-transit/">Magic Transit Reference Architecture</a>, and <a href="/reference-architecture/architectures/sase/">Evolving to a SASE architecture with Cloudflare</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: a noun phrase naming the architecture or solution, such as &quot;Cloudflare Load Balancing Reference Architecture&quot;.</li>
<li><strong>Description</strong>: name the solution and the products, say how they fit into existing infrastructure and for which use case, and name the intended audience, such as IT and security professionals.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Copy this skeleton and adapt it to your architecture:</p>
<pre tabindex="0"><code>&#45;--&#10;title: &lt;Noun phrase naming the architecture or solution&gt;&#10;description: How &lt;products&gt; fit &lt;infrastructure&gt; for &lt;use case&gt;, written for &lt;the intended audience&gt;.&#10;pcx_content_type: reference-architecture&#10;sidebar:&#10;  order: 10&#10;products:&#10;  &#45; product-a&#10;&#45;--&#10;&#10;Open with two or three paragraphs on the subject matter, then state who the document is for and what they will learn.&#10;&#10;&#35;# &lt;Architecture area&gt;&#10;&#10;Present the reference diagram with numbered callouts, and explain each element in prose so the meaning survives without the image.&#10;&#10;&#35;# &lt;Use case to solution&gt;&#10;&#10;Map the customer use case to the Cloudflare solution, and flag any caveats that affect how the architecture applies.&#10;&#10;&#35;# Related links&#10;&#10;Link the supporting how-tos, concepts, and product documentation with current routes.&#10;</code></pre>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><strong>Diagrams</strong> are the signature component: a single reference diagram reflects the overall architecture, with captions and numbered callouts explaining each element, and supporting diagrams develop specific parts.</li>
<li><strong>Introduction and intended audience</strong> open the document in prose, with two or three paragraphs on the subject matter followed by who it is for and what they will learn.</li>
<li><strong>Notes and warnings</strong> flag caveats that affect how the architecture applies.</li>
<li><a href="/style-guide/build-the-page/components/public-stats/"><strong>PublicStats</strong></a> surfaces Cloudflare network statistics where they strengthen the case for the architecture.</li>
<li><strong>What does not fit:</strong> procedural steps, because a reference architecture designs rather than instructs. Link a how-to for implementation.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre tabindex="0"><code class="language-yaml">pcx_content_type: reference-architecture&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="reference-architecture-diagrams">Reference architecture diagrams</h2>
<p>A reference architecture diagram is the lighter variant: a single diagram with numbered callouts and just enough text to explain it, for a solution that does not need a full written architecture. The tone is instructional and straightforward.</p>
<ul>
<li><strong>When to use it</strong>: reach for it when one diagram carries the solution and needs little written explanation. Choose a full reference architecture when the design needs detailed discussion.</li>
<li><strong>Title</strong>: a noun phrase, as for a full reference architecture.</li>
<li><strong>Structure</strong>: a single reference diagram, numbered callouts that explain each element, a short description of what the diagram relates to, and related links to supporting content.</li>
<li><strong>Frontmatter</strong>: set <code>pcx_content_type</code> to <code>reference-architecture-diagram</code>.</li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Text equivalents for every diagram.</strong> Explain each numbered callout in prose and give the diagram a text equivalent, because an agent cannot read the image and the meaning must survive without it.</li>
<li><strong>Literal product and use-case names.</strong> Name the exact Cloudflare products and the use case in text, not only inside the diagram, so the architecture is retrievable on its own.</li>
<li><strong>Load-bearing links.</strong> Link the supporting how-tos, concepts, and product docs with real, current routes, because the architecture points outward to implementation.</li>
</ul>
