<p>A how-to explains how to complete a single task within a product. The tone is instructional and straightforward.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Use a how-to when the reader has already chosen a product and needs to complete one specific task within it. It is not:</p>
<ul>
<li><strong>A tutorial.</strong> A tutorial teaches by building something and cannot fail the reader, whereas a how-to serves someone mid-task who already knows the goal.</li>
<li><strong>A concept.</strong> If you find yourself explaining why the product works this way for more than a sentence, move it to a concept page and link to it.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: a short verb phrase in the second-person imperative. Do not use gerunds, bare nouns, or a &quot;How to&quot; prefix.</li>
<li><strong>Description</strong>: start with a verb, name the Cloudflare product or feature, and state the task it accomplishes, then add a key detail or prerequisite.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus how-to recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-how-to`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-how-to`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-how-to`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-how-to`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-how-to`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-how-to`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/build-the-page/components/steps/"><strong>Steps</strong></a> are the signature structure: the Steps component or a plain ordered list, whichever you use, must read identically in the Markdown twin. If a page has no steps, question whether it is a how-to.</li>
<li><a href="/style-guide/build-the-page/components/tabs/"><strong>Tabs and code groups</strong></a> carry variant axes such as language, platform, or CLI versus dashboard inside one canonical page. For alternative methods, pick the recommended one and link the rest, and never duplicate the page.</li>
<li><strong>Callouts</strong> warn before a destructive step. A page drowning in exception callouts has the wrong happy path.</li>
<li><strong>End in a fixed order:</strong> verification, then the irreversible closing step if there is one, then optional blocks, then Next steps. Never end on the last numbered step.</li>
<li><strong>Multi-procedure pages</strong> number their section headings (<code>## 1.</code>, <code>## 2.</code>) so the sequence is unambiguous, and cap each phase at roughly ten steps.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: how-to&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;  &#45; product-c&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Self-contained steps.</strong> Name the product area, the full command, and the exact label the reader selects, and never use a positional reference such as &quot;as configured above.&quot;</li>
<li><strong>Literal output.</strong> Keep expected output in fenced code blocks with complete, realistic values rather than truncated placeholders, because agents match on the literal text you show.</li>
<li><strong>Twin-safe steps.</strong> When a step's only copy lives inside a tab or other component, make sure it survives as labeled text in the Markdown twin so conversion cannot drop it.</li>
</ul>
