<p><a href="/ai-search/">AI Search</a> returns the source chunks it uses to generate an answer. Use those chunks to show citations, references, or source links in your application.</p>
<p>This guide shows how to build a <a href="/workers/">Cloudflare Worker</a> that returns an AI-generated answer with the documents that informed it. Use this pattern when you want users to verify answers, inspect source material, or debug retrieval quality.</p>
<h2 id="what-you-will-build">What you will build</h2>
<p>You will create a Worker endpoint that:</p>
<ul>
<li>Sends a user question to <code>chatCompletions()</code></li>
<li>Returns the generated answer with source identifiers, snippets, metadata, and relevance scores</li>
<li>Groups repeated chunks into one citation per source document</li>
<li>Handles citations for standard and streaming responses</li>
</ul>
<h2 id="how-citations-work">How citations work</h2>
<p>AI Search retrieves source chunks before it generates an answer:</p>
<ol>
<li>Finds matching chunks from your indexed documents.</li>
<li>Sends those chunks to the model as context.</li>
<li>Returns the answer and chunks in the response.</li>
</ol>
<p>Each returned chunk contains an <code>item</code> object with <code>key</code> (filename or URL), <code>timestamp</code>, and any custom <code>metadata</code> you attached during indexing. For citations, <code>item.key</code> is usually the most useful field because it identifies the source document.</p>
<p>The <code>score</code> field indicates how relevant the chunk was to the query. The <code>chunks</code> array is also available in the <code>search()</code> response, and the same approach applies.</p>
<h2 id="1-create-a-worker"><ol>
<li>Create a Worker</li>
</ol></h2>
<p>Create a Worker project for the citation examples:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- ai-search-citations</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- ai-search-citations" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare ai-search-citations</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare ai-search-citations" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest ai-search-citations</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest ai-search-citations" aria-label="Copy to clipboard">Copy</button></div></div>
<p>When prompted, choose <strong>Hello World example</strong>, <strong>Worker only</strong>, and <strong>TypeScript</strong>.</p>
<p>Move into the project directory:</p>
<pre><code class="language-sh">cd ai-search-citations&#10;</code></pre>
<h2 id="2-configure-the-binding"><ol start="2">
<li>Configure the binding</li>
</ol></h2>
<p>Add an AI Search namespace binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3031.md")
</div>
<p>This binding lets your Worker access AI Search instances in the <code>default</code> namespace. The examples use an instance named <code>my-instance</code>.</p>
<p>If you do not have an instance yet, create one and add content before you run the Worker. To create an instance with Wrangler, refer to <a href="/ai-search/get-started/wrangler/">Wrangler commands</a>.</p>
<h2 id="3-display-citations-from-chat-completions"><ol start="3">
<li>Display citations from chat completions</li>
</ol></h2>
<p>Start with the simplest citation pattern: return the generated answer and a list of source documents in the same JSON response.</p>
<p>Replace the contents of <code>src/index.ts</code> with the following Worker code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3032.md")
</div>
<p>The response looks like:</p>
<pre><code class="language-json">{&#10;	&quot;answer&quot;: &quot;Cloudflare is a global network that provides security, performance, and reliability services...&quot;,&#10;	&quot;citations&quot;: [&#10;		{&#10;			&quot;index&quot;: 1,&#10;			&quot;source&quot;: &quot;docs/what-is-cloudflare.md&quot;,&#10;			&quot;score&quot;: 0.92,&#10;			&quot;snippet&quot;: &quot;Cloudflare is one of the world&#x27;s largest networks. Today, businesses, non-profits, bloggers...&quot;,&#10;			&quot;metadata&quot;: {&#10;				&quot;folder&quot;: &quot;docs&quot;&#10;			}&#10;		},&#10;		{&#10;			&quot;index&quot;: 2,&#10;			&quot;source&quot;: &quot;blog/intro-to-cloudflare.md&quot;,&#10;			&quot;score&quot;: 0.85,&#10;			&quot;snippet&quot;: &quot;Cloudflare provides a broad range of services to businesses of all sizes...&quot;,&#10;			&quot;metadata&quot;: {&#10;				&quot;folder&quot;: &quot;blog&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h2 id="4-deduplicate-citations-by-source"><ol start="4">
<li>Deduplicate citations by source</li>
</ol></h2>
<p>Multiple chunks can come from the same document. Group them by <code>item.key</code> to show one citation per source document.</p>
<p>To show one citation per source, update <code>src/index.ts</code> to group chunks by source document:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3033.md")
</div>
<h2 id="5-parse-citations-from-a-streaming-response"><ol start="5">
<li>Parse citations from a streaming response</li>
</ol></h2>
<p>When using <code>stream: true</code>, the chunks are sent as a separate Server-Sent Events (SSE) event named <code>chunks</code> before the streamed answer begins. Parse this event to show citations before the full answer finishes streaming.</p>
<p>To show citations before the full answer finishes streaming, update <code>src/index.ts</code> to transform the stream:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3034.md")
</div>
<h2 id="6-use-scoring-details-to-rank-citations"><ol start="6">
<li>Use scoring details to rank citations</li>
</ol></h2>
<p>Each chunk includes a <code>scoring_details</code> object with a breakdown of how it was scored. Use these details to filter out low-quality citations or display confidence indicators.</p>
<p>To filter citations by relevance, update <code>src/index.ts</code> to use score fields:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3035.md")
</div>
<h2 id="use-citation-fields">Use citation fields</h2>
<p>Each chunk in the <code>chunks</code> array can include the following fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>string</td>
<td>Unique identifier for the chunk.</td>
</tr>
<tr>
<td><code>type</code></td>
<td>string</td>
<td>Content type, typically <code>text</code>.</td>
</tr>
<tr>
<td><code>score</code></td>
<td>number</td>
<td>Overall relevance score between 0 and 1.</td>
</tr>
<tr>
<td><code>text</code></td>
<td>string</td>
<td>The text content of the chunk.</td>
</tr>
<tr>
<td><code>item.key</code></td>
<td>string</td>
<td>The file path or URL of the source document.</td>
</tr>
<tr>
<td><code>item.timestamp</code></td>
<td>number</td>
<td>Unix timestamp of when the item was last indexed.</td>
</tr>
<tr>
<td><code>item.metadata</code></td>
<td>object</td>
<td>Custom metadata associated with the source item.</td>
</tr>
<tr>
<td><code>scoring_details.vector_score</code></td>
<td>number</td>
<td>Semantic similarity score (0 to 1).</td>
</tr>
<tr>
<td><code>scoring_details.keyword_score</code></td>
<td>number</td>
<td>BM25 keyword match score. Present when using hybrid or keyword retrieval.</td>
</tr>
<tr>
<td><code>scoring_details.keyword_rank</code></td>
<td>number</td>
<td>Keyword rank position.</td>
</tr>
<tr>
<td><code>scoring_details.vector_rank</code></td>
<td>number</td>
<td>Vector rank position.</td>
</tr>
<tr>
<td><code>scoring_details.reranking_score</code></td>
<td>number</td>
<td>Reranking score (0 to 1). Present when reranking is enabled.</td>
</tr>
<tr>
<td><code>scoring_details.fusion_method</code></td>
<td>string</td>
<td>Fusion method used (<code>rrf</code> or <code>max</code>). Present when using hybrid retrieval.</td>
</tr>
</tbody>
</table>
<p>For multi-instance searches, each chunk also includes an <code>instance_id</code> field identifying which instance it came from. To search or chat across multiple instances, refer to <a href="/ai-search/api/search/workers-binding/#namespace-methods">namespace methods</a>.</p>
