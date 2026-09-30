<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 17, 2026</time><h2 id="post-title">Reject busy synchronous inference requests</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>The <code>rejectIfBusy</code> option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.</p>
<p>Pass the option as the third argument to the Workers AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17820.md")</div>
<p>For the native REST API, add the option to the request body:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Explain capacity queues.&quot; }],&#10;    &quot;options&quot;: { &quot;rejectIfBusy&quot;: true }&#10;  }&#x27;&#10;</code></pre>
<p>Refer to <a href="/workers-ai/features/reject-if-busy/">Reject busy requests</a> for OpenAI-compatible usage and error behavior.</p>
</div></article></div>
