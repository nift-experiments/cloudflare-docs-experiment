---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/inworld/tts-1.5-max/
  description: inworld/tts-1.5-max
  full_title: Inworld TTS 1.5 Max · Cloudflare AI docs
  head_html: <title>Inworld TTS 1.5 Max · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="inworld/tts-1.5-max"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/inworld/tts-1.5-max/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Inworld TTS 1.5 Max · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="inworld/tts-1.5-max"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/inworld/tts-1.5-max/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/inworld/tts-1.5-max/#page","headline":"Inworld TTS 1.5 Max \u00b7 Cloudflare AI docs","description":"inworld/tts-1.5-max","url":"https://developers.cloudflare.com/ai/models/inworld/tts-1.5-max/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/inworld/tts-1.5-max/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/inworld.svg" alt="Inworld logo" width="48" height="48">

<h1 id="inworld-tts-1-5-max">Inworld TTS 1.5 Max</h1>

<p><code>inworld/tts-1.5-max</code></p>

Highest-quality text-to-speech with under 200ms latency, emotion control, and 15-language support.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Speech</td></tr>
<tr><th>Terms</th><td><a href="https://inworld.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per character: 3.5e-05</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate speech with default settings

<section class="model-example"><strong>Simple Speech</strong>
<p>Generate speech with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/simple-speech.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/simple-speech.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;inworld/tts-1.5-max&#x27;,
  {
    output_format: &#x27;mp3&#x27;,
    temperature: 1,
    text: &#x27;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&#x27;,
    timestamp_type: &#x27;none&#x27;,
    voice_id: &#x27;Dennis&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;inworld/tts-1.5-max&quot;,
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Slow Narration</strong>
<p>Slower speech for narration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;speaking_rate&quot;: 0.85,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/slow-narration.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/slow-narration.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;inworld/tts-1.5-max&#x27;,
  {
    output_format: &#x27;mp3&#x27;,
    speaking_rate: 0.85,
    temperature: 1,
    text: &#x27;In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.&#x27;,
    timestamp_type: &#x27;none&#x27;,
    voice_id: &#x27;Dennis&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;inworld/tts-1.5-max&quot;,
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;speaking_rate&quot;: 0.85,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>High Quality Audio</strong>
<p>Higher sample rate for studio quality</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;sample_rate&quot;: 48000,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;This recording is generated at studio quality for the best possible listening experience.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/high-quality-audio.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/high-quality-audio.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;inworld/tts-1.5-max&#x27;,
  {
    output_format: &#x27;mp3&#x27;,
    sample_rate: 48000,
    temperature: 1,
    text: &#x27;This recording is generated at studio quality for the best possible listening experience.&#x27;,
    timestamp_type: &#x27;none&#x27;,
    voice_id: &#x27;Dennis&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;inworld/tts-1.5-max&quot;,
  &quot;input&quot;: {
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;sample_rate&quot;: 48000,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;This recording is generated at studio quality for the best possible listening experience.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>With Text Normalization</strong>
<p>Expand numbers and abbreviations before synthesis</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;apply_text_normalization&quot;: true,
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;The meeting is at 3:30 PM on Jan 15th, 2026. Please confirm by calling 555-0123.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  },
  &quot;output&quot;: {
    &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/with-text-normalization.mp3&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;audio&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/inworld__tts-1.5-max/with-text-normalization.mp3&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;inworld/tts-1.5-max&#x27;,
  {
    apply_text_normalization: true,
    output_format: &#x27;mp3&#x27;,
    temperature: 1,
    text: &#x27;The meeting is at 3:30 PM on Jan 15th, 2026. Please confirm by calling 555-0123.&#x27;,
    timestamp_type: &#x27;none&#x27;,
    voice_id: &#x27;Dennis&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;inworld/tts-1.5-max&quot;,
  &quot;input&quot;: {
    &quot;apply_text_normalization&quot;: true,
    &quot;output_format&quot;: &quot;mp3&quot;,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: &quot;The meeting is at 3:30 PM on Jan 15th, 2026. Please confirm by calling 555-0123.&quot;,
    &quot;timestamp_type&quot;: &quot;none&quot;,
    &quot;voice_id&quot;: &quot;Dennis&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The text to be synthesized into speech. Maximum input of 2,000 characters.</td></tr><tr><td><code>voice_id</code></td><td>string</td><td>Required. The ID of the voice to use for synthesizing speech. Defaults to Dennis. Default: Dennis; Values: Loretta, Darlene, Marlene, Hank, Evelyn, Celeste, Pippa, Tessa, Liam, Callum, Hamish, Abby, Graham, Rupert, Mortimer, Snik, Anjali, Saanvi, Arjun, Claire, Oliver, Simon, Elliot, James, Serena, Gareth, Vinny, Lauren, Jessica, Ethan, Tyler, Jason, Chloe, Veronica, Victoria, Miranda, Sebastian, Victor, Malcolm, Nate, Brian, Amina, Kelsey, Derek, Evan, Kayla, Jake, Grant, Tristan, Nadia, Selene, Marcus, Riley, Damon, Cedric, Mia, Naomi, Jonah, Levi, Avery, Brandon, Conrad, Bianca, Lucian, Trevor, Alex, Ashley, Craig, Deborah, Dennis, Edward, Elizabeth, Hades, Julia, Pixie, Mark, Olivia, Priya, Ronald, Sarah, Shaun, Theodore, Timothy, Wendy, Dominus, Hana, Clive, Carter, Blake, Luna, Reed, Duncan, Felix, Eleanor, Sophie</td></tr><tr><td><code>output_format</code></td><td>string</td><td>Required. The output format for the audio. Supported formats are mp3, opus, wav, and flac. Defaults to mp3. Default: mp3; Values: mp3, opus, wav, flac</td></tr><tr><td><code>bit_rate</code></td><td>integer</td><td>Bits per second of the audio. Only for compressed audio formats (mp3, opus). The default is 128,000. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>sample_rate</code></td><td>integer</td><td>The synthesis sample rate in hertz. Accepts: 8000, 16000, 22050, 24000, 32000, 44100, 48000. The default is 48,000. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>speaking_rate</code></td><td>number</td><td>Speaking rate/speed, in the range [0.5, 1.5]. The default is 1.0. We recommend using values above 0.8 to ensure high quality. Minimum: 0.5; Maximum: 1.5</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Required. Determines the degree of randomness when sampling audio tokens. Defaults to 1.0. Accepts values between 0 (exclusive) and 2 (inclusive). Higher values = more expressive, lower values = more deterministic. Default: 1; Minimum: 0.01; Maximum: 2</td></tr><tr><td><code>timestamp_type</code></td><td>string</td><td>Required. Controls timestamp metadata returned with the audio. "word" returns word-level timing, "character" returns character-level timing. Note: adds latency. Defaults to none. Default: none; Values: none, word, character</td></tr><tr><td><code>apply_text_normalization</code></td><td>boolean</td><td>When enabled, text normalization expands numbers, dates, times, and abbreviations before converting to speech. Turning this off may reduce latency.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio</code></td><td>string</td><td>Required. URL to the generated audio file</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/inworld/tts-1.5-max/schema-input.json)
- [Output schema](/ai/models/inworld/tts-1.5-max/schema-output.json)

