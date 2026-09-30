---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/google/gemini-3.5-flash-lite/
  description: google/gemini-3.5-flash-lite
  full_title: Gemini 3.5 Flash-Lite · Cloudflare AI docs
  head_html: <title>Gemini 3.5 Flash-Lite · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="google/gemini-3.5-flash-lite"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/google/gemini-3.5-flash-lite/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Gemini 3.5 Flash-Lite · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="google/gemini-3.5-flash-lite"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/google/gemini-3.5-flash-lite/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/google/gemini-3.5-flash-lite/#page","headline":"Gemini 3.5 Flash-Lite \u00b7 Cloudflare AI docs","description":"google/gemini-3.5-flash-lite","url":"https://developers.cloudflare.com/ai/models/google/gemini-3.5-flash-lite/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/google/gemini-3.5-flash-lite/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-3-5-flash-lite">Gemini 3.5 Flash-Lite</h1>

<p><code>google/gemini-3.5-flash-lite</code></p>

Gemini 3.5 Flash-Lite is a low-latency, cost-effective multimodal model optimized for high-throughput, low-cost execution for subagent tasks and document parsing.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,048,576 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.3, Output tokens (per 1M): 2.5, Cached input tokens (per 1M): 0.03, Cache creation tokens (per 1M): 0.03</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic generateContent request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic generateContent request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental physical principles that describe how energy behaves in the universe\u2014specifically regarding heat, work, entropy, and the limits of energy transfer. \n\nHere is a summary of the three laws, along with a \&quot;zeroth law\&quot; that was established later but is equally fundamental.\n\n---\n\n### The Zeroth Law of Thermodynamics\n*(Establishes temperature as a measurable property and defines thermal equilibrium.)*\n* **The Law:** If two systems are each in thermal equilibrium with a third system, they are also in thermal equilibrium with each other.\n* **Plain English:** If System A is the same temperature as System C, and System B is also the same temperature as System C, then System A and System B are the same temperature. \n* **Why it matters:** This law forms the scientific basis for thermometers.\n\n---\n\n### The First Law of Thermodynamics\n*(The Law of Conservation of Energy)*\n* **The Law:** Energy cannot be created or destroyed in an isolated system; it can only be changed from one form to another.\n* **Plain English:** You can\u2019t get something for nothing. The total amount of energy in the universe remains constant. If a system gains energy, it must come from somewhere else; if it loses energy, it must go somewhere else.\n* **Example:** When you drive a car, chemical energy stored in the gasoline is converted into thermal energy (heat) and kinetic energy (motion). No energy is lost, just transformed.\n\n---\n\n### The Second Law of Thermodynamics\n*(The Law of Entropy)*\n* **The Law:** The total entropy (disorder or randomness) of an isolated system always increases over time. Heat naturally flows from a hotter object to a cooler object, never the reverse spontaneously.\n* **Plain English:** Things naturally fall apart, cool down, or become disorganized unless you put work into maintaining them. You cannot convert heat energy into work with 100% efficiency; some energy is always \&quot;lost\&quot; as unusable waste heat.\n* **Example:** A cup of hot coffee left on a table will eventually cool down to room temperature. The reverse\u2014a room-temperature cup of coffee spontaneously absorbing heat from the room to become boiling hot\u2014never happens naturally. \n* **Why it matters:** This law explains why perpetual motion machines are impossible and gives our universe a \&quot;direction of time\&quot; (often called the \&quot;arrow of time\&quot;).\n\n---\n\n### The Third Law of Thermodynamics\n*(The Behavior at Absolute Zero)*\n* **The Law:** As the temperature of a system approaches absolute zero ($0\\text{ Kelvin}$ or $-273.15^\\circ\\text{C}$), the entropy of a pure, perfect crystalline substance approaches a minimum value (typically zero).\n* **Plain English:** You cannot reach absolute zero. As atoms get colder and colder, they slow down and lose thermal motion, but you can never completely stop molecular motion entirely.\n* **Why it matters:** It sets a fundamental lower limit on temperature and helps scientists calculate the absolute entropy of substances.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The three laws of thermodynamics are fundamental physical principles that describe how energy behaves in the universe\u2014specifically regarding heat, work, entropy, and the limits of energy transfer. \n\nHere is a summary of the three laws, along with a \&quot;zeroth law\&quot; that was established later but is equally fundamental.\n\n---\n\n### The Zeroth Law of Thermodynamics\n*(Establishes temperature as a measurable property and defines thermal equilibrium.)*\n* **The Law:** If two systems are each in thermal equilibrium with a third system, they are also in thermal equilibrium with each other.\n* **Plain English:** If System A is the same temperature as System C, and System B is also the same temperature as System C, then System A and System B are the same temperature. \n* **Why it matters:** This law forms the scientific basis for thermometers.\n\n---\n\n### The First Law of Thermodynamics\n*(The Law of Conservation of Energy)*\n* **The Law:** Energy cannot be created or destroyed in an isolated system; it can only be changed from one form to another.\n* **Plain English:** You can\u2019t get something for nothing. The total amount of energy in the universe remains constant. If a system gains energy, it must come from somewhere else; if it loses energy, it must go somewhere else.\n* **Example:** When you drive a car, chemical energy stored in the gasoline is converted into thermal energy (heat) and kinetic energy (motion). No energy is lost, just transformed.\n\n---\n\n### The Second Law of Thermodynamics\n*(The Law of Entropy)*\n* **The Law:** The total entropy (disorder or randomness) of an isolated system always increases over time. Heat naturally flows from a hotter object to a cooler object, never the reverse spontaneously.\n* **Plain English:** Things naturally fall apart, cool down, or become disorganized unless you put work into maintaining them. You cannot convert heat energy into work with 100% efficiency; some energy is always \&quot;lost\&quot; as unusable waste heat.\n* **Example:** A cup of hot coffee left on a table will eventually cool down to room temperature. The reverse\u2014a room-temperature cup of coffee spontaneously absorbing heat from the room to become boiling hot\u2014never happens naturally. \n* **Why it matters:** This law explains why perpetual motion machines are impossible and gives our universe a \&quot;direction of time\&quot; (often called the \&quot;arrow of time\&quot;).\n\n---\n\n### The Third Law of Thermodynamics\n*(The Behavior at Absolute Zero)*\n* **The Law:** As the temperature of a system approaches absolute zero ($0\\text{ Kelvin}$ or $-273.15^\\circ\\text{C}$), the entropy of a pure, perfect crystalline substance approaches a minimum value (typically zero).\n* **Plain English:** You cannot reach absolute zero. As atoms get colder and colder, they slow down and lose thermal motion, but you can never completely stop molecular motion entirely.\n* **Why it matters:** It sets a fundamental lower limit on temperature and helps scientists calculate the absolute entropy of substances.&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1/ol32QPrMVbKQjdSf9juhARUkac2Z+KPcq5oo84TKrgbEj7WuE+4yuNhidBd0=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 8,
      &quot;candidatesTokenCount&quot;: 634,
      &quot;totalTokenCount&quot;: 642,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 8
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 634
        }
      ]
    },
    &quot;modelVersion&quot;: &quot;gemini-3.5-flash-lite&quot;,
    &quot;createTime&quot;: &quot;2026-07-21T16:21:55.338444Z&quot;,
    &quot;responseId&quot;: &quot;o5xfaozUFK2o8sYPiYHy-Ag&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.5-flash-lite&#x27;,
  { contents: [{ parts: [{ text: &#x27;What are the three laws of thermodynamics?&#x27; }], role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.5-flash-lite&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Data Extraction</strong>
<p>Structured data extraction from unstructured text, a common subagent task</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Extract the name, email, and phone number from this text as JSON: &#x27;Hi, I&#x27;m Jordan Blake, reach me at jordan.blake@example.com or 555-2938.&#x27;&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are a data extraction assistant. Respond with only valid JSON, no extra commentary.&quot;
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;{\n  \&quot;name\&quot;: \&quot;Jordan Blake\&quot;,\n  \&quot;email\&quot;: \&quot;jordan.blake@example.com\&quot;,\n  \&quot;phone\&quot;: \&quot;555-2938\&quot;\n}&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;{\n  \&quot;name\&quot;: \&quot;Jordan Blake\&quot;,\n  \&quot;email\&quot;: \&quot;jordan.blake@example.com\&quot;,\n  \&quot;phone\&quot;: \&quot;555-2938\&quot;\n}&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1+AejOv/9okEuBeoArPDSAKd5ZcT4tlNk6itaskjb7ezx7K9fEu5NLFUx4iUig=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 63,
      &quot;candidatesTokenCount&quot;: 43,
      &quot;totalTokenCount&quot;: 106,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 63
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 43
        }
      ]
    },
    &quot;modelVersion&quot;: &quot;gemini-3.5-flash-lite&quot;,
    &quot;createTime&quot;: &quot;2026-07-21T16:21:57.867550Z&quot;,
    &quot;responseId&quot;: &quot;pZxfat75NIvG8sYP3dfakAo&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.5-flash-lite&#x27;,
  {
    contents: [
      {
        parts: [
          {
            text: &quot;Extract the name, email, and phone number from this text as JSON: &#x27;Hi, I&#x27;m Jordan Blake, reach me at jordan.blake@example.com or 555-2938.&#x27;&quot;,
          },
        ],
        role: &#x27;user&#x27;,
      },
    ],
    generationConfig: { temperature: 0 },
    systemInstruction: {
      parts: [
        {
          text: &#x27;You are a data extraction assistant. Respond with only valid JSON, no extra commentary.&#x27;,
        },
      ],
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.5-flash-lite&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Extract the name, email, and phone number from this text as JSON: &#x27;\&#x27;&#x27;Hi, I&#x27;\&#x27;&#x27;m Jordan Blake, reach me at jordan.blake@example.com or 555-2938.&#x27;\&#x27;&#x27;&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are a data extraction assistant. Respond with only valid JSON, no extra commentary.&quot;
        }
      ]
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a short conversation with low-latency, high-throughput responses</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Summarize this in one sentence: The meeting covered Q3 budget overruns, a proposed hiring freeze, and a plan to renegotiate vendor contracts.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;The meeting addressed Q3 budget overruns by proposing a hiring freeze and vendor contract renegotiations.&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Now make it even shorter, under 10 words.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 512
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Addressing Q3 budget overruns, hiring freezes, and vendor contracts.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;content&quot;: {
          &quot;role&quot;: &quot;model&quot;,
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Addressing Q3 budget overruns, hiring freezes, and vendor contracts.&quot;,
              &quot;thoughtSignature&quot;: &quot;AY89a1/dUv1ajorDdpZkOzaeL0fb5CjoZL4SoKtpQeX8AK5jF5vNa/v4F6r7OqdabWs=&quot;
            }
          ]
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;usageMetadata&quot;: {
      &quot;promptTokenCount&quot;: 61,
      &quot;candidatesTokenCount&quot;: 14,
      &quot;totalTokenCount&quot;: 75,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 61
        }
      ],
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 14
        }
      ]
    },
    &quot;modelVersion&quot;: &quot;gemini-3.5-flash-lite&quot;,
    &quot;createTime&quot;: &quot;2026-07-21T16:21:58.695703Z&quot;,
    &quot;responseId&quot;: &quot;ppxfape7KqSn8sYPpMq_gQ8&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-3.5-flash-lite&#x27;,
  {
    contents: [
      {
        parts: [
          {
            text: &#x27;Summarize this in one sentence: The meeting covered Q3 budget overruns, a proposed hiring freeze, and a plan to renegotiate vendor contracts.&#x27;,
          },
        ],
        role: &#x27;user&#x27;,
      },
      {
        parts: [
          {
            text: &#x27;The meeting addressed Q3 budget overruns by proposing a hiring freeze and vendor contract renegotiations.&#x27;,
          },
        ],
        role: &#x27;model&#x27;,
      },
      { parts: [{ text: &#x27;Now make it even shorter, under 10 words.&#x27; }], role: &#x27;user&#x27; },
    ],
    generationConfig: { maxOutputTokens: 512 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-3.5-flash-lite&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Summarize this in one sentence: The meeting covered Q3 budget overruns, a proposed hiring freeze, and a plan to renegotiate vendor contracts.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;The meeting addressed Q3 budget overruns by proposing a hiring freeze and vendor contract renegotiations.&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Now make it even shorter, under 10 words.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 512
    }
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>contents</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].role</code></td><td>string</td><td>Values: user, model</td></tr><tr><td><code>contents[].parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>systemInstruction</code></td><td>object</td><td></td></tr><tr><td><code>systemInstruction.parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>systemInstruction.parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>generationConfig</code></td><td>object</td><td></td></tr><tr><td><code>generationConfig.temperature</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topP</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topK</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.maxOutputTokens</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.candidateCount</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.stopSequences</code></td><td>array</td><td></td></tr><tr><td><code>generationConfig.responseMimeType</code></td><td>string</td><td></td></tr><tr><td><code>safetySettings</code></td><td>array</td><td></td></tr><tr><td><code>safetySettings[].category</code></td><td>string</td><td>Required.</td></tr><tr><td><code>safetySettings[].threshold</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>toolConfig</code></td><td>object</td><td></td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>candidates</code></td><td>array</td><td></td></tr><tr><td><code>usageMetadata</code></td><td>object</td><td></td></tr><tr><td><code>usageMetadata.promptTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.candidatesTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.totalTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>modelVersion</code></td><td>string</td><td></td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/gemini-3.5-flash-lite/schema-input.json)
- [Output schema](/ai/models/google/gemini-3.5-flash-lite/schema-output.json)

