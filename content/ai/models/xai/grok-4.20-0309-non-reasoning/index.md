<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-4-20-non-reasoning">Grok 4.20 Non-Reasoning</h1>

<p><code>xai/grok-4.20-0309-non-reasoning</code></p>

xAI's Grok 4.20 non-reasoning model. Skips the thinking trace for fast, single-pass responses while keeping the same training as the reasoning variant.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>2,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 6, Cached input tokens (per 1M): 0.2</td></tr>
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
    &quot;text&quot;: &quot;**The Three Laws of Thermodynamics** (in their most common, concise form):\n\n### **Zeroth Law of Thermodynamics** (often called the \&quot;zeroth\&quot; because it logically precedes the others)\n&gt; If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other.\n\nThis is the basis for the concept of **temperature** \u2014 it allows us to define a universal temperature scale.\n\n### **First Law of Thermodynamics**\n&gt; Energy cannot be created or destroyed, only converted from one form to another.\n\nMathematically:  \n**\u0394U = Q \u2212 W**  \n(where \u0394U is the change in internal energy, Q is heat added to the system, and W is work done *by* the system)\n\nThis is essentially the **law of conservation of energy** applied to thermodynamic systems.\n\n### **Second Law of Thermodynamics**\n&gt; The entropy of an isolated system always increases over time, or remains constant in ideal reversible processes. Heat flows spontaneously from hot to cold, never the reverse.\n\nCommon statements:\n- \&quot;The entropy of the universe tends to a maximum.\&quot;\n- \&quot;It is impossible to construct a heat engine that is 100% efficient.\&quot;\n\nThis law introduces the concept of **irreversibility** and the **arrow of time**.\n\n---\n\n### Bonus: The **Third Law of Thermodynamics** (Nernst Heat Theorem)\n&gt; As the temperature of a system approaches absolute zero (0 K), the entropy of a perfect crystal approaches a minimum (usually zero).\n\nThis implies it&#x27;s impossible to reach absolute zero in a finite number of steps.\n\n---\n\n**Summary (popular phrasing):**\n1. **Zeroth**: Temperature exists.\n2. **First**: You can&#x27;t win (energy is conserved).\n3. **Second**: You can&#x27;t break even (entropy always increases).\n4. **Third**: You can&#x27;t even quit the game (absolute zero is unreachable).&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;**The Three Laws of Thermodynamics** (in their most common, concise form):\n\n### **Zeroth Law of Thermodynamics** (often called the \&quot;zeroth\&quot; because it logically precedes the others)\n&gt; If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other.\n\nThis is the basis for the concept of **temperature** \u2014 it allows us to define a universal temperature scale.\n\n### **First Law of Thermodynamics**\n&gt; Energy cannot be created or destroyed, only converted from one form to another.\n\nMathematically:  \n**\u0394U = Q \u2212 W**  \n(where \u0394U is the change in internal energy, Q is heat added to the system, and W is work done *by* the system)\n\nThis is essentially the **law of conservation of energy** applied to thermodynamic systems.\n\n### **Second Law of Thermodynamics**\n&gt; The entropy of an isolated system always increases over time, or remains constant in ideal reversible processes. Heat flows spontaneously from hot to cold, never the reverse.\n\nCommon statements:\n- \&quot;The entropy of the universe tends to a maximum.\&quot;\n- \&quot;It is impossible to construct a heat engine that is 100% efficient.\&quot;\n\nThis law introduces the concept of **irreversibility** and the **arrow of time**.\n\n---\n\n### Bonus: The **Third Law of Thermodynamics** (Nernst Heat Theorem)\n&gt; As the temperature of a system approaches absolute zero (0 K), the entropy of a perfect crystal approaches a minimum (usually zero).\n\nThis implies it&#x27;s impossible to reach absolute zero in a finite number of steps.\n\n---\n\n**Summary (popular phrasing):**\n1. **Zeroth**: Temperature exists.\n2. **First**: You can&#x27;t win (energy is conserved).\n3. **Second**: You can&#x27;t break even (entropy always increases).\n4. **Third**: You can&#x27;t even quit the game (absolute zero is unreachable).&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777675694,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;ad22f976-34a4-e1f2-5d44-2c6b9c2fb9e5&quot;,
    &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 378,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;cost_in_usd_ticks&quot;: 10403000,
      &quot;num_sources_used&quot;: 0,
      &quot;prompt_tokens&quot;: 130,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 64,
        &quot;image_tokens&quot;: 0,
        &quot;text_tokens&quot;: 130
      },
      &quot;total_tokens&quot;: 508
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-0309-non-reasoning&#x27;,
  { messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.20-0309-non-reasoning&quot;,
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
    &quot;text&quot;: &quot;**Reading a JSON file in Python** is very straightforward using the built-in `json` module.\n\n### 1. Basic Method (Recommended)\n\n```python\nimport json\nfrom pathlib import Path\n\n# Method 1: Using pathlib (modern and clean)\ndef read_json_file(file_path):\n    with open(file_path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n        data = json.load(file)\n    return data\n\n# Usage\ndata = read_json_file(&#x27;data.json&#x27;)\nprint(data)\n```\n\n### 2. Most Common Patterns\n\n```python\nimport json\n\n# Option 1: Using pathlib (Recommended)\ndata = json.loads(Path(&#x27;data.json&#x27;).read_text(encoding=&#x27;utf-8&#x27;))\n\n# Option 2: Traditional way\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n    data = json.load(f)\n\n# Option 3: One-liner\ndata = json.load(open(&#x27;data.json&#x27;, encoding=&#x27;utf-8&#x27;))\n```\n\n### 3. Complete Example with Error Handling\n\n```python\nimport json\nfrom pathlib import Path\nfrom typing import Any\n\ndef read_json(file_path: str | Path) -&gt; Any:\n    \&quot;\&quot;\&quot;Safely read a JSON file with proper error handling.\&quot;\&quot;\&quot;\n    try:\n        path = Path(file_path)\n        with open(path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n            return json.load(file)\n            \n    except FileNotFoundError:\n        print(f\&quot;Error: File &#x27;{file_path}&#x27; not found.\&quot;)\n        return None\n    except json.JSONDecodeError as e:\n        print(f\&quot;Error: Invalid JSON in &#x27;{file_path}&#x27;: {e}\&quot;)\n        return None\n    except Exception as e:\n        print(f\&quot;Unexpected error reading &#x27;{file_path}&#x27;: {e}\&quot;)\n        return None\n\n\n# Usage examples:\ndata = read_json(&#x27;config.json&#x27;)\ndata = read_json(Path(&#x27;data/settings.json&#x27;))\n\n# Access the data\nif data:\n    print(data.get(&#x27;name&#x27;))\n    print(data[&#x27;users&#x27;][0][&#x27;email&#x27;])\n```\n\n### Key Points:\n\n- Use `json.load()` when reading from a **file object**\n- Use `json.loads()` when reading from a **string**\n- Always specify `encoding=&#x27;utf-8&#x27;` (best practice)\n- Use `pathlib.Path` for modern Python code\n- Always handle potential `JSONDecodeError` and `FileNotFoundError`\n\nWould you like to see how to also **write** JSON files or work with specific JSON structures (like configurations, lists of objects, etc.)?&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;**Reading a JSON file in Python** is very straightforward using the built-in `json` module.\n\n### 1. Basic Method (Recommended)\n\n```python\nimport json\nfrom pathlib import Path\n\n# Method 1: Using pathlib (modern and clean)\ndef read_json_file(file_path):\n    with open(file_path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n        data = json.load(file)\n    return data\n\n# Usage\ndata = read_json_file(&#x27;data.json&#x27;)\nprint(data)\n```\n\n### 2. Most Common Patterns\n\n```python\nimport json\n\n# Option 1: Using pathlib (Recommended)\ndata = json.loads(Path(&#x27;data.json&#x27;).read_text(encoding=&#x27;utf-8&#x27;))\n\n# Option 2: Traditional way\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n    data = json.load(f)\n\n# Option 3: One-liner\ndata = json.load(open(&#x27;data.json&#x27;, encoding=&#x27;utf-8&#x27;))\n```\n\n### 3. Complete Example with Error Handling\n\n```python\nimport json\nfrom pathlib import Path\nfrom typing import Any\n\ndef read_json(file_path: str | Path) -&gt; Any:\n    \&quot;\&quot;\&quot;Safely read a JSON file with proper error handling.\&quot;\&quot;\&quot;\n    try:\n        path = Path(file_path)\n        with open(path, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n            return json.load(file)\n            \n    except FileNotFoundError:\n        print(f\&quot;Error: File &#x27;{file_path}&#x27; not found.\&quot;)\n        return None\n    except json.JSONDecodeError as e:\n        print(f\&quot;Error: Invalid JSON in &#x27;{file_path}&#x27;: {e}\&quot;)\n        return None\n    except Exception as e:\n        print(f\&quot;Unexpected error reading &#x27;{file_path}&#x27;: {e}\&quot;)\n        return None\n\n\n# Usage examples:\ndata = read_json(&#x27;config.json&#x27;)\ndata = read_json(Path(&#x27;data/settings.json&#x27;))\n\n# Access the data\nif data:\n    print(data.get(&#x27;name&#x27;))\n    print(data[&#x27;users&#x27;][0][&#x27;email&#x27;])\n```\n\n### Key Points:\n\n- Use `json.load()` when reading from a **file object**\n- Use `json.loads()` when reading from a **string**\n- Always specify `encoding=&#x27;utf-8&#x27;` (best practice)\n- Use `pathlib.Path` for modern Python code\n- Always handle potential `JSONDecodeError` and `FileNotFoundError`\n\nWould you like to see how to also **write** JSON files or work with specific JSON structures (like configurations, lists of objects, etc.)?&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777675694,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;90c95869-a6c3-9a03-95d1-32f6a41a14ca&quot;,
    &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 521,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;cost_in_usd_ticks&quot;: 14165500,
      &quot;num_sources_used&quot;: 0,
      &quot;prompt_tokens&quot;: 145,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 64,
        &quot;image_tokens&quot;: 0,
        &quot;text_tokens&quot;: 145
      },
      &quot;total_tokens&quot;: 666
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-0309-non-reasoning&#x27;,
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
  &quot;model&quot;: &quot;xai/grok-4.20-0309-non-reasoning&quot;,
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
    &quot;text&quot;: &quot;Here are some excellent stops along (or just off) the main routes from San Francisco to Los Angeles. I\u2019ve grouped them roughly in north-to-south order so you can slot them into your itinerary easily.\n\n### Classic Coastal Route (Highway 1 / Pacific Coast Highway)\nThis is the most scenic option and the one most people picture when they say \u201croad trip from SF to LA.\u201d\n\n1. **Half Moon Bay** (\u2248 30 min south of SF)  \n   - Cute coastal town with beaches, tide pools, and the famous \u201cPumpkin Festival\u201d in October. Great for a quick coffee or beach walk.\n\n2. **Pescadero &amp; A\u00f1o Nuevo State Park** (\u2248 1 hr from SF)  \n   - Stop at **Duarte\u2019s Tavern** for artichoke soup and pie. A\u00f1o Nuevo has elephant seals (best Dec\u2013March).\n\n3. **Santa Cruz** (\u2248 1.5 hrs from SF)  \n   - Beach Boardwalk, redwood hikes in Henry Cowell Redwoods, or the famous surf at Pleasure Point. Good food scene.\n\n4. **Monterey &amp; Pacific Grove** (\u2248 2 hrs from SF)  \n   - Cannery Row, Monterey Bay Aquarium (book ahead), 17-Mile Drive, and the monarch butterfly sanctuary in Pacific Grove (Oct\u2013Feb).\n\n5. **Big Sur** (\u2248 3\u20134 hrs from SF \u2013 the heart of the drive)  \n   - **Bixby Bridge** photo stop  \n   - **Point Sur Lighthouse** (tours available)  \n   - **Julia Pfeiffer Burns State Park** \u2013 McWay Falls (waterfall onto the beach)  \n   - **Pfeiffer Beach** \u2013 purple sand and keyhole rock  \n   - **Nepenthe** or **Big Sur Bakery** for lunch with a view  \n   - **Ventana Big Sur** or **Post Ranch Inn** if you want an upscale overnight.\n\n6. **Cambria / Hearst Castle** (\u2248 5\u20136 hrs from SF)  \n   - Tour the famous Hearst Castle (reservations required).  \n   - Moonstone Beach boardwalk for sunset.\n\n7. **San Luis Obispo (SLO)** (\u2248 6.5 hrs from SF)  \n   - Bubblegum Alley, great farm-to-table food, and a lively downtown.\n\n8. **Pismo Beach**  \n   - Classic California beach town with sand dunes you can drive on (ATV tours available).\n\n9. **Solvang** (short detour)  \n   - Danish-themed village with windmills, bakeries, and \u00c6bleskiver pancakes. Fun for 1\u20132 hours.\n\n10. **Santa Barbara** (\u2248 8\u20139 hrs from SF if you linger)  \n    - \u201cAmerican Riviera.\u201d State Street for shopping, Mission Santa Barbara, beaches, and wine tasting in the Funk Zone.\n\n11. **Malibu** (final stretch before LA)  \n    - Point Dume, El Matador Beach, or a sunset dinner at Malibu Pier.\n\n### Inland / Faster Route Highlights (I-5 corridor)\nIf you\u2019re short on time but still want stops:\n\n- **Gilroy** \u2013 \u201cGarlic Capital of the World\u201d (garlic ice cream if you\u2019re brave).\n- **Pacheco Pass** \u2192 **San Luis Reservoir** for dramatic views.\n- **Harris Ranch** \u2013 iconic Central Valley steakhouse stop.\n- **Bakersfield** \u2013 for Basque food or country-music vibes.\n- **Tejon Pass / Magic Mountain** \u2013 quick amusement-park option.\n\n### Suggested Itineraries\n\n**Scenic 2-Day Trip (most popular)**  \nDay 1: SF \u2192 Big Sur (overnight in Big Sur or Cambria)  \nDay 2: Big Sur \u2192 Santa Barbara \u2192 LA\n\n**3-Day Leisure Trip**  \nDay 1: SF \u2192 Monterey / Carmel (overnight)  \nDay 2: Monterey \u2192 Cambria / Hearst Castle \u2192 SLO (overnight)  \nDay 3: SLO \u2192 Santa Barbara \u2192 Malibu \u2192 LA\n\nWould you like me to:\n- Build a day-by-day itinerary with driving times and restaurant recommendations?\n- Focus on specific interests (hiking, food, photography, wine, budget, luxury, etc.)?\n- Include where to stay or current road conditions / permit info for Big Sur?\n\nJust let me know your preferences (how many days, budget level, must-see activities, etc.) and I\u2019ll tailor it further!&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;Here are some excellent stops along (or just off) the main routes from San Francisco to Los Angeles. I\u2019ve grouped them roughly in north-to-south order so you can slot them into your itinerary easily.\n\n### Classic Coastal Route (Highway 1 / Pacific Coast Highway)\nThis is the most scenic option and the one most people picture when they say \u201croad trip from SF to LA.\u201d\n\n1. **Half Moon Bay** (\u2248 30 min south of SF)  \n   - Cute coastal town with beaches, tide pools, and the famous \u201cPumpkin Festival\u201d in October. Great for a quick coffee or beach walk.\n\n2. **Pescadero &amp; A\u00f1o Nuevo State Park** (\u2248 1 hr from SF)  \n   - Stop at **Duarte\u2019s Tavern** for artichoke soup and pie. A\u00f1o Nuevo has elephant seals (best Dec\u2013March).\n\n3. **Santa Cruz** (\u2248 1.5 hrs from SF)  \n   - Beach Boardwalk, redwood hikes in Henry Cowell Redwoods, or the famous surf at Pleasure Point. Good food scene.\n\n4. **Monterey &amp; Pacific Grove** (\u2248 2 hrs from SF)  \n   - Cannery Row, Monterey Bay Aquarium (book ahead), 17-Mile Drive, and the monarch butterfly sanctuary in Pacific Grove (Oct\u2013Feb).\n\n5. **Big Sur** (\u2248 3\u20134 hrs from SF \u2013 the heart of the drive)  \n   - **Bixby Bridge** photo stop  \n   - **Point Sur Lighthouse** (tours available)  \n   - **Julia Pfeiffer Burns State Park** \u2013 McWay Falls (waterfall onto the beach)  \n   - **Pfeiffer Beach** \u2013 purple sand and keyhole rock  \n   - **Nepenthe** or **Big Sur Bakery** for lunch with a view  \n   - **Ventana Big Sur** or **Post Ranch Inn** if you want an upscale overnight.\n\n6. **Cambria / Hearst Castle** (\u2248 5\u20136 hrs from SF)  \n   - Tour the famous Hearst Castle (reservations required).  \n   - Moonstone Beach boardwalk for sunset.\n\n7. **San Luis Obispo (SLO)** (\u2248 6.5 hrs from SF)  \n   - Bubblegum Alley, great farm-to-table food, and a lively downtown.\n\n8. **Pismo Beach**  \n   - Classic California beach town with sand dunes you can drive on (ATV tours available).\n\n9. **Solvang** (short detour)  \n   - Danish-themed village with windmills, bakeries, and \u00c6bleskiver pancakes. Fun for 1\u20132 hours.\n\n10. **Santa Barbara** (\u2248 8\u20139 hrs from SF if you linger)  \n    - \u201cAmerican Riviera.\u201d State Street for shopping, Mission Santa Barbara, beaches, and wine tasting in the Funk Zone.\n\n11. **Malibu** (final stretch before LA)  \n    - Point Dume, El Matador Beach, or a sunset dinner at Malibu Pier.\n\n### Inland / Faster Route Highlights (I-5 corridor)\nIf you\u2019re short on time but still want stops:\n\n- **Gilroy** \u2013 \u201cGarlic Capital of the World\u201d (garlic ice cream if you\u2019re brave).\n- **Pacheco Pass** \u2192 **San Luis Reservoir** for dramatic views.\n- **Harris Ranch** \u2013 iconic Central Valley steakhouse stop.\n- **Bakersfield** \u2013 for Basque food or country-music vibes.\n- **Tejon Pass / Magic Mountain** \u2013 quick amusement-park option.\n\n### Suggested Itineraries\n\n**Scenic 2-Day Trip (most popular)**  \nDay 1: SF \u2192 Big Sur (overnight in Big Sur or Cambria)  \nDay 2: Big Sur \u2192 Santa Barbara \u2192 LA\n\n**3-Day Leisure Trip**  \nDay 1: SF \u2192 Monterey / Carmel (overnight)  \nDay 2: Monterey \u2192 Cambria / Hearst Castle \u2192 SLO (overnight)  \nDay 3: SLO \u2192 Santa Barbara \u2192 Malibu \u2192 LA\n\nWould you like me to:\n- Build a day-by-day itinerary with driving times and restaurant recommendations?\n- Focus on specific interests (hiking, food, photography, wine, budget, luxury, etc.)?\n- Include where to stay or current road conditions / permit info for Big Sur?\n\nJust let me know your preferences (how many days, budget level, must-see activities, etc.) and I\u2019ll tailor it further!&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777675700,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;4eb7a1aa-c8a6-9b80-96e0-b49fe3efbb1d&quot;,
    &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 915,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;cost_in_usd_ticks&quot;: 24578000,
      &quot;num_sources_used&quot;: 0,
      &quot;prompt_tokens&quot;: 190,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 64,
        &quot;image_tokens&quot;: 0,
        &quot;text_tokens&quot;: 190
      },
      &quot;total_tokens&quot;: 1105
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-0309-non-reasoning&#x27;,
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
  &quot;model&quot;: &quot;xai/grok-4.20-0309-non-reasoning&quot;,
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
    &quot;text&quot;: &quot;The rain-slicked alley behind the old theater smelled of rotting velvet and gunpowder. Detective Elias Crowe knelt beside the body, his flashlight beam cutting through the downpour, and paused.\n\nThere, clutched in the dead man\u2019s rigid fingers, was a single playing card: the Queen of Hearts. That wasn\u2019t unusual in itself. What stopped Crowe cold was that the card was warm, almost hot, as though it had just come off a printing press. And when he turned it over, the back wasn\u2019t patterned with the usual bicycles or fleurs-de-lis.\n\nIt was a tiny, perfectly detailed photograph of the crime scene itself, taken from an angle that should have been impossible\u2014directly above the body, as if the card had been watching the murder happen.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;The rain-slicked alley behind the old theater smelled of rotting velvet and gunpowder. Detective Elias Crowe knelt beside the body, his flashlight beam cutting through the downpour, and paused.\n\nThere, clutched in the dead man\u2019s rigid fingers, was a single playing card: the Queen of Hearts. That wasn\u2019t unusual in itself. What stopped Crowe cold was that the card was warm, almost hot, as though it had just come off a printing press. And when he turned it over, the back wasn\u2019t patterned with the usual bicycles or fleurs-de-lis.\n\nIt was a tiny, perfectly detailed photograph of the crime scene itself, taken from an angle that should have been impossible\u2014directly above the body, as if the card had been watching the murder happen.&quot;,
          &quot;refusal&quot;: null,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1777675700,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;id&quot;: &quot;ffb95915-83b7-ac06-34d9-f031b0056ab1&quot;,
    &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 154,
      &quot;completion_tokens_details&quot;: {
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0,
        &quot;reasoning_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;cost_in_usd_ticks&quot;: 4865500,
      &quot;num_sources_used&quot;: 0,
      &quot;prompt_tokens&quot;: 135,
      &quot;prompt_tokens_details&quot;: {
        &quot;audio_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 64,
        &quot;image_tokens&quot;: 0,
        &quot;text_tokens&quot;: 135
      },
      &quot;total_tokens&quot;: 289
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-0309-non-reasoning&#x27;,
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
  &quot;model&quot;: &quot;xai/grok-4.20-0309-non-reasoning&quot;,
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
      &quot;Recursion&quot;,
      &quot;**&quot;,
      &quot; is&quot;,
      &quot; a&quot;,
      &quot; programming&quot;,
      &quot; concept&quot;,
      &quot; where&quot;,
      &quot; a&quot;,
      &quot; function&quot;,
      &quot; **&quot;,
      &quot;calls&quot;,
      &quot; itself&quot;,
      &quot;**&quot;,
      &quot; to&quot;,
      &quot; solve&quot;,
      &quot; a&quot;,
      &quot; smaller&quot;,
      &quot; version&quot;,
      &quot; of&quot;,
      &quot; the&quot;,
      &quot; same&quot;,
      &quot; problem&quot;,
      &quot;.\n\n&quot;,
      &quot;It&#x27;s&quot;,
      &quot; like&quot;,
      &quot; solving&quot;,
      &quot; a&quot;,
      &quot; big&quot;,
      &quot; problem&quot;,
      &quot; by&quot;,
      &quot; repeatedly&quot;,
      &quot; breaking&quot;,
      &quot; it&quot;,
      &quot; down&quot;,
      &quot; into&quot;,
      &quot; smaller&quot;,
      &quot;,&quot;,
      &quot; identical&quot;,
      &quot; problems&quot;,
      &quot; until&quot;,
      &quot; you&quot;,
      &quot; reach&quot;,
      &quot; a&quot;,
      &quot; simple&quot;,
      &quot; case&quot;,
      &quot; that&quot;,
      &quot; can&quot;,
      &quot; be&quot;,
      &quot; solved&quot;,
      &quot; directly&quot;,
      &quot;.\n\n&quot;,
      &quot;---\n\n&quot;,
      &quot;###&quot;,
      &quot; Simple&quot;,
      &quot; Example&quot;,
      &quot;:&quot;,
      &quot; Factor&quot;,
      &quot;ial&quot;,
      &quot;\n\n&quot;,
      &quot;The&quot;,
      &quot; **&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;**&quot;,
      &quot; of&quot;,
      &quot; a&quot;,
      &quot; number&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;`&quot;,
      &quot; (&quot;,
      &quot;written&quot;,
      &quot; as&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;!&quot;,
      &quot;`)&quot;,
      &quot; is&quot;,
      &quot;:\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;5&quot;,
      &quot;!&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;4&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;3&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;120&quot;,
      &quot;`\n\n&quot;,
      &quot;We&quot;,
      &quot; can&quot;,
      &quot; define&quot;,
      &quot; factorial&quot;,
      &quot; recursively&quot;,
      &quot;:\n\n&quot;,
      &quot;###&quot;,
      &quot; Recursive&quot;,
      &quot; Definition&quot;,
      &quot;:\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(n&quot;,
      &quot;)&quot;,
      &quot; =&quot;,
      &quot; n&quot;,
      &quot; \u00d7&quot;,
      &quot; factorial&quot;,
      &quot;(n&quot;,
      &quot;-&quot;,
      &quot;1&quot;,
      &quot;)`&quot;,
      &quot;   &quot;,
      &quot; \u2190&quot;,
      &quot; recursive&quot;,
      &quot; case&quot;,
      &quot;\n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;0&quot;,
      &quot;)&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;`&quot;,
      &quot;                    &quot;,
      &quot; \u2190&quot;,
      &quot; **&quot;,
      &quot;base&quot;,
      &quot; case&quot;,
      &quot;**&quot;,
      &quot; (&quot;,
      &quot;stops&quot;,
      &quot; the&quot;,
      &quot; recursion&quot;,
      &quot;)\n\n&quot;,
      &quot;---\n\n&quot;,
      &quot;###&quot;,
      &quot; Code&quot;,
      &quot; Example&quot;,
      &quot; (&quot;,
      &quot;Python&quot;,
      &quot;):\n\n&quot;,
      &quot;```&quot;,
      &quot;python&quot;,
      &quot;\n&quot;,
      &quot;def&quot;,
      &quot; factorial&quot;,
      &quot;(n&quot;,
      &quot;):\n&quot;,
      &quot;   &quot;,
      &quot; #&quot;,
      &quot; Base&quot;,
      &quot; case&quot;,
      &quot;:&quot;,
      &quot; stop&quot;,
      &quot; recursion&quot;,
      &quot;\n&quot;,
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
      &quot;\n&quot;,
      &quot;   &quot;,
      &quot; #&quot;,
      &quot; Recursive&quot;,
      &quot; case&quot;,
      &quot;:&quot;,
      &quot; call&quot;,
      &quot; itself&quot;,
      &quot; with&quot;,
      &quot; a&quot;,
      &quot; smaller&quot;,
      &quot; number&quot;,
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
      &quot;)\n\n\n&quot;,
      &quot;#&quot;,
      &quot; Test&quot;,
      &quot; it&quot;,
      &quot;\n&quot;,
      &quot;print&quot;,
      &quot;(f&quot;,
      &quot;actorial&quot;,
      &quot;(&quot;,
      &quot;5&quot;,
      &quot;))&quot;,
      &quot;  &quot;,
      &quot; #&quot;,
      &quot; Output&quot;,
      &quot;:&quot;,
      &quot; &quot;,
      &quot;120&quot;,
      &quot;\n&quot;,
      &quot;```\n\n&quot;,
      &quot;---\n\n&quot;,
      &quot;###&quot;,
      &quot; How&quot;,
      &quot; it&quot;,
      &quot; works&quot;,
      &quot; step&quot;,
      &quot; by&quot;,
      &quot; step&quot;,
      &quot;:\n\n&quot;,
      &quot;When&quot;,
      &quot; you&quot;,
      &quot; call&quot;,
      &quot; `&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;5&quot;,
      &quot;)`&quot;,
      &quot;:\n\n&quot;,
      &quot;```\n&quot;,
      &quot;factor&quot;,
      &quot;ial&quot;,
      &quot;(&quot;,
      &quot;5&quot;,
      &quot;)&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \u00d7&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;4&quot;,
      &quot;)\n&quot;,
      &quot;            &quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;4&quot;,
      &quot; \u00d7&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;))\n&quot;,
      &quot;            &quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;4&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;3&quot;,
      &quot; \u00d7&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)))\n&quot;,
      &quot;            &quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;4&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;3&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;2&quot;,
      &quot; \u00d7&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;))))\n&quot;,
      &quot;            &quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;5&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;4&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;3&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;2&quot;,
      &quot; \u00d7&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;)))&quot;,
      &quot;    &quot;,
      &quot; \u2190&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot; reached&quot;,
      &quot;\n&quot;,
      &quot;            &quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;120&quot;,
      &quot;\n&quot;,
      &quot;```\n\n&quot;,
      &quot;Each&quot;,
      &quot; recursive&quot;,
      &quot; call&quot;,
      &quot; creates&quot;,
      &quot; a&quot;,
      &quot; new&quot;,
      &quot; \&quot;&quot;,
      &quot;layer&quot;,
      &quot;\&quot;&quot;,
      &quot; until&quot;,
      &quot; it&quot;,
      &quot; hits&quot;,
      &quot; the&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot;,&quot;,
      &quot; then&quot;,
      &quot; it&quot;,
      &quot; starts&quot;,
      &quot; returning&quot;,
      &quot; values&quot;,
      &quot; back&quot;,
      &quot; up&quot;,
      &quot; the&quot;,
      &quot; chain&quot;,
      &quot;.\n\n&quot;,
      &quot;---\n\n&quot;,
      &quot;###&quot;,
      &quot; Key&quot;,
      &quot; Parts&quot;,
      &quot; of&quot;,
      &quot; Rec&quot;,
      &quot;ursion&quot;,
      &quot;:\n&quot;,
      &quot;1&quot;,
      &quot;.&quot;,
      &quot; **&quot;,
      &quot;Base&quot;,
      &quot; Case&quot;,
      &quot;**&quot;,
      &quot; \u2013&quot;,
      &quot; The&quot;,
      &quot; simplest&quot;,
      &quot; case&quot;,
      &quot; that&quot;,
      &quot; can&quot;,
      &quot; be&quot;,
      &quot; solved&quot;,
      &quot; directly&quot;,
      &quot; (&quot;,
      &quot;stops&quot;,
      &quot; infinite&quot;,
      &quot; recursion&quot;,
      &quot;).\n&quot;,
      &quot;2&quot;,
      &quot;.&quot;,
      &quot; **&quot;,
      &quot;Recursive&quot;,
      &quot; Case&quot;,
      &quot;**&quot;,
      &quot; \u2013&quot;,
      &quot; The&quot;,
      &quot; function&quot;,
      &quot; calls&quot;,
      &quot; itself&quot;,
      &quot; with&quot;,
      &quot; a&quot;,
      &quot; simpler&quot;,
      &quot;/small&quot;,
      &quot;er&quot;,
      &quot; input&quot;,
      &quot;.\n\n&quot;,
      &quot;---\n\n&quot;,
      &quot;Would&quot;,
      &quot; you&quot;,
      &quot; like&quot;,
      &quot; me&quot;,
      &quot; to&quot;,
      &quot; also&quot;,
      &quot; show&quot;,
      &quot; a&quot;,
      &quot; visual&quot;,
      &quot; example&quot;,
      &quot; using&quot;,
      &quot; a&quot;,
      &quot; stack&quot;,
      &quot; or&quot;,
      &quot; another&quot;,
      &quot; common&quot;,
      &quot; recursive&quot;,
      &quot; example&quot;,
      &quot; like&quot;,
      &quot; counting&quot;,
      &quot; down&quot;,
      &quot; or&quot;,
      &quot; summing&quot;,
      &quot; numbers&quot;,
      &quot;?&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;,
            &quot;role&quot;: &quot;assistant&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Recursion&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; programming&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; concept&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; where&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;calls&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solve&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; version&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; same&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;It&#x27;s&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; like&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solving&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; big&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; by&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; repeatedly&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; breaking&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; down&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; into&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; identical&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problems&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; until&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; you&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reach&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; simple&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; that&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; can&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; be&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solved&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; directly&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;---\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Simple&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Example&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Factor&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;The&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; number&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679681,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;written&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; as&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`)&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;120&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;We&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; can&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; define&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursively&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Recursive&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Definition&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2190&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;                    &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2190&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;stops&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;---\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Code&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Example&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Python&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;):\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;python&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;def&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;):\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679682,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Base&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stop&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; if&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ==&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; or&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ==&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; return&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Recursive&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; call&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; with&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; number&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; else&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; return&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; -&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;#&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Test&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;print&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(f&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;actorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;))&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Output&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;120&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;---\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; How&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; works&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; step&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; by&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; step&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;When&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; you&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; call&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)`&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factor&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;            &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;))\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;            &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679683,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)))\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;            &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;))))\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;            &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;5&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;4&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)))&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;    &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2190&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reached&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;            &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;120&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Each&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; call&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; creates&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; new&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \&quot;&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;layer&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\&quot;&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; until&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; hits&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; then&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; starts&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; returning&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; values&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; back&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; up&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; chain&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;---\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Key&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Parts&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Rec&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursion&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Base&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2013&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; The&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; simplest&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679684,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; that&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; can&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; be&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solved&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; directly&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;stops&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; infinite&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Recursive&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Case&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2013&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; The&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; with&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; simpler&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;/small&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;er&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; input&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;---\n\n&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Would&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; you&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; like&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; me&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; also&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; show&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; visual&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; example&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; using&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stack&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; or&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; another&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; common&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; example&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; like&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; counting&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; down&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; or&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; summing&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; numbers&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;?&quot;
          },
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {},
          &quot;finish_reason&quot;: &quot;stop&quot;,
          &quot;index&quot;: 0
        }
      ],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;
    },
    {
      &quot;choices&quot;: [],
      &quot;created&quot;: 1777679685,
      &quot;id&quot;: &quot;f987889c-ee9b-97a6-9c83-c687c444bbfb&quot;,
      &quot;model&quot;: &quot;grok-4.20-0309-non-reasoning&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;system_fingerprint&quot;: &quot;fp_bdeb03b7cd&quot;,
      &quot;usage&quot;: {
        &quot;completion_tokens&quot;: 441,
        &quot;completion_tokens_details&quot;: {
          &quot;accepted_prediction_tokens&quot;: 0,
          &quot;audio_tokens&quot;: 0,
          &quot;reasoning_tokens&quot;: 0,
          &quot;rejected_prediction_tokens&quot;: 0
        },
        &quot;cost_in_usd_ticks&quot;: 12003000,
        &quot;num_sources_used&quot;: 0,
        &quot;prompt_tokens&quot;: 132,
        &quot;prompt_tokens_details&quot;: {
          &quot;audio_tokens&quot;: 0,
          &quot;cached_tokens&quot;: 64,
          &quot;image_tokens&quot;: 0,
          &quot;text_tokens&quot;: 132
        },
        &quot;total_tokens&quot;: 573
      }
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.20-0309-non-reasoning&#x27;,
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
  &quot;model&quot;: &quot;xai/grok-4.20-0309-non-reasoning&quot;,
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

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].name</code></td><td>string</td><td></td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>messages[].name</code></td><td>string</td><td></td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>messages[].tool_calls</code></td><td>array</td><td></td></tr><tr><td><code>messages[].tool_calls[].id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function.arguments</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].name</code></td><td>string</td><td></td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_call_id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>deferred</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>frequency_penalty</code></td><td>number or null</td><td></td></tr><tr><td><code>logprobs</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>integer or null</td><td></td></tr><tr><td><code>max_tokens</code></td><td>integer or null</td><td></td></tr><tr><td><code>n</code></td><td>integer or null</td><td></td></tr><tr><td><code>parallel_tool_calls</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>presence_penalty</code></td><td>number or null</td><td></td></tr><tr><td><code>reasoning_effort</code></td><td>string or null</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.strict</code></td><td>boolean</td><td></td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.strict</code></td><td>boolean</td><td></td></tr><tr><td><code>search_parameters</code></td><td>object</td><td></td></tr><tr><td><code>search_parameters.from_date</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>search_parameters.max_search_results</code></td><td>integer or null</td><td></td></tr><tr><td><code>search_parameters.mode</code></td><td>string or null</td><td></td></tr><tr><td><code>search_parameters.return_citations</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>search_parameters.sources</code></td><td>array or null</td><td></td></tr><tr><td><code>search_parameters.to_date</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>seed</code></td><td>integer or null</td><td></td></tr><tr><td><code>stop</code></td><td>array or null</td><td></td></tr><tr><td><code>stream</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td>Required.</td></tr><tr><td><code>temperature</code></td><td>number or null</td><td></td></tr><tr><td><code>tool_choice</code></td><td>string or object</td><td></td></tr><tr><td><code>tool_choice.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tool_choice.function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tool_choice.function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools</code></td><td>array or null</td><td></td></tr><tr><td><code>top_logprobs</code></td><td>integer or null</td><td></td></tr><tr><td><code>top_p</code></td><td>number or null</td><td></td></tr><tr><td><code>user</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>web_search_options</code></td><td>object</td><td></td></tr><tr><td><code>web_search_options.search_context_size</code></td><td>['string', 'null']</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>choices[].message.reasoning_content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.refusal</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].logprobs</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].logprobs.content</code></td><td>array or null</td><td>Required.</td></tr><tr><td><code>choices[].logprobs.content</code></td><td>array or null</td><td>Required.</td></tr><tr><td><code>citations</code></td><td>array or null</td><td></td></tr><tr><td><code>output_files</code></td><td>array or null</td><td></td></tr><tr><td><code>system_fingerprint</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens_details.text_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details.audio_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details.image_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details.cached_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details</code></td><td>object</td><td></td></tr><tr><td><code>usage.completion_tokens_details.reasoning_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details.audio_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details.accepted_prediction_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details.rejected_prediction_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.cost_in_usd_ticks</code></td><td>number</td><td></td></tr><tr><td><code>usage.num_sources_used</code></td><td>number</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-4.20-0309-non-reasoning/schema-input.json)
- [Output schema](/ai/models/xai/grok-4.20-0309-non-reasoning/schema-output.json)

