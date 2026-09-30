<p>A get-started page takes a new user from not using a product to a first working setup by the shortest honest path. The tone is instructional and encouraging.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a get-started page when a new user needs the shortest path from nothing to one working result, before they explore the product in depth. It is not:</p>
<ul>
<li><strong>A how-to.</strong> A how-to completes one specific task for a reader who already uses the product, whereas a get-started page delivers a new user's first success end to end.</li>
<li><strong>A tutorial.</strong> A tutorial teaches through a longer guided project, whereas a get-started page stops at the first working result and routes the reader onward.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: the page title is Get started.</li>
<li><strong>Description</strong>: name the product, summarize the first setup the reader completes, and note the key prerequisites.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus get-started recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-quickstart`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-quickstart`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-quickstart`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-quickstart`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-quickstart`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-quickstart`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/prerequisites/"><strong>Prerequisites</strong></a> list what the reader needs before starting, such as an active zone, a subscription or plan, or setup outside Cloudflare.</li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/steps-tasks-procedures/"><strong>Steps</strong></a> lead the reader to product adoption, covering the minimum setup plus the most general use case, and often reuse partials from the how-to pages.</li>
<li><a href="/style-guide/style-and-grammar/formatting/structure/links/"><strong>Links</strong></a> close the page with next steps that point the reader toward deeper configuration once they have a working setup.</li>
<li><strong>What does not fit:</strong> exhaustive configuration or edge cases. Keep those in how-tos and reference pages, and link to them.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: get-started&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="examples">Examples</h2>
<ul>
<li><a href="/waiting-room/get-started/">Waiting Room: Get started</a></li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Shortest honest path.</strong> Include only the steps that reach a first working result, because a get-started page is judged by how quickly a reader or agent reaches success, not by coverage.</li>
<li><strong>Show the result.</strong> State and show the working outcome the steps produce, so a reader or agent can verify success before moving on.</li>
<li><strong>Complete prerequisites.</strong> State exactly what the reader needs before starting, because an agent cannot begin a setup it is not equipped to reach.</li>
</ul>
