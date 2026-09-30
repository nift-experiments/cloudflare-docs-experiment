<p>Legacy pipelines, those created before September 25, 2025 via the legacy API, are on a deprecation path.</p>
<p>To check if your pipelines are legacy pipelines, view them in the dashboard under <strong>Pipelines</strong> &gt; <strong>Pipelines</strong> or run the <a href="/workers/wrangler/commands/pipelines/#pipelines-list"><code>pipelines list</code></a> command in <a href="/workers/wrangler/">Wrangler</a>. Legacy pipelines are labeled &quot;legacy&quot; in both locations.</p>
<p>New pipelines offer SQL transformations, multiple output formats, and improved architecture.</p>
<h2 id="notable-changes">Notable changes</h2>
<ul>
<li>New pipelines support SQL transformations for data processing.</li>
<li>New pipelines write to JSON, Parquet, and Apache Iceberg formats instead of JSON only.</li>
<li>New pipelines separate streams, pipelines, and sinks into distinct resources.</li>
<li>New pipelines support optional structured schemas with validation.</li>
<li>New pipelines offer configurable rolling policies and customizable partitioning.</li>
</ul>
<h2 id="moving-to-new-pipelines">Moving to new pipelines</h2>
<p>Legacy pipelines will continue to work until Pipelines is Generally Available, but new features and improvements are only available in the new pipeline architecture. To migrate:</p>
<ol>
<li>Create a new pipeline using the interactive setup:</li>
</ol>
<pre><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<ol start="2">
<li>
<p>Configure your new pipeline with the desired streams, SQL transformations, and sinks.</p>
</li>
<li>
<p>Update your applications to send data to the new stream endpoints.</p>
</li>
<li>
<p>Once verified, delete your legacy pipeline.</p>
</li>
</ol>
<p>For detailed guidance, refer to the <a href="/pipelines/getting-started/">getting started guide</a>.</p>
