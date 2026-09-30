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
<pre><code>&#45;--&#10;title: &lt;Noun phrase naming the architecture or solution&gt;&#10;description: How &lt;products&gt; fit &lt;infrastructure&gt; for &lt;use case&gt;, written for &lt;the intended audience&gt;.&#10;pcx_content_type: reference-architecture&#10;sidebar:&#10;  order: 10&#10;products:&#10;  &#45; product-a&#10;&#45;--&#10;&#10;Open with two or three paragraphs on the subject matter, then state who the document is for and what they will learn.&#10;&#10;&#35;# &lt;Architecture area&gt;&#10;&#10;Present the reference diagram with numbered callouts, and explain each element in prose so the meaning survives without the image.&#10;&#10;&#35;# &lt;Use case to solution&gt;&#10;&#10;Map the customer use case to the Cloudflare solution, and flag any caveats that affect how the architecture applies.&#10;&#10;&#35;# Related links&#10;&#10;Link the supporting how-tos, concepts, and product documentation with current routes.&#10;</code></pre>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><strong>Diagrams</strong> are the signature component: a single reference diagram reflects the overall architecture, with captions and numbered callouts explaining each element, and supporting diagrams develop specific parts.</li>
<li><strong>Introduction and intended audience</strong> open the document in prose, with two or three paragraphs on the subject matter followed by who it is for and what they will learn.</li>
<li><strong>Notes and warnings</strong> flag caveats that affect how the architecture applies.</li>
<li><a href="/style-guide/build-the-page/components/public-stats/"><strong>PublicStats</strong></a> surfaces Cloudflare network statistics where they strengthen the case for the architecture.</li>
<li><strong>What does not fit:</strong> procedural steps, because a reference architecture designs rather than instructs. Link a how-to for implementation.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: reference-architecture&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
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
