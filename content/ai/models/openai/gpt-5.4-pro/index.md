---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/openai/gpt-5.4-pro/
  description: openai/gpt-5.4-pro
  full_title: GPT-5.4 pro · Cloudflare AI docs
  head_html: <title>GPT-5.4 pro · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="openai/gpt-5.4-pro"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/openai/gpt-5.4-pro/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="GPT-5.4 pro · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="openai/gpt-5.4-pro"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/openai/gpt-5.4-pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/openai/gpt-5.4-pro/#page","headline":"GPT-5.4 pro \u00b7 Cloudflare AI docs","description":"openai/gpt-5.4-pro","url":"https://developers.cloudflare.com/ai/models/openai/gpt-5.4-pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/openai/gpt-5.4-pro/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-5-4-pro">GPT-5.4 pro</h1>

<p><code>openai/gpt-5.4-pro</code></p>

GPT-5.4 pro uses OpenAI's Responses API with built-in tools, improved reasoning, and stateful context management.

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
    &quot;text&quot;: &quot;The **three laws of thermodynamics** usually mean:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed, only transferred or transformed.  \n   - In thermodynamics: the change in a system\u2019s internal energy equals heat added to the system minus work done by the system.\n\n2. **Second Law \u2014 Entropy Increases**  \n   In any natural process, the total entropy of an isolated system tends to increase.  \n   - This means energy spontaneously spreads out, and no heat engine can be 100% efficient.\n   - Heat naturally flows from hot objects to cold ones, not the reverse without input of work.\n\n3. **Third Law \u2014 Entropy at Absolute Zero**  \n   As temperature approaches **absolute zero** (0 K), the entropy of a perfect crystal approaches zero.  \n   - A consequence is that absolute zero cannot be reached in a finite number of steps.\n\nSmall note: thermodynamics also has a **Zeroth Law**, which is often listed before these:\n- If system A is in thermal equilibrium with B, and B is in thermal equilibrium with C, then A is in thermal equilibrium with C.  \n- This is the basis for the concept of **temperature**.\n\nIf you want, I can also give a **one-line intuitive version** of each law.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054203,
    &quot;created_at&quot;: 1777054122,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_00272dd8da5b37c90169ebb1aaeb288194a6e5ddeb7bb03dc8&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.4-pro-2026-03-05&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_00272dd8da5b37c90169ebb1faf90c81948fd9a67a37b4c209&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;The **three laws of thermodynamics** usually mean:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed, only transferred or transformed.  \n   - In thermodynamics: the change in a system\u2019s internal energy equals heat added to the system minus work done by the system.\n\n2. **Second Law \u2014 Entropy Increases**  \n   In any natural process, the total entropy of an isolated system tends to increase.  \n   - This means energy spontaneously spreads out, and no heat engine can be 100% efficient.\n   - Heat naturally flows from hot objects to cold ones, not the reverse without input of work.\n\n3. **Third Law \u2014 Entropy at Absolute Zero**  \n   As temperature approaches **absolute zero** (0 K), the entropy of a perfect crystal approaches zero.  \n   - A consequence is that absolute zero cannot be reached in a finite number of steps.\n\nSmall note: thermodynamics also has a **Zeroth Law**, which is often listed before these:\n- If system A is in thermal equilibrium with B, and B is in thermal equilibrium with C, then A is in thermal equilibrium with C.  \n- This is the basis for the concept of **temperature**.\n\nIf you want, I can also give a **one-line intuitive version** of each law.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_00272dd8da5b37c90169ebb1fafad0819488ef71fbebf8527a&quot;,
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
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
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
      &quot;input_tokens&quot;: 15,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 342,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 67
      },
      &quot;total_tokens&quot;: 357
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.4-pro&#x27;,
  { input: &#x27;What are the three laws of thermodynamics?&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.4-pro&quot;,
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
    &quot;text&quot;: &quot;Use Python\u2019s built-in `json` module.\n\n### Read a JSON file into a Python object\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\n### What you get back\n`json.load()` converts JSON into normal Python types:\n\n- JSON object \u2192 `dict`\n- JSON array \u2192 `list`\n- JSON string \u2192 `str`\n- JSON number \u2192 `int` / `float`\n- JSON true/false \u2192 `True` / `False`\n- JSON null \u2192 `None`\n\n### Example\nIf `data.json` contains:\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;skills\&quot;: [\&quot;Python\&quot;, \&quot;SQL\&quot;]\n}\n```\n\nThen:\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data[\&quot;name\&quot;])    # Alice\nprint(data[\&quot;skills\&quot;])  # [&#x27;Python&#x27;, &#x27;SQL&#x27;]\n```\n\n### Handle errors safely\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Invalid JSON.\&quot;)\n```\n\n### If you already have JSON as a string\nUse `json.loads()` instead:\n```python\nimport json\n\ntext = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(text)\nprint(data)\n```\n\nIf you want, I can also show how to **write JSON back to a file**.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054145,
    &quot;created_at&quot;: 1777054123,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_00e5a81e42bf0bda0169ebb1ab449c8190a0d57802b4aebebd&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.4-pro-2026-03-05&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_00e5a81e42bf0bda0169ebb1c0e57881909eaf01efa0557a43&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Use Python\u2019s built-in `json` module.\n\n### Read a JSON file into a Python object\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\n### What you get back\n`json.load()` converts JSON into normal Python types:\n\n- JSON object \u2192 `dict`\n- JSON array \u2192 `list`\n- JSON string \u2192 `str`\n- JSON number \u2192 `int` / `float`\n- JSON true/false \u2192 `True` / `False`\n- JSON null \u2192 `None`\n\n### Example\nIf `data.json` contains:\n```json\n{\n  \&quot;name\&quot;: \&quot;Alice\&quot;,\n  \&quot;age\&quot;: 30,\n  \&quot;skills\&quot;: [\&quot;Python\&quot;, \&quot;SQL\&quot;]\n}\n```\n\nThen:\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data[\&quot;name\&quot;])    # Alice\nprint(data[\&quot;skills\&quot;])  # [&#x27;Python&#x27;, &#x27;SQL&#x27;]\n```\n\n### Handle errors safely\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError:\n    print(\&quot;Invalid JSON.\&quot;)\n```\n\n### If you already have JSON as a string\nUse `json.loads()` instead:\n```python\nimport json\n\ntext = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(text)\nprint(data)\n```\n\nIf you want, I can also show how to **write JSON back to a file**.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_00e5a81e42bf0bda0169ebb1c0e7608190b3928d22f252a21a&quot;,
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
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
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
      &quot;input_tokens&quot;: 30,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 397,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 35
      },
      &quot;total_tokens&quot;: 427
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.4-pro&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-5.4-pro&quot;,
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
    &quot;text&quot;: &quot;- Monterey is great for the aquarium, Cannery Row, and ocean views.  \n- San Luis Obispo is a fun lunch stop with a charming downtown and Mission Plaza.  \n- Santa Barbara offers beaches, palm-lined streets, and an easy coastal break.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777421276,
    &quot;created_at&quot;: 1777421147,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;id&quot;: &quot;resp_08addd0821ac85160169f14b5b16d881968c58b918efd0d015&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 16000,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.4-pro-2026-03-05&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_08addd0821ac85160169f14bdca35c819696eb984a7f0beead&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;- Monterey is great for the aquarium, Cannery Row, and ocean views.  \n- San Luis Obispo is a fun lunch stop with a charming downtown and Mission Plaza.  \n- Santa Barbara offers beaches, palm-lined streets, and an easy coastal break.&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_08addd0821ac85160169f14bdca4ec8196a5b40b76291544f5&quot;,
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
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
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
      &quot;input_tokens&quot;: 78,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 104,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 46
      },
      &quot;total_tokens&quot;: 182
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.4-pro&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-5.4-pro&quot;,
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
    &quot;text&quot;: &quot;Silent circuits dream  \nLearning patterns in the dark  \nDawn wakes metal minds&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054190,
    &quot;created_at&quot;: 1777054156,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_01b04056ffd5d9ac0169ebb1cc85348196a164e1d9e99ac1f5&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.4-pro-2026-03-05&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_01b04056ffd5d9ac0169ebb1ee42688196859b0cd089b7924c&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Silent circuits dream  \nLearning patterns in the dark  \nDawn wakes metal minds&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_01b04056ffd5d9ac0169ebb1ee44248196aa66c63d28c6a59b&quot;,
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
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
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
      &quot;input_tokens&quot;: 13,
      &quot;input_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 122,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 101
      },
      &quot;total_tokens&quot;: 135
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.4-pro&#x27;,
  { input: &#x27;Write a haiku about artificial intelligence&#x27;, temperature: 1 },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.4-pro&quot;,
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
    &quot;text&quot;: &quot;Step 1: Find their combined speed since they are moving toward each other.\n\n- Train from Chicago: **60 mph**\n- Train from New York: **80 mph**\n\nCombined speed:\n\n**60 + 80 = 140 mph**\n\nStep 2: Use the distance formula:\n\n\\[\n\\text{time}=\\frac{\\text{distance}}{\\text{speed}}\n\\]\n\n\\[\n\\text{time}=\\frac{900}{140}\n\\]\n\n\\[\n\\text{time}=6.428571\\text{ hours}\n\\]\n\nStep 3: Convert the decimal part to minutes.\n\n\\[\n0.428571 \\times 60 \\approx 25.7 \\text{ minutes}\n\\]\n\nSo they meet after about:\n\n**6 hours 26 minutes**\n\nFinal answer: **The trains meet about 6 hours 26 minutes after they leave.**&quot;
  },
  &quot;raw_response&quot;: {
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1777054263,
    &quot;created_at&quot;: 1777054191,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;resp_01e1e7671514bf440169ebb1ef8af88190b68b1e60a0cb59ed&quot;,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: null,
    &quot;max_tool_calls&quot;: null,
    &quot;metadata&quot;: {},
    &quot;model&quot;: &quot;gpt-5.4-pro-2026-03-05&quot;,
    &quot;moderation&quot;: null,
    &quot;object&quot;: &quot;response&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_01e1e7671514bf440169ebb236f1e88190931dc758c55a4050&quot;,
        &quot;summary&quot;: [],
        &quot;type&quot;: &quot;reasoning&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Step 1: Find their combined speed since they are moving toward each other.\n\n- Train from Chicago: **60 mph**\n- Train from New York: **80 mph**\n\nCombined speed:\n\n**60 + 80 = 140 mph**\n\nStep 2: Use the distance formula:\n\n\\[\n\\text{time}=\\frac{\\text{distance}}{\\text{speed}}\n\\]\n\n\\[\n\\text{time}=\\frac{900}{140}\n\\]\n\n\\[\n\\text{time}=6.428571\\text{ hours}\n\\]\n\nStep 3: Convert the decimal part to minutes.\n\n\\[\n0.428571 \\times 60 \\approx 25.7 \\text{ minutes}\n\\]\n\nSo they meet after about:\n\n**6 hours 26 minutes**\n\nFinal answer: **The trains meet about 6 hours 26 minutes after they leave.**&quot;,
            &quot;type&quot;: &quot;output_text&quot;
          }
        ],
        &quot;id&quot;: &quot;msg_01e1e7671514bf440169ebb236f3a88190b6a99b6fc6389fde&quot;,
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
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
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
      &quot;output_tokens&quot;: 272,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 88
      },
      &quot;total_tokens&quot;: 320
    },
    &quot;user&quot;: null
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.4-pro&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-5.4-pro&quot;,
  &quot;input&quot;: &quot;Solve this problem step by step: A train leaves Chicago at 60mph heading east. Another train leaves New York at 80mph heading west. They are 900 miles apart. When do they meet?&quot;,
  &quot;reasoning&quot;: {
    &quot;effort&quot;: &quot;medium&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-5.4-pro/schema-input.json)
- [Output schema](/ai/models/openai/gpt-5.4-pro/schema-output.json)

