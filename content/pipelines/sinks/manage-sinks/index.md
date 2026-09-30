<p>Learn how to:</p>
<ul>
<li>Create and configure sinks for data storage</li>
<li>View sink configuration</li>
<li>Delete sinks when no longer needed</li>
</ul>
<h2 id="create-a-sink">Create a sink</h2>
<p>Sinks are made available to pipelines as SQL tables using the sink name (e.g., <code>INSERT INTO my_sink SELECT * FROM my_stream</code>).</p>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11102.md")
</div>
<h3 id="wrangler-cli">Wrangler CLI</h3>
<p>To create a sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-create"><code>pipelines sinks create</code></a> command:</p>
<pre><code class="language-bash">npx wrangler pipelines sinks create &lt;SINK_NAME&gt; \&#10;  &#45;-type r2 \&#10;  &#45;-bucket my-bucket \&#10;</code></pre>
<p>For sink-specific configuration options, refer to <a href="/pipelines/sinks/available-sinks/">Available sinks</a>.</p>
<p>Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-setup"><code>pipelines setup</code></a> command:</p>
<pre><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<h2 id="view-sink-configuration">View sink configuration</h2>
<h3 id="dashboard-1">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11103.md")
</div>
<h3 id="wrangler-cli-1">Wrangler CLI</h3>
<p>To view a specific sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-get"><code>pipelines sinks get</code></a> command with either the sink ID or sink name:</p>
<pre><code class="language-bash">npx wrangler pipelines sinks get &lt;SINK_NAME_OR_ID&gt;&#10;</code></pre>
<p>To list all sinks in your account, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-list"><code>pipelines sinks list</code></a> command:</p>
<pre><code class="language-bash">npx wrangler pipelines sinks list&#10;</code></pre>
<h2 id="delete-a-sink">Delete a sink</h2>
<h3 id="dashboard-2">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11104.md")
</div>
<h3 id="wrangler-cli-2">Wrangler CLI</h3>
<p>To delete a sink, run the <a href="/workers/wrangler/commands/pipelines/#pipelines-sinks-delete"><code>pipelines sinks delete</code></a> command:</p>
<pre><code class="language-bash">npx wrangler pipelines sinks delete &lt;SINK_ID&gt;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11101.md")
</aside>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Sinks cannot be modified after creation. To change sink configuration, you must delete and recreate the sink.</li>
<li>The R2 Data Catalog Sink does not currently support writing to R2 buckets into a different jurisdiction.</li>
</ul>
