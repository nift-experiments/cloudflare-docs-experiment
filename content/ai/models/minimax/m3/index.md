---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/minimax/m3/
  description: minimax/m3
  full_title: MiniMax M3 · Cloudflare AI docs
  head_html: <title>MiniMax M3 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="minimax/m3"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/minimax/m3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="MiniMax M3 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="minimax/m3"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/minimax/m3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/minimax/m3/#page","headline":"MiniMax M3 \u00b7 Cloudflare AI docs","description":"minimax/m3","url":"https://developers.cloudflare.com/ai/models/minimax/m3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/minimax/m3/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-m3">MiniMax M3</h1>

<p><code>minimax/m3</code></p>

MiniMax's M3 language model with frontier coding and agentic capabilities, a 1M token context window, and multilingual support.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://www.minimaxi.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input &lt;=512k (per 1M): 0.3, Cached input &lt;=512k (per 1M): 0.06, Output &lt;=512k (per 1M): 1.2, Input &gt;512k (per 1M): 1.2, Cached input &gt;512k (per 1M): 0.24, Output &gt;512k (per 1M): 4.8</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic chat completion request

<section class="model-example"><strong>Simple Conversation</strong>
<p>Basic chat completion request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 2048,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What is the capital of France?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The capital of France is **Paris**.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;066cf8a95614a7ebfcaa6ffd7f2cd663&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;The capital of France is **Paris**.&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user is asking a simple factual question: \&quot;What is the capital of France?\&quot; This is straightforward - the capital of France is Paris.&quot;,
          &quot;reasoning_details&quot;: [
            {
              &quot;type&quot;: &quot;reasoning.text&quot;,
              &quot;id&quot;: &quot;reasoning-text-1&quot;,
              &quot;format&quot;: &quot;MiniMax-response-v1&quot;,
              &quot;index&quot;: 0,
              &quot;text&quot;: &quot;The user is asking a simple factual question: \&quot;What is the capital of France?\&quot; This is straightforward - the capital of France is Paris.&quot;
            }
          ]
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336041,
    &quot;model&quot;: &quot;MiniMax-M3&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 221,
      &quot;prompt_tokens&quot;: 183,
      &quot;completion_tokens&quot;: 38,
      &quot;total_characters&quot;: 0,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 114
      }
    },
    &quot;input_sensitive&quot;: false,
    &quot;output_sensitive&quot;: false,
    &quot;base_resp&quot;: {
      &quot;status_code&quot;: 0,
      &quot;status_msg&quot;: &quot;&quot;
    },
    &quot;input_sensitive_type&quot;: 0,
    &quot;output_sensitive_type&quot;: 0,
    &quot;output_sensitive_int&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/m3&#x27;,
  { max_tokens: 2048, messages: [{ content: &#x27;What is the capital of France?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/m3&quot;,
  &quot;max_tokens&quot;: 2048,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What is the capital of France?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With System Prompt</strong>
<p>Using a system prompt to guide behavior</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 2048,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;You are a helpful cooking assistant. Give concise recipes with metric measurements.&quot;,
        &quot;role&quot;: &quot;system&quot;
      },
      {
        &quot;content&quot;: &quot;How do I make a simple pasta aglio e olio?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;temperature&quot;: 0.7
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;# Pasta Aglio e Olio\n\nA classic Italian dish that comes together in minutes with just a few ingredients.\n\n**Serves:** 2 | **Prep:** 5 min | **Cook:** 15 min\n\n## Ingredients\n- 200 g spaghetti or linguine\n- 80 ml extra virgin olive oil\n- 4 garlic cloves, thinly sliced\n- 1\u20132 small dried red chilies, crushed (or \u00bc tsp chili flakes)\n- Salt, for pasta water\n- 15 g fresh flat-leaf parsley, chopped\n- Grated Parmesan or Pecorino (optional, traditionalists skip it)\n\n## Method\n1. **Boil pasta:** Bring a large pot of well-salted water to a rolling boil. Cook the pasta until al dente (about 1 minute less than package instructions). Reserve 1 cup of pasta water before draining.\n2. **Infuse oil:** While the pasta cooks, gently heat the olive oil in a wide pan over low-medium heat. Add the garlic and chilies, and cook slowly for 2\u20133 minutes until the garlic turns pale golden. **Don&#x27;t let it brown** \u2014 it will turn bitter.\n3. **Combine:** Add the drained pasta to the pan with a splash of reserved pasta water. Toss vigorously over medium heat for about 1 minute so the pasta absorbs the oil.\n4. **Finish:** Add more pasta water as needed to create a light, silky sauce that coats the noodles. Stir in the parsley and season with salt.\n5. **Serve** immediately, topped with cheese if using.\n\n## Tips\n- Cold olive oil + slow heat = better flavor extraction.\n- The starch in the pasta water is key to a glossy, emulsified sauce.\n\nBuon appetito! \ud83c\udf5d&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;066cf8abfaba58c357c660ebfad38073&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;# Pasta Aglio e Olio\n\nA classic Italian dish that comes together in minutes with just a few ingredients.\n\n**Serves:** 2 | **Prep:** 5 min | **Cook:** 15 min\n\n## Ingredients\n- 200 g spaghetti or linguine\n- 80 ml extra virgin olive oil\n- 4 garlic cloves, thinly sliced\n- 1\u20132 small dried red chilies, crushed (or \u00bc tsp chili flakes)\n- Salt, for pasta water\n- 15 g fresh flat-leaf parsley, chopped\n- Grated Parmesan or Pecorino (optional, traditionalists skip it)\n\n## Method\n1. **Boil pasta:** Bring a large pot of well-salted water to a rolling boil. Cook the pasta until al dente (about 1 minute less than package instructions). Reserve 1 cup of pasta water before draining.\n2. **Infuse oil:** While the pasta cooks, gently heat the olive oil in a wide pan over low-medium heat. Add the garlic and chilies, and cook slowly for 2\u20133 minutes until the garlic turns pale golden. **Don&#x27;t let it brown** \u2014 it will turn bitter.\n3. **Combine:** Add the drained pasta to the pan with a splash of reserved pasta water. Toss vigorously over medium heat for about 1 minute so the pasta absorbs the oil.\n4. **Finish:** Add more pasta water as needed to create a light, silky sauce that coats the noodles. Stir in the parsley and season with salt.\n5. **Serve** immediately, topped with cheese if using.\n\n## Tips\n- Cold olive oil + slow heat = better flavor extraction.\n- The starch in the pasta water is key to a glossy, emulsified sauce.\n\nBuon appetito! \ud83c\udf5d&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user is asking for a simple pasta aglio e olio recipe. The system prompt says I should give concise recipes with metric measurements. Let me provide a classic, simple recipe.&quot;,
          &quot;reasoning_details&quot;: [
            {
              &quot;type&quot;: &quot;reasoning.text&quot;,
              &quot;id&quot;: &quot;reasoning-text-1&quot;,
              &quot;format&quot;: &quot;MiniMax-response-v1&quot;,
              &quot;index&quot;: 0,
              &quot;text&quot;: &quot;The user is asking for a simple pasta aglio e olio recipe. The system prompt says I should give concise recipes with metric measurements. Let me provide a classic, simple recipe.&quot;
            }
          ]
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336043,
    &quot;model&quot;: &quot;MiniMax-M3&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 595,
      &quot;prompt_tokens&quot;: 197,
      &quot;completion_tokens&quot;: 398,
      &quot;total_characters&quot;: 0,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 114
      }
    },
    &quot;input_sensitive&quot;: false,
    &quot;output_sensitive&quot;: false,
    &quot;base_resp&quot;: {
      &quot;status_code&quot;: 0,
      &quot;status_msg&quot;: &quot;&quot;
    },
    &quot;input_sensitive_type&quot;: 0,
    &quot;output_sensitive_type&quot;: 0,
    &quot;output_sensitive_int&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/m3&#x27;,
  {
    max_tokens: 2048,
    messages: [
      {
        content:
          &#x27;You are a helpful cooking assistant. Give concise recipes with metric measurements.&#x27;,
        role: &#x27;system&#x27;,
      },
      { content: &#x27;How do I make a simple pasta aglio e olio?&#x27;, role: &#x27;user&#x27; },
    ],
    temperature: 0.7,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/m3&quot;,
  &quot;max_tokens&quot;: 2048,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;You are a helpful cooking assistant. Give concise recipes with metric measurements.&quot;,
      &quot;role&quot;: &quot;system&quot;
    },
    {
      &quot;content&quot;: &quot;How do I make a simple pasta aglio e olio?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;temperature&quot;: 0.7
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a conversation with context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 2048,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What are the main differences between TCP and UDP?&quot;,
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;content&quot;: &quot;TCP is connection-oriented and guarantees delivery, while UDP is connectionless and faster but without delivery guarantees.&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      },
      {
        &quot;content&quot;: &quot;When would I choose UDP over TCP?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;temperature&quot;: 0.5
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Use UDP for time-sensitive applications like video streaming, online gaming, or VoIP where speed matters more than perfect reliability.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;066cf8bb1c666fc68c6810518100c7ba&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;Use UDP for time-sensitive applications like video streaming, online gaming, or VoIP where speed matters more than perfect reliability.&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336059,
    &quot;model&quot;: &quot;MiniMax-M3&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 250,
      &quot;prompt_tokens&quot;: 225,
      &quot;completion_tokens&quot;: 25,
      &quot;total_characters&quot;: 0,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 114
      }
    },
    &quot;input_sensitive&quot;: false,
    &quot;output_sensitive&quot;: false,
    &quot;base_resp&quot;: {
      &quot;status_code&quot;: 0,
      &quot;status_msg&quot;: &quot;&quot;
    },
    &quot;input_sensitive_type&quot;: 0,
    &quot;output_sensitive_type&quot;: 0,
    &quot;output_sensitive_int&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/m3&#x27;,
  {
    max_tokens: 2048,
    messages: [
      { content: &#x27;What are the main differences between TCP and UDP?&#x27;, role: &#x27;user&#x27; },
      {
        content:
          &#x27;TCP is connection-oriented and guarantees delivery, while UDP is connectionless and faster but without delivery guarantees.&#x27;,
        role: &#x27;assistant&#x27;,
      },
      { content: &#x27;When would I choose UDP over TCP?&#x27;, role: &#x27;user&#x27; },
    ],
    temperature: 0.5,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/m3&quot;,
  &quot;max_tokens&quot;: 2048,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What are the main differences between TCP and UDP?&quot;,
      &quot;role&quot;: &quot;user&quot;
    },
    {
      &quot;content&quot;: &quot;TCP is connection-oriented and guarantees delivery, while UDP is connectionless and faster but without delivery guarantees.&quot;,
      &quot;role&quot;: &quot;assistant&quot;
    },
    {
      &quot;content&quot;: &quot;When would I choose UDP over TCP?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;temperature&quot;: 0.5
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Creative Writing</strong>
<p>Higher temperature for creative output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 2048,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Write a haiku about programming.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;temperature&quot;: 0.9
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Fingers on the keys,\nBuilding worlds from empty void\u2014\nCode becomes the light.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;066cf8be5675980f2ff647974879fb77&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;Fingers on the keys,\nBuilding worlds from empty void\u2014\nCode becomes the light.&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user wants a haiku about programming. A haiku is a traditional Japanese poem with three lines following a 5-7-5 syllable pattern. I should create one that captures something meaningful about programming.\n\nLet me think of a few options:\n\n1. About debugging:\nLines (5-7-5):\n- \&quot;Bugs hide in the code\&quot; (4) - need 5\n- \&quot;Silent errors whisper\&quot; (6) - need 7\n- \&quot;Find them, fix, deploy\&quot; (5) \u2713\n\nLet me recount:\n- \&quot;Bugs hide in the code\&quot; - Bugs(1) hide(2) in(3) the(4) code(5) = 5 \u2713\n- \&quot;Silent errors whisper\&quot; - Si-lent(2) er-rors(4) whis-per(6) = 6, need 7\n- Try: \&quot;Silent errors always whisper\&quot; - 7 \u2713\n- \&quot;Find them, fix, deploy\&quot; - Find(1) them(2) fix(3) de-ploy(5) = 5 \u2713\n\n2. About code in general:\n- \&quot;Logic flows like streams\&quot; (5) - Lo-gic(2) flows(3) like(4) streams(5) = 5 \u2713\n- \&quot;Through brackets and curved braces\&quot; (7) - Through(1) brack-ets(3) and(4) curved(5) bra-ces(7) = 7 \u2713\n- \&quot;Dreams made into life\&quot; (5) - Dreams(1) made(2) in-to(4) life(5) = 5 \u2713\n\n3. Another option:\n- \&quot;Fingers on the keys\&quot; (5) - Fin-gers(2) on(3) the(4) keys(5) = 5 \u2713\n- \&quot;Building worlds from nothing\&quot; (7) - Build-ing(2) worlds(3) from(4) no-thing(6) = 6, need 7\n- Try: \&quot;Building worlds from empty void\&quot; - Build-ing(2) worlds(3) from(4) emp-ty(6) void(7) = 7 \u2713\n- \&quot;Code becomes the light\&quot; (5) - Code(1) be-comes(3) the(4) light(5) = 5 \u2713\n\nLet me go with option 2 or 3, both are nice. I&#x27;ll provide one clean haiku and maybe offer an alternative.\n\nActually, let me just give one good one. Option 3 feels more poetic and evocative.\n\nLet me verify option 3 once more:\n- \&quot;Fingers on the keys\&quot; - Fin-gers(2) on(3) the(4) keys(5) = 5 \u2713\n- \&quot;Building worlds from empty void\&quot; - Build-ing(2) worlds(3) from(4) emp-ty(6) void(7) = 7 \u2713\n- \&quot;Code becomes the light\&quot; - Code(1) be-comes(3) the(4) light(5) = 5 \u2713\n\nThat works well. I could also provide a simpler one focused on a different aspect of programming.\n\nI&#x27;ll give a haiku with a clean delivery. Let me also think about a second option to make it more useful, or just stick with one well-crafted one.\n\nI&#x27;ll provide one haiku and keep it concise.&quot;,
          &quot;reasoning_details&quot;: [
            {
              &quot;type&quot;: &quot;reasoning.text&quot;,
              &quot;id&quot;: &quot;reasoning-text-1&quot;,
              &quot;format&quot;: &quot;MiniMax-response-v1&quot;,
              &quot;index&quot;: 0,
              &quot;text&quot;: &quot;The user wants a haiku about programming. A haiku is a traditional Japanese poem with three lines following a 5-7-5 syllable pattern. I should create one that captures something meaningful about programming.\n\nLet me think of a few options:\n\n1. About debugging:\nLines (5-7-5):\n- \&quot;Bugs hide in the code\&quot; (4) - need 5\n- \&quot;Silent errors whisper\&quot; (6) - need 7\n- \&quot;Find them, fix, deploy\&quot; (5) \u2713\n\nLet me recount:\n- \&quot;Bugs hide in the code\&quot; - Bugs(1) hide(2) in(3) the(4) code(5) = 5 \u2713\n- \&quot;Silent errors whisper\&quot; - Si-lent(2) er-rors(4) whis-per(6) = 6, need 7\n- Try: \&quot;Silent errors always whisper\&quot; - 7 \u2713\n- \&quot;Find them, fix, deploy\&quot; - Find(1) them(2) fix(3) de-ploy(5) = 5 \u2713\n\n2. About code in general:\n- \&quot;Logic flows like streams\&quot; (5) - Lo-gic(2) flows(3) like(4) streams(5) = 5 \u2713\n- \&quot;Through brackets and curved braces\&quot; (7) - Through(1) brack-ets(3) and(4) curved(5) bra-ces(7) = 7 \u2713\n- \&quot;Dreams made into life\&quot; (5) - Dreams(1) made(2) in-to(4) life(5) = 5 \u2713\n\n3. Another option:\n- \&quot;Fingers on the keys\&quot; (5) - Fin-gers(2) on(3) the(4) keys(5) = 5 \u2713\n- \&quot;Building worlds from nothing\&quot; (7) - Build-ing(2) worlds(3) from(4) no-thing(6) = 6, need 7\n- Try: \&quot;Building worlds from empty void\&quot; - Build-ing(2) worlds(3) from(4) emp-ty(6) void(7) = 7 \u2713\n- \&quot;Code becomes the light\&quot; (5) - Code(1) be-comes(3) the(4) light(5) = 5 \u2713\n\nLet me go with option 2 or 3, both are nice. I&#x27;ll provide one clean haiku and maybe offer an alternative.\n\nActually, let me just give one good one. Option 3 feels more poetic and evocative.\n\nLet me verify option 3 once more:\n- \&quot;Fingers on the keys\&quot; - Fin-gers(2) on(3) the(4) keys(5) = 5 \u2713\n- \&quot;Building worlds from empty void\&quot; - Build-ing(2) worlds(3) from(4) emp-ty(6) void(7) = 7 \u2713\n- \&quot;Code becomes the light\&quot; - Code(1) be-comes(3) the(4) light(5) = 5 \u2713\n\nThat works well. I could also provide a simpler one focused on a different aspect of programming.\n\nI&#x27;ll give a haiku with a clean delivery. Let me also think about a second option to make it more useful, or just stick with one well-crafted one.\n\nI&#x27;ll provide one haiku and keep it concise.&quot;
            }
          ]
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336062,
    &quot;model&quot;: &quot;MiniMax-M3&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 912,
      &quot;prompt_tokens&quot;: 183,
      &quot;completion_tokens&quot;: 729,
      &quot;total_characters&quot;: 0,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 114
      }
    },
    &quot;input_sensitive&quot;: false,
    &quot;output_sensitive&quot;: false,
    &quot;base_resp&quot;: {
      &quot;status_code&quot;: 0,
      &quot;status_msg&quot;: &quot;&quot;
    },
    &quot;input_sensitive_type&quot;: 0,
    &quot;output_sensitive_type&quot;: 0,
    &quot;output_sensitive_int&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/m3&#x27;,
  {
    max_tokens: 2048,
    messages: [{ content: &#x27;Write a haiku about programming.&#x27;, role: &#x27;user&#x27; }],
    temperature: 0.9,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/m3&quot;,
  &quot;max_tokens&quot;: 2048,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Write a haiku about programming.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;temperature&quot;: 0.9
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, user, assistant, tool</td></tr><tr><td><code>messages[].name</code></td><td>string</td><td></td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls</code></td><td>array</td><td></td></tr><tr><td><code>messages[].tool_calls[].id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function.arguments</code></td><td>string</td><td>Required.</td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tools[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools[].function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tools[].function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools[].function.description</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools[].function.parameters</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tool_choice</code></td><td>string</td><td>Values: none, auto</td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.description</code></td><td>string</td><td></td></tr><tr><td><code>response_format.json_schema.schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.schema.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.schema.properties</code></td><td>object</td><td>Required.</td></tr><tr><td><code>mask_sensitive_info</code></td><td>boolean</td><td></td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: user, assistant</td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>system</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>top_k</code></td><td>number</td><td></td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>metadata</code></td><td>object</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array</td><td></td></tr><tr><td><code>choices[].message.tool_calls[].id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.tool_calls[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.tool_calls[].function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.tool_calls[].function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.tool_calls[].function.arguments</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].finish_reason</code></td><td>string</td><td>Required. Values: stop, length, tool_calls</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required. Values: chat.completion, chat.completion.chunk</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>input_sensitive</code></td><td>boolean</td><td></td></tr><tr><td><code>output_sensitive</code></td><td>boolean</td><td></td></tr><tr><td><code>base_resp</code></td><td>object</td><td></td></tr><tr><td><code>base_resp.status_code</code></td><td>number</td><td>Required.</td></tr><tr><td><code>base_resp.status_msg</code></td><td>string</td><td>Required.</td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content</code></td><td>array</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].text</code></td><td>string</td><td></td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>stop_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td>Required.</td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/m3/schema-input.json)
- [Output schema](/ai/models/minimax/m3/schema-output.json)

