---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/openai/gpt-5.5/
  description: openai/gpt-5.5
  full_title: GPT-5.5 · Cloudflare AI docs
  head_html: <title>GPT-5.5 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="openai/gpt-5.5"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/openai/gpt-5.5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="GPT-5.5 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="openai/gpt-5.5"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/openai/gpt-5.5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/openai/gpt-5.5/#page","headline":"GPT-5.5 \u00b7 Cloudflare AI docs","description":"openai/gpt-5.5","url":"https://developers.cloudflare.com/ai/models/openai/gpt-5.5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/openai/gpt-5.5/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-5-5">GPT-5.5</h1>

<p><code>openai/gpt-5.5</code></p>

GPT-5.5 is OpenAI's flagship model with strong coding, reasoning, and multimodal capabilities.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 5, Output tokens (per 1M): 30</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic chat completion request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic chat completion request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What are the three laws of thermodynamics?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The **three laws of thermodynamics** are:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed, only transferred or transformed.  \n   In thermodynamics, this is often written as:  \n   \\[\n   \\Delta U = Q - W\n   \\]  \n   where \\(\\Delta U\\) is the change in internal energy, \\(Q\\) is heat added, and \\(W\\) is work done by the system.\n\n2. **Second Law \u2014 Entropy Increases**  \n   In an isolated system, entropy tends to increase over time.  \n   This means natural processes tend to move toward greater disorder or energy dispersal, and heat flows spontaneously from hot objects to cold ones.\n\n3. **Third Law \u2014 Absolute Zero Is Unattainable**  \n   As the temperature of a perfect crystal approaches absolute zero, its entropy approaches zero.  \n   It also implies that absolute zero, \\(0\\,K\\), cannot be reached by any finite physical process.\n\nThere is also a **Zeroth Law**, which says that if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This is the basis for temperature measurement.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;The **three laws of thermodynamics** are:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed, only transferred or transformed.  \n   In thermodynamics, this is often written as:  \n   \\[\n   \\Delta U = Q - W\n   \\]  \n   where \\(\\Delta U\\) is the change in internal energy, \\(Q\\) is heat added, and \\(W\\) is work done by the system.\n\n2. **Second Law \u2014 Entropy Increases**  \n   In an isolated system, entropy tends to increase over time.  \n   This means natural processes tend to move toward greater disorder or energy dispersal, and heat flows spontaneously from hot objects to cold ones.\n\n3. **Third Law \u2014 Absolute Zero Is Unattainable**  \n   As the temperature of a perfect crystal approaches absolute zero, its entropy approaches zero.  \n   It also implies that absolute zero, \\(0\\,K\\), cannot be reached by any finite physical process.\n\nThere is also a **Zeroth Law**, which says that if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This is the basis for temperature measurement.&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777055247,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DYFXL1K160il6W2QJPWy2h4LmF7Xr&quot;,
    &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 291,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 32,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;prompt_tokens&quot;: 15,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 306
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5&#x27;,
  { messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What are the three laws of thermodynamics?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With System Message</strong>
<p>Using a system message to set context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;,
        &quot;role&quot;: &quot;system&quot;
      },
      {
        &quot;content&quot;: &quot;How do I read a JSON file in Python?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;You can read a JSON file in Python using the built-in `json` module.\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\nIf `data.json` contains:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30\n}\n```\n\nThen `data` will be a Python dictionary:\n\n```python\n{\n    \&quot;name\&quot;: \&quot;Alice\&quot;,\n    \&quot;age\&quot;: 30\n}\n```\n\nYou can access values like this:\n\n```python\nprint(data[\&quot;name\&quot;])  # Alice\nprint(data[\&quot;age\&quot;])   # 30\n```\n\nA slightly more explicit version with encoding:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n    data = json.load(file)\n```\n\nIf you have a JSON string instead of a file, use `json.loads()`:\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n\nprint(data[\&quot;name\&quot;])\n```&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;You can read a JSON file in Python using the built-in `json` module.\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\nIf `data.json` contains:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30\n}\n```\n\nThen `data` will be a Python dictionary:\n\n```python\n{\n    \&quot;name\&quot;: \&quot;Alice\&quot;,\n    \&quot;age\&quot;: 30\n}\n```\n\nYou can access values like this:\n\n```python\nprint(data[\&quot;name\&quot;])  # Alice\nprint(data[\&quot;age\&quot;])   # 30\n```\n\nA slightly more explicit version with encoding:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n    data = json.load(file)\n```\n\nIf you have a JSON string instead of a file, use `json.loads()`:\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n\nprint(data[\&quot;name\&quot;])\n```&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777055247,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DYFXLJQFBS1K4LCprRF4eOgdbucx7&quot;,
    &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 232,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;prompt_tokens&quot;: 30,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 262
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5&#x27;,
  {
    messages: [
      { content: &#x27;You are a helpful coding assistant specializing in Python.&#x27;, role: &#x27;system&#x27; },
      { content: &#x27;How do I read a JSON file in Python?&#x27;, role: &#x27;user&#x27; },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;,
      &quot;role&quot;: &quot;system&quot;
    },
    {
      &quot;content&quot;: &quot;How do I read a JSON file in Python?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a conversation with context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_completion_tokens&quot;: 8192,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;,
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;content&quot;: &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      },
      {
        &quot;content&quot;: &quot;Yes, what are some good places to stop?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Absolutely \u2014 the best stops depend on whether you take the **scenic coastal route** or the **faster inland route**.\n\n## Scenic Route: Highway 1 / 101\nThis is the classic California road trip route, best if you have **1\u20133 days**.\n\n### Great stops from north to south\n- **Half Moon Bay** \u2013 Coastal views, beaches, and a nice breakfast/lunch stop.\n- **Santa Cruz** \u2013 Beach Boardwalk, surfing, casual food, fun atmosphere.\n- **Monterey** \u2013 Monterey Bay Aquarium, Cannery Row, harbor views.\n- **Carmel-by-the-Sea** \u2013 Beautiful village, beach, shops, and restaurants.\n- **Big Sur** \u2013 One of the most scenic stretches in California. Stop at:\n  - Bixby Bridge\n  - Pfeiffer Beach\n  - McWay Falls\n- **San Simeon / Hearst Castle** \u2013 Tour Hearst Castle or see the elephant seals nearby.\n- **Paso Robles** \u2013 Wine tasting and good restaurants, especially if you cut inland.\n- **San Luis Obispo** \u2013 Great overnight stop; downtown, Mission Plaza, good food.\n- **Pismo Beach** \u2013 Beach stop, pier, clam chowder.\n- **Solvang** \u2013 Danish-style town with bakeries, wine tasting, and cute streets.\n- **Santa Barbara** \u2013 One of the best stops: beaches, State Street, the courthouse, Funk Zone.\n- **Malibu** \u2013 Scenic coastal drive, beaches, and a final stop before LA.\n\n## Faster Route: I-5\nBest if you want to get to LA quickly, about **5.5\u20136.5 hours** depending on traffic.\n\nGood practical stops:\n- **Casa de Fruta** \u2013 Roadside stop with snacks, fruit, and restrooms.\n- **Harris Ranch** \u2013 Popular meal stop, especially for steak.\n- **Kettleman City** \u2013 Gas, food, and a good halfway break.\n- **Tejon Ranch / Grapevine area** \u2013 Final major stop before entering LA traffic.\n\n## My recommendation\nIf you have the time, do at least **one overnight** and take the coast:\n\n**Day 1:** San Francisco \u2192 Santa Cruz \u2192 Monterey/Carmel \u2192 Big Sur \u2192 San Luis Obispo  \n**Day 2:** San Luis Obispo \u2192 Solvang \u2192 Santa Barbara \u2192 Malibu \u2192 Los Angeles\n\nAlso, check current road conditions for **Highway 1 near Big Sur**, since closures can happen due to landslides.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;choices&quot;: [
        {
          &quot;finish_reason&quot;: &quot;stop&quot;,
          &quot;index&quot;: 0,
          &quot;message&quot;: {
            &quot;annotations&quot;: [],
            &quot;content&quot;: &quot;Absolutely \u2014 the best stops depend on whether you take the **scenic coastal route** or the **faster inland route**.\n\n## Scenic Route: Highway 1 / 101\nThis is the classic California road trip route, best if you have **1\u20133 days**.\n\n### Great stops from north to south\n- **Half Moon Bay** \u2013 Coastal views, beaches, and a nice breakfast/lunch stop.\n- **Santa Cruz** \u2013 Beach Boardwalk, surfing, casual food, fun atmosphere.\n- **Monterey** \u2013 Monterey Bay Aquarium, Cannery Row, harbor views.\n- **Carmel-by-the-Sea** \u2013 Beautiful village, beach, shops, and restaurants.\n- **Big Sur** \u2013 One of the most scenic stretches in California. Stop at:\n  - Bixby Bridge\n  - Pfeiffer Beach\n  - McWay Falls\n- **San Simeon / Hearst Castle** \u2013 Tour Hearst Castle or see the elephant seals nearby.\n- **Paso Robles** \u2013 Wine tasting and good restaurants, especially if you cut inland.\n- **San Luis Obispo** \u2013 Great overnight stop; downtown, Mission Plaza, good food.\n- **Pismo Beach** \u2013 Beach stop, pier, clam chowder.\n- **Solvang** \u2013 Danish-style town with bakeries, wine tasting, and cute streets.\n- **Santa Barbara** \u2013 One of the best stops: beaches, State Street, the courthouse, Funk Zone.\n- **Malibu** \u2013 Scenic coastal drive, beaches, and a final stop before LA.\n\n## Faster Route: I-5\nBest if you want to get to LA quickly, about **5.5\u20136.5 hours** depending on traffic.\n\nGood practical stops:\n- **Casa de Fruta** \u2013 Roadside stop with snacks, fruit, and restrooms.\n- **Harris Ranch** \u2013 Popular meal stop, especially for steak.\n- **Kettleman City** \u2013 Gas, food, and a good halfway break.\n- **Tejon Ranch / Grapevine area** \u2013 Final major stop before entering LA traffic.\n\n## My recommendation\nIf you have the time, do at least **one overnight** and take the coast:\n\n**Day 1:** San Francisco \u2192 Santa Cruz \u2192 Monterey/Carmel \u2192 Big Sur \u2192 San Luis Obispo  \n**Day 2:** San Luis Obispo \u2192 Solvang \u2192 Santa Barbara \u2192 Malibu \u2192 Los Angeles\n\nAlso, check current road conditions for **Highway 1 near Big Sur**, since closures can happen due to landslides.&quot;,
            &quot;refusal&quot;: null,
            &quot;role&quot;: &quot;assistant&quot;
          }
        }
      ],
      &quot;created&quot;: 1777055396,
      &quot;id&quot;: &quot;chatcmpl-DYFZkYd5fz0fm7iFcu6jZFKFuSxKA&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;object&quot;: &quot;chat.completion&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: {
        &quot;completion_tokens&quot;: 623,
        &quot;completion_tokens_details&quot;: {
          &quot;accepted_prediction_tokens&quot;: 0,
          &quot;audio_tokens&quot;: 0,
          &quot;reasoning_tokens&quot;: 93,
          &quot;rejected_prediction_tokens&quot;: 0
        },
        &quot;prompt_tokens&quot;: 76,
        &quot;prompt_tokens_details&quot;: {
          &quot;audio_tokens&quot;: 0,
          &quot;cached_tokens&quot;: 0
        },
        &quot;total_tokens&quot;: 699
      }
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5&#x27;,
  {
    max_completion_tokens: 8192,
    messages: [
      {
        content: &#x27;I need help planning a road trip from San Francisco to Los Angeles.&#x27;,
        role: &#x27;user&#x27;,
      },
      {
        content:
          &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
        role: &#x27;assistant&#x27;,
      },
      { content: &#x27;Yes, what are some good places to stop?&#x27;, role: &#x27;user&#x27; },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5&quot;,
  &quot;max_completion_tokens&quot;: 8192,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;,
      &quot;role&quot;: &quot;user&quot;
    },
    {
      &quot;content&quot;: &quot;I&#x27;\&#x27;&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
      &quot;role&quot;: &quot;assistant&quot;
    },
    {
      &quot;content&quot;: &quot;Yes, what are some good places to stop?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Creative Writing</strong>
<p>Longer completion for creative output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_completion_tokens&quot;: 8192,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Detective Mara Venn found the clue inside the grandfather clock, though the clock had not worked in twenty years.\n\nThe house was silent around her, all velvet shadows and rain-streaked windows, the kind of silence that made every breath feel borrowed. Lord Edevane\u2019s body lay in the study below, surrounded by overturned books, broken glass, and enough obvious evidence to make Mara immediately distrust all of it.\n\nShe had come upstairs only because of the ticking.\n\nIt was faint, irregular, and impossible.\n\nMara opened the clock\u2019s warped oak door and raised her lantern. No weights. No pendulum. No mechanism at all.\n\nJust a small glass vial hanging from a red thread.\n\nInside the vial was a single human tooth, etched with three tiny words in gold:\n\n**ASK THE DEAD.**&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;Detective Mara Venn found the clue inside the grandfather clock, though the clock had not worked in twenty years.\n\nThe house was silent around her, all velvet shadows and rain-streaked windows, the kind of silence that made every breath feel borrowed. Lord Edevane\u2019s body lay in the study below, surrounded by overturned books, broken glass, and enough obvious evidence to make Mara immediately distrust all of it.\n\nShe had come upstairs only because of the ticking.\n\nIt was faint, irregular, and impossible.\n\nMara opened the clock\u2019s warped oak door and raised her lantern. No weights. No pendulum. No mechanism at all.\n\nJust a small glass vial hanging from a red thread.\n\nInside the vial was a single human tooth, etched with three tiny words in gold:\n\n**ASK THE DEAD.**&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777055252,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DYFXQ7OpB748Ysf32CgoYeohlL1Qm&quot;,
    &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 180,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 8,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;prompt_tokens&quot;: 19,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 199
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5&#x27;,
  {
    max_completion_tokens: 8192,
    messages: [
      {
        content: &#x27;Write a short story opening about a detective finding an unusual clue.&#x27;,
        role: &#x27;user&#x27;,
      },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5&quot;,
  &quot;max_completion_tokens&quot;: 8192,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Streaming Response</strong>
<p>Enable streaming for real-time output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Explain the concept of recursion with a simple example.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;stream&quot;: true,
    &quot;stream_options&quot;: {
      &quot;include_usage&quot;: true
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: [
      &quot;Rec&quot;,
      &quot;ursion&quot;,
      &quot; is&quot;,
      &quot; when&quot;,
      &quot; a&quot;,
      &quot; function&quot;,
      &quot; solves&quot;,
      &quot; a&quot;,
      &quot; problem&quot;,
      &quot; by&quot;,
      &quot; calling&quot;,
      &quot; itself&quot;,
      &quot; with&quot;,
      &quot; a&quot;,
      &quot; smaller&quot;,
      &quot; or&quot;,
      &quot; simpler&quot;,
      &quot; version&quot;,
      &quot; of&quot;,
      &quot; the&quot;,
      &quot; same&quot;,
      &quot; problem&quot;,
      &quot;.\n\n&quot;,
      &quot;A&quot;,
      &quot; recursion&quot;,
      &quot; usually&quot;,
      &quot; has&quot;,
      &quot; two&quot;,
      &quot; parts&quot;,
      &quot;:\n\n&quot;,
      &quot;1&quot;,
      &quot;.&quot;,
      &quot; **&quot;,
      &quot;Base&quot;,
      &quot; case&quot;,
      &quot;**&quot;,
      &quot;:&quot;,
      &quot; when&quot;,
      &quot; to&quot;,
      &quot; stop&quot;,
      &quot; calling&quot;,
      &quot; itself&quot;,
      &quot;.\n&quot;,
      &quot;2&quot;,
      &quot;.&quot;,
      &quot; **&quot;,
      &quot;Recursive&quot;,
      &quot; case&quot;,
      &quot;**&quot;,
      &quot;:&quot;,
      &quot; the&quot;,
      &quot; part&quot;,
      &quot; where&quot;,
      &quot; the&quot;,
      &quot; function&quot;,
      &quot; calls&quot;,
      &quot; itself&quot;,
      &quot;.\n\n&quot;,
      &quot;Example&quot;,
      &quot;:&quot;,
      &quot; counting&quot;,
      &quot; down&quot;,
      &quot; from&quot;,
      &quot; a&quot;,
      &quot; number&quot;,
      &quot;.\n\n&quot;,
      &quot;```&quot;,
      &quot;python&quot;,
      &quot;\n&quot;,
      &quot;def&quot;,
      &quot; countdown&quot;,
      &quot;(n&quot;,
      &quot;):\n&quot;,
      &quot;   &quot;,
      &quot; if&quot;,
      &quot; n&quot;,
      &quot; ==&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot;:&quot;,
      &quot;         &quot;,
      &quot; #&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot;\n&quot;,
      &quot;       &quot;,
      &quot; print&quot;,
      &quot;(\&quot;&quot;,
      &quot;Done&quot;,
      &quot;!\&quot;)\n&quot;,
      &quot;   &quot;,
      &quot; else&quot;,
      &quot;:\n&quot;,
      &quot;       &quot;,
      &quot; print&quot;,
      &quot;(n&quot;,
      &quot;)\n&quot;,
      &quot;       &quot;,
      &quot; countdown&quot;,
      &quot;(n&quot;,
      &quot; -&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;)&quot;,
      &quot; #&quot;,
      &quot; recursive&quot;,
      &quot; case&quot;,
      &quot;\n\n&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)\n&quot;,
      &quot;``&quot;,
      &quot;`\n\n&quot;,
      &quot;Output&quot;,
      &quot;:\n\n&quot;,
      &quot;```&quot;,
      &quot;text&quot;,
      &quot;\n&quot;,
      &quot;3&quot;,
      &quot;\n&quot;,
      &quot;2&quot;,
      &quot;\n&quot;,
      &quot;1&quot;,
      &quot;\n&quot;,
      &quot;Done&quot;,
      &quot;!\n&quot;,
      &quot;``&quot;,
      &quot;`\n\n&quot;,
      &quot;Here&quot;,
      &quot; is&quot;,
      &quot; what&quot;,
      &quot; happens&quot;,
      &quot;:\n\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)`&quot;,
      &quot; prints&quot;,
      &quot; `&quot;,
      &quot;3&quot;,
      &quot;`,&quot;,
      &quot; then&quot;,
      &quot; calls&quot;,
      &quot; `&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)`\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)`&quot;,
      &quot; prints&quot;,
      &quot; `&quot;,
      &quot;2&quot;,
      &quot;`,&quot;,
      &quot; then&quot;,
      &quot; calls&quot;,
      &quot; `&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)`\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)`&quot;,
      &quot; prints&quot;,
      &quot; `&quot;,
      &quot;1&quot;,
      &quot;`,&quot;,
      &quot; then&quot;,
      &quot; calls&quot;,
      &quot; `&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;0&quot;,
      &quot;)`\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;count&quot;,
      &quot;down&quot;,
      &quot;(&quot;,
      &quot;0&quot;,
      &quot;)`&quot;,
      &quot; reaches&quot;,
      &quot; the&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot; and&quot;,
      &quot; stops&quot;,
      &quot;\n\n&quot;,
      &quot;So&quot;,
      &quot;,&quot;,
      &quot; recursion&quot;,
      &quot; is&quot;,
      &quot; like&quot;,
      &quot; breaking&quot;,
      &quot; a&quot;,
      &quot; problem&quot;,
      &quot; into&quot;,
      &quot; smaller&quot;,
      &quot; versions&quot;,
      &quot; of&quot;,
      &quot; itself&quot;,
      &quot; until&quot;,
      &quot; reaching&quot;,
      &quot; a&quot;,
      &quot; stopping&quot;,
      &quot; point&quot;,
      &quot;.&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;refusal&quot;: null,
            &quot;role&quot;: &quot;assistant&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;5EGG4gGR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Rec&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;PC9MLZ9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;VbG0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;8mi93Nd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; when&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;eGE27&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;rZkBfGOc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;V&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solves&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Rs8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;kmUAKF1C&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;DQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; by&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;S18dDfo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calling&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;G2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;bNE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; with&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;djMLK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;XyNGTKNo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;3X&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;kwO1s6O&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; simpler&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;B1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; version&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Ka&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;D9gzGmg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;eyaDYN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; same&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;qTvce&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ev&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;TyCFD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;A&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;bT9SqCNg9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; usually&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;NI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; has&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;hDgXv1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; two&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ys7Caj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; parts&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;mIIl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;pfhft&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;zjiO0PgFQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;XQj11tI80&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;5MSIOYl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;n1SttB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;eFRpn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;FHmNxqWk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;6lEr6D5e6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; when&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;b0Gqx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;l9zpsGr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stop&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;v2IVk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calling&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;LS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;l5d&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;fSrrHjQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;EbwKdcU9C&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ZmDxJwt9z&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;h7MPbW9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;W&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;uCnrV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;0eSlK0Mp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;1kcOBGCKD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;pnR7nw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; part&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;soMOx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; where&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;dyu2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;1pIuYF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;N&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;zwhN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;YKL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;dnqD3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;4Kc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;fZWxhWq4C&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; counting&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;v&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;uKvpx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; from&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;SFDwO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;BPv79srW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; number&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;8Uv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;uYxTV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;BJFTTvo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;rAfM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Z8CYnqBF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;def&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;pD7EKZy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; countdown&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;zEcpl7Uj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;):\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;cU2hpq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;340wsD3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; if&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;MI5xT6S&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;wQtnb0t7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ==&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;k3JYQpd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;GZrobqnTv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;yDNgFClM0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ddvWbP2ox&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;         &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;T&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ISah9B3n&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;5O0ER&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;PsfLL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;0c0SEoRu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Iqu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; print&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ktAa&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(\&quot;&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;q8rK1md&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Done&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Pb7qja&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!\&quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;hM9g&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;7dsqwxK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; else&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;hsxJh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;hf6uqTN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;9yw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; print&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;9jES&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;bUKArc88&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;mJZUouj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Mua&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; countdown&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;er9iOSmy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; -&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;UQw3iqsz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;hUEoqTGnn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;V79RiPWpp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;jpiRQPl6B&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;SxPFlq3E&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;o7Wyd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;zilGBD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ziES1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;3QqZOu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Kxha7lo8v&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Oct10c5XA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;23voDY5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;``&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;mCgDQLxG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;gRY8h&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Output&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;7GNA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;8x3vj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;4vYxHC4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;text&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;0sS6nN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;meHuLw0X&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;gJQuhgzFd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Jvo8FBc6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;dnxIufcD8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Km7a8UC7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;cYO7Hxt15&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;W4ExVvIC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Done&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;0sbKSu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;HKIwuqW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;``&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;bE7NIioE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Fyg0m&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Here&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;DbV9Ca&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;1S76ZNh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; what&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;8Lh3Y&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; happens&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;DP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;bM3YN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;zF8dlBeTS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;OCRFD1hj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;bQYFO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;5ga1k2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Wn9bV2HDq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Ia66AmeQj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;cvuPanLZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; prints&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;A7r&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;R1D6358y&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;QB4hqywe9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;9uOadFNj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; then&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;dQYrZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;o69o&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;EEO2ns82&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;G47jn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;vo4rPU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ggg2PlJel&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;8kr8iyNnj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;hsDppb&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;aUpOvuVEx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;yJZdR09a&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;g1X41&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;xdezpZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Mm6maKbsQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;XLs3BhCni&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;EL2BZ7I7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; prints&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;VVT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;fDVz4cAh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;J0llIjLRB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;MBSp0S5Y&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; then&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;oX6BU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;T6n7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;GjdJrmSC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;WViGq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Ul09xE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;hFml3ZuxN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;82s2kqnYC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;1V388U&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;6nzVtVPxg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;0SKjbMEQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;WiUO0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;kMsbJK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;QAV2f73XY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;aRJg0P21i&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;7qbxr9gw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; prints&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Rlo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;wP5W58a1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;E45ycnlvV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;HqEtskaW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; then&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;dVynU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;2JMj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;VijtM4hV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Bu8uB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;vDuCrr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;VT5daebp9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;aL3hgZrRx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;zWpKQx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;CGySUTwSi&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;cJIm5UE6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;BhrYW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;TbSQw8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;TDvUTQTfF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;4IQqIcWmu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;UnGrAM5K&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reaches&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;ir&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;VKcp34&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;NlIPy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Do891&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; and&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Ml5po1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stops&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;QvuX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;PUvfwe&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;So&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;udBwKUNV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;khMfhrK3j&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;jqHYqr1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; like&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;tN1Td&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; breaking&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;c&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;sQ7bP50u&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;Mo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; into&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;8tNcs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;4s&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; versions&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;z&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;EnKEPrh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;jaZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; until&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;2tDV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reaching&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;N&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;AFM2inZS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stopping&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; point&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;YNdx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;rDzVGxf5r&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {},
          &quot;finish_reason&quot;: &quot;stop&quot;,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;PRdn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [],
      &quot;created&quot;: 1777055295,
      &quot;id&quot;: &quot;chatcmpl-DYFY7TPENOUYNWL4XUE07mP4N37Jp&quot;,
      &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
      &quot;obfuscation&quot;: &quot;0lMavgk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: {
        &quot;completion_tokens&quot;: 228,
        &quot;completion_tokens_details&quot;: {
          &quot;accepted_prediction_tokens&quot;: 0,
          &quot;audio_tokens&quot;: 0,
          &quot;reasoning_tokens&quot;: 0,
          &quot;rejected_prediction_tokens&quot;: 0
        },
        &quot;prompt_tokens&quot;: 16,
        &quot;prompt_tokens_details&quot;: {
          &quot;audio_tokens&quot;: 0,
          &quot;cached_tokens&quot;: 0
        },
        &quot;total_tokens&quot;: 244
      }
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5&#x27;,
  {
    messages: [{ content: &#x27;Explain the concept of recursion with a simple example.&#x27;, role: &#x27;user&#x27; }],
    stream: true,
    stream_options: { include_usage: true },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Explain the concept of recursion with a simple example.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;stream&quot;: true,
  &quot;stream_options&quot;: {
    &quot;include_usage&quot;: true
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Web Search</strong>
<p>Letting the model use OpenAI's built-in web search tool to answer with current information</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;What were the top news stories about Cloudflare this week? Summarise in three bullets.&quot;,
    &quot;max_output_tokens&quot;: 4096,
    &quot;tools&quot;: [
      {
        &quot;type&quot;: &quot;web_search_preview&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Treating \u201cthis week\u201d as **June 15\u201322, 2026**:\n\n- **Cloudflare had a North America/Europe-impacting service incident on June 22.** Its status page said increased error rates and latency began at **13:35 UTC**, affecting **Analytics, CDN/Cache, and Durable Objects**; Cloudflare later pointed to a **fiber cut in Eastern North America** and said traffic-engineering work had mitigated most congestion/packet drops by the afternoon. ([cloudflarestatus.com](https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51))\n\n- **Cloudflare pushed harder into AI-assisted Zero Trust/SASE deployments.** It launched the **Cloudflare One Stack**, a set of agent \u201cskills\u201d for configuring, migrating, and managing Zero Trust environments, alongside a new **Cloudflare One Design Partner** initiative aimed at partners helping customers move from legacy security architectures; early named partners included Arctiq, Consortium, CMT, Presidio, and The Missing Link. ([blog.cloudflare.com](https://blog.cloudflare.com/cloudflare-one-stack/))\n\n- **Cloudflare advanced its \u201cAI agents can build and deploy\u201d strategy.** It introduced **Temporary Cloudflare Accounts for AI agents**, letting agents use `wrangler deploy --temporary` to ship Workers without a prior account for a 60-minute claim window, and also opened more Agents SDK primitives to frameworks such as **Flue** for durable, production-grade agent workflows. ([blog.cloudflare.com](https://blog.cloudflare.com/temporary-accounts/))&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_04a2eb20ce6ad6f8016a3999229868819ba43a3002b7e5e301&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1782159650,
    &quot;model&quot;: &quot;gpt-5.5-2026-04-23&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a399923112c819bbabc8ec848f597e2&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a399923ced4819b94eb840567ee5fc1&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare news this week June 2026 Cloudflare&quot;,
            &quot;Cloudflare latest news June 2026&quot;,
            &quot;site:blog.cloudflare.com Cloudflare June 2026&quot;,
            &quot;Cloudflare stock news this week June 2026&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare news this week June 2026 Cloudflare&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a3999282ad8819ba080a8ddfee09e0e&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a39992838d8819b82979350fb85558b&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare outage June 22 2026 status incident&quot;,
            &quot;Cloudflare June 22 2026 outage&quot;,
            &quot;Cloudflare launches partner initiative AI SASE adoption June 18 2026&quot;,
            &quot;Cloudflare news June 17 2026&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare outage June 22 2026 status incident&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a39992b85b8819b8494e22e7f1ade54&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a39992b9090819b868cc4de44726b49&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;site:blog.cloudflare.com June 18 2026 Cloudflare blog&quot;,
            &quot;site:blog.cloudflare.com June 17 2026 Cloudflare blog&quot;,
            &quot;site:blog.cloudflare.com June 16 2026 Cloudflare blog&quot;,
            &quot;site:blog.cloudflare.com June 15 2026 Cloudflare blog&quot;
          ],
          &quot;query&quot;: &quot;site:blog.cloudflare.com June 18 2026 Cloudflare blog&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a39992d42b8819b91e73be8db39cf7f&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a39992d7720819bb7a20bb6db6d12a7&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://www.cloudflarestatus.com/uptime&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a39992eccb0819ba2f60db633880269&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a39992f55d4819b90baed7dcc1189b4&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a3999317194819b8aa69341a57c7022&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a3999321808819b8065a8f50825261d&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare after:2026-06-15 before:2026-06-23 news&quot;,
            &quot;Cloudflare site:reuters.com after:2026-06-15 before:2026-06-23&quot;,
            &quot;Cloudflare site:finance.yahoo.com after:2026-06-15 before:2026-06-23&quot;,
            &quot;Cloudflare site:investors.com after:2026-06-15 before:2026-06-23&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare after:2026-06-15 before:2026-06-23 news&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a3999393be8819bb6199dd097e3c451&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a39993a4038819bb990a96c3388c97f&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare Flue agent harnesses frameworks June 2026&quot;,
            &quot;site:blog.cloudflare.com Flue Cloudflare June 2026&quot;,
            &quot;\&quot;Bringing more agent harnesses\&quot; Cloudflare&quot;,
            &quot;Cloudflare AI Agents SDK Flue June 2026&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare Flue agent harnesses frameworks June 2026&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a399941a9ec819b9772297dbafe616a&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a399941c820819b9c737c5bbac428a5&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://noise.getoto.net/2026/06/17/bringing-more-agent-harnesses-and-frameworks-to-cloudflare-starting-with-flue/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a399943832c819bb678926f11223a00&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a399943e4d0819bbfeb601cd55a683d&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://blog.cloudflare.com/agents-platform-flue-sdk/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a399945c25c819b8329904bba285bd7&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a3999491ed0819b8c1623b7545fca7a&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://blog.cloudflare.com/temporary-cloudflare-accounts-for-ai-agents/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a39994b78d0819b8e663097a07806c8&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a39994bb2c4819bb73593fb0cf46293&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://blog.cloudflare.com/agents-platform-flue-sdk/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a39994f2f9c819b9088ecfeb3e06e00&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_04a2eb20ce6ad6f8016a39994f902c819bb852d31e550d7771&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://blog.cloudflare.com/temporary-accounts/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_04a2eb20ce6ad6f8016a399950fae4819ba302f413d4bfaf40&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;msg_04a2eb20ce6ad6f8016a399953b544819ba7651b7966a4cb7e&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 511,
                &quot;start_index&quot;: 430,
                &quot;title&quot;: &quot;Cloudflare Status - Increased Error Rates&quot;,
                &quot;url&quot;: &quot;https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51&quot;
              },
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 1021,
                &quot;start_index&quot;: 947,
                &quot;title&quot;: &quot;Introducing the Cloudflare One stack: agent-powered deployment&quot;,
                &quot;url&quot;: &quot;https://blog.cloudflare.com/cloudflare-one-stack/&quot;
              },
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 1471,
                &quot;start_index&quot;: 1399,
                &quot;title&quot;: &quot;Temporary Cloudflare Accounts for AI agents&quot;,
                &quot;url&quot;: &quot;https://blog.cloudflare.com/temporary-accounts/&quot;
              }
            ],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Treating \u201cthis week\u201d as **June 15\u201322, 2026**:\n\n- **Cloudflare had a North America/Europe-impacting service incident on June 22.** Its status page said increased error rates and latency began at **13:35 UTC**, affecting **Analytics, CDN/Cache, and Durable Objects**; Cloudflare later pointed to a **fiber cut in Eastern North America** and said traffic-engineering work had mitigated most congestion/packet drops by the afternoon. ([cloudflarestatus.com](https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51))\n\n- **Cloudflare pushed harder into AI-assisted Zero Trust/SASE deployments.** It launched the **Cloudflare One Stack**, a set of agent \u201cskills\u201d for configuring, migrating, and managing Zero Trust environments, alongside a new **Cloudflare One Design Partner** initiative aimed at partners helping customers move from legacy security architectures; early named partners included Arctiq, Consortium, CMT, Presidio, and The Missing Link. ([blog.cloudflare.com](https://blog.cloudflare.com/cloudflare-one-stack/))\n\n- **Cloudflare advanced its \u201cAI agents can build and deploy\u201d strategy.** It introduced **Temporary Cloudflare Accounts for AI agents**, letting agents use `wrangler deploy --temporary` to ship Workers without a prior account for a 60-minute claim window, and also opened more Agents SDK primitives to frameworks such as **Flue** for durable, production-grade agent workflows. ([blog.cloudflare.com](https://blog.cloudflare.com/temporary-accounts/))&quot;
          }
        ],
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      }
    ],
    &quot;status&quot;: &quot;completed&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 83593,
      &quot;output_tokens&quot;: 1842,
      &quot;total_tokens&quot;: 85435,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 4224
      },
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 1515
      }
    },
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1782159704,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 4096,
    &quot;max_tool_calls&quot;: null,
    &quot;moderation&quot;: null,
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;24h&quot;,
    &quot;reasoning&quot;: {
      &quot;context&quot;: &quot;current_turn&quot;,
      &quot;effort&quot;: &quot;medium&quot;,
      &quot;summary&quot;: null
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;store&quot;: false,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      },
      &quot;verbosity&quot;: &quot;medium&quot;
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [
      {
        &quot;type&quot;: &quot;web_search_preview&quot;,
        &quot;search_content_types&quot;: [
          &quot;text&quot;
        ],
        &quot;search_context_size&quot;: &quot;medium&quot;,
        &quot;user_location&quot;: {
          &quot;type&quot;: &quot;approximate&quot;,
          &quot;city&quot;: null,
          &quot;country&quot;: &quot;US&quot;,
          &quot;region&quot;: null,
          &quot;timezone&quot;: null
        }
      }
    ],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.98,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;user&quot;: null,
    &quot;metadata&quot;: {},
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5&#x27;,
  {
    input: &#x27;What were the top news stories about Cloudflare this week? Summarise in three bullets.&#x27;,
    max_output_tokens: 4096,
    tools: [{ type: &#x27;web_search_preview&#x27; }],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5&quot;,
  &quot;input&quot;: &quot;What were the top news stories about Cloudflare this week? Summarise in three bullets.&quot;,
  &quot;max_output_tokens&quot;: 4096,
  &quot;tools&quot;: [
    {
      &quot;type&quot;: &quot;web_search_preview&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-5.5/schema-input.json)
- [Output schema](/ai/models/openai/gpt-5.5/schema-output.json)

