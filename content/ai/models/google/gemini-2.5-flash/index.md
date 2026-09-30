<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-2-5-flash">Gemini 2.5 Flash</h1>

<p><code>google/gemini-2.5-flash</code></p>

Google's fast multimodal Gemini 2.5 model with strong reasoning and a 1M token context window.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.3, Output tokens (per 1M): 2.5, Cached input tokens (per 1M): 0.03</td></tr>
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
    &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental principles that govern how energy is transferred and transformed in physical systems. They are:\n\n1.  **The First Law of Thermodynamics (Law of Conservation of Energy)**\n    *   **Statement:** Energy cannot be created or destroyed in an isolated system; it can only be transformed from one form to another.\n    *   **Explanation:** This law means that the total amount of energy in the universe remains constant. When energy appears to be \&quot;lost,\&quot; it has merely changed into a different form (e.g., chemical energy into heat, electrical energy into light and heat). Mathematically, for a closed system, it&#x27;s often expressed as: $\\Delta U = Q - W$, where $\\Delta U$ is the change in the internal energy of the system, $Q$ is the heat added to the system, and $W$ is the work done *by* the system.\n\n2.  **The Second Law of Thermodynamics (Law of Entropy Increase)**\n    *   **Statement:** The total entropy of an isolated system can only increase over time, or remain constant in ideal cases; it never decreases.\n    *   **Explanation:** Entropy is a measure of disorder or randomness within a system. This law essentially states that natural processes tend to move towards a state of greater disorder or randomness. For example, a broken glass won&#x27;t spontaneously reassemble, and heat naturally flows from a hotter object to a colder one, not the other way around. This law also implies that no heat engine can be 100% efficient because some energy will always be lost to increasing the entropy of the surroundings (often as waste heat).\n\n3.  **The Third Law of Thermodynamics**\n    *   **Statement:** As a system approaches absolute zero, its entropy approaches a constant minimum value. For a perfect crystal at absolute zero (0 Kelvin or -273.15 \u00b0C), the entropy is exactly zero.\n    *   **Explanation:** This law provides a fundamental reference point for the measurement of entropy. It means that at absolute zero, all molecular motion would cease, and the system would be in its most ordered possible state (a perfect crystal with no defects). In practice, reaching absolute zero is impossible, as doing so would require an infinite number of steps, each becoming progressively harder.\n\nThese three laws are cornerstones of physics and chemistry, explaining a vast range of phenomena from the operation of engines to the direction of chemical reactions and the very evolution of the universe.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.7025290479937804,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental principles that govern how energy is transferred and transformed in physical systems. They are:\n\n1.  **The First Law of Thermodynamics (Law of Conservation of Energy)**\n    *   **Statement:** Energy cannot be created or destroyed in an isolated system; it can only be transformed from one form to another.\n    *   **Explanation:** This law means that the total amount of energy in the universe remains constant. When energy appears to be \&quot;lost,\&quot; it has merely changed into a different form (e.g., chemical energy into heat, electrical energy into light and heat). Mathematically, for a closed system, it&#x27;s often expressed as: $\\Delta U = Q - W$, where $\\Delta U$ is the change in the internal energy of the system, $Q$ is the heat added to the system, and $W$ is the work done *by* the system.\n\n2.  **The Second Law of Thermodynamics (Law of Entropy Increase)**\n    *   **Statement:** The total entropy of an isolated system can only increase over time, or remain constant in ideal cases; it never decreases.\n    *   **Explanation:** Entropy is a measure of disorder or randomness within a system. This law essentially states that natural processes tend to move towards a state of greater disorder or randomness. For example, a broken glass won&#x27;t spontaneously reassemble, and heat naturally flows from a hotter object to a colder one, not the other way around. This law also implies that no heat engine can be 100% efficient because some energy will always be lost to increasing the entropy of the surroundings (often as waste heat).\n\n3.  **The Third Law of Thermodynamics**\n    *   **Statement:** As a system approaches absolute zero, its entropy approaches a constant minimum value. For a perfect crystal at absolute zero (0 Kelvin or -273.15 \u00b0C), the entropy is exactly zero.\n    *   **Explanation:** This law provides a fundamental reference point for the measurement of entropy. It means that at absolute zero, all molecular motion would cease, and the system would be in its most ordered possible state (a perfect crystal with no defects). In practice, reaching absolute zero is impossible, as doing so would require an infinite number of steps, each becoming progressively harder.\n\nThese three laws are cornerstones of physics and chemistry, explaining a vast range of phenomena from the operation of engines to the direction of chemical reactions and the very evolution of the universe.&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:47.652835Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash&quot;,
    &quot;responseId&quot;: &quot;1wvxaaPsJ8CG998Pn665-Ag&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 515,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 515
        }
      ],
      &quot;promptTokenCount&quot;: 8,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 8
        }
      ],
      &quot;thoughtsTokenCount&quot;: 1020,
      &quot;totalTokenCount&quot;: 1543,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash&#x27;,
  { contents: [{ parts: [{ text: &#x27;What are the three laws of thermodynamics?&#x27; }], role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-2.5-flash&quot;,
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
    &quot;text&quot;: &quot;Reading a JSON (JavaScript Object Notation) file in Python is straightforward, thanks to the built-in `json` module.\n\nHere&#x27;s a step-by-step guide with examples:\n\n---\n\n### 1. The `json` Module\n\nPython&#x27;s `json` module provides methods for working with JSON data. The two primary methods you&#x27;ll use for reading are:\n\n*   **`json.load()`**: Reads JSON data from a file-like object (e.g., a file opened with `open()`).\n*   **`json.loads()`**: Reads JSON data from a string.\n\n---\n\n### 2. Example: Reading a JSON File (`json.load()`)\n\nThis is the most common way to read a JSON file.\n\n**Step 1: Create a sample JSON file**\n\nLet&#x27;s create a file named `data.json` with the following content:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;isStudent\&quot;: false,\n  \&quot;courses\&quot;: [\n    {\&quot;title\&quot;: \&quot;Math\&quot;, \&quot;credits\&quot;: 3},\n    {\&quot;title\&quot;: \&quot;Science\&quot;, \&quot;credits\&quot;: 4}\n  ],\n  \&quot;address\&quot;: null\n}\n```\n\n**Step 2: Python code to read the file**\n\n```python\nimport json\n\nfile_path = &#x27;data.json&#x27;\n\ntry:\n    # Open the JSON file in read mode (&#x27;r&#x27;)\n    # The &#x27;with&#x27; statement ensures the file is properly closed even if errors occur.\n    with open(file_path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n        # Use json.load() to parse the JSON data from the file\n        data = json.load(file)\n\n    print(\&quot;JSON data successfully loaded:\&quot;)\n    print(data)\n    print(f\&quot;\\nType of loaded data: {type(data)}\&quot;)\n\n    # You can now access the data like a Python dictionary or list\n    print(f\&quot;Name: {data[&#x27;name&#x27;]}\&quot;)\n    print(f\&quot;Age: {data[&#x27;age&#x27;]}\&quot;)\n    print(f\&quot;First course title: {data[&#x27;courses&#x27;][0][&#x27;title&#x27;]}\&quot;)\n\nexcept FileNotFoundError:\n    print(f\&quot;Error: The file &#x27;{file_path}&#x27; was not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(f\&quot;Error: Could not decode JSON from &#x27;{file_path}&#x27;. Check its format.\&quot;)\nexcept Exception as e:\n    print(f\&quot;An unexpected error occurred: {e}\&quot;)\n\n```\n\n**Explanation:**\n\n1.  **`import json`**: Imports the necessary module.\n2.  **`with open(file_path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:`**:\n    *   Opens the file specified by `file_path`.\n    *   `&#x27;r&#x27;` indicates read mode.\n    *   `encoding=&#x27;utf-8&#x27;` is a good practice, especially if your JSON might contain non-ASCII characters.\n    *   The `with` statement is a context manager that ensures the file is automatically closed when the block is exited, even if errors occur.\n3.  **`data = json.load(file)`**: This is the core line. It reads the entire content of the `file` object, parses it as JSON, and converts it into a corresponding Python object (usually a dictionary or a list).\n4.  **Error Handling**: The `try...except` block is crucial for robust code:\n    *   `FileNotFoundError`: Catches the error if the specified file doesn&#x27;t exist.\n    *   `json.JSONDecodeError`: Catches errors if the file content is not valid JSON.\n    *   `Exception as e`: Catches any other unexpected errors.\n\n---\n\n### 3. Example: Reading JSON from a String (`json.loads()`)\n\nSometimes, you might receive JSON data as a string (e.g., from a web API response). In such cases, you use `json.loads()`.\n\n```python\nimport json\n\njson_string_data = &#x27;&#x27;&#x27;\n{\n  \&quot;product\&quot;: \&quot;Laptop\&quot;,\n  \&quot;price\&quot;: 1200.50,\n  \&quot;inStock\&quot;: true,\n  \&quot;features\&quot;: [\&quot;lightweight\&quot;, \&quot;fast processor\&quot;]\n}\n&#x27;&#x27;&#x27;\n\ntry:\n    # Use json.loads() to parse the JSON data from a string\n    data_from_string = json.loads(json_string_data)\n\n    print(\&quot;\\nJSON data from string successfully loaded:\&quot;)\n    print(data_from_string)\n    print(f\&quot;Type of loaded data: {type(data_from_string)}\&quot;)\n\n    print(f\&quot;Product: {data_from_string[&#x27;product&#x27;]}\&quot;)\n    print(f\&quot;Price: ${data_from_string[&#x27;price&#x27;]}\&quot;)\n\nexcept json.JSONDecodeError:\n    print(\&quot;Error: Could not decode JSON from the string. Check its format.\&quot;)\nexcept Exception as e:\n    print(f\&quot;An unexpected error occurred: {e}\&quot;)\n```\n\n---\n\n### 4. JSON to Python Type Conversion\n\nWhen `json.load()` or `json.loads()` parses JSON, it converts JSON data types to their corresponding Python types:\n\n| JSON Type     | Python Type     |\n| :------------ | :-------------- |\n| object        | `dict`          |\n| array         | `list`          |\n| string        | `str`           |\n| number        | `int` or `float` |\n| boolean       | `bool`          |\n| null          | `None`          |\n\n---\n\n### Best Practices:\n\n*   **Always use `with open(...)`**: It&#x27;s safer and handles file closing automatically.\n*   **Include `encoding=&#x27;utf-8&#x27;`**: This prevents issues with character encoding, especially for international data.\n*   **Implement Error Handling**: Use `try...except` blocks to gracefully handle `FileNotFoundError` and `json.JSONDecodeError`.\n*   **Understand `load` vs. `loads`**: Use `load` for file objects and `loads` for strings.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.20984612667199337,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Reading a JSON (JavaScript Object Notation) file in Python is straightforward, thanks to the built-in `json` module.\n\nHere&#x27;s a step-by-step guide with examples:\n\n---\n\n### 1. The `json` Module\n\nPython&#x27;s `json` module provides methods for working with JSON data. The two primary methods you&#x27;ll use for reading are:\n\n*   **`json.load()`**: Reads JSON data from a file-like object (e.g., a file opened with `open()`).\n*   **`json.loads()`**: Reads JSON data from a string.\n\n---\n\n### 2. Example: Reading a JSON File (`json.load()`)\n\nThis is the most common way to read a JSON file.\n\n**Step 1: Create a sample JSON file**\n\nLet&#x27;s create a file named `data.json` with the following content:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;isStudent\&quot;: false,\n  \&quot;courses\&quot;: [\n    {\&quot;title\&quot;: \&quot;Math\&quot;, \&quot;credits\&quot;: 3},\n    {\&quot;title\&quot;: \&quot;Science\&quot;, \&quot;credits\&quot;: 4}\n  ],\n  \&quot;address\&quot;: null\n}\n```\n\n**Step 2: Python code to read the file**\n\n```python\nimport json\n\nfile_path = &#x27;data.json&#x27;\n\ntry:\n    # Open the JSON file in read mode (&#x27;r&#x27;)\n    # The &#x27;with&#x27; statement ensures the file is properly closed even if errors occur.\n    with open(file_path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n        # Use json.load() to parse the JSON data from the file\n        data = json.load(file)\n\n    print(\&quot;JSON data successfully loaded:\&quot;)\n    print(data)\n    print(f\&quot;\\nType of loaded data: {type(data)}\&quot;)\n\n    # You can now access the data like a Python dictionary or list\n    print(f\&quot;Name: {data[&#x27;name&#x27;]}\&quot;)\n    print(f\&quot;Age: {data[&#x27;age&#x27;]}\&quot;)\n    print(f\&quot;First course title: {data[&#x27;courses&#x27;][0][&#x27;title&#x27;]}\&quot;)\n\nexcept FileNotFoundError:\n    print(f\&quot;Error: The file &#x27;{file_path}&#x27; was not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(f\&quot;Error: Could not decode JSON from &#x27;{file_path}&#x27;. Check its format.\&quot;)\nexcept Exception as e:\n    print(f\&quot;An unexpected error occurred: {e}\&quot;)\n\n```\n\n**Explanation:**\n\n1.  **`import json`**: Imports the necessary module.\n2.  **`with open(file_path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:`**:\n    *   Opens the file specified by `file_path`.\n    *   `&#x27;r&#x27;` indicates read mode.\n    *   `encoding=&#x27;utf-8&#x27;` is a good practice, especially if your JSON might contain non-ASCII characters.\n    *   The `with` statement is a context manager that ensures the file is automatically closed when the block is exited, even if errors occur.\n3.  **`data = json.load(file)`**: This is the core line. It reads the entire content of the `file` object, parses it as JSON, and converts it into a corresponding Python object (usually a dictionary or a list).\n4.  **Error Handling**: The `try...except` block is crucial for robust code:\n    *   `FileNotFoundError`: Catches the error if the specified file doesn&#x27;t exist.\n    *   `json.JSONDecodeError`: Catches errors if the file content is not valid JSON.\n    *   `Exception as e`: Catches any other unexpected errors.\n\n---\n\n### 3. Example: Reading JSON from a String (`json.loads()`)\n\nSometimes, you might receive JSON data as a string (e.g., from a web API response). In such cases, you use `json.loads()`.\n\n```python\nimport json\n\njson_string_data = &#x27;&#x27;&#x27;\n{\n  \&quot;product\&quot;: \&quot;Laptop\&quot;,\n  \&quot;price\&quot;: 1200.50,\n  \&quot;inStock\&quot;: true,\n  \&quot;features\&quot;: [\&quot;lightweight\&quot;, \&quot;fast processor\&quot;]\n}\n&#x27;&#x27;&#x27;\n\ntry:\n    # Use json.loads() to parse the JSON data from a string\n    data_from_string = json.loads(json_string_data)\n\n    print(\&quot;\\nJSON data from string successfully loaded:\&quot;)\n    print(data_from_string)\n    print(f\&quot;Type of loaded data: {type(data_from_string)}\&quot;)\n\n    print(f\&quot;Product: {data_from_string[&#x27;product&#x27;]}\&quot;)\n    print(f\&quot;Price: ${data_from_string[&#x27;price&#x27;]}\&quot;)\n\nexcept json.JSONDecodeError:\n    print(\&quot;Error: Could not decode JSON from the string. Check its format.\&quot;)\nexcept Exception as e:\n    print(f\&quot;An unexpected error occurred: {e}\&quot;)\n```\n\n---\n\n### 4. JSON to Python Type Conversion\n\nWhen `json.load()` or `json.loads()` parses JSON, it converts JSON data types to their corresponding Python types:\n\n| JSON Type     | Python Type     |\n| :------------ | :-------------- |\n| object        | `dict`          |\n| array         | `list`          |\n| string        | `str`           |\n| number        | `int` or `float` |\n| boolean       | `bool`          |\n| null          | `None`          |\n\n---\n\n### Best Practices:\n\n*   **Always use `with open(...)`**: It&#x27;s safer and handles file closing automatically.\n*   **Include `encoding=&#x27;utf-8&#x27;`**: This prevents issues with character encoding, especially for international data.\n*   **Implement Error Handling**: Use `try...except` blocks to gracefully handle `FileNotFoundError` and `json.JSONDecodeError`.\n*   **Understand `load` vs. `loads`**: Use `load` for file objects and `loads` for strings.&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:48.848405Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash&quot;,
    &quot;responseId&quot;: &quot;2AvxaZXkM5mA6tkPxraQ6Qg&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 1320,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 1320
        }
      ],
      &quot;promptTokenCount&quot;: 20,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 20
        }
      ],
      &quot;thoughtsTokenCount&quot;: 1357,
      &quot;totalTokenCount&quot;: 2697,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-2.5-flash&quot;,
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
    &quot;text&quot;: &quot;Okay, you&#x27;ve got two main routes, each with its own character and fantastic stops&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -10.623407151963976,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Okay, you&#x27;ve got two main routes, each with its own character and fantastic stops&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;MAX_TOKENS&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:57.011971Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash&quot;,
    &quot;responseId&quot;: &quot;4QvxacNd9bf33w-WuK35Ag&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 18,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 18
        }
      ],
      &quot;promptTokenCount&quot;: 64,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 64
        }
      ],
      &quot;thoughtsTokenCount&quot;: 478,
      &quot;totalTokenCount&quot;: 560,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-2.5-flash&quot;,
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
    &quot;text&quot;: &quot;The rain had been a relentless drumbeat against&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -13.157335069444445,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The rain had been a relentless drumbeat against&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;MAX_TOKENS&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:35:01.318796Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash&quot;,
    &quot;responseId&quot;: &quot;5Qvxacy6E6CV9LsP2P_v0Ak&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 9,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 9
        }
      ],
      &quot;promptTokenCount&quot;: 13,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 13
        }
      ],
      &quot;thoughtsTokenCount&quot;: 287,
      &quot;totalTokenCount&quot;: 309,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-2.5-flash&quot;,
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

- [Input schema](/ai/models/google/gemini-2.5-flash/schema-input.json)
- [Output schema](/ai/models/google/gemini-2.5-flash/schema-output.json)

