---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/anthropic/claude-fable-5/
  description: anthropic/claude-fable-5
  full_title: Claude Fable 5 · Cloudflare AI docs
  head_html: <title>Claude Fable 5 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="anthropic/claude-fable-5"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/anthropic/claude-fable-5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Claude Fable 5 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="anthropic/claude-fable-5"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/anthropic/claude-fable-5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/anthropic/claude-fable-5/#page","headline":"Claude Fable 5 \u00b7 Cloudflare AI docs","description":"anthropic/claude-fable-5","url":"https://developers.cloudflare.com/ai/models/anthropic/claude-fable-5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/anthropic/claude-fable-5/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/anthropic.svg" alt="Anthropic logo" width="48" height="48">

<h1 id="claude-fable-5">Claude Fable 5</h1>

<p><code>anthropic/claude-fable-5</code></p>

Claude Fable 5 is Anthropic's most capable widely released model, built for the most demanding reasoning and long-horizon agentic work. Adaptive thinking is always on, and the model supports a 1M token context window with up to 128k output tokens per request.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://www.anthropic.com/legal/commercial-terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 10, Output tokens (per 1M): 50, Cached input tokens (per 1M): 1, Cache creation tokens (per 1M): 12.5</td></tr>
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
    &quot;text&quot;: &quot;# The Three Laws of Thermodynamics\n\n## First Law: Conservation of Energy\nEnergy cannot be created or destroyed\u2014only converted from one form to another. The total energy of an isolated system remains constant.\n\n**Formula:** \u0394U = Q \u2212 W (change in internal energy = heat added \u2212 work done by the system)\n\n**Example:** When you burn fuel in an engine, chemical energy converts to heat and mechanical work, but the total energy is conserved.\n\n## Second Law: Entropy Increases\nThe entropy (disorder) of an isolated system always increases over time. Heat flows spontaneously from hot objects to cold ones, never the reverse.\n\n**Key implications:**\n- No heat engine can be 100% efficient\n- Natural processes are irreversible\n- It explains why time seems to have a direction (\&quot;arrow of time\&quot;)\n\n**Example:** An ice cube melts in warm water, but you&#x27;ll never see warm water spontaneously form an ice cube.\n\n## Third Law: Absolute Zero\nAs a system approaches absolute zero (0 Kelvin, or \u2212273.15\u00b0C), its entropy approaches a minimum constant value. It&#x27;s impossible to reach absolute zero in a finite number of steps.\n\n**Example:** Scientists can get extremely close to absolute zero (billionths of a degree above), but never quite reach it.\n\n---\n\n**Bonus \u2014 The Zeroth Law:** Added later but considered more fundamental: if two systems are each in thermal equilibrium with a third system, they&#x27;re in equilibrium with each other. This is what makes thermometers work!\n\nA popular summary: *\&quot;You can&#x27;t win (1st), you can&#x27;t break even (2nd), and you can&#x27;t quit the game (3rd).\&quot;*&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_01TEGjkVwYzfuHrCs5V1Q9de&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;&quot;,
        &quot;signature&quot;: &quot;CAISqAIKYggOGAIqQOscSUEIqskVCTFKJ0i4W90Fia0m32aS+8j6gvpJQkVwCImYZvUlLT0ngohDiWPGx+uORrrkI5qUFGBXijU7UVkyDmNsYXVkZS1mYWJsZS01OAFCCHRoaW5raW5nEgwqVZaKUtMPjtT1ZB8aDHzMnpu8xeeshAEKESIwKiCTZBZGAysSVswoEkB20VfYeJeeMBAqcVEwop/ut0LXzwhnDUAEAYUg4kSv39yWKnTO/ICIz4jCyl7L4SMQd616l3PD2uCuyJRUtqnFLO40PxXgwz8fizzEJMSwFXcjTAkEOdo16C6bHJ7kahwYdjcrrvbQV8OFn0555bExOWsJYiTZVdRrO9XgzDVohWsByfew+FJU7cg/MhO5wA3FikOmOP01pBgB&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;# The Three Laws of Thermodynamics\n\n## First Law: Conservation of Energy\nEnergy cannot be created or destroyed\u2014only converted from one form to another. The total energy of an isolated system remains constant.\n\n**Formula:** \u0394U = Q \u2212 W (change in internal energy = heat added \u2212 work done by the system)\n\n**Example:** When you burn fuel in an engine, chemical energy converts to heat and mechanical work, but the total energy is conserved.\n\n## Second Law: Entropy Increases\nThe entropy (disorder) of an isolated system always increases over time. Heat flows spontaneously from hot objects to cold ones, never the reverse.\n\n**Key implications:**\n- No heat engine can be 100% efficient\n- Natural processes are irreversible\n- It explains why time seems to have a direction (\&quot;arrow of time\&quot;)\n\n**Example:** An ice cube melts in warm water, but you&#x27;ll never see warm water spontaneously form an ice cube.\n\n## Third Law: Absolute Zero\nAs a system approaches absolute zero (0 Kelvin, or \u2212273.15\u00b0C), its entropy approaches a minimum constant value. It&#x27;s impossible to reach absolute zero in a finite number of steps.\n\n**Example:** Scientists can get extremely close to absolute zero (billionths of a degree above), but never quite reach it.\n\n---\n\n**Bonus \u2014 The Zeroth Law:** Added later but considered more fundamental: if two systems are each in thermal equilibrium with a third system, they&#x27;re in equilibrium with each other. This is what makes thermometers work!\n\nA popular summary: *\&quot;You can&#x27;t win (1st), you can&#x27;t break even (2nd), and you can&#x27;t quit the game (3rd).\&quot;*&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-fable-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 20,
      &quot;output_tokens&quot;: 577
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-fable-5&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-fable-5&quot;,
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
    &quot;text&quot;: &quot;# Reading a JSON File in Python\n\nUse the built-in `json` module with the `json.load()` function:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\n## Key Points\n\n- **`json.load(file)`** \u2014 reads JSON from a *file object*\n- **`json.loads(string)`** \u2014 parses JSON from a *string* (note the \&quot;s\&quot;)\n- The `with` statement automatically closes the file when done\n\n## Accessing the Data\n\nJSON objects become Python dictionaries, and JSON arrays become lists:\n\n```python\n# Given data.json:\n# {\n#   \&quot;name\&quot;: \&quot;Alice\&quot;,\n#   \&quot;age\&quot;: 30,\n#   \&quot;hobbies\&quot;: [\&quot;reading\&quot;, \&quot;coding\&quot;]\n# }\n\nprint(data[\&quot;name\&quot;])        # Alice\nprint(data[\&quot;age\&quot;])         # 30\nprint(data[\&quot;hobbies\&quot;][0])  # reading\n```\n\n## Handling Errors\n\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n        data = json.load(file)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError as e:\n    print(f\&quot;Invalid JSON: {e}\&quot;)\n```\n\n## Type Conversions\n\n| JSON | Python |\n|------|--------|\n| object | `dict` |\n| array | `list` |\n| string | `str` |\n| number | `int` / `float` |\n| `true` / `false` | `True` / `False` |\n| `null` | `None` |\n\nThat&#x27;s all you need for most use cases. For very large files, consider streaming libraries like `ijson`.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_013oB35i6D6cJW17UoavzSEs&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;&quot;,
        &quot;signature&quot;: &quot;CAIS9wEKYggOGAIqQFeZ1YZ5RyQ9EbHCqt5fSx9vMAMrhvdbZ+CLKMjT6OXEkD0ktq1p+6St3xTcEVpxkyLpemCD799ZbfCwYd+hJ8wyDmNsYXVkZS1mYWJsZS01OAFCCHRoaW5raW5nEgzx2jYo+ujge2+SskIaDHjgiplZQMyTmf+LNyIwXid3ttbHyXFgieCEovuD3vs0EsVznHmbkYlIY9NyF+a/dx04UlNIrelymYxnEZX7KkPe1UpvY5zXlRmwx3hSBIEFA9FHalSXG7jipEwzoJeyxon8+/rF/zkHacZuq8melq/TmwNzVE4jNU6rDEuvJO0C4l9dGAE=&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;# Reading a JSON File in Python\n\nUse the built-in `json` module with the `json.load()` function:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\n## Key Points\n\n- **`json.load(file)`** \u2014 reads JSON from a *file object*\n- **`json.loads(string)`** \u2014 parses JSON from a *string* (note the \&quot;s\&quot;)\n- The `with` statement automatically closes the file when done\n\n## Accessing the Data\n\nJSON objects become Python dictionaries, and JSON arrays become lists:\n\n```python\n# Given data.json:\n# {\n#   \&quot;name\&quot;: \&quot;Alice\&quot;,\n#   \&quot;age\&quot;: 30,\n#   \&quot;hobbies\&quot;: [\&quot;reading\&quot;, \&quot;coding\&quot;]\n# }\n\nprint(data[\&quot;name\&quot;])        # Alice\nprint(data[\&quot;age\&quot;])         # 30\nprint(data[\&quot;hobbies\&quot;][0])  # reading\n```\n\n## Handling Errors\n\n```python\nimport json\n\ntry:\n    with open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as file:\n        data = json.load(file)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError as e:\n    print(f\&quot;Invalid JSON: {e}\&quot;)\n```\n\n## Type Conversions\n\n| JSON | Python |\n|------|--------|\n| object | `dict` |\n| array | `list` |\n| string | `str` |\n| number | `int` / `float` |\n| `true` / `false` | `True` / `False` |\n| `null` | `None` |\n\nThat&#x27;s all you need for most use cases. For very large files, consider streaming libraries like `ijson`.&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-fable-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 38,
      &quot;output_tokens&quot;: 537
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-fable-5&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-fable-5&quot;,
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

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a conversation with context</p>
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
    &quot;text&quot;: &quot;Great question! Your stops depend a lot on which route you take, so let me break it down:\n\n## Highway 1 / Pacific Coast Highway (Scenic Route)\nThis adds significant time (10+ hours of driving) but is one of the most beautiful drives in the world:\n\n- **Half Moon Bay** \u2013 Charming coastal town, great for breakfast\n- **Santa Cruz** \u2013 Beach boardwalk and surf culture\n- **Monterey &amp; Carmel** \u2013 World-class aquarium, scenic 17-Mile Drive\n- **Big Sur** \u2013 Stunning cliffs, Bixby Bridge, McWay Falls, redwood hikes\n- **San Simeon** \u2013 Hearst Castle and elephant seal viewing at Piedras Blancas\n- **Morro Bay** \u2013 Iconic Morro Rock\n- **Pismo Beach** \u2013 Classic beach town vibes\n- **Santa Barbara** \u2013 Beautiful Spanish architecture, wine country nearby\n- **Malibu** \u2013 Beaches and a great way to roll into LA\n\n## Highway 101 (Balanced Option, ~7-8 hours)\n- **San Jose** \u2013 Winchester Mystery House\n- **Gilroy** \u2013 Garlic capital (and outlet shopping)\n- **Paso Robles** \u2013 Excellent wine region\n- **San Luis Obispo** \u2013 Cute college town, Bubblegum Alley\n- **Solvang** \u2013 Quirky Danish village with bakeries and windmills\n- **Santa Barbara** \u2013 Same as above\n\n## I-5 (Fastest, ~5-6 hours)\nHonestly, not much to see\u2014mostly farmland. Best stop is **Harris Ranch** in Coalinga for a famous steak lunch.\n\n**My suggestion:** If you have 2+ days, take Highway 1 and stay overnight in Monterey, Big Sur, or San Luis Obispo. If you only have one day, 101 gives you a nice mix of speed and scenery.\n\nHow much time do you have for the trip? That&#x27;ll help narrow down the best plan!&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_01JoMwDGJCvYbHtRYpMaaVCp&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;&quot;,
        &quot;signature&quot;: &quot;CAISnQIKYggOGAIqQK/zBQqMA66bUkZi524Lt0j+w8Eutw4fEZezWpC3T8DkRpnoqnfcGJL1WYXiD+kMGT1/gHSAjBTaezw2E8x5XM8yDmNsYXVkZS1mYWJsZS01OAFCCHRoaW5raW5nEgzQCE8UtUZmIwbubiUaDJd3PUdinhPnsMTDyCIwM6zPNTJBliPRjAxg0rXfsMOgkpBJ2f4PsQF8Qx1/OOnBTzzeThC3LqMxwIvRLQNpKmnrVhJc59urfrUjH5w+2LZJMmRg0KiCqdpSRx65zmj0us3grXlxJ5+5KQkaZMILR038gQ1uVGAQ6IhEzj2LaC5fGMRuo9onFlGkksp3s+gb1jaNoo7hEgxzzD+1GPmhtahCBIrXsJUBctAYAQ==&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Great question! Your stops depend a lot on which route you take, so let me break it down:\n\n## Highway 1 / Pacific Coast Highway (Scenic Route)\nThis adds significant time (10+ hours of driving) but is one of the most beautiful drives in the world:\n\n- **Half Moon Bay** \u2013 Charming coastal town, great for breakfast\n- **Santa Cruz** \u2013 Beach boardwalk and surf culture\n- **Monterey &amp; Carmel** \u2013 World-class aquarium, scenic 17-Mile Drive\n- **Big Sur** \u2013 Stunning cliffs, Bixby Bridge, McWay Falls, redwood hikes\n- **San Simeon** \u2013 Hearst Castle and elephant seal viewing at Piedras Blancas\n- **Morro Bay** \u2013 Iconic Morro Rock\n- **Pismo Beach** \u2013 Classic beach town vibes\n- **Santa Barbara** \u2013 Beautiful Spanish architecture, wine country nearby\n- **Malibu** \u2013 Beaches and a great way to roll into LA\n\n## Highway 101 (Balanced Option, ~7-8 hours)\n- **San Jose** \u2013 Winchester Mystery House\n- **Gilroy** \u2013 Garlic capital (and outlet shopping)\n- **Paso Robles** \u2013 Excellent wine region\n- **San Luis Obispo** \u2013 Cute college town, Bubblegum Alley\n- **Solvang** \u2013 Quirky Danish village with bakeries and windmills\n- **Santa Barbara** \u2013 Same as above\n\n## I-5 (Fastest, ~5-6 hours)\nHonestly, not much to see\u2014mostly farmland. Best stop is **Harris Ranch** in Coalinga for a famous steak lunch.\n\n**My suggestion:** If you have 2+ days, take Highway 1 and stay overnight in Monterey, Big Sur, or San Luis Obispo. If you only have one day, 101 gives you a nice mix of speed and scenery.\n\nHow much time do you have for the trip? That&#x27;ll help narrow down the best plan!&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-fable-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 103,
      &quot;output_tokens&quot;: 706
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-fable-5&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-fable-5&quot;,
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

