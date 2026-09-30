<p>Every product's documentation is built from the same core set of sections, so a reader who knows one product's docs can predict where to find things in another.</p>
<p>Consistency is enforced, not optional. A product may add sections that it genuinely needs, but those additions are additive: a product never renames, restructures, or redefines a core section because a different shape &quot;makes more sense&quot; for it. Keep the core the same, and grow around it.</p>
<p>This page defines the shared core at the section (folder) level. To choose the type of an individual page, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="required-sections">Required sections</h2>
<p>Every product includes at least these two pages, from its first release:</p>
<ul>
<li><a href="/style-guide/documentation-content-strategy/content-types/overview/">Overview</a>, which orients a new reader and routes them onward.</li>
<li><a href="/style-guide/documentation-content-strategy/content-types/get-started/">Get started</a>, which takes a new user from nothing to a first working result.</li>
</ul>
<h2 id="core-sections">Core sections</h2>
<p>Beyond the required pair, use these standard sections whenever your product has the content they describe. Use the standard name so that readers and agents navigate every product's docs the same way.</p>
<table>
<thead>
<tr>
<th>Section</th>
<th>What it contains</th>
<th>Related content type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Overview</td>
<td>Orients a new reader to the product and routes them onward. Required.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/overview/">Overview</a></td>
</tr>
<tr>
<td>Get started</td>
<td>The shortest path from nothing to a first working result. Required.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/get-started/">Get started</a></td>
</tr>
<tr>
<td>Concepts</td>
<td>What the product's key ideas are and why they work the way they do.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/concept/">Concept</a></td>
</tr>
<tr>
<td>Features</td>
<td>Groups the task and settings content for a major feature of the product.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/how-to/">How to</a></td>
</tr>
<tr>
<td>Guides</td>
<td>Task-focused pages for completing one specific job.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/how-to/">How to</a></td>
</tr>
<tr>
<td>Tutorials</td>
<td>End-to-end lessons where the reader builds a real project.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/tutorial/">Tutorial</a></td>
</tr>
<tr>
<td>Examples</td>
<td>Complete, runnable samples that show how something is done.</td>
<td>None</td>
</tr>
<tr>
<td>Configuration</td>
<td>The settings, values, and options for a configuration-intensive feature.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/configuration/">Configuration</a></td>
</tr>
<tr>
<td>Reference</td>
<td>Complete, neutral lookup details such as parameters, values, and options.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/reference/">Reference</a></td>
</tr>
<tr>
<td>API</td>
<td>The product's API documentation and command guidance.</td>
<td><a href="/style-guide/api-content-strategy/">API content strategy</a></td>
</tr>
<tr>
<td>Models</td>
<td>The available models and their details, for AI products.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/reference/">Reference</a></td>
</tr>
<tr>
<td>Observability</td>
<td>Testing, metrics, analytics, and local development.</td>
<td>None</td>
</tr>
<tr>
<td>Best practices</td>
<td>Recommended patterns and guidance for using the product well.</td>
<td>None</td>
</tr>
<tr>
<td>Platform</td>
<td>Product-wide pages such as pricing, limits, changelog, betas, and known issues.</td>
<td><a href="/style-guide/documentation-content-strategy/content-types/changelog/">Changelog</a></td>
</tr>
<tr>
<td>Glossary</td>
<td>The product's defined terms.</td>
<td><a href="/style-guide/build-the-page/components/glossary/">Glossary</a></td>
</tr>
</tbody>
</table>
<h2 id="structure-and-ordering-rules">Structure and ordering rules</h2>
<ul>
<li>Keep the Overview at the product root <code>index.mdx</code>. Make every other core section a folder, even when it currently holds a single page. A lone <code>get-started.mdx</code> becomes a <code>get-started/</code> folder.</li>
<li>Place the core folders before any product-specific folders, in the order given under <a href="#core-sections">Core sections</a>.</li>
<li>Give every product a Platform folder that holds at least one page, so this section is present consistently rather than only on some products.</li>
<li>Name any product-specific folder uniquely and clearly. A product-specific folder is additive: it adds to the core, and it never replaces or reshapes a core section.</li>
<li>Add sections freely, but do not edit the core. If a core section does not fit your product as written, raise it through docs governance rather than renaming or restructuring it locally.</li>
</ul>
<h2 id="bring-an-existing-product-into-line">Bring an existing product into line</h2>
<p>Audit the product against the core, then close the gaps:</p>
<ul>
<li>Rename non-standard folders to the standard names. For example, rename a <code>getting-started</code> folder to <code>get-started</code>, and rename a <code>how-to</code> folder to the standard <code>guides</code>.</li>
<li>Fold loose files into their core folder. A single <code>concepts.mdx</code> becomes a <code>concepts/</code> folder.</li>
<li>Pull core content up to the top level when it sits inside <code>platform/</code> but belongs to a core section.</li>
<li>Create the core sections your product is missing.</li>
<li>Keep useful product-specific folders, and confirm each one is uniquely named and additive.</li>
</ul>
<h2 id="product-categories">Product categories</h2>
<p>The core applies across every product category, including Compute, Storage, AI, Media, and the vertical products. A category can share additional sections that its products all need. For example, AI products commonly add a Models section. As a product matures it keeps the same core and grows by adding sections, not by reshaping the core.</p>
