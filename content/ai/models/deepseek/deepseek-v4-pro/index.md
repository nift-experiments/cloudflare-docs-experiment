<img src="/assets/upstream/images/workers-ai/deepseek.svg" alt="Deepseek logo" width="48" height="48">

<h1 id="deepseek-v4-pro">DeepSeek V4 Pro</h1>

<p><code>deepseek/deepseek-v4-pro</code></p>

DeepSeek V4 Pro is a high-capability reasoning model from DeepSeek, served via Fireworks infrastructure for production-grade inference.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>131,072 tokens</td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 1.74, Output tokens (per 1M): 3.48, Cached input tokens (per 1M): 0.145</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic chat completion request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic chat completion request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What is the capital of France?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The capital of France is **Paris**.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-3a08845344c942108c3ab7b29112f012&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1781047641,
    &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;The capital of France is **Paris**.&quot;,
          &quot;reasoning_content&quot;: &quot;We need to answer the question: \&quot;What is the capital of France?\&quot; This is straightforward. The capital of France is Paris. I should answer concisely.&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 11,
      &quot;completion_tokens&quot;: 43,
      &quot;total_tokens&quot;: 54,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      }
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;deepseek/deepseek-v4-pro&#x27;,
  {
    messages: [{ content: &#x27;What is the capital of France?&#x27;, role: &#x27;user&#x27; }],
    model: &#x27;deepseek/deepseek-v4-pro&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What is the capital of France?&quot;,
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
    ],
    &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;,
    &quot;temperature&quot;: 0.3
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;To read a JSON file in Python, you use the built-in `json` module. The most common approach is `json.load()` which reads directly from a file object.\n\n### Basic example\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\n### Key points\n- **`json.load(file)`** \u2013 parses JSON from a file-like object.\n- **`json.loads(string)`** \u2013 parses JSON from a string (useful if you already have JSON data in memory).\n- Always open the file in read mode (`&#x27;r&#x27;`) and specify the correct encoding (usually `&#x27;utf-8&#x27;`).\n- The result is a Python dictionary (if the JSON is an object) or a list (if it\u2019s an array).\n\n### Handling errors\nWrap the loading in a `try`/`except` to catch malformed JSON or file issues:\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError as e:\n    print(f\&quot;Invalid JSON: {e}\&quot;)\n```\n\n### Reading from a string\nIf you already have a JSON string:\n```python\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n```\n\nThat\u2019s it! Let me know if you need help with writing JSON or more advanced usage.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-1aecff3044dc4e349362b9237f0e63b4&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1781047642,
    &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;To read a JSON file in Python, you use the built-in `json` module. The most common approach is `json.load()` which reads directly from a file object.\n\n### Basic example\n```python\nimport json\n\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n    data = json.load(f)\n\nprint(data)\n```\n\n### Key points\n- **`json.load(file)`** \u2013 parses JSON from a file-like object.\n- **`json.loads(string)`** \u2013 parses JSON from a string (useful if you already have JSON data in memory).\n- Always open the file in read mode (`&#x27;r&#x27;`) and specify the correct encoding (usually `&#x27;utf-8&#x27;`).\n- The result is a Python dictionary (if the JSON is an object) or a list (if it\u2019s an array).\n\n### Handling errors\nWrap the loading in a `try`/`except` to catch malformed JSON or file issues:\n```python\nimport json\n\ntry:\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\&quot;File not found.\&quot;)\nexcept json.JSONDecodeError as e:\n    print(f\&quot;Invalid JSON: {e}\&quot;)\n```\n\n### Reading from a string\nIf you already have a JSON string:\n```python\njson_string = &#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;, \&quot;age\&quot;: 30}&#x27;\ndata = json.loads(json_string)\n```\n\nThat\u2019s it! Let me know if you need help with writing JSON or more advanced usage.&quot;,
          &quot;reasoning_content&quot;: &quot;We need to provide a clear, concise answer on how to read a JSON file in Python. The user likely wants to know the standard method using the `json` module. We&#x27;ll explain opening the file, using `json.load()` for file objects, and `json.loads()` for strings. Also mention error handling, encoding, and maybe a simple example. Keep it friendly and informative.&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 24,
      &quot;completion_tokens&quot;: 413,
      &quot;total_tokens&quot;: 437,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      }
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;deepseek/deepseek-v4-pro&#x27;,
  {
    messages: [
      { content: &#x27;You are a helpful coding assistant specializing in Python.&#x27;, role: &#x27;system&#x27; },
      { content: &#x27;How do I read a JSON file in Python?&#x27;, role: &#x27;user&#x27; },
    ],
    model: &#x27;deepseek/deepseek-v4-pro&#x27;,
    temperature: 0.3,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;,
      &quot;role&quot;: &quot;system&quot;
    },
    {
      &quot;content&quot;: &quot;How do I read a JSON file in Python?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;temperature&quot;: 0.3
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
    &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;,
    &quot;stream&quot;: true
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
      &quot; smaller&quot;,
      &quot; version&quot;,
      &quot; of&quot;,
      &quot; the&quot;,
      &quot; same&quot;,
      &quot; problem&quot;,
      &quot;.&quot;,
      &quot; Each&quot;,
      &quot; recursive&quot;,
      &quot; call&quot;,
      &quot; works&quot;,
      &quot; on&quot;,
      &quot; a&quot;,
      &quot; simpler&quot;,
      &quot; input&quot;,
      &quot;,&quot;,
      &quot; and&quot;,
      &quot; there&quot;,
      &quot;\u2019&quot;,
      &quot;s&quot;,
      &quot; always&quot;,
      &quot; a&quot;,
      &quot; **&quot;,
      &quot;base&quot;,
      &quot; case&quot;,
      &quot;**&quot;,
      &quot; that&quot;,
      &quot; stops&quot;,
      &quot; the&quot;,
      &quot; recursion&quot;,
      &quot;,&quot;,
      &quot; preventing&quot;,
      &quot; an&quot;,
      &quot; infinite&quot;,
      &quot; loop&quot;,
      &quot;.\n\n&quot;,
      &quot;###&quot;,
      &quot; The&quot;,
      &quot; Two&quot;,
      &quot; Essential&quot;,
      &quot; Parts&quot;,
      &quot;\n&quot;,
      &quot;1&quot;,
      &quot;.&quot;,
      &quot; **&quot;,
      &quot;Base&quot;,
      &quot; case&quot;,
      &quot;**&quot;,
      &quot; \u2013&quot;,
      &quot; the&quot;,
      &quot; simplest&quot;,
      &quot; scenario&quot;,
      &quot; that&quot;,
      &quot; can&quot;,
      &quot; be&quot;,
      &quot; answered&quot;,
      &quot; directly&quot;,
      &quot; (&quot;,
      &quot;no&quot;,
      &quot; more&quot;,
      &quot; recursive&quot;,
      &quot; calls&quot;,
      &quot;).\n&quot;,
      &quot;2&quot;,
      &quot;.&quot;,
      &quot; **&quot;,
      &quot;Rec&quot;,
      &quot;ursive&quot;,
      &quot; case&quot;,
      &quot;**&quot;,
      &quot; \u2013&quot;,
      &quot; the&quot;,
      &quot; function&quot;,
      &quot; calls&quot;,
      &quot; itself&quot;,
      &quot; with&quot;,
      &quot; a&quot;,
      &quot; smaller&quot;,
      &quot;/s&quot;,
      &quot;impl&quot;,
      &quot;er&quot;,
      &quot; argument&quot;,
      &quot;,&quot;,
      &quot; moving&quot;,
      &quot; toward&quot;,
      &quot; the&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot;.\n\n&quot;,
      &quot;###&quot;,
      &quot; Simple&quot;,
      &quot; Example&quot;,
      &quot;:&quot;,
      &quot; Fact&quot;,
      &quot;orial&quot;,
      &quot;\n&quot;,
      &quot;The&quot;,
      &quot; factorial&quot;,
      &quot; of&quot;,
      &quot; a&quot;,
      &quot; non&quot;,
      &quot;-negative&quot;,
      &quot; integer&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;`&quot;,
      &quot; (&quot;,
      &quot;written&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;!&quot;,
      &quot;`)&quot;,
      &quot; is&quot;,
      &quot; the&quot;,
      &quot; product&quot;,
      &quot; of&quot;,
      &quot; all&quot;,
      &quot; positive&quot;,
      &quot; integers&quot;,
      &quot; up&quot;,
      &quot; to&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;`.&quot;,
      &quot;  \n&quot;,
      &quot;Definition&quot;,
      &quot;:&quot;,
      &quot;  \n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;0&quot;,
      &quot;!&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;`&quot;,
      &quot; (&quot;,
      &quot;base&quot;,
      &quot; case&quot;,
      &quot;)&quot;,
      &quot;  \n&quot;,
      &quot;-&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot;!&quot;,
      &quot; =&quot;,
      &quot; n&quot;,
      &quot; \u00d7&quot;,
      &quot; (&quot;,
      &quot;n&quot;,
      &quot;\u2212&quot;,
      &quot;1&quot;,
      &quot;)!&quot;,
      &quot;`&quot;,
      &quot; for&quot;,
      &quot; `&quot;,
      &quot;n&quot;,
      &quot; &gt;&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot;`&quot;,
      &quot; (&quot;,
      &quot;rec&quot;,
      &quot;ursive&quot;,
      &quot; case&quot;,
      &quot;)\n\n&quot;,
      &quot;####&quot;,
      &quot; Python&quot;,
      &quot; implementation&quot;,
      &quot;\n&quot;,
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
      &quot;:&quot;,
      &quot;         &quot;,
      &quot; #&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot;\n&quot;,
      &quot;       &quot;,
      &quot; return&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;\n&quot;,
      &quot;   &quot;,
      &quot; else&quot;,
      &quot;:&quot;,
      &quot;              &quot;,
      &quot; #&quot;,
      &quot; recursive&quot;,
      &quot; case&quot;,
      &quot;\n&quot;,
      &quot;       &quot;,
      &quot; return&quot;,
      &quot; n&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(n&quot;,
      &quot; -&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;)\n&quot;,
      &quot;```\n\n&quot;,
      &quot;####&quot;,
      &quot; How&quot;,
      &quot; it&quot;,
      &quot; works&quot;,
      &quot; step&quot;,
      &quot;-by&quot;,
      &quot;-step&quot;,
      &quot; for&quot;,
      &quot; `&quot;,
      &quot;fact&quot;,
      &quot;orial&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)&quot;,
      &quot;`\n&quot;,
      &quot;```\n&quot;,
      &quot;fact&quot;,
      &quot;orial&quot;,
      &quot;(&quot;,
      &quot;3&quot;,
      &quot;)\n&quot;,
      &quot; &quot;,
      &quot; \u2192&quot;,
      &quot; &quot;,
      &quot;3&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)&quot;,
      &quot;          &quot;,
      &quot; #&quot;,
      &quot; waiting&quot;,
      &quot; for&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;2&quot;,
      &quot;)\n&quot;,
      &quot;       &quot;,
      &quot; \u2192&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)&quot;,
      &quot;    &quot;,
      &quot; #&quot;,
      &quot; waiting&quot;,
      &quot; for&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;1&quot;,
      &quot;)\n&quot;,
      &quot;             &quot;,
      &quot; \u2192&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; *&quot;,
      &quot; factorial&quot;,
      &quot;(&quot;,
      &quot;0&quot;,
      &quot;)\n&quot;,
      &quot;                   &quot;,
      &quot; \u2192&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot; ==&quot;,
      &quot; &quot;,
      &quot;0&quot;,
      &quot;?&quot;,
      &quot; \u2192&quot;,
      &quot; return&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;  &quot;,
      &quot; #&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot; reached&quot;,
      &quot;\n&quot;,
      &quot;             &quot;,
      &quot; \u2192&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; *&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot;\n&quot;,
      &quot;       &quot;,
      &quot; \u2192&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot; *&quot;,
      &quot; &quot;,
      &quot;1&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot;\n&quot;,
      &quot; &quot;,
      &quot; \u2192&quot;,
      &quot; &quot;,
      &quot;3&quot;,
      &quot; *&quot;,
      &quot; &quot;,
      &quot;2&quot;,
      &quot; =&quot;,
      &quot; &quot;,
      &quot;6&quot;,
      &quot;\n&quot;,
      &quot;```\n&quot;,
      &quot;The&quot;,
      &quot; calls&quot;,
      &quot; \&quot;&quot;,
      &quot;stack&quot;,
      &quot; up&quot;,
      &quot;\&quot;&quot;,
      &quot; until&quot;,
      &quot; the&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot; is&quot;,
      &quot; hit&quot;,
      &quot;,&quot;,
      &quot; then&quot;,
      &quot; they&quot;,
      &quot; resolve&quot;,
      &quot; in&quot;,
      &quot; reverse&quot;,
      &quot; order&quot;,
      &quot;,&quot;,
      &quot; multiplying&quot;,
      &quot; as&quot;,
      &quot; they&quot;,
      &quot; go&quot;,
      &quot;.\n\n&quot;,
      &quot;###&quot;,
      &quot; Key&quot;,
      &quot; Takeaways&quot;,
      &quot;\n&quot;,
      &quot;-&quot;,
      &quot; Rec&quot;,
      &quot;ursion&quot;,
      &quot; breaks&quot;,
      &quot; a&quot;,
      &quot; problem&quot;,
      &quot; into&quot;,
      &quot; self&quot;,
      &quot;-s&quot;,
      &quot;imilar&quot;,
      &quot; sub&quot;,
      &quot;problems&quot;,
      &quot;.\n&quot;,
      &quot;-&quot;,
      &quot; Every&quot;,
      &quot; recursive&quot;,
      &quot; function&quot;,
      &quot; needs&quot;,
      &quot; a&quot;,
      &quot; stopping&quot;,
      &quot; condition&quot;,
      &quot; (&quot;,
      &quot;base&quot;,
      &quot; case&quot;,
      &quot;).\n&quot;,
      &quot;-&quot;,
      &quot; Without&quot;,
      &quot; a&quot;,
      &quot; base&quot;,
      &quot; case&quot;,
      &quot;,&quot;,
      &quot; you&quot;,
      &quot; get&quot;,
      &quot; infinite&quot;,
      &quot; recursion&quot;,
      &quot; (&quot;,
      &quot;event&quot;,
      &quot;ually&quot;,
      &quot; a&quot;,
      &quot; stack&quot;,
      &quot; overflow&quot;,
      &quot;).\n&quot;,
      &quot;-&quot;,
      &quot; It&quot;,
      &quot;\u2019&quot;,
      &quot;s&quot;,
      &quot; especially&quot;,
      &quot; natural&quot;,
      &quot; for&quot;,
      &quot; problems&quot;,
      &quot; with&quot;,
      &quot; a&quot;,
      &quot; recursive&quot;,
      &quot; structure&quot;,
      &quot; (&quot;,
      &quot;t&quot;,
      &quot;rees&quot;,
      &quot;,&quot;,
      &quot; sorting&quot;,
      &quot;,&quot;,
      &quot; divide&quot;,
      &quot;-and&quot;,
      &quot;-con&quot;,
      &quot;quer&quot;,
      &quot;,&quot;,
      &quot; etc&quot;,
      &quot;.).&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;role&quot;: &quot;assistant&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;We&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; need&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; explain&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; with&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; user&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; asked&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; \&quot;&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;Explain&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; concept&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; with&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.\&quot;&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; So&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; should&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; provide&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; clear&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; explanation&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; maybe&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; using&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; Fibonacci&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; but&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;&#x27;ll&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; define&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; as&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; calling&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; solve&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; smaller&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; instances&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; same&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; until&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; reached&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; can&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; use&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;)!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; with&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; Or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; maybe&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; count&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; tree&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; traversal&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;&#x27;ll&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; use&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; as&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; classic&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; in&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; programming&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;&#x27;ll&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; illustrate&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; with&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; pseud&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;ocode&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; or&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; Python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;&#x27;ll&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; break&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; down&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; call&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; stack&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;&#x27;ll&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; explain&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; and&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; I&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;&#x27;ll&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; show&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; step&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;-by&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;-step&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; execution&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; for&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;).&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; answer&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; should&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; be&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; instructive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; concise&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; and&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; cover&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot; concept&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;reasoning_content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Rec&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; programming&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; technique&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; where&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; solve&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; version&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; same&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Each&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; call&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; works&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; on&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; simpler&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; input&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; and&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; there&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\u2019&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;s&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; always&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; that&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stops&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; preventing&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; an&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; infinite&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; loop&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Two&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Essential&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Parts&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2013&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; simplest&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; scenario&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; that&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; can&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; be&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; answered&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; directly&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;no&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; more&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Rec&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;**&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2013&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; with&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; smaller&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;/s&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;impl&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;er&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; argument&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; moving&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; toward&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Simple&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Example&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Fact&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;orial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; non&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-negative&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; integer&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;written&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; product&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; all&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; positive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; integers&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; up&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`.&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  \n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Definition&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  \n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  \n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u00d7&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\u2212&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)!&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; for&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &gt;&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;rec&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;####&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; implementation&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;python&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;def&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;):\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; if&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ==&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;         &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; return&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; else&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;              &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; return&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; -&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;####&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; How&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; it&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; works&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; step&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-by&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-step&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; for&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; `&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;fact&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;orial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;`\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;fact&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;orial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;          &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; waiting&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; for&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;    &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; waiting&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; for&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;             &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; factorial&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;                   &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; ==&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;0&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;?&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; return&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; #&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reached&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;             &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;       &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;1&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2192&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; *&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; =&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; &quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;6&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;The&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calls&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \&quot;&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;stack&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; up&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\&quot;&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; until&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; the&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; is&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; hit&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; then&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; they&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; resolve&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; in&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; reverse&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; order&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; multiplying&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; as&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; they&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; go&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;###&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Key&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Takeaways&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Rec&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; breaks&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; into&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; self&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-s&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;imilar&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; sub&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;problems&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Every&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; function&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; needs&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stopping&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; condition&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; Without&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; base&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; you&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; get&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; infinite&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursion&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;event&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;ually&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; stack&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; overflow&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;).\n&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; It&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\u2019&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;s&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; especially&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; natural&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; for&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problems&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; with&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; structure&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; (&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;t&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;rees&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; sorting&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; divide&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-and&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;-con&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;quer&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;,&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; etc&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.).&quot;
          },
          &quot;finish_reason&quot;: null,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [
        {
          &quot;index&quot;: 0,
          &quot;delta&quot;: {},
          &quot;finish_reason&quot;: &quot;stop&quot;,
          &quot;raw_output&quot;: null
        }
      ],
      &quot;usage&quot;: null
    },
    {
      &quot;id&quot;: &quot;chatcmpl-cf0a764075534f728f55b99dacf898ba&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;created&quot;: 1781047647,
      &quot;model&quot;: &quot;accounts/fireworks/models/deepseek-v4-pro&quot;,
      &quot;choices&quot;: [],
      &quot;usage&quot;: {
        &quot;prompt_tokens&quot;: 14,
        &quot;total_tokens&quot;: 622,
        &quot;completion_tokens&quot;: 608,
        &quot;prompt_tokens_details&quot;: {
          &quot;cached_tokens&quot;: 0
        }
      }
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;deepseek/deepseek-v4-pro&#x27;,
  {
    messages: [{ content: &#x27;Explain the concept of recursion with a simple example.&#x27;, role: &#x27;user&#x27; }],
    model: &#x27;deepseek/deepseek-v4-pro&#x27;,
    stream: true,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;deepseek/deepseek-v4-pro&quot;,
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

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/deepseek/deepseek-v4-pro/schema-input.json)
- [Output schema](/ai/models/deepseek/deepseek-v4-pro/schema-output.json)

