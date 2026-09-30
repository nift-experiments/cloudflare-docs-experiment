<p>A troubleshooting page pairs each failure a reader hits with its cause and the steps that resolve it, organized by symptom rather than by question. The tone is guiding, straightforward, and solution-oriented.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Troubleshooting lives in two places: inline as a &quot;What if ...&quot; callout or accordion on the page where the failure happens, and on a dedicated troubleshooting page per product area once the inline entries pass roughly five or the same failure spans several pages. Reach for it to help a reader recover from a failure. It is not:</p>
<ul>
<li><strong>A how-to.</strong> A how-to pursues a goal, whereas troubleshooting recovers from a failure.</li>
<li><strong>An error reference.</strong> A complete per-code catalog is reference material. This page covers symptoms, multi-cause problems, and the &quot;it is slow or flaky&quot; cases that error codes do not capture.</li>
<li><strong>A global FAQ.</strong> A troubleshooting page is organized by failure, not by question.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Page title</strong>: &quot;Troubleshooting&quot; followed by the product, feature, or area, as in &quot;Troubleshooting delivery&quot;.</li>
<li><strong>Entry titles</strong>: the verbatim symptom, ideally the exact error message, because &quot;Error: signature timestamp outside tolerance&quot; beats &quot;Signature problems&quot; in search and in a sidebar scan. Trim a long message to its distinctive substring of roughly 70 characters with an ASCII &quot;...&quot; marking the cut, and keep the message type such as &quot;Error:&quot;. A symptom with no message gets observable phrasing, as in &quot;Deliveries succeed but arrive twice&quot;.</li>
<li><strong>Description</strong>: state that the page fixes the common failures in the area, by symptom.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus troubleshooting recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-troubleshooting`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-troubleshooting`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-troubleshooting`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-troubleshooting`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-troubleshooting`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-troubleshooting`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><strong>Fenced code blocks</strong> carry the verbatim error message, the match target for search, readers, and retrieval. Show one realistic concrete instance with real values, and never paraphrase the message or elide its distinctive part.</li>
<li><strong>Bold Cause, Fix, and Verify labels</strong> give every entry the same internal order, so a panicking reader can skip straight to the fix.</li>
<li><a href="/style-guide/build-the-page/components/details/"><strong>Details</strong></a> accordions fit the inline form at a feature page's end, but on a dedicated page the entries stay open, because a hidden symptom is unfindable.</li>
<li><strong>What does not fit:</strong> Cards, a marketing tone, and reassurance offered without a fix.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: troubleshooting&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="organizing-entries">Organizing entries</h2>
<p>Order entries by frequency, most common failure first, and let a data-loss failure jump the queue. Keep troubleshooting inline until a product area passes roughly five entries, then move it to a dedicated page and leave a link behind at the inline site. Every workaround states its cost and names its permanent alternative. A dedicated page ends with a &quot;Still stuck?&quot; section that gives the escalation path and a collect-this-first list, which is the type's honesty clause: a page implying completeness strands the reader with the one failure it missed.</p>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Self-contained entries.</strong> Write each entry so it stands alone, because entry N is retrieved without the entry before it and without the page intro. Give it the full symptom, cause, and fix.</li>
<li><strong>Executable fixes.</strong> Structure cause and fix as declaratives an agent can run: &quot;check your configuration&quot; is not a fix, a concrete command such as <code>hookline test-event --endpoint &lt;id&gt;</code> is.</li>
<li><strong>Verbatim symptoms.</strong> Show the error message verbatim in a fenced block as one concrete instance, so search, readers, and retrieval all match on the literal text.</li>
</ul>
