---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/xai/grok-4.20-multi-agent-0309/
  description: xai/grok-4.20-multi-agent-0309
  full_title: Grok 4.20 Multi-Agent · Cloudflare AI docs
  head_html: <title>Grok 4.20 Multi-Agent · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="xai/grok-4.20-multi-agent-0309"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/xai/grok-4.20-multi-agent-0309/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Grok 4.20 Multi-Agent · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="xai/grok-4.20-multi-agent-0309"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/xai/grok-4.20-multi-agent-0309/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/xai/grok-4.20-multi-agent-0309/#page","headline":"Grok 4.20 Multi-Agent \u00b7 Cloudflare AI docs","description":"xai/grok-4.20-multi-agent-0309","url":"https://developers.cloudflare.com/ai/models/xai/grok-4.20-multi-agent-0309/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/xai/grok-4.20-multi-agent-0309/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-4-20-multi-agent">Grok 4.20 Multi-Agent</h1>

<p><code>xai/grok-4.20-multi-agent-0309</code></p>

xAI's Grok 4.20 multi-agent model with a 2M-token context window. Multiple agents collaborate in parallel to perform deep research tasks, with function calling, structured outputs, and reasoning capabilities.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>2,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 6, Cached input tokens (per 1M): 0.2</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic Responses API request with a string input

