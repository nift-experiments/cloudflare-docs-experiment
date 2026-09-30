---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/assemblyai/universal-3-pro/
  description: assemblyai/universal-3-pro
  full_title: AssemblyAI Universal-3 Pro · Cloudflare AI docs
  head_html: <title>AssemblyAI Universal-3 Pro · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="assemblyai/universal-3-pro"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/assemblyai/universal-3-pro/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AssemblyAI Universal-3 Pro · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="assemblyai/universal-3-pro"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/assemblyai/universal-3-pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/assemblyai/universal-3-pro/#page","headline":"AssemblyAI Universal-3 Pro \u00b7 Cloudflare AI docs","description":"assemblyai/universal-3-pro","url":"https://developers.cloudflare.com/ai/models/assemblyai/universal-3-pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/assemblyai/universal-3-pro/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/assemblyai.svg" alt="Assemblyai logo" width="48" height="48">

<h1 id="assemblyai-universal-3-pro">AssemblyAI Universal-3 Pro</h1>

<p><code>assemblyai/universal-3-pro</code></p>

AssemblyAI's Universal 3 Pro speech recognition model for high-accuracy transcription.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Automatic Speech Recognition</td></tr>
<tr><th>Terms</th><td><a href="https://www.assemblyai.com/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per audio minute: 0.0035</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Transcribe an audio file with default settings

