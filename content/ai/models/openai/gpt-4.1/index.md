<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-4-1">GPT-4.1</h1>

<p><code>openai/gpt-4.1</code></p>

OpenAI's flagship GPT model for complex tasks with a million-token context window.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,047,576 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 8, Cached input tokens (per 1M): 0.5</td></tr>
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
    &quot;text&quot;: &quot;Certainly! The **three laws of thermodynamics** are fundamental principles describing how energy moves and changes in physical systems:\n\n---\n\n**1. First Law of Thermodynamics (Law of Energy Conservation):**  \n*Energy cannot be created or destroyed, only converted from one form to another.*\n\n- In other words, the total energy of an isolated system is constant.\n- Mathematically:  \n  \u0394U = Q \u2212 W  \n  Where \u0394U is the change in internal energy, Q is heat added to the system, and W is work done by the system.\n\n---\n\n**2. Second Law of Thermodynamics (Law of Entropy):**  \n*The entropy of an isolated system always increases over time, or remains constant in ideal cases; it never decreases.*\n\n- This law explains why certain processes are irreversible, and why heat flows from hotter to colder bodies naturally.\n- It also means that energy transformations are never 100% efficient; some energy is always dispersed as heat.\n\n---\n\n**3. Third Law of Thermodynamics:**  \n*As temperature approaches absolute zero (0 K), the entropy of a perfect crystal approaches zero.*\n\n- This suggests it is impossible to reach absolute zero in any finite number of steps.\n- At absolute zero, a perfectly ordered crystal would have only one microstate (minimum entropy).\n\n---\n\n**Summary Table:**\n\n| Law        | Main Statement                                             |\n|------------|-----------------------------------------------------------|\n| First      | Energy is conserved                                       |\n| Second     | Entropy increases or remains constant                     |\n| Third      | Entropy approaches zero as temperature approaches 0 K     |&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;Certainly! The **three laws of thermodynamics** are fundamental principles describing how energy moves and changes in physical systems:\n\n---\n\n**1. First Law of Thermodynamics (Law of Energy Conservation):**  \n*Energy cannot be created or destroyed, only converted from one form to another.*\n\n- In other words, the total energy of an isolated system is constant.\n- Mathematically:  \n  \u0394U = Q \u2212 W  \n  Where \u0394U is the change in internal energy, Q is heat added to the system, and W is work done by the system.\n\n---\n\n**2. Second Law of Thermodynamics (Law of Entropy):**  \n*The entropy of an isolated system always increases over time, or remains constant in ideal cases; it never decreases.*\n\n- This law explains why certain processes are irreversible, and why heat flows from hotter to colder bodies naturally.\n- It also means that energy transformations are never 100% efficient; some energy is always dispersed as heat.\n\n---\n\n**3. Third Law of Thermodynamics:**  \n*As temperature approaches absolute zero (0 K), the entropy of a perfect crystal approaches zero.*\n\n- This suggests it is impossible to reach absolute zero in any finite number of steps.\n- At absolute zero, a perfectly ordered crystal would have only one microstate (minimum entropy).\n\n---\n\n**Summary Table:**\n\n| Law        | Main Statement                                             |\n|------------|-----------------------------------------------------------|\n| First      | Energy is conserved                                       |\n| Second     | Entropy increases or remains constant                     |\n| Third      | Entropy approaches zero as temperature approaches 0 K     |&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776470813,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DVnUz3cM4bgGfNijU6O2Bjr5zBIE8&quot;,
    &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_464203d4c6&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 319,
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
      &quot;total_tokens&quot;: 335
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1&#x27;,
  { messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-4.1&quot;,
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
    &quot;text&quot;: &quot;To read a JSON file in Python, you can use the built-in `json` module. Here\u2019s a simple step-by-step example:\n\n### 1. Import the `json` module\n\n```python\nimport json\n```\n\n### 2. Open and read the JSON file\n\nAssuming your JSON file is named `data.json`:\n\n```python\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n```\n\n### 3. Now `data` is a Python object (usually a `dict` or `list`)  \nYou can use `data` just like any other Python dictionary or list.\n\n### Full Example\n\nAssume `data.json` contains:\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;city\&quot;: \&quot;Wonderland\&quot;\n}\n```\n\nPython code:\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\nprint(data[\&quot;name\&quot;])  # Output: Alice\nprint(data[\&quot;age\&quot;])   # Output: 30\n```\n\n---\n\n**Recap:**  \n- Use `import json`.\n- Use `with open(filename) as f: data = json.load(f)`\n- Now, `data` contains your JSON data as Python objects!&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;To read a JSON file in Python, you can use the built-in `json` module. Here\u2019s a simple step-by-step example:\n\n### 1. Import the `json` module\n\n```python\nimport json\n```\n\n### 2. Open and read the JSON file\n\nAssuming your JSON file is named `data.json`:\n\n```python\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n```\n\n### 3. Now `data` is a Python object (usually a `dict` or `list`)  \nYou can use `data` just like any other Python dictionary or list.\n\n### Full Example\n\nAssume `data.json` contains:\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;city\&quot;: \&quot;Wonderland\&quot;\n}\n```\n\nPython code:\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\nprint(data[\&quot;name\&quot;])  # Output: Alice\nprint(data[\&quot;age\&quot;])   # Output: 30\n```\n\n---\n\n**Recap:**  \n- Use `import json`.\n- Use `with open(filename) as f: data = json.load(f)`\n- Now, `data` contains your JSON data as Python objects!&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776470814,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DVnV0JChfu6u4m6dzXKPW2Rb0MofH&quot;,
    &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_7e40a569fc&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 268,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;prompt_tokens&quot;: 31,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 299
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1&quot;,
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
    &quot;text&quot;: &quot;Great! There are two main routes between San Francisco and Los Angeles:\n\n**1. The Scenic Pacific Coast Highway (Highway 1):**  \nThis is the most beautiful (and slower) option, hugging the coastline with stunning ocean views. Key stops along this route include:\n\n- **Half Moon Bay:** Charming coastal town, great for beaches and breakfast.\n- **Santa Cruz:** Fun boardwalk, surf spots, and natural bridges.\n- **Monterey:** Monterey Bay Aquarium, Cannery Row, 17-Mile Drive.\n- **Carmel-by-the-Sea:** Picturesque town, great art galleries, boutiques, and beaches.\n- **Big Sur:** Breathtaking cliffs, Bixby Creek Bridge, McWay Falls, and several state parks for hiking (like Julia Pfeiffer Burns State Park).\n- **Hearst Castle (San Simeon):** Grand historic estate you can tour.\n- **Cambria &amp; Morro Bay:** Cute small towns, Morro Rock, great seafood.\n- **San Luis Obispo:** Lively downtown, Madonna Inn for quirky photos, Mission San Luis Obispo.\n- **Pismo Beach:** Famous for its dunes and clam chowder.\n- **Santa Barbara:** Gorgeous beaches, Spanish architecture, great lunch stop, wine tasting.\n- **Malibu:** Beautiful beaches and coastal views just before you reach LA.\n\n*Tip: This route is best enjoyed over 2-3 days, but you can do portions if you\u2019re on a tighter schedule.*\n\n---\n\n**2. The Fast Inland Route (Highway 101 or I-5):**  \nQuicker, but less scenic. For quick but worthwhile stops:\n\n- **Gilroy:** Garlic capital, outlet shopping.\n- **Paso Robles:** Renowned wineries and adorable downtown.\n- **Santa Barbara:** As above, worth a detour if you take Hwy 101.\n\nIf you\u2019re on **I-5**, main stops are limited\u2014Harris Ranch is a classic spot for a meal (and cattle viewing), but scenery is mostly farmland.\n\n---\n\n**Let me know:**\n- Do you have 1 day or several for the drive?\n- What are your interests (scenery, food, wine, beaches, hiking)?\n- Traveling solo, as a couple, or with family/kids?\n\nWith a bit more info, I can tailor a perfect list for you!&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;Great! There are two main routes between San Francisco and Los Angeles:\n\n**1. The Scenic Pacific Coast Highway (Highway 1):**  \nThis is the most beautiful (and slower) option, hugging the coastline with stunning ocean views. Key stops along this route include:\n\n- **Half Moon Bay:** Charming coastal town, great for beaches and breakfast.\n- **Santa Cruz:** Fun boardwalk, surf spots, and natural bridges.\n- **Monterey:** Monterey Bay Aquarium, Cannery Row, 17-Mile Drive.\n- **Carmel-by-the-Sea:** Picturesque town, great art galleries, boutiques, and beaches.\n- **Big Sur:** Breathtaking cliffs, Bixby Creek Bridge, McWay Falls, and several state parks for hiking (like Julia Pfeiffer Burns State Park).\n- **Hearst Castle (San Simeon):** Grand historic estate you can tour.\n- **Cambria &amp; Morro Bay:** Cute small towns, Morro Rock, great seafood.\n- **San Luis Obispo:** Lively downtown, Madonna Inn for quirky photos, Mission San Luis Obispo.\n- **Pismo Beach:** Famous for its dunes and clam chowder.\n- **Santa Barbara:** Gorgeous beaches, Spanish architecture, great lunch stop, wine tasting.\n- **Malibu:** Beautiful beaches and coastal views just before you reach LA.\n\n*Tip: This route is best enjoyed over 2-3 days, but you can do portions if you\u2019re on a tighter schedule.*\n\n---\n\n**2. The Fast Inland Route (Highway 101 or I-5):**  \nQuicker, but less scenic. For quick but worthwhile stops:\n\n- **Gilroy:** Garlic capital, outlet shopping.\n- **Paso Robles:** Renowned wineries and adorable downtown.\n- **Santa Barbara:** As above, worth a detour if you take Hwy 101.\n\nIf you\u2019re on **I-5**, main stops are limited\u2014Harris Ranch is a classic spot for a meal (and cattle viewing), but scenery is mostly farmland.\n\n---\n\n**Let me know:**\n- Do you have 1 day or several for the drive?\n- What are your interests (scenery, food, wine, beaches, hiking)?\n- Traveling solo, as a couple, or with family/kids?\n\nWith a bit more info, I can tailor a perfect list for you!&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776470817,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DVnV37uMPRNbZz6wc0f1dEO7gTp17&quot;,
    &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_3fcf29cddc&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 481,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;prompt_tokens&quot;: 75,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 556
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1&quot;,
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
    &quot;text&quot;: &quot;Detective Lila Maren knelt beside the wrought-iron fence, her breath misting in the pale dawn light. The alley was quiet, save for the distant hum of the city waking. She scanned the scuffed cobblestones, expecting the usual\u2014a cigarette butt, perhaps, or a scrap of torn fabric. Instead, nestled in a shallow puddle, she found a single red chess pawn, oddly pristine amid the grime.\n\nLila lifted it with gloved fingers, turning it over as she studied its glossy sheen. No markings. No blood. Just a chess piece, out of place and glinting like a secret. She frowned, recalling the message scrawled on the victim\u2019s mirror upstairs: \u201cCheckmate.\u201d The game, it seemed, was just beginning.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;Detective Lila Maren knelt beside the wrought-iron fence, her breath misting in the pale dawn light. The alley was quiet, save for the distant hum of the city waking. She scanned the scuffed cobblestones, expecting the usual\u2014a cigarette butt, perhaps, or a scrap of torn fabric. Instead, nestled in a shallow puddle, she found a single red chess pawn, oddly pristine amid the grime.\n\nLila lifted it with gloved fingers, turning it over as she studied its glossy sheen. No markings. No blood. Just a chess piece, out of place and glinting like a secret. She frowned, recalling the message scrawled on the victim\u2019s mirror upstairs: \u201cCheckmate.\u201d The game, it seemed, was just beginning.&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776470819,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DVnV5b5ltpItctts03EY2jcCCWLEe&quot;,
    &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_7a56a8eabf&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 159,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;prompt_tokens&quot;: 20,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 179
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1&quot;,
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
      &quot;**&quot;,
      &quot;Rec&quot;,
      &quot;ursion&quot;,
      &quot;**&quot;,
      &quot; is&quot;,
      &quot; a&quot;,
      &quot; programming&quot;,
      &quot; technique&quot;,
      &quot; where&quot;,
      &quot; a&quot;,
      &quot; function&quot;,
      &quot; calls&quot;,
      &quot; itself&quot;,
      &quot; to&quot;,
      &quot; solve&quot;,
      &quot; a&quot;,
      &quot; problem&quot;,
      &quot;.&quot;,
      &quot; Each&quot;,
      &quot; time&quot;,
      &quot; the&quot;,
      &quot; function&quot;,
      &quot; calls&quot;,
      &quot; itself&quot;,
      &quot;,&quot;,
      &quot; it&quot;,
      &quot; breaks&quot;,
      &quot; the&quot;,
      &quot; problem&quot;,
      &quot; down&quot;,
      &quot; into&quot;,
      &quot; smaller&quot;,
      &quot; sub&quot;,
      &quot;pro&quot;,
      &quot;blems&quot;,
      &quot;.&quot;,
      &quot; For&quot;,
      &quot; recursion&quot;,
      &quot; to&quot;,
      &quot; stop&quot;,
      &quot;,&quot;,
      &quot; a&quot;,
      &quot; **&quot;,
      &quot;base&quot;,
      &quot; case&quot;,
      &quot;**&quot;,
      &quot; (&quot;,
      &quot;or&quot;,
      &quot; termination&quot;,
      &quot; condition&quot;,
      &quot;)&quot;,
      &quot; is&quot;,
      &quot; required&quot;,
      &quot;.\n\n&quot;,
      &quot;**&quot;,
      &quot;Simple&quot;,
      &quot; Example&quot;,
      &quot;:&quot;,
      &quot; Calcul&quot;,
      &quot;ating&quot;,
      &quot; Factor&quot;,
      &quot;ial&quot;,
      &quot;**\n\n&quot;,
      &quot;The&quot;,
      &quot; **&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;**&quot;,
      &quot; of&quot;,
      &quot; a&quot;,
      &quot; non&quot;,
      &quot;-negative&quot;,
      &quot; integer&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;`&quot;,
      &quot; (&quot;,
      &quot;written&quot;,
      &quot; as&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;!&quot;,
      &quot;`)&quot;,
      &quot; is&quot;,
      &quot; the&quot;,
      &quot; product&quot;,
      &quot; of&quot;,
      &quot; all&quot;,
      &quot; positive&quot;,
      &quot; integers&quot;,
      &quot; less&quot;,
      &quot; than&quot;,
      &quot; or&quot;,
      &quot; equal&quot;,
      &quot; to&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;`.\n\n&quot;,
      &quot;**&quot;,
      &quot;Mat&quot;,
      &quot;hem&quot;,
      &quot;atically&quot;,
      &quot;:&quot;,
      &quot;**\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;!&quot;,
      &quot; =&quot;,
      &quot; n&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;n&quot;,
      &quot;-&quot;,
      &quot;1&quot;,
      &quot;)&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;n&quot;,
      &quot;-&quot;,
      &quot;2&quot;,
      &quot;)&quot;,
      &quot; \u00d7&quot;,
      &quot; ...&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;`\n&quot;,
      &quot;-&quot;,
      &quot; By&quot;,
      &quot; definition&quot;,
      &quot;,&quot;,
      &quot; `&quot;,
      &quot;0&quot;,
      &quot;!&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;`\n\n&quot;,
      &quot;**&quot;,
      &quot;Recursive&quot;,
      &quot; Definition&quot;,
      &quot;:&quot;,
      &quot;**\n&quot;,
      &quot;-&quot;,
      &quot; If&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot; ==&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot;`,&quot;,
      &quot; then&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(n&quot;,
      &quot;)&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;`&quot;,
      &quot;  &quot;,
      &quot; (&quot;,
      &quot;base&quot;,
      &quot; case&quot;,
      &quot;)\n&quot;,
      &quot;-&quot;,
      &quot; If&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot; &gt;&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot;`,&quot;,
      &quot; then&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(n&quot;,
      &quot;)&quot;,
      &quot; =&quot;,
      &quot; n&quot;,
      &quot; \u00d7&quot;,
      &quot; factorial&quot;,
      &quot;(n&quot;,
      &quot;-&quot;,
      &quot;1&quot;,
      &quot;)`&quot;,
      &quot; &quot;,
      &quot; (&quot;,
      &quot;recursive&quot;,
      &quot; case&quot;,
      &quot;)\n\n&quot;,
      &quot;**&quot;,
      &quot;Code&quot;,
      &quot; Example&quot;,
      &quot; in&quot;,
      &quot; Python&quot;,
      &quot;:&quot;,
      &quot;**\n&quot;,
      &quot;```&quot;,
      &quot;python&quot;,
      &quot;\n&quot;,
      &quot;def&quot;,
      &quot; factorial&quot;,
      &quot;(n&quot;,
      &quot;):\n&quot;,
      &quot;   &quot;,
      &quot; if&quot;,
      &quot; n&quot;,
      &quot; ==&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot;:&quot;,
      &quot;        &quot;,
      &quot; #&quot;,
      &quot; Base&quot;,
      &quot; case&quot;,
      &quot;\n&quot;,
      &quot;       &quot;,
      &quot; return&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;\n&quot;,
      &quot;   &quot;,
      &quot; else&quot;,
      &quot;:\n&quot;,
      &quot;       &quot;,
      &quot; return&quot;,
      &quot; n&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(n&quot;,
      &quot; -&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;)&quot;,
      &quot;  &quot;,
      &quot; #&quot;,
      &quot; Recursive&quot;,
      &quot; call&quot;,
      &quot;\n&quot;,
      &quot;``&quot;,
      &quot;`\n\n&quot;,
      &quot;**&quot;,
      &quot;How&quot;,
      &quot; it&quot;,
      &quot; works&quot;,
      &quot;:&quot;,
      &quot;**\n&quot;,
      &quot;To&quot;,
      &quot; compute&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;4&quot;,
      &quot;)`&quot;,
      &quot;:\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;4&quot;,
      &quot;)`&quot;,
      &quot; returns&quot;,
      &quot; `&quot;,
      &quot;4&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)`\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)`&quot;,
      &quot; returns&quot;,
      &quot; `&quot;,
      &quot;3&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)`\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)`&quot;,
      &quot; returns&quot;,
      &quot; `&quot;,
      &quot;2&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)`\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)`&quot;,
      &quot; returns&quot;,
      &quot; `&quot;,
      &quot;1&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;0&quot;,
      &quot;)`\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;0&quot;,
      &quot;)`&quot;,
      &quot; returns&quot;,
      &quot; `&quot;,
      &quot;1&quot;,
      &quot;`&quot;,
      &quot; (&quot;,
      &quot;base&quot;,
      &quot; case&quot;,
      &quot;)\n\n&quot;,
      &quot;So&quot;,
      &quot;,\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)`&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)`&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot;\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)`&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;3&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;6&quot;,
      &quot;\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;4&quot;,
      &quot;)`&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;4&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;6&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;24&quot;,
      &quot;\n\n&quot;,
      &quot;**&quot;,
      &quot;In&quot;,
      &quot; summary&quot;,
      &quot;:**&quot;,
      &quot;  \n&quot;,
      &quot;Rec&quot;,
      &quot;ursion&quot;,
      &quot; is&quot;,
      &quot; when&quot;,
      &quot; a&quot;,
      &quot; function&quot;,
      &quot; calls&quot;,
      &quot; itself&quot;,
      &quot;,&quot;,
      &quot; and&quot;,
      &quot; the&quot;,
      &quot; problem&quot;,
      &quot; gets&quot;,
      &quot; divided&quot;,
      &quot; into&quot;,
      &quot; smaller&quot;,
      &quot; parts&quot;,
      &quot; until&quot;,
      &quot; reaching&quot;,
      &quot; a&quot;,
      &quot; simple&quot;,
      &quot;,&quot;,
      &quot; solv&quot;,
      &quot;able&quot;,
      &quot; case&quot;,
      &quot; (&quot;,
      &quot;the&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot;).&quot;
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
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nqlUcqwR28bhP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;F8I8qrGpbmKbK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Rec&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5Cms1o43rBPM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RfvBqEP7j&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;AQv7Gd5DYc5Re&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;adspjAFjYuY3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6ZmcHKV6xLAQG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; programming&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zji&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; technique&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5xRfs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; where&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PWhDGQUHP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mfR7ISQs4nR9H&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;eBDMR9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;wUV4KhFPx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vh4HWZgN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Iy1a0C1B4cvd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solve&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;qOus54Wy9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5WQk8effKoiUE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2q7r72e&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BBEkc4h45SXYKr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Each&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yjhZypwz0N&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; time&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;IBQEMnwhEN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;TnCHcH3xBF4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;F3Jzjd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;20MP8Q1cB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;8pSk1s0R&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cVe50RdPTo3VFX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;H6Se7tRDeUFu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; breaks&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7If4IFlM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xme2Pq0P2FK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RchXm4m&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KWlZC69plP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; into&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;FSXSS0Cvip&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;JG92npi&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; sub&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ANR6HUogCAs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;pro&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WCAIyahUldsC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;blems&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5DWx2elHud&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BUstAwZaLE12C3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; For&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5upUPUIExdK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;X42oh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pPNyJMTs2ONc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stop&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;u7jNxZfgak&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Dj3LzEcL3owoBH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;AWo8M8QObBOMS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;TDYnblFSwSH5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ULy4anzi8WG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;A4bizECHkS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3grrLtaOb9G0q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1COsNQu6Qz0FP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dwZ4sf0P8YrOW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; termination&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4wm&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; condition&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tvDCA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;rqeyKwZ04cIdZo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0CkOTXOLNLzt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; required&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YQ2nBl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6H0sAcNeEZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PZLYLRXH8hSdp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;V9R1zooZ1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cdFiO3r&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tWXoXKiiqTbqIC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Calcul&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;uSovr8Yw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ating&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OFdCm2nH5F&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ndjwq2N0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;AMll5H6zZimG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bMua3xOa9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ym8qjnILljlY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Sk8C4mqvTd4L&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;C6LEKBwv6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;O1bvJC3rfOwt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YLcdb8COx2QRT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WEY4HLNk3Qkd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;9TiDu0DoxvPY0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; non&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;IlEsuVQ7ELC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-negative&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;HsE8pO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; integer&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yupnj0v&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ieTbecc4wFSjI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xZRM2cv6C7LtYY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zmiiekPAgAn6Xx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OIbAvVAy7HmS4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;written&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;kgcbQ9Gg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; as&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6G4KDF6Tf4rN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xlcbW2kMcbBUF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CvvLc2DMzcSshL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;A8SL1JjBOnUoqn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pJl6kdQrSViVC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pAk51ySzhAAg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KBMB3brqXY7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; product&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;IitkQmg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WfYY4VTtxNlm&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; all&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Crl80acksiq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; positive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EBvau5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; integers&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;80VTBo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; less&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EN6JsNQGl2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; than&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;duHyTwsdky&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;F4NzgsZSm2d9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; equal&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ZiogGwBBb&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5JIEThqtAwel&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;lnyYIwLvfpmZU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;LnqTbCaYYSovEV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2S1AP6Mth&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3qDclRKgnvt35&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Mat&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;JzTFk5T5Y9KR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;hem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;VT1h1MqMBnbq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;atically&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;VYcdCNl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DPfGmPVxNwjAkq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zhWBcPxr3yB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5pmMg4etCG9Xfo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;X8ISiVayT86Q9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XFE0ltRDMJxmOz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;sc0CxJHaxTxLTz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;B9dmjORYZpOnV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;I1uu3Py66ynkI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DElzozSr1GCv8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nsTKm6NO7KSRs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7dq3KkSrmJ2hhM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;G4TrDpbLcl2QiK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5SStWsiJMxrp5b&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;r0nu3IA2MwJhb9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;D1ztlM4KeiQCF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1KPAEoQlUEUFO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;w2AnSQhMPedJrS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dokjpDtY99ILAX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nbbE8SOaHorpcq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;S9f96MGQmwXoxJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;VFK6XVAcc0zED&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ...&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Xjo35JXZw2V&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PqDRTZfJO7u8g&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;val4h3489De4Cj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0xlCCeVYguuPTe&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;8A9jBH8ULP4T&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ApBRghvAjaEsxH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; By&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gmNaT7ejDblF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; definition&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;81aQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;G2bROV5jlK06zt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bbTQkm9dHzfCt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PV4jCs1Di0MJaO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;59U3cUckTK0HGi&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dVPt3EPHSccbL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6XKxI6M82pTaGN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;C0fJhGTyFCikUE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ubaoNSIpL8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ep6Hry2jAlOnr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MFoWvP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Definition&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;jeDG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BCvjFTZ3C6KQ7B&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0RCJhcRio2k&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6FEvHzFbY5gyml&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; If&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hqnFmPp0tYaw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DrSsO0SBRIeq7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zK4dsiWLFsWJLr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ==&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bAPCC4cabryj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;QIOrsZnqc8uX1b&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7d7zqHlLTq5pqH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;TRXV128YV562b&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; then&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;JyfYjBu54L&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KnfuSYZgmdj4u&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nLLMQcYQB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;lF596AzzrOZR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Fu64sZT05V965&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;aQjn0maQx1GEqf&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;f8xdPTYcAUtpO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ih8ijucODJPb5F&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zDJfZrrpcoS9Vt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gNduNvrkWKjyUk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;C5e9xPYAxUk7a&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EYJYCBzF6G9z5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6xDL3ENcJ66&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dGPzwy9Fz3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3OWqh1JRm1HL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;f1dgZUOxEgMlMd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; If&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ChQmMRcyP4UX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tatzvEhehgtvG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4XBq5OSDozfVxt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &gt;&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EQ52PGuprrU7o&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;twT7Rn48pqOlDr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DWpuXSvcs2Dzys&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;heJ7cUSYOCZN2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; then&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;9QpMTKMyUQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zzzNYJ5NIu4YJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;E94Mjp3Vs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yBuBWyZLG6yI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bHmNJmC2hXFk4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;LzMa36oFi7wrza&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Y0aZihRbOnZjp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;f5HLYbngXQ76F&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;K3OwfVfBoU3MK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6M7R0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mkJsOWsLdxrIK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;v5x8aFfuY7E0b2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SXWFksay8ytClQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ThhByjTz2GF7V&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;V417yzlgyJ49FM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Ack0ndddKMFtV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;i2SKZc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xT5yCuV2Kl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;kLmyvZk437&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CC1YahHnRtZqv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Code&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;au9sHRBL8jr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EXmEfIM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; in&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6X7k4Dx3GeLT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;stiiJBXq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;U2ooJYZZWMGm0j&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;x6JlNgPk3r5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;sU1IlPjYzlVg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zS8TNijT9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MYO3OucTsSMSD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;def&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;j6r8F71Iq4l0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0uyP7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;uA7RJxUYwP6Qx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;):\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;22JIVvantbv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7buI85oBjsBf&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; if&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0Pod2k6U45vR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;p2UHSiS0myQnH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ==&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WddV1sJQjyNt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6ThuFkzaWH90LS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;VFgRt53ZxB0sLn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;agg7ICgjSmMK69&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;        &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CcpnZJc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2yhwynJ41Ih5I&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vQ8CL36JEl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;neUuxu59cx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cUxAcuOGFF4YM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ITcz1eFg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; return&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5cAbLhZq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ROKcCUgG473ZwV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;9vI0TWDXPh7eSR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GpJ3GqfyV2ZCE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;v3uluKEisc6j&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; else&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MfDqOPmYAN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6pAelzTSQAPR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pzGrpSN0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; return&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;aU8eNCpz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;acGp4lp1V3PF4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mZxPjtyOoOSta&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pSzH5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hPPWv3oOiBdvg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; -&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XFtqnX8vrv69k&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Koco8SgAyhduN1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;epPhwZkBb60kBA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;h43Cc32AJNXoxz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;o4dDr3lA3b2So&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UN1mYsHhonPWM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;iQRUZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; call&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;E27gmSfEJv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;P5U5RboYiox1Y&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;``&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MEcj3xxNwyK4V&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4cSaqhuFAw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cHHNEsX61vlV9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;How&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Gw7D8e5kVPMa&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ZzTTNvpStbZa&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; works&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;10KBagdJJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;35bgbnQYJzTiw4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dyRplYcRBAC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;To&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;fHHH12Uii0GjA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; compute&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5gihPo3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4wCtazEnYiOsZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WKLtItpE2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2xvepzBNzVqc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;39pl6kOVfaVHRe&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tylvytl8G6Lz4q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;iURtiDzxOV1cI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;iSspfrEO4MlU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;FsBYFxc9HgRfRT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nPlgNwAfjqmkF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;agR8DXiL2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;fNYZ10kL8BMa&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DwFXJN6jTs9lO2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;26Yk8qq7ZO2NVr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;8GiaEwYLuOOpk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; returns&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YBihoMK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;oX5WHxzOLzUOv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tHlBWg9dOda5uW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hPDjWH3awYy2n&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OhcSc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;K5ix5XrlKbOeXd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;qRU3TEbhN7L4ly&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4UHOXepHu71&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7eXhp7XlyBkCDS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SRR1eIkbaS3DF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;njUht3TcJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dtobWJnyYvIQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1PztlmyF3sNvAV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;o1175Ai4duaweW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;uXpRr6ID7PvAC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; returns&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;fe6P5eJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MagtUxKFCdVId&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KT5B3pyMCGvumk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;n8ScFKnx6BHif&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;q2MZy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GW6cabw3xnBpjN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vmAYXfET31qdcZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dmCIXLhCCsP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PsJ3Hsov8q7Fwy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CyFHAj2e0dGQD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0lCbQ1lAy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;9YYZWiVYqyUa&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4YQZYOVKc5Sj0j&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;kM7iDo6fcisQXH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hHCSkvX8Ldf34&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; returns&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;n2Y3vuN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;AqbVRXxUc1T79&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;NAO47XHgZxnEBn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yfR9EkfxakDTq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;E0i8K&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GvjSY2MnHmLpic&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;y2tKxh67Mdwtfu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Co4Vfx3ck6P&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;NI1083dP0gyfN6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OkFM4TFuyH5nR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DkkVICbl2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;uxOomOeqCwrp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;fzPlaAIpAsnhQA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MnBPEbxkhm9Lpr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hUy6idO6hnNNX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; returns&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;LqFOh9K&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;J71q04k0sV1XD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CspyVR5PvkjBmK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5JjrpBZKcwIrL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Y4eHt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WzvPAbZfemw4NT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YJyRPyBVgW3ojR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Y9QjCpYKMBR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tM8CGZqyEvp09d&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;N4tkgIriPqM6D&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;IRWD0lMvR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PkO33yLgzT4S&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;eSJb9p5ROzmjhl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XDFemcs0jfeYdD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;iVLgbYXGLfC67&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; returns&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EjcMaBW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xWQpCQLz4JVLU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;O5iY9ROkm7QoEh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WuEpda9e0V93iA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bmcah9rRIPrOq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;03mBmt1AADo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GUUzDgCSR0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3qb4G5N5IL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;So&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PS6uO5jhS9Zbe&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;g5rltdW6kiBb&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EGFP8uBat3zfqE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;qB2yvTREcnGej&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;oFW6mgvQv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dwo2oqxAVkGZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;8qQjHDqbSp5YgW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zpgSybVTiACF5O&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;rzZy927R7IjJ1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cTGPQIi4QPprr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XC0RsuNublrTcW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;l0ItrXqRLLPMBI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CqNKKeBQKT8wD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OJYyjMKX46bdr4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;H20UgHqLfVyBj2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;rGJ6bFIxWRGvC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PC5tmyTKyu65gW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3Dpz8PdkgMvWq0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RIS7dyo5sNZxA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CkEwQCvER4qcjV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YYsjZv4qYyBUv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2IXiI3qsq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;rYQFqrBS3iTY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1Hf2q2cHj7vrDq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;991ClIryWYVctR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7iBhcbobz6GZ9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YjJq8OEk52cAh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xIvQozjT5BYW25&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Gar8RQQfxvkH6p&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GLnxQJcYxR4cr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;QnjhcUebqL8EWH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yYzh8MAzMy6JVZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;IJudc3lo4uGoH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BRec9VWSN33zCc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vhO1wUQ4xOh36O&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UQ3Tx9virdw3T&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MEvHyVnbIBJfQo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UrN0UTgOWfb0j&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;sRph4TFLC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;58QfQcehfqXO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ZFerhZwCAKj2ya&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;u2JwTxoEW0VBCs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;U0ZuJIVrJST8h&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;QFs77CA9fhTNM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5Rvl6KkBLTu8QT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pDaO6f1cMz8ltt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Wa4mujRgPiedi&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CqgYkPC5CTEhwl&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;a0FEiasW3IHG2A&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bZN3lkfRknQdh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OjqEx8VvbnDmUD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;6&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RbLEN4ATD0NpL8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;57XUlZz4z80L5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6NKdPY9U36XVdL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RQGnWAoXrV7Jm&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OGWk9dGdx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0EGMmucAdc6m&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;evgZArF9Kjmnon&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CUuFPSAy8nkrrB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CeWFHaERgUdnv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;npez5Mw8M4zXy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BzE81uyTpXB78Q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yG3X7RVRm8izCR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;O7whl7Wi6ttHK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gjIuH84Ot692Ta&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;6&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;9LCdZ7NVem5j1D&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;19ShyYcubjAHR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tKplOl4gjPRQ7Q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;24&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1XDjz00plcOKW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ZTeOnfVxdxC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;exeiYKcthso34&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;In&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1KCRWgwxktt6h&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; summary&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pqPzY97&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GRQ5KeQkjeKd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  \n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;oT0AzPYDa92&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Rec&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;L35Q96nmXBbt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nGGgrENHd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;t62Buiq1RDa5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; when&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4pxhEI69Iw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zGJep2pjrgfw1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OCs0X7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cuzDQbgva&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;jisYd3l5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UzluW5tdWR84Ap&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; and&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ujlaX3Sick8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;K1DAPkYstqY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Y6sPHx0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; gets&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;M4QmBHAX8v&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; divided&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DX0iGDR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; into&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;jpyh0ycwac&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;fSiwhmY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; parts&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nx3ZlRroa&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; until&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Fzo3djwkb&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reaching&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vcz1Vm&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Fs8b7DJ9AU3ZS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;n2oThkGB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Byc2BVvn6Ri6Xd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solv&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yT1fSnRJgE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;able&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pOktXLePH3p&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WqkIhLAcqu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KN4wqm4MkF00G&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;sHP5jP0AFGve&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tivsPDq10v&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;A8ACxg7bht&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BJlEVOT35aBO9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {},
          &quot;finish_reason&quot;: &quot;stop&quot;,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ZdkQE6Sfy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [],
      &quot;created&quot;: 1776470822,
      &quot;id&quot;: &quot;chatcmpl-DVnV8rG1ILDUR9r3HsKDVd4dbGH0A&quot;,
      &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;qHFF5gBP2hPp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_51f6d1255b&quot;,
      &quot;usage&quot;: {
        &quot;completion_tokens&quot;: 440,
        &quot;completion_tokens_details&quot;: {
          &quot;accepted_prediction_tokens&quot;: 0,
          &quot;audio_tokens&quot;: 0,
          &quot;reasoning_tokens&quot;: 0,
          &quot;rejected_prediction_tokens&quot;: 0
        },
        &quot;prompt_tokens&quot;: 17,
        &quot;prompt_tokens_details&quot;: {
          &quot;audio_tokens&quot;: 0,
          &quot;cached_tokens&quot;: 0
        },
        &quot;total_tokens&quot;: 457
      }
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1&quot;,
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
    &quot;text&quot;: &quot;Here are the top news stories about Cloudflare this week:\n\n- **Launch of New Partner Initiative for AI and SASE Adoption**: Cloudflare introduced the Cloudflare One Design Partner designation and an AI-powered toolkit to accelerate the adoption of artificial intelligence (AI) and secure access service edge (SASE) architectures. This initiative aims to help organizations modernize legacy security infrastructures and overcome challenges like configuration risks and lengthy deployment times. ([itpro.com](https://www.itpro.com/technology/artificial-intelligence/cloudflare-launches-new-partner-initiative-to-support-ai-and-sase-adoption?utm_source=openai))\n\n- **Completion of Agent Infrastructure Stack with Browser Run Rebuild**: Cloudflare completed its agent infrastructure stack by rebuilding Browser Run on its own Containers platform. This upgrade delivers higher concurrency, faster response times, and support for WebGL and WebMCP, enhancing the performance and scalability of AI agents. ([infoq.com](https://www.infoq.com/news/2026/05/cloudflare-agent-platform-stack/?utm_source=openai))\n\n- **Workforce Reduction Amid AI Adoption**: Cloudflare announced plans to reduce its global workforce by about 20%, cutting more than 1,100 jobs. This restructuring is part of the company&#x27;s shift towards an AI-first operating model, reflecting the rapid adoption of AI tools and the resulting changes in operational processes. ([business-standard.com](https://www.business-standard.com/technology/tech-news/cloudflare-to-cut-about-20-workforce-as-ai-adoption-reshapes-operations-126050800117_1.html?utm_source=openai)) &quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0fdf05943aa0606d016a398f3d52b48198b359c259da57fcf2&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1782157117,
    &quot;model&quot;: &quot;gpt-4.1-2025-04-14&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;ws_0fdf05943aa0606d016a398f3db07c8198a82f9fb39e0ca765&quot;,
        &quot;type&quot;: &quot;web_search_call&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;action&quot;: {
          &quot;type&quot;: &quot;search&quot;,
          &quot;queries&quot;: [
            &quot;Cloudflare top news stories this week&quot;
          ],
          &quot;query&quot;: &quot;Cloudflare top news stories this week&quot;
        }
      },
      {
        &quot;id&quot;: &quot;msg_0fdf05943aa0606d016a398f3f38808198be80ca5b78103aaf&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 658,
                &quot;start_index&quot;: 494,
                &quot;title&quot;: &quot;Cloudflare launches new partner initiative to support AI and SASE adoption&quot;,
                &quot;url&quot;: &quot;https://www.itpro.com/technology/artificial-intelligence/cloudflare-launches-new-partner-initiative-to-support-ai-and-sase-adoption?utm_source=openai&quot;
              },
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 1098,
                &quot;start_index&quot;: 998,
                &quot;title&quot;: &quot;Cloudflare Completes Its Agent Infrastructure Stack with Browser Run Rebuild and Six-Layer Platform - InfoQ&quot;,
                &quot;url&quot;: &quot;https://www.infoq.com/news/2026/05/cloudflare-agent-platform-stack/?utm_source=openai&quot;
              },
              {
                &quot;type&quot;: &quot;url_citation&quot;,
                &quot;end_index&quot;: 1618,
                &quot;start_index&quot;: 1427,
                &quot;title&quot;: &quot;Cloudflare to cut about 20% workforce as AI adoption reshapes operations | Tech News - Business Standard&quot;,
                &quot;url&quot;: &quot;https://www.business-standard.com/technology/tech-news/cloudflare-to-cut-about-20-workforce-as-ai-adoption-reshapes-operations-126050800117_1.html?utm_source=openai&quot;
              }
            ],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Here are the top news stories about Cloudflare this week:\n\n- **Launch of New Partner Initiative for AI and SASE Adoption**: Cloudflare introduced the Cloudflare One Design Partner designation and an AI-powered toolkit to accelerate the adoption of artificial intelligence (AI) and secure access service edge (SASE) architectures. This initiative aims to help organizations modernize legacy security infrastructures and overcome challenges like configuration risks and lengthy deployment times. ([itpro.com](https://www.itpro.com/technology/artificial-intelligence/cloudflare-launches-new-partner-initiative-to-support-ai-and-sase-adoption?utm_source=openai))\n\n- **Completion of Agent Infrastructure Stack with Browser Run Rebuild**: Cloudflare completed its agent infrastructure stack by rebuilding Browser Run on its own Containers platform. This upgrade delivers higher concurrency, faster response times, and support for WebGL and WebMCP, enhancing the performance and scalability of AI agents. ([infoq.com](https://www.infoq.com/news/2026/05/cloudflare-agent-platform-stack/?utm_source=openai))\n\n- **Workforce Reduction Amid AI Adoption**: Cloudflare announced plans to reduce its global workforce by about 20%, cutting more than 1,100 jobs. This restructuring is part of the company&#x27;s shift towards an AI-first operating model, reflecting the rapid adoption of AI tools and the resulting changes in operational processes. ([business-standard.com](https://www.business-standard.com/technology/tech-news/cloudflare-to-cut-about-20-workforce-as-ai-adoption-reshapes-operations-126050800117_1.html?utm_source=openai)) &quot;
          }
        ],
        &quot;role&quot;: &quot;assistant&quot;
      }
    ],
    &quot;status&quot;: &quot;completed&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 320,
      &quot;output_tokens&quot;: 343,
      &quot;total_tokens&quot;: 663,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 0
      }
    },
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1782157123,
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
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
    &quot;reasoning&quot;: {
      &quot;context&quot;: null,
      &quot;effort&quot;: null,
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
    &quot;top_p&quot;: 1,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;user&quot;: null,
    &quot;metadata&quot;: {},
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1&quot;,
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

- [Input schema](/ai/models/openai/gpt-4.1/schema-input.json)
- [Output schema](/ai/models/openai/gpt-4.1/schema-output.json)

