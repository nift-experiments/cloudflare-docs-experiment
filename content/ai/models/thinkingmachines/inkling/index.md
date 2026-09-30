---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/thinkingmachines/inkling/
  description: thinkingmachines/inkling
  full_title: Inkling · Cloudflare AI docs
  head_html: <title>Inkling · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="thinkingmachines/inkling"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/thinkingmachines/inkling/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Inkling · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="thinkingmachines/inkling"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/thinkingmachines/inkling/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/thinkingmachines/inkling/#page","headline":"Inkling \u00b7 Cloudflare AI docs","description":"thinkingmachines/inkling","url":"https://developers.cloudflare.com/ai/models/thinkingmachines/inkling/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/thinkingmachines/inkling/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Thinkingmachines logo" width="48" height="48">

<h1 id="inkling">Inkling</h1>

<p><code>thinkingmachines/inkling</code></p>

Inkling is Thinking Machines' open-weights hybrid reasoning model, built on a mixture-of-experts architecture. It reasons by default, exposing its chain-of-thought as leading thinking content blocks, with reasoning effort tunable via a Tinker-specific output_config.effort parameter. Available through Tinker's beta Anthropic Messages-compatible endpoint alongside tool use, streaming, and multi-turn conversations. Currently intended for low-traffic testing and internal use rather than high-throughput production deployments; prompt caching, citations, and audio input are not supported through this endpoint.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>64,000 tokens</td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 1.87, Output tokens (per 1M): 4.68, Cached input tokens (per 1M): 0.374, Cache creation tokens (per 1M): 1.87</td></tr>
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
    &quot;text&quot;: &quot;Paris.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_922ec1780752447c802ec60be3dabfd6&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;The user is asking a simple factual question: \&quot;The capital of France is\&quot;. The answer is Paris. I should provide the answer clearly and concisely.&quot;,
        &quot;signature&quot;: &quot;&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Paris.&quot;
      }
    ],
    &quot;model&quot;: &quot;thinkingmachines/Inkling&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 0,
      &quot;output_tokens&quot;: 41,
      &quot;cache_creation_input_tokens&quot;: 19,
      &quot;cache_read_input_tokens&quot;: 0
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;thinkingmachines/inkling&#x27;,
  { max_tokens: 512, messages: [{ content: &#x27;The capital of France is&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;thinkingmachines/inkling&quot;,
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
    &quot;text&quot;: &quot;The weather in Paris is sunny with a temperature of 22\u00b0C. Enjoy the nice weather!&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_ddfc346862fc4a3f8afc1f8f53e1d932&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;The user asked for the weather in Paris and the function returned \&quot;Sunny, 22\u00b0C\&quot;. I should provide a clear, friendly answer with this information.&quot;,
        &quot;signature&quot;: &quot;&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The weather in Paris is sunny with a temperature of 22\u00b0C. Enjoy the nice weather!&quot;
      }
    ],
    &quot;model&quot;: &quot;thinkingmachines/Inkling&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 0,
      &quot;output_tokens&quot;: 57,
      &quot;cache_creation_input_tokens&quot;: 95,
      &quot;cache_read_input_tokens&quot;: 0
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;thinkingmachines/inkling&#x27;,
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
  &quot;model&quot;: &quot;thinkingmachines/inkling&quot;,
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

<section class="model-example"><strong>Extended Thinking Effort</strong>
<p>Controlling reasoning effort via Tinker's output_config.effort extension. The model's chain-of-thought is returned as a leading thinking content block before the answer.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;max_tokens&quot;: 1024,
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What is 17 * 23?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;output_config&quot;: {
      &quot;effort&quot;: &quot;high&quot;
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;17 \u00d7 23 = **391**\n\n(Breakdown: 17 \u00d7 20 = 340, plus 17 \u00d7 3 = 51; 340 + 51 = 391)&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;msg_a7e845f498bd44e9b1d63dca8b104a2e&quot;,
    &quot;type&quot;: &quot;message&quot;,
    &quot;role&quot;: &quot;assistant&quot;,
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;thinking&quot;,
        &quot;thinking&quot;: &quot;The user is asking for the product of 17 and 23. Let me calculate that.\n\n17 * 23 = ?\n\nI can compute this as:\n17 * 20 = 340\n17 * 3 = 51\n340 + 51 = 391\n\nAlternatively:\n17 * 23 = 17 * (25 - 2) = 425 - 34 = 391\nOr (20 - 3) * 23 = 460 - 69 = 391\n\nSo the answer is 391.&quot;,
        &quot;signature&quot;: &quot;&quot;
      },
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;17 \u00d7 23 = **391**\n\n(Breakdown: 17 \u00d7 20 = 340, plus 17 \u00d7 3 = 51; 340 + 51 = 391)&quot;
      }
    ],
    &quot;model&quot;: &quot;thinkingmachines/Inkling&quot;,
    &quot;stop_reason&quot;: &quot;end_turn&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 0,
      &quot;output_tokens&quot;: 155,
      &quot;cache_creation_input_tokens&quot;: 22,
      &quot;cache_read_input_tokens&quot;: 0
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;thinkingmachines/inkling&#x27;,
  {
    max_tokens: 1024,
    messages: [{ content: &#x27;What is 17 * 23?&#x27;, role: &#x27;user&#x27; }],
    output_config: { effort: &#x27;high&#x27; },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/messages \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;thinkingmachines/inkling&quot;,
  &quot;max_tokens&quot;: 1024,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What is 17 * 23?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;output_config&quot;: {
    &quot;effort&quot;: &quot;high&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: user, assistant</td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>system</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>top_k</code></td><td>number</td><td></td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>metadata</code></td><td>object</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content</code></td><td>array</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].text</code></td><td>string</td><td></td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>stop_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td>Required.</td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.cache_creation_input_tokens</code></td><td>number</td><td></td></tr><tr><td><code>usage.cache_read_input_tokens</code></td><td>number</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/thinkingmachines/inkling/schema-input.json)
- [Output schema](/ai/models/thinkingmachines/inkling/schema-output.json)

