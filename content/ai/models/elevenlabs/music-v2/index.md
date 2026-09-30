---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/
  description: elevenlabs/music-v2
  full_title: ElevenLabs Music v2 · Cloudflare AI docs
  head_html: <title>ElevenLabs Music v2 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="elevenlabs/music-v2"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="ElevenLabs Music v2 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="elevenlabs/music-v2"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/#page","headline":"ElevenLabs Music v2 \u00b7 Cloudflare AI docs","description":"elevenlabs/music-v2","url":"https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/elevenlabs/music-v2/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/elevenlabs.svg" alt="Elevenlabs logo" width="48" height="48">

<h1 id="elevenlabs-music-v2">ElevenLabs Music v2</h1>

<p><code>elevenlabs/music-v2</code></p>

ElevenLabs Music v2 composes songs and instrumental tracks from a prompt or detailed composition plan.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Music Generation</td></tr>
<tr><th>Terms</th><td><a href="https://elevenlabs.io/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>output_audio_seconds: 0.0025, Default (per second): 0.0025</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate an instrumental music track from a short prompt

<section class="model-example"><strong>Cinematic Instrumental</strong>
<p>Generate an instrumental music track from a short prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A warm cinematic ambient track with soft piano, subtle strings, and a hopeful mood&quot;,
    &quot;music_length_ms&quot;: 30000,
    &quot;force_instrumental&quot;: true,
    &quot;output_format&quot;: &quot;mp3_48000_192&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/elevenlabs/music-v2/cinematic-instrumental.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;state&quot;: &quot;Completed&quot;,
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://examples.aig.cloudflare.com/elevenlabs/music-v2/cinematic-instrumental.mp3&quot;
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;elevenlabs/music-v2&#x27;,
  {
    prompt: &#x27;A warm cinematic ambient track with soft piano, subtle strings, and a hopeful mood&#x27;,
    music_length_ms: 30000,
    force_instrumental: true,
    output_format: &#x27;mp3_48000_192&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;elevenlabs/music-v2&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A warm cinematic ambient track with soft piano, subtle strings, and a hopeful mood&quot;,
    &quot;music_length_ms&quot;: 30000,
    &quot;force_instrumental&quot;: true,
    &quot;output_format&quot;: &quot;mp3_48000_192&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Minimum length: 1</td></tr><tr><td><code>composition_plan</code></td><td>object</td><td></td></tr><tr><td><code>composition_plan.chunks</code></td><td>array</td><td>Required.</td></tr><tr><td><code>composition_plan.chunks[].text</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>composition_plan.chunks[].duration_ms</code></td><td>integer</td><td>Required. Minimum: 3000; Maximum: 120000</td></tr><tr><td><code>composition_plan.chunks[].positive_styles</code></td><td>array</td><td>Required.</td></tr><tr><td><code>composition_plan.chunks[].negative_styles</code></td><td>array</td><td></td></tr><tr><td><code>composition_plan.chunks[].context_adherence</code></td><td>string</td><td>Values: low, medium, high</td></tr><tr><td><code>composition_plan.chunks[].conditioning_ref</code></td><td>object</td><td></td></tr><tr><td><code>composition_plan.chunks[].conditioning_ref.song_id</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>composition_plan.chunks[].conditioning_ref.range</code></td><td>object</td><td>Required.</td></tr><tr><td><code>composition_plan.chunks[].conditioning_ref.range.start_ms</code></td><td>integer</td><td>Required. Minimum: 0; Maximum: 9007199254740991</td></tr><tr><td><code>composition_plan.chunks[].conditioning_ref.range.end_ms</code></td><td>integer</td><td>Required. Minimum: 1; Maximum: 9007199254740991</td></tr><tr><td><code>composition_plan.chunks[].condition_strength</code></td><td>string</td><td>Values: low, medium, high, xhigh</td></tr><tr><td><code>composition_plan.chunks[].song_id</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>composition_plan.chunks[].range</code></td><td>object</td><td>Required.</td></tr><tr><td><code>composition_plan.chunks[].range.start_ms</code></td><td>integer</td><td>Required. Minimum: 0; Maximum: 9007199254740991</td></tr><tr><td><code>composition_plan.chunks[].range.end_ms</code></td><td>integer</td><td>Required. Minimum: 1; Maximum: 9007199254740991</td></tr><tr><td><code>music_length_ms</code></td><td>integer</td><td>Minimum: 3000; Maximum: 600000</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Values: auto, mp3_48000_128, mp3_48000_192, mp3_48000_240, mp3_48000_320, mp3_22050_32, mp3_24000_48, mp3_44100_32, mp3_44100_64, mp3_44100_96, mp3_44100_128, mp3_44100_192, opus_48000_32, opus_48000_64, opus_48000_96, opus_48000_128, opus_48000_192</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 4294967295</td></tr><tr><td><code>force_instrumental</code></td><td>boolean</td><td></td></tr><tr><td><code>store_for_inpainting</code></td><td>boolean</td><td></td></tr><tr><td><code>sign_with_c2pa</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated music file.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/elevenlabs/music-v2/schema-input.json)
- [Output schema](/ai/models/elevenlabs/music-v2/schema-output.json)