<section class="model-example"><strong>Simple Question</strong>
<p>Basic Responses API request with a string input</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;What are the three laws of thermodynamics?&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;**The three laws of thermodynamics** (often referred to as the first, second, and third) are fundamental principles in physics that govern energy, heat, work, and entropy in physical systems. There is also a foundational \&quot;zeroth law\&quot; that is logically prior but was formalized later, which is why it is numbered zero.\n\nHere is a clear summary of each:\n\n### Zeroth Law of Thermodynamics (Thermal Equilibrium)\nIf two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other. This law establishes the concept of temperature and allows us to use thermometers meaningfully. It is the basis for all temperature measurement but is not always counted among the original \&quot;three laws.\&quot;\n\n### First Law of Thermodynamics (Conservation of Energy)\nEnergy cannot be created or destroyed, only converted from one form to another or transferred as heat or work.  \nMathematically: **\u0394U = Q \u2212 W** (where \u0394U is the change in internal energy of a system, Q is heat added to the system, and W is work done by the system).  \nThis is essentially the law of conservation of energy applied to thermodynamic processes.\n\n### Second Law of Thermodynamics (Entropy and Directionality)\nThe total entropy of an isolated system can never decrease over time. It either stays the same (in reversible processes) or increases (in irreversible processes).  \nThis law explains why heat flows spontaneously from hot objects to cold ones (never the reverse), why some processes are irreversible, and the concept of the arrow of time. It also implies that it is impossible to build a perfectly efficient heat engine or a perpetual motion machine of the second kind.\n\n### Third Law of Thermodynamics (Absolute Zero and Entropy)\nAs the temperature of a system approaches absolute zero (0 Kelvin or -273.15\u00b0C), the entropy of a perfect crystalline substance approaches a minimum value (often taken as zero).  \nThis law implies that absolute zero is theoretically unreachable in a finite number of steps and has important consequences for the behavior of matter at extremely low temperatures.\n\nThese laws form the foundation of classical thermodynamics, with wide applications in physics, chemistry, engineering, and biology. They are empirical laws derived from centuries of observation and experimentation.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;completed_at&quot;: 1777679670,
    &quot;created_at&quot;: 0,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;0717357c-40f0-91d2-84db-cd601a0759e4&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {
      &quot;system_fingerprint&quot;: &quot;&quot;
    },
    &quot;model&quot;: &quot;grok-4.20-multi-agent-0309&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;**The three laws of thermodynamics** (often referred to as the first, second, and third) are fundamental principles in physics that govern energy, heat, work, and entropy in physical systems. There is also a foundational \&quot;zeroth law\&quot; that is logically prior but was formalized later, which is why it is numbered zero.\n\nHere is a clear summary of each:\n\n### Zeroth Law of Thermodynamics (Thermal Equilibrium)\nIf two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other. This law establishes the concept of temperature and allows us to use thermometers meaningfully. It is the basis for all temperature measurement but is not always counted among the original \&quot;three laws.\&quot;\n\n### First Law of Thermodynamics (Conservation of Energy)\nEnergy cannot be created or destroyed, only converted from one form to another or transferred as heat or work.  \nMathematically: **\u0394U = Q \u2212 W** (where \u0394U is the change in internal energy of a system, Q is heat added to the system, and W is work done by the system).  \nThis is essentially the law of conservation of energy applied to thermodynamic processes.\n\n### Second Law of Thermodynamics (Entropy and Directionality)\nThe total entropy of an isolated system can never decrease over time. It either stays the same (in reversible processes) or increases (in irreversible processes).  \nThis law explains why heat flows spontaneously from hot objects to cold ones (never the reverse), why some processes are irreversible, and the concept of the arrow of time. It also implies that it is impossible to build a perfectly efficient heat engine or a perpetual motion machine of the second kind.\n\n### Third Law of Thermodynamics (Absolute Zero and Entropy)\nAs the temperature of a system approaches absolute zero (0 Kelvin or -273.15\u00b0C), the entropy of a perfect crystalline substance approaches a minimum value (often taken as zero).  \nThis law implies that absolute zero is theoretically unreachable in a finite number of steps and has important consequences for the behavior of matter at extremely low temperatures.\n\nThese laws form the foundation of classical thermodynamics, with wide applications in physics, chemistry, engineering, and biology. They are empirical laws derived from centuries of observation and experimentation.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_0717357c-40f0-91d2-84db-cd601a0759e4&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;,
      &quot;summary&quot;: &quot;detailed&quot;
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: true,
    &quot;temperature&quot;: 0.7,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      }
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.95,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;cost_in_usd_ticks&quot;: 127946000,
      &quot;input_tokens&quot;: 11014,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 8448
      },
      &quot;num_server_side_tools_used&quot;: 0,
      &quot;num_sources_used&quot;: 0,
      &quot;output_tokens&quot;: 3159,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 2704
      },
      &quot;total_tokens&quot;: 14173
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-multi-agent-0309&#x27;,
  { input: &#x27;What are the three laws of thermodynamics?&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.20-multi-agent-0309&quot;,
  &quot;input&quot;: &quot;What are the three laws of thermodynamics?&quot;
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With Instructions</strong>
<p>Using instructions to set the agent persona</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;In two sentences, why does the moon appear larger near the horizon?&quot;,
    &quot;instructions&quot;: &quot;You are a careful research assistant. Keep answers short and cite sources when relevant.&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The Moon appears larger near the horizon because of a perceptual illusion (not an optical one): the brain interprets the horizon as farther away than the zenith due to distance cues from terrain and the flattened-dome appearance of the sky, so it scales up the Moon&#x27;s perceived size to match its unchanged angular diameter. High in the sky with no such references, the Moon looks comparatively smaller.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;completed_at&quot;: 1777679665,
    &quot;created_at&quot;: 0,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;86852e2f-b620-e6a1-8b6a-ddcf1c0348bc&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: &quot;You are a careful research assistant. Keep answers short and cite sources when relevant.&quot;,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {
      &quot;system_fingerprint&quot;: &quot;&quot;
    },
    &quot;model&quot;: &quot;grok-4.20-multi-agent-0309&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;The Moon appears larger near the horizon because of a perceptual illusion (not an optical one): the brain interprets the horizon as farther away than the zenith due to distance cues from terrain and the flattened-dome appearance of the sky, so it scales up the Moon&#x27;s perceived size to match its unchanged angular diameter. High in the sky with no such references, the Moon looks comparatively smaller.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_86852e2f-b620-e6a1-8b6a-ddcf1c0348bc&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;,
      &quot;summary&quot;: &quot;detailed&quot;
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: true,
    &quot;temperature&quot;: 0.7,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      }
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.95,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;cost_in_usd_ticks&quot;: 69728000,
      &quot;input_tokens&quot;: 3682,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 3264
      },
      &quot;num_server_side_tools_used&quot;: 0,
      &quot;num_sources_used&quot;: 0,
      &quot;output_tokens&quot;: 2319,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 2230
      },
      &quot;total_tokens&quot;: 6001
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-multi-agent-0309&#x27;,
  {
    input: &#x27;In two sentences, why does the moon appear larger near the horizon?&#x27;,
    instructions:
      &#x27;You are a careful research assistant. Keep answers short and cite sources when relevant.&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.20-multi-agent-0309&quot;,
  &quot;input&quot;: &quot;In two sentences, why does the moon appear larger near the horizon?&quot;,
  &quot;instructions&quot;: &quot;You are a careful research assistant. Keep answers short and cite sources when relevant.&quot;
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a conversation by passing typed input items</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: [
      {
        &quot;content&quot;: &quot;I need to plan a 3-day weekend in Tokyo.&quot;,
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;content&quot;: &quot;Sounds fun. Are you more interested in food, culture, or nightlife? That will steer the recommendations.&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      },
      {
        &quot;content&quot;: &quot;Food. Suggest one signature dish per day in one sentence each.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;max_output_tokens&quot;: 8192
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;**Day 1:** Begin your Tokyo food journey by savoring fresh Edomae-style nigiri sushi at Tsukiji Outer Market, where skilled chefs pair perfectly seasoned rice with the day&#x27;s freshest seafood straight from the market.  \n**Day 2:** Dive into a rich bowl of tonkotsu ramen in a bustling Shinjuku shop, featuring silky pork-bone broth, springy noodles, chashu pork, and a marinated egg for ultimate comfort.  \n**Day 3:** Conclude the weekend by grilling premium A5 Wagyu yakiniku tableside in Roppongi, savoring melt-in-your-mouth slices of marbled Japanese beef alongside vegetables and savory dipping sauces.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;completed_at&quot;: 1777679685,
    &quot;created_at&quot;: 0,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;eb44cf72-01bc-0674-a7de-b31df024f668&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 8192,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {
      &quot;system_fingerprint&quot;: &quot;&quot;
    },
    &quot;model&quot;: &quot;grok-4.20-multi-agent-0309&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;**Day 1:** Begin your Tokyo food journey by savoring fresh Edomae-style nigiri sushi at Tsukiji Outer Market, where skilled chefs pair perfectly seasoned rice with the day&#x27;s freshest seafood straight from the market.  \n**Day 2:** Dive into a rich bowl of tonkotsu ramen in a bustling Shinjuku shop, featuring silky pork-bone broth, springy noodles, chashu pork, and a marinated egg for ultimate comfort.  \n**Day 3:** Conclude the weekend by grilling premium A5 Wagyu yakiniku tableside in Roppongi, savoring melt-in-your-mouth slices of marbled Japanese beef alongside vegetables and savory dipping sauces.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_eb44cf72-01bc-0674-a7de-b31df024f668&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;,
      &quot;summary&quot;: &quot;detailed&quot;
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: true,
    &quot;temperature&quot;: 0.7,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      }
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.95,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;cost_in_usd_ticks&quot;: 249846000,
      &quot;input_tokens&quot;: 16886,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 11648
      },
      &quot;num_server_side_tools_used&quot;: 0,
      &quot;num_sources_used&quot;: 0,
      &quot;output_tokens&quot;: 6443,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 6288
      },
      &quot;total_tokens&quot;: 23329
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-multi-agent-0309&#x27;,
  {
    input: [
      { content: &#x27;I need to plan a 3-day weekend in Tokyo.&#x27;, role: &#x27;user&#x27; },
      {
        content:
          &#x27;Sounds fun. Are you more interested in food, culture, or nightlife? That will steer the recommendations.&#x27;,
        role: &#x27;assistant&#x27;,
      },
      { content: &#x27;Food. Suggest one signature dish per day in one sentence each.&#x27;, role: &#x27;user&#x27; },
    ],
    max_output_tokens: 8192,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.20-multi-agent-0309&quot;,
  &quot;input&quot;: [
    {
      &quot;content&quot;: &quot;I need to plan a 3-day weekend in Tokyo.&quot;,
      &quot;role&quot;: &quot;user&quot;
    },
    {
      &quot;content&quot;: &quot;Sounds fun. Are you more interested in food, culture, or nightlife? That will steer the recommendations.&quot;,
      &quot;role&quot;: &quot;assistant&quot;
    },
    {
      &quot;content&quot;: &quot;Food. Suggest one signature dish per day in one sentence each.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;max_output_tokens&quot;: 8192
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Web Search</strong>
<p>Letting the agent use xAI built-in web search to answer with current info</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;What were the top news stories about xAI this week? Summarise in three bullets.&quot;,
    &quot;max_turns&quot;: 4,
    &quot;tools&quot;: [
      {
        &quot;type&quot;: &quot;web_search&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;**Top xAI news stories this week (late April to early May 2026):**[[1]](https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/)[[2]](https://x.ai/news)\n\n- **Elon Musk testified in his lawsuit against OpenAI**, admitting that xAI had \u201cpartly\u201d used OpenAI models (via distillation techniques) to train Grok. The multi-day testimony framed Musk as an AI safety advocate contrasting with OpenAI\u2019s for-profit shift; it occurred as xAI operates under its recent acquisition by SpaceX.[[1]](https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/)[[3]](https://www.theverge.com/ai-artificial-intelligence/921546/elon-musk-xai-openai-trial-model-distillation)\n\n- **xAI released major voice and audio updates**, including Custom Voices/Voice Library (allowing voice cloning from short recordings), Grok Voice Think Fast 1.0 (a capable voice agent for API use), and Speech-to-Text/Text-to-Speech APIs with natural voices, multilingual support, and simple pricing (announced April 23\u201330).[[2]](https://x.ai/news)\n\n- **Grok 4.3 launched with strong benchmarks and aggressive pricing**, scoring 53 on the Artificial Analysis Intelligence Index (improved agentic/tool-use performance, ~4 points ahead of its predecessor), alongside ~40\u201360% price cuts; this ties into broader product momentum and the post-acquisition context, though some reports noted employee departures and prior coding lags.[[4]](https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite)\n\nThese reflect xAI\u2019s rapid product iteration in voice/agent capabilities and model performance while navigating legal, integration, and operational developments following the SpaceX deal.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;completed_at&quot;: 1777680547,
    &quot;created_at&quot;: 0,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;ee8dcd35-f5a1-9a07-924c-db90a88da556&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {
      &quot;system_fingerprint&quot;: &quot;&quot;
    },
    &quot;model&quot;: &quot;grok-4.20-multi-agent-0309&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;action&quot;: {
          &quot;query&quot;: &quot;xAI news April 2026 OR May 2026&quot;,
          &quot;sources&quot;: [],
          &quot;type&quot;: &quot;search&quot;
        },
        &quot;id&quot;: &quot;ws_ee8dcd35-f5a1-9a07-924c-db90a88da556_0&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;
      },
      {
        &quot;action&quot;: {
          &quot;query&quot;: &quot;xAI Grok latest news this week&quot;,
          &quot;sources&quot;: [],
          &quot;type&quot;: &quot;search&quot;
        },
        &quot;id&quot;: &quot;ws_ee8dcd35-f5a1-9a07-924c-db90a88da556_1&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;
      },
      {
        &quot;action&quot;: {
          &quot;query&quot;: &quot;\&quot;xAI\&quot; (announcement OR launch OR funding OR Grok) after:2026-04-20&quot;,
          &quot;sources&quot;: [],
          &quot;type&quot;: &quot;search&quot;
        },
        &quot;id&quot;: &quot;ws_ee8dcd35-f5a1-9a07-924c-db90a88da556_2&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;
      },
      {
        &quot;id&quot;: &quot;tco_ee8dcd35-f5a1-9a07-924c-db90a88da556&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;id&quot;: &quot;tco_ee8dcd35-f5a1-9a07-924c-db90a88da556&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;id&quot;: &quot;tco_ee8dcd35-f5a1-9a07-924c-db90a88da556&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://x.ai/news&quot;
        },
        &quot;id&quot;: &quot;ws_ee8dcd35-f5a1-9a07-924c-db90a88da556_3&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;
      },
      {
        &quot;action&quot;: {
          &quot;query&quot;: &quot;Elon Musk testifies xAI OpenAI Grok April 2026 OR May 2026&quot;,
          &quot;sources&quot;: [],
          &quot;type&quot;: &quot;search&quot;
        },
        &quot;id&quot;: &quot;ws_ee8dcd35-f5a1-9a07-924c-db90a88da556_4&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;
      },
      {
        &quot;id&quot;: &quot;tco_ee8dcd35-f5a1-9a07-924c-db90a88da556&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;id&quot;: &quot;tco_ee8dcd35-f5a1-9a07-924c-db90a88da556&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [
              {
                &quot;end_index&quot;: 166,
                &quot;start_index&quot;: 66,
                &quot;title&quot;: &quot;1&quot;,
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;url&quot;: &quot;https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/&quot;
              },
              {
                &quot;end_index&quot;: 190,
                &quot;start_index&quot;: 166,
                &quot;title&quot;: &quot;2&quot;,
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;url&quot;: &quot;https://x.ai/news&quot;
              },
              {
                &quot;end_index&quot;: 617,
                &quot;start_index&quot;: 517,
                &quot;title&quot;: &quot;1&quot;,
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;url&quot;: &quot;https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/&quot;
              },
              {
                &quot;end_index&quot;: 728,
                &quot;start_index&quot;: 617,
                &quot;title&quot;: &quot;3&quot;,
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;url&quot;: &quot;https://www.theverge.com/ai-artificial-intelligence/921546/elon-musk-xai-openai-trial-model-distillation&quot;
              },
              {
                &quot;end_index&quot;: 1078,
                &quot;start_index&quot;: 1054,
                &quot;title&quot;: &quot;2&quot;,
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;url&quot;: &quot;https://x.ai/news&quot;
              },
              {
                &quot;end_index&quot;: 1593,
                &quot;start_index&quot;: 1457,
                &quot;title&quot;: &quot;4&quot;,
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;url&quot;: &quot;https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite&quot;
              }
            ],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;**Top xAI news stories this week (late April to early May 2026):**[[1]](https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/)[[2]](https://x.ai/news)\n\n- **Elon Musk testified in his lawsuit against OpenAI**, admitting that xAI had \u201cpartly\u201d used OpenAI models (via distillation techniques) to train Grok. The multi-day testimony framed Musk as an AI safety advocate contrasting with OpenAI\u2019s for-profit shift; it occurred as xAI operates under its recent acquisition by SpaceX.[[1]](https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/)[[3]](https://www.theverge.com/ai-artificial-intelligence/921546/elon-musk-xai-openai-trial-model-distillation)\n\n- **xAI released major voice and audio updates**, including Custom Voices/Voice Library (allowing voice cloning from short recordings), Grok Voice Think Fast 1.0 (a capable voice agent for API use), and Speech-to-Text/Text-to-Speech APIs with natural voices, multilingual support, and simple pricing (announced April 23\u201330).[[2]](https://x.ai/news)\n\n- **Grok 4.3 launched with strong benchmarks and aggressive pricing**, scoring 53 on the Artificial Analysis Intelligence Index (improved agentic/tool-use performance, ~4 points ahead of its predecessor), alongside ~40\u201360% price cuts; this ties into broader product momentum and the post-acquisition context, though some reports noted employee departures and prior coding lags.[[4]](https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite)\n\nThese reflect xAI\u2019s rapid product iteration in voice/agent capabilities and model performance while navigating legal, integration, and operational developments following the SpaceX deal.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_ee8dcd35-f5a1-9a07-924c-db90a88da556&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;,
      &quot;summary&quot;: &quot;detailed&quot;
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: true,
    &quot;temperature&quot;: 0.7,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      }
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [
      {
        &quot;search_context_size&quot;: &quot;medium&quot;,
        &quot;type&quot;: &quot;web_search&quot;
      }
    ],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.95,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;cost_in_usd_ticks&quot;: 2026981500,
      &quot;input_tokens&quot;: 98165,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 43072
      },
      &quot;num_server_side_tools_used&quot;: 21,
      &quot;num_sources_used&quot;: 0,
      &quot;output_tokens&quot;: 8087,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 7740
      },
      &quot;server_side_tool_usage_details&quot;: {
        &quot;code_interpreter_calls&quot;: 0,
        &quot;document_search_calls&quot;: 0,
        &quot;file_search_calls&quot;: 0,
        &quot;mcp_calls&quot;: 0,
        &quot;web_search_calls&quot;: 21,
        &quot;x_search_calls&quot;: 0
      },
      &quot;total_tokens&quot;: 106252
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-multi-agent-0309&#x27;,
  {
    input: &#x27;What were the top news stories about xAI this week? Summarise in three bullets.&#x27;,
    max_turns: 4,
    tools: [{ type: &#x27;web_search&#x27; }],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.20-multi-agent-0309&quot;,
  &quot;input&quot;: &quot;What were the top news stories about xAI this week? Summarise in three bullets.&quot;,
  &quot;max_turns&quot;: 4,
  &quot;tools&quot;: [
    {
      &quot;type&quot;: &quot;web_search&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>With Reasoning</strong>
<p>Asking the agent to think harder before responding</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Solve this step by step: Two trains 900 miles apart travel toward each other at 60 and 80 mph. When do they meet?&quot;,
    &quot;max_output_tokens&quot;: 8192,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The two trains are moving toward each other, so the distance between them closes at a combined rate of 60 + 80 = 140 mph.\n\nTime to meet = total distance / combined speed = 900 / 140.\n\nThis simplifies (by dividing numerator and denominator by 20) to exactly 45/7 hours (or 6 3/7 hours).\n\nTo verify, in that time the first train travels 60 * (45/7) = 2700/7 \u2248 385.71 miles, and the second travels 80 * (45/7) = 3600/7 \u2248 514.29 miles. These add up to exactly 900 miles, confirming they meet after that interval (assuming both start at the same time).\n\n**Final Answer**\n\n45/7 hours&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;completed_at&quot;: 1777679680,
    &quot;created_at&quot;: 0,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;09617b62-0046-cc3e-6d7d-4231238686fb&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 8192,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {
      &quot;system_fingerprint&quot;: &quot;&quot;
    },
    &quot;model&quot;: &quot;grok-4.20-multi-agent-0309&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;The two trains are moving toward each other, so the distance between them closes at a combined rate of 60 + 80 = 140 mph.\n\nTime to meet = total distance / combined speed = 900 / 140.\n\nThis simplifies (by dividing numerator and denominator by 20) to exactly 45/7 hours (or 6 3/7 hours).\n\nTo verify, in that time the first train travels 60 * (45/7) = 2700/7 \u2248 385.71 miles, and the second travels 80 * (45/7) = 3600/7 \u2248 514.29 miles. These add up to exactly 900 miles, confirming they meet after that interval (assuming both start at the same time).\n\n**Final Answer**\n\n45/7 hours&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_09617b62-0046-cc3e-6d7d-4231238686fb&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;,
      &quot;summary&quot;: &quot;detailed&quot;
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: true,
    &quot;temperature&quot;: 0.7,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      }
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.95,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;cost_in_usd_ticks&quot;: 119112500,
      &quot;input_tokens&quot;: 12473,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 9600
      },
      &quot;num_server_side_tools_used&quot;: 0,
      &quot;num_sources_used&quot;: 0,
      &quot;output_tokens&quot;: 2560,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 2384
      },
      &quot;total_tokens&quot;: 15033
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-multi-agent-0309&#x27;,
  {
    input:
      &#x27;Solve this step by step: Two trains 900 miles apart travel toward each other at 60 and 80 mph. When do they meet?&#x27;,
    max_output_tokens: 8192,
    reasoning: { effort: &#x27;medium&#x27; },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.20-multi-agent-0309&quot;,
  &quot;input&quot;: &quot;Solve this step by step: Two trains 900 miles apart travel toward each other at 60 and 80 mph. When do they meet?&quot;,
  &quot;max_output_tokens&quot;: 8192,
  &quot;reasoning&quot;: {
    &quot;effort&quot;: &quot;medium&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>max_output_tokens</code></td><td>integer or null</td><td></td></tr><tr><td><code>max_turns</code></td><td>integer or null</td><td></td></tr><tr><td><code>parallel_tool_calls</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>previous_response_id</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>prompt_cache_key</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string or null</td><td></td></tr><tr><td><code>reasoning.generate_summary</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>reasoning.summary</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>search_parameters</code></td><td>object</td><td></td></tr><tr><td><code>search_parameters.from_date</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>search_parameters.max_search_results</code></td><td>integer or null</td><td></td></tr><tr><td><code>search_parameters.mode</code></td><td>string or null</td><td></td></tr><tr><td><code>search_parameters.return_citations</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>search_parameters.sources</code></td><td>array or null</td><td></td></tr><tr><td><code>search_parameters.to_date</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>store</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>stream</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>temperature</code></td><td>number or null</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>tool_choice</code></td><td>string or object</td><td></td></tr><tr><td><code>tool_choice.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tool_choice.function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tool_choice.function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools</code></td><td>array or null</td><td></td></tr><tr><td><code>top_logprobs</code></td><td>integer or null</td><td></td></tr><tr><td><code>logprobs</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>top_p</code></td><td>number or null</td><td></td></tr><tr><td><code>user</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>context_management</code></td><td>array or null</td><td></td></tr><tr><td><code>include</code></td><td>array or null</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>completed_at</code></td><td>['number', 'null']</td><td></td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>status</code></td><td>string</td><td>Required. Values: in_progress, completed, incomplete, failed</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>parallel_tool_calls</code></td><td>boolean</td><td></td></tr><tr><td><code>previous_response_id</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>reasoning</code></td><td>null</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>top_p</code></td><td>['number', 'null']</td><td></td></tr><tr><td><code>temperature</code></td><td>['number', 'null']</td><td></td></tr><tr><td><code>instructions</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>incomplete_details</code></td><td>null</td><td></td></tr><tr><td><code>metadata</code></td><td>object</td><td></td></tr><tr><td><code>store</code></td><td>boolean</td><td></td></tr><tr><td><code>user</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>error</code></td><td>null</td><td></td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.input_tokens_details</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens_details.cached_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens_details</code></td><td>object</td><td></td></tr><tr><td><code>usage.output_tokens_details.reasoning_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.cost_in_usd_ticks</code></td><td>['number', 'null']</td><td></td></tr><tr><td><code>usage.num_sources_used</code></td><td>number</td><td></td></tr><tr><td><code>usage.num_server_side_tools_used</code></td><td>number</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-4.20-multi-agent-0309/schema-input.json)
- [Output schema](/ai/models/xai/grok-4.20-multi-agent-0309/schema-output.json)