<section class="model-example"><strong>Creative Writing with Adaptive Thinking</strong>
<p>Use adaptive thinking with high effort to steer creative output. Adaptive thinking is always on for Claude Fable 5; use the `effort` parameter to control depth.</p>
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
    &quot;text&quot;: &quot;# The Paper Bird\n\nDetective Mara Voss had worked homicide for eleven years, and in that time she&#x27;d catalogued every variety of crime scene debris: shell casings, cigarette butts, the sad confetti of torn receipts. But she had never found an origami crane perched in a dead man&#x27;s open palm.\n\nThe victim\u2014Gerald Fitch, fifty-three, accountant\u2014lay sprawled across his kitchen floor as though he&#x27;d simply decided to stop standing. No wounds. No struggle. Just the crane, folded from heavy cream paper, balanced on his hand like it had landed there of its own accord.\n\n\&quot;Don&#x27;t touch it,\&quot; she said, though the rookie behind her hadn&#x27;t moved. She crouched, knees popping, and angled her flashlight at the paper bird. There\u2014faint lines beneath the folds. Writing.\n\nShe photographed it from six angles before lifting it with gloved fingers, and unfolded it wing by wing with the care of someone defusing a bomb. The creases gave up their secret slowly: a single sentence, written in tight, slanted script.\n\n*He counted everything except his sins.*\n\nMara read it three times. Then she looked back at Gerald Fitch&#x27;s face\u2014peaceful, almost smug, even in death\u2014and felt the familiar cold prickle at the base of her skull. The one that told her this wasn&#x27;t an ending.\n\nIt was an invitation.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_01VaGXWd9kdzHMepPnPHTTvG&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;&quot;,
        &quot;signature&quot;: &quot;CAISxgIKYggOGAIqQCa14WJvO05NEThN13nBXzVEqA35Ki9nluIV0epwzd5nZM6Iyotcv9JA6vAh21iikvC/FNzJso0wR6JiUwir4ekyDmNsYXVkZS1mYWJsZS01OAFCCHRoaW5raW5nEgz1lKb9mdSCyv6XyPsaDNpKckL3pPM/5C9mkSIwNQrKl5lQs1F2p+1lxVtoAuthy8llMmyUgpy1coZQ4fmw3wlNJI98aNDajf9r3hGoKpEBiMAXur1Qp83FUupryf2Y2xHOMcH9MWev85QNIzNZapR30GC3aD1nTWv2a2cAUy9fZN+nEnPTstS8Wga900d1vDmhu42Yv+45MaE6Oa6syHzBO3+bSCZ/jioWSQxGhxw8jwGhR6DC6mp2iDYZGKpTExw7WftcL6mYpKgBus50atpeUCWXi7/IdHqDUkPRyb1LRxgB&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;# The Paper Bird\n\nDetective Mara Voss had worked homicide for eleven years, and in that time she&#x27;d catalogued every variety of crime scene debris: shell casings, cigarette butts, the sad confetti of torn receipts. But she had never found an origami crane perched in a dead man&#x27;s open palm.\n\nThe victim\u2014Gerald Fitch, fifty-three, accountant\u2014lay sprawled across his kitchen floor as though he&#x27;d simply decided to stop standing. No wounds. No struggle. Just the crane, folded from heavy cream paper, balanced on his hand like it had landed there of its own accord.\n\n\&quot;Don&#x27;t touch it,\&quot; she said, though the rookie behind her hadn&#x27;t moved. She crouched, knees popping, and angled her flashlight at the paper bird. There\u2014faint lines beneath the folds. Writing.\n\nShe photographed it from six angles before lifting it with gloved fingers, and unfolded it wing by wing with the care of someone defusing a bomb. The creases gave up their secret slowly: a single sentence, written in tight, slanted script.\n\n*He counted everything except his sins.*\n\nMara read it three times. Then she looked back at Gerald Fitch&#x27;s face\u2014peaceful, almost smug, even in death\u2014and felt the familiar cold prickle at the base of her skull. The one that told her this wasn&#x27;t an ending.\n\nIt was an invitation.&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-fable-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 26,
      &quot;output_tokens&quot;: 487
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-fable-5&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-fable-5&quot;,
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
      &quot;#&quot;,
      &quot; Recursion\n\n**Recursion** is a programming concept where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems&quot;,
      &quot;.\n\n## Key Components\n\nEvery recursive function needs two parts:\n\n1. **Base case** \u2014 a condition that stops the recursion (prevents infinite loops)\n2. **&quot;,
      &quot;Recursive case** \u2014 where the function calls itself with a smaller/simpler input\n\n## Simple Example: Factorial\n\nThe factorial of a number `&quot;,
      &quot;n` (written `n!`) is the product of all positive integers up to `n`:\n\n- `5! = 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 = 120`\n\nNotice&quot;,
      &quot; the pattern: `5! = 5 \u00d7 4!` \u2014 the problem contains a smaller version of itself.&quot;,
      &quot; Perfect for recursion!\n\n```python\ndef factorial(n):\n    if n &lt;= 1:          # Base case\n        return 1\n    else:               # Recursive case\n        &quot;,
      &quot;return n * factorial(n - 1)\n\nprint(factorial(5))  # Output: 120\n```\n\n## How It Unfolds\n\n```\nfactorial(5)\n= 5 \u00d7 factorial(&quot;,
      &quot;4)\n= 5 \u00d7 4 \u00d7 factorial(3)\n= 5 \u00d7 4 \u00d7 3 \u00d7 factorial(2)\n= 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 factorial(1)\n=&quot;,
      &quot; 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1      \u2190 base case reached\n= 120\n```\n\nThe calls \&quot;stack up\&quot; until h&quot;,
      &quot;itting the base case, then results are multiplied back up the chain.\n\n## An Intuitive Analogy\n\nImagine you&#x27;re in&quot;,
      &quot; a movie theater line and want to know your position. Instead of counting everyone yourself, you ask the person in front of you,&quot;,
      &quot; \&quot;What&#x27;s your position?\&quot; They ask the person in front of them... until someone at the front says \&quot;I&#x27;m first!\&quot; (base case). Then each person adds 1 and&quot;,
      &quot; passes the answer back.\n\n## When to Use Recursion\n\nRecursion shines for naturally recursive structures like&quot;,
      &quot;:\n- Tree traversal\n- Directory/file systems\n- Divide-and-conquer algorithms (e.g., merge sort)&quot;,
      &quot;\n\n\u26a0\ufe0f **Caution:** Without a proper base case, recursion runs forever and causes a *stack overflow*.&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;type&quot;: &quot;message_start&quot;,
      &quot;message&quot;: {
        &quot;model&quot;: &quot;claude-fable-5&quot;,
        &quot;id&quot;: &quot;msg_01Rwmx9xySGeaRDPFstZ7gMV&quot;,
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
        &quot;text&quot;: &quot;#&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; Recursion\n\n**Recursion** is a programming concept where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;.\n\n## Key Components\n\nEvery recursive function needs two parts:\n\n1. **Base case** \u2014 a condition that stops the recursion (prevents infinite loops)\n2. **&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;Recursive case** \u2014 where the function calls itself with a smaller/simpler input\n\n## Simple Example: Factorial\n\nThe factorial of a number `&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;n` (written `n!`) is the product of all positive integers up to `n`:\n\n- `5! = 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 = 120`\n\nNotice&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; the pattern: `5! = 5 \u00d7 4!` \u2014 the problem contains a smaller version of itself.&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; Perfect for recursion!\n\n```python\ndef factorial(n):\n    if n &lt;= 1:          # Base case\n        return 1\n    else:               # Recursive case\n        &quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;return n * factorial(n - 1)\n\nprint(factorial(5))  # Output: 120\n```\n\n## How It Unfolds\n\n```\nfactorial(5)\n= 5 \u00d7 factorial(&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;4)\n= 5 \u00d7 4 \u00d7 factorial(3)\n= 5 \u00d7 4 \u00d7 3 \u00d7 factorial(2)\n= 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 factorial(1)\n=&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1      \u2190 base case reached\n= 120\n```\n\nThe calls \&quot;stack up\&quot; until h&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;itting the base case, then results are multiplied back up the chain.\n\n## An Intuitive Analogy\n\nImagine you&#x27;re in&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; a movie theater line and want to know your position. Instead of counting everyone yourself, you ask the person in front of you,&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; \&quot;What&#x27;s your position?\&quot; They ask the person in front of them... until someone at the front says \&quot;I&#x27;m first!\&quot; (base case). Then each person adds 1 and&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot; passes the answer back.\n\n## When to Use Recursion\n\nRecursion shines for naturally recursive structures like&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;:\n- Tree traversal\n- Directory/file systems\n- Divide-and-conquer algorithms (e.g., merge sort)&quot;
      }
    },
    {
      &quot;type&quot;: &quot;content_block_delta&quot;,
      &quot;index&quot;: 0,
      &quot;delta&quot;: {
        &quot;type&quot;: &quot;text_delta&quot;,
        &quot;text&quot;: &quot;\n\n\u26a0\ufe0f **Caution:** Without a proper base case, recursion runs forever and causes a *stack overflow*.&quot;
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
        &quot;output_tokens&quot;: 689,
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
  &#x27;anthropic/claude-fable-5&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-fable-5&quot;,
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

- [Input schema](/ai/models/anthropic/claude-fable-5/schema-input.json)
- [Output schema](/ai/models/anthropic/claude-fable-5/schema-output.json)

