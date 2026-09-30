---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/
  description: assemblyai/universal-3.5-pro
  full_title: AssemblyAI Universal-3.5 Pro · Cloudflare AI docs
  head_html: <title>AssemblyAI Universal-3.5 Pro · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="assemblyai/universal-3.5-pro"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AssemblyAI Universal-3.5 Pro · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="assemblyai/universal-3.5-pro"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/#page","headline":"AssemblyAI Universal-3.5 Pro \u00b7 Cloudflare AI docs","description":"assemblyai/universal-3.5-pro","url":"https://developers.cloudflare.com/ai/models/assemblyai/universal-3.5-pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/assemblyai/universal-3.5-pro/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/assemblyai.svg" alt="Assemblyai logo" width="48" height="48">

<h1 id="assemblyai-universal-3-5-pro">AssemblyAI Universal-3.5 Pro</h1>

<p><code>assemblyai/universal-3.5-pro</code></p>

AssemblyAI's Universal-3.5 Pro speech recognition model for fast, high-accuracy transcription.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Automatic Speech Recognition</td></tr>
<tr><th>Terms</th><td><a href="https://www.assemblyai.com/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per audio minute: 0.0035, Per minute (speaker diarization): 0.0003, Per minute (key terms): 0.00083, Per minute (medical): 0.0025</td></tr>
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
    &quot;id&quot;: &quot;93b8082d-22c2-4dd0-adf6-0037d2c7027a&quot;,
    &quot;language_model&quot;: &quot;assemblyai_default&quot;,
    &quot;acoustic_model&quot;: &quot;assemblyai_default&quot;,
    &quot;language_code&quot;: &quot;en&quot;,
    &quot;speech_understanding&quot;: null,
    &quot;translated_texts&quot;: null,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/alloy.wav&quot;,
    &quot;text&quot;: &quot;The sun rises in the east and sets in the west. This simple fact has been observed by humans for thousands of years.&quot;,
    &quot;words&quot;: [
      {
        &quot;text&quot;: &quot;The&quot;,
        &quot;start&quot;: 32,
        &quot;end&quot;: 129,
        &quot;confidence&quot;: 0.95348084,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;sun&quot;,
        &quot;start&quot;: 129,
        &quot;end&quot;: 404,
        &quot;confidence&quot;: 0.97099674,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;rises&quot;,
        &quot;start&quot;: 420,
        &quot;end&quot;: 809,
        &quot;confidence&quot;: 0.9999746,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;in&quot;,
        &quot;start&quot;: 841,
        &quot;end&quot;: 922,
        &quot;confidence&quot;: 0.999997,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;the&quot;,
        &quot;start&quot;: 922,
        &quot;end&quot;: 1068,
        &quot;confidence&quot;: 0.99999905,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;east&quot;,
        &quot;start&quot;: 1149,
        &quot;end&quot;: 1456,
        &quot;confidence&quot;: 0.9853527,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;and&quot;,
        &quot;start&quot;: 1570,
        &quot;end&quot;: 1634,
        &quot;confidence&quot;: 0.999203,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;sets&quot;,
        &quot;start&quot;: 1715,
        &quot;end&quot;: 2055,
        &quot;confidence&quot;: 0.999995,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;in&quot;,
        &quot;start&quot;: 2055,
        &quot;end&quot;: 2104,
        &quot;confidence&quot;: 0.99999857,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;the&quot;,
        &quot;start&quot;: 2120,
        &quot;end&quot;: 2217,
        &quot;confidence&quot;: 0.9999993,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;west.&quot;,
        &quot;start&quot;: 2217,
        &quot;end&quot;: 2638,
        &quot;confidence&quot;: 0.9959912,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;This&quot;,
        &quot;start&quot;: 3107,
        &quot;end&quot;: 3221,
        &quot;confidence&quot;: 0.9999709,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;simple&quot;,
        &quot;start&quot;: 3269,
        &quot;end&quot;: 3560,
        &quot;confidence&quot;: 0.9999976,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;fact&quot;,
        &quot;start&quot;: 3593,
        &quot;end&quot;: 3997,
        &quot;confidence&quot;: 0.999998,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;has&quot;,
        &quot;start&quot;: 3997,
        &quot;end&quot;: 4175,
        &quot;confidence&quot;: 0.999995,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;been&quot;,
        &quot;start&quot;: 4224,
        &quot;end&quot;: 4289,
        &quot;confidence&quot;: 0.9999974,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;observed&quot;,
        &quot;start&quot;: 4337,
        &quot;end&quot;: 4807,
        &quot;confidence&quot;: 0.9999957,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;by&quot;,
        &quot;start&quot;: 4807,
        &quot;end&quot;: 4952,
        &quot;confidence&quot;: 0.999998,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;humans&quot;,
        &quot;start&quot;: 4969,
        &quot;end&quot;: 5422,
        &quot;confidence&quot;: 0.99999607,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;for&quot;,
        &quot;start&quot;: 5422,
        &quot;end&quot;: 5519,
        &quot;confidence&quot;: 0.99999416,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;thousands&quot;,
        &quot;start&quot;: 5616,
        &quot;end&quot;: 6118,
        &quot;confidence&quot;: 0.9999938,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;of&quot;,
        &quot;start&quot;: 6118,
        &quot;end&quot;: 6231,
        &quot;confidence&quot;: 0.9999945,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;years.&quot;,
        &quot;start&quot;: 6328,
        &quot;end&quot;: 6636,
        &quot;confidence&quot;: 0.9984148,
        &quot;speaker&quot;: null
      }
    ],
    &quot;utterances&quot;: null,
    &quot;confidence&quot;: 0.9957971,
    &quot;audio_duration&quot;: 7,
    &quot;punctuate&quot;: true,
    &quot;format_text&quot;: true,
    &quot;webhook_url&quot;: null,
    &quot;webhook_status_code&quot;: null,
    &quot;webhook_auth&quot;: false,
    &quot;webhook_auth_header_name&quot;: null,
    &quot;speed_boost&quot;: false,
    &quot;auto_highlights_result&quot;: null,
    &quot;auto_highlights&quot;: false,
    &quot;audio_start_from&quot;: null,
    &quot;audio_end_at&quot;: null,
    &quot;word_boost&quot;: [],
    &quot;boost_param&quot;: null,
    &quot;prompt&quot;: null,
    &quot;keyterms_prompt&quot;: [],
    &quot;filter_profanity&quot;: false,
    &quot;redact_pii&quot;: false,
    &quot;redact_pii_audio&quot;: false,
    &quot;redact_pii_audio_quality&quot;: null,
    &quot;redact_pii_audio_options&quot;: null,
    &quot;redact_pii_policies&quot;: null,
    &quot;redact_pii_sub&quot;: null,
    &quot;redact_static_entities&quot;: null,
    &quot;speaker_labels&quot;: false,
    &quot;speaker_options&quot;: null,
    &quot;content_safety&quot;: false,
    &quot;iab_categories&quot;: false,
    &quot;content_safety_labels&quot;: {
      &quot;status&quot;: &quot;unavailable&quot;,
      &quot;results&quot;: [],
      &quot;summary&quot;: {}
    },
    &quot;iab_categories_result&quot;: {
      &quot;status&quot;: &quot;unavailable&quot;,
      &quot;results&quot;: [],
      &quot;summary&quot;: {}
    },
    &quot;language_detection&quot;: true,
    &quot;language_detection_options&quot;: null,
    &quot;language_detection_results&quot;: null,
    &quot;language_confidence_threshold&quot;: null,
    &quot;language_confidence&quot;: 0.9998,
    &quot;custom_spelling&quot;: null,
    &quot;throttled&quot;: false,
    &quot;auto_chapters&quot;: false,
    &quot;summarization&quot;: false,
    &quot;summary_type&quot;: null,
    &quot;summary_model&quot;: null,
    &quot;custom_topics&quot;: false,
    &quot;topics&quot;: [],
    &quot;speech_threshold&quot;: null,
    &quot;speech_model&quot;: null,
    &quot;speech_models&quot;: [
      &quot;universal-3-5-pro&quot;
    ],
    &quot;speech_model_used&quot;: &quot;universal-3-5-pro&quot;,
    &quot;temperature&quot;: null,
    &quot;remove_audio_tags&quot;: &quot;all&quot;,
    &quot;chapters&quot;: null,
    &quot;disfluencies&quot;: false,
    &quot;entity_detection&quot;: false,
    &quot;sentiment_analysis&quot;: false,
    &quot;sentiment_analysis_results&quot;: null,
    &quot;entities&quot;: null,
    &quot;speakers_expected&quot;: null,
    &quot;summary&quot;: null,
    &quot;custom_topics_results&quot;: null,
    &quot;is_deleted&quot;: null,
    &quot;multichannel&quot;: null,
    &quot;project_id&quot;: 1747096,
    &quot;token_id&quot;: 1768830
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;assemblyai/universal-3.5-pro&#x27;,
  { audio_url: &#x27;https://cdn.openai.com/API/docs/audio/alloy.wav&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;assemblyai/universal-3.5-pro&quot;,
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/alloy.wav&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Language and Keyterms</strong>
<p>Transcribe with an explicit language and domain terms</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/echo.wav&quot;,
    &quot;language_code&quot;: &quot;en&quot;,
    &quot;keyterms_prompt&quot;: [
      &quot;Kubernetes&quot;,
      &quot;microservices&quot;,
      &quot;containerization&quot;,
      &quot;load balancer&quot;
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;In the heart of the city, there is a large park where people go to relax and enjoy nature. The park has a beautiful pond with ducks and swans.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;7f184aba-4a6d-49fa-b47a-f2ec47e67878&quot;,
    &quot;language_model&quot;: &quot;assemblyai_default&quot;,
    &quot;acoustic_model&quot;: &quot;assemblyai_default&quot;,
    &quot;language_code&quot;: &quot;en_us&quot;,
    &quot;speech_understanding&quot;: null,
    &quot;translated_texts&quot;: null,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/echo.wav&quot;,
    &quot;text&quot;: &quot;In the heart of the city, there is a large park where people go to relax and enjoy nature. The park has a beautiful pond with ducks and swans.&quot;,
    &quot;words&quot;: [
      {
        &quot;text&quot;: &quot;In&quot;,
        &quot;start&quot;: 32,
        &quot;end&quot;: 80,
        &quot;confidence&quot;: 0.99823916,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;the&quot;,
        &quot;start&quot;: 177,
        &quot;end&quot;: 241,
        &quot;confidence&quot;: 0.9997907,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;heart&quot;,
        &quot;start&quot;: 258,
        &quot;end&quot;: 500,
        &quot;confidence&quot;: 0.9998222,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;of&quot;,
        &quot;start&quot;: 500,
        &quot;end&quot;: 548,
        &quot;confidence&quot;: 0.9999982,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;the&quot;,
        &quot;start&quot;: 596,
        &quot;end&quot;: 677,
        &quot;confidence&quot;: 0.99993014,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;city,&quot;,
        &quot;start&quot;: 677,
        &quot;end&quot;: 967,
        &quot;confidence&quot;: 0.9999535,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;there&quot;,
        &quot;start&quot;: 1322,
        &quot;end&quot;: 1435,
        &quot;confidence&quot;: 0.99998367,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;is&quot;,
        &quot;start&quot;: 1467,
        &quot;end&quot;: 1516,
        &quot;confidence&quot;: 0.9989073,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;a&quot;,
        &quot;start&quot;: 1564,
        &quot;end&quot;: 1596,
        &quot;confidence&quot;: 0.99998987,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;large&quot;,
        &quot;start&quot;: 1709,
        &quot;end&quot;: 2016,
        &quot;confidence&quot;: 0.99996316,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;park&quot;,
        &quot;start&quot;: 2129,
        &quot;end&quot;: 2467,
        &quot;confidence&quot;: 0.99998546,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;where&quot;,
        &quot;start&quot;: 2693,
        &quot;end&quot;: 2838,
        &quot;confidence&quot;: 0.99389255,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;people&quot;,
        &quot;start&quot;: 2854,
        &quot;end&quot;: 3145,
        &quot;confidence&quot;: 0.99998343,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;go&quot;,
        &quot;start&quot;: 3177,
        &quot;end&quot;: 3338,
        &quot;confidence&quot;: 0.9999392,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;to&quot;,
        &quot;start&quot;: 3338,
        &quot;end&quot;: 3467,
        &quot;confidence&quot;: 0.9999963,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;relax&quot;,
        &quot;start&quot;: 3500,
        &quot;end&quot;: 4064,
        &quot;confidence&quot;: 0.99998176,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;and&quot;,
        &quot;start&quot;: 4064,
        &quot;end&quot;: 4161,
        &quot;confidence&quot;: 0.99998665,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;enjoy&quot;,
        &quot;start&quot;: 4161,
        &quot;end&quot;: 4484,
        &quot;confidence&quot;: 0.9999976,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;nature.&quot;,
        &quot;start&quot;: 4484,
        &quot;end&quot;: 4887,
        &quot;confidence&quot;: 0.9999689,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;The&quot;,
        &quot;start&quot;: 5597,
        &quot;end&quot;: 5758,
        &quot;confidence&quot;: 0.9997563,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;park&quot;,
        &quot;start&quot;: 5758,
        &quot;end&quot;: 6016,
        &quot;confidence&quot;: 0.99999034,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;has&quot;,
        &quot;start&quot;: 6064,
        &quot;end&quot;: 6177,
        &quot;confidence&quot;: 0.99998844,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;a&quot;,
        &quot;start&quot;: 6177,
        &quot;end&quot;: 6242,
        &quot;confidence&quot;: 0.9999819,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;beautiful&quot;,
        &quot;start&quot;: 6322,
        &quot;end&quot;: 6774,
        &quot;confidence&quot;: 0.9999924,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;pond&quot;,
        &quot;start&quot;: 6790,
        &quot;end&quot;: 7193,
        &quot;confidence&quot;: 0.99999106,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;with&quot;,
        &quot;start&quot;: 7193,
        &quot;end&quot;: 7355,
        &quot;confidence&quot;: 0.9997123,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;ducks&quot;,
        &quot;start&quot;: 7371,
        &quot;end&quot;: 7806,
        &quot;confidence&quot;: 0.9999808,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;and&quot;,
        &quot;start&quot;: 7855,
        &quot;end&quot;: 7919,
        &quot;confidence&quot;: 0.9999771,
        &quot;speaker&quot;: null
      },
      {
        &quot;text&quot;: &quot;swans.&quot;,
        &quot;start&quot;: 7935,
        &quot;end&quot;: 8629,
        &quot;confidence&quot;: 0.99828225,
        &quot;speaker&quot;: null
      }
    ],
    &quot;utterances&quot;: null,
    &quot;confidence&quot;: 0.9995849,
    &quot;audio_duration&quot;: 9,
    &quot;punctuate&quot;: true,
    &quot;format_text&quot;: true,
    &quot;webhook_url&quot;: null,
    &quot;webhook_status_code&quot;: null,
    &quot;webhook_auth&quot;: false,
    &quot;webhook_auth_header_name&quot;: null,
    &quot;speed_boost&quot;: false,
    &quot;auto_highlights_result&quot;: null,
    &quot;auto_highlights&quot;: false,
    &quot;audio_start_from&quot;: null,
    &quot;audio_end_at&quot;: null,
    &quot;word_boost&quot;: [],
    &quot;boost_param&quot;: null,
    &quot;prompt&quot;: null,
    &quot;keyterms_prompt&quot;: [
      &quot;Kubernetes&quot;,
      &quot;microservices&quot;,
      &quot;containerization&quot;,
      &quot;load balancer&quot;
    ],
    &quot;filter_profanity&quot;: false,
    &quot;redact_pii&quot;: false,
    &quot;redact_pii_audio&quot;: false,
    &quot;redact_pii_audio_quality&quot;: null,
    &quot;redact_pii_audio_options&quot;: null,
    &quot;redact_pii_policies&quot;: null,
    &quot;redact_pii_sub&quot;: null,
    &quot;redact_static_entities&quot;: null,
    &quot;speaker_labels&quot;: false,
    &quot;speaker_options&quot;: null,
    &quot;content_safety&quot;: false,
    &quot;iab_categories&quot;: false,
    &quot;content_safety_labels&quot;: {
      &quot;status&quot;: &quot;unavailable&quot;,
      &quot;results&quot;: [],
      &quot;summary&quot;: {}
    },
    &quot;iab_categories_result&quot;: {
      &quot;status&quot;: &quot;unavailable&quot;,
      &quot;results&quot;: [],
      &quot;summary&quot;: {}
    },
    &quot;language_detection&quot;: false,
    &quot;language_detection_options&quot;: null,
    &quot;language_detection_results&quot;: null,
    &quot;language_confidence_threshold&quot;: null,
    &quot;language_confidence&quot;: null,
    &quot;custom_spelling&quot;: null,
    &quot;throttled&quot;: false,
    &quot;auto_chapters&quot;: false,
    &quot;summarization&quot;: false,
    &quot;summary_type&quot;: null,
    &quot;summary_model&quot;: null,
    &quot;custom_topics&quot;: false,
    &quot;topics&quot;: [],
    &quot;speech_threshold&quot;: null,
    &quot;speech_model&quot;: null,
    &quot;speech_models&quot;: [
      &quot;universal-3-5-pro&quot;
    ],
    &quot;speech_model_used&quot;: &quot;universal-3-5-pro&quot;,
    &quot;temperature&quot;: null,
    &quot;remove_audio_tags&quot;: &quot;all&quot;,
    &quot;chapters&quot;: null,
    &quot;disfluencies&quot;: false,
    &quot;entity_detection&quot;: false,
    &quot;sentiment_analysis&quot;: false,
    &quot;sentiment_analysis_results&quot;: null,
    &quot;entities&quot;: null,
    &quot;speakers_expected&quot;: null,
    &quot;summary&quot;: null,
    &quot;custom_topics_results&quot;: null,
    &quot;is_deleted&quot;: null,
    &quot;multichannel&quot;: null,
    &quot;project_id&quot;: 1747096,
    &quot;token_id&quot;: 1768830
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;assemblyai/universal-3.5-pro&#x27;,
  {
    audio_url: &#x27;https://cdn.openai.com/API/docs/audio/echo.wav&#x27;,
    language_code: &#x27;en&#x27;,
    keyterms_prompt: [&#x27;Kubernetes&#x27;, &#x27;microservices&#x27;, &#x27;containerization&#x27;, &#x27;load balancer&#x27;],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;assemblyai/universal-3.5-pro&quot;,
  &quot;input&quot;: {
    &quot;audio_url&quot;: &quot;https://cdn.openai.com/API/docs/audio/echo.wav&quot;,
    &quot;language_code&quot;: &quot;en&quot;,
    &quot;keyterms_prompt&quot;: [
      &quot;Kubernetes&quot;,
      &quot;microservices&quot;,
      &quot;containerization&quot;,
      &quot;load balancer&quot;
    ]
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>audio_url</code></td><td>string</td><td>Required. The URL of the audio or video file to transcribe, or a data URI.</td></tr><tr><td><code>audio_start_from</code></td><td>integer</td><td>Timestamp in milliseconds at which to begin transcription. Minimum: 0; Maximum: 9007199254740991</td></tr><tr><td><code>audio_end_at</code></td><td>integer</td><td>Timestamp in milliseconds at which to stop transcription. Minimum: 0; Maximum: 9007199254740991</td></tr><tr><td><code>language_code</code></td><td>string</td><td>Language code of the audio.</td></tr><tr><td><code>language_detection</code></td><td>boolean</td><td>Whether to automatically detect the language.</td></tr><tr><td><code>language_detection_options</code></td><td>object</td><td></td></tr><tr><td><code>language_detection_options.expected_languages</code></td><td>array</td><td>Languages expected in the audio.</td></tr><tr><td><code>language_detection_options.fallback_language</code></td><td>string</td><td>Fallback language when detection is uncertain.</td></tr><tr><td><code>language_detection_options.code_switching</code></td><td>boolean</td><td>Whether to detect switching between languages.</td></tr><tr><td><code>language_detection_options.code_switching_confidence_threshold</code></td><td>number</td><td>Minimum confidence for code-switching detection. Minimum: 0; Maximum: 1</td></tr><tr><td><code>language_detection_options.localization</code></td><td>array</td><td>Regional language variants to use when rendering text.</td></tr><tr><td><code>prompt</code></td><td>string</td><td>Natural-language instructions for transcription style.</td></tr><tr><td><code>keyterms_prompt</code></td><td>array</td><td>Words or phrases to prioritize during transcription.</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Controls transcription randomness from 0 to 1. Minimum: 0; Maximum: 1</td></tr><tr><td><code>punctuate</code></td><td>boolean</td><td>Whether to add punctuation.</td></tr><tr><td><code>format_text</code></td><td>boolean</td><td>Whether to apply text formatting.</td></tr><tr><td><code>disfluencies</code></td><td>boolean</td><td>Whether to include filler words such as um and uh.</td></tr><tr><td><code>filter_profanity</code></td><td>boolean</td><td>Whether to filter profanity.</td></tr><tr><td><code>speaker_labels</code></td><td>boolean</td><td>Whether to identify speakers in the transcript.</td></tr><tr><td><code>speakers_expected</code></td><td>integer</td><td>Expected number of speakers. Maximum: 9007199254740991</td></tr><tr><td><code>speaker_options</code></td><td>object</td><td></td></tr><tr><td><code>speaker_options.min_speakers_expected</code></td><td>integer</td><td>Minimum number of speakers to identify. Maximum: 9007199254740991</td></tr><tr><td><code>speaker_options.max_speakers_expected</code></td><td>integer</td><td>Maximum number of speakers to identify. Maximum: 9007199254740991</td></tr><tr><td><code>multichannel</code></td><td>boolean</td><td>Whether to transcribe each audio channel separately.</td></tr><tr><td><code>custom_spelling</code></td><td>array</td><td></td></tr><tr><td><code>custom_spelling[].from</code></td><td>array</td><td>Required. Words or phrases to replace.</td></tr><tr><td><code>custom_spelling[].to</code></td><td>string</td><td>Required. Replacement word or phrase.</td></tr><tr><td><code>auto_highlights</code></td><td>boolean</td><td>Whether to extract key phrases.</td></tr><tr><td><code>content_safety</code></td><td>boolean</td><td>Whether to detect sensitive content.</td></tr><tr><td><code>content_safety_confidence</code></td><td>integer</td><td>Content safety confidence threshold from 25 to 100. Minimum: 25; Maximum: 100</td></tr><tr><td><code>iab_categories</code></td><td>boolean</td><td>Whether to classify topics using IAB categories.</td></tr><tr><td><code>entity_detection</code></td><td>boolean</td><td>Whether to detect named entities.</td></tr><tr><td><code>sentiment_analysis</code></td><td>boolean</td><td>Whether to analyze sentence sentiment.</td></tr><tr><td><code>domain</code></td><td>string</td><td>Domain-specific model for medical terminology.</td></tr><tr><td><code>speech_threshold</code></td><td>number</td><td>Minimum fraction of speech required for transcription. Minimum: 0; Maximum: 1</td></tr><tr><td><code>redact_pii</code></td><td>boolean</td><td>Whether to redact personally identifiable information.</td></tr><tr><td><code>redact_pii_audio</code></td><td>boolean</td><td>Whether to generate an audio file with spoken PII redacted.</td></tr><tr><td><code>redact_pii_audio_quality</code></td><td>string</td><td>Format of the redacted audio file. Values: mp3, wav</td></tr><tr><td><code>redact_pii_audio_options</code></td><td>object</td><td></td></tr><tr><td><code>redact_pii_audio_options.return_redacted_no_speech_audio</code></td><td>boolean</td><td>Whether to return redacted audio when no speech is detected.</td></tr><tr><td><code>redact_pii_audio_options.override_audio_redaction_method</code></td><td>string</td><td>Replace redacted speech with silence instead of a beep.</td></tr><tr><td><code>redact_pii_policies</code></td><td>array</td><td>PII categories to redact.</td></tr><tr><td><code>redact_pii_sub</code></td><td>string</td><td>Replacement strategy for redacted PII. Values: entity_name, hash</td></tr><tr><td><code>redact_pii_return_unredacted</code></td><td>boolean</td><td>Whether to include unredacted fields alongside the redacted transcript.</td></tr><tr><td><code>redact_static_entities</code></td><td>object</td><td>User-defined terms to redact, grouped by label.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string</td><td>Required. The transcribed text.</td></tr><tr><td><code>words</code></td><td>array or null</td><td>Word-level timestamps and confidence scores.</td></tr><tr><td><code>utterances</code></td><td>array or null</td><td>Speaker-separated utterances (when speaker_labels is enabled).</td></tr><tr><td><code>confidence</code></td><td>['number', 'null']</td><td>Overall confidence score for the transcription.</td></tr><tr><td><code>language_code</code></td><td>['string', 'null']</td><td>Detected or specified language code.</td></tr><tr><td><code>language_confidence</code></td><td>['number', 'null']</td><td>Confidence score for language detection.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/assemblyai/universal-3.5-pro/schema-input.json)
- [Output schema](/ai/models/assemblyai/universal-3.5-pro/schema-output.json)

