<p>A concept page builds the reader's mental model of a topic: what a thing is, why it works the way it does, and where its boundaries lie. It serves anyone getting oriented or already operating the product and filling in the why. The tone is instructional, descriptive, approachable, and supportive.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a concept page when readers keep needing the same explanation in the middle of other pages, because that recurring detour is the signal the model deserves its own home. It is not:</p>
<ul>
<li><strong>A how-to.</strong> A concept carries no procedural steps or configuration walkthroughs. Code that shows the idea is welcome, code the reader follows along with is not.</li>
<li><strong>A reference.</strong> Reference is complete and neutral, whereas a concept is selective and opinionated, so &quot;we recommend&quot; belongs here.</li>
<li><strong>An overview.</strong> An overview routes the reader onward, whereas a concept explains. Keep one concept per page.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: a concise noun phrase naming the concept. Use &quot;About&quot; for a high-level product concept page. Otherwise use a feature name, functionality, or Internet concept such as Health checks or CDN. Do not use &quot;Overview&quot;, &quot;Introduction&quot;, or &quot;How it works&quot;, because they name the genre rather than the subject. As a self-check, a good title still reads naturally with &quot;About&quot; in front of it.</li>
<li><strong>Description</strong>: state what the concept is and what it means for the reader's code or choices.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus concept recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-concept`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-concept`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-concept`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-concept`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-concept`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-concept`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><strong>Prose is the primary component.</strong> Short paragraphs, one idea per section: this is the type where writing quality carries the page.</li>
<li><strong>Diagrams and illustrative code</strong> fit when they show the model, and a diagram always ships with a text equivalent.</li>
<li><a href="/style-guide/style-and-grammar/formatting/structure/tables/"><strong>Comparison tables</strong></a> fit where there is a genuine either/or, alongside the boundaries the concept is confused with.</li>
<li><strong>What does not fit:</strong> Steps (a concept has no procedural steps or walkthroughs), Tabs (a concept does not vary by platform, and if it does it is two concepts), and Cards.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: concept&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Self-contained definition.</strong> Lead with the contract in checkable terms such as &quot;at least once&quot; or &quot;not ordered&quot; rather than reassuring adjectives, because the definition paragraphs are what an agent retrieves and quotes, so they must stand on their own.</li>
<li><strong>Literal payloads.</strong> Keep illustrative code and payloads in fenced blocks with complete, realistic values rather than paraphrase.</li>
<li><strong>Declarative boundaries.</strong> Write the boundaries as flat declarative bullets stating what the concept is not, so an agent can lift them without reconstructing the prose.</li>
</ul>
