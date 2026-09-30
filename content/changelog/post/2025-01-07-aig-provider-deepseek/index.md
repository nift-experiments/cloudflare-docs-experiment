<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 2, 2025</time><h2 id="post-title">AI Gateway adds DeepSeek as a Provider</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p><a href="/ai-gateway/"><strong>AI Gateway</strong></a> now supports <a href="/ai-gateway/usage/providers/deepseek/"><strong>DeepSeek</strong></a>, including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or <a href="/workers-ai/">Workers AI</a>, AI Gateway empowers you to:</p>
<ul>
<li><strong>Monitor</strong>: Gain actionable insights with analytics and logs.</li>
<li><strong>Control</strong>: Implement caching, rate limiting, and fallbacks.</li>
<li><strong>Optimize</strong>: Improve performance with feedback and evaluations.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/deepseek.png" alt="AI Gateway adds DeepSeek as a provider" /></p>
<p>To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer DEEPSEEK_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;deepseek-chat&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>For detailed setup instructions, see our <a href="/ai-gateway/usage/providers/deepseek/">DeepSeek provider documentation</a>.</p>
</div></article></div>
