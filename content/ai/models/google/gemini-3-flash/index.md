<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-3-flash">Gemini 3 Flash</h1>

<p><code>google/gemini-3-flash</code></p>

Gemini 3 Flash is Google's fast multimodal model with frontier intelligence, superior search, and grounding capabilities.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input &lt;=200k (per 1M): 0.5, Cached input &lt;=200k (per 1M): 0.05, Output &lt;=200k (per 1M): 3, Input &gt;200k (per 1M): 0.5, Cached input &gt;200k (per 1M): 0.05, Output &gt;200k (per 1M): 3</td></tr>
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
    &quot;text&quot;: &quot;While there are technically four laws (starting with the \&quot;Zeroth Law\&quot;), the **Three Laws of Thermodynamics** are the fundamental principles that describe how energy, heat, and matter behave.\n\nHere is a breakdown of the three laws:\n\n---\n\n### 1. The First Law: Conservation of Energy\n**Definition:** Energy cannot be created or destroyed, only transformed from one form to another. The total energy of an isolated system remains constant.\n\n*   **In simple terms:** You can&#x27;t get something for nothing.\n*   **The Equation:** $\\Delta U = Q - W$\n    *   ($\\Delta U$ is the change in internal energy, $Q$ is heat added, and $W$ is work done by the system).\n*   **Example:** In a car engine, the chemical energy of the gasoline is converted into heat and then into mechanical work to move the car.\n\n### 2. The Second Law: Entropy\n**Definition:** The total entropy (disorder) of an isolated system can never decrease over time; it can only remain constant or increase. This law dictates the \&quot;arrow of time.\&quot;\n\n*   **In simple terms:** Things tend to get messy and disorganized over time. Heat always flows spontaneously from a hotter object to a colder object, never the other way around without adding work.\n*   **Key Concept:** This law explains why 100% efficiency is impossible\u2014some energy is always \&quot;lost\&quot; as waste heat.\n*   **Example:** If you place a hot cup of coffee in a cold room, the coffee cools down as heat spreads into the room. The heat will never spontaneously jump back from the room into the coffee to make it boil again.\n\n### 3. The Third Law: Absolute Zero\n**Definition:** As the temperature of a system approaches absolute zero ($0$ Kelvin or $-273.15^\\circ$ Celsius), the entropy of a perfect crystal approaches a constant minimum (usually zero).\n\n*   **In simple terms:** You can\u2019t reach absolute zero.\n*   **Key Concept:** As atoms get colder, they slow down. At absolute zero, all molecular motion would essentially stop. However, because moving heat requires a temperature difference, it is physically impossible to reach a temperature of exactly zero Kelvin in a finite number of steps.\n*   **Example:** Scientists use advanced lasers and magnets to get atoms within billionths of a degree of absolute zero, but they can never quite hit the \&quot;stop\&quot; button entirely.\n\n---\n\n### Summary Mnemonic\nThere is a famous (and slightly cynical) way to remember these laws, often called **\&quot;Ginsberg\u2019s Theorem\&quot;**:\n\n1.  **First Law:** You can&#x27;t win. (You can&#x27;t get more energy out than you put in).\n2.  **Second Law:** You can&#x27;t break even. (You always lose some energy to entropy).\n3.  **Third Law:** You can&#x27;t get out of the game. (You can&#x27;t reach absolute zero to stop the process).\n\n***\n\n**Note on the Zeroth Law:** If you ever hear about a \&quot;Zeroth Law,\&quot; it simply states that if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This is the law that allows us to use thermometers.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;While there are technically four laws (starting with the \&quot;Zeroth Law\&quot;), the **Three Laws of Thermodynamics** are the fundamental principles that describe how energy, heat, and matter behave.\n\nHere is a breakdown of the three laws:\n\n---\n\n### 1. The First Law: Conservation of Energy\n**Definition:** Energy cannot be created or destroyed, only transformed from one form to another. The total energy of an isolated system remains constant.\n\n*   **In simple terms:** You can&#x27;t get something for nothing.\n*   **The Equation:** $\\Delta U = Q - W$\n    *   ($\\Delta U$ is the change in internal energy, $Q$ is heat added, and $W$ is work done by the system).\n*   **Example:** In a car engine, the chemical energy of the gasoline is converted into heat and then into mechanical work to move the car.\n\n### 2. The Second Law: Entropy\n**Definition:** The total entropy (disorder) of an isolated system can never decrease over time; it can only remain constant or increase. This law dictates the \&quot;arrow of time.\&quot;\n\n*   **In simple terms:** Things tend to get messy and disorganized over time. Heat always flows spontaneously from a hotter object to a colder object, never the other way around without adding work.\n*   **Key Concept:** This law explains why 100% efficiency is impossible\u2014some energy is always \&quot;lost\&quot; as waste heat.\n*   **Example:** If you place a hot cup of coffee in a cold room, the coffee cools down as heat spreads into the room. The heat will never spontaneously jump back from the room into the coffee to make it boil again.\n\n### 3. The Third Law: Absolute Zero\n**Definition:** As the temperature of a system approaches absolute zero ($0$ Kelvin or $-273.15^\\circ$ Celsius), the entropy of a perfect crystal approaches a constant minimum (usually zero).\n\n*   **In simple terms:** You can\u2019t reach absolute zero.\n*   **Key Concept:** As atoms get colder, they slow down. At absolute zero, all molecular motion would essentially stop. However, because moving heat requires a temperature difference, it is physically impossible to reach a temperature of exactly zero Kelvin in a finite number of steps.\n*   **Example:** Scientists use advanced lasers and magnets to get atoms within billionths of a degree of absolute zero, but they can never quite hit the \&quot;stop\&quot; button entirely.\n\n---\n\n### Summary Mnemonic\nThere is a famous (and slightly cynical) way to remember these laws, often called **\&quot;Ginsberg\u2019s Theorem\&quot;**:\n\n1.  **First Law:** You can&#x27;t win. (You can&#x27;t get more energy out than you put in).\n2.  **Second Law:** You can&#x27;t break even. (You always lose some energy to entropy).\n3.  **Third Law:** You can&#x27;t get out of the game. (You can&#x27;t reach absolute zero to stop the process).\n\n***\n\n**Note on the Zeroth Law:** If you ever hear about a \&quot;Zeroth Law,\&quot; it simply states that if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This is the law that allows us to use thermometers.&quot;,
              &quot;thoughtSignature&quot;: &quot;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&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 8,
      &quot;candidatesTokenCount&quot;: 697,
      &quot;totalTokenCount&quot;: 1107,
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
          &quot;tokenCount&quot;: 697
        }
      ],
      &quot;thoughtsTokenCount&quot;: 402
    },
    &quot;modelVersion&quot;: &quot;gemini-3-flash-preview&quot;,
    &quot;createTime&quot;: &quot;2026-07-24T21:49:35.132185Z&quot;,
    &quot;responseId&quot;: &quot;791jatmICOSg3dAPo6eioAg&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3-flash&#x27;,
  { contents: [{ parts: [{ text: &#x27;What are the three laws of thermodynamics?&#x27; }], role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3-flash&quot;,
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
    &quot;text&quot;: &quot;To read a JSON file in Python, you use the built-in `json` module.\n\nHere is the most common and recommended way to do it:\n\n### The Standard Method\n```python\nimport json\n\n# Open the file and load the data\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n    data = json.load(file)\n\n# Now &#x27;data&#x27; is a Python dictionary or list\nprint(data)\n```\n\n### Breakdown of the code:\n1.  **`import json`**: Imports Python\u2019s built-in JSON library.\n2.  **`with open(...)`**: This is a \&quot;context manager.\&quot; It ensures the file is properly closed after you are done reading it, even if an error occurs.\n3.  **`&#x27;r&#x27;`**: Opens the file in **read** mode.\n4.  **`encoding=&#x27;utf-8&#x27;`**: This is optional but highly recommended to ensure special characters (like emojis or non-English letters) are handled correctly.\n5.  **`json.load(file)`**: This function takes the file object and converts the JSON data into a Python object (usually a `dict` or a `list`).\n\n---\n\n### `json.load()` vs `json.loads()`\nIt is easy to confuse these two functions:\n*   **`json.load()`** (no &#x27;s&#x27;): Used to read from a **file object**.\n*   **`json.loads()`** (stands for \&quot;load string\&quot;): Used to parse a **string** containing JSON data.\n\n**Example of `json.loads()`:**\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n\nprint(data[\&quot;name\&quot;]) # Output: Alice\n```\n\n---\n\n### Handling Errors\nIf the file doesn&#x27;t exist or the JSON is formatted incorrectly, your program will crash. You can wrap the code in a `try-except` block to handle this gracefully:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\nexcept FileNotFoundError:\n    print(\&quot;The file was not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;The file is not a valid JSON format.\&quot;)\n```\n\n### Pro Tip: Using Pandas (for Data Science)\nIf your JSON file contains a list of records (like a table), the **Pandas** library is often much faster and easier:\n\n```python\nimport pandas as pd\n\ndf = pd.read_json(&#x27;data.json&#x27;)\nprint(df.head())\n```&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;To read a JSON file in Python, you use the built-in `json` module.\n\nHere is the most common and recommended way to do it:\n\n### The Standard Method\n```python\nimport json\n\n# Open the file and load the data\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n    data = json.load(file)\n\n# Now &#x27;data&#x27; is a Python dictionary or list\nprint(data)\n```\n\n### Breakdown of the code:\n1.  **`import json`**: Imports Python\u2019s built-in JSON library.\n2.  **`with open(...)`**: This is a \&quot;context manager.\&quot; It ensures the file is properly closed after you are done reading it, even if an error occurs.\n3.  **`&#x27;r&#x27;`**: Opens the file in **read** mode.\n4.  **`encoding=&#x27;utf-8&#x27;`**: This is optional but highly recommended to ensure special characters (like emojis or non-English letters) are handled correctly.\n5.  **`json.load(file)`**: This function takes the file object and converts the JSON data into a Python object (usually a `dict` or a `list`).\n\n---\n\n### `json.load()` vs `json.loads()`\nIt is easy to confuse these two functions:\n*   **`json.load()`** (no &#x27;s&#x27;): Used to read from a **file object**.\n*   **`json.loads()`** (stands for \&quot;load string\&quot;): Used to parse a **string** containing JSON data.\n\n**Example of `json.loads()`:**\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n\nprint(data[\&quot;name\&quot;]) # Output: Alice\n```\n\n---\n\n### Handling Errors\nIf the file doesn&#x27;t exist or the JSON is formatted incorrectly, your program will crash. You can wrap the code in a `try-except` block to handle this gracefully:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\nexcept FileNotFoundError:\n    print(\&quot;The file was not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;The file is not a valid JSON format.\&quot;)\n```\n\n### Pro Tip: Using Pandas (for Data Science)\nIf your JSON file contains a list of records (like a table), the **Pandas** library is often much faster and easier:\n\n```python\nimport pandas as pd\n\ndf = pd.read_json(&#x27;data.json&#x27;)\nprint(df.head())\n```&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a19gXBYi6TaPLwfAGabkFykrt/VT0/7TNJg4gxnDwsvi+dRCrWduSfukGMbFawR9yTOOOX0pGghcixRX1DIU/Itu9t80Igw3jfw9rKDQS7mB9K+wmeEyqLlL7J5x2mIuhvvjkgFwXGWGlkTWXe4DX+701K79JeiDVgvOVoa0E0aWUXz/4FInnHCc3FhgEpjXnHSsvXS1jVfOgYrfxnJb5FaQ4C4rWI7Y7q+xdH8kD37tiPBc4hLo/4OOR92ufuOY/hPkQfdyGXm9FOg6jSFD5NOnIC/S+6yaDwrj9Ruvgig9Y7wxikcXLfT68sR3x3ekEO+awkk69xbo42AJ7g9WxOKImcUQVZv7mpPLrKRwH5NZnmZTSowsbZ7rnMtbhiiTqbULB2irj9orfaCUpNISpU7eXn37LD5E5mWcI2zkhfLgUAj2H487UTnCUOX7GassWppELpwE5UrRf4SraDKsYyL28tqYThLtX2TB+G5Qku8zPqApKoERXYW376q8tRws/SA3uBLNovZtc3ihERcb5CfptNebVFTZjG3vfPuErVOLk4wpQKyVMcrR7TWH/COhP/Y6oDRl5etAsHHhVZV3M46J71eGFrni61zqlm/6dOl/BMreovZ2lvQVy6Zf8SXMZwXxvOyoUBxltPrFzSpRq+ju6sRHO3JKsE6wFXjWfzjHy/5fISMrLgr7pTUsDG8Y4GlUXiY/WMFw2gldNnMWSjAxKJNl9mJQuKmIQpfYgbfUeKa8eHnXVohl4u0oD9RcRx/1UTpvt57nKL8KfOhTWUyn32gw6Y0jvil+jZfiV6vvI9kSFIfWqXqyuld/3xou8+4Pdg9oxc/enc4EEtOor+0vl0d05+DhnDUPe4o2gt6N8/xpRGdMUYtx2twut6NHPVrZzt6lhqw0Rh/1+LMPgwgkQOaAg86MDcAQOE63DxPaubbWVIvswQX/cCQ1TQT1SVnas1KG3HNQhYZfSrrgXeDp7OYntzKAoaNd1wtry6ZB88NYC9R48AI05bWaduwnTWHJv/n2q64p5KYlOMrnRPsmvNvDhHQfIeGL8k4IVc2v6XqL5mkTwBRxla1d3U/rZGiGF3Pt9SXpZtZKw2WfPxn4T938FrblqrDMy0tNF0Wesao0b0IGyiS75J5RFWtZFXNKZrEyd1/mUkQOhgIQqSuRU9lrMLJEgyKRgjv9nQy/bcpuP1fZhLQBo/BE/e2yuBy7k7MyKZLQTuntqQNrastY6/z9UV/Gv7KIe8L7KNaN1ljVHWHDnBgrlq3xL6VY4Mtgb8zCi372eKRQl/E2EPW/aRngzYj1q0k+G+O58wSebWusR52vpMpdQ7VHSudS14Dvqxap3Fz69CL7UOqEJ4A=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 20,
      &quot;candidatesTokenCount&quot;: 582,
      &quot;totalTokenCount&quot;: 875,
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
          &quot;tokenCount&quot;: 582
        }
      ],
      &quot;thoughtsTokenCount&quot;: 273
    },
    &quot;modelVersion&quot;: &quot;gemini-3-flash-preview&quot;,
    &quot;createTime&quot;: &quot;2026-07-24T21:49:42.962953Z&quot;,
    &quot;responseId&quot;: &quot;9t1jaonjOoGL3dAPnayyuA0&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3-flash&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-3-flash&quot;,
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
    &quot;text&quot;: &quot;The stops you choose will depend entirely on which route you take. Since I mentioned the 5-6 hour timeframe earlier, that usually refers to the **I-5 (Inland)** route, but most people prefer the **Highway 1 (Coastal)** route for a \&quot;road trip\&quot; experience.\n\nHere are the best stops for the three most common routes:\n\n### 1. The Scenic Route: Highway 1 (Pacific Coast Highway)\n*Best for: Incredible views, photo ops, and a multi-day trip.*\n* **Santa Cruz:** Walk the historic Beach Boardwalk or see the Redwood trees at Roaring Camp.\n* **Monterey &amp; Carmel-by-the-Sea:** Visit the world-famous Monterey Bay Aquarium and drive the \&quot;17-Mile Drive\&quot; for views of Pebble Beach.\n* **Big Sur:** Cross the iconic **Bixby Creek Bridge** and stop at **McWay Falls** (a waterfall that drops right onto the beach).\n* **San Simeon:** Tour **Hearst Castle**, the massive estate of William Randolph Hearst, or see the Elephant Seal Rookery at Piedras Blancas.\n* **Solvang:** A charming, \&quot;Little Denmark\&quot; village known for Dutch architecture and bakeries.\n* **Santa Barbara:** Known as the \&quot;American Riviera,\&quot; it has beautiful Spanish architecture and great shopping on State Street.\n\n### 2. The Middle Ground: US-101\n*Best for: A balance of speed and scenery (approx. 6\u20137 hours).*\n* **Paso Robles:** If you like wine, this is one of California\u2019s premier wine regions with beautiful rolling hills.\n* **San Luis Obispo (SLO):** Visit the historic mission, walk through the \&quot;Bubblegum Alley,\&quot; or hike Bishop Peak.\n* **Pismo Beach:** Famous for its wide sandy beaches and \&quot;Clam Chowder\&quot; at Splash Caf\u00e9.\n* **Ventura:** A great spot to see the pier and grab fresh seafood before hitting the LA traffic.\n\n### 3. The Quickest Route: I-5 (The Grapevine)\n*Best for: Getting there as fast as possible (approx. 5\u20136 hours).*\n* **Harris Ranch (Coalinga):** A famous landmark and massive ranch. It&#x27;s the best place for a high-quality steak dinner or a deli sandwich in the middle of the valley.\n* **Bravo Farms (Kettleman City):** A fun, kitschy stop with a petting zoo, ice cream, nuts, and a \&quot;seven-story\&quot; treehouse for kids to climb.\n* **Tejon Ranch Outlets:** Located at the base of \&quot;The Grapevine,\&quot; it\u2019s great for discount designer shopping before the final stretch into LA.\n\n---\n\n### A few \&quot;Pro Tips\&quot; for your drive:\n1.  **Check for Closures:** If you take **Highway 1 (Big Sur)**, check Caltrans before you go. That road is prone to landslides and parts are occasionally closed for repairs.\n2.  **The \&quot;Grapevine\&quot;:** If taking the I-5, you will pass over a high mountain ridge called the Grapevine. In winter, it can occasionally close due to snow; in summer, keep an eye on your engine temperature as it&#x27;s a long, steep climb.\n3.  **LA Traffic:** Try to time your arrival in Los Angeles either before 2:00 PM or after 8:00 PM to avoid the worst of the gridlock.\n\n**Which route sounds more like your style?** I can give you more specific recommendations for food or hotels once you choose!&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The stops you choose will depend entirely on which route you take. Since I mentioned the 5-6 hour timeframe earlier, that usually refers to the **I-5 (Inland)** route, but most people prefer the **Highway 1 (Coastal)** route for a \&quot;road trip\&quot; experience.\n\nHere are the best stops for the three most common routes:\n\n### 1. The Scenic Route: Highway 1 (Pacific Coast Highway)\n*Best for: Incredible views, photo ops, and a multi-day trip.*\n* **Santa Cruz:** Walk the historic Beach Boardwalk or see the Redwood trees at Roaring Camp.\n* **Monterey &amp; Carmel-by-the-Sea:** Visit the world-famous Monterey Bay Aquarium and drive the \&quot;17-Mile Drive\&quot; for views of Pebble Beach.\n* **Big Sur:** Cross the iconic **Bixby Creek Bridge** and stop at **McWay Falls** (a waterfall that drops right onto the beach).\n* **San Simeon:** Tour **Hearst Castle**, the massive estate of William Randolph Hearst, or see the Elephant Seal Rookery at Piedras Blancas.\n* **Solvang:** A charming, \&quot;Little Denmark\&quot; village known for Dutch architecture and bakeries.\n* **Santa Barbara:** Known as the \&quot;American Riviera,\&quot; it has beautiful Spanish architecture and great shopping on State Street.\n\n### 2. The Middle Ground: US-101\n*Best for: A balance of speed and scenery (approx. 6\u20137 hours).*\n* **Paso Robles:** If you like wine, this is one of California\u2019s premier wine regions with beautiful rolling hills.\n* **San Luis Obispo (SLO):** Visit the historic mission, walk through the \&quot;Bubblegum Alley,\&quot; or hike Bishop Peak.\n* **Pismo Beach:** Famous for its wide sandy beaches and \&quot;Clam Chowder\&quot; at Splash Caf\u00e9.\n* **Ventura:** A great spot to see the pier and grab fresh seafood before hitting the LA traffic.\n\n### 3. The Quickest Route: I-5 (The Grapevine)\n*Best for: Getting there as fast as possible (approx. 5\u20136 hours).*\n* **Harris Ranch (Coalinga):** A famous landmark and massive ranch. It&#x27;s the best place for a high-quality steak dinner or a deli sandwich in the middle of the valley.\n* **Bravo Farms (Kettleman City):** A fun, kitschy stop with a petting zoo, ice cream, nuts, and a \&quot;seven-story\&quot; treehouse for kids to climb.\n* **Tejon Ranch Outlets:** Located at the base of \&quot;The Grapevine,\&quot; it\u2019s great for discount designer shopping before the final stretch into LA.\n\n---\n\n### A few \&quot;Pro Tips\&quot; for your drive:\n1.  **Check for Closures:** If you take **Highway 1 (Big Sur)**, check Caltrans before you go. That road is prone to landslides and parts are occasionally closed for repairs.\n2.  **The \&quot;Grapevine\&quot;:** If taking the I-5, you will pass over a high mountain ridge called the Grapevine. In winter, it can occasionally close due to snow; in summer, keep an eye on your engine temperature as it&#x27;s a long, steep climb.\n3.  **LA Traffic:** Try to time your arrival in Los Angeles either before 2:00 PM or after 8:00 PM to avoid the worst of the gridlock.\n\n**Which route sounds more like your style?** I can give you more specific recommendations for food or hotels once you choose!&quot;,
              &quot;thoughtSignature&quot;: &quot;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&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 64,
      &quot;candidatesTokenCount&quot;: 762,
      &quot;totalTokenCount&quot;: 1356,
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
          &quot;tokenCount&quot;: 762
        }
      ],
      &quot;thoughtsTokenCount&quot;: 530
    },
    &quot;modelVersion&quot;: &quot;gemini-3-flash-preview&quot;,
    &quot;createTime&quot;: &quot;2026-07-24T21:49:48.502515Z&quot;,
    &quot;responseId&quot;: &quot;_N1javPVHrSk3dAP45z02AQ&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3-flash&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-3-flash&quot;,
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
      &quot;maxOutputTokens&quot;: 4096,
      &quot;temperature&quot;: 0.8
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The humidity in the room was wrong. That was the first thing Detective Elias Thorne noticed. It wasn\u2019t the metallic tang of blood or the heavy stillness of a man who had stopped breathing three hours ago. It was the smell of a thunderstorm in a room with no open windows.\n\nJulian Vane, a man who had made millions selling security software, sat slumped in his designer leather chair. His throat had been opened with surgical precision, but Thorne\u2019s eyes didn&#x27;t linger on the gore. They were drawn to the mahogany desk, where a small, silver saucer sat perfectly centered.\n\nIn the middle of the saucer was a single, glowing sugar cube.\n\nThorne leaned in, his shadow stretching long across the Persian rug. He didn\u2019t reach for his tweezers yet. The cube wasn&#x27;t just white; it pulsed with a soft, rhythmic violet light, timed exactly to the pace of a resting human heartbeat. \n\n\&quot;Miller,\&quot; Thorne called out without looking back at his partner. \&quot;Tell me the victim had a penchant for bioluminescent snacks.\&quot;\n\n\&quot;He was a hedge fund manager, Elias,\&quot; Miller replied, snapping photos of the entryway. \&quot;The most exotic thing he consumed was unpasteurized goat cheese.\&quot;\n\nThorne pulled a magnifying loupe from his coat pocket. As he peered through the glass, his breath hitched. Inside the crystalline structure of the sugar, frozen like a prehistoric insect in amber, was a microscopic set of brass gears. They were no larger than a grain of dust, and they were turning slowly in reverse.\n\nIt wasn&#x27;t just a clue. It was a piece of machinery that shouldn&#x27;t exist, ticking away inside a condiment. \n\n\&quot;Get the lead-lined evidence bag,\&quot; Thorne whispered, the hair on his arms standing up as the violet pulse of the cube suddenly skipped a beat, matching his own racing heart. \&quot;I don&#x27;t think we&#x27;re looking for a murderer anymore. I think we&#x27;re looking for a clockmaker.\&quot;&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The humidity in the room was wrong. That was the first thing Detective Elias Thorne noticed. It wasn\u2019t the metallic tang of blood or the heavy stillness of a man who had stopped breathing three hours ago. It was the smell of a thunderstorm in a room with no open windows.\n\nJulian Vane, a man who had made millions selling security software, sat slumped in his designer leather chair. His throat had been opened with surgical precision, but Thorne\u2019s eyes didn&#x27;t linger on the gore. They were drawn to the mahogany desk, where a small, silver saucer sat perfectly centered.\n\nIn the middle of the saucer was a single, glowing sugar cube.\n\nThorne leaned in, his shadow stretching long across the Persian rug. He didn\u2019t reach for his tweezers yet. The cube wasn&#x27;t just white; it pulsed with a soft, rhythmic violet light, timed exactly to the pace of a resting human heartbeat. \n\n\&quot;Miller,\&quot; Thorne called out without looking back at his partner. \&quot;Tell me the victim had a penchant for bioluminescent snacks.\&quot;\n\n\&quot;He was a hedge fund manager, Elias,\&quot; Miller replied, snapping photos of the entryway. \&quot;The most exotic thing he consumed was unpasteurized goat cheese.\&quot;\n\nThorne pulled a magnifying loupe from his coat pocket. As he peered through the glass, his breath hitched. Inside the crystalline structure of the sugar, frozen like a prehistoric insect in amber, was a microscopic set of brass gears. They were no larger than a grain of dust, and they were turning slowly in reverse.\n\nIt wasn&#x27;t just a clue. It was a piece of machinery that shouldn&#x27;t exist, ticking away inside a condiment. \n\n\&quot;Get the lead-lined evidence bag,\&quot; Thorne whispered, the hair on his arms standing up as the violet pulse of the cube suddenly skipped a beat, matching his own racing heart. \&quot;I don&#x27;t think we&#x27;re looking for a murderer anymore. I think we&#x27;re looking for a clockmaker.\&quot;&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a18uipJRkTss/UkZqyfwi6x82MixOXaO/uk3eCy64EV7aK4ttUgHP/GuCy87VIrRh2pBSFfaCIIgvg2Z0XXmG5k/oDbEIPlNbZjr7vrmMXRAeRatL+26MGjPoTkScvjCzzPACLHFVI4yuFtPLJgA6wKc+VnbldWtibzoIYW8pnja28iaIsV45zyQdP4OVlcG2zM79rLT5gdijGgyvXax6o4ddAYrkbmbguVQaigAYAoZscjdnDbsof72g7TspNIz2Cg84eCBk1OEJ9yJNsbzyMWDOlvXYFHnt+ZdQ2e+NMP+EvoxLfzyafvufBe8PoFy1nQezOtLUHjh8kzsvS3MbBfjylLF+REUMCKryJ9TbSmR2kvGvKZO+SAiImB9qfnFDw7IlqFBVRug8Xwa/FWZVZ5/Xj0ZPik+jpkA6ZP2jIcAp65natEzK3+EQDNeZVcVWomI5E2KCEgk5NeT6FqSsW326YpMnJQ+H6zCMzZgNZ/mVutbkiuXmdNVevVhT7I7UG0rbvARhvqsVZ5cRVktoY0vHAgjeqR1H46TiL3Km6QE2Dv21VA0udMMvLwZJVKLFppJc2leyUXi9NY34iKXWwWVllE4MrdULFUAnY/lrcpnCUGGWobryA8Tv7VvFPjGU/vqLdM88M2+9E91xyfR5Ud9tq47ZjDAqNFPhMIk6ZbzHbzXWgZWfF0qDRTBe711nl63mW6YaB2D7ORB9P5nb0YeIj1J9drnZeE/MqPuVLR5UZZ0nv76Nj36EIAsDjjYG2SWEjGpWD9rYhQP5OsyqwasD7Ug7/I7hFEWNs+qUMk82tOlH+nwGX+y/fNdkvUIY6cqn/tyVQXOpxJlSC77qPncwh/yMWZVNnWC0W6YxRwhM0XkcUsVNgAq5W1ogsLuo8q3R4DHp6sY+3D2DsUDzAw5OJKT0j7DjQ/ewJbhzN48boclWAWXGEGaiLukT+RkwEEL0lJLT1wyIbYfwHbjHgR2x6mh8n+zmzmXpnc030mLgj0WGn7ad2zrVBYH9s2evp0iFofgVHlIpvP1f3oLmn9WdC4gsJSFD38qqVHz7a/yfRl5enlJneD0gIGBgh7+KM7GL6zL317ouFxl09YZlApIK8r4s//Mz4MWIgDvM7jBAemSHoKpGwf9KdzWfXcoiWISUKOSWgUwybhIP1KHAwiBdr+1pbRKKzLa+VWa3z1EqtQ0Tf7a3LSAau2wy6g62M5hbtKEG10JEPqON13wihmzy4szC2pRTBIw67hhqT6pjYBDDGjDiGAZVucs+mo+gkC57ZSooNkXrIGMmoWfmYyD/efE4RbcPaO8Fb/TmkJex4rRd3+/6NmhhEuD1Q5U4nrTo9+pvkE5rC85ghMr+ZmT05xJsC1U2JZIHD4gPA6Lmx0QXg90emB7HwLoqadr99xtm8ZNaWjkzXKfZzJeCvtdwmX7kUTuzTRO/QNogqZbw0pJgAqGg0+raZumw9Cf3pXQARmoRW+UycAhO53d3jCjR3ofTdAsHmcuENGcP3Aa3m0rjvrSR4ZwvJ3DMc4F1wkdHnEfidYAYywq/L8CXJLPRW6mij21cbIpOICww4h0hWSeFSdqgUjKbDWMvF+eXj6XqW2OTeGxdgRaNneCrpCJzhCWZznL1GYQfTXGuWE/MuA6eTofdcBXbpPK9wtCDaEvglAMydRDtqXgloE+ETx3b2VbBwoFjn1tvx00DmuHlq+JwzMj0WtLk8JjNe87pOj9nRh1tp7SYWIrJCy5KjuygdK7bqZazwn7UeHlRcHPSzbfJvKALpNRFSXtq/+aDHTWlxFcLU/BLGVIWmQyVRfs4Xvmyjw8n0L0i6olwymAuSbvs0QkDpGH16kQ0eXnXm+jdtl/eQtVNagF2pc8DtS0AvvXKUHxFwGZvofxTeNIMR2SLxJPE53669keIKkA5aXSIk1XG/53mt13WhI1Z70Nq5EwrkQQwBXMc46/zB0HdfIG6hxcLiw++WSE7JvgucoEYt7rUYzKpoHyAXtME+bVTSVABXI9gxQcKB7fc3O0v76XOEr5UBVPJk6YTInmbD8AJrTmsoEI67yhIaPPKHMS7i2CJKjzQXPXuLUd2SURi/pAf95TIZiBB2jk3ziE3We1N7oIfeWKgaJk1aR76u3Jtm/qmtXK6ihoUdhhIoUlz+Fz0nm+P8guqsNtt1vqAS4dR1xJbrU5gPkXh4uMuC/O1hbed7cr48nts0WoxJz+dOQ0JUcic1g40zucicF8Wtrb9d1a3MCtLHgcAVwUY7HwsRY5YyddNeOalfTnAtvnaETfMKyX34CE6rwWLvMH4UhfuXELOK17R7eWC3zGZEblW5Tw2Ay4TOCKshPprc78Ss/+1bPC2S0sOyuEv70eoPcO11nJC6ThFzOf6SzrFZ8LbP0il6h7G1/+KseRqR+QjX+OONsxZhd/ZE0vQMl0mTMx2aWoBN/yqJmI6W2MIfMRVqmWR+xL+kibfu8j7zvWWN6hDkP+aYGEfmd18BBKnIfQLH/WM3L6zaCe/+En1aA57ssqupxk/Og1SMbWube/IKOJ3EFqAo25Uofw2sK3P2WRCUwFkXWoMSKzDvUHVW9dSH6hgOb4n/vwEewAOdtuxLcL8xO9uUsVee7VDaLE9lqw+rYOavCDTxICJPWKf9ndUW6YQBchhiQ0KAS+C10FyPVKiNsV9iFaGv1QYPGhKvuQxr2+vYisLNv1nctMkPpEzHC/7yDrxCGgHB3acAb+eS7QzKbh0U26ou46Bqbyoj38Ht6mTAlT6bb8JO1vP4+qfy+a+bvJ8kPMSNzjxobN7lNw+rzMK7xaLKW+hr4pZnPPAeuf9fRyOtvqn5sd4NUc/WilloSwFXkvylDz3eX/j1M8OZQkKEr6hPawHBhftonhWu/j0xoMZ/OcDf2Kut3+/l0rmk5gc2M8x1yrnCuOrJL9Z1fvFU0ftefJD7e3lPS95uTgBx0o2RpsOExCoVFABogSzTrMJ6uLnu98PT28XiipCaojsAk34idQWOiQTEfFUrSIkX0lH9EP1auHexa+EUMTLJfGj4B24OJZqzn6827TcfiGqDcQQrv6iElNOsbCac1FI7Wv6ChrlBYHXhBQqqruxH2KDfaDekHSbsJyXq1rEKSvqow363/hUznI03ftV3bXH73w2rRZoxl+3jSTRYm0bhMMVkkk/iH9Kz5RSdRJlLPMZFYHAibSlIJ2QxM8Z/vZwgUy7MqUQfa0mQjhGOXZJiPCOYwYsKPJYzBF8SFt/sybVIQEtHLGvFFokm6921EQuLTp+OpASHLQjZml2gY9ZNhK2HGICYykdRQOiLT3M79V4UaRFo1tjRQBCiAO/dJ24EP2Dmjw3rI66SLX6s+jHAs5rC3rzhDKQ3rreRvnglvG1R1BseenbfB9q8wq/ckLZ9laeEfBcWsLOfio/vr9wIFpDSlHWzGgE7z1hh6m2GhzqBJBTicgqWioAoNSTgTWGgI7SJ+ZVjW+lSRWszassATLb/LFljPc5OLl+hsMWNPTjk2YtbloJ4ueImJP8pmQE774NppcuDG8Uy8RzALjq8eOVsCREqaHQA8hQXgyCFqZ1hDdzfhcCfQv6u6z522CNTtuKVuv/qN3819C5QU9v4D1LBH/ZEcAC584eEWmLkfH9EMoL4Or6Q2ZY6cC692dMReaBFJz3bu1mzC/DImbgE8dzZqfyhTHsHBLVnk39b7mMZc0HkQh+J9Y+LxemXPcIjRXJcpXjgbpcD7TkJBgcwawE9rI57nrtufVWsjyyGxz5r4MBBy2NcvssAPsgUN1n2fGam+DhmDmdc6KLTaeE0K+1CEeDaXQN7pInGeurIY85WzB35oO94zAS6u10ZKluhedOAlDZCMTZ/CknJ5Mm4SNZJ6MoBrMy2DYymZjzUI3D3AeUbZjLUpEfaqplhMwP9gzoUpTuisQuRDkcLhm56q5tL9GyFROSUc9GV9bgXN66CbIr9vkz7fa+fu5YhCzyFsoFcboXgv2vKxTPRdVd4L+T4zzo7ujbbMV5hDprsZviND9ncmeiAWL8fh1PpRWy5g4Z229YopJdBjL0MaF+bMaEtnYvoN2BhXjVmZl7GfpTezZU2ACXZfToEZ/IAfnxzYX+h1+YbhXaQBINtcVRborON84vub45TH7A0l69ZA08gkayegb0L70oFXOH7izvVHS5utLrEE/clA/Bq0GI2QADAp6qEgnEP3XpFKxJjCpBfGtpX31Fx2ouZPQq/fp87ASCgvbuXFmtySuPr1ceC+mXy+TJJ58wk9bRkR7GXU6HwMUlOpKBgf0xiBw6fxu2uQGbIbEc0kuM+gIUdi6NvJpishm/as5buesjvq4u2r3Y1AtW5j+tgMuH8bk+i8CvmXqBR3adUJfNbQxpIp7liWMSBenPrH/7ETubYwmjFg9uw/lWfEkrFJuaRVD4H1WYG7Wwyki7Zt/nJTCZWC0LgOVJZ1vmpwqTnAml7VJBLlAP2xdBDWjSdFHxWCCNNCUpz8kjQpbGn06h/gfOYQYG9GnBS/MzQy7lzrXFTsEbf/fB6HsSU2g/t4ooreVF+sSPhfyOsLyfr61YG+DUYf5uIPtUBf5WSA8eUu0zJTPTRILNFaqMnhxOMA7limeCZPG+Yzwww==&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 13,
      &quot;candidatesTokenCount&quot;: 409,
      &quot;totalTokenCount&quot;: 1275,
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
          &quot;tokenCount&quot;: 409
        }
      ],
      &quot;thoughtsTokenCount&quot;: 853
    },
    &quot;modelVersion&quot;: &quot;gemini-3-flash-preview&quot;,
    &quot;createTime&quot;: &quot;2026-07-24T23:10:39.662413Z&quot;,
    &quot;responseId&quot;: &quot;7_Bjao23KPaH3dAP_vWlwAY&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3-flash&#x27;,
  {
    contents: [
      {
        parts: [{ text: &#x27;Write a short story opening about a detective finding an unusual clue.&#x27; }],
        role: &#x27;user&#x27;,
      },
    ],
    generationConfig: { maxOutputTokens: 4096, temperature: 0.8 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3-flash&quot;,
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
      &quot;maxOutputTokens&quot;: 4096,
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

- [Input schema](/ai/models/google/gemini-3-flash/schema-input.json)
- [Output schema](/ai/models/google/gemini-3-flash/schema-output.json)

