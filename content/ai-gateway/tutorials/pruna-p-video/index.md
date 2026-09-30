---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/tutorials/pruna-p-video/
  description: Learn how to call prunaai/p-video on Replicate through AI Gateway
  full_title: Use Pruna P-video through AI Gateway · Cloudflare AI Gateway docs
  head_html: <title>Use Pruna P-video through AI Gateway · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to call prunaai/p-video on Replicate through AI Gateway"><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/tutorials/pruna-p-video/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/tutorials/pruna-p-video/index.md"><meta property="og:title" content="Use Pruna P-video through AI Gateway · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to call prunaai/p-video on Replicate through AI Gateway"><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/tutorials/pruna-p-video/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="AI Gateway"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/tutorials/pruna-p-video/#page","headline":"Use Pruna P-video through AI Gateway \u00b7 Cloudflare AI Gateway docs","description":"Learn how to call prunaai/p-video on Replicate through AI Gateway","url":"https://developers.cloudflare.com/ai-gateway/tutorials/pruna-p-video/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/tutorials/pruna-p-video/
  schema: 1
---
<p>This tutorial shows how to call the <a href="https://replicate.com/prunaai/p-video">Pruna's P-video</a> model on <a href="/ai-gateway/usage/providers/replicate/">Replicate</a> through AI Gateway.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://cloudflare.com/sign-up">Cloudflare account</a></li>
<li>A <a href="https://replicate.com/">Replicate account</a> with an API token</li>
</ul>
<h2 id="1-get-a-replicate-api-token"><ol>
<li>Get a Replicate API token</li>
</ol></h2>
<ol>
<li>Go to <a href="https://replicate.com/">replicate.com</a> and sign up for an account.</li>
<li>Once logged in, go to <a href="https://replicate.com/account/api-tokens">replicate.com/settings/api-tokens</a>.</li>
<li>Select <strong>Create token</strong> and give it a name.</li>
<li>Copy the token and store it somewhere safe.</li>
</ol>
<h2 id="2-create-an-ai-gateway"><ol start="2">
<li>Create an AI Gateway</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2792.md")
</div></div>
<p>Note your <strong>Account ID</strong> and <strong>Gateway name</strong> for use in later steps.</p>
<p>To add authentication to your gateway, refer to <a href="/ai-gateway/configuration/authentication/">Authenticated Gateway</a>.</p>
<h2 id="3-construct-the-gateway-url"><ol start="3">
<li>Construct the gateway URL</li>
</ol></h2>
<p>Replace the standard Replicate API base URL with the AI Gateway URL:</p>
<pre tabindex="0"><code class="language-txt">&#35; Instead of:&#10;https://api.replicate.com/v1&#10;&#10;&#35; Use:&#10;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate&#10;</code></pre>
<p>For example, if your account ID is <code>abc123</code> and your gateway is <code>my-gateway</code>:</p>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/abc123/my-gateway/replicate&#10;</code></pre>
<h2 id="4-generate-a-video"><ol start="4">
<li>Generate a video</li>
</ol></h2>
<p>P-video predictions generally complete within 30 seconds. Because this is under Replicate's 60-second synchronous limit, you can use the <code>Prefer: wait</code> header to send a request and get the result in a single call:</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate/predictions \&#10;  &#45;-header &quot;Authorization: Bearer {replicate_api_token}&quot; \&#10;  &#45;-header &quot;cf-aig-authorization: Bearer {cloudflare_api_token}&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;Prefer: wait&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;version&quot;: &quot;prunaai/p-video&quot;,&#10;    &quot;input&quot;: {&#10;      &quot;prompt&quot;: &quot;A cat walking through a field of flowers in slow motion&quot;,&#10;      &quot;duration&quot;: 5,&#10;      &quot;aspect_ratio&quot;: &quot;16:9&quot;,&#10;      &quot;resolution&quot;: &quot;720p&quot;,&#10;      &quot;fps&quot;: 24&#10;    }&#10;  }&#x27;&#10;</code></pre>
<ul>
<li><code>Authorization</code> — your Replicate API token (authenticates with Replicate).</li>
<li><code>cf-aig-authorization</code> — your Cloudflare API token (for authenticated gateways).</li>
<li><code>Prefer: wait</code> — blocks until the prediction completes instead of returning immediately.</li>
</ul>
<p>For a full list of available input parameters, check out the <a href="https://replicate.com/prunaai/p-video">prunaai/p-video model page</a> on Replicate.</p>
<p>When the prediction completes, the response includes the <code>output</code> field with a URL to the generated video file.</p>
<h2 id="5-optional-use-async-polling-for-longer-requests"><ol start="5">
<li>(Optional) Use async polling for longer requests</li>
</ol></h2>
<p>If your request may exceed 60 seconds (for example, with longer durations or higher resolutions), use async mode instead. Send the request without the <code>Prefer: wait</code> header:</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate/predictions \&#10;  &#45;-header &quot;Authorization: Bearer {replicate_api_token}&quot; \&#10;  &#45;-header &quot;cf-aig-authorization: Bearer {cloudflare_api_token}&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;version&quot;: &quot;prunaai/p-video&quot;,&#10;    &quot;input&quot;: {&#10;      &quot;prompt&quot;: &quot;A cat walking through a field of flowers in slow motion&quot;,&#10;      &quot;duration&quot;: 5,&#10;      &quot;aspect_ratio&quot;: &quot;16:9&quot;,&#10;      &quot;resolution&quot;: &quot;720p&quot;,&#10;      &quot;fps&quot;: 24&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>The response includes a prediction <code>id</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;id&quot;: &quot;xyz789...&quot;,&#10;  &quot;status&quot;: &quot;starting&quot;,&#10;  &quot;urls&quot;: {&#10;    &quot;get&quot;: &quot;https://api.replicate.com/v1/predictions/xyz789...&quot;,&#10;    &quot;cancel&quot;: &quot;https://api.replicate.com/v1/predictions/xyz789.../cancel&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Poll the prediction status until it completes:</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate/predictions/{prediction_id} \&#10;  &#45;-header &quot;Authorization: Bearer {replicate_api_token}&quot; \&#10;  &#45;-header &quot;cf-aig-authorization: Bearer {cloudflare_api_token}&quot;&#10;</code></pre>
<p>Keep polling until <code>status</code> is <code>succeeded</code> (or <code>failed</code>). When complete, the <code>output</code> field contains a URL to the generated video file.</p>
<h2 id="next-steps">Next steps</h2>
<p>From here you can:</p>
<ul>
<li>Use <a href="/ai-gateway/observability/logging/">logging</a> to monitor requests and debug issues.</li>
<li>Set up <a href="/ai-gateway/features/rate-limiting/">rate limiting</a> to control usage.</li>
<li>Use other models on Replicate or our other <a href="/ai-gateway/usage/providers/">supported providers</a> through AI Gateway.</li>
</ul>
