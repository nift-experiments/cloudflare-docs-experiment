<p>Use the <a href="/api/resources/turnstile/">Cloudflare API</a> for programmatic widget management and automation.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, you must have:</p>
<ul>
<li>A Cloudflare API token with <code>Account:Turnstile:Edit</code> permissions</li>
<li>An account ID found in your Cloudflare dashboard</li>
</ul>
<h3 id="create-a-widget-via-the-api">Create a widget via the API</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/challenges/widgets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;domains&quot;: [&#10;    &quot;example.com&quot;&#10;  ],&#10;  &quot;mode&quot;: &quot;managed&quot;,&#10;  &quot;name&quot;: &quot;My Example Turnstile Widget&quot;&#10;}&#x27;</code></pre>
<h3 id="manage-widgets-via-the-api">Manage widgets via the API</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/challenges/widgets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/challenges/widgets/{sitekey} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/challenges/widgets/{sitekey} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;domains&quot;: [&#10;    &quot;203.0.113.1&quot;,&#10;    &quot;cloudflare.com&quot;,&#10;    &quot;blog.example.com&quot;&#10;  ],&#10;  &quot;mode&quot;: &quot;invisible&quot;,&#10;  &quot;name&quot;: &quot;blog.cloudflare.com login form&quot;,&#10;  &quot;clearance_level&quot;: &quot;interactive&quot;&#10;}&#x27;</code></pre>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/challenges/widgets/{sitekey}/rotate_secret \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;invalidate_immediately&quot;: false&#10;}&#x27;</code></pre>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/challenges/widgets/{sitekey} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
