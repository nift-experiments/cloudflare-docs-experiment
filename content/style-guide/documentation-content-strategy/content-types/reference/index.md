<p>A reference page enumerates the facts about one nameable surface, such as a file format, a command, or a set of limits, completely and in a uniform structure. The tone is plain and straightforward.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Reach for a reference page when a reader needs to look up exact facts about one surface. Two laws govern the type: completeness, because a missing entry breaks a reference the way a missing word breaks a dictionary, and uniformity, because every entry answers the same questions in the same order. It is not:</p>
<ul>
<li><strong>A how-to.</strong> Reference describes, never instructs. A &quot;to do this, first ...&quot; entry means you extract a how-to and link it.</li>
<li><strong>A concept.</strong> Opinion and rationale live on the concept page, so one orienting sentence with a concept link is the whole prose allowance at the top.</li>
<li><strong>A dumping ground.</strong> &quot;Miscellaneous&quot; is where facts go to become unfindable. Keep one surface per page and mirror the product's own structure.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>. For live examples, refer to <a href="/images/polish/cf-polished-statuses/">Common Cf-Polished statuses</a> and <a href="/logs/logpush/logpush-job/api-configuration/">Logpush API configuration</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: the surface's name as the reader searches for it, such as &quot;CLI commands&quot;, &quot;Event types&quot;, or &quot;Limits&quot;. Use &quot;Reference&quot; for a single standalone page, use nouns for a section with child pages, and add &quot;reference&quot; to a noun only when the bare name is ambiguous, as in &quot;Retry policy reference&quot;.</li>
<li><strong>Description</strong>: name the entry kinds the surface accepts and the fact categories each entry lists.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus reference recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-reference`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-reference`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-reference`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-reference`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-reference`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-reference`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/style-and-grammar/formatting/structure/tables/"><strong>Tables</strong></a> are the signature component: a quick-reference table before the entries makes the common lookup zero-scroll. Keep tables simple, because merged cells and meaning-by-layout break both scanning and extraction.</li>
<li><strong>Definition lines</strong> carry the same facts in a fixed order, such as type, default, required, and constraints, bolded or badged consistently across every entry.</li>
<li><a href="/style-guide/build-the-page/components/directory-listing/"><strong>DirectoryListing</strong></a> links the child pages when the reference is a section rather than a single page.</li>
<li><strong>What does not fit:</strong> Steps, Cards, and callouts (a fact that needs a warning usually belongs in the entry as a constraint), plus tabs or accordions that hide entries (a collapsed entry is invisible to search-and-grab readers and to extraction).</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: reference&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="completeness-and-source-of-truth">Completeness and source of truth</h2>
<p>A reference is complete or clearly scoped, with nothing in between, so if a subset lives elsewhere the first line says where. Give every fact exactly one source: generate values that live in code or a schema, and where generation does not yet exist, name the source so maintainers know what to diff against. Hand-maintained fact pages such as limits or quotas carry a visible <code>reviewed</code> date. When a surface passes roughly 30 entries, split it along its own seams, such as file layout or command groups, never alphabetically.</p>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Self-identifying entries.</strong> Give every entry heading its full name, such as the dotted path <code>retry.max_attempts</code> rather than <code>max_attempts</code> under a &quot;Retry&quot; heading, so a retrieved chunk carries its own identity.</li>
<li><strong>Machine-checkable values.</strong> State ranges, defaults, and limits as literal values rather than &quot;a reasonable number&quot;, and keep examples minimal in fenced blocks with realistic values.</li>
<li><strong>Nothing hidden.</strong> Keep every entry in the open, because a collapsed or tabbed entry is invisible to extraction. The Markdown twin of a reference page is the page.</li>
</ul>
