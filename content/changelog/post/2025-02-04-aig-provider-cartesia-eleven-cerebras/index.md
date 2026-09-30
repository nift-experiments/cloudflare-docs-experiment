<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 5, 2025</time><h2 id="post-title">AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p><a href="/ai-gateway/">AI Gateway</a> has added three new providers: <a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a>, <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a>, and <a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a>, giving you more even more options for providers you can use through AI Gateway. Here's a brief overview of each:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a> provides text-to-speech models that produce natural-sounding speech with low latency.</li>
<li><a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> delivers low-latency AI inference to Meta's Llama 3.1 8B and Llama 3.3 70B models.</li>
<li><a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a> offers text-to-speech models with human-like voices in 32 languages.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/cerebras2.png" alt="Example of Cerebras log in AI Gateway" /></p>
<p>To get started with AI Gateway, just update the base URL. Here's how you can send a request to <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> using cURL:</p>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/cerebras/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer CEREBRAS_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;llama-3.3-70b&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
</div></article></div>
