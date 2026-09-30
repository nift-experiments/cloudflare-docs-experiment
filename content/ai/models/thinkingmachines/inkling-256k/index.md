<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Thinkingmachines logo" width="48" height="48">

<h1 id="inkling-256k">Inkling 256K</h1>

<p><code>thinkingmachines/inkling-256k</code></p>

The 256K-context variant of Inkling, Thinking Machines' open-weights hybrid reasoning MoE model. Same hybrid reasoning, tool-use, and streaming support as the base model, with an extended context window for longer conversations and documents. Currently intended for low-traffic testing and internal use rather than high-throughput production deployments.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>262,144 tokens</td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 3.74, Output tokens (per 1M): 9.36, Cached input tokens (per 1M): 0.748, Cache creation tokens (per 1M): 3.74</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic message request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic message request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 512,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;The capital of France is&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The capital of France is **Paris**.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_f3f0874570144f29add4272d4f07491d&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;The user is asking \&quot;The capital of France is\&quot;. This is a straightforward factual question. The capital of France is Paris. I should provide the answer clearly and concisely.&quot;,
        &quot;signature&quot;: &quot;&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The capital of France is **Paris**.&quot;
      }
    ],
    &quot;model&quot;: &quot;thinkingmachines/Inkling:peft:262144&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 0,
      &quot;output_tokens&quot;: 52,
      &quot;cache_creation_input_tokens&quot;: 19,
      &quot;cache_read_input_tokens&quot;: 0
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;thinkingmachines/inkling-256k&#x27;,
  { max_tokens: 512, messages: [{ content: &#x27;The capital of France is&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;thinkingmachines/inkling-256k&quot;,
  &quot;max_tokens&quot;: 512,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;The capital of France is&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Tool Use</strong>
<p>Tool use round-trip: the model requests a tool call, then answers using the tool_result supplied in a follow-up user message</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 1024,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What&#x27;s the weather in Paris?&quot;,
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;id&quot;: &quot;toolu_01A1x1x1x1x1x1x1x1x1x1x1&quot;,
            &quot;input&quot;: {
              &quot;city&quot;: &quot;Paris&quot;
            },
            &quot;name&quot;: &quot;get_weather&quot;,
            &quot;type&quot;: &quot;tool_use&quot;
          }
        ],
        &quot;role&quot;: &quot;assistant&quot;
      },
      {
        &quot;content&quot;: [
          {
            &quot;content&quot;: &quot;Sunny, 22\u00b0C&quot;,
            &quot;tool_use_id&quot;: &quot;toolu_01A1x1x1x1x1x1x1x1x1x1x1&quot;,
            &quot;type&quot;: &quot;tool_result&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;tools&quot;: [
      {
        &quot;description&quot;: &quot;Get the current weather for a city.&quot;,
        &quot;input_schema&quot;: {
          &quot;properties&quot;: {
            &quot;city&quot;: {
              &quot;type&quot;: &quot;string&quot;
            }
          },
          &quot;required&quot;: [
            &quot;city&quot;
          ],
          &quot;type&quot;: &quot;object&quot;
        },
        &quot;name&quot;: &quot;get_weather&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The weather in Paris is sunny with a temperature of 22\u00b0C.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_5711f240c8da46eeb462f8900281d087&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;The user asked for the weather in Paris. The function returned \&quot;Sunny, 22\u00b0C\&quot;. I should provide a clear, concise answer.&quot;,
        &quot;signature&quot;: &quot;&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The weather in Paris is sunny with a temperature of 22\u00b0C.&quot;
      }
    ],
    &quot;model&quot;: &quot;thinkingmachines/Inkling:peft:262144&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 0,
      &quot;output_tokens&quot;: 49,
      &quot;cache_creation_input_tokens&quot;: 95,
      &quot;cache_read_input_tokens&quot;: 0
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;thinkingmachines/inkling-256k&#x27;,
  {
    max_tokens: 1024,
    messages: [
      { content: &quot;What&#x27;s the weather in Paris?&quot;, role: &#x27;user&#x27; },
      {
        content: [
          {
            id: &#x27;toolu_01A1x1x1x1x1x1x1x1x1x1x1&#x27;,
            input: { city: &#x27;Paris&#x27; },
            name: &#x27;get_weather&#x27;,
            type: &#x27;tool_use&#x27;,
          },
        ],
        role: &#x27;assistant&#x27;,
      },
      {
        content: [
          {
            content: &#x27;Sunny, 22°C&#x27;,
            tool_use_id: &#x27;toolu_01A1x1x1x1x1x1x1x1x1x1x1&#x27;,
            type: &#x27;tool_result&#x27;,
          },
        ],
        role: &#x27;user&#x27;,
      },
    ],
    tools: [
      {
        description: &#x27;Get the current weather for a city.&#x27;,
        input_schema: {
          properties: { city: { type: &#x27;string&#x27; } },
          required: [&#x27;city&#x27;],
          type: &#x27;object&#x27;,
        },
        name: &#x27;get_weather&#x27;,
      },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;thinkingmachines/inkling-256k&quot;,
  &quot;max_tokens&quot;: 1024,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What&#x27;\&#x27;&#x27;s the weather in Paris?&quot;,
      &quot;role&quot;: &quot;user&quot;
    },
    {
      &quot;content&quot;: [
        {
          &quot;id&quot;: &quot;toolu_01A1x1x1x1x1x1x1x1x1x1x1&quot;,
          &quot;input&quot;: {
            &quot;city&quot;: &quot;Paris&quot;
          },
          &quot;name&quot;: &quot;get_weather&quot;,
          &quot;type&quot;: &quot;tool_use&quot;
        }
      ],
      &quot;role&quot;: &quot;assistant&quot;
    },
    {
      &quot;content&quot;: [
        {
          &quot;content&quot;: &quot;Sunny, 22°C&quot;,
          &quot;tool_use_id&quot;: &quot;toolu_01A1x1x1x1x1x1x1x1x1x1x1&quot;,
          &quot;type&quot;: &quot;tool_result&quot;
        }
      ],
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;tools&quot;: [
    {
      &quot;description&quot;: &quot;Get the current weather for a city.&quot;,
      &quot;input_schema&quot;: {
        &quot;properties&quot;: {
          &quot;city&quot;: {
            &quot;type&quot;: &quot;string&quot;
          }
        },
        &quot;required&quot;: [
          &quot;city&quot;
        ],
        &quot;type&quot;: &quot;object&quot;
      },
      &quot;name&quot;: &quot;get_weather&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: user, assistant</td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>system</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>top_k</code></td><td>number</td><td></td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>metadata</code></td><td>object</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content</code></td><td>array</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].text</code></td><td>string</td><td></td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>stop_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td>Required.</td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.cache_creation_input_tokens</code></td><td>number</td><td></td></tr><tr><td><code>usage.cache_read_input_tokens</code></td><td>number</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/thinkingmachines/inkling-256k/schema-input.json)
- [Output schema](/ai/models/thinkingmachines/inkling-256k/schema-output.json)

