<p>An overview is the landing page a reader reaches first in a product area: it answers &quot;what is this, and where do I start?&quot; in one paragraph, then routes onward. The tone is accessible, welcoming, conversational, and outspoken.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Use an overview as the single landing page for a product or major product area, the page its sidebar section opens on. It is not:</p>
<ul>
<li><strong>A concept page.</strong> Move architecture and tradeoffs to a concept page and link to them. An overview orients rather than explains.</li>
<li><strong>A bare table of contents.</strong> A list of links with no orientation only duplicates the sidebar.</li>
<li><strong>A marketing page.</strong> The reader has already clicked into the docs.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>. For a live example, refer to the <a href="/argo-smart-routing/">Argo Smart Routing overview</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: the name of the product, product group, or content area, as a noun. Do not append &quot;documentation&quot;, use a gerund phrase, or use &quot;Introduction&quot;.</li>
<li><strong>Description</strong>: name the Cloudflare product and what it does for whom in one sentence, then state the plans it is available on.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus overview recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-overview`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-overview`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-overview`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-overview`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-overview`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-overview`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/build-the-page/components/cards/"><strong>Cards</strong></a> are the signature components: this is the one type where cards are the body content, because routing is the body. Keep card text to a name plus one line, because a card that explains is a concept paragraph in a box. In the Markdown twin cards flatten to link-plus-description lists, so write the one-liners so they work in both forms.</li>
<li><strong>Link lists</strong> beat cards when the grid forces padded copy, or when a group genuinely must run past the roughly five-link cap, because prose lists scan better at volume.</li>
<li><strong>What does not fit:</strong> Steps (nothing is performed here), code blocks (nothing is looked up, though inline code in the orientation line is fine), and accordions (an overview with hidden content is hiding its own map).</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: overview&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;  &#45; product-c&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="managing-overview-pages">Managing overview pages</h2>
<p>Every product or major product area must have an overview, so the answer to a weak one is always to strengthen it, never to remove it. If a page reads like a bare table of contents, add the orientation that says what the area is and where to start. Do not delete it and let the sidebar stand in.</p>
<p>The only page you hide is a structural group node: a folder that exists purely to group its children in the sidebar and was never a content page. You cannot delete a folder's <code>index.mdx</code> without a build error, so hide the placeholder and redirect readers past it by setting <code>group.hideIndex</code> to <code>true</code>:</p>
<pre><code class="language-yaml">&#45;--&#10;title: Placeholder&#10;sidebar:&#10;  group:&#10;    hideIndex: true&#10;&#45;--&#10;</code></pre>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Self-contained orientation.</strong> Write the opening paragraph so it stays accurate in isolation, because it is what an agent quotes when asked what the product is. Do not lean on the title or a later section to complete its meaning.</li>
<li><strong>Literal availability.</strong> State availability with literal plan, region, or release-stage names rather than a paraphrase.</li>
<li><strong>Load-bearing links.</strong> Use real, current routes, because a stale route here strands a reader at the front door.</li>
</ul>
