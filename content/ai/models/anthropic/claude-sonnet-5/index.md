---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/
  description: anthropic/claude-sonnet-5
  full_title: Claude Sonnet 5 · Cloudflare AI docs
  head_html: <title>Claude Sonnet 5 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="anthropic/claude-sonnet-5"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Claude Sonnet 5 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="anthropic/claude-sonnet-5"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/#page","headline":"Claude Sonnet 5 \u00b7 Cloudflare AI docs","description":"anthropic/claude-sonnet-5","url":"https://developers.cloudflare.com/ai/models/anthropic/claude-sonnet-5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/anthropic/claude-sonnet-5/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/anthropic.svg" alt="Anthropic logo" width="48" height="48">

<h1 id="claude-sonnet-5">Claude Sonnet 5</h1>

<p><code>anthropic/claude-sonnet-5</code></p>

Claude Sonnet 5 is Anthropic's most agentic Sonnet model yet, built for coding, tool use, reasoning, and long-horizon professional work at lower cost than Opus-class models.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://www.anthropic.com/legal/commercial-terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 10, Cached input tokens (per 1M): 0.2, Cache creation tokens (per 1M): 2.5</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic message request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic message request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 1024,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What are the three laws of thermodynamics?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;# The Three (Four) Laws of Thermodynamics\n\nHere are the fundamental laws, typically numbered 1-3 (with a \&quot;Zeroth Law\&quot; often included as foundational):\n\n## Zeroth Law\n**If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.**\n- This establishes the concept of temperature as a measurable property.\n\n## First Law (Conservation of Energy)\n**Energy cannot be created or destroyed, only transformed or transferred.**\n- Often expressed as: \u0394U = Q \u2212 W\n- (Change in internal energy = Heat added \u2212 Work done by the system)\n- This means the total energy of an isolated system remains constant.\n\n## Second Law (Entropy)\n**The total entropy of an isolated system can never decrease over time; it tends to increase or remain constant.**\n- Heat flows spontaneously from hot to cold objects, not the reverse.\n- This law explains why certain processes are irreversible and establishes the \&quot;arrow of time.\&quot;\n- No heat engine can be 100% efficient at converting heat into work.\n\n## Third Law\n**As the temperature of a system approaches absolute zero (0 Kelvin), the entropy of the system approaches a minimum (constant) value.**\n- Absolute zero is unattainable in a finite number of steps.\n- At absolute zero, a perfect crystal would have exactly zero entropy.\n\n---\n\n**Quick summary often used colloquially:**\n1. You can&#x27;t win (can&#x27;t get more energy out than you put in)\n2. You can&#x27;t break even (some energy is always lost as unusable heat)\n3. You can&#x27;t get out of the game (can&#x27;t reach absolute zero)&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_01RdqxfAYz2PfZTfiAYpX6Tz&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;# The Three (Four) Laws of Thermodynamics\n\nHere are the fundamental laws, typically numbered 1-3 (with a \&quot;Zeroth Law\&quot; often included as foundational):\n\n## Zeroth Law\n**If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.**\n- This establishes the concept of temperature as a measurable property.\n\n## First Law (Conservation of Energy)\n**Energy cannot be created or destroyed, only transformed or transferred.**\n- Often expressed as: \u0394U = Q \u2212 W\n- (Change in internal energy = Heat added \u2212 Work done by the system)\n- This means the total energy of an isolated system remains constant.\n\n## Second Law (Entropy)\n**The total entropy of an isolated system can never decrease over time; it tends to increase or remain constant.**\n- Heat flows spontaneously from hot to cold objects, not the reverse.\n- This law explains why certain processes are irreversible and establishes the \&quot;arrow of time.\&quot;\n- No heat engine can be 100% efficient at converting heat into work.\n\n## Third Law\n**As the temperature of a system approaches absolute zero (0 Kelvin), the entropy of the system approaches a minimum (constant) value.**\n- Absolute zero is unattainable in a finite number of steps.\n- At absolute zero, a perfect crystal would have exactly zero entropy.\n\n---\n\n**Quick summary often used colloquially:**\n1. You can&#x27;t win (can&#x27;t get more energy out than you put in)\n2. You can&#x27;t break even (some energy is always lost as unusable heat)\n3. You can&#x27;t get out of the game (can&#x27;t reach absolute zero)&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-sonnet-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 20,
      &quot;output_tokens&quot;: 539
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-sonnet-5&#x27;,
  {
    max_tokens: 1024,
    messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;anthropic/claude-sonnet-5&quot;,
  &quot;max_tokens&quot;: 1024,
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
    &quot;max_tokens&quot;: 1024,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;How do I read a JSON file in Python?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;system&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;# Reading a JSON File in Python\n\nPython&#x27;s built-in `json` module makes this straightforward.\n\n## Basic Example\n\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\n## Explanation\n\n- **`json.load(file)`** \u2014 reads from a file object and parses JSON into Python objects\n- **`json.loads(string)`** \u2014 use this instead if you have a JSON *string* (not a file) to parse\n\n## Example with Sample Data\n\nSuppose `data.json` contains:\n\n```json\n{\n    \&quot;name\&quot;: \&quot;Alice\&quot;,\n    \&quot;age\&quot;: 30,\n    \&quot;skills\&quot;: [\&quot;Python\&quot;, \&quot;SQL\&quot;]\n}\n```\n\nYou can read and use it like this:\n\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\nprint(data[&#x27;name&#x27;])      # Alice\nprint(data[&#x27;skills&#x27;])    # [&#x27;Python&#x27;, &#x27;SQL&#x27;]\n```\n\n## Handling Errors\n\nIt&#x27;s good practice to handle common issues like missing files or invalid JSON:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Invalid JSON format.\&quot;)\n```\n\n## Reading JSON from a String\n\nIf your JSON is already a string in memory:\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Bob\&quot;, \&quot;age\&quot;: 25}&#x27;\ndata = json.loads(json_string)\nprint(data[&#x27;name&#x27;])  # Bob\n```\n\n## Key Type Mappings\n\n| JSON Type | Python Type |\n|-----------|-------------|\n| object    | dict        |\n| array     | list        |\n| string    | str         |\n| number    | int / float |\n| true/false| bool        |\n| null      | None        |\n\nThat covers the essentials \u2014 let me know if you need help with nested data, writing JSON, or working with large files.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_01PptUvPAdU3SPQLQPwG7G3s&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;# Reading a JSON File in Python\n\nPython&#x27;s built-in `json` module makes this straightforward.\n\n## Basic Example\n\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\n## Explanation\n\n- **`json.load(file)`** \u2014 reads from a file object and parses JSON into Python objects\n- **`json.loads(string)`** \u2014 use this instead if you have a JSON *string* (not a file) to parse\n\n## Example with Sample Data\n\nSuppose `data.json` contains:\n\n```json\n{\n    \&quot;name\&quot;: \&quot;Alice\&quot;,\n    \&quot;age\&quot;: 30,\n    \&quot;skills\&quot;: [\&quot;Python\&quot;, \&quot;SQL\&quot;]\n}\n```\n\nYou can read and use it like this:\n\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\nprint(data[&#x27;name&#x27;])      # Alice\nprint(data[&#x27;skills&#x27;])    # [&#x27;Python&#x27;, &#x27;SQL&#x27;]\n```\n\n## Handling Errors\n\nIt&#x27;s good practice to handle common issues like missing files or invalid JSON:\n\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;) as file:\n        data = json.load(file)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Invalid JSON format.\&quot;)\n```\n\n## Reading JSON from a String\n\nIf your JSON is already a string in memory:\n\n```python\nimport json\n\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Bob\&quot;, \&quot;age\&quot;: 25}&#x27;\ndata = json.loads(json_string)\nprint(data[&#x27;name&#x27;])  # Bob\n```\n\n## Key Type Mappings\n\n| JSON Type | Python Type |\n|-----------|-------------|\n| object    | dict        |\n| array     | list        |\n| string    | str         |\n| number    | int / float |\n| true/false| bool        |\n| null      | None        |\n\nThat covers the essentials \u2014 let me know if you need help with nested data, writing JSON, or working with large files.&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-sonnet-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 38,
      &quot;output_tokens&quot;: 609
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-sonnet-5&#x27;,
  {
    max_tokens: 1024,
    messages: [{ content: &#x27;How do I read a JSON file in Python?&#x27;, role: &#x27;user&#x27; }],
    system: &#x27;You are a helpful coding assistant specializing in Python.&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;anthropic/claude-sonnet-5&quot;,
  &quot;max_tokens&quot;: 1024,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;How do I read a JSON file in Python?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;system&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Creative Writing with High Effort</strong>
<p>Use adaptive thinking with high effort for deeper reasoning.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 2048,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;output_config&quot;: {
      &quot;effort&quot;: &quot;high&quot;
    },
    &quot;thinking&quot;: {
      &quot;type&quot;: &quot;adaptive&quot;
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Detective Mara Voss crouched beside the overturned chair, careful not to let her coat brush the chalk outline still drying on the hardwood floor. The apartment smelled of lavender and something underneath it\u2014copper, sharp and unmistakable.\n\n\&quot;You seeing this?\&quot; she called to her partner, Reyes, who was photographing the bookshelf.\n\nHe crossed the room, careful of the evidence markers scattered like yellow teeth across the carpet. Mara pointed at the small object resting in the dead man&#x27;s open palm: a single playing card, the seven of diamonds, except where the diamonds should have been, someone had drawn seven tiny, perfect spirals in red ink.\n\n\&quot;Could be nothing,\&quot; Reyes said, though his voice suggested he didn&#x27;t believe it.\n\n\&quot;Could be.\&quot; Mara pulled an evidence bag from her pocket but didn&#x27;t reach for the card yet. Something about it held her still. The spirals weren&#x27;t random\u2014she&#x27;d seen that pattern before, scratched into the doorframe of a cold case file she&#x27;d inherited three years ago. A case that had never made sense, that had kept her awake on more nights than she cared to admit.\n\n\&quot;Mara?\&quot;\n\nShe blinked, realized she&#x27;d been staring. \&quot;This isn&#x27;t our first body with this signature,\&quot; she said quietly. \&quot;I just didn&#x27;t know there&#x27;d be a second.\&quot;\n\nOutside, rain began to tap against the window, and somewhere in the building, a door clicked shut\u2014soft, deliberate, like someone had been listening.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_01DACMFVHe3JbaQREntjsDuc&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Detective Mara Voss crouched beside the overturned chair, careful not to let her coat brush the chalk outline still drying on the hardwood floor. The apartment smelled of lavender and something underneath it\u2014copper, sharp and unmistakable.\n\n\&quot;You seeing this?\&quot; she called to her partner, Reyes, who was photographing the bookshelf.\n\nHe crossed the room, careful of the evidence markers scattered like yellow teeth across the carpet. Mara pointed at the small object resting in the dead man&#x27;s open palm: a single playing card, the seven of diamonds, except where the diamonds should have been, someone had drawn seven tiny, perfect spirals in red ink.\n\n\&quot;Could be nothing,\&quot; Reyes said, though his voice suggested he didn&#x27;t believe it.\n\n\&quot;Could be.\&quot; Mara pulled an evidence bag from her pocket but didn&#x27;t reach for the card yet. Something about it held her still. The spirals weren&#x27;t random\u2014she&#x27;d seen that pattern before, scratched into the doorframe of a cold case file she&#x27;d inherited three years ago. A case that had never made sense, that had kept her awake on more nights than she cared to admit.\n\n\&quot;Mara?\&quot;\n\nShe blinked, realized she&#x27;d been staring. \&quot;This isn&#x27;t our first body with this signature,\&quot; she said quietly. \&quot;I just didn&#x27;t know there&#x27;d be a second.\&quot;\n\nOutside, rain began to tap against the window, and somewhere in the building, a door clicked shut\u2014soft, deliberate, like someone had been listening.&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-sonnet-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 26,
      &quot;output_tokens&quot;: 469
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-sonnet-5&#x27;,
  {
    max_tokens: 2048,
    messages: [
      {
        content: &#x27;Write a short story opening about a detective finding an unusual clue.&#x27;,
        role: &#x27;user&#x27;,
      },
    ],
    output_config: { effort: &#x27;high&#x27; },
    thinking: { type: &#x27;adaptive&#x27; },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;anthropic/claude-sonnet-5&quot;,
  &quot;max_tokens&quot;: 2048,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;output_config&quot;: {
    &quot;effort&quot;: &quot;high&quot;
  },
  &quot;thinking&quot;: {
    &quot;type&quot;: &quot;adaptive&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Streaming Response</strong>
<p>Enable streaming for real-time output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 1024,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Explain the concept of recursion with a simple example.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;stream&quot;: true
  },
  &quot;output&quot;: {
    &quot;text&quot;: [
      &quot;# Recursion&quot;,
      &quot;\n\n**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems.\n\n## Key&quot;,
      &quot; Components\n\nEvery recursive function needs:\n1. **Base case** \u2013 a condition that stops the recursion (prevents infinite loops)&quot;,
      &quot;\n2. **Recursive case** \u2013 where the function calls itself with a smaller/simpler input\n\n## Simple Example: Factorial&quot;,
      &quot;\n\nThe factorial of a number `n` (written `n!`) is the product of all positive integers up to `n`.\n\nMathematically: `5!&quot;,
      &quot; = 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 = 120`\n\nThis can be defined recursively as:\n```\nn! = n \u00d7 (n&quot;,
      &quot;-1)!\n0! = 1  (base case)\n```\n\n### Code Example (Python)\n\n```python\ndef factorial(n):\n    # Base case&quot;,
      &quot;\n    if n == 0:\n        return 1\n    # Recursive case\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(5))  # Output: 120\n```\n\n###&quot;,
      &quot; How It Works (Step-by-Step)\n\n```\nfactorial(5)\n= 5 * factorial(4)\n= 5 * (4 * factorial(3))\n=&quot;,
      &quot; 5 * (4 * (3 * factorial(2)))\n= 5 * (4 * (3 * (2 * factorial(1))))\n= 5 * (4 * (3 * (2 * (1&quot;,
      &quot; * factorial(0)))))\n= 5 * (4 * (3 * (2 * (1 * 1))))\n= 120\n```\n\nThe function keeps calling itself with smaller values&quot;,
      &quot; until it hits the **base case** (`n == 0`), then the results \&quot;unwind\&quot; back up, multiplying together to produ&quot;,
      &quot;ce the final answer.\n\n## Why Use Recursion?\n\n- Makes code **cleaner** for problems that&quot;,
      &quot; are naturally recursive (trees, fractals, divide-and-conquer algorithms)\n- Mirrors **&quot;,
      &quot;mathematical definitions** closely\n- Useful for problems like: tree traversal, sorting algorithms (quicksort, m&quot;,
      &quot;ergesort), the Fibonacci sequence, and navigating file systems\n\n## Caution \u26a0\ufe0f\nWithout a proper base case, recursion&quot;,
      &quot; leads to **infinite recursion** and a stack overflow error!&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;type&quot;: &quot;message_start&quot;,
      &quot;message&quot;: {
        &quot;model&quot;: &quot;claude-sonnet-5&quot;,
        &quot;id&quot;: &quot;msg_0188koTEnwXJD4cbqRcEfaCT&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;content&quot;: [],
        &quot;stop_reason&quot;: null,
        &quot;stop_sequence&quot;: null,
        &quot;stop_details&quot;: null,
        &quot;usage&quot;: {
          &quot;input_tokens&quot;: 22,
          &quot;cache_creation_input_tokens&quot;: 0,
          &quot;cache_read_input_tokens&quot;: 0,
          &quot;cache_creation&quot;: {
            &quot;ephemeral_5m_input_tokens&quot;: 0,
            &quot;ephemeral_1h_input_tokens&quot;: 0
          },
          &quot;output_tokens&quot;: 6,
          &quot;service_tier&quot;: &quot;standard&quot;,
          &quot;inference_geo&quot;: &quot;global&quot;
        }
      }
    },
    {
      &quot;type&quot;: &quot;content_block_start&quot;,
      &quot;index&quot;: 0,
      &quot;content_block&quot;: {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;&quot;
      }
    },
    {
      &quot;type&quot;: &quot;ping&quot;
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;# Recursion&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;\n\n**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems.\n\n## Key&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; Components\n\nEvery recursive function needs:\n1. **Base case** \u2013 a condition that stops the recursion (prevents infinite loops)&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;\n2. **Recursive case** \u2013 where the function calls itself with a smaller/simpler input\n\n## Simple Example: Factorial&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;\n\nThe factorial of a number `n` (written `n!`) is the product of all positive integers up to `n`.\n\nMathematically: `5!&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; = 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 = 120`\n\nThis can be defined recursively as:\n```\nn! = n \u00d7 (n&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;-1)!\n0! = 1  (base case)\n```\n\n### Code Example (Python)\n\n```python\ndef factorial(n):\n    # Base case&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;\n    if n == 0:\n        return 1\n    # Recursive case\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(5))  # Output: 120\n```\n\n###&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; How It Works (Step-by-Step)\n\n```\nfactorial(5)\n= 5 * factorial(4)\n= 5 * (4 * factorial(3))\n=&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; 5 * (4 * (3 * factorial(2)))\n= 5 * (4 * (3 * (2 * factorial(1))))\n= 5 * (4 * (3 * (2 * (1&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; * factorial(0)))))\n= 5 * (4 * (3 * (2 * (1 * 1))))\n= 120\n```\n\nThe function keeps calling itself with smaller values&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; until it hits the **base case** (`n == 0`), then the results \&quot;unwind\&quot; back up, multiplying together to produ&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;ce the final answer.\n\n## Why Use Recursion?\n\n- Makes code **cleaner** for problems that&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; are naturally recursive (trees, fractals, divide-and-conquer algorithms)\n- Mirrors **&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;mathematical definitions** closely\n- Useful for problems like: tree traversal, sorting algorithms (quicksort, m&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;ergesort), the Fibonacci sequence, and navigating file systems\n\n## Caution \u26a0\ufe0f\nWithout a proper base case, recursion&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; leads to **infinite recursion** and a stack overflow error!&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_stop&quot;,
      &quot;index&quot;: 0
    },
    {
      &quot;type&quot;: &quot;message_delta&quot;,
      &quot;delta&quot;: {
        &quot;stop_reason&quot;: &quot;end_turn&quot;,
        &quot;stop_sequence&quot;: null,
        &quot;stop_details&quot;: null
      },
      &quot;usage&quot;: {
        &quot;input_tokens&quot;: 22,
        &quot;cache_creation_input_tokens&quot;: 0,
        &quot;cache_read_input_tokens&quot;: 0,
        &quot;output_tokens&quot;: 708,
        &quot;output_tokens_details&quot;: {
          &quot;thinking_tokens&quot;: 0
        }
      }
    },
    {
      &quot;type&quot;: &quot;message_stop&quot;
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-sonnet-5&#x27;,
  {
    max_tokens: 1024,
    messages: [{ content: &#x27;Explain the concept of recursion with a simple example.&#x27;, role: &#x27;user&#x27; }],
    stream: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;anthropic/claude-sonnet-5&quot;,
  &quot;max_tokens&quot;: 1024,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Explain the concept of recursion with a simple example.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;stream&quot;: true
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: user, assistant</td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>system</code></td><td>string</td><td></td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>metadata</code></td><td>object</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content</code></td><td>array</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].text</code></td><td>string</td><td></td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>stop_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td>Required.</td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/anthropic/claude-sonnet-5/schema-input.json)
- [Output schema](/ai/models/anthropic/claude-sonnet-5/schema-output.json)

