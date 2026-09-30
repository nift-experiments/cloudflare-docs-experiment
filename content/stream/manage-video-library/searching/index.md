<p>You can search for videos by name through the Stream API by adding a <code>search</code> query parameter to the <a href="/api/resources/stream/methods/list/">list media files</a> endpoint.</p>
<h2 id="what-you-will-need">What you will need</h2>
<p>To make API requests you will need a <a href="https://www.cloudflare.com/a/account/my-account">Cloudflare API token</a> and your Cloudflare <a href="https://www.cloudflare.com/a/overview/">account ID</a>.</p>
<h2 id="curl-example">cURL example</h2>
<p>This example lists media where the name matches <code>puppy.mp4</code>.</p>
<pre><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream?search=puppy&quot; \&#10;     &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot;&#10;</code></pre>
