<p>We have various approaches for making our content visible to AI as well as making sure it's easily consumed in a plain-text format.</p>
<h2 id="ai-discoverability">AI discoverability</h2>
<p>The primary proposal in this space is <a href="https://llmstxt.org/"><code>llms.txt</code></a>, offering a well-known path for a Markdown list of all your pages.</p>
<p>We have implemented <code>llms.txt</code> and <code>llms-full.txt</code> as follows:</p>
<ul>
<li><a href="/llms.txt"><code>llms.txt</code></a> — A directory of all Cloudflare documentation products, grouped by category. Each entry links to that product's own <code>llms.txt</code> — for example, <a href="/workers/llms.txt"><code>/workers/llms.txt</code></a> — which lists every page for that product in Markdown format.</li>
<li><a href="/llms-full.txt"><code>llms-full.txt</code></a> — The full contents of all Cloudflare documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models. We also provide a <code>llms-full.txt</code> file on a per-product basis — for example, <a href="/workers/llms-full.txt"><code>/workers/llms-full.txt</code></a>.</li>
</ul>
<p>To obtain a Markdown version of a single documentation page, you can:</p>
<ul>
<li>
<p>Send a request to <code>/$page/index.md</code> — Add <code>/index.md</code> to the end of any page to get the Markdown version. For example, <a href="/docs-for-agents/index.md"><code>/docs-for-agents/index.md</code></a>.</p>
</li>
<li>
<p>Send a request to any page with an <code>Accept: text/markdown</code> header — Uses <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> to convert the page to Markdown at the network layer. For example:</p>
</li>
</ul>
<pre><code class="language-bash">curl &quot;https://developers.cloudflare.com/docs-for-agents/&quot; \&#10;  &#45;-header &quot;Accept: text/markdown&quot;&#10;</code></pre>
<p>Both methods return the same Markdown output, powered by <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a>.</p>
<p>In the top right of this page, you will see a <code>Page options</code> button where you can copy the current page as Markdown that can be given to your LLM of choice.</p>
<div class="nb-width">
@markup("md", "content/.markup/bodies/14608.md")
</div>
<h2 id="textual-representation-of-interactive-elements">Textual representation of interactive elements</h2>
<p>HTML is easily parsed - after all, the browser has to parse it to decide how to render the page you're reading now - it tends to not be very <em>portable</em>. This limitation is especially painful in an AI context, because all the extra presentation information consumes additional tokens.</p>
<p>For example, given our <a href="/style-guide/build-the-page/components/tabs/"><code>Tabs</code></a>, the panels are hidden until the tab itself is clicked:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14611.md")
</div></div>
<p>If we run the resulting HTML from this component through a solution like <a href="https://www.npmjs.com/package/turndown"><code>turndown</code></a>:</p>
<pre><code class="language-md">&#45; [One](#tab-panel-6)&#10;&#45; [Two](#tab-panel-7)&#10;&#10;One Content&#10;&#10;Two Content&#10;</code></pre>
<p>The references to the panels <code>id</code>, usually handled by JavaScript, are visible but non-functional.</p>
<p>The primary answer or core instruction should always appear in the main content flow, not exclusively inside a tab or collapsible section.</p>
<p>Use tabs for platform-specific variations (for example, Dashboard versus API versus Terraform) only after stating the general concept. Use Details for supplementary information, not for the primary answer.</p>
<h3 id="turning-our-components-into-markdownable-html">Turning our components into &quot;Markdownable&quot; HTML</h3>
<p>To solve this, we use <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a>, which converts HTML to Markdown at the Cloudflare network layer. It handles:</p>
<ul>
<li>Removing non-content tags (<code>script</code>, <code>style</code>, <code>link</code>, etc.)</li>
<li>Transforming interactive components like <code>Tabs</code> into standard unordered lists</li>
<li>Adapting code block HTML into clean Markdown fenced code blocks</li>
</ul>
<p>Taking the <code>Tabs</code> example from the previous section, Markdown for Agents will give us a normal unordered list with the content properly associated with a given list item:</p>
<pre><code class="language-md">&#45; One&#10;&#10;  One Content&#10;&#10;&#45; Two&#10;&#10;  Two Content&#10;</code></pre>
<p>You can request any page as Markdown in two ways:</p>
<ul>
<li>Send a request with an <code>Accept: text/markdown</code> header:</li>
</ul>
<pre><code class="language-bash">curl &quot;https://developers.cloudflare.com/docs-for-agents/&quot; \&#10;  &#45;-header &quot;Accept: text/markdown&quot;&#10;</code></pre>
<ul>
<li>Append <code>index.md</code> to the URL — for example, <a href="/docs-for-agents/index.md"><code>/docs-for-agents/index.md</code></a></li>
</ul>
<h3 id="saving-on-tokens">Saving on tokens</h3>
<p>Most AI pricing is around input &amp; output tokens and Markdown greatly reduces the amount of input tokens required.</p>
<p>For example, let's take a look at the amount of tokens required for the <a href="/workers/get-started/guide/">Workers Get Started</a> using <a href="https://platform.openai.com/tokenizer">OpenAI's tokenizer</a>:</p>
<ul>
<li>HTML: 15,229 tokens</li>
<li>Markdown: 2,110 tokens (7.22x less than HTML)</li>
</ul>
<p>When providing our content to AI, we can see a real-world ~7x saving in input tokens cost.</p>
<h2 id="curating-content">Curating content</h2>
<p>Other than the work making our content <a href="#ai-discoverability">discoverable</a>, most of the other work of making content for AI aligns with SEO or content best practices, such as:</p>
<ul>
<li>Using semantic HTML</li>
<li>Adding headings</li>
<li>Reducing inconsistencies in naming or outdated information</li>
</ul>
<p>For more details, refer to <a href="https://developers.google.com/search/docs/appearance/ai-features#seo-best-practices">Google's AI guidance</a>.</p>
<h3 id="noindex-directives"><code>noindex</code> directives</h3>
<p>The only <em>special</em> work we have done is adding a <a href="https://developers.google.com/search/docs/crawling-indexing/block-indexing"><code>noindex</code> directives</a> to specific types of content (via a <a href="/style-guide/build-the-page/frontmatter/custom-properties/#noindex">frontmatter tag</a>).</p>
<pre><code class="language-html">&lt;meta name=&quot;robots&quot; content=&quot;noindex&quot;&gt;&#10;</code></pre>
<p>For example, we have certain pages that discuss deprecated features, such as <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/">Wrangler 1</a>. While technically accurate, they are no longer advisable to follow and could potentially confuse AI outputs.</p>
<p>At the moment, it's unclear whether all AI crawlers will respect these directives, but it's the only signal we have to exclude something from their indexing (and we do not want to set up <a href="/waf/">WAF</a> rules for individual pages).</p>
