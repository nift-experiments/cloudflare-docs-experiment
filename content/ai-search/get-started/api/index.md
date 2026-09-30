<p>This guide walks you through creating an AI Search instance using the REST API.</p>
<h2 id="1-create-an-api-token"><ol>
<li>Create an API token</li>
</ol></h2>
<p>You need an API token with <strong>AI Search:Edit</strong> and <strong>AI Search:Run</strong> permissions.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong>.</li>
<li>Enter a <strong>Token name</strong>, for example <code>AI Search Manager</code>.</li>
<li>Under <strong>Permissions</strong>, add two permissions:
<ul>
<li><strong>Account</strong> &gt; <strong>AI Search:Edit</strong></li>
<li><strong>Account</strong> &gt; <strong>AI Search:Run</strong></li>
</ul>
</li>
<li>Select <strong>Continue to summary</strong>, then select <strong>Create Token</strong>.</li>
<li>Copy and save the token value. This is your <code>API_TOKEN</code>.</li>
</ol>
<h2 id="2-create-an-ai-search-instance"><ol start="2">
<li>Create an AI Search instance</li>
</ol></h2>
<p>Use the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/">Create instance API</a> to create an instance. Replace <code>&lt;ACCOUNT_ID&gt;</code> with your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;&#10;  }&#x27;&#10;</code></pre>
<h3 id="connect-a-data-source-optional">Connect a data source (optional)</h3>
<p>You can create an instance that is connected to a website or R2 bucket as a data source. AI Search indexes the content automatically.</p>
<p><strong>Website:</strong></p>
<p>Automatically crawl and index a <a href="/ai-search/configuration/data-source/website/">website</a> that you own.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source&quot;: &quot;example.com&quot;&#10;  }&#x27;&#10;</code></pre>
<p><strong>R2 bucket:</strong></p>
<p>Index documents stored in an <a href="/ai-search/configuration/data-source/r2/">R2 bucket</a>. Connecting an R2 bucket requires a <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a>. If you have never created an R2-backed instance before, you need to pass the <code>token_id</code> field in the create request. Refer to the <a href="/ai-search/configuration/indexing/service-api-token/">service API token configuration</a> for setup instructions.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;r2&quot;,&#10;    &quot;source&quot;: &quot;&lt;R2_BUCKET_NAME&gt;&quot;,&#10;    &quot;token_id&quot;: &quot;&lt;SERVICE_TOKEN_ID&gt;&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="3-add-content"><ol start="3">
<li>Add content</li>
</ol></h2>
<p>If you did not create an instance that is connected to a data source, upload files using the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/">Items API</a>. You can skip this step if you connected a website or R2 bucket.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/my-instance/items&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;F &quot;file=@/path/to/your/file.pdf&quot;&#10;</code></pre>
<p>AI Search indexes uploaded files automatically.</p>
<h2 id="4-check-indexing-status"><ol start="4">
<li>Check indexing status</li>
</ol></h2>
<p>Check if your content has finished indexing.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/my-instance/stats&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h2 id="try-it-out">Try it out</h2>
<p>Once indexing is complete, run your first query.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/my-instance/search&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I get started?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>You can also test queries in the dashboard by going to your instance and selecting the <strong>Playground</strong> tab.</p>
<h2 id="add-to-your-application">Add to your application</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/api/search/workers-binding/"><h3 id="card-workers-binding-ai-search-api-search-workers-binding">Workers binding</h3><p>Query AI Search directly from your Workers code.</p></a>
<a class="nb-card nb-link-card" href="/ai-search/api/search/rest-api/"><h3 id="card-rest-api-ai-search-api-search-rest-api">REST API</h3><p>Query AI Search using HTTP requests.</p></a></p>
