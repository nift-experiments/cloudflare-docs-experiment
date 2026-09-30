<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 10, 2026</time><h2 id="post-title">Flagship API reference now available</h2>
<div class="changelog-badges"><span>flagship</span></div><div class="changelog-body"><p>The <strong><a href="/api/resources/flagship/">Flagship API reference</a></strong> is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.</p>
<p>For example, create a new boolean flag with the API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;key&quot;: &quot;new-checkout&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;default_variation&quot;: &quot;off&quot;,&#10;    &quot;variations&quot;: {&#10;      &quot;off&quot;: false,&#10;      &quot;on&quot;: true&#10;    },&#10;    &quot;rules&quot;: []&#10;  }&#x27;&#10;</code></pre>
<p>To create an API token, go to <a href="https://dash.cloudflare.com/?to=/:account/api-tokens">Account API Tokens</a> in the Cloudflare dashboard and search for Flagship.</p>
<p>The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the <a href="https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship">Flagship reference in the Cloudflare skill</a> to create and manage Flagship resources.</p>
<p>Refer to the <a href="/flagship/">Flagship documentation</a> to learn more about evaluating feature flags from your applications.</p>
</div></article></div>
