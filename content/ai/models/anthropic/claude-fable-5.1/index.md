<img src="/assets/upstream/images/workers-ai/anthropic.svg" alt="Anthropic logo" width="48" height="48">

<h1 id="claude-fable-5-1">Claude Fable 5.1</h1>

<p><code>anthropic/claude-fable-5.1</code></p>

Claude Fable 5.1 is Anthropic's next model in the Fable family, with improvements in agentic coding, long-running agentic workflows, knowledge work, front-end and visual code generation, and finance and analysis tasks. It supports adaptive thinking and a 1M token context window.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://www.anthropic.com/legal/commercial-terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 10, Output tokens (per 1M): 50, Cached input tokens (per 1M): 0.25, Cache creation tokens (per 1M): 12.5</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Set context with a system message

<section class="model-example"><strong>With System Message</strong>
<p>Set context with a system message</p>
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
    &quot;text&quot;: &quot;Use the built-in `json` module:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\n**What this does:**\n- `open(...)` opens the file; the `with` block closes it automatically.\n- `json.load(f)` parses the file contents into Python objects:\n  - JSON object `{}` \u2192 `dict`\n  - JSON array `[]` \u2192 `list`\n  - strings \u2192 `str`, numbers \u2192 `int`/`float`, `true`/`false` \u2192 `True`/`False`, `null` \u2192 `None`\n\n**Example:** if `data.json` contains\n\n```json\n{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30, \&quot;tags\&quot;: [\&quot;admin\&quot;, \&quot;user\&quot;]}\n```\n\nthen:\n\n```python\nprint(data[\&quot;name\&quot;])     # Alice\nprint(data[\&quot;tags\&quot;][0])  # admin\n```\n\n**Related tips:**\n- If you already have JSON as a string (not a file), use `json.loads(text)` instead.\n- To handle a missing or malformed file gracefully:\n\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\&quot;File not found\&quot;)\nexcept json.JSONDecodeError as e:\n    print(f\&quot;Invalid JSON: {e}\&quot;)\n```\n\n- To write JSON back out: `json.dump(data, f, indent=2)`.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_011CedBpeQJCnJHy2SvhfpSH&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Use the built-in `json` module:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\n**What this does:**\n- `open(...)` opens the file; the `with` block closes it automatically.\n- `json.load(f)` parses the file contents into Python objects:\n  - JSON object `{}` \u2192 `dict`\n  - JSON array `[]` \u2192 `list`\n  - strings \u2192 `str`, numbers \u2192 `int`/`float`, `true`/`false` \u2192 `True`/`False`, `null` \u2192 `None`\n\n**Example:** if `data.json` contains\n\n```json\n{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30, \&quot;tags\&quot;: [\&quot;admin\&quot;, \&quot;user\&quot;]}\n```\n\nthen:\n\n```python\nprint(data[\&quot;name\&quot;])     # Alice\nprint(data[\&quot;tags\&quot;][0])  # admin\n```\n\n**Related tips:**\n- If you already have JSON as a string (not a file), use `json.loads(text)` instead.\n- To handle a missing or malformed file gracefully:\n\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\&quot;File not found\&quot;)\nexcept json.JSONDecodeError as e:\n    print(f\&quot;Invalid JSON: {e}\&quot;)\n```\n\n- To write JSON back out: `json.dump(data, f, indent=2)`.&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-fable-5-1&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 40,
      &quot;output_tokens&quot;: 451
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-fable-5.1&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-fable-5.1&quot;,
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

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continue a conversation with prior assistant context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 1024,
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
    &quot;text&quot;: &quot;Great choice! Your stops depend on which route you take, so here are the two main options:\n\n**Highway 1 / Pacific Coast Highway (scenic, ~10-12 hours with stops, best over 2 days)**\n\n- **Half Moon Bay** \u2013 Quaint coastal town with good seafood and beaches\n- **Santa Cruz** \u2013 Beach Boardwalk, surfing culture, and redwoods nearby\n- **Monterey** \u2013 World-class aquarium, Cannery Row, and Fisherman&#x27;s Wharf\n- **17-Mile Drive / Pebble Beach** \u2013 Iconic coastline with the Lone Cypress (small toll)\n- **Carmel-by-the-Sea** \u2013 Charming village with galleries and Carmel Beach\n- **Big Sur** \u2013 The highlight: Bixby Bridge, McWay Falls, Pfeiffer Beach (purple sand), and Nepenthe restaurant for lunch with a view\n- **Hearst Castle (San Simeon)** \u2013 Fascinating mansion tour; the elephant seals at Piedras Blancas nearby are a fun free stop\n- **Cambria / Morro Bay** \u2013 Morro Rock and a laid-back harbor town\n- **San Luis Obispo** \u2013 Great downtown, Bubblegum Alley, and the quirky Madonna Inn\n- **Pismo Beach** \u2013 Classic beach town, good for a break\n- **Solvang** \u2013 A Danish-themed village with pastries and wine tasting\n- **Santa Barbara** \u2013 Beautiful Spanish architecture, State Street, and the waterfront\n- **Malibu** \u2013 Beaches and a final scenic stretch into LA\n\n**US-101 (faster, ~6-7 hours)**\n\n- **Gilroy** \u2013 Garlic capital, outlet shopping\n- **Paso Robles** \u2013 Excellent wine country, less crowded than Napa\n- **San Luis Obispo, Solvang, and Santa Barbara** are also on this route\n\n**I-5 (fastest, ~6 hours, but not scenic)**\n\n- **Harris Ranch** \u2013 The classic stop for a steak dinner\n- **Casa de Fruta** \u2013 Roadside attraction with snacks and a small train\n\n**Tips:**\n- Check Caltrans for Highway 1 road closures\u2014Big Sur sections sometimes close due to landslides\n- If doing Highway 1, consider an overnight in Monterey/Carmel, Big Sur, or Cambria\n- Fill up on gas before Big Sur; it&#x27;s expensive and sparse there\n\nWould you like help building a day-by-day itinerary based on how much time you have?&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_011CedBqDdZMZFGUp1yQHKL2&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;&quot;,
        &quot;signature&quot;: &quot;CAQShAUKEAgRGAI4AUIIdGhpbmtpbmcSDIPYwphr/ruEkQm5GRoMi2EZKjsehazJ6il4IjB4hJSu75aNtzCRDW20p3aRVBEl75/aOV5i2an6izSSmbWjhFYvkCSKKvsu6DNM1cwqoQQ0QHB3yemi+cxK105ZiZr2sbYwafT0INKT3HAAvkp8y+Q7o0ro7AZj+6UIUfu9tedn1MFxcGXrh+D8zA9tUXMELTqT4pELiY76hDhkFcCopOoUOCedyQotgDHna+WOdUVKV8BgJaLrvnCYchIHSb0HnWesjzp4GvrOkw3rxfIOl16/W1DTJ638aSYk9ozUMdKxNdyS3OcSvlN7jWiZMOzF6pZ11LTrXOQKy+xWk6Z9TnZ2PoSgBvK2r4xR49xsh+beq0Tq6iYvwUYYMbEOu0xb4t2qHCYJ+80fmyQwxUXdL4fCv0DNuakFX4fzRBOfELrgTDz2LiYm1J2B3Au2KPK/Yet+Qr6KO0G4FOCS5zlGpe9WSVgYzSu/gXm7O1CIrsV6Vfxtq7pv5S/+CL4rwTGJUunzdl8qozMlaJ7uD4kEuK1AMaJ4bcLGxiYDZ1p22pdhtsSGvO1BTb/hPn8PPQfIkEDq8UmRTxCJ+XnfJNAeOeOwB+S9CESoBN85U7yBiPXwvhpgG5uqT1dz9URyMFQHSHbrqoGT3gcilcsYUxzAwA17H5Fvhs1p0/6J0ek21fK/9+3YuryKWHhvM1XFA0uOwZu0xhmatkmLSrmnxEITpP4xHH1OZ2SQUURWn9vjoNLiTAySVKFl26+4nvGcZqDExckEPcBqoU6w7vgFg8nEcHlhs+aSw5S4cNFD5wRizh/iDaZ9+wbkXw5qC/sQ8AtYThgB&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Great choice! Your stops depend on which route you take, so here are the two main options:\n\n**Highway 1 / Pacific Coast Highway (scenic, ~10-12 hours with stops, best over 2 days)**\n\n- **Half Moon Bay** \u2013 Quaint coastal town with good seafood and beaches\n- **Santa Cruz** \u2013 Beach Boardwalk, surfing culture, and redwoods nearby\n- **Monterey** \u2013 World-class aquarium, Cannery Row, and Fisherman&#x27;s Wharf\n- **17-Mile Drive / Pebble Beach** \u2013 Iconic coastline with the Lone Cypress (small toll)\n- **Carmel-by-the-Sea** \u2013 Charming village with galleries and Carmel Beach\n- **Big Sur** \u2013 The highlight: Bixby Bridge, McWay Falls, Pfeiffer Beach (purple sand), and Nepenthe restaurant for lunch with a view\n- **Hearst Castle (San Simeon)** \u2013 Fascinating mansion tour; the elephant seals at Piedras Blancas nearby are a fun free stop\n- **Cambria / Morro Bay** \u2013 Morro Rock and a laid-back harbor town\n- **San Luis Obispo** \u2013 Great downtown, Bubblegum Alley, and the quirky Madonna Inn\n- **Pismo Beach** \u2013 Classic beach town, good for a break\n- **Solvang** \u2013 A Danish-themed village with pastries and wine tasting\n- **Santa Barbara** \u2013 Beautiful Spanish architecture, State Street, and the waterfront\n- **Malibu** \u2013 Beaches and a final scenic stretch into LA\n\n**US-101 (faster, ~6-7 hours)**\n\n- **Gilroy** \u2013 Garlic capital, outlet shopping\n- **Paso Robles** \u2013 Excellent wine country, less crowded than Napa\n- **San Luis Obispo, Solvang, and Santa Barbara** are also on this route\n\n**I-5 (fastest, ~6 hours, but not scenic)**\n\n- **Harris Ranch** \u2013 The classic stop for a steak dinner\n- **Casa de Fruta** \u2013 Roadside attraction with snacks and a small train\n\n**Tips:**\n- Check Caltrans for Highway 1 road closures\u2014Big Sur sections sometimes close due to landslides\n- If doing Highway 1, consider an overnight in Monterey/Carmel, Big Sur, or Cambria\n- Fill up on gas before Big Sur; it&#x27;s expensive and sparse there\n\nWould you like help building a day-by-day itinerary based on how much time you have?&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-fable-5-1&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 105,
      &quot;output_tokens&quot;: 930
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-fable-5.1&#x27;,
  {
    max_tokens: 1024,
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
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;anthropic/claude-fable-5.1&quot;,
  &quot;max_tokens&quot;: 1024,
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

<section class="model-example"><strong>Streaming Response</strong>
<p>Stream a response for real-time output</p>
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
      &quot;**&quot;,
      &quot;Recursion** is a technique where a function solves a problem by calling itself on a smaller version of that same problem, until it reaches a simple case it can answer directly.\n\nEvery recursive function needs two par&quot;,
      &quot;ts:\n\n1. **Base case** \u2013 the simplest input, where the answer is known immediately and no further calls are made. This is what stops the recursion.\n2. **Recursive case** \u2013 the function&quot;,
      &quot; calls itself with a \&quot;smaller\&quot; input, moving toward the base case.\n\n## Example: Factorial\n\nThe factorial of *n* (written *n!*) is *n \u00d7 (n\u2212&quot;,
      &quot;1) \u00d7 (n\u22122) \u00d7 ... \u00d7 1*. For example, 5! = 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 = 120.\n\nNotice that 5! is just 5 \u00d7 4!. And 4! is 4 \u00d7 3!. This&quot;,
      &quot; \&quot;defined in terms of itself\&quot; pattern is what makes it recursive.\n\n```python\ndef factorial(n):\n    if n == 1:                    # base case\n        return 1\n    return n * factorial(n - &quot;,
      &quot;1)   # recursive case\n```\n\nTracing `factorial(4)`:\n\n```\nfactorial(4)\n= 4 * factorial(3)\n= 4 * (3 * factorial(2))\n= 4 * (3 * (2 * factorial(1)))&quot;,
      &quot;\n= 4 * (3 * (2 * 1))      \u2190 base case reached\n= 4 * (3 * 2)\n= 4 * 6\n= 24\n```\n\nThe calls \&quot;stack up\&quot; until the base case is hit, then the results unwind back to&quot;,
      &quot; the original call.\n\n## A real-world analogy\n\nImagine you&#x27;re in a long line and want to know your position. You ask the person in front of you, \&quot;What&quot;,
      &quot;&#x27;s your position?\&quot; They don&#x27;t know either, so they ask the person in front of *them*. This continues until it reaches the person at the front, who says \&quot;I&#x27;m #1\&quot; (base case). Each&quot;,
      &quot; person then adds 1 to the answer they receive and passes it back, until the number reaches you.\n\n## Key things to remember\n\n- **&quot;,
      &quot;Without a base case**, the function calls itself forever (in practice, until the program crashes with a stack overflow).\n- Each recursive call must make progress toward the base case.\n- Recursion is especially natural for problems with self&quot;,
      &quot;-similar structure: traversing trees, exploring directories, parsing nested expressions, or algorithms like merge sort and binary search.&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;type&quot;: &quot;message_start&quot;,
      &quot;message&quot;: {
        &quot;model&quot;: &quot;claude-fable-5-1&quot;,
        &quot;id&quot;: &quot;msg_011CedBrJsMHVisMiwBi3NSy&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;role&quot;: &quot;assistant&quot;,
        &quot;content&quot;: [],
        &quot;stop_reason&quot;: null,
        &quot;stop_sequence&quot;: null,
        &quot;stop_details&quot;: null,
        &quot;usage&quot;: {
          &quot;input_tokens&quot;: 24,
          &quot;cache_creation_input_tokens&quot;: 0,
          &quot;cache_read_input_tokens&quot;: 0,
          &quot;cache_creation&quot;: {
            &quot;ephemeral_5m_input_tokens&quot;: 0,
            &quot;ephemeral_1h_input_tokens&quot;: 0
          },
          &quot;output_tokens&quot;: 1,
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
        &quot;text&quot;: &quot;**&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;Recursion** is a technique where a function solves a problem by calling itself on a smaller version of that same problem, until it reaches a simple case it can answer directly.\n\nEvery recursive function needs two par&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;ts:\n\n1. **Base case** \u2013 the simplest input, where the answer is known immediately and no further calls are made. This is what stops the recursion.\n2. **Recursive case** \u2013 the function&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; calls itself with a \&quot;smaller\&quot; input, moving toward the base case.\n\n## Example: Factorial\n\nThe factorial of *n* (written *n!*) is *n \u00d7 (n\u2212&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;1) \u00d7 (n\u22122) \u00d7 ... \u00d7 1*. For example, 5! = 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 = 120.\n\nNotice that 5! is just 5 \u00d7 4!. And 4! is 4 \u00d7 3!. This&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; \&quot;defined in terms of itself\&quot; pattern is what makes it recursive.\n\n```python\ndef factorial(n):\n    if n == 1:                    # base case\n        return 1\n    return n * factorial(n - &quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;1)   # recursive case\n```\n\nTracing `factorial(4)`:\n\n```\nfactorial(4)\n= 4 * factorial(3)\n= 4 * (3 * factorial(2))\n= 4 * (3 * (2 * factorial(1)))&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;\n= 4 * (3 * (2 * 1))      \u2190 base case reached\n= 4 * (3 * 2)\n= 4 * 6\n= 24\n```\n\nThe calls \&quot;stack up\&quot; until the base case is hit, then the results unwind back to&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; the original call.\n\n## A real-world analogy\n\nImagine you&#x27;re in a long line and want to know your position. You ask the person in front of you, \&quot;What&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;&#x27;s your position?\&quot; They don&#x27;t know either, so they ask the person in front of *them*. This continues until it reaches the person at the front, who says \&quot;I&#x27;m #1\&quot; (base case). Each&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; person then adds 1 to the answer they receive and passes it back, until the number reaches you.\n\n## Key things to remember\n\n- **&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;Without a base case**, the function calls itself forever (in practice, until the program crashes with a stack overflow).\n- Each recursive call must make progress toward the base case.\n- Recursion is especially natural for problems with self&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;-similar structure: traversing trees, exploring directories, parsing nested expressions, or algorithms like merge sort and binary search.&quot;
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
        &quot;input_tokens&quot;: 24,
        &quot;cache_creation_input_tokens&quot;: 0,
        &quot;cache_read_input_tokens&quot;: 0,
        &quot;output_tokens&quot;: 718,
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
  &#x27;anthropic/claude-fable-5.1&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-fable-5.1&quot;,
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

- [Input schema](/ai/models/anthropic/claude-fable-5.1/schema-input.json)
- [Output schema](/ai/models/anthropic/claude-fable-5.1/schema-output.json)

