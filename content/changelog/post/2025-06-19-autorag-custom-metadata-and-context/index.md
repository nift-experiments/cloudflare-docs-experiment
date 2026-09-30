<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 19, 2025</time><h2 id="post-title">View custom metadata in responses and guide AI-search with context in AutoRAG</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>In <a href="/ai-search/">AutoRAG</a>, you can now view your object's custom metadata in the response from <a href="/ai-search/api/search/workers-binding/"><code>/search</code></a> and <a href="/ai-search/api/search/workers-binding/"><code>/ai-search</code></a>, and optionally add a <code>context</code> field in the custom metadata of an object to provide additional guidance for AI-generated answers.</p>
<p>You can add <a href="/r2/api/workers/workers-api-reference/#r2putoptions">custom metadata</a> to an object when uploading it to your R2 bucket.</p>
<h4 id="object-s-custom-metadata-in-search-responses">Object's custom metadata in search responses</h4>
<p>When you run a search, AutoRAG now returns any custom metadata associated with the object. This metadata appears in the response inside <code>attributes</code> then <code>file</code> , and can be used for downstream processing.</p>
<p>For example, the <code>attributes</code> section of your search response may look like:</p>
<pre><code class="language-json">{&#10;	&quot;attributes&quot;: {&#10;		&quot;timestamp&quot;: 1750001460000,&#10;		&quot;folder&quot;: &quot;docs/&quot;,&#10;		&quot;filename&quot;: &quot;launch-checklist.md&quot;,&#10;		&quot;file&quot;: {&#10;			&quot;url&quot;: &quot;https://wiki.company.com/docs/launch-checklist&quot;,&#10;			&quot;context&quot;: &quot;A checklist for internal launch readiness, including legal, engineering, and marketing steps.&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="add-a-context-field-to-guide-llm-answers">Add a <code>context</code> field to guide LLM answers</h4>
<p>When you include a custom metadata field named <code>context</code>, AutoRAG attaches that value to each chunk of the file. When you run an <code>/ai-search</code> query, this <code>context</code> is passed to the LLM and can be used as additional input when generating an answer.</p>
<p>We recommend using the <code>context</code> field to describe supplemental information you want the LLM to consider, such as a summary of the document or a source URL. If you have several different metadata attributes, you can join them together however you choose within the <code>context</code> string.</p>
<p>For example:</p>
<pre><code class="language-json">{&#10;	&quot;context&quot;: &quot;summary: &#x27;Checklist for internal product launch readiness, including legal, engineering, and marketing steps.&#x27;; url: &#x27;https://wiki.company.com/docs/launch-checklist&#x27;&quot;&#10;}&#10;</code></pre>
<p>This gives you more control over how your content is interpreted, without requiring you to modify the original contents of the file.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>
</div></article></div>
