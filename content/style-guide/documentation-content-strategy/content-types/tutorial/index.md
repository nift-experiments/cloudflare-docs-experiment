<p>A tutorial takes a newcomer from nothing to a working project, one visible result at a time, with the author carrying all of the responsibility. The tone is guiding, straightforward, educational, and authoritative.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a tutorial when competence requires assembling several of the product's pieces into one real project, the kind of value that shows only when features work together. It is the most expensive type to build and keep true, so reach for one deliberately. It is not:</p>
<ul>
<li><strong>A quickstart.</strong> A quickstart proves the product works in minutes, whereas a tutorial builds competence through a meaningful project in about an hour.</li>
<li><strong>A how-to.</strong> A how-to serves a competent reader who carries themselves, whereas a tutorial's reader knows nothing, so when something breaks it is the tutorial's fault.</li>
<li><strong>A concept course.</strong> A tutorial teaches by doing rather than by explaining. Link the concept instead of unfolding it.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>. For a live example, refer to <a href="/workers/tutorials/">Workers tutorials</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: a short verb phrase in the second-person imperative, named by the outcome, such as &quot;Build an order-notification service&quot;. Do not use &quot;Learn ...&quot; or &quot;Tutorial 1&quot;.</li>
<li><strong>Description</strong>: state what the reader will build and what they will be able to do afterward, then give an honest time estimate.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus tutorial recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-tutorial`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-tutorial`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-tutorial`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-tutorial`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-tutorial`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-tutorial`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/build-the-page/components/steps/"><strong>Steps</strong></a> or numbered <code>##</code> parts are the spine, and every part ends with the verbatim &quot;You should see&quot; output that proves it worked. Never skip one.</li>
<li><strong>Error-recovery prose</strong> at the points readers actually stumble is happy-path content, not an exception callout, because in a tutorial an anticipated error is not an exception.</li>
<li><a href="/style-guide/build-the-page/components/github-code/"><strong>GitHubCode</strong></a> and <a href="/style-guide/build-the-page/components/package-managers/"><strong>PackageManagers</strong></a> keep sample code and install commands pinned and in sync, and <a href="/style-guide/build-the-page/components/list-tutorials/"><strong>ListTutorials</strong></a> surfaces the tutorial in listings.</li>
<li><strong>What does not fit:</strong> Tabs and options of any kind (the author already chose the one path, and per-stack means per-page), long conceptual asides (link out instead), and anything that hides steps.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: tutorial&#10;difficulty: Beginner&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>Set <code>difficulty</code> to Beginner, Intermediate, or Advanced, and stamp <code>reviewed</code> with the date you last ran the tutorial end to end. For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="keeping-tutorials-current">Keeping tutorials current</h2>
<p>A tutorial is the most expensive type to keep true, because it must work for every reader, every time, on a cold machine, and a broken tutorial convinces a newcomer that the product itself is broken. Fewest and freshest wins, so one tested tutorial beats five stale ones. Pin every version the tutorial depends on, re-run it end to end on a clean environment each release, and stamp <code>reviewed</code> with that date.</p>
<ul>
<li><a href="/style-guide/build-the-page/components/list-tutorials/"><code>ListTutorials</code></a></li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Self-contained parts.</strong> Give every part a full-context heading, the full command, and the verbatim result, so a reader or agent landing mid-tutorial knows where they are, and never use a positional reference such as &quot;as configured above.&quot;</li>
<li><strong>Literal output.</strong> Keep every expected output in a fenced code block with complete, realistic values, because that &quot;You should see&quot; text is what agents and readers match against.</li>
<li><strong>Pinned versions.</strong> Name and pin every version in the prerequisites, so the tutorial does not silently drift off the latest release.</li>
</ul>
