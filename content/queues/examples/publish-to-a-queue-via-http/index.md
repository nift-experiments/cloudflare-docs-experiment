<p class="article-summary">Publish to a Queue directly via HTTP.</p>
<p>The following example shows you how to publish messages to a Queue from any HTTP client, using a Cloudflare API token to authenticate.</p>
<p>This allows you to write to a Queue from any service or programming language that supports HTTP, including Go, Rust, Python or even a Bash script.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/queues/get-started/#3-create-a-queue">queue created</a> via the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> or the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</li>
<li>A Cloudflare API token with the <code>Queues Edit</code> permission.</li>
</ul>
<h3 id="1-send-a-test-message"><ol>
<li>Send a test message</li>
</ol></h3>
<p>To make sure you successfully authenticate and write a message to your queue, use <code>curl</code> on the command line:</p>
<pre><code class="language-sh">&#35; Make sure to replace the placeholder with your shared secret&#10;curl -XPOST -H &quot;Authorization: Bearer &lt;paste-your-api-token-here&gt;&quot; &quot;https://api.cloudflare.com/client/v4/accounts/&lt;paste-your-account-id-here&gt;/queues/&lt;paste-your-queue-id-here&gt;/messages&quot; --data &#x27;{ &quot;body&quot;: { &quot;greeting&quot;: &quot;hello&quot; } }&#x27;&#10;</code></pre>
<pre><code class="language-sh">{&quot;success&quot;:true}&#10;</code></pre>
<p>This will issue a HTTP POST request, and if successful, return a HTTP 200 with a <code>success: true</code> response body.</p>
<ul>
<li>If you receive a HTTP 403, this is because your API token is invalid or does not have the <code>Queues Edit</code> permission.</li>
</ul>
<p>For full documentation about the HTTP Push API, refer to the <a href="https://developers.cloudflare.com/api/resources/queues/subresources/messages/">Cloudflare API documentation</a>.</p>
