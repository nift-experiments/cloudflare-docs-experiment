---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/alibaba/qwen3.8-max/
  description: alibaba/qwen3.8-max
  full_title: Qwen 3.8 Max · Cloudflare AI docs
  head_html: <title>Qwen 3.8 Max · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="alibaba/qwen3.8-max"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/alibaba/qwen3.8-max/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Qwen 3.8 Max · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="alibaba/qwen3.8-max"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/alibaba/qwen3.8-max/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/alibaba/qwen3.8-max/#page","headline":"Qwen 3.8 Max \u00b7 Cloudflare AI docs","description":"alibaba/qwen3.8-max","url":"https://developers.cloudflare.com/ai/models/alibaba/qwen3.8-max/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/alibaba/qwen3.8-max/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="qwen-3-8-max">Qwen 3.8 Max</h1>

<p><code>alibaba/qwen3.8-max</code></p>

Alibaba's Qwen 3.8 Max is a 2.4-trillion-parameter MoE flagship built for professional-grade coding and long-horizon autonomous work, capable of delivering complete, production-grade projects spanning 10+ days across legal, financial, design, and other specialized domains. Native visual understanding of images and extended video runs through the full plan-execute-verify cycle, served via DashScope's OpenAI-compatible endpoint.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 6, Cached input tokens (per 1M): 0.25</td></tr>
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
    &quot;text&quot;: &quot;The three main laws of thermodynamics are:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed; it can only be transferred or converted from one form to another.  \n   In equation form:  \n   \\[\n   \\Delta U = Q - W\n   \\]  \n   where \\(\\Delta U\\) is the change in internal energy, \\(Q\\) is heat added to the system, and \\(W\\) is work done by the system.\n\n2. **Second Law \u2014 Entropy Increases**  \n   In any natural process, the total entropy of an isolated system tends to increase.  \n   In simpler terms, energy naturally spreads out, and processes have a preferred direction\u2014heat flows from hot to cold, not the reverse, without external work.\n\n3. **Third Law \u2014 Absolute Zero Limit**  \n   As the temperature of a system approaches absolute zero, its entropy approaches a minimum value.  \n   It is impossible to reach absolute zero in a finite number of steps.\n\nThere is also a **Zeroth Law**, which says that if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This law establishes the concept of temperature.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;The three main laws of thermodynamics are:\n\n1. **First Law \u2014 Conservation of Energy**  \n   Energy cannot be created or destroyed; it can only be transferred or converted from one form to another.  \n   In equation form:  \n   \\[\n   \\Delta U = Q - W\n   \\]  \n   where \\(\\Delta U\\) is the change in internal energy, \\(Q\\) is heat added to the system, and \\(W\\) is work done by the system.\n\n2. **Second Law \u2014 Entropy Increases**  \n   In any natural process, the total entropy of an isolated system tends to increase.  \n   In simpler terms, energy naturally spreads out, and processes have a preferred direction\u2014heat flows from hot to cold, not the reverse, without external work.\n\n3. **Third Law \u2014 Absolute Zero Limit**  \n   As the temperature of a system approaches absolute zero, its entropy approaches a minimum value.  \n   It is impossible to reach absolute zero in a finite number of steps.\n\nThere is also a **Zeroth Law**, which says that if two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This law establishes the concept of temperature.&quot;,
          &quot;reasoning_content&quot;: &quot;We need answer user: \&quot;What are the three laws of thermodynamics?\&quot; Need likely mention there are four including zeroth? User asks three laws, likely first, second, third. Could also include zeroth? Need answer succinctly but detailed. Need final. Make sure not claim only three if common includes zeroth. Could say traditionally the \u201cthree laws\u201d are first, second, third; there&#x27;s also zeroth. Explain. Need maybe avoid too much. Final with bullet points.&quot;,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1786048647,
    &quot;id&quot;: &quot;chatcmpl-2b915318-d6f0-9bab-88a6-504a5113fbc3&quot;,
    &quot;model&quot;: &quot;qwen3.8-max&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 356,
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 99,
        &quot;text_tokens&quot;: 356
      },
      &quot;prompt_tokens&quot;: 57,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0,
        &quot;text_tokens&quot;: 57
      },
      &quot;total_tokens&quot;: 413
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3.8-max&#x27;,
  { messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/qwen3.8-max&quot;,
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
    &quot;text&quot;: &quot;Use Python\u2019s built-in `json` module:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\n`data` will usually be a Python `dict` or `list`, depending on the JSON file.\n\nIf the JSON is a string instead of a file, use:\n\n```python\nimport json\n\ndata = json.loads(&#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;}&#x27;)\n```&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;Use Python\u2019s built-in `json` module:\n\n```python\nimport json\n\nwith open(\&quot;data.json\&quot;, \&quot;r\&quot;) as file:\n    data = json.load(file)\n\nprint(data)\n```\n\n`data` will usually be a Python `dict` or `list`, depending on the JSON file.\n\nIf the JSON is a string instead of a file, use:\n\n```python\nimport json\n\ndata = json.loads(&#x27;{\&quot;name\&quot;: \&quot;Alice\&quot;}&#x27;)\n```&quot;,
          &quot;reasoning_content&quot;: &quot;We need to answer user&#x27;s simple question: \&quot;How do I read a JSON file in Python?\&quot; Need produce final. Need maybe include code using json.load, with open. Mention json.loads for string. Ensure helpful. No need overdo.&quot;,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1786048656,
    &quot;id&quot;: &quot;chatcmpl-7d75d520-ba7c-98ac-bb93-3122e0d2ef4b&quot;,
    &quot;model&quot;: &quot;qwen3.8-max&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 154,
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 49,
        &quot;text_tokens&quot;: 154
      },
      &quot;prompt_tokens&quot;: 73,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0,
        &quot;text_tokens&quot;: 73
      },
      &quot;total_tokens&quot;: 227
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3.8-max&#x27;,
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
  &quot;model&quot;: &quot;alibaba/qwen3.8-max&quot;,
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

