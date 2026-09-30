<p>Bucket locks prevent the deletion and overwriting of objects in an R2 bucket for a specified period — or indefinitely. When enabled, bucket locks enforce retention policies on your objects, helping protect them from accidental or premature deletions.</p>
<h2 id="get-started-with-bucket-locks">Get started with bucket locks</h2>
<p>Before getting started, you will need:</p>
<ul>
<li>An existing R2 bucket. If you do not already have an existing R2 bucket, refer to <a href="/r2/buckets/create-buckets/">Create buckets</a>.</li>
<li>(API only) An API token with <a href="/r2/api/tokens/#permissions">permissions</a> to edit R2 bucket configuration.</li>
</ul>
<h3 id="enable-bucket-lock-via-dashboard">Enable bucket lock via dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the bucket you would like to add bucket lock rule to.
3. Switch to the **Settings** tab, then scroll down to the **Bucket lock rules** card.
4. Select **Add rule** and enter the rule name, prefix, and retention period.
5. Select **Save changes**.
<h3 id="enable-bucket-lock-via-wrangler">Enable bucket lock via Wrangler</h3>
<ol>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="/workers/wrangler/install-and-update/">Wrangler, the Developer Platform CLI</a>.</li>
<li>Log in to Wrangler with the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code> command</a>.</li>
<li>Add a bucket lock rule to your bucket by running the <a href="/workers/wrangler/commands/r2/#r2-bucket-lock-add"><code>r2 bucket lock add</code> command</a>.</li>
</ol>
<pre><code class="language-sh">npx wrangler r2 bucket lock add &lt;BUCKET_NAME&gt; [OPTIONS]&#10;</code></pre>
<p>Alternatively, you can set the entire bucket lock configuration for a bucket from a JSON file using the <a href="/workers/wrangler/commands/r2/#r2-bucket-lock-set"><code>r2 bucket lock set</code> command</a>.</p>
<pre><code class="language-sh">npx wrangler r2 bucket lock set &lt;BUCKET_NAME&gt; --file &lt;FILE_PATH&gt;&#10;</code></pre>
<p>The JSON file should be in the format of the request body of the <a href="/api/resources/r2/subresources/buckets/subresources/locks/methods/update/">put bucket lock configuration API</a>.</p>
<h3 id="enable-bucket-lock-via-api">Enable bucket lock via API</h3>
<p>For information about getting started with the Cloudflare API, refer to <a href="/fundamentals/api/how-to/make-api-calls/">Make API calls</a>. For information on required parameters and more examples of how to set bucket lock configuration, refer to the <a href="/api/resources/r2/subresources/buckets/subresources/locks/methods/update/">API documentation</a>.</p>
<p>Below is an example of setting a bucket lock configuration (a collection of rules):</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/r2/buckets/&lt;BUCKET_NAME&gt;/lock&quot; \&#10;    &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;    &#45;H &quot;Content-Type: application/json&quot; \&#10;    &#45;d &#x27;{&#10;        &quot;rules&quot;: [&#10;            {&#10;                &quot;id&quot;: &quot;lock-logs-7d&quot;,&#10;                &quot;enabled&quot;: true,&#10;                &quot;prefix&quot;: &quot;logs/&quot;,&#10;                &quot;condition&quot;: {&#10;                    &quot;type&quot;: &quot;Age&quot;,&#10;                    &quot;maxAgeSeconds&quot;: 604800&#10;                }&#10;            },&#10;            {&#10;                &quot;id&quot;: &quot;lock-images-indefinite&quot;,&#10;                &quot;enabled&quot;: true,&#10;                &quot;prefix&quot;: &quot;images/&quot;,&#10;                &quot;condition&quot;: {&#10;                    &quot;type&quot;: &quot;Indefinite&quot;&#10;                }&#10;            }&#10;        ]&#10;    }&#x27;&#10;</code></pre>
<p>This request creates two rules:</p>
<ul>
<li><code>lock-logs-7d</code>: Objects under the <code>logs/</code> prefix are retained for 7 days (604800 seconds).</li>
<li><code>lock-images-indefinite</code>: Objects under the <code>images/</code> prefix are locked indefinitely.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11497.md")
</aside>
<h2 id="get-bucket-lock-rules-for-your-r2-bucket">Get bucket lock rules for your R2 bucket</h2>
<h3 id="dashboard">Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the bucket you would like to add bucket lock rule to.
3. Switch to the **Settings** tab, then scroll down to the **Bucket lock rules** card.
<h3 id="wrangler">Wrangler</h3>
<p>To list bucket lock rules, run the <a href="/workers/wrangler/commands/r2/#r2-bucket-lock-list"><code>r2 bucket lock list</code> command</a>:</p>
<pre><code class="language-sh">npx wrangler r2 bucket lock list &lt;BUCKET_NAME&gt;&#10;</code></pre>
<h3 id="api">API</h3>
<p>For more information on required parameters and examples of how to get bucket lock rules, refer to the <a href="/api/resources/r2/subresources/buckets/subresources/locks/methods/get/">API documentation</a>.</p>
<h2 id="remove-bucket-lock-rules-from-your-r2-bucket">Remove bucket lock rules from your R2 bucket</h2>
<h3 id="dashboard-1">Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the bucket you would like to add bucket lock rule to.
3. Switch to the **Settings** tab, then scroll down to the **Bucket lock rules** card.
4. Locate the rule you want to remove, select the `...` icon next to it, and then select **Delete**.
<h3 id="wrangler-1">Wrangler</h3>
<p>To remove a bucket lock rule, run the <a href="/workers/wrangler/commands/r2/#r2-bucket-lock-remove"><code>r2 bucket lock remove</code> command</a>:</p>
<pre><code class="language-sh">npx wrangler r2 bucket lock remove &lt;BUCKET_NAME&gt; --id &lt;RULE_ID&gt;&#10;</code></pre>
<h3 id="api-1">API</h3>
<p>To remove bucket lock rules via API, exclude them from your updated configuration and use the <a href="/api/resources/r2/subresources/buckets/subresources/locks/methods/update/">put bucket lock configuration API</a>.</p>
<h2 id="bucket-lock-rules">Bucket lock rules</h2>
<p>A bucket lock configuration can include up to 1,000 rules. Each rule specifies which objects it covers (via prefix) and how long those objects must remain locked. You can:</p>
<ul>
<li>Lock objects for a specific duration. For example, 90 days.</li>
<li>Retain objects until a certain date. For example, until January 1, 2026.</li>
<li>Keep objects locked indefinitely.</li>
</ul>
<p>If multiple rules apply to the same prefix or object key, the strictest (longest) retention requirement takes precedence.</p>
<h2 id="notes">Notes</h2>
<ul>
<li>Rules without prefix apply to all objects in the bucket.</li>
<li>Rules apply to both new and existing objects in the bucket.</li>
<li>Bucket lock rules take precedence over <a href="/r2/buckets/object-lifecycles/">lifecycle rules</a>. For example, if a lifecycle rule attempts to delete an object at 30 days but a bucket lock rule requires it be retained for 90 days, the object will not be deleted until the 90-day requirement is met.</li>
<li>A bucket cannot be emptied while any bucket lock rules are configured. Remove all lock rules before <a href="/r2/buckets/delete-buckets/#empty-a-bucket">emptying a bucket</a>. Bucket lock rules also apply when <a href="/r2/objects/delete-objects/">deleting folders</a> from the dashboard.</li>
</ul>
