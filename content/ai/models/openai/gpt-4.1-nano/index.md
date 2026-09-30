---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/openai/gpt-4.1-nano/
  description: openai/gpt-4.1-nano
  full_title: GPT-4.1 nano · Cloudflare AI docs
  head_html: <title>GPT-4.1 nano · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="openai/gpt-4.1-nano"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/openai/gpt-4.1-nano/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="GPT-4.1 nano · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="openai/gpt-4.1-nano"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/openai/gpt-4.1-nano/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/openai/gpt-4.1-nano/#page","headline":"GPT-4.1 nano \u00b7 Cloudflare AI docs","description":"openai/gpt-4.1-nano","url":"https://developers.cloudflare.com/ai/models/openai/gpt-4.1-nano/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/openai/gpt-4.1-nano/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-4-1-nano">GPT-4.1 nano</h1>

<p><code>openai/gpt-4.1-nano</code></p>

GPT-4.1 Nano is OpenAI’s smallest and cheapest GPT-4.1 variant, optimized for high-throughput, low-latency tasks.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.1, Output tokens (per 1M): 0.4, Cached input tokens (per 1M): 0.025</td></tr>
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
    &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental principles that describe the behavior of energy and temperature in physical systems:\n\n1. **First Law of Thermodynamics (Law of Energy Conservation):**  \n   Energy cannot be created or destroyed in an isolated system. The total energy remains constant, implying that the change in the internal energy of a system is equal to the heat added to the system minus the work done by the system.  \n   Mathematically:  \n   \\[\n   \\Delta U = Q - W\n   \\]\n\n2. **Second Law of Thermodynamics:**  \n   The entropy of an isolated system always tends to increase over time, and natural processes tend to move towards a state of maximum entropy. This law introduces the concept of irreversibility and asserts that heat cannot spontaneously flow from a colder to a hotter body without external work.\n\n3. **Third Law of Thermodynamics:**  \n   As the temperature of a perfect crystal approaches absolute zero (0 Kelvin), the entropy of the system approaches a constant minimum, often taken as zero. This implies that absolute zero temperature is unattainable in a finite number of steps.\n\nThese laws form the foundation of thermodynamics and are essential in understanding energy systems, engines, refrigerators, and many other physical phenomena.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;The three laws of thermodynamics are fundamental principles that describe the behavior of energy and temperature in physical systems:\n\n1. **First Law of Thermodynamics (Law of Energy Conservation):**  \n   Energy cannot be created or destroyed in an isolated system. The total energy remains constant, implying that the change in the internal energy of a system is equal to the heat added to the system minus the work done by the system.  \n   Mathematically:  \n   \\[\n   \\Delta U = Q - W\n   \\]\n\n2. **Second Law of Thermodynamics:**  \n   The entropy of an isolated system always tends to increase over time, and natural processes tend to move towards a state of maximum entropy. This law introduces the concept of irreversibility and asserts that heat cannot spontaneously flow from a colder to a hotter body without external work.\n\n3. **Third Law of Thermodynamics:**  \n   As the temperature of a perfect crystal approaches absolute zero (0 Kelvin), the entropy of the system approaches a constant minimum, often taken as zero. This implies that absolute zero temperature is unattainable in a finite number of steps.\n\nThese laws form the foundation of thermodynamics and are essential in understanding energy systems, engines, refrigerators, and many other physical phenomena.&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777320190,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DZMScK7GU5VKq3YMOIJvLRfotOhnW&quot;,
    &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_8fc5e9a3e3&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 252,
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
      &quot;total_tokens&quot;: 268
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1-nano&#x27;,
  { messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-4.1-nano&quot;,
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
    &quot;text&quot;: &quot;To read a JSON file in Python, you can use the built-in `json` module which provides functions for parsing JSON data. Here&#x27;s a simple step-by-step example:\n\n1. Import the `json` module.\n2. Open the JSON file using `open()`.\n3. Use `json.load()` to parse the data from the file into a Python data structure (usually a dictionary or list).\n\nHere&#x27;s an example:\n\n```python\nimport json\n\n# Specify the path to your JSON file\nfile_path = &#x27;data.json&#x27;\n\n# Open the file and load the JSON data\nwith open(file_path, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\n# Now you can work with &#x27;data&#x27; as a Python dictionary or list\nprint(data)\n```\n\n### Notes:\n- Make sure the JSON file exists at the specified location.\n- If the JSON data is in string format rather than a file, you can use `json.loads()` instead.\n- Always handle potential exceptions (like `FileNotFoundError` or `json.JSONDecodeError`) when working with files and JSON data.\n\nWould you like an example with error handling or working with JSON data in a string?&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;To read a JSON file in Python, you can use the built-in `json` module which provides functions for parsing JSON data. Here&#x27;s a simple step-by-step example:\n\n1. Import the `json` module.\n2. Open the JSON file using `open()`.\n3. Use `json.load()` to parse the data from the file into a Python data structure (usually a dictionary or list).\n\nHere&#x27;s an example:\n\n```python\nimport json\n\n# Specify the path to your JSON file\nfile_path = &#x27;data.json&#x27;\n\n# Open the file and load the JSON data\nwith open(file_path, &#x27;r&#x27;) as file:\n    data = json.load(file)\n\n# Now you can work with &#x27;data&#x27; as a Python dictionary or list\nprint(data)\n```\n\n### Notes:\n- Make sure the JSON file exists at the specified location.\n- If the JSON data is in string format rather than a file, you can use `json.loads()` instead.\n- Always handle potential exceptions (like `FileNotFoundError` or `json.JSONDecodeError`) when working with files and JSON data.\n\nWould you like an example with error handling or working with JSON data in a string?&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777320192,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DZMSexsEYr8aaW33Xyn2IaPnygnY5&quot;,
    &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_1bedc25778&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 238,
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
      &quot;total_tokens&quot;: 269
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1-nano&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1-nano&quot;,
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
    &quot;text&quot;: &quot;Great! Here are some interesting stops along the San Francisco to Los Angeles route, mainly along the iconic Highway 1 and scenic coastal areas:\n\n1. **Santa Cruz**  \n   - Enjoy the beaches, surf culture, and the famous Santa Cruz Beach Boardwalk amusement park.\n\n2. **Monterey &amp; Carmel-by-the-Sea**  \n   - Monterey: Visit the Monterey Bay Aquarium and Cannery Row.  \n   - Carmel: Stroll through charming streets, galleries, and enjoy the stunning coastal views.\n\n3. **Big Sur**  \n   - One of the most breathtaking parts of California&#x27;s coast.  \n   - Stop at Pfeiffer Beach, Bixby Creek Bridge, McWay Falls, and Julia Pfeiffer Burns State Park.\n\n4. **San Simeon**  \n   - Tour Hearst Castle, a magnificent historic estate with stunning architecture and gardens.\n\n5. **Cambria or Morro Bay**  \n   - Enjoy small-town charm, local shops, and coastal scenery.\n\n6. **Elephant Seal Rookery at Piedras Blancas**  \n   - See seals along the coast (near San Simeon).\n\n7. **Santa Barbara**  \n   - Often called the \&quot;American Riviera,\&quot; it&#x27;s known for beautiful beaches, Spanish-style architecture, and lively downtown.\n\n8. **Malibu**  \n   - Famous for its beaches and celebrity homes. Consider a quick stop at Zuma Beach or Malibu Pier.\n\nIf you&#x27;re looking for a more inland route, you can also take Interstate 5 and explore some of California\u2019s inland attractions, but the coastal drive offers some of the most iconic scenic views.\n\nWould you like a suggested itinerary or specific activity recommendations at any of these stops?&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;Great! Here are some interesting stops along the San Francisco to Los Angeles route, mainly along the iconic Highway 1 and scenic coastal areas:\n\n1. **Santa Cruz**  \n   - Enjoy the beaches, surf culture, and the famous Santa Cruz Beach Boardwalk amusement park.\n\n2. **Monterey &amp; Carmel-by-the-Sea**  \n   - Monterey: Visit the Monterey Bay Aquarium and Cannery Row.  \n   - Carmel: Stroll through charming streets, galleries, and enjoy the stunning coastal views.\n\n3. **Big Sur**  \n   - One of the most breathtaking parts of California&#x27;s coast.  \n   - Stop at Pfeiffer Beach, Bixby Creek Bridge, McWay Falls, and Julia Pfeiffer Burns State Park.\n\n4. **San Simeon**  \n   - Tour Hearst Castle, a magnificent historic estate with stunning architecture and gardens.\n\n5. **Cambria or Morro Bay**  \n   - Enjoy small-town charm, local shops, and coastal scenery.\n\n6. **Elephant Seal Rookery at Piedras Blancas**  \n   - See seals along the coast (near San Simeon).\n\n7. **Santa Barbara**  \n   - Often called the \&quot;American Riviera,\&quot; it&#x27;s known for beautiful beaches, Spanish-style architecture, and lively downtown.\n\n8. **Malibu**  \n   - Famous for its beaches and celebrity homes. Consider a quick stop at Zuma Beach or Malibu Pier.\n\nIf you&#x27;re looking for a more inland route, you can also take Interstate 5 and explore some of California\u2019s inland attractions, but the coastal drive offers some of the most iconic scenic views.\n\nWould you like a suggested itinerary or specific activity recommendations at any of these stops?&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777320194,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DZMSggejH8U1yMFzW7Ibn1J2xL8xx&quot;,
    &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_8fc5e9a3e3&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 341,
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
      &quot;total_tokens&quot;: 416
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1-nano&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1-nano&quot;,
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
    &quot;text&quot;: &quot;Detective Mara Collins cautiously stepped into the dimly lit workshop, the scent of oil and old wood lingering in the air. Pieces of broken clock gears and scattered tools dotted the cluttered space, but it was the tiny, shimmering feather tucked behind a loose brick that caught her eye. It was unlike any bird feather she\u2019d seen\u2014irregularly shaped, iridescent, and strangely warm to the touch. As she examined it, a shiver ran down her spine, promising that this was no ordinary clue, but a signature left behind by someone desperately trying to be remembered.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;logprobs&quot;: null,
        &quot;message&quot;: {
          &quot;annotations&quot;: [],
          &quot;content&quot;: &quot;Detective Mara Collins cautiously stepped into the dimly lit workshop, the scent of oil and old wood lingering in the air. Pieces of broken clock gears and scattered tools dotted the cluttered space, but it was the tiny, shimmering feather tucked behind a loose brick that caught her eye. It was unlike any bird feather she\u2019d seen\u2014irregularly shaped, iridescent, and strangely warm to the touch. As she examined it, a shiver ran down her spine, promising that this was no ordinary clue, but a signature left behind by someone desperately trying to be remembered.&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777320194,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;chatcmpl-DZMSg3VYyqTPmNOmWnu1UqurYsxlI&quot;,
    &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 117,
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
      &quot;total_tokens&quot;: 137
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1-nano&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1-nano&quot;,
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
      &quot;Rec&quot;,
      &quot;ursion&quot;,
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
      &quot; It&quot;,
      &quot;\u2019s&quot;,
      &quot; especially&quot;,
      &quot; useful&quot;,
      &quot; when&quot;,
      &quot; a&quot;,
      &quot; problem&quot;,
      &quot; can&quot;,
      &quot; be&quot;,
      &quot; broken&quot;,
      &quot; down&quot;,
      &quot; into&quot;,
      &quot; smaller&quot;,
      &quot;,&quot;,
      &quot; similar&quot;,
      &quot; sub&quot;,
      &quot;pro&quot;,
      &quot;blems&quot;,
      &quot;.&quot;,
      &quot; Each&quot;,
      &quot; recursive&quot;,
      &quot; call&quot;,
      &quot; works&quot;,
      &quot; on&quot;,
      &quot; a&quot;,
      &quot; smaller&quot;,
      &quot; piece&quot;,
      &quot;,&quot;,
      &quot; and&quot;,
      &quot; the&quot;,
      &quot; process&quot;,
      &quot; continues&quot;,
      &quot; until&quot;,
      &quot; a&quot;,
      &quot; basic&quot;,
      &quot; case&quot;,
      &quot; is&quot;,
      &quot; reached&quot;,
      &quot;,&quot;,
      &quot; which&quot;,
      &quot; stops&quot;,
      &quot; the&quot;,
      &quot; recursion&quot;,
      &quot;.\n\n&quot;,
      &quot;**&quot;,
      &quot;Simple&quot;,
      &quot; Example&quot;,
      &quot;:**&quot;,
      &quot; Calcul&quot;,
      &quot;ating&quot;,
      &quot; the&quot;,
      &quot; factorial&quot;,
      &quot; of&quot;,
      &quot; a&quot;,
      &quot; number&quot;,
      &quot;\n\n&quot;,
      &quot;The&quot;,
      &quot; factorial&quot;,
      &quot; of&quot;,
      &quot; a&quot;,
      &quot; number&quot;,
      &quot; \\(&quot;,
      &quot; n&quot;,
      &quot; \\&quot;,
      &quot;)&quot;,
      &quot; (&quot;,
      &quot;written&quot;,
      &quot; as&quot;,
      &quot; \\(&quot;,
      &quot; n&quot;,
      &quot;!&quot;,
      &quot; \\&quot;,
      &quot;))&quot;,
      &quot; is&quot;,
      &quot; the&quot;,
      &quot; product&quot;,
      &quot; of&quot;,
      &quot; all&quot;,
      &quot; positive&quot;,
      &quot; integers&quot;,
      &quot; up&quot;,
      &quot; to&quot;,
      &quot; \\(&quot;,
      &quot; n&quot;,
      &quot; \\&quot;,
      &quot;).\n\n&quot;,
      &quot;For&quot;,
      &quot; example&quot;,
      &quot;:\n&quot;,
      &quot;\\[&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot;!&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \\&quot;,
      &quot;times&quot;,
      &quot; &quot;,
      &quot;4&quot;,
      &quot; \\&quot;,
      &quot;times&quot;,
      &quot; &quot;,
      &quot;3&quot;,
      &quot; \\&quot;,
      &quot;times&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot; \\&quot;,
      &quot;times&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;120&quot;,
      &quot; \\&quot;,
      &quot;]\n\n&quot;,
      &quot;**&quot;,
      &quot;Recursive&quot;,
      &quot; approach&quot;,
      &quot;:&quot;,
      &quot;**\n\n&quot;,
      &quot;-&quot;,
      &quot; The&quot;,
      &quot; factorial&quot;,
      &quot; of&quot;,
      &quot; \\(&quot;,
      &quot; n&quot;,
      &quot; \\&quot;,
      &quot;)&quot;,
      &quot; is&quot;,
      &quot; \\(&quot;,
      &quot; n&quot;,
      &quot; \\&quot;,
      &quot;)&quot;,
      &quot; multiplied&quot;,
      &quot; by&quot;,
      &quot; the&quot;,
      &quot; factorial&quot;,
      &quot; of&quot;,
      &quot; \\(&quot;,
      &quot; n&quot;,
      &quot;-&quot;,
      &quot;1&quot;,
      &quot; \\&quot;,
      &quot;).\n&quot;,
      &quot;-&quot;,
      &quot; Base&quot;,
      &quot; case&quot;,
      &quot;:&quot;,
      &quot; factorial&quot;,
      &quot; of&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; (&quot;,
      &quot;or&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot;)&quot;,
      &quot; is&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;.\n\n&quot;,
      &quot;**&quot;,
      &quot;Python&quot;,
      &quot; code&quot;,
      &quot; example&quot;,
      &quot;:&quot;,
      &quot;**\n\n&quot;,
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
      &quot; or&quot;,
      &quot; n&quot;,
      &quot; ==&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;:\n&quot;,
      &quot;       &quot;,
      &quot; return&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; &quot;,
      &quot; #&quot;,
      &quot; Base&quot;,
      &quot; case&quot;,
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
      &quot; &quot;,
      &quot; #&quot;,
      &quot; Recursive&quot;,
      &quot; call&quot;,
      &quot;\n\n&quot;,
      &quot;print&quot;,
      &quot;(f&quot;,
      &quot;actor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;5&quot;,
      &quot;))&quot;,
      &quot; &quot;,
      &quot; #&quot;,
      &quot; Output&quot;,
      &quot;:&quot;,
      &quot; &quot;,
      &quot;120&quot;,
      &quot;\n&quot;,
      &quot;``&quot;,
      &quot;`\n\n&quot;,
      &quot;In&quot;,
      &quot; this&quot;,
      &quot; example&quot;,
      &quot;:\n&quot;,
      &quot;-&quot;,
      &quot; When&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;5&quot;,
      &quot;)`&quot;,
      &quot; is&quot;,
      &quot; called&quot;,
      &quot;,&quot;,
      &quot; it&quot;,
      &quot; computes&quot;,
      &quot; \\(&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \\&quot;,
      &quot;times&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;4&quot;,
      &quot;)&quot;,
      &quot; \\&quot;,
      &quot;).\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;4&quot;,
      &quot;)`&quot;,
      &quot; computes&quot;,
      &quot; \\(&quot;,
      &quot; &quot;,
      &quot;4&quot;,
      &quot; \\&quot;,
      &quot;times&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)&quot;,
      &quot; \\&quot;,
      &quot;),&quot;,
      &quot; and&quot;,
      &quot; so&quot;,
      &quot; on&quot;,
      &quot;.\n&quot;,
      &quot;-&quot;,
      &quot; When&quot;,
      &quot; it&quot;,
      &quot; reaches&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)&quot;,
      &quot;`,&quot;,
      &quot; it&quot;,
      &quot; hits&quot;,
      &quot; the&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot; and&quot;,
      &quot; returns&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;.\n&quot;,
      &quot;-&quot;,
      &quot; The&quot;,
      &quot; recursive&quot;,
      &quot; calls&quot;,
      &quot; then&quot;,
      &quot; resolve&quot;,
      &quot;,&quot;,
      &quot; multiplying&quot;,
      &quot; the&quot;,
      &quot; numbers&quot;,
      &quot; back&quot;,
      &quot; up&quot;,
      &quot; to&quot;,
      &quot; give&quot;,
      &quot; the&quot;,
      &quot; final&quot;,
      &quot; result&quot;,
      &quot;.&quot;
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Iw5l2php&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dCJPqHY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;O1ew&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xTyaAMs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SpJDtgAT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0IgvVgQIAefSNr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;I6Ny&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hwhFKMKr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;u&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Vht5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vpH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3z04HKt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2tfh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;qUZbYRt5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;iO6W2ullu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; It&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mwNhczb&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\u2019s&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RsyJwxGM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; especially&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OXQUNbjTMKpC84k&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; useful&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5nw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XEn0j&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;lKMF8slJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; can&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5G6yUA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; be&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;z8xYEOE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; broken&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OiV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CYUHM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2IFZq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;jg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yFN12xYdd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; similar&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;trjsj6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CU6gtCf&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;G1DAj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4lip3oJYY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2ZwY8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zj98S&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ktDo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; on&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;k64oScx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7a2wO1Fu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; piece&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YZtg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CQ4W1PdUc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2pM99y&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;LJQjRB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; process&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;35&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; continues&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SAN4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WuEEhpuk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; basic&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dbHf&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KIJ84&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;E00kVCL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reached&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;em&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;jO86iqSTF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; which&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DPto&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stops&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2lod&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CobyW7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;8eX1h&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DQnPO09Y&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Ddig&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;R4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;X5y1Zve&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ghf&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ttJaH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;X8DgtI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zsMVdp5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Rj6RG4Q1&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; number&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Xb4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PhDpOi&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;kojq6Fh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;b7rmsft&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;C2TIw6BT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; number&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YD6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;o7hxd7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RL1doRO9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;J9Xwbiw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;9PmX9VvrY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0hIVVLB5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Ilu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6IAaSp0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;q7YO9n&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DKDEz3jg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ZasAqbE2H&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0uLtFy5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;))&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KljMkvwn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;344rDaN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;aIgXPQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;rW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PamFPFN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dg7Qou&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;N&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; up&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;NopcCBR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;r7r4qd0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5ICeUP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SUYaI4XM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WJBUHCB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4fKh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;For&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Mzp9xVW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;51&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xVAUd3k&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\\[&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;NXe7kfy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;VuR1zK51r&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;TgscAfqZz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nRRFz2HCG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gxsFAuAy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pRFKIVHBj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;s9SkxgYCN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gOB4bkp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;times&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Gq7PL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BrXu0vpPY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;HdhssuKhe&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2XCQwzW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;times&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SKj4P&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;24SRaa7Vy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pNOkITAwN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gN1O4dw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;times&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GY6H3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hRWIehobt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;NMVsCUWyF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mL5983Q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;times&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4XjuM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7qWZkcEld&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OagfENHoN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RjFZZmdd&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;v9L41bA06&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;120&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;HE9eYNG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XMOnXr8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;]\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5LnVI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cRAHOmwp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;w&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; approach&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;O&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Z6Cs6ubob&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;pBBG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YLHx6nrpq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;c0iMD2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bYOAGNs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;4SvwxD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1qKjyAZr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;T2TgzKJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RPP3z5QEw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;M2e0vQH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dUe8UD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Ybc7M5be&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;uOhKDD2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;TYs7EyzbY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; multiplied&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XjLkPo5sbduqWIF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; by&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;x7Auf1c&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yJw8Zn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2DaGSQx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;a8jzQy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xwukHdK5&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CAiHik7hw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;IERQGbMe8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;0pw5SbS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zRud6w&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tPMKosEpK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BFfKj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5te8A&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KVg1zN0uZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7ru0CQ3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UI5ngaCnH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;88VQLi1bG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;J83oZ8tF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;jsSmYDmG&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YMzcTuS54&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;J10a57ySs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;WI4x3bKpu&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;FZfIJUw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ijDr1mmq3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BjA26aCv8&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YRBp3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;G9RkkedK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BX4e&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; code&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;R3qmW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7M&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RIn8lbEb0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vTEC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Uz9JiFj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;QS66&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;9GWEeNOp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PGFOFTP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Rnxg3Fpz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;2TSnV3&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5yBRtja&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;kqjBLlL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bmrRTkX2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PKj3hTz&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mpLmGgbi6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Lmt5jTYWi&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ZHiAwC7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mROj2ygE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;z1wRHVm&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RVnklsx6i&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ynQ3500k0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ycezYMB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;c0U&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3Y2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nH6EBOg59&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MR2QY8T8B&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;K8MtRCy5v&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YWNZcUyv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KjD9l&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;808vF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;8en8pzgj&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;p1By6Ih&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;nenWZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zo4AQD9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Bex&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;mcS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;95Zo7mdA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;GtlmdusP&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XjUr65JH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;DRfF982D&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;VUiC5lGCR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;20l7FP493&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KreNP9TCR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tlEmOmUcy&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Yk8ic60Z&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;IjUrV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PFBDSE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;print&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;OzCam&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(f&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;qBe81WOp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;actor&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vOaw4&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;b1eUzwX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;8FNqNpEeU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UT1gl6OJ0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;))&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SsJxIiKJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;FmXOuFvFf&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ofvfLwQ9&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Output&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;3EX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gi3cCKOD7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tpGYNap15&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;120&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;7DxtFCr&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;sNMXzAeQ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;d0aXmPRN&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SeKel&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;PwXaEePh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; this&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;yGpd2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;uo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hAGirua&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Gx3L2Pqm7&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; When&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;MELou&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;sKQ2LZVL&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;32aF&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;S4Yieky&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YaxxAFQis&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;aYnZdh0jh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;gZ5yDpqU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;HalUnzk&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; called&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;aoJ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tkxbif2zs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RMfJOFE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; computes&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;F&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;1NIEYK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;NMn5OAwT2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Ni8PfFJ80&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;kXvSHSh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;times&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ONMbg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;QJPJPIFKU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;clg4J19UV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zzsyQhVLq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;s66pf5E&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;XnwahX&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cmJ0cHHoV&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;CcTRLNPn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;6nt6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hFs1Q2y&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;smyn75Scx&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UAPENA6mO&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;EyuvwujA&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; computes&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zzNR6r&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;5NsVpHLiv&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tvvt8vM8b&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;o39Rthi&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;times&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KVyir&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Dd7YTFUED&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;YPuboOJLS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;r7xXD1iWq&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \\&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;UDob4Bt&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;),&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Qxnc3cq0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ioNXOM&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; so&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;cb8BQBc&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; on&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;U2gTNAs&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;BSzpHLE&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bmhBrSxrH&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; When&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;xWA9k&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Wk3jgHD&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reaches&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;rI&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bPgImsil&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;X8OZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KQgXuSg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;QSaanDOS0&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bZxvUca2q&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;bO3Pbc7rC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;RV15GjQb&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;uTP1XWn&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; hits&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;X4BSg&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;kOp8Xh&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;oxZ4t&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ggdLB&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;H6Mu1X&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;g6&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;K42ywpUfU&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KySh13E70&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vTBxnqW&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;K5GkVBotR&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;HLUMYf&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Mkml&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;g4iFT&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; resolve&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;S2&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;hkuzhnNNZ&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; multiplying&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;zE9QbKwzEstZmp&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;wzkQzo&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; numbers&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;LK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; back&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;suSnC&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; up&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;P2wbaba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;vaWWxay&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; give&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;aXvdY&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;SjQsZS&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; final&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;Adre&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; result&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;index&quot;: 0,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;KIb&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;ipP88O5ob&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
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
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;dwbw&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [],
      &quot;created&quot;: 1777320196,
      &quot;id&quot;: &quot;chatcmpl-DZMSi0LW1G5hMlCi690nyLIRbQopZ&quot;,
      &quot;model&quot;: &quot;gpt-4.1-nano-2025-04-14&quot;,
      &quot;obfuscation&quot;: &quot;tNgMbOK&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;service_tier&quot;: &quot;default&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_04a6e55762&quot;,
      &quot;usage&quot;: {
        &quot;completion_tokens&quot;: 337,
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
        &quot;total_tokens&quot;: 354
      }
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-4.1-nano&#x27;,
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
  &quot;model&quot;: &quot;openai/gpt-4.1-nano&quot;,
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

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-4.1-nano/schema-input.json)
- [Output schema](/ai/models/openai/gpt-4.1-nano/schema-output.json)

