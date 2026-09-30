<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-5-5-pro">GPT-5.5 pro</h1>

<p><code>openai/gpt-5.5-pro</code></p>

GPT-5.5 pro uses OpenAI's Responses API with built-in tools, improved reasoning, and stateful context management.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 30, Output tokens (per 1M): 180</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic Responses API request with string input

<section class="model-example"><strong>Simple Question</strong>
<p>Basic Responses API request with string input</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;What are the three laws of thermodynamics?&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The **three laws of thermodynamics** are:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed, only transferred or transformed.  \n   In thermodynamics: the change in a system\u2019s internal energy equals heat added to the system minus work done by the system.  \n   \\[\n   \\Delta U = Q - W\n   \\]\n\n2. **Second Law \u2014 Entropy Increases**  \n   In any natural process, the total entropy of an isolated system tends to increase.  \n   Equivalently, heat flows spontaneously from hotter objects to colder ones, and no heat engine can be 100% efficient.\n\n3. **Third Law \u2014 Absolute Zero Limit**  \n   As temperature approaches absolute zero, the entropy of a perfect crystal approaches zero.  \n   It also implies that absolute zero cannot be reached by any finite physical process.\n\nThere is also a **Zeroth Law**, often stated separately: if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This is what makes temperature well-defined.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054314,
    &quot;created_at&quot;: 1777054206,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_063e06a488467aad0169ebb1fc91d4819081d5cf054ee32daa&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.5-pro-2026-04-23&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_063e06a488467aad0169ebb262c1408190aa715f10dd4763dc&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;The **three laws of thermodynamics** are:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed, only transferred or transformed.  \n   In thermodynamics: the change in a system\u2019s internal energy equals heat added to the system minus work done by the system.  \n   \\[\n   \\Delta U = Q - W\n   \\]\n\n2. **Second Law \u2014 Entropy Increases**  \n   In any natural process, the total entropy of an isolated system tends to increase.  \n   Equivalently, heat flows spontaneously from hotter objects to colder ones, and no heat engine can be 100% efficient.\n\n3. **Third Law \u2014 Absolute Zero Limit**  \n   As temperature approaches absolute zero, the entropy of a perfect crystal approaches zero.  \n   It also implies that absolute zero cannot be reached by any finite physical process.\n\nThere is also a **Zeroth Law**, often stated separately: if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This is what makes temperature well-defined.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_063e06a488467aad0169ebb262c45c819093301855572fac7f&quot;,
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;24h&quot;,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;high&quot;,
      &quot;summary&quot;: null
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: false,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      },
      &quot;verbosity&quot;: &quot;medium&quot;
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.98,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 15,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 293,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 66
      },
      &quot;total_tokens&quot;: 308
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5-pro&#x27;,
  { input: &#x27;What are the three laws of thermodynamics?&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5-pro&quot;,
  &quot;input&quot;: &quot;What are the three laws of thermodynamics?&quot;
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With Instructions</strong>
<p>Using instructions to set context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;How do I read a JSON file in Python?&quot;,
    &quot;instructions&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Use Python\u2019s built-in `json` module:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\nIf `data.json` contains:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30\n}\n```\n\nThen `data` will be a Python dictionary:\n\n```python\nprint(data[\&quot;name\&quot;])  # Alice\nprint(data[\&quot;age\&quot;])   # 30\n```\n\nYou can also handle common errors:\n\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n        data = json.load(file)\n\n    print(data)\n\nexcept FileNotFoundError:\n    print(\&quot;The JSON file was not found.\&quot;)\n\nexcept json.JSONDecodeError:\n    print(\&quot;The file is not valid JSON.\&quot;)\n```\n\nUse `json.load(file)` for reading from a file, and `json.loads(string)` for parsing a JSON string.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054286,
    &quot;created_at&quot;: 1777054264,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_0a5627201ea32bd60169ebb23813c081978bb6448d3757ad16&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.5-pro-2026-04-23&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_0a5627201ea32bd60169ebb24e286081979a18901a559d3252&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Use Python\u2019s built-in `json` module:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\nIf `data.json` contains:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30\n}\n```\n\nThen `data` will be a Python dictionary:\n\n```python\nprint(data[\&quot;name\&quot;])  # Alice\nprint(data[\&quot;age\&quot;])   # 30\n```\n\nYou can also handle common errors:\n\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n        data = json.load(file)\n\n    print(data)\n\nexcept FileNotFoundError:\n    print(\&quot;The JSON file was not found.\&quot;)\n\nexcept json.JSONDecodeError:\n    print(\&quot;The file is not valid JSON.\&quot;)\n```\n\nUse `json.load(file)` for reading from a file, and `json.loads(string)` for parsing a JSON string.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_0a5627201ea32bd60169ebb24e2a148197917120444493cfa0&quot;,
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;24h&quot;,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;high&quot;,
      &quot;summary&quot;: null
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: false,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      },
      &quot;verbosity&quot;: &quot;medium&quot;
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.98,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 30,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 387,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 170
      },
      &quot;total_tokens&quot;: 417
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5-pro&#x27;,
  {
    input: &#x27;How do I read a JSON file in Python?&#x27;,
    instructions: &#x27;You are a helpful coding assistant specializing in Python.&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5-pro&quot;,
  &quot;input&quot;: &quot;How do I read a JSON file in Python?&quot;,
  &quot;instructions&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a conversation with message array</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: [
      {
        &quot;content&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;,
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;content&quot;: &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      },
      {
        &quot;content&quot;: &quot;Yes, name three good stops in one short sentence each.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;max_output_tokens&quot;: 16000
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;- Monterey/Carmel is great for beaches, seafood, and a quick scenic stroll.  \n- Big Sur offers dramatic ocean views, Bixby Bridge, and McWay Falls.  \n- Santa Barbara is perfect for lunch, State Street, and Stearns Wharf.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777421264,
    &quot;created_at&quot;: 1777421233,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;id&quot;: &quot;resp_01ed6abc47bd85fc0169f14bb1332481968b1628177ee39463&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 16000,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.5-pro-2026-04-23&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_01ed6abc47bd85fc0169f14bcfd2508196b39551bf06fa05b5&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;- Monterey/Carmel is great for beaches, seafood, and a quick scenic stroll.  \n- Big Sur offers dramatic ocean views, Bixby Bridge, and McWay Falls.  \n- Santa Barbara is perfect for lunch, State Street, and Stearns Wharf.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_01ed6abc47bd85fc0169f14bcfd38c81968fbe4768d5cc9b0f&quot;,
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;24h&quot;,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;high&quot;,
      &quot;summary&quot;: null
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: false,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      },
      &quot;verbosity&quot;: &quot;medium&quot;
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.98,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 78,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 251,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 191
      },
      &quot;total_tokens&quot;: 329
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5-pro&#x27;,
  {
    input: [
      {
        content: &#x27;I need help planning a road trip from San Francisco to Los Angeles.&#x27;,
        role: &#x27;user&#x27;,
      },
      {
        content:
          &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
        role: &#x27;assistant&#x27;,
      },
      { content: &#x27;Yes, name three good stops in one short sentence each.&#x27;, role: &#x27;user&#x27; },
    ],
    max_output_tokens: 16000,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5-pro&quot;,
  &quot;input&quot;: [
    {
      &quot;content&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;,
      &quot;role&quot;: &quot;user&quot;
    },
    {
      &quot;content&quot;: &quot;I&#x27;\&#x27;&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
      &quot;role&quot;: &quot;assistant&quot;
    },
    {
      &quot;content&quot;: &quot;Yes, name three good stops in one short sentence each.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;max_output_tokens&quot;: 16000
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Temperature Control</strong>
<p>Using temperature for creative responses</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Write a haiku about artificial intelligence&quot;,
    &quot;temperature&quot;: 1
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Silent circuits dream  \nLearning patterns in starlight  \nDawn hums through the code&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054304,
    &quot;created_at&quot;: 1777054296,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_0861b6980fc9f4ab0169ebb2585a388196b5ae496c923d5c46&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.5-pro-2026-04-23&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_0861b6980fc9f4ab0169ebb260b08c81968600b365effb3d15&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Silent circuits dream  \nLearning patterns in starlight  \nDawn hums through the code&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_0861b6980fc9f4ab0169ebb260b29c81968b2573cb5b00befc&quot;,
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;24h&quot;,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;high&quot;,
      &quot;summary&quot;: null
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: false,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      },
      &quot;verbosity&quot;: &quot;medium&quot;
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.98,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 13,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 121,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 97
      },
      &quot;total_tokens&quot;: 134
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5-pro&#x27;,
  { input: &#x27;Write a haiku about artificial intelligence&#x27;, temperature: 1 },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5-pro&quot;,
  &quot;input&quot;: &quot;Write a haiku about artificial intelligence&quot;,
  &quot;temperature&quot;: 1
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>With Reasoning</strong>
<p>Using reasoning effort for complex problems</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Solve this problem step by step: A train leaves Chicago at 60mph heading east. Another train leaves New York at 80mph heading west. They are 900 miles apart. When do they meet?&quot;,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Assuming both trains leave at the same time:\n\n1. Train from Chicago speed: **60 mph**\n2. Train from New York speed: **80 mph**\n3. Since they are moving toward each other, add their speeds:\n\n\\[\n60 + 80 = 140 \\text{ mph}\n\\]\n\n4. They are **900 miles** apart, so time is:\n\n\\[\n\\text{time} = \\frac{900}{140}\n\\]\n\n\\[\n\\text{time} = 6.428571\\ldots \\text{ hours}\n\\]\n\n5. Convert the decimal part:\n\n\\[\n0.428571 \\times 60 \\approx 25.7 \\text{ minutes}\n\\]\n\nSo they meet after about:\n\n\\[\n\\boxed{6 \\text{ hours } 26 \\text{ minutes}}\n\\]\n\nMore exactly, they meet after **6 hours, 25 minutes, and 43 seconds**.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054312,
    &quot;created_at&quot;: 1777054305,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_03fc3b8888c0aecf0169ebb2616f408195b4462e87d425924a&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.5-pro-2026-04-23&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_03fc3b8888c0aecf0169ebb2684a4c8195b4fd258c0d92977d&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Assuming both trains leave at the same time:\n\n1. Train from Chicago speed: **60 mph**\n2. Train from New York speed: **80 mph**\n3. Since they are moving toward each other, add their speeds:\n\n\\[\n60 + 80 = 140 \\text{ mph}\n\\]\n\n4. They are **900 miles** apart, so time is:\n\n\\[\n\\text{time} = \\frac{900}{140}\n\\]\n\n\\[\n\\text{time} = 6.428571\\ldots \\text{ hours}\n\\]\n\n5. Convert the decimal part:\n\n\\[\n0.428571 \\times 60 \\approx 25.7 \\text{ minutes}\n\\]\n\nSo they meet after about:\n\n\\[\n\\boxed{6 \\text{ hours } 26 \\text{ minutes}}\n\\]\n\nMore exactly, they meet after **6 hours, 25 minutes, and 43 seconds**.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_03fc3b8888c0aecf0169ebb2684bc0819589f472918a0073f2&quot;,
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;type&quot;: &quot;message&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;24h&quot;,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;,
      &quot;summary&quot;: null
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;store&quot;: false,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      },
      &quot;verbosity&quot;: &quot;medium&quot;
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.98,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 48,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 381,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 182
      },
      &quot;total_tokens&quot;: 429
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.5-pro&#x27;,
  {
    input:
      &#x27;Solve this problem step by step: A train leaves Chicago at 60mph heading east. Another train leaves New York at 80mph heading west. They are 900 miles apart. When do they meet?&#x27;,
    reasoning: { effort: &#x27;medium&#x27; },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.5-pro&quot;,
  &quot;input&quot;: &quot;Solve this problem step by step: A train leaves Chicago at 60mph heading east. Another train leaves New York at 80mph heading west. They are 900 miles apart. When do they meet?&quot;,
  &quot;reasoning&quot;: {
    &quot;effort&quot;: &quot;medium&quot;
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
    &quot;text&quot;: &quot;Assuming **\u201cthis week\u201d = Jun 16\u201322, 2026**:\n\n- **Cloudflare service incident:** Cloudflare reported increased error rates/latency from 13:35 UTC today, affecting Analytics, CDN/Cache and Durable Objects; it later pointed to a fiber cut in Eastern North America and said traffic engineering had mitigated most congestion/packet loss. ([cloudflarestatus.com](https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51))\n- **New anti-bot/privacy protocol:** Cloudflare announced work with Mozilla Firefox, Google Chrome, Microsoft Edge and Shopify on **Private Access Control Tokens (PACT)**, meant to verify legitimate humans/agents without CAPTCHAs or invasive tracking. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/2026/cloudflare-collaborates-with-leading-browsers-to-develop-a-privacy-first-protocol-for-the-global-internet/))\n- **AI + SASE partner push:** Cloudflare launched a **Cloudflare One Design Partner** program and **Cloudflare One Stack**, giving select partners AI-powered workflows to help customers deploy and manage Zero Trust/SASE migrations. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/2026/cloudflare-launches-design-partner-designation-to-accelerate-secure-ai-and-seamless-sase-adoption/))&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0fe61a92ccd82def016a3999c63130819a802271120be10eb8&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1782159814,
    &quot;model&quot;: &quot;gpt-5.5-pro-2026-04-23&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a21cc1c819abf92ab7bc7693b91&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a21d2bc819ab3ca33a96dbae75b&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare news this week June 2026&quot;,
            &quot;Cloudflare latest news June 2026&quot;,
            &quot;site:blog.cloudflare.com Cloudflare June 2026&quot;,
            &quot;Cloudflare stock news June 2026&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare news this week June 2026&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a23240c819abcb66f4e6074d9bb&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a233940819a886fe58c76af4475&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare June 22 2026 outage&quot;,
            &quot;Cloudflare outage June 22 2026&quot;,
            &quot;Cloudflare news June 22 2026&quot;,
            &quot;Cloudflare news June 18 2026&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare June 22 2026 outage&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a26503c819aa08c657db048d931&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a266c3c819a9c2ab66307ca1f26&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://www.cloudflarestatus.com/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a26f1cc819a9e03d45e77d279df&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a2716f4819a9192da4315b2d3d4&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a27525c819a8a61f7405ee19d00&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a276a7c819a99477a5b3d1eeaba&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://www.cloudflare.com/press/press-releases/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a27c9b4819aa415421854c8a235&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a27e6f0819aad66447fbfd41467&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://www.cloudflare.com/press/press-releases/2026/cloudflare-launches-design-partner-designation-to-accelerate-secure-ai-and-seamless-sase-adoption/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a28247c819aa2f43a2401eed9a2&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a2840a4819aa0ce23de6ec658cb&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare PACT privacy-first protocol browsers news June 22 2026&quot;,
            &quot;Cloudflare leading browsers PACT Mozilla Google Microsoft Shopify June 22 2026&quot;,
            &quot;Cloudflare One Stack agent-powered deployment news June 17 2026&quot;,
            &quot;Cloudflare Design Partner Cloudflare One Stack SASE adoption June 17 2026&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare PACT privacy-first protocol browsers news June 22 2026&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a2ec420819a8391167e995a57d9&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a2ef608819a9cbcc945e42d0791&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare June 2026 latest site:theregister.com&quot;,
            &quot;Cloudflare June 2026 latest site:bleepingcomputer.com OR site:thehackernews.com&quot;,
            &quot;Cloudflare June 2026 \&quot;June 22\&quot; \&quot;error rates\&quot;&quot;,
            &quot;Cloudflare June 2026 \&quot;PACT\&quot; \&quot;Private Access Control Tokens\&quot;&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare June 2026 latest site:theregister.com&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a340edc819a95e0c1e4b5614f10&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a349134819ab8bc982a5aa737ad&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare&quot;,
            &quot;Cloudflare news&quot;,
            &quot;Cloudflare outage&quot;,
            &quot;Cloudflare PACT&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a3e086c819aab8c4070f38deb93&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a3e3d44819aa420a1a6e9206955&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;site:blog.cloudflare.com/ 2026/06/17 Cloudflare&quot;,
            &quot;site:blog.cloudflare.com/ 2026/06/18 Cloudflare&quot;,
            &quot;site:blog.cloudflare.com/ 2026/06/19 Cloudflare&quot;,
            &quot;site:blog.cloudflare.com/ 2026/06/22 Cloudflare&quot;
          ],
          &quot;query&quot;: &quot;site:blog.cloudflare.com/ 2026/06/17 Cloudflare&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a416410819a99bdad035902ddd9&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;ws_0fe61a92ccd82def016a399a41a87c819a918ac53a59f75243&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;open_page&quot;,
          &quot;url&quot;: &quot;https://blog.cloudflare.com/cloudflare-one-stack/&quot;
        }
      },
      {
        &quot;id&quot;: &quot;rs_0fe61a92ccd82def016a399a42968c819a9016993c608908de&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;msg_0fe61a92ccd82def016a399a42a7f8819aa00992b84608e5ac&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 414,
                &quot;start_index&quot;: 333,
                &quot;title&quot;: &quot;Cloudflare Status - Increased Error Rates&quot;,
                &quot;url&quot;: &quot;https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51&quot;
              },
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 846,
                &quot;start_index&quot;: 667,
                &quot;title&quot;: &quot;www.cloudflare.com&quot;,
                &quot;url&quot;: &quot;https://www.cloudflare.com/press/press-releases/2026/cloudflare-collaborates-with-leading-browsers-to-develop-a-privacy-first-protocol-for-the-global-internet/&quot;
              },
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 1250,
                &quot;start_index&quot;: 1079,
                &quot;title&quot;: &quot;www.cloudflare.com&quot;,
                &quot;url&quot;: &quot;https://www.cloudflare.com/press/press-releases/2026/cloudflare-launches-design-partner-designation-to-accelerate-secure-ai-and-seamless-sase-adoption/&quot;
              }
            ],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Assuming **\u201cthis week\u201d = Jun 16\u201322, 2026**:\n\n- **Cloudflare service incident:** Cloudflare reported increased error rates/latency from 13:35 UTC today, affecting Analytics, CDN/Cache and Durable Objects; it later pointed to a fiber cut in Eastern North America and said traffic engineering had mitigated most congestion/packet loss. ([cloudflarestatus.com](https://www.cloudflarestatus.com/incidents/v3yl7jqmqj51))\n- **New anti-bot/privacy protocol:** Cloudflare announced work with Mozilla Firefox, Google Chrome, Microsoft Edge and Shopify on **Private Access Control Tokens (PACT)**, meant to verify legitimate humans/agents without CAPTCHAs or invasive tracking. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/2026/cloudflare-collaborates-with-leading-browsers-to-develop-a-privacy-first-protocol-for-the-global-internet/))\n- **AI + SASE partner push:** Cloudflare launched a **Cloudflare One Design Partner** program and **Cloudflare One Stack**, giving select partners AI-powered workflows to help customers deploy and manage Zero Trust/SASE migrations. ([cloudflare.com](https://www.cloudflare.com/press/press-releases/2026/cloudflare-launches-design-partner-designation-to-accelerate-secure-ai-and-seamless-sase-adoption/))&quot;
          }
        ],
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      }
    ],
    &quot;status&quot;: &quot;completed&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 83877,
      &quot;output_tokens&quot;: 2919,
      &quot;total_tokens&quot;: 86796,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 2689
      }
    },
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1782159941,
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
      &quot;effort&quot;: &quot;high&quot;,
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
  &#x27;openai/gpt-5.5-pro&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-5.5-pro&quot;,
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

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-5.5-pro/schema-input.json)
- [Output schema](/ai/models/openai/gpt-5.5-pro/schema-output.json)

