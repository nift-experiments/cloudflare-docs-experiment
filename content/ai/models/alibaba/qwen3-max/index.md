---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/alibaba/qwen3-max/
  description: alibaba/qwen3-max
  full_title: Qwen 3 Max · Cloudflare AI docs
  head_html: <title>Qwen 3 Max · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="alibaba/qwen3-max"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/alibaba/qwen3-max/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Qwen 3 Max · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="alibaba/qwen3-max"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/alibaba/qwen3-max/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/alibaba/qwen3-max/#page","headline":"Qwen 3 Max \u00b7 Cloudflare AI docs","description":"alibaba/qwen3-max","url":"https://developers.cloudflare.com/ai/models/alibaba/qwen3-max/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/alibaba/qwen3-max/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="qwen-3-max">Qwen 3 Max</h1>

<p><code>alibaba/qwen3-max</code></p>

Alibaba's Qwen 3 Max is a large language model with strong coding, reasoning, and multilingual capabilities, served via DashScope's OpenAI-compatible endpoint.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 1.2, Output tokens (per 1M): 6</td></tr>
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
    &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental principles that describe the behavior of energy and entropy in physical systems:\n\n1. **Zeroth Law of Thermodynamics**:  \n   *If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other.*  \n   This law establishes the concept of temperature and justifies the use of thermometers.\n\n2. **First Law of Thermodynamics** (Law of Energy Conservation):  \n   *Energy cannot be created or destroyed in an isolated system; it can only change forms.*  \n   Mathematically, this is often expressed as:  \n   \\[\n   \\Delta U = Q - W\n   \\]  \n   where \\(\\Delta U\\) is the change in internal energy of the system, \\(Q\\) is the heat added to the system, and \\(W\\) is the work done by the system.\n\n3. **Second Law of Thermodynamics**:  \n   *The total entropy of an isolated system can never decrease over time; it either increases or remains constant in ideal reversible processes.*  \n   This law introduces the concept of irreversibility and explains why certain processes occur spontaneously in one direction (e.g., heat flows from hot to cold).\n\nThere is also a **Third Law of Thermodynamics**, which is sometimes included as the fourth in historical contexts but is now standardly recognized as the third:\n\n4. **Third Law of Thermodynamics**:  \n   *As the temperature of a system approaches absolute zero, the entropy of the system approaches a constant minimum value.*  \n   In practical terms, it implies that absolute zero (0 K) cannot be reached in a finite number of steps.\n\nSo, while commonly referred to as \u201cthree laws,\u201d modern physics includes **four**\u2014with the Zeroth Law added later for logical completeness, even though it was formulated after the first three.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;The three laws of thermodynamics are fundamental principles that describe the behavior of energy and entropy in physical systems:\n\n1. **Zeroth Law of Thermodynamics**:  \n   *If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other.*  \n   This law establishes the concept of temperature and justifies the use of thermometers.\n\n2. **First Law of Thermodynamics** (Law of Energy Conservation):  \n   *Energy cannot be created or destroyed in an isolated system; it can only change forms.*  \n   Mathematically, this is often expressed as:  \n   \\[\n   \\Delta U = Q - W\n   \\]  \n   where \\(\\Delta U\\) is the change in internal energy of the system, \\(Q\\) is the heat added to the system, and \\(W\\) is the work done by the system.\n\n3. **Second Law of Thermodynamics**:  \n   *The total entropy of an isolated system can never decrease over time; it either increases or remains constant in ideal reversible processes.*  \n   This law introduces the concept of irreversibility and explains why certain processes occur spontaneously in one direction (e.g., heat flows from hot to cold).\n\nThere is also a **Third Law of Thermodynamics**, which is sometimes included as the fourth in historical contexts but is now standardly recognized as the third:\n\n4. **Third Law of Thermodynamics**:  \n   *As the temperature of a system approaches absolute zero, the entropy of the system approaches a constant minimum value.*  \n   In practical terms, it implies that absolute zero (0 K) cannot be reached in a finite number of steps.\n\nSo, while commonly referred to as \u201cthree laws,\u201d modern physics includes **four**\u2014with the Zeroth Law added later for logical completeness, even though it was formulated after the first three.&quot;,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776471062,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-1cc68967-fae9-9f2f-aa72-ec0674038c0a&quot;,
    &quot;model&quot;: &quot;qwen3-max&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 375,
      &quot;prompt_tokens&quot;: 17,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 392
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3-max&#x27;,
  { messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/qwen3-max&quot;,
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
    &quot;text&quot;: &quot;To read a JSON file in Python, you can use the built-in `json` module. Here&#x27;s the basic approach:\n\n## Basic Example\n\n```python\nimport json\n\n# Read JSON file\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\n# Now you can work with your data\nprint(data)\n```\n\n## Step-by-step breakdown:\n\n1. **Import the json module**: `import json`\n2. **Open the file**: Use `open()` with mode `&#x27;r&#x27;` (read mode)\n3. **Parse the JSON**: Use `json.load()` to parse the file content into Python objects\n4. **Use context manager**: The `with` statement automatically closes the file when done\n\n## Common Data Types After Loading\n\nJSON data gets converted to these Python types:\n- JSON object \u2192 Python dictionary (`dict`)\n- JSON array \u2192 Python list (`list`)\n- JSON string \u2192 Python string (`str`)\n- JSON number \u2192 Python int or float\n- JSON boolean \u2192 Python `True` or `False`\n- JSON null \u2192 Python `None`\n\n## Example with Error Handling\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\n    print(\&quot;Data loaded successfully!\&quot;)\n    print(data)\nexcept FileNotFoundError:\n    print(\&quot;File not found!\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Invalid JSON format!\&quot;)\n```\n\n## Reading JSON from a String\n\nIf you have JSON as a string (not a file), use `json.loads()` instead:\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\nprint(data)  # {&#x27;name&#x27;: &#x27;Alice&#x27;, &#x27;age&#x27;: 30}\n```\n\n## Specifying Encoding (if needed)\n\nFor files with non-UTF-8 encoding:\n\n```python\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n    data = json.load(file)\n```\n\nThe `json.load()` function handles UTF-8 by default, so you usually don&#x27;t need to specify encoding unless you&#x27;re dealing with a different character encoding.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;To read a JSON file in Python, you can use the built-in `json` module. Here&#x27;s the basic approach:\n\n## Basic Example\n\n```python\nimport json\n\n# Read JSON file\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\n# Now you can work with your data\nprint(data)\n```\n\n## Step-by-step breakdown:\n\n1. **Import the json module**: `import json`\n2. **Open the file**: Use `open()` with mode `&#x27;r&#x27;` (read mode)\n3. **Parse the JSON**: Use `json.load()` to parse the file content into Python objects\n4. **Use context manager**: The `with` statement automatically closes the file when done\n\n## Common Data Types After Loading\n\nJSON data gets converted to these Python types:\n- JSON object \u2192 Python dictionary (`dict`)\n- JSON array \u2192 Python list (`list`)\n- JSON string \u2192 Python string (`str`)\n- JSON number \u2192 Python int or float\n- JSON boolean \u2192 Python `True` or `False`\n- JSON null \u2192 Python `None`\n\n## Example with Error Handling\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\n    print(\&quot;Data loaded successfully!\&quot;)\n    print(data)\nexcept FileNotFoundError:\n    print(\&quot;File not found!\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Invalid JSON format!\&quot;)\n```\n\n## Reading JSON from a String\n\nIf you have JSON as a string (not a file), use `json.loads()` instead:\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\nprint(data)  # {&#x27;name&#x27;: &#x27;Alice&#x27;, &#x27;age&#x27;: 30}\n```\n\n## Specifying Encoding (if needed)\n\nFor files with non-UTF-8 encoding:\n\n```python\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n    data = json.load(file)\n```\n\nThe `json.load()` function handles UTF-8 by default, so you usually don&#x27;t need to specify encoding unless you&#x27;re dealing with a different character encoding.&quot;,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776471064,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-ba93d05e-b778-9fe4-97f6-a2b16726e379&quot;,
    &quot;model&quot;: &quot;qwen3-max&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 449,
      &quot;prompt_tokens&quot;: 33,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 482
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3-max&#x27;,
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
  &quot;model&quot;: &quot;alibaba/qwen3-max&quot;,
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
    &quot;text&quot;: &quot;Great! The classic route from San Francisco to Los Angeles along the California coast\u2014especially **Highway 1 (Pacific Coast Highway)**\u2014is one of the most scenic drives in the world. While it takes longer than the inland I-5 freeway (about 8\u201310 hours without stops), it\u2019s absolutely worth it for the views and experiences. Here are some top places to stop, roughly ordered from north to south:\n\n### \ud83c\udf09 **Half Moon Bay**  \n- Just 30 miles south of SF  \n- Charming coastal town with beaches, tide pools, and great seafood  \n- Stop at **Pillar Point Harbor** or walk the **Coastal Trail**\n\n### \ud83c\udfde\ufe0f **Santa Cruz**  \n- Famous for its beach boardwalk (oldest in California!), surfing, and laid-back vibe  \n- Visit the **Santa Cruz Beach Boardwalk** or explore **Natural Bridges State Beach**\n\n### \ud83d\udc2c **Monterey &amp; Carmel-by-the-Sea**  \n- **Monterey**: Don\u2019t miss the world-class **Monterey Bay Aquarium** and Cannery Row  \n- **Carmel**: Quaint village with art galleries, fairytale cottages, and **Carmel Beach**  \n- Optional detour: **17-Mile Drive** through Pebble Beach (toll road with stunning ocean views)\n\n### \ud83c\udf32 **Big Sur**  \n- The crown jewel of the PCH! Dramatic cliffs, redwoods, and ocean vistas  \n- Must-stops:  \n  - **Bixby Creek Bridge** (iconic photo spot)  \n  - **McWay Falls** at Julia Pfeiffer Burns State Park (80-ft waterfall onto a beach!)  \n  - **Nepenthe** restaurant for lunch with panoramic views  \n\n&gt; \u26a0\ufe0f Note: Check road conditions before heading through Big Sur\u2014landslides occasionally close Highway 1.\n\n### \ud83c\udf77 **San Simeon**  \n- Home of **Hearst Castle**, the opulent estate of newspaper magnate William Randolph Hearst  \n- Also great for spotting **elephant seals** at the **Piedras Blancas Rookery** just north of town\n\n### \ud83c\udfd6\ufe0f **Cambria &amp; Morro Bay**  \n- **Cambria**: Cozy seaside village with unique shops and forest-meets-ocean scenery  \n- **Morro Bay**: Known for **Morro Rock**, kayaking, and fresh oysters\n\n### \ud83c\udf34 **San Luis Obispo (SLO)**  \n- A relaxed college town with a historic mission, farmers\u2019 market (Thursday nights!), and great food  \n- Nearby: **Bubblegum Alley** and **Madonna Inn** (quirky, Instagrammable hotel)\n\n### \ud83c\udfc4 **Pismo Beach**  \n- Classic Central Coast surf town with dunes and a long pier  \n- Try clam chowder\u2014it\u2019s the \u201cClam Capital of the World\u201d!\n\n### \ud83c\udf3a **Santa Barbara**  \n- \u201cThe American Riviera\u201d with Spanish architecture, palm-lined streets, and wine tasting  \n- Stroll **Stearns Wharf**, visit the **Mission Santa Barbara**, or relax on **East Beach**\n\n### \ud83c\udfd9\ufe0f **Final Stretch to Los Angeles**  \n- From Santa Barbara, you can stay on Highway 1 through **Malibu** (stop at **El Matador Beach** or **Point Dume**)  \n- Or hop on US-101 for a quicker arrival into LA\n\n---\n\n### Tips:\n- **Allow 2\u20133 days** if you want to enjoy the stops without rushing  \n- **Book lodging in advance**, especially in Big Sur, Carmel, or Santa Barbara  \n- **Fill your gas tank**\u2014some stretches (like Big Sur) have limited services  \n- **Pack layers**\u2014coastal weather changes fast, even in summer!\n\nWould you like help planning an itinerary based on how many days you have?&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;Great! The classic route from San Francisco to Los Angeles along the California coast\u2014especially **Highway 1 (Pacific Coast Highway)**\u2014is one of the most scenic drives in the world. While it takes longer than the inland I-5 freeway (about 8\u201310 hours without stops), it\u2019s absolutely worth it for the views and experiences. Here are some top places to stop, roughly ordered from north to south:\n\n### \ud83c\udf09 **Half Moon Bay**  \n- Just 30 miles south of SF  \n- Charming coastal town with beaches, tide pools, and great seafood  \n- Stop at **Pillar Point Harbor** or walk the **Coastal Trail**\n\n### \ud83c\udfde\ufe0f **Santa Cruz**  \n- Famous for its beach boardwalk (oldest in California!), surfing, and laid-back vibe  \n- Visit the **Santa Cruz Beach Boardwalk** or explore **Natural Bridges State Beach**\n\n### \ud83d\udc2c **Monterey &amp; Carmel-by-the-Sea**  \n- **Monterey**: Don\u2019t miss the world-class **Monterey Bay Aquarium** and Cannery Row  \n- **Carmel**: Quaint village with art galleries, fairytale cottages, and **Carmel Beach**  \n- Optional detour: **17-Mile Drive** through Pebble Beach (toll road with stunning ocean views)\n\n### \ud83c\udf32 **Big Sur**  \n- The crown jewel of the PCH! Dramatic cliffs, redwoods, and ocean vistas  \n- Must-stops:  \n  - **Bixby Creek Bridge** (iconic photo spot)  \n  - **McWay Falls** at Julia Pfeiffer Burns State Park (80-ft waterfall onto a beach!)  \n  - **Nepenthe** restaurant for lunch with panoramic views  \n\n&gt; \u26a0\ufe0f Note: Check road conditions before heading through Big Sur\u2014landslides occasionally close Highway 1.\n\n### \ud83c\udf77 **San Simeon**  \n- Home of **Hearst Castle**, the opulent estate of newspaper magnate William Randolph Hearst  \n- Also great for spotting **elephant seals** at the **Piedras Blancas Rookery** just north of town\n\n### \ud83c\udfd6\ufe0f **Cambria &amp; Morro Bay**  \n- **Cambria**: Cozy seaside village with unique shops and forest-meets-ocean scenery  \n- **Morro Bay**: Known for **Morro Rock**, kayaking, and fresh oysters\n\n### \ud83c\udf34 **San Luis Obispo (SLO)**  \n- A relaxed college town with a historic mission, farmers\u2019 market (Thursday nights!), and great food  \n- Nearby: **Bubblegum Alley** and **Madonna Inn** (quirky, Instagrammable hotel)\n\n### \ud83c\udfc4 **Pismo Beach**  \n- Classic Central Coast surf town with dunes and a long pier  \n- Try clam chowder\u2014it\u2019s the \u201cClam Capital of the World\u201d!\n\n### \ud83c\udf3a **Santa Barbara**  \n- \u201cThe American Riviera\u201d with Spanish architecture, palm-lined streets, and wine tasting  \n- Stroll **Stearns Wharf**, visit the **Mission Santa Barbara**, or relax on **East Beach**\n\n### \ud83c\udfd9\ufe0f **Final Stretch to Los Angeles**  \n- From Santa Barbara, you can stay on Highway 1 through **Malibu** (stop at **El Matador Beach** or **Point Dume**)  \n- Or hop on US-101 for a quicker arrival into LA\n\n---\n\n### Tips:\n- **Allow 2\u20133 days** if you want to enjoy the stops without rushing  \n- **Book lodging in advance**, especially in Big Sur, Carmel, or Santa Barbara  \n- **Fill your gas tank**\u2014some stretches (like Big Sur) have limited services  \n- **Pack layers**\u2014coastal weather changes fast, even in summer!\n\nWould you like help planning an itinerary based on how many days you have?&quot;,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776471088,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-8ebaff89-c5a7-9010-b5a4-84e5f446841a&quot;,
    &quot;model&quot;: &quot;qwen3-max&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 821,
      &quot;prompt_tokens&quot;: 81,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 902
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3-max&#x27;,
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
  &quot;model&quot;: &quot;alibaba/qwen3-max&quot;,
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
    &quot;text&quot;: &quot;Rain slicked the cobblestones of Blackwater Lane, turning the gaslight into smears of gold on wet stone. Detective Aris Thorne hunched deeper into his trench coat, the damp wool smell a familiar companion to the city\u2019s usual perfume of coal smoke and despair. Another dead end\u2014literally and figuratively\u2014in the case of the vanished heiress, Elara Vance. The alley reeked of stale beer and something sharper, metallic.\n\nThen he saw it.\n\nNestled in a puddle near a overflowing gutter, half-submerged but gleaming with unnatural clarity, was a single playing card. Not just any card. The Queen of Hearts. But this one was wrong. Horribly wrong.\n\nThe queen\u2019s face wasn\u2019t printed ink. It was *stitched*. Delicate, almost surgical sutures traced her features\u2014a crimson thread for lips, fine black silk for eyes, silver wire forming the curve of a regal brow. And where the heart symbol should be, centered on her chest, was a tiny, perfect keyhole, wrought from what looked like tarnished silver. Rainwater pooled around it, but the stitches remained unnervingly dry, as if repelling the downpour.\n\nThorne crouched, ignoring the ache in his knees and the cold seeping through his trousers. He didn\u2019t touch it. Not yet. This wasn\u2019t evidence left by accident; it was a message. A challenge. And the meticulous, chilling craftsmanship whispered of a mind far more dangerous than the common cutpurse or jealous rival he\u2019d been chasing. The rain drummed a frantic rhythm on his hat, but the only sound he truly heard was the sudden, icy thrum of his own pulse. The game, it seemed, had just changed its rules.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;Rain slicked the cobblestones of Blackwater Lane, turning the gaslight into smears of gold on wet stone. Detective Aris Thorne hunched deeper into his trench coat, the damp wool smell a familiar companion to the city\u2019s usual perfume of coal smoke and despair. Another dead end\u2014literally and figuratively\u2014in the case of the vanished heiress, Elara Vance. The alley reeked of stale beer and something sharper, metallic.\n\nThen he saw it.\n\nNestled in a puddle near a overflowing gutter, half-submerged but gleaming with unnatural clarity, was a single playing card. Not just any card. The Queen of Hearts. But this one was wrong. Horribly wrong.\n\nThe queen\u2019s face wasn\u2019t printed ink. It was *stitched*. Delicate, almost surgical sutures traced her features\u2014a crimson thread for lips, fine black silk for eyes, silver wire forming the curve of a regal brow. And where the heart symbol should be, centered on her chest, was a tiny, perfect keyhole, wrought from what looked like tarnished silver. Rainwater pooled around it, but the stitches remained unnervingly dry, as if repelling the downpour.\n\nThorne crouched, ignoring the ache in his knees and the cold seeping through his trousers. He didn\u2019t touch it. Not yet. This wasn\u2019t evidence left by accident; it was a message. A challenge. And the meticulous, chilling craftsmanship whispered of a mind far more dangerous than the common cutpurse or jealous rival he\u2019d been chasing. The rain drummed a frantic rhythm on his hat, but the only sound he truly heard was the sudden, icy thrum of his own pulse. The game, it seemed, had just changed its rules.&quot;,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1776471079,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-7bdc3457-d069-92c5-9ea0-0f1c3987d776&quot;,
    &quot;model&quot;: &quot;qwen3-max&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 362,
      &quot;prompt_tokens&quot;: 21,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 383
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3-max&#x27;,
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
  &quot;model&quot;: &quot;alibaba/qwen3-max&quot;,
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
      &quot;Recursion**&quot;,
      &quot; is a programming technique where a&quot;,
      &quot; function calls itself to solve a problem&quot;,
      &quot; by breaking it down into smaller,&quot;,
      &quot; similar subproblems.\n\n##&quot;,
      &quot; Key Components of Recursion&quot;,
      &quot;\n\n1. **Base case&quot;,
      &quot;**: A condition that stops&quot;,
      &quot; the recursion (prevents&quot;,
      &quot; infinite loops)\n2.&quot;,
      &quot; **Recursive case**: The&quot;,
      &quot; function calls itself with modified&quot;,
      &quot; arguments that move toward the&quot;,
      &quot; base case\n\n## Simple&quot;,
      &quot; Example: Calculating Factor&quot;,
      &quot;ial\n\nThe factorial of a&quot;,
      &quot; number `n` (&quot;,
      &quot;written as `n!`)&quot;,
      &quot; is the product of all positive&quot;,
      &quot; integers from 1 to n&quot;,
      &quot;.\n- 5! =&quot;,
      &quot; 5 \u00d7 4 \u00d7&quot;,
      &quot; 3 \u00d7 2 \u00d7&quot;,
      &quot; 1 = 12&quot;,
      &quot;0\n- By definition:&quot;,
      &quot; 0! = 1&quot;,
      &quot;\n\n### Recursive Implementation\n\n```python&quot;,
      &quot;\ndef factorial(n):\n   &quot;,
      &quot; # Base case: stop&quot;,
      &quot; when n is 0 or&quot;,
      &quot; 1\n    if n&quot;,
      &quot; &lt;= 1:\n        return &quot;,
      &quot;1\n    \n    # Recursive&quot;,
      &quot; case: n! = n&quot;,
      &quot; \u00d7 (n-1)!\n&quot;,
      &quot;    return n * factorial(n&quot;,
      &quot; - 1)\n\n# Example usage&quot;,
      &quot;\nprint(factorial(5&quot;,
      &quot;))  # Output: &quot;,
      &quot;120\n```\n\n&quot;,
      &quot;### How it works step by&quot;,
      &quot; step:\n\n```\nfactorial&quot;,
      &quot;(5)\n\u251c\u2500\u2500 &quot;,
      &quot;5 * factorial(4&quot;,
      &quot;)\n    \u251c\u2500\u2500 4&quot;,
      &quot; * factorial(3)\n       &quot;,
      &quot; \u251c\u2500\u2500 3 * factorial(&quot;,
      &quot;2)\n            \u251c\u2500\u2500 2&quot;,
      &quot; * factorial(1)\n               &quot;,
      &quot; \u2514\u2500\u2500 returns 1 (&quot;,
      &quot;base case)\n            \u2514&quot;,
      &quot;\u2500\u2500 returns 2 * &quot;,
      &quot;1 = 2\n       &quot;,
      &quot; \u2514\u2500\u2500 returns 3&quot;,
      &quot; * 2 = 6&quot;,
      &quot;\n    \u2514\u2500\u2500 returns&quot;,
      &quot; 4 * 6 =&quot;,
      &quot; 24\n\u2514&quot;,
      &quot;\u2500\u2500 returns 5 * &quot;,
      &quot;24 = 12&quot;,
      &quot;0\n```\n\n## Why&quot;,
      &quot; Recursion Works\n\nEach&quot;,
      &quot; recursive call works on a **&quot;,
      &quot;smaller version** of the&quot;,
      &quot; original problem until it reaches&quot;,
      &quot; the simplest case (base case).&quot;,
      &quot; Then, the results bubble&quot;,
      &quot; back up to build the final&quot;,
      &quot; answer.\n\n**Important**: Always&quot;,
      &quot; ensure your recursive function has a proper&quot;,
      &quot; base case, otherwise it&quot;,
      &quot; will run infinitely and cause a&quot;,
      &quot; stack overflow error!&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;role&quot;: &quot;assistant&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
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
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Recursion**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is a programming technique where a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function calls itself to solve a problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; by breaking it down into smaller,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; similar subproblems.\n\n##&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Key Components of Recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\n1. **Base case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**: A condition that stops&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the recursion (prevents&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; infinite loops)\n2.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **Recursive case**: The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function calls itself with modified&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; arguments that move toward the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base case\n\n## Simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Example: Calculating Factor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial\n\nThe factorial of a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; number `n` (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;written as `n!`)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is the product of all positive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; integers from 1 to n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n- 5! =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 5 \u00d7 4 \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 3 \u00d7 2 \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 1 = 12&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0\n- By definition:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 0! = 1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\n### Recursive Implementation\n\n```python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\ndef factorial(n):\n   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; # Base case: stop&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; when n is 0 or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 1\n    if n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &lt;= 1:\n        return &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1\n    \n    # Recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case: n! = n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7 (n-1)!\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;    return n * factorial(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; - 1)\n\n# Example usage&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\nprint(factorial(5&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;))  # Output: &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;120\n```\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;### How it works step by&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; step:\n\n```\nfactorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(5)\n\u251c\u2500\u2500 &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5 * factorial(4&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n    \u251c\u2500\u2500 4&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; * factorial(3)\n       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u251c\u2500\u2500 3 * factorial(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2)\n            \u251c\u2500\u2500 2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; * factorial(1)\n               &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2514\u2500\u2500 returns 1 (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base case)\n            \u2514&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\u2500\u2500 returns 2 * &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1 = 2\n       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2514\u2500\u2500 returns 3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; * 2 = 6&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n    \u2514\u2500\u2500 returns&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 4 * 6 =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 24\n\u2514&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\u2500\u2500 returns 5 * &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;24 = 12&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0\n```\n\n## Why&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Recursion Works\n\nEach&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive call works on a **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;smaller version** of the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; original problem until it reaches&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the simplest case (base case).&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Then, the results bubble&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; back up to build the final&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; answer.\n\n**Important**: Always&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ensure your recursive function has a proper&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base case, otherwise it&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; will run infinitely and cause a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stack overflow error!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;
          },
          &quot;finish_reason&quot;: &quot;stop&quot;,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [],
      &quot;created&quot;: 1776471081,
      &quot;id&quot;: &quot;chatcmpl-269e4881-6d79-91da-ad5b-a5d16443cade&quot;,
      &quot;model&quot;: &quot;qwen3-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: null,
      &quot;usage&quot;: {
        &quot;completion_tokens&quot;: 422,
        &quot;prompt_tokens&quot;: 19,
        &quot;prompt_tokens_details&quot;: {
          &quot;cached_tokens&quot;: 0
        },
        &quot;total_tokens&quot;: 441
      }
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3-max&#x27;,
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
  &quot;model&quot;: &quot;alibaba/qwen3-max&quot;,
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
<p>Letting Qwen use DashScope's built-in web search via enable_search</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;enable_search&quot;: true,
    &quot;max_tokens&quot;: 4096,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What were the top news stories about Cloudflare this week? Summarise in three bullets.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;As of the week ending June 23, 2026, the top Cloudflare news stories include:\n\n- **Acquisition of VoidZero**: On June 4, 2026, Cloudflare announced it acquired VoidZero to accelerate development of the AI-native web, enhancing its platform for next-generation agentic applications.\n\n- **Secure Sandboxes for Claude Managed Agents**: On May 19, 2026, Cloudflare introduced secure, scalable sandboxes integrated with Anthropic\u2019s Claude Managed Agents, strengthening runtime security for AI agents\u2014a key update still resonating in early June coverage.\n\n- **Industry Recognition and Strategic Momentum**: Throughout June, Cloudflare continued to be highlighted as a Leader in Edge Development Platforms (per an independent research firm report on May 5, widely cited in June) and maintained media visibility through its ongoing \u201cAgents Week 2026\u201d initiatives, reinforcing its position at the forefront of agentic AI infrastructure.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-5860fcba-c7bc-9e5e-afd8-d32376b5a423&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1782161284,
    &quot;model&quot;: &quot;qwen3-max&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;As of the week ending June 23, 2026, the top Cloudflare news stories include:\n\n- **Acquisition of VoidZero**: On June 4, 2026, Cloudflare announced it acquired VoidZero to accelerate development of the AI-native web, enhancing its platform for next-generation agentic applications.\n\n- **Secure Sandboxes for Claude Managed Agents**: On May 19, 2026, Cloudflare introduced secure, scalable sandboxes integrated with Anthropic\u2019s Claude Managed Agents, strengthening runtime security for AI agents\u2014a key update still resonating in early June coverage.\n\n- **Industry Recognition and Strategic Momentum**: Throughout June, Cloudflare continued to be highlighted as a Leader in Edge Development Platforms (per an independent research firm report on May 5, widely cited in June) and maintained media visibility through its ongoing \u201cAgents Week 2026\u201d initiatives, reinforcing its position at the forefront of agentic AI infrastructure.&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;logprobs&quot;: null
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 3589,
      &quot;completion_tokens&quot;: 196,
      &quot;total_tokens&quot;: 3785,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      }
    },
    &quot;system_fingerprint&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3-max&#x27;,
  {
    enable_search: true,
    max_tokens: 4096,
    messages: [
      {
        content:
          &#x27;What were the top news stories about Cloudflare this week? Summarise in three bullets.&#x27;,
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
  &quot;model&quot;: &quot;alibaba/qwen3-max&quot;,
  &quot;enable_search&quot;: true,
  &quot;max_tokens&quot;: 4096,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What were the top news stories about Cloudflare this week? Summarise in three bullets.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/qwen3-max/schema-input.json)
- [Output schema](/ai/models/alibaba/qwen3-max/schema-output.json)

