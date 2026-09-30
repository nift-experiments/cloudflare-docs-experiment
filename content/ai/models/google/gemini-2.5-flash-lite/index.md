---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash-lite/
  description: google/gemini-2.5-flash-lite
  full_title: Gemini 2.5 Flash Lite · Cloudflare AI docs
  head_html: <title>Gemini 2.5 Flash Lite · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="google/gemini-2.5-flash-lite"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash-lite/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Gemini 2.5 Flash Lite · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="google/gemini-2.5-flash-lite"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash-lite/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash-lite/#page","headline":"Gemini 2.5 Flash Lite \u00b7 Cloudflare AI docs","description":"google/gemini-2.5-flash-lite","url":"https://developers.cloudflare.com/ai/models/google/gemini-2.5-flash-lite/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/google/gemini-2.5-flash-lite/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-2-5-flash-lite">Gemini 2.5 Flash Lite</h1>

<p><code>google/gemini-2.5-flash-lite</code></p>

Google's lightest and most cost-efficient Gemini 2.5 model for high-throughput tasks.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.1, Output tokens (per 1M): 0.4, Cached input tokens (per 1M): 0.01</td></tr>
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
    &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental principles that describe the behavior of energy and matter. Here they are:\n\n1.  **The Zeroth Law of Thermodynamics:**\n    *   **Statement:** If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other.\n    *   **In simpler terms:** This law essentially defines the concept of temperature. If object A is the same temperature as object B, and object B is the same temperature as object C, then object A must also be the same temperature as object C. It allows us to use thermometers to measure temperature, as they achieve thermal equilibrium with the object being measured.\n\n2.  **The First Law of Thermodynamics (Conservation of Energy):**\n    *   **Statement:** Energy cannot be created or destroyed, only transferred or changed from one form to another. In a closed system, the total energy remains constant.\n    *   **In simpler terms:** This is the law of conservation of energy. It means that the amount of energy in the universe is fixed. You can&#x27;t get energy out of nowhere, and you can&#x27;t make energy disappear. It can be converted, for example, from chemical energy in fuel to heat and kinetic energy in a car engine, but the total amount of energy stays the same.\n    *   **Mathematical representation:** $\\Delta U = Q - W$\n        *   $\\Delta U$ is the change in internal energy of the system.\n        *   $Q$ is the heat added to the system.\n        *   $W$ is the work done by the system.\n\n3.  **The Second Law of Thermodynamics (Entropy):**\n    *   **Statement:** In any isolated system, the total entropy (a measure of disorder or randomness) can only increase over time, or remain constant in ideal cases where the system is in a steady state or undergoing a reversible process. It never decreases.\n    *   **In simpler terms:** This law explains why certain processes happen spontaneously and others don&#x27;t. It&#x27;s often described as \&quot;things tend to get messier.\&quot; Heat naturally flows from hotter objects to colder objects, never the other way around spontaneously. Engines are never 100% efficient because some energy is always lost as unusable heat, increasing the overall entropy of the universe.\n    *   **Implications:**\n        *   It dictates the direction of spontaneous processes.\n        *   It explains why perpetual motion machines of the second kind (which would convert all heat into work without any losses) are impossible.\n        *   It suggests that the universe is heading towards a state of maximum entropy, often referred to as \&quot;heat death.\&quot;\n\nThese three laws are fundamental to understanding how energy works in everything from chemical reactions and engines to living organisms and the universe as a whole.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.2047232930570739,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental principles that describe the behavior of energy and matter. Here they are:\n\n1.  **The Zeroth Law of Thermodynamics:**\n    *   **Statement:** If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other.\n    *   **In simpler terms:** This law essentially defines the concept of temperature. If object A is the same temperature as object B, and object B is the same temperature as object C, then object A must also be the same temperature as object C. It allows us to use thermometers to measure temperature, as they achieve thermal equilibrium with the object being measured.\n\n2.  **The First Law of Thermodynamics (Conservation of Energy):**\n    *   **Statement:** Energy cannot be created or destroyed, only transferred or changed from one form to another. In a closed system, the total energy remains constant.\n    *   **In simpler terms:** This is the law of conservation of energy. It means that the amount of energy in the universe is fixed. You can&#x27;t get energy out of nowhere, and you can&#x27;t make energy disappear. It can be converted, for example, from chemical energy in fuel to heat and kinetic energy in a car engine, but the total amount of energy stays the same.\n    *   **Mathematical representation:** $\\Delta U = Q - W$\n        *   $\\Delta U$ is the change in internal energy of the system.\n        *   $Q$ is the heat added to the system.\n        *   $W$ is the work done by the system.\n\n3.  **The Second Law of Thermodynamics (Entropy):**\n    *   **Statement:** In any isolated system, the total entropy (a measure of disorder or randomness) can only increase over time, or remain constant in ideal cases where the system is in a steady state or undergoing a reversible process. It never decreases.\n    *   **In simpler terms:** This law explains why certain processes happen spontaneously and others don&#x27;t. It&#x27;s often described as \&quot;things tend to get messier.\&quot; Heat naturally flows from hotter objects to colder objects, never the other way around spontaneously. Engines are never 100% efficient because some energy is always lost as unusable heat, increasing the overall entropy of the universe.\n    *   **Implications:**\n        *   It dictates the direction of spontaneous processes.\n        *   It explains why perpetual motion machines of the second kind (which would convert all heat into work without any losses) are impossible.\n        *   It suggests that the universe is heading towards a state of maximum entropy, often referred to as \&quot;heat death.\&quot;\n\nThese three laws are fundamental to understanding how energy works in everything from chemical reactions and engines to living organisms and the universe as a whole.&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:41.622271Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash-lite&quot;,
    &quot;responseId&quot;: &quot;0Qvxab_9Jc-R9LsPkdy1uAo&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 586,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 586
        }
      ],
      &quot;promptTokenCount&quot;: 8,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 8
        }
      ],
      &quot;totalTokenCount&quot;: 594,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash-lite&#x27;,
  { contents: [{ parts: [{ text: &#x27;What are the three laws of thermodynamics?&#x27; }], role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-2.5-flash-lite&quot;,
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
    &quot;text&quot;: &quot;Reading a JSON file in Python is a straightforward process thanks to the built-in `json` module. Here&#x27;s a breakdown of how to do it, along with explanations and examples:\n\n**The Core Concept**\n\nJSON (JavaScript Object Notation) is a lightweight data-interchange format. Python&#x27;s `json` module provides functions to:\n\n*   **`json.load()`**: Reads a JSON document from a file-like object and parses it into a Python object (dictionaries, lists, strings, numbers, booleans, and `None`).\n*   **`json.loads()`**: Reads a JSON document from a string and parses it into a Python object.\n\nSince you&#x27;re asking about reading from a file, `json.load()` is the function you&#x27;ll primarily use.\n\n**Steps to Read a JSON File**\n\n1.  **Import the `json` module:**\n    ```python\n    import json\n    ```\n\n2.  **Open the JSON file:** You need to open the file in read mode (`&#x27;r&#x27;`). It&#x27;s best practice to use a `with` statement, which ensures the file is automatically closed even if errors occur.\n    ```python\n    with open(&#x27;your_file.json&#x27;, &#x27;r&#x27;) as f:\n        # File operations will go here\n    ```\n    Replace `&#x27;your_file.json&#x27;` with the actual path to your JSON file.\n\n3.  **Load the JSON data:** Use `json.load()` to read the content from the opened file object and convert it into a Python data structure.\n    ```python\n    with open(&#x27;your_file.json&#x27;, &#x27;r&#x27;) as f:\n        data = json.load(f)\n    ```\n\n**Example**\n\nLet&#x27;s assume you have a JSON file named `data.json` with the following content:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;isStudent\&quot;: false,\n  \&quot;courses\&quot;: [\n    {\&quot;title\&quot;: \&quot;Math\&quot;, \&quot;credits\&quot;: 3},\n    {\&quot;title\&quot;: \&quot;Science\&quot;, \&quot;credits\&quot;: 4}\n  ],\n  \&quot;address\&quot;: {\n    \&quot;street\&quot;: \&quot;123 Main St\&quot;,\n    \&quot;city\&quot;: \&quot;Anytown\&quot;\n  }\n}\n```\n\nHere&#x27;s the Python code to read this file:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as f:\n        data = json.load(f)\n\n    # Now &#x27;data&#x27; is a Python dictionary\n    print(f\&quot;Name: {data[&#x27;name&#x27;]}\&quot;)\n    print(f\&quot;Age: {data[&#x27;age&#x27;]}\&quot;)\n    print(f\&quot;Is Student: {data[&#x27;isStudent&#x27;]}\&quot;)\n    print(\&quot;Courses:\&quot;)\n    for course in data[&#x27;courses&#x27;]:\n        print(f\&quot;  - {course[&#x27;title&#x27;]} ({course[&#x27;credits&#x27;]} credits)\&quot;)\n    print(f\&quot;City: {data[&#x27;address&#x27;][&#x27;city&#x27;]}\&quot;)\n\nexcept FileNotFoundError:\n    print(\&quot;Error: The file &#x27;data.json&#x27; was not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Error: Could not decode JSON from the file. Please check its format.\&quot;)\nexcept Exception as e:\n    print(f\&quot;An unexpected error occurred: {e}\&quot;)\n```\n\n**Explanation of the Example:**\n\n*   **`import json`**: Imports the necessary module.\n*   **`with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as f:`**: Opens `data.json` in read mode. The file object is assigned to the variable `f`.\n*   **`data = json.load(f)`**: Reads the entire content of the file `f` and parses it. The resulting Python object (in this case, a dictionary) is stored in the `data` variable.\n*   **Accessing Data**: You can then access the data using standard Python dictionary and list indexing:\n    *   `data[&#x27;name&#x27;]` accesses the value associated with the \&quot;name\&quot; key.\n    *   `data[&#x27;courses&#x27;]` accesses the list of courses.\n    *   `data[&#x27;courses&#x27;][0]` accesses the first course dictionary.\n    *   `data[&#x27;courses&#x27;][0][&#x27;title&#x27;]` accesses the title of the first course.\n*   **Error Handling**: The `try...except` block is crucial for robust code.\n    *   `FileNotFoundError`: Catches the case where `data.json` doesn&#x27;t exist.\n    *   `json.JSONDecodeError`: Catches errors if the file&#x27;s content is not valid JSON.\n    *   `Exception`: A general catch-all for any other unexpected errors.\n\n**Reading JSON from a String**\n\nIf you have JSON data as a string (e.g., from an API response), you&#x27;d use `json.loads()`:\n\n```python\nimport json\n\njson_string = \&quot;\&quot;\&quot;\n{\n  \&quot;product\&quot;: \&quot;Laptop\&quot;,\n  \&quot;price\&quot;: 1200.50,\n  \&quot;inStock\&quot;: true\n}\n\&quot;\&quot;\&quot;\n\ntry:\n    data = json.loads(json_string)\n    print(f\&quot;Product: {data[&#x27;product&#x27;]}\&quot;)\n    print(f\&quot;Price: ${data[&#x27;price&#x27;]:.2f}\&quot;)\n    print(f\&quot;In Stock: {data[&#x27;inStock&#x27;]}\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Error: Could not decode JSON from the string.\&quot;)\n```\n\n**Key Considerations:**\n\n*   **File Encoding:** By default, `open()` uses the system&#x27;s default encoding. If your JSON file uses a different encoding (like UTF-8, which is common), you should specify it:\n    ```python\n    with open(&#x27;your_file.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n        data = json.load(f)\n    ```\n*   **JSON Structure:** The `json.load()` function will convert JSON data types to their Python equivalents:\n    *   JSON objects (`{}`) become Python dictionaries (`dict`).\n    *   JSON arrays (`[]`) become Python lists (`list`).\n    *   JSON strings (`\&quot;...\&quot;`) become Python strings (`str`).\n    *   JSON numbers (integers and floats) become Python integers (`int`) or floats (`float`).\n    *   JSON booleans (`true`, `false`) become Python booleans (`True`, `False`).\n    *   JSON `null` becomes Python `None`.\n*   **Error Handling is Essential:** Always include error handling to gracefully manage situations where the file is missing or contains invalid JSON.\n\nBy following these steps, you can effectively read and work with JSON data in your Python applications.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.05239303652533901,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Reading a JSON file in Python is a straightforward process thanks to the built-in `json` module. Here&#x27;s a breakdown of how to do it, along with explanations and examples:\n\n**The Core Concept**\n\nJSON (JavaScript Object Notation) is a lightweight data-interchange format. Python&#x27;s `json` module provides functions to:\n\n*   **`json.load()`**: Reads a JSON document from a file-like object and parses it into a Python object (dictionaries, lists, strings, numbers, booleans, and `None`).\n*   **`json.loads()`**: Reads a JSON document from a string and parses it into a Python object.\n\nSince you&#x27;re asking about reading from a file, `json.load()` is the function you&#x27;ll primarily use.\n\n**Steps to Read a JSON File**\n\n1.  **Import the `json` module:**\n    ```python\n    import json\n    ```\n\n2.  **Open the JSON file:** You need to open the file in read mode (`&#x27;r&#x27;`). It&#x27;s best practice to use a `with` statement, which ensures the file is automatically closed even if errors occur.\n    ```python\n    with open(&#x27;your_file.json&#x27;, &#x27;r&#x27;) as f:\n        # File operations will go here\n    ```\n    Replace `&#x27;your_file.json&#x27;` with the actual path to your JSON file.\n\n3.  **Load the JSON data:** Use `json.load()` to read the content from the opened file object and convert it into a Python data structure.\n    ```python\n    with open(&#x27;your_file.json&#x27;, &#x27;r&#x27;) as f:\n        data = json.load(f)\n    ```\n\n**Example**\n\nLet&#x27;s assume you have a JSON file named `data.json` with the following content:\n\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;isStudent\&quot;: false,\n  \&quot;courses\&quot;: [\n    {\&quot;title\&quot;: \&quot;Math\&quot;, \&quot;credits\&quot;: 3},\n    {\&quot;title\&quot;: \&quot;Science\&quot;, \&quot;credits\&quot;: 4}\n  ],\n  \&quot;address\&quot;: {\n    \&quot;street\&quot;: \&quot;123 Main St\&quot;,\n    \&quot;city\&quot;: \&quot;Anytown\&quot;\n  }\n}\n```\n\nHere&#x27;s the Python code to read this file:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as f:\n        data = json.load(f)\n\n    # Now &#x27;data&#x27; is a Python dictionary\n    print(f\&quot;Name: {data[&#x27;name&#x27;]}\&quot;)\n    print(f\&quot;Age: {data[&#x27;age&#x27;]}\&quot;)\n    print(f\&quot;Is Student: {data[&#x27;isStudent&#x27;]}\&quot;)\n    print(\&quot;Courses:\&quot;)\n    for course in data[&#x27;courses&#x27;]:\n        print(f\&quot;  - {course[&#x27;title&#x27;]} ({course[&#x27;credits&#x27;]} credits)\&quot;)\n    print(f\&quot;City: {data[&#x27;address&#x27;][&#x27;city&#x27;]}\&quot;)\n\nexcept FileNotFoundError:\n    print(\&quot;Error: The file &#x27;data.json&#x27; was not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Error: Could not decode JSON from the file. Please check its format.\&quot;)\nexcept Exception as e:\n    print(f\&quot;An unexpected error occurred: {e}\&quot;)\n```\n\n**Explanation of the Example:**\n\n*   **`import json`**: Imports the necessary module.\n*   **`with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as f:`**: Opens `data.json` in read mode. The file object is assigned to the variable `f`.\n*   **`data = json.load(f)`**: Reads the entire content of the file `f` and parses it. The resulting Python object (in this case, a dictionary) is stored in the `data` variable.\n*   **Accessing Data**: You can then access the data using standard Python dictionary and list indexing:\n    *   `data[&#x27;name&#x27;]` accesses the value associated with the \&quot;name\&quot; key.\n    *   `data[&#x27;courses&#x27;]` accesses the list of courses.\n    *   `data[&#x27;courses&#x27;][0]` accesses the first course dictionary.\n    *   `data[&#x27;courses&#x27;][0][&#x27;title&#x27;]` accesses the title of the first course.\n*   **Error Handling**: The `try...except` block is crucial for robust code.\n    *   `FileNotFoundError`: Catches the case where `data.json` doesn&#x27;t exist.\n    *   `json.JSONDecodeError`: Catches errors if the file&#x27;s content is not valid JSON.\n    *   `Exception`: A general catch-all for any other unexpected errors.\n\n**Reading JSON from a String**\n\nIf you have JSON data as a string (e.g., from an API response), you&#x27;d use `json.loads()`:\n\n```python\nimport json\n\njson_string = \&quot;\&quot;\&quot;\n{\n  \&quot;product\&quot;: \&quot;Laptop\&quot;,\n  \&quot;price\&quot;: 1200.50,\n  \&quot;inStock\&quot;: true\n}\n\&quot;\&quot;\&quot;\n\ntry:\n    data = json.loads(json_string)\n    print(f\&quot;Product: {data[&#x27;product&#x27;]}\&quot;)\n    print(f\&quot;Price: ${data[&#x27;price&#x27;]:.2f}\&quot;)\n    print(f\&quot;In Stock: {data[&#x27;inStock&#x27;]}\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Error: Could not decode JSON from the string.\&quot;)\n```\n\n**Key Considerations:**\n\n*   **File Encoding:** By default, `open()` uses the system&#x27;s default encoding. If your JSON file uses a different encoding (like UTF-8, which is common), you should specify it:\n    ```python\n    with open(&#x27;your_file.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n        data = json.load(f)\n    ```\n*   **JSON Structure:** The `json.load()` function will convert JSON data types to their Python equivalents:\n    *   JSON objects (`{}`) become Python dictionaries (`dict`).\n    *   JSON arrays (`[]`) become Python lists (`list`).\n    *   JSON strings (`\&quot;...\&quot;`) become Python strings (`str`).\n    *   JSON numbers (integers and floats) become Python integers (`int`) or floats (`float`).\n    *   JSON booleans (`true`, `false`) become Python booleans (`True`, `False`).\n    *   JSON `null` becomes Python `None`.\n*   **Error Handling is Essential:** Always include error handling to gracefully manage situations where the file is missing or contains invalid JSON.\n\nBy following these steps, you can effectively read and work with JSON data in your Python applications.&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:41.673305Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash-lite&quot;,
    &quot;responseId&quot;: &quot;0QvxaZmMKdSNq8YPyLuh0AQ&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 1438,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 1438
        }
      ],
      &quot;promptTokenCount&quot;: 20,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 20
        }
      ],
      &quot;totalTokenCount&quot;: 1458,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash-lite&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-2.5-flash-lite&quot;,
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
    &quot;text&quot;: &quot;Absolutely! The drive from San Francisco to Los Angeles offers a variety of stunning scenery and charming towns. Here are some of the most popular and highly recommended stops, depending on your interests and how much time you have:\n\n**The Classic Coastal Route (Highway 1 - the most scenic, but can be slower):**\n\nThis is the iconic drive for a reason! Expect breathtaking ocean views, dramatic cliffs, and charming seaside towns. Be aware that sections of Highway 1 can be prone to closures due to landslides, so always check road conditions before you go (Caltrans is your friend!).\n\n*   **Monterey:**\n    *   **Monterey Bay Aquarium:** World-renowned and a must-visit. Plan for at least 2-3 hours.\n    *   **Cannery Row:** Historic waterfront street, now filled with shops, restaurants, and hotels.\n    *   **Old Fisherman&#x27;s Wharf:** Great for whale watching tours, seafood, and souvenirs.\n    *   **17-Mile Drive (Pebble Beach):** A private toll road with stunning coastal scenery, iconic golf courses, and the Lone Cypress.\n*   **Carmel-by-the-Sea:**\n    *   **Charming Village:** Wander through art galleries, boutiques, and quaint cottages.\n    *   **Carmel Beach:** Beautiful white sand beach, perfect for a stroll.\n    *   **Mission San Carlos Borrom\u00e9o del r\u00edo Carmelo:** A historic Spanish mission.\n*   **Big Sur:** This is the heart of the coastal beauty.\n    *   **Bixby Creek Bridge:** An iconic photo opportunity.\n    *   **McWay Falls (Julia Pfeiffer Burns State Park):** A waterfall that cascades onto the beach.\n    *   **Point Reyes Lighthouse (requires a detour, but worth it for lighthouse lovers):** Dramatic views.\n    *   **Hiking trails:** Numerous options for all skill levels.\n    *   **Nepenthe:** A famous restaurant with incredible ocean views, perfect for a lunch or drink.\n*   **Hearst Castle (San Simeon):**\n    *   **Opulent Estate:** A fascinating glimpse into the life of William Randolph Hearst. Book tours in advance, as they often sell out.\n*   **Cambria:**\n    *   **Moonstone Beach:** Known for its smooth, colorful \&quot;moonstones.\&quot;\n    *   &quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.2926192626953125,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Absolutely! The drive from San Francisco to Los Angeles offers a variety of stunning scenery and charming towns. Here are some of the most popular and highly recommended stops, depending on your interests and how much time you have:\n\n**The Classic Coastal Route (Highway 1 - the most scenic, but can be slower):**\n\nThis is the iconic drive for a reason! Expect breathtaking ocean views, dramatic cliffs, and charming seaside towns. Be aware that sections of Highway 1 can be prone to closures due to landslides, so always check road conditions before you go (Caltrans is your friend!).\n\n*   **Monterey:**\n    *   **Monterey Bay Aquarium:** World-renowned and a must-visit. Plan for at least 2-3 hours.\n    *   **Cannery Row:** Historic waterfront street, now filled with shops, restaurants, and hotels.\n    *   **Old Fisherman&#x27;s Wharf:** Great for whale watching tours, seafood, and souvenirs.\n    *   **17-Mile Drive (Pebble Beach):** A private toll road with stunning coastal scenery, iconic golf courses, and the Lone Cypress.\n*   **Carmel-by-the-Sea:**\n    *   **Charming Village:** Wander through art galleries, boutiques, and quaint cottages.\n    *   **Carmel Beach:** Beautiful white sand beach, perfect for a stroll.\n    *   **Mission San Carlos Borrom\u00e9o del r\u00edo Carmelo:** A historic Spanish mission.\n*   **Big Sur:** This is the heart of the coastal beauty.\n    *   **Bixby Creek Bridge:** An iconic photo opportunity.\n    *   **McWay Falls (Julia Pfeiffer Burns State Park):** A waterfall that cascades onto the beach.\n    *   **Point Reyes Lighthouse (requires a detour, but worth it for lighthouse lovers):** Dramatic views.\n    *   **Hiking trails:** Numerous options for all skill levels.\n    *   **Nepenthe:** A famous restaurant with incredible ocean views, perfect for a lunch or drink.\n*   **Hearst Castle (San Simeon):**\n    *   **Opulent Estate:** A fascinating glimpse into the life of William Randolph Hearst. Book tours in advance, as they often sell out.\n*   **Cambria:**\n    *   **Moonstone Beach:** Known for its smooth, colorful \&quot;moonstones.\&quot;\n    *   &quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;MAX_TOKENS&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:45.059845Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash-lite&quot;,
    &quot;responseId&quot;: &quot;1QvxacXTA6iaq8YP8M2gkAc&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 500,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 500
        }
      ],
      &quot;promptTokenCount&quot;: 64,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 64
        }
      ],
      &quot;totalTokenCount&quot;: 564,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash-lite&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-2.5-flash-lite&quot;,
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
    &quot;text&quot;: &quot;The air in the cramped apartment hung thick with the scent of stale cigarettes and something vaguely floral, a cloying perfume that did little to mask the metallic tang of dried blood. Detective Miles Corbin, a man whose trench coat seemed permanently etched with the grime of a thousand city streets, surveyed the scene with weary eyes. Another Tuesday, another victim. But this one, a young woman named Clara Bellweather, had left behind more than just a messy end to her life.\n\nMiles knelt beside the overturned coffee table, its polished surface marred by a dark, sticky stain. He\u2019d seen plenty of overturned furniture, plenty of blood. What made him pause, what pricked at his seasoned detective\u2019s intuition, was the object nestled amidst the shattered ceramic mug and scattered papers. It was a single, perfectly preserved peacock feather.\n\nNot just any feather, either. This one shimmered with an iridescent blues and greens, its eye a mesmerizing swirl of sapphire and emerald. It was impossibly vibrant, almost glowing against the drab carpet. Miles had seen exotic pets, he\u2019d even seen a crime scene once that involved a boa constrictor, but never, in all his years, had he encountered a peacock feather at a homicide. And not just a stray one, mind you. This looked\u2026placed. Deliberately. As if the killer, in their haste or their madness, had left behind a calling card of pure, unadulterated strangeness.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.5958368333719545,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The air in the cramped apartment hung thick with the scent of stale cigarettes and something vaguely floral, a cloying perfume that did little to mask the metallic tang of dried blood. Detective Miles Corbin, a man whose trench coat seemed permanently etched with the grime of a thousand city streets, surveyed the scene with weary eyes. Another Tuesday, another victim. But this one, a young woman named Clara Bellweather, had left behind more than just a messy end to her life.\n\nMiles knelt beside the overturned coffee table, its polished surface marred by a dark, sticky stain. He\u2019d seen plenty of overturned furniture, plenty of blood. What made him pause, what pricked at his seasoned detective\u2019s intuition, was the object nestled amidst the shattered ceramic mug and scattered papers. It was a single, perfectly preserved peacock feather.\n\nNot just any feather, either. This one shimmered with an iridescent blues and greens, its eye a mesmerizing swirl of sapphire and emerald. It was impossibly vibrant, almost glowing against the drab carpet. Miles had seen exotic pets, he\u2019d even seen a crime scene once that involved a boa constrictor, but never, in all his years, had he encountered a peacock feather at a homicide. And not just a stray one, mind you. This looked\u2026placed. Deliberately. As if the killer, in their haste or their madness, had left behind a calling card of pure, unadulterated strangeness.&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:46.279307Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-flash-lite&quot;,
    &quot;responseId&quot;: &quot;1gvxaYuGEZafq8YP873hkQQ&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 295,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 295
        }
      ],
      &quot;promptTokenCount&quot;: 13,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 13
        }
      ],
      &quot;totalTokenCount&quot;: 308,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-flash-lite&#x27;,
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
  &quot;model&quot;: &quot;google/gemini-2.5-flash-lite&quot;,
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

- [Input schema](/ai/models/google/gemini-2.5-flash-lite/schema-input.json)
- [Output schema](/ai/models/google/gemini-2.5-flash-lite/schema-output.json)

