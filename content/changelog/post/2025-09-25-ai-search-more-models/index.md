---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/
  description: New updates and improvements at Cloudflare.
  full_title: AI Search (formerly AutoRAG) now with More Models To Choose From · Changelog
  head_html: <title>AI Search (formerly AutoRAG) now with More Models To Choose From · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI Search (formerly AutoRAG) now with More Models To Choose From · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/#page","headline":"AI Search (formerly AutoRAG) now with More Models To Choose From \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-ai-search-more-models/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-25-ai-search-more-models/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 25, 2025</time><h2 id="post-title">AI Search (formerly AutoRAG) now with More Models To Choose From</h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>AutoRAG is now AI Search! The new name marks a new and bigger mission: to make world-class search infrastructure available to every developer and business.</p>
<p>With AI Search you can now use models from different providers like OpenAI and Anthropic. By attaching your provider keys to the AI Gateway linked to your AI Search instance, you can use many more models for both embedding and inference.</p>
<p>To use AI Search with other <a href="/ai-search/configuration/models/">model providers</a>:</p>
<ol>
<li><strong>Add provider keys to AI Gateway</strong>
<ol>
<li>Go to AI &gt; AI Gateway in the dashboard.</li>
<li>Select or create an AI gateway.</li>
<li>In Provider Keys, choose your provider, click Add, and enter the key.</li>
</ol>
</li>
<li><strong>Connect a gateway to AI Search</strong>: When creating a new AI Search, select the AI Gateway with your provider keys. For an existing AI Search, go to Settings and switch to a gateway that has your keys under Resources.</li>
<li><strong>Select models</strong>: Embedding models are only available to be changed when creating a new AI Search. Generation model can be selected when creating a new AI Search and can be changed at any time in Settings.</li>
</ol>
<p>Once configured, your AI Search instance will be able to reference models available through your AI Gateway when making a <code>/ai-search</code> request:</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;  async fetch(request, env) {&#10;    &#10;    // Query your AI Search instance with a natural language question to an OpenAI model&#10;    const result = await env.AI.autorag(&quot;my-ai-search&quot;).aiSearch({&#10;      query: &quot;What&#x27;s new for Cloudflare Birthday Week?&quot;,&#10;      model: &quot;openai/gpt-5&quot;&#10;    });&#10;&#10;    // Return only the generated answer as plain text&#10;    return new Response(result.response, {&#10;      headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>In the coming weeks we will also roll out updates to align the APIs with the new name. The existing APIs will continue to be supported for the time being. Stay tuned to the <a href="/changelog/product/ai-search/">AI Search Changelog</a> and <a href="https://discord.cloudflare.com/">Discord</a> for more updates!</p>
</div></article></div>
