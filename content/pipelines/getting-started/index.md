<p>This guide will instruct you through:</p>
<ul>
<li>Creating an <a href="/r2/api/tokens/">API token</a> needed for pipelines to authenticate with your data catalog.</li>
<li>Creating your first pipeline with a simple ecommerce schema that writes to an <a href="https://iceberg.apache.org/">Apache Iceberg</a> table managed by R2 Data Catalog.</li>
<li>Sending sample ecommerce data via HTTP endpoint.</li>
<li>Validating data in your bucket and querying it with R2 SQL.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/636.md")
</div></details>
<h2 id="1-create-an-api-token"><ol>
<li>Create an API token</li>
</ol></h2>
<p>Pipelines must authenticate to R2 Data Catalog with an <a href="/r2/api/tokens/">R2 API token</a> that has catalog and R2 permissions.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/637.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/635.md")
</aside>
<h2 id="2-create-your-first-pipeline"><ol start="2">
<li>Create your first pipeline</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/642.md")
</div></div>
<h2 id="3-send-sample-data"><ol start="3">
<li>Send sample data</li>
</ol></h2>
<p>Send ecommerce events to your pipeline's HTTP endpoint:</p>
<pre><code class="language-bash">curl -X POST https://{stream-id}.ingest.cloudflare.com \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;[&#10;    {&#10;      &quot;user_id&quot;: &quot;user_12345&quot;,&#10;      &quot;event_type&quot;: &quot;purchase&quot;,&#10;      &quot;product_id&quot;: &quot;widget-001&quot;,&#10;      &quot;amount&quot;: 29.99&#10;    },&#10;    {&#10;      &quot;user_id&quot;: &quot;user_67890&quot;,&#10;      &quot;event_type&quot;: &quot;view_product&quot;,&#10;      &quot;product_id&quot;: &quot;widget-002&quot;&#10;    },&#10;    {&#10;      &quot;user_id&quot;: &quot;user_12345&quot;,&#10;      &quot;event_type&quot;: &quot;add_to_cart&quot;,&#10;      &quot;product_id&quot;: &quot;widget-003&quot;,&#10;      &quot;amount&quot;: 15.50&#10;    }&#10;  ]&#x27;&#10;</code></pre>
<p>Replace <code>{stream-id}</code> with your actual stream endpoint from the pipeline setup.</p>
<h2 id="4-validate-data-in-your-bucket"><ol start="4">
<li>Validate data in your bucket</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/643.md")
</div>
<h2 id="5-query-your-data-using-r2-sql"><ol start="5">
<li>Query your data using R2 SQL</li>
</ol></h2>
<p>Set up your environment to use R2 SQL:</p>
<pre><code class="language-bash">export WRANGLER_R2_SQL_AUTH_TOKEN=YOUR_API_TOKEN&#10;</code></pre>
<p>Or create a <code>.env</code> file with:</p>
<pre><code class="language-txt">WRANGLER_R2_SQL_AUTH_TOKEN=YOUR_API_TOKEN&#10;</code></pre>
<p>Where <code>YOUR_API_TOKEN</code> is the token you created in step 1. For more information on setting environment variables, refer to <a href="/workers/wrangler/system-environment-variables/">Wrangler system environment variables</a>.</p>
<p>Query your data:</p>
<pre><code class="language-bash">npx wrangler r2 sql query &quot;YOUR_WAREHOUSE_NAME&quot; &quot;&#10;SELECT&#10;    user_id,&#10;    event_type,&#10;    product_id,&#10;    amount&#10;FROM default.ecommerce&#10;WHERE event_type = &#x27;purchase&#x27;&#10;LIMIT 10&quot;&#10;</code></pre>
<p>Replace <code>YOUR_WAREHOUSE_NAME</code> with the warehouse name noted during pipeline setup. You can find it in the Cloudflare dashboard under <strong>R2 object storage</strong> &gt; your bucket &gt; <strong>Settings</strong> &gt; <strong>R2 Data Catalog</strong>.</p>
<p>You can also query this table with any engine that supports Apache Iceberg. To learn more about connecting other engines to R2 Data Catalog, refer to <a href="/r2-data-catalog/config-examples/">Connect to Iceberg engines</a>.</p>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/pipelines/streams/"><h3 id="card-streams-pipelines-streams">Streams</h3><p>Learn about configuring streams for data ingestion.</p></a></p>
<p><a class="nb-card nb-link-card" href="/pipelines/pipelines/"><h3 id="card-pipelines-pipelines-pipelines">Pipelines</h3><p>Understand SQL transformations and pipeline configuration.</p></a></p>
<p><a class="nb-card nb-link-card" href="/pipelines/sinks/"><h3 id="card-sinks-pipelines-sinks">Sinks</h3><p>Configure data destinations and output formats.</p></a></p>
<p><a class="nb-card nb-link-card" href="/pipelines/examples/"><h3 id="card-examples-pipelines-examples">Examples</h3><p>Browse end-to-end examples that show how to build with Pipelines.</p></a></p>
