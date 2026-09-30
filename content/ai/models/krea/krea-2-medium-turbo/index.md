---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/
  description: krea/krea-2-medium-turbo
  full_title: Krea 2 Medium Turbo · Cloudflare AI docs
  head_html: <title>Krea 2 Medium Turbo · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="krea/krea-2-medium-turbo"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Krea 2 Medium Turbo · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="krea/krea-2-medium-turbo"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/#page","headline":"Krea 2 Medium Turbo \u00b7 Cloudflare AI docs","description":"krea/krea-2-medium-turbo","url":"https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/krea/krea-2-medium-turbo/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Krea logo" width="48" height="48">

<h1 id="krea-2-medium-turbo">Krea 2 Medium Turbo</h1>

<p><code>krea/krea-2-medium-turbo</code></p>

The fastest Krea 2 model, built for low-cost iteration on expressive illustrations, style-driven concepts, and rapid visual exploration. Keeps the Krea 2 style system and expressive visual range but uses a distilled sampling schedule so you can move through ideas much faster. Especially useful for expressive illustration, graphic styles, typography experiments, and quick campaign or concept directions.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.krea.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.015, Per image: 0.015</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Official Krea 2 Medium Turbo example from https://docs.krea.ai/api-reference/krea/krea-2-medium-turbo.

<section class="model-example"><strong>Default</strong>
<p>Official Krea 2 Medium Turbo example from https://docs.krea.ai/api-reference/krea/krea-2-medium-turbo.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Ice citadel, frost mages and snow beasts, in a cool, fantasy anime style.&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;resolution&quot;: &quot;1K&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/krea/krea-2-medium-turbo/default.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://examples.aig.cloudflare.com/krea/krea-2-medium-turbo/default.png&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;krea/krea-2-medium-turbo&#x27;,
  {
    prompt: &#x27;Ice citadel, frost mages and snow beasts, in a cool, fantasy anime style.&#x27;,
    aspect_ratio: &#x27;1:1&#x27;,
    resolution: &#x27;1K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;krea/krea-2-medium-turbo&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;Ice citadel, frost mages and snow beasts, in a cool, fantasy anime style.&quot;,
    &quot;aspect_ratio&quot;: &quot;1:1&quot;,
    &quot;resolution&quot;: &quot;1K&quot;
  }
}&#x27;</code></pre>
<img src="https://examples.aig.cloudflare.com/krea/krea-2-medium-turbo/default.png" alt="Default">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required. Text prompt describing the image to generate.</td></tr><tr><td><code>aspect_ratio</code></td><td>string</td><td>Required. Aspect ratio of the generated image. Values: 1:1, 4:3, 3:2, 16:9, 2.35:1, 4:5, 2:3, 9:16</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Resolution scale. Values: 1K</td></tr><tr><td><code>seed</code></td><td>['number', 'null']</td><td>Random seed for reproducible generations. Pass null or omit for a random seed.</td></tr><tr><td><code>styles</code></td><td>array</td><td>Styles (typically LoRAs) to apply to the generation.</td></tr><tr><td><code>styles[].id</code></td><td>string</td><td>Required. Style (typically LoRA) identifier.</td></tr><tr><td><code>styles[].strength</code></td><td>number</td><td>Required. Style strength, between -2 and 2. Minimum: -2; Maximum: 2</td></tr><tr><td><code>image_style_references</code></td><td>array</td><td>Reference images to drive the visual style (up to 10).</td></tr><tr><td><code>image_style_references[].url</code></td><td>string</td><td>Required. URL of the reference image (max 1024 chars).</td></tr><tr><td><code>image_style_references[].strength</code></td><td>number</td><td>Style influence (0 = no influence, 1 = maximum). Default 0.5. Default: 0.5; Minimum: 0; Maximum: 1</td></tr><tr><td><code>creativity</code></td><td>string</td><td>Prompt expansion mode. `raw` disables expansion; `low`, `medium`, `high` control strength. Does not affect the K2 Intensity, Complexity, or Movement slider LoRAs. Default: low; Values: raw, low, medium, high</td></tr><tr><td><code>intensity</code></td><td>integer</td><td>K2 Intensity slider (-100 to 100). 0 disables the slider LoRA. Default: 0; Minimum: -100; Maximum: 100</td></tr><tr><td><code>complexity</code></td><td>integer</td><td>K2 Complexity slider (-100 to 100). 0 disables the slider LoRA. Default: 0; Minimum: -100; Maximum: 100</td></tr><tr><td><code>movement</code></td><td>integer</td><td>K2 Movement slider (-100 to 100). 0 disables the slider LoRA. Default: 0; Minimum: -100; Maximum: 100</td></tr><tr><td><code>moodboards</code></td><td>array</td><td>Moodboard references (currently limited to one).</td></tr><tr><td><code>moodboards[].id</code></td><td>string</td><td>Required. Moodboard identifier.</td></tr><tr><td><code>moodboards[].strength</code></td><td>number</td><td>Moodboard influence (0 = no influence, 1 = maximum). Default 0.23. Default: 0.23; Minimum: 0; Maximum: 1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required. Presigned URL for the generated image.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/krea/krea-2-medium-turbo/schema-input.json)
- [Output schema](/ai/models/krea/krea-2-medium-turbo/schema-output.json)

