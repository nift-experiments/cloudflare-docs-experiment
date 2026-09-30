<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 6, 2025</time><h2 id="post-title">Request timeouts and retries with AI Gateway</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway adds additional ways to handle requests - <a href="/ai-gateway/configuration/request-handling/#request-timeouts">Request Timeouts</a> and <a href="/ai-gateway/configuration/request-handling/#request-retries">Request Retries</a>, making it easier to keep your applications responsive and reliable.</p>
<p>Timeouts and retries can be used on both the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> or directly to a <a href="/ai-gateway/usage/providers/">supported provider</a>.</p>
<p><strong>Request timeouts</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-timeouts">request timeout</a> allows you to trigger <a href="/ai-gateway/configuration/fallbacks/">fallbacks</a> or a retry if a provider takes too long to respond.</p>
<p>To set a request timeout directly to a provider, add a <code>cf-aig-request-timeout</code> header.</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/workers-ai/@cf/meta/llama-3.1-8b-instruct \&#10; &#45;-header &#x27;Authorization: Bearer {cf_api_token}&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-header &#x27;cf-aig-request-timeout: 5000&#x27;&#10; &#45;-data &#x27;{&quot;prompt&quot;: &quot;What is Cloudflare?&quot;}&#x27;&#10;</code></pre>
<p><strong>Request retries</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-retries">request retry</a> automatically retries failed requests, so you can recover from temporary issues without intervening.</p>
<p>To set up request retries directly to a provider, add the following headers:</p>
<ul>
<li>cf-aig-max-attempts (number)</li>
<li>cf-aig-retry-delay (number)</li>
<li>cf-aig-backoff (&quot;constant&quot; | &quot;linear&quot; | &quot;exponential)</li>
</ul>
</div></article></div>
