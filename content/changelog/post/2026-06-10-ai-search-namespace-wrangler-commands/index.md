<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 10, 2026</time><h2 id="post-title">Manage AI Search namespaces with Wrangler CLI</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports namespace-level Wrangler commands, making it easier to manage <a href="/ai-search/concepts/namespaces/">namespaces</a> from your terminal, scripts, and agent workflows.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search namespace list</code></td>
<td>List AI Search namespaces</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace create</code></td>
<td>Create a new AI Search namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace get</code></td>
<td>Get details for a namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace update</code></td>
<td>Update a namespace description</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace delete</code></td>
<td>Delete an AI Search namespace</td>
</tr>
</tbody>
</table>
<p>Create a namespace for a new application or tenant directly from the CLI:</p>
<pre><code class="language-sh">wrangler ai-search namespace create docs-production --description &quot;Production documentation search&quot;&#10;</code></pre>
<p>List namespaces with pagination or filter by name or description:</p>
<pre><code class="language-sh">wrangler ai-search namespace list --search docs --page 1 --per-page 10&#10;</code></pre>
<p>Use <code>--json</code> with <code>list</code>, <code>create</code>, <code>get</code>, and <code>update</code> to return structured output that automation and AI agents can parse directly.</p>
<p>Instance-level commands also now support a <code>--namespace</code> flag, so you can interact with instances inside a specific namespace from the CLI:</p>
<pre><code class="language-sh">wrangler ai-search list --namespace docs-production&#10;</code></pre>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>
</div></article></div>
