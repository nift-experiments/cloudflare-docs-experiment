<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-3-1-flash-lite">Gemini 3.1 Flash Lite</h1>

<p><code>google/gemini-3.1-flash-lite</code></p>

Google's lightest and most cost-efficient Gemini model for high-throughput tasks.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input &lt;=200k (per 1M): 0.25, Cached input &lt;=200k (per 1M): 0.03, Output &lt;=200k (per 1M): 1.5, Input &gt;200k (per 1M): 0.25, Cached input &gt;200k (per 1M): 0.03, Output &gt;200k (per 1M): 1.5</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic generateContent request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic generateContent request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The three laws of thermodynamics (along with the \&quot;zeroth\&quot; law, which is foundational) describe how energy moves, transforms, and behaves in physical systems.\n\nHere is a breakdown of the laws:\n\n### 0. The Zeroth Law (The Law of Equilibrium)\nBefore the first three were established, scientists realized there needed to be a rule about temperature.\n*   **The Law:** If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.\n*   **What it means:** This is the scientific basis for the thermometer. It allows us to define \&quot;temperature\&quot; as a measurable property.\n\n---\n\n### 1. The First Law (The Law of Conservation of Energy)\n*   **The Law:** Energy cannot be created or destroyed in an isolated system; it can only be transferred or converted from one form to another.\n*   **What it means:** The total amount of energy in the universe is constant. If you put energy into a system (as heat or work), it must either increase the system&#x27;s internal energy or be released as work. You cannot get more energy out of a system than you put into it (this rules out \&quot;perpetual motion machines of the first kind\&quot;).\n\n---\n\n### 2. The Second Law (The Law of Entropy)\n*   **The Law:** The total entropy (disorder) of an isolated system can never decrease over time; it can only remain constant or increase.\n*   **What it means:** Heat always flows naturally from a hotter object to a colder object, never the other way around unless external work is performed. Because energy spreads out and becomes less \&quot;useful\&quot; (it degrades into heat), no process is 100% efficient. This law provides an \&quot;arrow of time,\&quot; explaining why things break down rather than spontaneously putting themselves back together.\n\n---\n\n### 3. The Third Law (The Law of Absolute Zero)\n*   **The Law:** As the temperature of a system approaches absolute zero (0 Kelvin), the entropy of a perfect crystal approaches zero.\n*   **What it means:** It is impossible to reach absolute zero through any finite number of processes. At absolute zero, all atomic motion stops, and the system reaches its state of minimum possible energy and perfect order.\n\n***\n\n### Summary for easy memory:\n*   **Zeroth Law:** You have to play by the rules (there is such a thing as temperature).\n*   **First Law:** You can&#x27;t win (you can&#x27;t create energy).\n*   **Second Law:** You can&#x27;t break even (you always lose some energy to entropy).\n*   **Third Law:** You can&#x27;t get out of the game (you can&#x27;t reach absolute zero).&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The three laws of thermodynamics (along with the \&quot;zeroth\&quot; law, which is foundational) describe how energy moves, transforms, and behaves in physical systems.\n\nHere is a breakdown of the laws:\n\n### 0. The Zeroth Law (The Law of Equilibrium)\nBefore the first three were established, scientists realized there needed to be a rule about temperature.\n*   **The Law:** If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.\n*   **What it means:** This is the scientific basis for the thermometer. It allows us to define \&quot;temperature\&quot; as a measurable property.\n\n---\n\n### 1. The First Law (The Law of Conservation of Energy)\n*   **The Law:** Energy cannot be created or destroyed in an isolated system; it can only be transferred or converted from one form to another.\n*   **What it means:** The total amount of energy in the universe is constant. If you put energy into a system (as heat or work), it must either increase the system&#x27;s internal energy or be released as work. You cannot get more energy out of a system than you put into it (this rules out \&quot;perpetual motion machines of the first kind\&quot;).\n\n---\n\n### 2. The Second Law (The Law of Entropy)\n*   **The Law:** The total entropy (disorder) of an isolated system can never decrease over time; it can only remain constant or increase.\n*   **What it means:** Heat always flows naturally from a hotter object to a colder object, never the other way around unless external work is performed. Because energy spreads out and becomes less \&quot;useful\&quot; (it degrades into heat), no process is 100% efficient. This law provides an \&quot;arrow of time,\&quot; explaining why things break down rather than spontaneously putting themselves back together.\n\n---\n\n### 3. The Third Law (The Law of Absolute Zero)\n*   **The Law:** As the temperature of a system approaches absolute zero (0 Kelvin), the entropy of a perfect crystal approaches zero.\n*   **What it means:** It is impossible to reach absolute zero through any finite number of processes. At absolute zero, all atomic motion stops, and the system reaches its state of minimum possible energy and perfect order.\n\n***\n\n### Summary for easy memory:\n*   **Zeroth Law:** You have to play by the rules (there is such a thing as temperature).\n*   **First Law:** You can&#x27;t win (you can&#x27;t create energy).\n*   **Second Law:** You can&#x27;t break even (you always lose some energy to entropy).\n*   **Third Law:** You can&#x27;t get out of the game (you can&#x27;t reach absolute zero).&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a19nds/5ZNrEilIoIIOsW4vmEKmo5R0rba/I6ZZTI9ml+6YrCI65LXveEZ/d/f0=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 8,
      &quot;candidatesTokenCount&quot;: 579,
      &quot;totalTokenCount&quot;: 587,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 8
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 579
        }
      ]
    },
    &quot;modelVersion&quot;: &quot;gemini-3.1-flash-lite&quot;,
    &quot;createTime&quot;: &quot;2026-07-21T16:29:03.710695Z&quot;,
    &quot;responseId&quot;: &quot;T55faqewK4Wq8sYPycj20Q0&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-lite&#x27;,
  { contents: [{ parts: [{ text: &#x27;What are the three laws of thermodynamics?&#x27; }], role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-lite&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With System Instruction</strong>
<p>Using a system instruction to set context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;How do I read a JSON file in Python?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0.3
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;To read a JSON file in Python, you use the built-in `json` module.\n\nHere is the standard way to do it:\n\n### The Basic Approach\n```python\nimport json\n\n# Open the file and load the data\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\n# Now &#x27;data&#x27; is a Python dictionary or list\nprint(data)\n```\n\n### Breakdown of the code:\n1.  **`import json`**: Imports Python&#x27;s built-in library for handling JSON.\n2.  **`with open(...)`**: This is a \&quot;context manager.\&quot; It is the best practice because it ensures the file is automatically closed after you are done reading it, even if an error occurs.\n3.  **`json.load(file)`**: This function parses the file content and converts it into the corresponding Python object (e.g., a JSON object becomes a `dict`, and a JSON array becomes a `list`).\n\n---\n\n### Handling Common Scenarios\n\n#### 1. What if the file is empty or malformed?\nIf the file is not valid JSON, `json.load()` will raise a `json.JSONDecodeError`. You can handle this with a `try-except` block:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\nexcept json.JSONDecodeError:\n    print(\&quot;The file contains invalid JSON.\&quot;)\nexcept FileNotFoundError:\n    print(\&quot;The file was not found.\&quot;)\n```\n\n#### 2. Reading a JSON string instead of a file\nIf you have the JSON data as a **string** (not a file), use `json.loads()` (the &#x27;s&#x27; stands for \&quot;string\&quot;):\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n\nprint(data[\&quot;name\&quot;]) # Output: Alice\n```\n\n### Summary: Which one to use?\n*   Use **`json.load(file_object)`** when reading from an actual **file** on your disk.\n*   Use **`json.loads(string)`** when reading from a **string** variable.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;To read a JSON file in Python, you use the built-in `json` module.\n\nHere is the standard way to do it:\n\n### The Basic Approach\n```python\nimport json\n\n# Open the file and load the data\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\n# Now &#x27;data&#x27; is a Python dictionary or list\nprint(data)\n```\n\n### Breakdown of the code:\n1.  **`import json`**: Imports Python&#x27;s built-in library for handling JSON.\n2.  **`with open(...)`**: This is a \&quot;context manager.\&quot; It is the best practice because it ensures the file is automatically closed after you are done reading it, even if an error occurs.\n3.  **`json.load(file)`**: This function parses the file content and converts it into the corresponding Python object (e.g., a JSON object becomes a `dict`, and a JSON array becomes a `list`).\n\n---\n\n### Handling Common Scenarios\n\n#### 1. What if the file is empty or malformed?\nIf the file is not valid JSON, `json.load()` will raise a `json.JSONDecodeError`. You can handle this with a `try-except` block:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\nexcept json.JSONDecodeError:\n    print(\&quot;The file contains invalid JSON.\&quot;)\nexcept FileNotFoundError:\n    print(\&quot;The file was not found.\&quot;)\n```\n\n#### 2. Reading a JSON string instead of a file\nIf you have the JSON data as a **string** (not a file), use `json.loads()` (the &#x27;s&#x27; stands for \&quot;string\&quot;):\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n\nprint(data[\&quot;name\&quot;]) # Output: Alice\n```\n\n### Summary: Which one to use?\n*   Use **`json.load(file_object)`** when reading from an actual **file** on your disk.\n*   Use **`json.loads(string)`** when reading from a **string** variable.&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1/+8Xbo6oiWplrPfjrfXblH509xYguBbs/SHNqslfm3tKk50KPOszVUx9++ro8=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 20,
      &quot;candidatesTokenCount&quot;: 496,
      &quot;totalTokenCount&quot;: 516,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 20
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 496
        }
      ]
    },
    &quot;modelVersion&quot;: &quot;gemini-3.1-flash-lite&quot;,
    &quot;createTime&quot;: &quot;2026-07-21T16:29:06.645326Z&quot;,
    &quot;responseId&quot;: &quot;Up5fas6xJ9jY8sYPgtSd8Ag&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-lite&#x27;,
  {
    contents: [{ parts: [{ text: &#x27;How do I read a JSON file in Python?&#x27; }], role: &#x27;user&#x27; }],
    generationConfig: { temperature: 0.3 },
    systemInstruction: {
      parts: [{ text: &#x27;You are a helpful coding assistant specializing in Python.&#x27; }],
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-lite&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;How do I read a JSON file in Python?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0.3
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
        }
      ]
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a conversation with context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Yes, what are some good places to stop?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 2048
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;To give you the best recommendations, it helps to know which route you plan to take. There are two primary ways to drive from San Francisco to LA:\n\n### 1. The Scenic Route: Highway 1 (Pacific Coast Highway)\nThis is the \&quot;bucket list\&quot; drive. It takes **8\u201310+ hours of pure driving time**, so it\u2019s best done over 2\u20133 days. If you have the time, this is the way to go.\n\n*   **Santa Cruz:** A classic surf town with a vintage boardwalk and amusement park.\n*   **Monterey &amp; Carmel-by-the-Sea:** Visit the famous Monterey Bay Aquarium, then drive the **17-Mile Drive** into the fairytale-like village of Carmel.\n*   **Big Sur:** The crown jewel of the trip. Stop at **Bixby Creek Bridge** for photos and **Pfeiffer Big Sur State Park** for redwoods. \n    *   *Note: Check Caltrans for road closures, as landslides occasionally affect parts of Highway 1.*\n*   **Hearst Castle (San Simeon):** A stunning, opulent estate built by William Randolph Hearst. Be sure to stop at the nearby **Elephant Seal Vista Point** to see hundreds of seals lounging on the beach.\n*   **San Luis Obispo &amp; Pismo Beach:** Great spots for a lunch break. If you like wine, detour slightly inland to the **Paso Robles** wine region.\n*   **Santa Barbara:** Known as the \&quot;American Riviera,\&quot; it has beautiful Spanish architecture, great seafood on the pier, and excellent shopping.\n\n---\n\n### 2. The Efficient Route: I-5\nIf you need to get to LA quickly (5\u20136 hours), you\u2019ll take I-5. It is mostly farmland and not particularly scenic, but there are a few interesting pit stops:\n\n*   **Harris Ranch (Coalinga):** A famous halfway point. It\u2019s a massive cattle ranch and steakhouse. You\u2019ll smell it before you see it, but it\u2019s a quintessential California road trip stop for a burger.\n*   **Tejon Outlets:** Located near the bottom of the Grapevine (the mountain pass into LA), it\u2019s a good place to stretch your legs and do some shopping before hitting the LA traffic.\n*   **Valencia/Magic Mountain:** If you\u2019re a thrill-seeker, Six Flags Magic Mountain is right off the freeway just as you enter the LA area.\n\n---\n\n### A \&quot;Hybrid\&quot; Option (The Best of Both Worlds)\nIf you want some scenery without committing to the full winding coastal road, do this:\n1.  Take **US-101 South** out of San Francisco.\n2.  Stop in **San Luis Obispo**.\n3.  Cut over to the coast to drive through **Santa Barbara** and **Malibu** as you enter Los Angeles. This avoids the slowest parts of the central coast while still giving you that beautiful Pacific ocean view for the final leg of the trip.\n\n**A few tips for your trip:**\n*   **Traffic:** Try to time your arrival into Los Angeles to avoid rush hour (7\u201310 AM or 3\u20137 PM). If you hit the LA freeway system during those times, your trip could easily double in length.\n*   **Direction:** Driving North-to-South (SF to LA) is actually better for the scenic route because you are in the lane closest to the ocean, making it easier to pull over into lookout points.\n\n**Do you have a specific number of days in mind for the trip, or are you looking for a particular vibe (e.g., foodie spots, nature, or shopping)?**&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;To give you the best recommendations, it helps to know which route you plan to take. There are two primary ways to drive from San Francisco to LA:\n\n### 1. The Scenic Route: Highway 1 (Pacific Coast Highway)\nThis is the \&quot;bucket list\&quot; drive. It takes **8\u201310+ hours of pure driving time**, so it\u2019s best done over 2\u20133 days. If you have the time, this is the way to go.\n\n*   **Santa Cruz:** A classic surf town with a vintage boardwalk and amusement park.\n*   **Monterey &amp; Carmel-by-the-Sea:** Visit the famous Monterey Bay Aquarium, then drive the **17-Mile Drive** into the fairytale-like village of Carmel.\n*   **Big Sur:** The crown jewel of the trip. Stop at **Bixby Creek Bridge** for photos and **Pfeiffer Big Sur State Park** for redwoods. \n    *   *Note: Check Caltrans for road closures, as landslides occasionally affect parts of Highway 1.*\n*   **Hearst Castle (San Simeon):** A stunning, opulent estate built by William Randolph Hearst. Be sure to stop at the nearby **Elephant Seal Vista Point** to see hundreds of seals lounging on the beach.\n*   **San Luis Obispo &amp; Pismo Beach:** Great spots for a lunch break. If you like wine, detour slightly inland to the **Paso Robles** wine region.\n*   **Santa Barbara:** Known as the \&quot;American Riviera,\&quot; it has beautiful Spanish architecture, great seafood on the pier, and excellent shopping.\n\n---\n\n### 2. The Efficient Route: I-5\nIf you need to get to LA quickly (5\u20136 hours), you\u2019ll take I-5. It is mostly farmland and not particularly scenic, but there are a few interesting pit stops:\n\n*   **Harris Ranch (Coalinga):** A famous halfway point. It\u2019s a massive cattle ranch and steakhouse. You\u2019ll smell it before you see it, but it\u2019s a quintessential California road trip stop for a burger.\n*   **Tejon Outlets:** Located near the bottom of the Grapevine (the mountain pass into LA), it\u2019s a good place to stretch your legs and do some shopping before hitting the LA traffic.\n*   **Valencia/Magic Mountain:** If you\u2019re a thrill-seeker, Six Flags Magic Mountain is right off the freeway just as you enter the LA area.\n\n---\n\n### A \&quot;Hybrid\&quot; Option (The Best of Both Worlds)\nIf you want some scenery without committing to the full winding coastal road, do this:\n1.  Take **US-101 South** out of San Francisco.\n2.  Stop in **San Luis Obispo**.\n3.  Cut over to the coast to drive through **Santa Barbara** and **Malibu** as you enter Los Angeles. This avoids the slowest parts of the central coast while still giving you that beautiful Pacific ocean view for the final leg of the trip.\n\n**A few tips for your trip:**\n*   **Traffic:** Try to time your arrival into Los Angeles to avoid rush hour (7\u201310 AM or 3\u20137 PM). If you hit the LA freeway system during those times, your trip could easily double in length.\n*   **Direction:** Driving North-to-South (SF to LA) is actually better for the scenic route because you are in the lane closest to the ocean, making it easier to pull over into lookout points.\n\n**Do you have a specific number of days in mind for the trip, or are you looking for a particular vibe (e.g., foodie spots, nature, or shopping)?**&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1+DkEptfX85ePwyRFYqv6jZiAGO5Z7gzH3IQR8a6+hYSOlBbY9Ho3m/LdqNW6M=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 64,
      &quot;candidatesTokenCount&quot;: 778,
      &quot;totalTokenCount&quot;: 842,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 64
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 778
        }
      ]
    },
    &quot;modelVersion&quot;: &quot;gemini-3.1-flash-lite&quot;,
    &quot;createTime&quot;: &quot;2026-07-21T16:29:09.152935Z&quot;,
    &quot;responseId&quot;: &quot;VZ5faueqCc3M8sYPy9OuKQ&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-lite&#x27;,
  {
    contents: [
      {
        parts: [{ text: &#x27;I need help planning a road trip from San Francisco to Los Angeles.&#x27; }],
        role: &#x27;user&#x27;,
      },
      {
        parts: [
          {
            text: &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
          },
        ],
        role: &#x27;model&#x27;,
      },
      { parts: [{ text: &#x27;Yes, what are some good places to stop?&#x27; }], role: &#x27;user&#x27; },
    ],
    generationConfig: { maxOutputTokens: 2048 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-lite&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I&#x27;\&#x27;&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Yes, what are some good places to stop?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 2048
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Creative Writing</strong>
<p>Higher temperature for creative output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 1500,
      &quot;temperature&quot;: 0.8
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The rain hammered against the window of the brownstone, a frantic, rhythmic drumming that did little to drown out the silence of the crime scene. Detective Elias Thorne knelt on the hardwood floor, his knees popping in the quiet room. \n\nThe victim, a reclusive clockmaker, lay sprawled near his workbench, but Thorne\u2019s eyes weren&#x27;t on the body. They were fixed on the center of the Persian rug, where a single, pristine object sat undisturbed by the violence that had clearly unfolded here.\n\nIt was a porcelain teacup, filled to the brim with fine, dry sand. \n\nThorne reached out with a gloved hand, careful not to disturb the delicate china. As he leaned closer, he saw something that made the hair on his neck prickle. Suspended in the center of the sand, perfectly vertical and defying the laws of gravity, was a single, iridescent blue feather. It wasn&#x27;t resting on the surface; it was anchored deep within, as if the sand had been poured around it while it stood upright.\n\nHe clicked his flashlight on, the beam cutting through the gloom. As the light hit the feather, the sand didn&#x27;t just glitter\u2014it began to flow, like a slow-motion whirlpool, spiraling toward the base of the cup without ever spilling over the rim. \n\n\&quot;Well,\&quot; Thorne whispered to the empty room, his breath hitching in his chest. \&quot;That\u2019s not how physics works.\&quot;&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The rain hammered against the window of the brownstone, a frantic, rhythmic drumming that did little to drown out the silence of the crime scene. Detective Elias Thorne knelt on the hardwood floor, his knees popping in the quiet room. \n\nThe victim, a reclusive clockmaker, lay sprawled near his workbench, but Thorne\u2019s eyes weren&#x27;t on the body. They were fixed on the center of the Persian rug, where a single, pristine object sat undisturbed by the violence that had clearly unfolded here.\n\nIt was a porcelain teacup, filled to the brim with fine, dry sand. \n\nThorne reached out with a gloved hand, careful not to disturb the delicate china. As he leaned closer, he saw something that made the hair on his neck prickle. Suspended in the center of the sand, perfectly vertical and defying the laws of gravity, was a single, iridescent blue feather. It wasn&#x27;t resting on the surface; it was anchored deep within, as if the sand had been poured around it while it stood upright.\n\nHe clicked his flashlight on, the beam cutting through the gloom. As the light hit the feather, the sand didn&#x27;t just glitter\u2014it began to flow, like a slow-motion whirlpool, spiraling toward the base of the cup without ever spilling over the rim. \n\n\&quot;Well,\&quot; Thorne whispered to the empty room, his breath hitching in his chest. \&quot;That\u2019s not how physics works.\&quot;&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1/6wTGp3Yq8GtD5KlCLzP3qfjfpyt5QrXvsDKNbS4FR2jBPXckbTU1JKLs3JRY=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 13,
      &quot;candidatesTokenCount&quot;: 300,
      &quot;totalTokenCount&quot;: 313,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 13
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 300
        }
      ]
    },
    &quot;modelVersion&quot;: &quot;gemini-3.1-flash-lite&quot;,
    &quot;createTime&quot;: &quot;2026-07-21T16:29:13.373559Z&quot;,
    &quot;responseId&quot;: &quot;WZ5farfmFuDa8sYPwZ-jsAU&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.1-flash-lite&#x27;,
  {
    contents: [
      {
        parts: [{ text: &#x27;Write a short story opening about a detective finding an unusual clue.&#x27; }],
        role: &#x27;user&#x27;,
      },
    ],
    generationConfig: { maxOutputTokens: 1500, temperature: 0.8 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.1-flash-lite&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 1500,
      &quot;temperature&quot;: 0.8
    }
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>contents</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].role</code></td><td>string</td><td>Values: user, model</td></tr><tr><td><code>contents[].parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>systemInstruction</code></td><td>object</td><td></td></tr><tr><td><code>systemInstruction.parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>systemInstruction.parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>generationConfig</code></td><td>object</td><td></td></tr><tr><td><code>generationConfig.temperature</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topP</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topK</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.maxOutputTokens</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.candidateCount</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.stopSequences</code></td><td>array</td><td></td></tr><tr><td><code>generationConfig.responseMimeType</code></td><td>string</td><td></td></tr><tr><td><code>safetySettings</code></td><td>array</td><td></td></tr><tr><td><code>safetySettings[].category</code></td><td>string</td><td>Required.</td></tr><tr><td><code>safetySettings[].threshold</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>toolConfig</code></td><td>object</td><td></td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>candidates</code></td><td>array</td><td></td></tr><tr><td><code>usageMetadata</code></td><td>object</td><td></td></tr><tr><td><code>usageMetadata.promptTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.candidatesTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.totalTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>modelVersion</code></td><td>string</td><td></td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/gemini-3.1-flash-lite/schema-input.json)
- [Output schema](/ai/models/google/gemini-3.1-flash-lite/schema-output.json)

