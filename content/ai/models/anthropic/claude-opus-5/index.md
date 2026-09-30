<img src="/assets/upstream/images/workers-ai/anthropic.svg" alt="Anthropic logo" width="48" height="48">

<h1 id="claude-opus-5">Claude Opus 5</h1>

<p><code>anthropic/claude-opus-5</code></p>

Claude Opus 5 is Anthropic's model for complex agentic coding and enterprise work, delivering intelligence close to Claude Fable 5 at half the price. It uses adaptive thinking to calibrate reasoning per task and supports a one million token context window at standard pricing. Unlike Fable 5, Opus 5 has no data retention requirements for general access.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://www.anthropic.com/legal/commercial-terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 5, Output tokens (per 1M): 25, Cached input tokens (per 1M): 0.5, Cache creation tokens (per 1M): 6.25</td></tr>
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
    &quot;text&quot;: &quot;The laws of thermodynamics describe how energy and heat behave in physical systems. Here are the three (plus a bonus fourth that was added later but numbered \&quot;zeroth\&quot;).\n\n**First Law \u2014 Conservation of Energy**\nEnergy cannot be created or destroyed, only transferred or converted between forms. For a closed system, the change in internal energy equals the heat added minus the work done by the system:\n\n\u0394U = Q \u2212 W\n\nPractical implication: there&#x27;s no such thing as a perpetual motion machine that produces energy from nothing.\n\n**Second Law \u2014 Entropy Increases**\nThe total entropy (disorder, or more precisely the number of accessible microscopic states) of an isolated system never decreases over time. Equivalent formulations:\n\n- Heat flows spontaneously from hot to cold, never the reverse\n- No heat engine can convert heat entirely into work \u2014 some is always lost to a cold reservoir\n- Processes have a preferred direction in time\n\nThis law is why engines have efficiency limits (the Carnot limit) and why it&#x27;s often described as giving time its \&quot;arrow.\&quot;\n\n**Third Law \u2014 Absolute Zero is Unreachable**\nAs a system&#x27;s temperature approaches absolute zero (0 K, \u2212273.15 \u00b0C), its entropy approaches a constant minimum \u2014 zero for a perfect crystal. A consequence is that no finite number of steps can cool something all the way to absolute zero; you can only get asymptotically closer.\n\n**Zeroth Law \u2014 Thermal Equilibrium**\nIf system A is in thermal equilibrium with system C, and B is also in equilibrium with C, then A and B are in equilibrium with each other. This is what makes temperature a meaningful, measurable property \u2014 it&#x27;s the basis for thermometers. It was formalized after the other three, hence the odd numbering.\n\nA common informal summary: *you can&#x27;t win (1st), you can&#x27;t break even (2nd), and you can&#x27;t get out of the game (3rd).*&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_011CdMcWsWTt6YQBsVgBJKET&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;&quot;,
        &quot;signature&quot;: &quot;CAIS+wkKhwEIEBgCKkCQkqK6v16N37+5nxwsLhxrzfCzIPF8EtZFUMp15QDBKBAUGSIu2rqp+X6/Hi8Ul8I6R5cRA5sW1cubAR0uFsttMg1jbGF1ZGUtb3B1cy01OAFCCHRoaW5raW5nWiQ5ODY2MTIzNC03NmUwLTRlMGQtYTgyMS1iZThmOGMzNDc0ZDYSDBjGGGXscwelkjSVsRoM76EmL+Pl2dtvcTfkIjBy2Ayh9NZsLWod+geEtrv0CZx22kjdWmRHFED/zy3kvHn4eM1OJrP3lhPjNTckDU0qoAh+2jG1EqZNl6grp923Shc5W4S3srKv4zy7w4z6n150KajRAZSSpC/BYrGJb6lq6nVEsgjvnrOHIeF3mq1Y3/3rPJ346UB5iJRwP+rpm6lA4LkUVQZZGYeKqUhplIEMOdQdajx2iPjmTMTV0DjdiB0bHWA776a1SXuK5VjTpcnn77iwz8okVSbhqL6annDIiWET5Z9kHhjuqHhxdAXMeGkmYWbD2i0ttDdpaHgmrvW0FRYHDEDSQr/zUT6sXgke+AIG/jWwe5SmqZIIlHhOHufoW549PnXx/W6fkiiu/sNwYL85/3toWXePQkDKnD4GEFClcdCHVOEdOh45aC7XxtRwSMTBtRDz5DeAQvHwosoZoM/dJYru0s00EkG9pAq7I15ED7XTtJkUCE61wMdqifXkOSsAHbKxH6nJemHfSpS+14jaAZdWydahPq1j8wJVppQ1KC73HJZJ1wgKHT2ZCT1WlV9FuE+hmqp13NUirZRe+o7DEJiNSenND0L1GZ13FWFXiFFSXMQiAwDJTk4yWk8cLCGt45dFtAW/m8QoKKxcx+JctfpE21IMKnOG9mPJjvUdNsP3s5bk3ZkD2dcpbv4jfdJsZdz7DqNnR0tQS0TGFAc+hBuYM0ftPJlfyhKlwpi227CIVmhlxKKAUkODCMrdjevZhyJ/JZKbAJ2yzGQ2TaLxlmkbhM4XH0RBaQ+ALv5tg+oNZ0vA9OA5uKwbN9u9yKDq7hYBQeSatyPoJ+pGxEoeGeFOP4bZHvOplm/5V67E90HzDf0k/EVvjkj0P5nqVHsUb9N6IYNkMPdsNAAenNWBNk3Z8kW1xGxRw/JXZGKUr1Ql6nD5dUMw3DIDKG1c1+8QPaata4WzR/zMO8+btn3VObUDjekjC72bKMfsAjMMkX7dWYojE94Hg2rAFRQ20hmbjYDAwt8x/k8LD8bGBa/xw5WHY1Fa64r5YvJgK98sCtJbo68axk6/Tf8AgnzwVzjDugI+pQJ2oAoC22iqQQVzTwmsoLnqi9i3F/fe9wHqITf+jGytEfT0AG73R9dFD73mac0QVIbWXkm8Weld3twIvtzC3W0IPb2v1rhQkRCCJM/s6IBvRP2N0PIwCE2oexDeW+rw59vL8d/tsZ1Woogo1+76ldngoeLF4rEV4VjfP22rTN6ZLcfnerdYbF1lDXfQhTHgs+4LvMuHfYX8lMIq/wJssPyIpnXhXtmxgd9/ce2OInU3dUHXqISUHXIeiHeDxglxblzSK9B0rAzk1UaVJn4PMNGF3M1wguw6i9AAx8s+1AU5hLOinfZ166Az9HUYz/uHkQ6d0JYRx5L6xHXaWXF51ZifLRtfoeNqLdHGKxrfjSNQK8Ouuce7SzLMGi4YH5W2rED1XmpwI69xXnssHuQKHqt7ggSV5P26e5EYAQ==&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The laws of thermodynamics describe how energy and heat behave in physical systems. Here are the three (plus a bonus fourth that was added later but numbered \&quot;zeroth\&quot;).\n\n**First Law \u2014 Conservation of Energy**\nEnergy cannot be created or destroyed, only transferred or converted between forms. For a closed system, the change in internal energy equals the heat added minus the work done by the system:\n\n\u0394U = Q \u2212 W\n\nPractical implication: there&#x27;s no such thing as a perpetual motion machine that produces energy from nothing.\n\n**Second Law \u2014 Entropy Increases**\nThe total entropy (disorder, or more precisely the number of accessible microscopic states) of an isolated system never decreases over time. Equivalent formulations:\n\n- Heat flows spontaneously from hot to cold, never the reverse\n- No heat engine can convert heat entirely into work \u2014 some is always lost to a cold reservoir\n- Processes have a preferred direction in time\n\nThis law is why engines have efficiency limits (the Carnot limit) and why it&#x27;s often described as giving time its \&quot;arrow.\&quot;\n\n**Third Law \u2014 Absolute Zero is Unreachable**\nAs a system&#x27;s temperature approaches absolute zero (0 K, \u2212273.15 \u00b0C), its entropy approaches a constant minimum \u2014 zero for a perfect crystal. A consequence is that no finite number of steps can cool something all the way to absolute zero; you can only get asymptotically closer.\n\n**Zeroth Law \u2014 Thermal Equilibrium**\nIf system A is in thermal equilibrium with system C, and B is also in equilibrium with C, then A and B are in equilibrium with each other. This is what makes temperature a meaningful, measurable property \u2014 it&#x27;s the basis for thermometers. It was formalized after the other three, hence the odd numbering.\n\nA common informal summary: *you can&#x27;t win (1st), you can&#x27;t break even (2nd), and you can&#x27;t get out of the game (3rd).*&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-opus-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 20,
      &quot;output_tokens&quot;: 969,
      &quot;cache_creation_input_tokens&quot;: 0,
      &quot;cache_read_input_tokens&quot;: 0
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-opus-5&#x27;,
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
  &quot;model&quot;: &quot;anthropic/claude-opus-5&quot;,
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
    &quot;max_tokens&quot;: 2048,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;How do I read a JSON file in Python?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;system&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;# Reading JSON Files in Python\n\nPython&#x27;s built-in `json` module handles this. The key function is `json.load()`.\n\n## The basic pattern\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\nThat&#x27;s it. `json.load()` reads from a file object; the `with` statement ensures the file gets closed even if something goes wrong.\n\n## `load()` vs `loads()`\n\nThis trips people up constantly:\n\n| Function | Input | Use when |\n|---|---|---|\n| `json.load(f)` | file object | reading from a file |\n| `json.loads(s)` | string (or bytes) | you already have JSON text |\n\n```python\n# From a string\ntext = &#x27;{\&quot;name\&quot;: \&quot;Ada\&quot;, \&quot;age\&quot;: 36}&#x27;\ndata = json.loads(text)\n\n# Equivalent to the file version\nwith open(\&quot;data.json\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.loads(f.read())   # works, but load(f) is cleaner\n```\n\n## What you get back\n\nJSON types map to Python types like this:\n\n```\nobject  -&gt; dict\narray   -&gt; list\nstring  -&gt; str\nnumber  -&gt; int / float\ntrue    -&gt; True\nfalse   -&gt; False\nnull    -&gt; None\n```\n\nSo access it like any nested dict/list:\n\n```python\n# data.json: {\&quot;users\&quot;: [{\&quot;name\&quot;: \&quot;Ada\&quot;, \&quot;roles\&quot;: [\&quot;admin\&quot;]}]}\ndata[\&quot;users\&quot;][0][\&quot;name\&quot;]        # \&quot;Ada\&quot;\ndata[\&quot;users\&quot;][0][\&quot;roles\&quot;][0]    # \&quot;admin\&quot;\n```\n\nUse `.get()` for keys that might be missing:\n\n```python\nemail = data[\&quot;users\&quot;][0].get(\&quot;email\&quot;, \&quot;unknown\&quot;)\n```\n\n## Handling errors properly\n\nReal-world files are messy. Catch the two things that actually go wrong:\n\n```python\nimport json\nfrom pathlib import Path\n\ndef read_json(path):\n    try:\n        with open(path, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n            return json.load(f)\n    except FileNotFoundError:\n        print(f\&quot;No such file: {path}\&quot;)\n    except json.JSONDecodeError as e:\n        print(f\&quot;Invalid JSON in {path} at line {e.lineno}, column {e.colno}: {e.msg}\&quot;)\n    return None\n\ndata = read_json(\&quot;data.json\&quot;)\n```\n\n`JSONDecodeError` is a subclass of `ValueError`, and it carries `lineno`, `colno`, and `pos` \u2014 genuinely useful for pinpointing a bad comma.\n\n## Using `pathlib` (slightly tidier)\n\n```python\nimport json\nfrom pathlib import Path\n\ndata = json.loads(Path(\&quot;data.json\&quot;).read_text(encoding=\&quot;utf-8\&quot;))\n```\n\n## Common gotchas\n\n**Always specify `encoding=\&quot;utf-8\&quot;`.** Without it, Python uses the platform default, which on some Windows setups is cp1252 and will blow up on non-ASCII characters. JSON is UTF-8 by spec.\n\n**JSON Lines (`.jsonl`) is a different format.** One JSON object per line \u2014 `json.load()` will fail. Parse line by line:\n\n```python\nwith open(\&quot;data.jsonl\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    records = [json.loads(line) for line in f if line.strip()]\n```\n\n**Trailing commas and comments aren&#x27;t valid JSON.** `{\&quot;a\&quot;: 1,}` or `// comment` will raise `JSONDecodeError`. If you&#x27;re stuck with such files, use the `json5` or `commentjson` package.\n\n**Huge files:** `json.load()` builds the whole structure in memory. For files that don&#x27;t fit, use a streaming parser like [`ijson`](https://pypi.org/project/ijson/):\n\n```python\nimport ijson\n\nwith open(\&quot;huge.json\&quot;, \&quot;rb\&quot;) as f:\n    for record in ijson.items(f, \&quot;users.item\&quot;):\n        process(record)\n```\n\n## Writing it back out\n\nFor completeness:\n\n```python\nwith open(\&quot;out.json\&quot;, \&quot;w\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    json.dump(data, f, indent=2, ensure_ascii=False)\n```\n\n`indent=2` makes it human-readable; `ensure_ascii=False` keeps non-ASCII characters as-is instead of escaping them to `\\uXXXX`.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_011CdMcXtLbe6orhyjErTMK4&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;&quot;,
        &quot;signature&quot;: &quot;CAISlgMKhwEIEBgCKkAMw2x29hUCKlXqNB76pH+D/yqNHzKCZSWl13/1q5MvcRHqGBsMYVt5OPNJRBpoK96H4yBdLeYFynRrC3brOl8VMg1jbGF1ZGUtb3B1cy01OAFCCHRoaW5raW5nWiQ5ODY2MTIzNC03NmUwLTRlMGQtYTgyMS1iZThmOGMzNDc0ZDYSDPHl470mvTSS/VVloBoMjuO0rbloh1ffzl7/IjCQVDk88te+JO4ShyaKbxvx7tByViz6N6zO3AnWMoRShuVZmByIC9M123krmAR3d0squwH0oba6v809aPGBRis6zXZjjkxj9xUPeK9bIiAs2F4LqShktrO0enUaJGxlcocxt2tmwdkC5SF7XOy5lKpcBDf6XvOTeaV0bYyxgAQ6L2FkiOU9NtnSGiZZ0VmKz2v8RZ9nVisaD6kA15+UOqX8SO5ZYny+Ttrgue6Cx5DJ7MfBcRcE6SsSsuyLnrRFY1S7XNsCcd0lY1rv1CzkYOnItoxD6fDWab8uxQGGXWBhUnSy4XxtZ0+TR/2fRTuXGAE=&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;# Reading JSON Files in Python\n\nPython&#x27;s built-in `json` module handles this. The key function is `json.load()`.\n\n## The basic pattern\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\nThat&#x27;s it. `json.load()` reads from a file object; the `with` statement ensures the file gets closed even if something goes wrong.\n\n## `load()` vs `loads()`\n\nThis trips people up constantly:\n\n| Function | Input | Use when |\n|---|---|---|\n| `json.load(f)` | file object | reading from a file |\n| `json.loads(s)` | string (or bytes) | you already have JSON text |\n\n```python\n# From a string\ntext = &#x27;{\&quot;name\&quot;: \&quot;Ada\&quot;, \&quot;age\&quot;: 36}&#x27;\ndata = json.loads(text)\n\n# Equivalent to the file version\nwith open(\&quot;data.json\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    data = json.loads(f.read())   # works, but load(f) is cleaner\n```\n\n## What you get back\n\nJSON types map to Python types like this:\n\n```\nobject  -&gt; dict\narray   -&gt; list\nstring  -&gt; str\nnumber  -&gt; int / float\ntrue    -&gt; True\nfalse   -&gt; False\nnull    -&gt; None\n```\n\nSo access it like any nested dict/list:\n\n```python\n# data.json: {\&quot;users\&quot;: [{\&quot;name\&quot;: \&quot;Ada\&quot;, \&quot;roles\&quot;: [\&quot;admin\&quot;]}]}\ndata[\&quot;users\&quot;][0][\&quot;name\&quot;]        # \&quot;Ada\&quot;\ndata[\&quot;users\&quot;][0][\&quot;roles\&quot;][0]    # \&quot;admin\&quot;\n```\n\nUse `.get()` for keys that might be missing:\n\n```python\nemail = data[\&quot;users\&quot;][0].get(\&quot;email\&quot;, \&quot;unknown\&quot;)\n```\n\n## Handling errors properly\n\nReal-world files are messy. Catch the two things that actually go wrong:\n\n```python\nimport json\nfrom pathlib import Path\n\ndef read_json(path):\n    try:\n        with open(path, \&quot;r\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n            return json.load(f)\n    except FileNotFoundError:\n        print(f\&quot;No such file: {path}\&quot;)\n    except json.JSONDecodeError as e:\n        print(f\&quot;Invalid JSON in {path} at line {e.lineno}, column {e.colno}: {e.msg}\&quot;)\n    return None\n\ndata = read_json(\&quot;data.json\&quot;)\n```\n\n`JSONDecodeError` is a subclass of `ValueError`, and it carries `lineno`, `colno`, and `pos` \u2014 genuinely useful for pinpointing a bad comma.\n\n## Using `pathlib` (slightly tidier)\n\n```python\nimport json\nfrom pathlib import Path\n\ndata = json.loads(Path(\&quot;data.json\&quot;).read_text(encoding=\&quot;utf-8\&quot;))\n```\n\n## Common gotchas\n\n**Always specify `encoding=\&quot;utf-8\&quot;`.** Without it, Python uses the platform default, which on some Windows setups is cp1252 and will blow up on non-ASCII characters. JSON is UTF-8 by spec.\n\n**JSON Lines (`.jsonl`) is a different format.** One JSON object per line \u2014 `json.load()` will fail. Parse line by line:\n\n```python\nwith open(\&quot;data.jsonl\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    records = [json.loads(line) for line in f if line.strip()]\n```\n\n**Trailing commas and comments aren&#x27;t valid JSON.** `{\&quot;a\&quot;: 1,}` or `// comment` will raise `JSONDecodeError`. If you&#x27;re stuck with such files, use the `json5` or `commentjson` package.\n\n**Huge files:** `json.load()` builds the whole structure in memory. For files that don&#x27;t fit, use a streaming parser like [`ijson`](https://pypi.org/project/ijson/):\n\n```python\nimport ijson\n\nwith open(\&quot;huge.json\&quot;, \&quot;rb\&quot;) as f:\n    for record in ijson.items(f, \&quot;users.item\&quot;):\n        process(record)\n```\n\n## Writing it back out\n\nFor completeness:\n\n```python\nwith open(\&quot;out.json\&quot;, \&quot;w\&quot;, encoding=\&quot;utf-8\&quot;) as f:\n    json.dump(data, f, indent=2, ensure_ascii=False)\n```\n\n`indent=2` makes it human-readable; `ensure_ascii=False` keeps non-ASCII characters as-is instead of escaping them to `\\uXXXX`.&quot;
      }
    ],
    &quot;model&quot;: &quot;claude-opus-5&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 38,
      &quot;output_tokens&quot;: 1398,
      &quot;cache_creation_input_tokens&quot;: 0,
      &quot;cache_read_input_tokens&quot;: 0
    },
    &quot;stop_sequence&quot;: null,
    &quot;stop_details&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;anthropic/claude-opus-5&#x27;,
  {
    max_tokens: 2048,
    messages: [{ content: &#x27;How do I read a JSON file in Python?&#x27;, role: &#x27;user&#x27; }],
    system: &#x27;You are a helpful coding assistant specializing in Python.&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;anthropic/claude-opus-5&quot;,
  &quot;max_tokens&quot;: 2048,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;How do I read a JSON file in Python?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;system&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: user, assistant</td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>system</code></td><td>string</td><td></td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>metadata</code></td><td>object</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content</code></td><td>array</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].text</code></td><td>string</td><td></td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>stop_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td>Required.</td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/anthropic/claude-opus-5/schema-input.json)
- [Output schema](/ai/models/anthropic/claude-opus-5/schema-output.json)