<section class="model-example"><strong>Basic Transcription</strong>
<p>Transcribe an audio file with default settings</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/alloy.wav&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The sun rises in the east and sets in the west. This simple fact has been observed by humans for thousands of years.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;confidence&quot;: 0.99276465,
      &quot;language_code&quot;: &quot;en&quot;,
      &quot;language_confidence&quot;: 0.9998,
      &quot;text&quot;: &quot;The sun rises in the east and sets in the west. This simple fact has been observed by humans for thousands of years.&quot;,
      &quot;utterances&quot;: null,
      &quot;words&quot;: [
        {
          &quot;confidence&quot;: 0.9713957,
          &quot;end&quot;: 129,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 32,
          &quot;text&quot;: &quot;The&quot;
        },
        {
          &quot;confidence&quot;: 0.97053415,
          &quot;end&quot;: 404,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 129,
          &quot;text&quot;: &quot;sun&quot;
        },
        {
          &quot;confidence&quot;: 0.9998932,
          &quot;end&quot;: 809,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 420,
          &quot;text&quot;: &quot;rises&quot;
        },
        {
          &quot;confidence&quot;: 0.999092,
          &quot;end&quot;: 922,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 841,
          &quot;text&quot;: &quot;in&quot;
        },
        {
          &quot;confidence&quot;: 0.9997658,
          &quot;end&quot;: 1068,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 922,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9684294,
          &quot;end&quot;: 1456,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1149,
          &quot;text&quot;: &quot;east&quot;
        },
        {
          &quot;confidence&quot;: 0.9894344,
          &quot;end&quot;: 1634,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1570,
          &quot;text&quot;: &quot;and&quot;
        },
        {
          &quot;confidence&quot;: 0.9999058,
          &quot;end&quot;: 2055,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1715,
          &quot;text&quot;: &quot;sets&quot;
        },
        {
          &quot;confidence&quot;: 0.9997663,
          &quot;end&quot;: 2104,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2055,
          &quot;text&quot;: &quot;in&quot;
        },
        {
          &quot;confidence&quot;: 0.9999552,
          &quot;end&quot;: 2217,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2120,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9913442,
          &quot;end&quot;: 2638,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2217,
          &quot;text&quot;: &quot;west.&quot;
        },
        {
          &quot;confidence&quot;: 0.9974367,
          &quot;end&quot;: 3221,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3107,
          &quot;text&quot;: &quot;This&quot;
        },
        {
          &quot;confidence&quot;: 0.99965656,
          &quot;end&quot;: 3560,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3269,
          &quot;text&quot;: &quot;simple&quot;
        },
        {
          &quot;confidence&quot;: 0.999713,
          &quot;end&quot;: 3997,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3593,
          &quot;text&quot;: &quot;fact&quot;
        },
        {
          &quot;confidence&quot;: 0.99924207,
          &quot;end&quot;: 4175,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3997,
          &quot;text&quot;: &quot;has&quot;
        },
        {
          &quot;confidence&quot;: 0.9995851,
          &quot;end&quot;: 4289,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4224,
          &quot;text&quot;: &quot;been&quot;
        },
        {
          &quot;confidence&quot;: 0.9984724,
          &quot;end&quot;: 4807,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4337,
          &quot;text&quot;: &quot;observed&quot;
        },
        {
          &quot;confidence&quot;: 0.9997143,
          &quot;end&quot;: 4952,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4807,
          &quot;text&quot;: &quot;by&quot;
        },
        {
          &quot;confidence&quot;: 0.9997894,
          &quot;end&quot;: 5422,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4969,
          &quot;text&quot;: &quot;humans&quot;
        },
        {
          &quot;confidence&quot;: 0.99947494,
          &quot;end&quot;: 5519,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 5422,
          &quot;text&quot;: &quot;for&quot;
        },
        {
          &quot;confidence&quot;: 0.99950385,
          &quot;end&quot;: 6118,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 5616,
          &quot;text&quot;: &quot;thousands&quot;
        },
        {
          &quot;confidence&quot;: 0.9995235,
          &quot;end&quot;: 6231,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6118,
          &quot;text&quot;: &quot;of&quot;
        },
        {
          &quot;confidence&quot;: 0.9519594,
          &quot;end&quot;: 6636,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6328,
          &quot;text&quot;: &quot;years.&quot;
        }
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;assemblyai/universal-3-pro&#x27;,
  { audio_url: &#x27;https://cdn.openai.com/API/docs/audio/alloy.wav&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;assemblyai/universal-3-pro&quot;,
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/alloy.wav&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With Language Code</strong>
<p>Transcribe with an explicit language code</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/echo.wav&quot;,
    &quot;language_code&quot;: &quot;en&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;In the heart of the city, there is a large park where people go to relax and enjoy nature. The park has a beautiful pond with ducks and swans.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;confidence&quot;: 0.9927905,
      &quot;language_code&quot;: &quot;en_us&quot;,
      &quot;language_confidence&quot;: null,
      &quot;text&quot;: &quot;In the heart of the city, there is a large park where people go to relax and enjoy nature. The park has a beautiful pond with ducks and swans.&quot;,
      &quot;utterances&quot;: null,
      &quot;words&quot;: [
        {
          &quot;confidence&quot;: 0.88134426,
          &quot;end&quot;: 80,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 32,
          &quot;text&quot;: &quot;In&quot;
        },
        {
          &quot;confidence&quot;: 0.9984907,
          &quot;end&quot;: 241,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 177,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.99956447,
          &quot;end&quot;: 500,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 258,
          &quot;text&quot;: &quot;heart&quot;
        },
        {
          &quot;confidence&quot;: 0.9995684,
          &quot;end&quot;: 548,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 500,
          &quot;text&quot;: &quot;of&quot;
        },
        {
          &quot;confidence&quot;: 0.99977916,
          &quot;end&quot;: 677,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 596,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9956655,
          &quot;end&quot;: 967,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 677,
          &quot;text&quot;: &quot;city,&quot;
        },
        {
          &quot;confidence&quot;: 0.9987048,
          &quot;end&quot;: 1435,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1322,
          &quot;text&quot;: &quot;there&quot;
        },
        {
          &quot;confidence&quot;: 0.99971443,
          &quot;end&quot;: 1516,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1467,
          &quot;text&quot;: &quot;is&quot;
        },
        {
          &quot;confidence&quot;: 0.99948585,
          &quot;end&quot;: 1596,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1564,
          &quot;text&quot;: &quot;a&quot;
        },
        {
          &quot;confidence&quot;: 0.9987669,
          &quot;end&quot;: 2016,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1709,
          &quot;text&quot;: &quot;large&quot;
        },
        {
          &quot;confidence&quot;: 0.9981509,
          &quot;end&quot;: 2467,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2129,
          &quot;text&quot;: &quot;park&quot;
        },
        {
          &quot;confidence&quot;: 0.9559358,
          &quot;end&quot;: 2838,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2693,
          &quot;text&quot;: &quot;where&quot;
        },
        {
          &quot;confidence&quot;: 0.99979085,
          &quot;end&quot;: 3145,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2854,
          &quot;text&quot;: &quot;people&quot;
        },
        {
          &quot;confidence&quot;: 0.9993555,
          &quot;end&quot;: 3338,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3177,
          &quot;text&quot;: &quot;go&quot;
        },
        {
          &quot;confidence&quot;: 0.9998317,
          &quot;end&quot;: 3467,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3338,
          &quot;text&quot;: &quot;to&quot;
        },
        {
          &quot;confidence&quot;: 0.99991953,
          &quot;end&quot;: 4064,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3500,
          &quot;text&quot;: &quot;relax&quot;
        },
        {
          &quot;confidence&quot;: 0.9988979,
          &quot;end&quot;: 4161,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4064,
          &quot;text&quot;: &quot;and&quot;
        },
        {
          &quot;confidence&quot;: 0.9999237,
          &quot;end&quot;: 4484,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4161,
          &quot;text&quot;: &quot;enjoy&quot;
        },
        {
          &quot;confidence&quot;: 0.998528,
          &quot;end&quot;: 4887,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4484,
          &quot;text&quot;: &quot;nature.&quot;
        },
        {
          &quot;confidence&quot;: 0.990198,
          &quot;end&quot;: 5758,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 5597,
          &quot;text&quot;: &quot;The&quot;
        },
        {
          &quot;confidence&quot;: 0.99979144,
          &quot;end&quot;: 6016,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 5758,
          &quot;text&quot;: &quot;park&quot;
        },
        {
          &quot;confidence&quot;: 0.99926263,
          &quot;end&quot;: 6177,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6064,
          &quot;text&quot;: &quot;has&quot;
        },
        {
          &quot;confidence&quot;: 0.9992211,
          &quot;end&quot;: 6242,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6177,
          &quot;text&quot;: &quot;a&quot;
        },
        {
          &quot;confidence&quot;: 0.99989605,
          &quot;end&quot;: 6774,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6322,
          &quot;text&quot;: &quot;beautiful&quot;
        },
        {
          &quot;confidence&quot;: 0.9998628,
          &quot;end&quot;: 7193,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6790,
          &quot;text&quot;: &quot;pond&quot;
        },
        {
          &quot;confidence&quot;: 0.99960047,
          &quot;end&quot;: 7355,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 7193,
          &quot;text&quot;: &quot;with&quot;
        },
        {
          &quot;confidence&quot;: 0.99963534,
          &quot;end&quot;: 7806,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 7371,
          &quot;text&quot;: &quot;ducks&quot;
        },
        {
          &quot;confidence&quot;: 0.99866796,
          &quot;end&quot;: 7919,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 7855,
          &quot;text&quot;: &quot;and&quot;
        },
        {
          &quot;confidence&quot;: 0.9833702,
          &quot;end&quot;: 8629,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 7935,
          &quot;text&quot;: &quot;swans.&quot;
        }
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;assemblyai/universal-3-pro&#x27;,
  { audio_url: &#x27;https://cdn.openai.com/API/docs/audio/echo.wav&#x27;, language_code: &#x27;en&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;assemblyai/universal-3-pro&quot;,
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/echo.wav&quot;,
    &quot;language_code&quot;: &quot;en&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>With Key Terms</strong>
<p>Improve accuracy for domain-specific vocabulary</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/nova.wav&quot;,
    &quot;keyterms_prompt&quot;: [
      &quot;Kubernetes&quot;,
      &quot;microservices&quot;,
      &quot;containerization&quot;,
      &quot;load balancer&quot;
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;In the kitchen, the aroma of freshly baked bread filled the air. The loaves were golden brown and crusty on the outside and soft and warm on the inside.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;confidence&quot;: 0.9901139,
      &quot;language_code&quot;: &quot;en&quot;,
      &quot;language_confidence&quot;: 0.9969,
      &quot;text&quot;: &quot;In the kitchen, the aroma of freshly baked bread filled the air. The loaves were golden brown and crusty on the outside and soft and warm on the inside.&quot;,
      &quot;utterances&quot;: null,
      &quot;words&quot;: [
        {
          &quot;confidence&quot;: 0.9785539,
          &quot;end&quot;: 80,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 32,
          &quot;text&quot;: &quot;In&quot;
        },
        {
          &quot;confidence&quot;: 0.99962807,
          &quot;end&quot;: 242,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 177,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.99617165,
          &quot;end&quot;: 565,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 258,
          &quot;text&quot;: &quot;kitchen,&quot;
        },
        {
          &quot;confidence&quot;: 0.9991928,
          &quot;end&quot;: 839,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 743,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.99992657,
          &quot;end&quot;: 1292,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 839,
          &quot;text&quot;: &quot;aroma&quot;
        },
        {
          &quot;confidence&quot;: 0.99955577,
          &quot;end&quot;: 1405,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1308,
          &quot;text&quot;: &quot;of&quot;
        },
        {
          &quot;confidence&quot;: 0.9996594,
          &quot;end&quot;: 1889,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1405,
          &quot;text&quot;: &quot;freshly&quot;
        },
        {
          &quot;confidence&quot;: 0.99850214,
          &quot;end&quot;: 2261,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 1970,
          &quot;text&quot;: &quot;baked&quot;
        },
        {
          &quot;confidence&quot;: 0.9999217,
          &quot;end&quot;: 2584,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2293,
          &quot;text&quot;: &quot;bread&quot;
        },
        {
          &quot;confidence&quot;: 0.9999,
          &quot;end&quot;: 2859,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2600,
          &quot;text&quot;: &quot;filled&quot;
        },
        {
          &quot;confidence&quot;: 0.99993885,
          &quot;end&quot;: 3004,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 2859,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9961201,
          &quot;end&quot;: 3262,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 3020,
          &quot;text&quot;: &quot;air.&quot;
        },
        {
          &quot;confidence&quot;: 0.99501073,
          &quot;end&quot;: 4119,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4054,
          &quot;text&quot;: &quot;The&quot;
        },
        {
          &quot;confidence&quot;: 0.9997483,
          &quot;end&quot;: 4522,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4215,
          &quot;text&quot;: &quot;loaves&quot;
        },
        {
          &quot;confidence&quot;: 0.9998282,
          &quot;end&quot;: 4781,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4619,
          &quot;text&quot;: &quot;were&quot;
        },
        {
          &quot;confidence&quot;: 0.99248224,
          &quot;end&quot;: 5249,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 4878,
          &quot;text&quot;: &quot;golden&quot;
        },
        {
          &quot;confidence&quot;: 0.9700398,
          &quot;end&quot;: 5718,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 5362,
          &quot;text&quot;: &quot;brown&quot;
        },
        {
          &quot;confidence&quot;: 0.9419883,
          &quot;end&quot;: 5992,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 5928,
          &quot;text&quot;: &quot;and&quot;
        },
        {
          &quot;confidence&quot;: 0.9994146,
          &quot;end&quot;: 6541,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6089,
          &quot;text&quot;: &quot;crusty&quot;
        },
        {
          &quot;confidence&quot;: 0.9997141,
          &quot;end&quot;: 6703,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6574,
          &quot;text&quot;: &quot;on&quot;
        },
        {
          &quot;confidence&quot;: 0.9999218,
          &quot;end&quot;: 6784,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6719,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9993179,
          &quot;end&quot;: 7365,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 6881,
          &quot;text&quot;: &quot;outside&quot;
        },
        {
          &quot;confidence&quot;: 0.8661144,
          &quot;end&quot;: 7462,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 7365,
          &quot;text&quot;: &quot;and&quot;
        },
        {
          &quot;confidence&quot;: 0.9996922,
          &quot;end&quot;: 7882,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 7462,
          &quot;text&quot;: &quot;soft&quot;
        },
        {
          &quot;confidence&quot;: 0.9998481,
          &quot;end&quot;: 7995,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 7882,
          &quot;text&quot;: &quot;and&quot;
        },
        {
          &quot;confidence&quot;: 0.99996424,
          &quot;end&quot;: 8270,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 8028,
          &quot;text&quot;: &quot;warm&quot;
        },
        {
          &quot;confidence&quot;: 0.9998791,
          &quot;end&quot;: 8399,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 8270,
          &quot;text&quot;: &quot;on&quot;
        },
        {
          &quot;confidence&quot;: 0.99982506,
          &quot;end&quot;: 8512,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 8415,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9834439,
          &quot;end&quot;: 8964,
          &quot;speaker&quot;: null,
          &quot;start&quot;: 8512,
          &quot;text&quot;: &quot;inside.&quot;
        }
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;assemblyai/universal-3-pro&#x27;,
  {
    audio_url: &#x27;https://cdn.openai.com/API/docs/audio/nova.wav&#x27;,
    keyterms_prompt: [&#x27;Kubernetes&#x27;, &#x27;microservices&#x27;, &#x27;containerization&#x27;, &#x27;load balancer&#x27;],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;assemblyai/universal-3-pro&quot;,
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/nova.wav&quot;,
    &quot;keyterms_prompt&quot;: [
      &quot;Kubernetes&quot;,
      &quot;microservices&quot;,
      &quot;containerization&quot;,
      &quot;load balancer&quot;
    ]
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Speaker Diarization</strong>
<p>Identify different speakers in the audio</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/onyx.wav&quot;,
    &quot;speaker_labels&quot;: true
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The train chugged along the tracks, carrying passengers to their destinations. The rhythmic sound of the wheels on the rails was soothing.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;confidence&quot;: 0.99781793,
      &quot;language_code&quot;: &quot;en&quot;,
      &quot;language_confidence&quot;: 0.9906,
      &quot;text&quot;: &quot;The train chugged along the tracks, carrying passengers to their destinations. The rhythmic sound of the wheels on the rails was soothing.&quot;,
      &quot;utterances&quot;: [
        {
          &quot;confidence&quot;: 0.99781793,
          &quot;end&quot;: 7719,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 32,
          &quot;text&quot;: &quot;The train chugged along the tracks, carrying passengers to their destinations. The rhythmic sound of the wheels on the rails was soothing.&quot;
        }
      ],
      &quot;words&quot;: [
        {
          &quot;confidence&quot;: 0.9742124,
          &quot;end&quot;: 113,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 32,
          &quot;text&quot;: &quot;The&quot;
        },
        {
          &quot;confidence&quot;: 0.99997795,
          &quot;end&quot;: 403,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 177,
          &quot;text&quot;: &quot;train&quot;
        },
        {
          &quot;confidence&quot;: 0.99713653,
          &quot;end&quot;: 904,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 516,
          &quot;text&quot;: &quot;chugged&quot;
        },
        {
          &quot;confidence&quot;: 0.9999881,
          &quot;end&quot;: 1130,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 904,
          &quot;text&quot;: &quot;along&quot;
        },
        {
          &quot;confidence&quot;: 0.9999676,
          &quot;end&quot;: 1308,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 1227,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9995983,
          &quot;end&quot;: 1808,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 1308,
          &quot;text&quot;: &quot;tracks,&quot;
        },
        {
          &quot;confidence&quot;: 0.9998933,
          &quot;end&quot;: 2341,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 2131,
          &quot;text&quot;: &quot;carrying&quot;
        },
        {
          &quot;confidence&quot;: 0.999992,
          &quot;end&quot;: 3068,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 2454,
          &quot;text&quot;: &quot;passengers&quot;
        },
        {
          &quot;confidence&quot;: 0.99999034,
          &quot;end&quot;: 3229,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 3100,
          &quot;text&quot;: &quot;to&quot;
        },
        {
          &quot;confidence&quot;: 0.9999908,
          &quot;end&quot;: 3423,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 3262,
          &quot;text&quot;: &quot;their&quot;
        },
        {
          &quot;confidence&quot;: 0.9992286,
          &quot;end&quot;: 4198,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 3423,
          &quot;text&quot;: &quot;destinations.&quot;
        },
        {
          &quot;confidence&quot;: 0.99871373,
          &quot;end&quot;: 5119,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 5038,
          &quot;text&quot;: &quot;The&quot;
        },
        {
          &quot;confidence&quot;: 0.9999517,
          &quot;end&quot;: 5523,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 5184,
          &quot;text&quot;: &quot;rhythmic&quot;
        },
        {
          &quot;confidence&quot;: 0.99993813,
          &quot;end&quot;: 5926,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 5523,
          &quot;text&quot;: &quot;sound&quot;
        },
        {
          &quot;confidence&quot;: 0.99991894,
          &quot;end&quot;: 6007,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 5926,
          &quot;text&quot;: &quot;of&quot;
        },
        {
          &quot;confidence&quot;: 0.99993825,
          &quot;end&quot;: 6088,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 6007,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.99995935,
          &quot;end&quot;: 6459,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 6169,
          &quot;text&quot;: &quot;wheels&quot;
        },
        {
          &quot;confidence&quot;: 0.99997675,
          &quot;end&quot;: 6605,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 6556,
          &quot;text&quot;: &quot;on&quot;
        },
        {
          &quot;confidence&quot;: 0.99999475,
          &quot;end&quot;: 6718,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 6637,
          &quot;text&quot;: &quot;the&quot;
        },
        {
          &quot;confidence&quot;: 0.9999932,
          &quot;end&quot;: 7105,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 6718,
          &quot;text&quot;: &quot;rails&quot;
        },
        {
          &quot;confidence&quot;: 0.999851,
          &quot;end&quot;: 7299,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 7138,
          &quot;text&quot;: &quot;was&quot;
        },
        {
          &quot;confidence&quot;: 0.98378325,
          &quot;end&quot;: 7719,
          &quot;speaker&quot;: &quot;A&quot;,
          &quot;start&quot;: 7299,
          &quot;text&quot;: &quot;soothing.&quot;
        }
      ]
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;assemblyai/universal-3-pro&#x27;,
  { audio_url: &#x27;https://cdn.openai.com/API/docs/audio/onyx.wav&#x27;, speaker_labels: true },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;assemblyai/universal-3-pro&quot;,
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/onyx.wav&quot;,
    &quot;speaker_labels&quot;: true
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio_url</code></td><td>string</td><td>The URL of the audio file to transcribe. Can be a publicly accessible URL or a data URI (data:audio/...;base64,...). For data URIs, the audio will be uploaded to AssemblyAI automatically. Required for pre-recorded transcription (when stream is false or not set).</td></tr><tr><td><code>websocket</code></td><td>boolean</td><td>Enable real-time WebSocket streaming for live audio transcription. When true, a WebSocket connection is established instead of submitting a pre-recorded transcription job. Cannot be used with audio_url.</td></tr><tr><td><code>language_code</code></td><td>string</td><td>The language code for the audio file (e.g., "en", "es", "fr"). Defaults to automatic language detection.</td></tr><tr><td><code>language_detection</code></td><td>boolean</td><td>Enable automatic language detection. When enabled with speech_models, the system will automatically select the best model for the detected language.</td></tr><tr><td><code>prompt</code></td><td>string</td><td>A custom prompt to guide transcription style, formatting, and output characteristics. Maximum 1,500 words.</td></tr><tr><td><code>keyterms_prompt</code></td><td>array</td><td>An array of up to 1,000 words or phrases (max 6 words per phrase) to improve transcription accuracy. Cannot be used with the prompt parameter.</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Controls randomness in model output (0.0-1.0). Lower values make output more deterministic. Default is 0.0. Minimum: 0; Maximum: 1</td></tr><tr><td><code>speaker_labels</code></td><td>boolean</td><td>Enable speaker diarization to identify different speakers in the audio.</td></tr><tr><td><code>speakers_expected</code></td><td>integer</td><td>Expected number of speakers for speaker diarization. Minimum: 1; Maximum: 9007199254740991</td></tr><tr><td><code>auto_chapters</code></td><td>boolean</td><td>Enable automatic chapter detection.</td></tr><tr><td><code>entity_detection</code></td><td>boolean</td><td>Enable detection of entities like names, organizations, and locations.</td></tr><tr><td><code>sentiment_analysis</code></td><td>boolean</td><td>Enable sentiment analysis for each sentence.</td></tr><tr><td><code>auto_highlights</code></td><td>boolean</td><td>Enable automatic extraction of key phrases and highlights.</td></tr><tr><td><code>content_safety</code></td><td>boolean</td><td>Enable content safety detection for sensitive content.</td></tr><tr><td><code>iab_categories</code></td><td>boolean</td><td>Enable IAB (Interactive Advertising Bureau) content taxonomy classification.</td></tr><tr><td><code>custom_spelling</code></td><td>array</td><td>Custom spelling rules to replace specific words or phrases in the transcription output.</td></tr><tr><td><code>custom_spelling[].from</code></td><td>array</td><td>Required.</td></tr><tr><td><code>custom_spelling[].to</code></td><td>string</td><td>Required.</td></tr><tr><td><code>disfluencies</code></td><td>boolean</td><td>Include filler words like "um", "uh", etc. in the transcript.</td></tr><tr><td><code>multichannel</code></td><td>boolean</td><td>Process each audio channel separately for multi-channel audio files.</td></tr><tr><td><code>dual_channel</code></td><td>boolean</td><td>Process audio as dual-channel (stereo) for better accuracy.</td></tr><tr><td><code>webhook_url</code></td><td>string</td><td>URL to receive webhook notifications when transcription is complete.</td></tr><tr><td><code>audio_start_from</code></td><td>integer</td><td>Timestamp (in milliseconds) to start transcription from. Minimum: 0; Maximum: 9007199254740991</td></tr><tr><td><code>audio_end_at</code></td><td>integer</td><td>Timestamp (in milliseconds) to end transcription at. Minimum: 0; Maximum: 9007199254740991</td></tr><tr><td><code>word_boost</code></td><td>array</td><td>Array of words to boost recognition accuracy (legacy - use keyterms_prompt instead).</td></tr><tr><td><code>boost_param</code></td><td>string</td><td>How much to boost the words in word_boost. Values: low, default, high</td></tr><tr><td><code>filter_profanity</code></td><td>boolean</td><td>Filter profanity from the transcription.</td></tr><tr><td><code>redact_pii</code></td><td>boolean</td><td>Redact personally identifiable information.</td></tr><tr><td><code>redact_pii_audio</code></td><td>boolean</td><td>Generate a redacted audio file with PII removed.</td></tr><tr><td><code>redact_pii_policies</code></td><td>array</td><td>Specific PII policies to apply for redaction.</td></tr><tr><td><code>redact_pii_sub</code></td><td>string</td><td>Strategy for substituting redacted PII. Values: entity_name, hash</td></tr><tr><td><code>speech_threshold</code></td><td>number</td><td>Confidence threshold for speech detection. Minimum: 0; Maximum: 1</td></tr><tr><td><code>domain</code></td><td>string</td><td>Domain-specific transcription mode. "medical-v1" enables medical terminology optimization. Values: medical-v1</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The transcribed text.</td></tr><tr><td><code>words</code></td><td>array or null</td><td>Word-level timestamps and confidence scores.</td></tr><tr><td><code>utterances</code></td><td>array or null</td><td>Speaker-separated utterances (when speaker_labels is enabled).</td></tr><tr><td><code>confidence</code></td><td>['number', 'null']</td><td>Overall confidence score for the transcription.</td></tr><tr><td><code>language_code</code></td><td>['string', 'null']</td><td>Detected or specified language code.</td></tr><tr><td><code>language_confidence</code></td><td>['number', 'null']</td><td>Confidence score for language detection.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/assemblyai/universal-3-pro/schema-input.json)
- [Output schema](/ai/models/assemblyai/universal-3-pro/schema-output.json)