<section class="model-example"><strong>Vision: Image Understanding</strong>
<p>Describing the contents of an image</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: [
          {
            &quot;image_url&quot;: {
              &quot;url&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg&quot;
            },
            &quot;type&quot;: &quot;image_url&quot;
          },
          {
            &quot;text&quot;: &quot;What is depicted in the image?&quot;,
            &quot;type&quot;: &quot;text&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The image shows a heartwarming beach scene at what appears to be sunset (golden hour). A young woman with long dark hair is sitting barefoot on the sand, wearing a black-and-white plaid flannel shirt and dark pants. She&#x27;s smiling as she gives a \&quot;high five\&quot; to a yellow Labrador Retriever sitting opposite her\u2014the dog has raised its paw to meet her open hand. In her other hand, she seems to be holding a small treat, suggesting a training or play moment.\n\nOther details include:\n\n- **The dog** is wearing a harness decorated with colorful paw prints, with a red leash trailing onto the sand.\n- **The setting** is a sandy beach with the ocean and a breaking wave visible in the background.\n- **The lighting** is soft and warm, with the sun creating a golden glow and slight lens flare on the right side, giving the scene a peaceful, affectionate mood.\n\nOverall, it depicts the bond between a person and her dog during a playful, tender moment by the sea.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;choices&quot;: [
      {
        &quot;finish_reason&quot;: &quot;stop&quot;,
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;content&quot;: &quot;The image shows a heartwarming beach scene at what appears to be sunset (golden hour). A young woman with long dark hair is sitting barefoot on the sand, wearing a black-and-white plaid flannel shirt and dark pants. She&#x27;s smiling as she gives a \&quot;high five\&quot; to a yellow Labrador Retriever sitting opposite her\u2014the dog has raised its paw to meet her open hand. In her other hand, she seems to be holding a small treat, suggesting a training or play moment.\n\nOther details include:\n\n- **The dog** is wearing a harness decorated with colorful paw prints, with a red leash trailing onto the sand.\n- **The setting** is a sandy beach with the ocean and a breaking wave visible in the background.\n- **The lighting** is soft and warm, with the sun creating a golden glow and slight lens flare on the right side, giving the scene a peaceful, affectionate mood.\n\nOverall, it depicts the bond between a person and her dog during a playful, tender moment by the sea.&quot;,
          &quot;reasoning_content&quot;: &quot;The user is asking me to describe what&#x27;s shown in the image. Let me look at the image carefully.\n\nThe image shows a beach scene, and from the quality of the light it seems to be sunset or sunrise (golden hour). A young woman with long black hair is sitting on the sand, wearing a checkered (plaid) shirt and dark-colored pants/jeans, barefoot. She&#x27;s smiling and appears to be doing a \&quot;high five\&quot; or \&quot;shake hands\&quot; with a dog\u2014looks like a yellow/golden Labrador Retriever. The dog is sitting on the sand, lifting its front paw and placing it on the woman&#x27;s hand. The dog is wearing a harness with a colorful pattern (looks like a paw print pattern), and a red leash is attached, dangling onto the sand.\n\nIn the background, you can see the sea with waves breaking, and the sky is bright and hazy, with warm sunlight streaming in from the right side of the image, creating a lens flare effect.\n\nThe scene depicts the bond between the woman and the dog, probably a training moment (the dog is doing a \&quot;high five\&quot; trick), and the woman might be holding a treat in her other hand.\n\nI should describe this clearly and concisely. Let me make it a friendly, descriptive response. No special instructions, just answer the question. Let me describe the main elements:\n\n- A woman sitting on a sandy beach\n- A Labrador Retriever dog\n- The two are doing a high five / shaking hands\n- Sunset/golden hour light\n- Ocean waves in the background\n- The dog is wearing a harness with a leash\n- The woman is smiling, wearing a plaid shirt, barefoot\n- She might be holding a treat\n\nFormat: A short descriptive paragraph is appropriate. No tools needed. It should be concise but complete. A medium-length paragraph should be fine. Let me try writing it.&quot;,
          &quot;role&quot;: &quot;assistant&quot;
        }
      }
    ],
    &quot;created&quot;: 1786048660,
    &quot;id&quot;: &quot;chatcmpl-8a8cec83-a8e2-9d27-9f9b-102906147b5c&quot;,
    &quot;model&quot;: &quot;qwen3.8-max&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;usage&quot;: {
      &quot;completion_tokens&quot;: 618,
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 400,
        &quot;text_tokens&quot;: 218
      },
      &quot;prompt_tokens&quot;: 2520,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0,
        &quot;image_tokens&quot;: 2503,
        &quot;text_tokens&quot;: 17
      },
      &quot;total_tokens&quot;: 3138
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3.8-max&#x27;,
  {
    messages: [
      {
        content: [
          {
            image_url: {
              url: &#x27;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg&#x27;,
            },
            type: &#x27;image_url&#x27;,
          },
          { text: &#x27;What is depicted in the image?&#x27;, type: &#x27;text&#x27; },
        ],
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
  &quot;model&quot;: &quot;alibaba/qwen3.8-max&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: [
        {
          &quot;image_url&quot;: {
            &quot;url&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg&quot;
          },
          &quot;type&quot;: &quot;image_url&quot;
        },
        {
          &quot;text&quot;: &quot;What is depicted in the image?&quot;,
          &quot;type&quot;: &quot;text&quot;
        }
      ],
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
      &quot;Recursion is a&quot;,
      &quot; way of solving a&quot;,
      &quot; problem where&quot;,
      &quot; a function calls itself&quot;,
      &quot; to solve smaller versions&quot;,
      &quot; of the same&quot;,
      &quot; problem.\n\nA&quot;,
      &quot; recursive function usually has&quot;,
      &quot; two&quot;,
      &quot; parts:\n\n1&quot;,
      &quot;.&quot;,
      &quot; **Base case**&quot;,
      &quot; \u2014 when to stop&quot;,
      &quot;  \n&quot;,
      &quot;2. **Recursive&quot;,
      &quot; case** \u2014 calling&quot;,
      &quot; itself with a smaller&quot;,
      &quot; input\n\nExample:&quot;,
      &quot; calculating `3!&quot;,
      &quot;` factorial&quot;,
      &quot;.\n\n```python&quot;,
      &quot;\ndef factorial(n&quot;,
      &quot;):\n    if&quot;,
      &quot; n == 1&quot;,
      &quot;:          # base&quot;,
      &quot; case\n&quot;,
      &quot;        return 1&quot;,
      &quot;\n    else:&quot;,
      &quot;\n        return n&quot;,
      &quot; * factorial(n -&quot;,
      &quot; 1) &quot;,
      &quot; # recursive case\n&quot;,
      &quot;```\n\nCalling:&quot;,
      &quot;\n\n```python\n&quot;,
      &quot;print(factorial(&quot;,
      &quot;3))\n```&quot;,
      &quot;\n\nThis works like&quot;,
      &quot;:\n\n```python&quot;,
      &quot;\nfactorial(&quot;,
      &quot;3) = &quot;,
      &quot;3 * factorial&quot;,
      &quot;(2)\n&quot;,
      &quot;factorial(2&quot;,
      &quot;) = 2&quot;,
      &quot; * factorial(1&quot;,
      &quot;)\nfactorial&quot;,
      &quot;(1) =&quot;,
      &quot; 1\n```&quot;,
      &quot;\n\nSo:\n\n&quot;,
      &quot;```python\n&quot;,
      &quot;3 * 2&quot;,
      &quot; * 1 =&quot;,
      &quot; 6\n```&quot;,
      &quot;\n\nRecursion is&quot;,
      &quot; useful when&quot;,
      &quot; a problem can be&quot;,
      &quot; broken into smaller repeated&quot;,
      &quot; subproblems.&quot;
    ]
  },
  &quot;raw_response&quot;: [
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null,
      &quot;choices&quot;: [
        {
          &quot;logprobs&quot;: null,
          &quot;index&quot;: 0,
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;role&quot;: &quot;assistant&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;finish_reason&quot;: null
        }
      ]
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot;We&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; need to answer&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; user:&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; \&quot;Explain the&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; concept of recursion with&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; a simple example.\&quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; Simple. Done.&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; Need final answer&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot;. Could include definition&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot;, base case,&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; recursive case, example&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; factorial&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; or countdown, maybe&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; Python. Keep&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot; clear.&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;Recursion is a&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; way of solving a&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem where&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a function calls itself&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; to solve smaller versions&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; of the same&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; problem.\n\nA&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; recursive function usually has&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; two&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; parts:\n\n1&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; **Base case**&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; \u2014 when to stop&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;  \n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;2. **Recursive&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case** \u2014 calling&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; itself with a smaller&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; input\n\nExample:&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; calculating `3!&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;` factorial&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;.\n\n```python&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\ndef factorial(n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;):\n    if&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; n == 1&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:          # base&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; case\n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;        return 1&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n    else:&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n        return n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; * factorial(n -&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 1) &quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; # recursive case\n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```\n\nCalling:&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\n```python\n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;print(factorial(&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3))\n```&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\nThis works like&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;:\n\n```python&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\nfactorial(&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3) = &quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3 * factorial&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(2)\n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;factorial(2&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;) = 2&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; * factorial(1&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;)\nfactorial&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;(1) =&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 1\n```&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\nSo:\n\n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;```python\n&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;3 * 2&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; * 1 =&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; 6\n```&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;\n\nRecursion is&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; useful when&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; a problem can be&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; broken into smaller repeated&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot; subproblems.&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: null,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;choices&quot;: [
        {
          &quot;delta&quot;: {
            &quot;content&quot;: &quot;&quot;,
            &quot;reasoning_content&quot;: &quot;&quot;
          },
          &quot;index&quot;: 0,
          &quot;finish_reason&quot;: &quot;stop&quot;,
          &quot;logprobs&quot;: null
        }
      ],
      &quot;created&quot;: 1786048673,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: null
    },
    {
      &quot;choices&quot;: [],
      &quot;created&quot;: 1786048673,
      &quot;id&quot;: &quot;chatcmpl-93de192c-09a4-9b99-8c9a-55f6302cc5c5&quot;,
      &quot;model&quot;: &quot;qwen3.8-max&quot;,
      &quot;object&quot;: &quot;chat.completion.chunk&quot;,
      &quot;usage&quot;: {
        &quot;completion_tokens&quot;: 263,
        &quot;completion_tokens_details&quot;: {
          &quot;reasoning_tokens&quot;: 47,
          &quot;text_tokens&quot;: 263
        },
        &quot;prompt_tokens&quot;: 59,
        &quot;prompt_tokens_details&quot;: {
          &quot;cached_tokens&quot;: 0,
          &quot;text_tokens&quot;: 59
        },
        &quot;total_tokens&quot;: 322
      }
    }
  ]
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/qwen3.8-max&#x27;,
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
  &quot;model&quot;: &quot;alibaba/qwen3.8-max&quot;,
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

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/qwen3.8-max/schema-input.json)
- [Output schema](/ai/models/alibaba/qwen3.8-max/schema-output.json)

