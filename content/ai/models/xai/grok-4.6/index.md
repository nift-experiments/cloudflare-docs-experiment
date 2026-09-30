---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/xai/grok-4.6/
  description: xai/grok-4.6
  full_title: Grok 4.6 · Cloudflare AI docs
  head_html: <title>Grok 4.6 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="xai/grok-4.6"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/xai/grok-4.6/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Grok 4.6 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="xai/grok-4.6"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/xai/grok-4.6/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/xai/grok-4.6/#page","headline":"Grok 4.6 \u00b7 Cloudflare AI docs","description":"xai/grok-4.6","url":"https://developers.cloudflare.com/ai/models/xai/grok-4.6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/xai/grok-4.6/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/xai.svg" alt="Xai logo" width="48" height="48">

<h1 id="grok-4-6">Grok 4.6</h1>

<p><code>xai/grok-4.6</code></p>

xAI's Grok 4.6, a flagship reasoning model for coding, agentic tasks, and visual work. Accepts text and image inputs, and supports function calling and structured outputs.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>500,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://x.ai/legal/terms-of-service-enterprise">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input &lt;200k (per 1M): 2, Cached input &lt;200k (per 1M): 0.5, Output &lt;200k (per 1M): 6, Input &gt;=200k (per 1M): 4, Cached input &gt;=200k (per 1M): 1, Output &gt;=200k (per 1M): 12</td></tr>
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
    &quot;text&quot;: &quot;**First law (conservation of energy):** The internal energy of an isolated system is constant; energy can change form (e.g., heat \\(\\leftrightarrow\\) work) but is neither created nor destroyed. In equation form, \\(\\Delta U = Q - W\\) (sign conventions vary).\n\n**Second law (entropy/directionality):** The entropy of an isolated system never decreases; spontaneous processes increase total entropy. Equivalently, heat cannot spontaneously flow from a colder body to a hotter one, and no cyclic process can convert heat entirely into work with 100% efficiency (Kelvin\u2013Planck and Clausius statements).\n\n**Third law (unattainability of absolute zero):** As temperature approaches 0 K, the entropy of a perfect crystal approaches a minimum (conventionally taken as zero). Absolute zero is therefore unattainable in a finite number of steps.\n\n(The zeroth law, which underpins the definition of temperature via thermal equilibrium, is sometimes listed separately and was formalized later.)\n\nThese statements have multiple equivalent formulations; the versions above are the most common in introductory physics/chemistry.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;46e7d84b-3292-9934-9830-10a2926ac872&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1786550938,
    &quot;model&quot;: &quot;grok-4.6&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;**First law (conservation of energy):** The internal energy of an isolated system is constant; energy can change form (e.g., heat \\(\\leftrightarrow\\) work) but is neither created nor destroyed. In equation form, \\(\\Delta U = Q - W\\) (sign conventions vary).\n\n**Second law (entropy/directionality):** The entropy of an isolated system never decreases; spontaneous processes increase total entropy. Equivalently, heat cannot spontaneously flow from a colder body to a hotter one, and no cyclic process can convert heat entirely into work with 100% efficiency (Kelvin\u2013Planck and Clausius statements).\n\n**Third law (unattainability of absolute zero):** As temperature approaches 0 K, the entropy of a perfect crystal approaches a minimum (conventionally taken as zero). Absolute zero is therefore unattainable in a finite number of steps.\n\n(The zeroth law, which underpins the definition of temperature via thermal equilibrium, is sometimes listed separately and was formalized later.)\n\nThese statements have multiple equivalent formulations; the versions above are the most common in introductory physics/chemistry.&quot;,
          &quot;reasoning_content&quot;: &quot;The question is: \&quot;What are the three laws of thermodynamics?\&quot;\nThe three laws of thermodynamics are:\n\n1. **First Law**: Energy is conserved. It cannot be created or destroyed, only converted between forms. The change in internal energy of a system equals the heat added to it minus the work done by it: \u0394U = Q - W.\n\n2.&quot;,
          &quot;refusal&quot;: null
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 214,
      &quot;completion_tokens&quot;: 220,
      &quot;total_tokens&quot;: 870,
      &quot;prompt_tokens_details&quot;: {
        &quot;text_tokens&quot;: 214,
        &quot;audio_tokens&quot;: 0,
        &quot;image_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 128
      },
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 436,
        &quot;audio_tokens&quot;: 0,
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;num_sources_used&quot;: 0,
      &quot;cost_in_usd_ticks&quot;: 41720000
    },
    &quot;system_fingerprint&quot;: &quot;fp_a7b4933f4a93564d&quot;,
    &quot;service_tier&quot;: &quot;default&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.6&#x27;,
  { messages: [{ content: &#x27;What are the three laws of thermodynamics?&#x27;, role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.6&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What are the three laws of thermodynamics?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Image Understanding</strong>
<p>Analyze an image supplied alongside a text prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: [
          {
            &quot;image_url&quot;: {
              &quot;url&quot;: &quot;https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png&quot;
            },
            &quot;type&quot;: &quot;image_url&quot;
          },
          {
            &quot;text&quot;: &quot;Describe the person in this image and their surroundings in one sentence.&quot;,
            &quot;type&quot;: &quot;text&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;A smiling young woman with dark hair in a navy knit sweater holds a fuzzy microphone while seated in a cozy room with a white fireplace mantel, framed photo collage, and warm lighting.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;5f620cf3-cd07-9a84-99d8-00f6f8712f95&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1786550950,
    &quot;model&quot;: &quot;grok-4.6&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;A smiling young woman with dark hair in a navy knit sweater holds a fuzzy microphone while seated in a cozy room with a white fireplace mantel, framed photo collage, and warm lighting.&quot;,
          &quot;reasoning_content&quot;: &quot;The task is: \&quot;Describe the person in this image and their surroundings in one sentence.\&quot;\n&quot;,
          &quot;refusal&quot;: null
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 2628,
      &quot;completion_tokens&quot;: 36,
      &quot;total_tokens&quot;: 2925,
      &quot;prompt_tokens_details&quot;: {
        &quot;text_tokens&quot;: 221,
        &quot;audio_tokens&quot;: 0,
        &quot;image_tokens&quot;: 2407,
        &quot;cached_tokens&quot;: 128
      },
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 261,
        &quot;audio_tokens&quot;: 0,
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;num_sources_used&quot;: 0,
      &quot;cost_in_usd_ticks&quot;: 68460000
    },
    &quot;system_fingerprint&quot;: &quot;fp_a7b4933f4a93564d&quot;,
    &quot;service_tier&quot;: &quot;default&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.6&#x27;,
  {
    messages: [
      {
        content: [
          {
            image_url: { url: &#x27;https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png&#x27; },
            type: &#x27;image_url&#x27;,
          },
          {
            text: &#x27;Describe the person in this image and their surroundings in one sentence.&#x27;,
            type: &#x27;text&#x27;,
          },
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
  &quot;model&quot;: &quot;xai/grok-4.6&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: [
        {
          &quot;image_url&quot;: {
            &quot;url&quot;: &quot;https://v3.fal.media/files/koala/NLVPfOI4XL1cWT2PmmqT3_Hope.png&quot;
          },
          &quot;type&quot;: &quot;image_url&quot;
        },
        {
          &quot;text&quot;: &quot;Describe the person in this image and their surroundings in one sentence.&quot;,
          &quot;type&quot;: &quot;text&quot;
        }
      ],
      &quot;role&quot;: &quot;user&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Function Calling</strong>
<p>Force the model to return a typed function call</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What is the current temperature in San Francisco?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;tool_choice&quot;: &quot;required&quot;,
    &quot;tools&quot;: [
      {
        &quot;function&quot;: {
          &quot;description&quot;: &quot;Get the current temperature for a city&quot;,
          &quot;name&quot;: &quot;get_temperature&quot;,
          &quot;parameters&quot;: {
            &quot;additionalProperties&quot;: false,
            &quot;properties&quot;: {
              &quot;city&quot;: {
                &quot;type&quot;: &quot;string&quot;
              },
              &quot;unit&quot;: {
                &quot;enum&quot;: [
                  &quot;celsius&quot;,
                  &quot;fahrenheit&quot;
                ],
                &quot;type&quot;: &quot;string&quot;
              }
            },
            &quot;required&quot;: [
              &quot;city&quot;,
              &quot;unit&quot;
            ],
            &quot;type&quot;: &quot;object&quot;
          },
          &quot;strict&quot;: true
        },
        &quot;type&quot;: &quot;function&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;tool_calls&quot;: [
      {
        &quot;id&quot;: &quot;call-67aeb658-cc74-4375-b860-f18970d8187a-0&quot;,
        &quot;function&quot;: {
          &quot;name&quot;: &quot;get_temperature&quot;,
          &quot;arguments&quot;: &quot;{\&quot;city\&quot;:\&quot;San Francisco\&quot;,\&quot;unit\&quot;:\&quot;fahrenheit\&quot;}&quot;
        },
        &quot;type&quot;: &quot;function&quot;
      }
    ]
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;d1c2cf6d-a4c2-9b8b-a6e3-ff60e4dd12b8&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1786550955,
    &quot;model&quot;: &quot;grok-4.6&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;&quot;,
          &quot;reasoning_content&quot;: &quot;The user is asking for the current temperature in San Francisco. I have a tool called \&quot;get_temperature\&quot; that can get the current temperature for a city. It requires \&quot;city\&quot; and \&quot;unit\&quot;.\n&quot;,
          &quot;tool_calls&quot;: [
            {
              &quot;id&quot;: &quot;call-67aeb658-cc74-4375-b860-f18970d8187a-0&quot;,
              &quot;function&quot;: {
                &quot;name&quot;: &quot;get_temperature&quot;,
                &quot;arguments&quot;: &quot;{\&quot;city\&quot;:\&quot;San Francisco\&quot;,\&quot;unit\&quot;:\&quot;fahrenheit\&quot;}&quot;
              },
              &quot;type&quot;: &quot;function&quot;
            }
          ],
          &quot;refusal&quot;: null
        },
        &quot;finish_reason&quot;: &quot;tool_calls&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 333,
      &quot;completion_tokens&quot;: 20,
      &quot;total_tokens&quot;: 654,
      &quot;prompt_tokens_details&quot;: {
        &quot;text_tokens&quot;: 333,
        &quot;audio_tokens&quot;: 0,
        &quot;image_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 128
      },
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 301,
        &quot;audio_tokens&quot;: 0,
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;num_sources_used&quot;: 0,
      &quot;cost_in_usd_ticks&quot;: 24000000
    },
    &quot;system_fingerprint&quot;: &quot;fp_a7b4933f4a93564d&quot;,
    &quot;service_tier&quot;: &quot;default&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.6&#x27;,
  {
    messages: [{ content: &#x27;What is the current temperature in San Francisco?&#x27;, role: &#x27;user&#x27; }],
    tool_choice: &#x27;required&#x27;,
    tools: [
      {
        function: {
          description: &#x27;Get the current temperature for a city&#x27;,
          name: &#x27;get_temperature&#x27;,
          parameters: {
            additionalProperties: false,
            properties: {
              city: { type: &#x27;string&#x27; },
              unit: { enum: [&#x27;celsius&#x27;, &#x27;fahrenheit&#x27;], type: &#x27;string&#x27; },
            },
            required: [&#x27;city&#x27;, &#x27;unit&#x27;],
            type: &#x27;object&#x27;,
          },
          strict: true,
        },
        type: &#x27;function&#x27;,
      },
    ],
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.6&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What is the current temperature in San Francisco?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;tool_choice&quot;: &quot;required&quot;,
  &quot;tools&quot;: [
    {
      &quot;function&quot;: {
        &quot;description&quot;: &quot;Get the current temperature for a city&quot;,
        &quot;name&quot;: &quot;get_temperature&quot;,
        &quot;parameters&quot;: {
          &quot;additionalProperties&quot;: false,
          &quot;properties&quot;: {
            &quot;city&quot;: {
              &quot;type&quot;: &quot;string&quot;
            },
            &quot;unit&quot;: {
              &quot;enum&quot;: [
                &quot;celsius&quot;,
                &quot;fahrenheit&quot;
              ],
              &quot;type&quot;: &quot;string&quot;
            }
          },
          &quot;required&quot;: [
            &quot;city&quot;,
            &quot;unit&quot;
          ],
          &quot;type&quot;: &quot;object&quot;
        },
        &quot;strict&quot;: true
      },
      &quot;type&quot;: &quot;function&quot;
    }
  ]
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Structured Output</strong>
<p>Constrain the response to a JSON schema</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Classify the sentiment of: The launch was smooth and customers loved it.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;response_format&quot;: {
      &quot;json_schema&quot;: {
        &quot;name&quot;: &quot;sentiment_result&quot;,
        &quot;schema&quot;: {
          &quot;additionalProperties&quot;: false,
          &quot;properties&quot;: {
            &quot;confidence&quot;: {
              &quot;maximum&quot;: 1,
              &quot;minimum&quot;: 0,
              &quot;type&quot;: &quot;number&quot;
            },
            &quot;sentiment&quot;: {
              &quot;enum&quot;: [
                &quot;positive&quot;,
                &quot;neutral&quot;,
                &quot;negative&quot;
              ],
              &quot;type&quot;: &quot;string&quot;
            }
          },
          &quot;required&quot;: [
            &quot;sentiment&quot;,
            &quot;confidence&quot;
          ],
          &quot;type&quot;: &quot;object&quot;
        },
        &quot;strict&quot;: true
      },
      &quot;type&quot;: &quot;json_schema&quot;
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;{\&quot;confidence\&quot;:0.95,\&quot;sentiment\&quot;:\&quot;positive\&quot;}&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;e89a3a47-b193-9785-9c35-f4dd3c098107&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1786550957,
    &quot;model&quot;: &quot;grok-4.6&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;{\&quot;confidence\&quot;:0.95,\&quot;sentiment\&quot;:\&quot;positive\&quot;}&quot;,
          &quot;reasoning_content&quot;: &quot;The task is to classify the sentiment of: \&quot;The launch was smooth and customers loved it.\&quot;\n&quot;,
          &quot;refusal&quot;: null
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 300,
      &quot;completion_tokens&quot;: 12,
      &quot;total_tokens&quot;: 607,
      &quot;prompt_tokens_details&quot;: {
        &quot;text_tokens&quot;: 300,
        &quot;audio_tokens&quot;: 0,
        &quot;image_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 128
      },
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 295,
        &quot;audio_tokens&quot;: 0,
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      },
      &quot;num_sources_used&quot;: 0,
      &quot;cost_in_usd_ticks&quot;: 22500000
    },
    &quot;system_fingerprint&quot;: &quot;fp_a7b4933f4a93564d&quot;,
    &quot;service_tier&quot;: &quot;default&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;xai/grok-4.6&#x27;,
  {
    messages: [
      {
        content: &#x27;Classify the sentiment of: The launch was smooth and customers loved it.&#x27;,
        role: &#x27;user&#x27;,
      },
    ],
    response_format: {
      json_schema: {
        name: &#x27;sentiment_result&#x27;,
        schema: {
          additionalProperties: false,
          properties: {
            confidence: { maximum: 1, minimum: 0, type: &#x27;number&#x27; },
            sentiment: { enum: [&#x27;positive&#x27;, &#x27;neutral&#x27;, &#x27;negative&#x27;], type: &#x27;string&#x27; },
          },
          required: [&#x27;sentiment&#x27;, &#x27;confidence&#x27;],
          type: &#x27;object&#x27;,
        },
        strict: true,
      },
      type: &#x27;json_schema&#x27;,
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;xai/grok-4.6&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Classify the sentiment of: The launch was smooth and customers loved it.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;response_format&quot;: {
    &quot;json_schema&quot;: {
      &quot;name&quot;: &quot;sentiment_result&quot;,
      &quot;schema&quot;: {
        &quot;additionalProperties&quot;: false,
        &quot;properties&quot;: {
          &quot;confidence&quot;: {
            &quot;maximum&quot;: 1,
            &quot;minimum&quot;: 0,
            &quot;type&quot;: &quot;number&quot;
          },
          &quot;sentiment&quot;: {
            &quot;enum&quot;: [
              &quot;positive&quot;,
              &quot;neutral&quot;,
              &quot;negative&quot;
            ],
            &quot;type&quot;: &quot;string&quot;
          }
        },
        &quot;required&quot;: [
          &quot;sentiment&quot;,
          &quot;confidence&quot;
        ],
        &quot;type&quot;: &quot;object&quot;
      },
      &quot;strict&quot;: true
    },
    &quot;type&quot;: &quot;json_schema&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].name</code></td><td>string</td><td></td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>messages[].name</code></td><td>string</td><td></td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>messages[].tool_calls</code></td><td>array</td><td></td></tr><tr><td><code>messages[].tool_calls[].id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_calls[].function.arguments</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].name</code></td><td>string</td><td></td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].content</code></td><td>string</td><td>Required.</td></tr><tr><td><code>messages[].tool_call_id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>max_completion_tokens</code></td><td>integer or null</td><td></td></tr><tr><td><code>max_tokens</code></td><td>integer or null</td><td></td></tr><tr><td><code>n</code></td><td>integer or null</td><td></td></tr><tr><td><code>parallel_tool_calls</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>prompt_cache_key</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>reasoning_effort</code></td><td>string or null</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.strict</code></td><td>boolean</td><td></td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.schema</code></td><td>object</td><td>Required.</td></tr><tr><td><code>response_format.json_schema.strict</code></td><td>boolean</td><td></td></tr><tr><td><code>search_parameters</code></td><td>object</td><td></td></tr><tr><td><code>search_parameters.from_date</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>search_parameters.max_search_results</code></td><td>integer or null</td><td></td></tr><tr><td><code>search_parameters.mode</code></td><td>string or null</td><td></td></tr><tr><td><code>search_parameters.return_citations</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>search_parameters.sources</code></td><td>array or null</td><td></td></tr><tr><td><code>search_parameters.to_date</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>seed</code></td><td>integer or null</td><td></td></tr><tr><td><code>service_tier</code></td><td>string</td><td>Values: default, priority</td></tr><tr><td><code>stream</code></td><td>['boolean', 'null']</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td>Required.</td></tr><tr><td><code>temperature</code></td><td>number or null</td><td></td></tr><tr><td><code>tool_choice</code></td><td>string or object</td><td></td></tr><tr><td><code>tool_choice.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tool_choice.function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tool_choice.function</code></td><td>object</td><td>Required.</td></tr><tr><td><code>tool_choice.function.name</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools</code></td><td>array or null</td><td></td></tr><tr><td><code>top_p</code></td><td>number or null</td><td></td></tr><tr><td><code>user</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>web_search_options</code></td><td>object</td><td></td></tr><tr><td><code>web_search_options.filters</code></td><td>object</td><td></td></tr><tr><td><code>web_search_options.search_context_size</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>web_search_options.user_location</code></td><td>object</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>choices[].message.reasoning_content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.refusal</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].logprobs</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].logprobs.content</code></td><td>array or null</td><td>Required.</td></tr><tr><td><code>choices[].logprobs.content</code></td><td>array or null</td><td>Required.</td></tr><tr><td><code>citations</code></td><td>array or null</td><td></td></tr><tr><td><code>output_files</code></td><td>array or null</td><td></td></tr><tr><td><code>service_tier</code></td><td>string</td><td>Required. Values: default, priority</td></tr><tr><td><code>system_fingerprint</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens_details.text_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details.audio_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details.image_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.prompt_tokens_details.cached_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details</code></td><td>object</td><td></td></tr><tr><td><code>usage.completion_tokens_details.reasoning_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details.audio_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details.accepted_prediction_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens_details.rejected_prediction_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.cost_in_usd_ticks</code></td><td>number</td><td></td></tr><tr><td><code>usage.num_sources_used</code></td><td>number</td><td></td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/xai/grok-4.6/schema-input.json)
- [Output schema](/ai/models/xai/grok-4.6/schema-output.json)

