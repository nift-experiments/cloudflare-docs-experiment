---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/
  description: Use screenshots, diagrams, and reference diagrams effectively in documentation.
  full_title: Images and diagrams · Cloudflare Style Guide
  head_html: <title>Images and diagrams · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Use screenshots, diagrams, and reference diagrams effectively in documentation."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/index.md"><meta property="og:title" content="Images and diagrams · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use screenshots, diagrams, and reference diagrams effectively in documentation."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/#page","headline":"Images and diagrams \u00b7 Cloudflare Style Guide","description":"Use screenshots, diagrams, and reference diagrams effectively in documentation.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/
  schema: 1
---
<p>Images help a reader see a tool, a process, or an architecture. This page covers three: screenshots, diagrams, and reference diagrams. Because images cost more to maintain than text, use them intentionally.</p>
<h2 id="screenshots">Screenshots</h2>
<p>A screenshot is a picture of a software tool, in this case usually the Cloudflare dashboard. We only recommend screenshots in specific scenarios, as they have a higher maintenance cost than other types of content.</p>
<h3 id="when-to-use">When to use</h3>
<p>Use screenshots sparingly and intentionally. For example, it is appropriate to use a screenshot when the task is simple but often confuses readers or is hard to describe with words alone.</p>
<p>A canonical example is <a href="/fundamentals/account/find-account-and-zone-ids/">Find account and zone ID</a> because:</p>
<ul>
<li>It is a high driver of SEO traffic to our <a href="https://community.cloudflare.com">Community</a>.</li>
<li>We tried explaining with words alone and that did not solve the confusion.</li>
<li>It is a task specifically related to new users, who are less familiar with Cloudflare concepts or navigation patterns.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14665.md")
</aside>
<h3 id="guidelines">Guidelines</h3>
<p>Screenshots should:</p>
<ul>
<li>Maintain the original aspect-lock ratio.</li>
<li>Keep resolution at 72dpi.</li>
<li>Keep width at 500-600 pixels.</li>
<li>Avoid sharing sensitive information (you may need to edit the underlying HTML in your browser).</li>
<li>Avoid including visuals that change frequently, such as sidebar navigation.</li>
<li>Have descriptive alt text.</li>
</ul>
<h3 id="usage">Usage</h3>
<pre tabindex="0"><code class="language-mdx">![Alt text](/assets/upstream/images/$PRODUCT_NAME/$IMAGE_NAME.png)&#10;</code></pre>
<p>Add screenshots to the corresponding <code>$PRODUCT_NAME</code> folder under <a href="https://github.com/cloudflare/cloudflare-docs/tree/production//assets/upstream/images"><code>//assets/upstream/images/</code></a>. You may want to add subfolders for organizational purposes.</p>
<h3 id="maintenance">Maintenance</h3>
<p>We avoid screenshots without a clear purpose because they are difficult to maintain. This is because:</p>
<ul>
<li>The UI might change and our team might not know.</li>
<li>Even if you do know what changed, it is difficult to find which screenshots reference a particular UI flow.</li>
<li>If something changes, you need to fully re-take the screenshot to replace it. This could involve adding fake data or hiding sensitive information.</li>
</ul>
<p>For more details on how we approach this maintenance, refer to <a href="/style-guide/how-we-docs/image-maintenance/">Image maintenance</a>.</p>
<h2 id="diagrams">Diagrams</h2>
<p>Diagrams are visualizations that depict a process, architecture, or some other form of technology. They explain complex topics in a compelling way and help a reader visualize a specific solution, process, or interaction between products. Diagrams are used in all content types. We recommend either SVG files or Mermaid diagrams.</p>
<h3 id="svg-diagrams">SVG diagrams</h3>
<p>Use SVG files instead of PNG or JPEG because SVG scales well when a reader zooms in. Use clear and straightforward alt text with your SVG for use by screen readers. We optimize SVG files with a <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/scripts/optimize-svgs.ts">recurring script</a> in our repo.</p>
<p>Format an SVG like this:</p>
<pre tabindex="0"><code class="language-md">![Alt text](/link/to/image.svg &quot;Caption to go under the image&quot;)&#10;</code></pre>
<p>For example:</p>
<p><img src="/assets/upstream/images/firewall/simple-flow.png" alt="A simple flow diagram shows interactions between important elements of the design." title="An example flow diagram" /></p>
<pre tabindex="0"><code class="language-md">![A simple flow diagram shows interactions between important elements of the design.](/assets/upstream/images/firewall/simple-flow.png &quot;An example flow diagram&quot;)&#10;</code></pre>
<h3 id="mermaid-diagrams">Mermaid diagrams</h3>
<p>Use Mermaid diagrams to illustrate product or process flows. If they work for your use case, Mermaid diagrams are preferable to SVG files because they are more easily searchable and changeable. Our Mermaid diagrams are based on <a href="https://github.com/remcohaszing/rehype-mermaid/"><code>rehype-mermaid</code></a> and <a href="https://www.npmjs.com/package/mermaid"><code>mermaid</code></a>.</p>
<p>Format a Mermaid diagram like this:</p>
<pre tabindex="0"><code class="language-md">&#10;</code></pre>
<p>flowchart LR
accTitle: Tunnels diagram
accDescr: The example in this diagram has three tunnel routes. Tunnels 1 and 2 have top priority and Tunnel 3 is secondary.</p>
<p>subgraph Cloudflare
direction LR
B[Cloudflare <br/> data center]
C[Cloudflare <br/> data center]
D[Cloudflare <br/> data center]
end</p>
<p>A((User)) --&gt; Cloudflare --- E[Anycast IP]
E[Anycast IP] --&gt; F[/Tunnel 1 / <br/> priority 1/] --&gt; I{{Customer <br/> data center/ <br/> network 1}}
E[Anycast IP] --&gt; G[/Tunnel 2 / <br/> priority 1/] --&gt; J{{Customer <br/> data center/ <br/> network 2}}
E[Anycast IP] --&gt; H[/Tunnel 3 / <br/> priority 2/] --&gt; K{{Customer <br/> data center/ <br/> network 3}}</p>
<pre tabindex="0"><code>&#10;</code></pre>
<p>For example, this renders as:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Tunnels diagram&#10;accDescr: The example in this diagram has three tunnel routes. Tunnels 1 and 2 have top priority and Tunnel 3 is secondary.&#10;&#10;subgraph Cloudflare&#10;direction LR&#10;B[Cloudflare &lt;br/&gt; data center]&#10;C[Cloudflare &lt;br/&gt; data center]&#10;D[Cloudflare &lt;br/&gt; data center]&#10;end&#10;&#10;A((User)) --&gt; Cloudflare --- E[Anycast IP]&#10;E[Anycast IP] --&gt; F[/Tunnel 1 / &lt;br/&gt; priority 1/] --&gt; I{{Customer &lt;br/&gt; data center/ &lt;br/&gt; network 1}}&#10;E[Anycast IP] --&gt; G[/Tunnel 2 / &lt;br/&gt; priority 1/] --&gt; J{{Customer &lt;br/&gt; data center/ &lt;br/&gt; network 2}}&#10;E[Anycast IP] --&gt; H[/Tunnel 3 / &lt;br/&gt; priority 2/] --&gt; K{{Customer &lt;br/&gt; data center/ &lt;br/&gt; network 3}}&#10;</code></pre>
<h2 id="reference-diagram">Reference diagram</h2>
<p>A single diagram that portrays all or part of Cloudflare's platform and how Cloudflare would align with a customer's infrastructure or use case.</p>
<p><strong>Used in</strong>: <a href="/style-guide/documentation-content-strategy/content-types/reference-architecture/">Reference architecture</a>, <a href="/style-guide/documentation-content-strategy/content-types/reference-architecture/#reference-architecture-diagrams">Reference architecture diagram</a></p>
<p>Show a complete Cloudflare architecture aligned with a specific infrastructure or use case. Whenever possible, the image should be an SVG.</p>
<p>For example:</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-21.svg" alt="A fully deployed SASE solution with Cloudflare protects every aspect of your business, ensuring all access to applications is secured and all threats from the Internet mitigated." title="A fully deployed SASE solution with Cloudflare" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
