<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-m2-7">MiniMax M2.7</h1>

<p><code>minimax/m2.7</code></p>

MiniMax's M2.7 language model with multilingual capabilities.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>128,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://www.minimaxi.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.3, Output tokens (per 1M): 1.2, Cached input tokens (per 1M): 0.06, Cache creation tokens (per 1M): 0.375</td></tr>
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
    &quot;id&quot;: &quot;066cf8dd69cbfedefa3ee5b16006f2bd&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;The capital of France is **Paris**.&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user asks: \&quot;What is the capital of France?\&quot; This is a straightforward factual question. The answer: Paris. The user likely wants the answer. No policy issues. There&#x27;s no disallowed content. Just answer with \&quot;Paris\&quot;. Should be simple. Possibly also elaborate slightly. But answer is \&quot;Paris\&quot;. Provide answer concisely.&quot;,
          &quot;reasoning_details&quot;: [
            {
              &quot;type&quot;: &quot;reasoning.text&quot;,
              &quot;id&quot;: &quot;reasoning-text-1&quot;,
              &quot;format&quot;: &quot;MiniMax-response-v1&quot;,
              &quot;index&quot;: 0,
              &quot;text&quot;: &quot;The user asks: \&quot;What is the capital of France?\&quot; This is a straightforward factual question. The answer: Paris. The user likely wants the answer. No policy issues. There&#x27;s no disallowed content. Just answer with \&quot;Paris\&quot;. Should be simple. Possibly also elaborate slightly. But answer is \&quot;Paris\&quot;. Provide answer concisely.&quot;
            }
          ]
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336093,
    &quot;model&quot;: &quot;MiniMax-M2.7&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 126,
      &quot;prompt_tokens&quot;: 48,
      &quot;completion_tokens&quot;: 78,
      &quot;total_characters&quot;: 0,
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 70
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
  &#x27;minimax/m2.7&#x27;,
  { max_tokens: 2048, messages: [{ content: &#x27;What is the capital of France?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/m2.7&quot;,
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
    &quot;text&quot;: &quot;# Pasta Aglio e Olio\n\n**Serves 2 | Prep: 5 min | Cook: 15 min**\n\n## Ingredients\n- 200g spaghetti\n- 60ml extra virgin olive oil\n- 4 garlic cloves, thinly sliced\n- 1/2 tsp dried chili flakes\n- Fresh parsley, chopped\n- Salt to taste\n\n## Method\n\n1. **Cook pasta** in well-salted boiling water until al dente. Reserve 120ml pasta water before draining.\n\n2. **Heat olive oil** in a large pan over medium-low heat. Add garlic slices.\n\n3. **Gently cook** garlic for 2-3 minutes until golden (not brown). Add chili flakes.\n\n4. **Add pasta** to the pan with 60ml pasta water. Toss vigorously for 2 minutes, adding more water if needed.\n\n5. **Finish** with parsley and serve immediately.\n\n## Tips\n- Low heat is key\u2014garlic burns quickly\n- Use good quality olive oil\n- The starchy water creates the silky sauce&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;066cf8e09497cc6c53d2b14969cbe3d8&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;# Pasta Aglio e Olio\n\n**Serves 2 | Prep: 5 min | Cook: 15 min**\n\n## Ingredients\n- 200g spaghetti\n- 60ml extra virgin olive oil\n- 4 garlic cloves, thinly sliced\n- 1/2 tsp dried chili flakes\n- Fresh parsley, chopped\n- Salt to taste\n\n## Method\n\n1. **Cook pasta** in well-salted boiling water until al dente. Reserve 120ml pasta water before draining.\n\n2. **Heat olive oil** in a large pan over medium-low heat. Add garlic slices.\n\n3. **Gently cook** garlic for 2-3 minutes until golden (not brown). Add chili flakes.\n\n4. **Add pasta** to the pan with 60ml pasta water. Toss vigorously for 2 minutes, adding more water if needed.\n\n5. **Finish** with parsley and serve immediately.\n\n## Tips\n- Low heat is key\u2014garlic burns quickly\n- Use good quality olive oil\n- The starchy water creates the silky sauce&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user wants a simple pasta aglio e olio recipe. This is a classic Italian dish that&#x27;s quick and uses few ingredients. I should provide concise instructions with metric measurements as requested.&quot;,
          &quot;reasoning_details&quot;: [
            {
              &quot;type&quot;: &quot;reasoning.text&quot;,
              &quot;id&quot;: &quot;reasoning-text-1&quot;,
              &quot;format&quot;: &quot;MiniMax-response-v1&quot;,
              &quot;index&quot;: 0,
              &quot;text&quot;: &quot;The user wants a simple pasta aglio e olio recipe. This is a classic Italian dish that&#x27;s quick and uses few ingredients. I should provide concise instructions with metric measurements as requested.&quot;
            }
          ]
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336096,
    &quot;model&quot;: &quot;MiniMax-M2.7&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 297,
      &quot;prompt_tokens&quot;: 41,
      &quot;completion_tokens&quot;: 256,
      &quot;total_characters&quot;: 0,
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 41
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
  &#x27;minimax/m2.7&#x27;,
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
  &quot;model&quot;: &quot;minimax/m2.7&quot;,
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
    &quot;text&quot;: &quot;UDP is preferred in situations where speed matters more than reliability. Here are common scenarios:\n\n**Real-time applications**\n\n- Video/audio streaming (Zoom, Skype, gaming)\n- VoIP calls where slight packet loss is tolerable\n- Live broadcasts\n\n**Low-latency requirements**\n\n- Online gaming\n- Real-time financial trading\n- Time-sensitive sensor data\n\n**Simple query-response**\n\n- DNS lookups (quick, fire-and-forget)\n- DHCP\n- NTP time synchronization\n\n**Broadcast/Multicast**\n\n- Service discovery (mDNS)\n- IPTV streaming to multiple recipients\n\n**Why not TCP in these cases?**\n\n- TCP&#x27;s retransmission and ordering can cause latency spikes\n- Connection overhead adds delay\n- Unnecessary for data that becomes stale quickly (old video frames)\n\n**Trade-offs to consider**\n\n- Application-level error handling may be needed\n- You must handle packet loss, reordering, and duplicates yourself\n- Some protocols layer reliability on top of UDP (QUIC, DNS over QUIC)\n\nIf you need guaranteed delivery and ordered data with no gaps, TCP remains the safer choice.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;066cf8e412153a383389e1601d684033&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;UDP is preferred in situations where speed matters more than reliability. Here are common scenarios:\n\n**Real-time applications**\n\n- Video/audio streaming (Zoom, Skype, gaming)\n- VoIP calls where slight packet loss is tolerable\n- Live broadcasts\n\n**Low-latency requirements**\n\n- Online gaming\n- Real-time financial trading\n- Time-sensitive sensor data\n\n**Simple query-response**\n\n- DNS lookups (quick, fire-and-forget)\n- DHCP\n- NTP time synchronization\n\n**Broadcast/Multicast**\n\n- Service discovery (mDNS)\n- IPTV streaming to multiple recipients\n\n**Why not TCP in these cases?**\n\n- TCP&#x27;s retransmission and ordering can cause latency spikes\n- Connection overhead adds delay\n- Unnecessary for data that becomes stale quickly (old video frames)\n\n**Trade-offs to consider**\n\n- Application-level error handling may be needed\n- You must handle packet loss, reordering, and duplicates yourself\n- Some protocols layer reliability on top of UDP (QUIC, DNS over QUIC)\n\nIf you need guaranteed delivery and ordered data with no gaps, TCP remains the safer choice.&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user is asking about when to choose UDP over TCP. This is a follow-up question about networking concepts. I should explain the use cases where UDP is preferable, such as real-time applications where slight data loss is acceptable, broadcasting, DNS queries, etc.\n\nLet me provide a clear, helpful answer about scenarios where UDP is the better choice.&quot;,
          &quot;reasoning_details&quot;: [
            {
              &quot;type&quot;: &quot;reasoning.text&quot;,
              &quot;id&quot;: &quot;reasoning-text-1&quot;,
              &quot;format&quot;: &quot;MiniMax-response-v1&quot;,
              &quot;index&quot;: 0,
              &quot;text&quot;: &quot;The user is asking about when to choose UDP over TCP. This is a follow-up question about networking concepts. I should explain the use cases where UDP is preferable, such as real-time applications where slight data loss is acceptable, broadcasting, DNS queries, etc.\n\nLet me provide a clear, helpful answer about scenarios where UDP is the better choice.&quot;
            }
          ]
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336100,
    &quot;model&quot;: &quot;MiniMax-M2.7&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 384,
      &quot;prompt_tokens&quot;: 89,
      &quot;completion_tokens&quot;: 295,
      &quot;total_characters&quot;: 0,
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 73
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
  &#x27;minimax/m2.7&#x27;,
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
  &quot;model&quot;: &quot;minimax/m2.7&quot;,
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
    &quot;text&quot;: &quot;Code flows like water  \nLogic weaves in silent streams  \nBugs fade in sunrise&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;066cf8eba419a621e81c91dd2899b9e6&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;Code flows like water  \nLogic weaves in silent streams  \nBugs fade in sunrise&quot;,
          &quot;name&quot;: &quot;MiniMax AI&quot;,
          &quot;audio_content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user asks: \&quot;Write a haiku about programming.\&quot; We need to respond with a haiku (5-7-5 syllable structure) about programming. No disallowed content. So simply produce a haiku. Perhaps a nice one. Let&#x27;s think.\n\nDefinition: Haiku is a short poem with three lines: first line five syllables, second line seven syllables, third line five syllables. Must convey something about programming. Let&#x27;s craft a haiku.\n\nPossible lines:\n\nLine1: \&quot;Code flows like water\&quot; (Count syllables: Code(1) flows(1) like(1) wa(1) ter(1) -&gt; \&quot;water\&quot; is two syllables: wa-ter = 2, so total = 1+1+1+2 =5) Actually: \&quot;Code flows like water\&quot;: Co-de (2) flows (1) like (1) wa-ter (2) = total 6? Let&#x27;s count: \&quot;Code\&quot; is one syllable? Actually \&quot;code\&quot; is one syllable. So \&quot;Code flows like water\&quot;: Code (1) flows (1) like (1) water (2) = total 5. Wait: Code = 1, flows = 1, like = 1, water = 2 =&gt; total = 5. Yes. So line1 is 5.\n\nLine2: \&quot;Logic weaves in silent streams\&quot; Count: Logic (2) weaves (1) in (1) si-lent (2) streams (1) = total = 2+1+1+2+1=7. Yes, 7.\n\nLine3: \&quot;Bugs fade in sunrise\&quot; Count: Bugs (1) fade (1) in (1) sun-rise (2) = total =5? Actually \&quot;sunrise\&quot; is two syllables: sun-rise. So Bugs (1) fade (1) in (1) sun-rise (2) = 5. Yes.\n\nAlternatively something about \&quot;silicon dreams\&quot; etc.\n\nMake sure we follow haiku structure: 5-7-5 syllables. Let&#x27;s double-check.\n\nHaiku about programming:\n\nLine1: \&quot;Code flows like water\&quot; (5)\nLine2: \&quot;Logic weaves in silent streams\&quot; (7)\nLine3: \&quot;Bugs fade in sunrise\&quot; (5)\n\nAll good.\n\nAlternatively: \&quot;Silent code compiles\&quot; (5? Count: Si-lent (2) code (1) com-piles (2) =5) But it&#x27;s okay.\n\nOk let&#x27;s produce a haiku: maybe:\n\n\&quot;Silicon sighs at night,\nfunctions dance in bright loops,\nbugs dissolve in dawn.\&quot; Let&#x27;s count.\n\nLine1: \&quot;Silicon sighs at night\&quot; Count: Si-li-con (3) sighs (1) at (1) night (1) =6? Actually \&quot;silicon\&quot; is three syllables: Si-li-con. sighs=1, at=1, night=1 =&gt; total = 3+1+1+1=6. Too many.\n\nMaybe \&quot;Silicon sighs at dusk\&quot; Count: Si-li-con (3) sighs (1) at (1) dusk (1) =6.\n\nOk not that.\n\nBetter to go with first attempt.\n\nMaybe \&quot;Infinite loops at night\&quot; Count: In-fi-nite (3) loops (1) at (1) night (1) =6.\n\nThus keep original.\n\nCheck:\n\nLine1: Code flows like water (5)\nLine2: Logic weaves in silent streams (7)\nLine3: Bugs fade in sunrise (5)\n\nBetter ensure second line count: Logic (2) weaves (1) in (1) silent (2) streams (1) =2+1+1+2+1=7.\n\nThird line: Bugs (1) fade (1) in (1) sunrise (2) =5.\n\nThus ok.\n\nOne could also add a title? The user only asked to write a haiku. So just output the haiku.\n\nThus final answer: the haiku.\n\nMake sure not to have any extra commentary beyond the haiku? The user just asked for a haiku. Typically we can output just the poem. Might add a short line like \&quot;Here&#x27;s a haiku:\&quot; but that&#x27;s extra. Safer to just output the poem.\n\nThus final.&quot;,
          &quot;reasoning_details&quot;: [
            {
              &quot;type&quot;: &quot;reasoning.text&quot;,
              &quot;id&quot;: &quot;reasoning-text-1&quot;,
              &quot;format&quot;: &quot;MiniMax-response-v1&quot;,
              &quot;index&quot;: 0,
              &quot;text&quot;: &quot;The user asks: \&quot;Write a haiku about programming.\&quot; We need to respond with a haiku (5-7-5 syllable structure) about programming. No disallowed content. So simply produce a haiku. Perhaps a nice one. Let&#x27;s think.\n\nDefinition: Haiku is a short poem with three lines: first line five syllables, second line seven syllables, third line five syllables. Must convey something about programming. Let&#x27;s craft a haiku.\n\nPossible lines:\n\nLine1: \&quot;Code flows like water\&quot; (Count syllables: Code(1) flows(1) like(1) wa(1) ter(1) -&gt; \&quot;water\&quot; is two syllables: wa-ter = 2, so total = 1+1+1+2 =5) Actually: \&quot;Code flows like water\&quot;: Co-de (2) flows (1) like (1) wa-ter (2) = total 6? Let&#x27;s count: \&quot;Code\&quot; is one syllable? Actually \&quot;code\&quot; is one syllable. So \&quot;Code flows like water\&quot;: Code (1) flows (1) like (1) water (2) = total 5. Wait: Code = 1, flows = 1, like = 1, water = 2 =&gt; total = 5. Yes. So line1 is 5.\n\nLine2: \&quot;Logic weaves in silent streams\&quot; Count: Logic (2) weaves (1) in (1) si-lent (2) streams (1) = total = 2+1+1+2+1=7. Yes, 7.\n\nLine3: \&quot;Bugs fade in sunrise\&quot; Count: Bugs (1) fade (1) in (1) sun-rise (2) = total =5? Actually \&quot;sunrise\&quot; is two syllables: sun-rise. So Bugs (1) fade (1) in (1) sun-rise (2) = 5. Yes.\n\nAlternatively something about \&quot;silicon dreams\&quot; etc.\n\nMake sure we follow haiku structure: 5-7-5 syllables. Let&#x27;s double-check.\n\nHaiku about programming:\n\nLine1: \&quot;Code flows like water\&quot; (5)\nLine2: \&quot;Logic weaves in silent streams\&quot; (7)\nLine3: \&quot;Bugs fade in sunrise\&quot; (5)\n\nAll good.\n\nAlternatively: \&quot;Silent code compiles\&quot; (5? Count: Si-lent (2) code (1) com-piles (2) =5) But it&#x27;s okay.\n\nOk let&#x27;s produce a haiku: maybe:\n\n\&quot;Silicon sighs at night,\nfunctions dance in bright loops,\nbugs dissolve in dawn.\&quot; Let&#x27;s count.\n\nLine1: \&quot;Silicon sighs at night\&quot; Count: Si-li-con (3) sighs (1) at (1) night (1) =6? Actually \&quot;silicon\&quot; is three syllables: Si-li-con. sighs=1, at=1, night=1 =&gt; total = 3+1+1+1=6. Too many.\n\nMaybe \&quot;Silicon sighs at dusk\&quot; Count: Si-li-con (3) sighs (1) at (1) dusk (1) =6.\n\nOk not that.\n\nBetter to go with first attempt.\n\nMaybe \&quot;Infinite loops at night\&quot; Count: In-fi-nite (3) loops (1) at (1) night (1) =6.\n\nThus keep original.\n\nCheck:\n\nLine1: Code flows like water (5)\nLine2: Logic weaves in silent streams (7)\nLine3: Bugs fade in sunrise (5)\n\nBetter ensure second line count: Logic (2) weaves (1) in (1) silent (2) streams (1) =2+1+1+2+1=7.\n\nThird line: Bugs (1) fade (1) in (1) sunrise (2) =5.\n\nThus ok.\n\nOne could also add a title? The user only asked to write a haiku. So just output the haiku.\n\nThus final answer: the haiku.\n\nMake sure not to have any extra commentary beyond the haiku? The user just asked for a haiku. Typically we can output just the poem. Might add a short line like \&quot;Here&#x27;s a haiku:\&quot; but that&#x27;s extra. Safer to just output the poem.\n\nThus final.&quot;
            }
          ]
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;created&quot;: 1780336107,
    &quot;model&quot;: &quot;MiniMax-M2.7&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;total_tokens&quot;: 936,
      &quot;prompt_tokens&quot;: 48,
      &quot;completion_tokens&quot;: 888,
      &quot;total_characters&quot;: 0,
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 872
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
  &#x27;minimax/m2.7&#x27;,
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
  &quot;model&quot;: &quot;minimax/m2.7&quot;,
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

- [Input schema](/ai/models/minimax/m2.7/schema-input.json)
- [Output schema](/ai/models/minimax/m2.7/schema-output.json)

