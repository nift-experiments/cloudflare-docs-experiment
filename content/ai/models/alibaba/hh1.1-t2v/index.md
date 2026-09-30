---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/
  description: alibaba/hh1.1-t2v
  full_title: HappyHorse 1.1 T2V · Cloudflare AI docs
  head_html: <title>HappyHorse 1.1 T2V · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="alibaba/hh1.1-t2v"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="HappyHorse 1.1 T2V · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="alibaba/hh1.1-t2v"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/#page","headline":"HappyHorse 1.1 T2V \u00b7 Cloudflare AI docs","description":"alibaba/hh1.1-t2v","url":"https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/alibaba/hh1.1-t2v/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="happyhorse-1-1-t2v">HappyHorse 1.1 T2V</h1>

<p><code>alibaba/hh1.1-t2v</code></p>

Alibaba's HappyHorse 1.1 text-to-video model. Generates videos from a text prompt with stronger dynamic expressiveness, better visual quality, and improved instruction following over 1.0. Configurable resolution, aspect ratio, and duration (3-15s).

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.18, @720p (per second): 0.14, @1080p (per second): 0.18</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a short video from a text prompt

<section class="model-example"><strong>Simple Text-to-Video</strong>
<p>Generate a short video from a text prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A little girl walking on the road&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/hh1.1-t2v/simple-text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/alibaba/hh1.1-t2v/simple-text-to-video.mp4&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/hh1.1-t2v&#x27;,
  { prompt: &#x27;A little girl walking on the road&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/hh1.1-t2v&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A little girl walking on the road&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 720P, 1080P</td></tr><tr><td><code>ratio</code></td><td>string</td><td>Values: 16:9, 9:16, 1:1, 4:3, 3:4</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Minimum: 3; Maximum: 15</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 2147483647</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/hh1.1-t2v/schema-input.json)
- [Output schema](/ai/models/alibaba/hh1.1-t2v/schema-output.json)

