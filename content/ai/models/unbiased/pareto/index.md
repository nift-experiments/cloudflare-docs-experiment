---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/unbiased/pareto/
  description: unbiased/pareto
  full_title: Pareto · Cloudflare AI docs
  head_html: <title>Pareto · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="unbiased/pareto"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/unbiased/pareto/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Pareto · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="unbiased/pareto"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/unbiased/pareto/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/unbiased/pareto/#page","headline":"Pareto \u00b7 Cloudflare AI docs","description":"unbiased/pareto","url":"https://developers.cloudflare.com/ai/models/unbiased/pareto/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/unbiased/pareto/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Unbiased logo" width="48" height="48">

<h1 id="pareto">Pareto</h1>

<p><code>unbiased/pareto</code></p>

Pareto is Unbiased's blended AI model. It engages multiple language models in parallel for each request, synthesizes one answer, and supports text and vision inputs through a single API response.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Terms</th><td><a href="https://unbiased.ai/terms/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2.5, Output tokens (per 1M): 7.5, Cached input tokens (per 1M): 0.25</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Ask Pareto for a concise answer.

<section class="model-example"><strong>Simple Question</strong>
<p>Ask Pareto for a concise answer.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;What is the capital of France? Answer in one word.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;max_tokens&quot;: 16
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Paris&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-mu5ww8tss0mj6ofw&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;model&quot;: &quot;union-alpha&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;Paris&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 11,
      &quot;completion_tokens&quot;: 5,
      &quot;total_tokens&quot;: 16,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;cost&quot;: 4.5e-05
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;unbiased/pareto&#x27;,
  {
    messages: [{ content: &#x27;What is the capital of France? Answer in one word.&#x27;, role: &#x27;user&#x27; }],
    max_tokens: 16,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;unbiased/pareto&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;What is the capital of France? Answer in one word.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;max_tokens&quot;: 16
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>System Guidance</strong>
<p>Set a helpful system role before asking a question.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;You explain technical topics in plain language.&quot;,
        &quot;role&quot;: &quot;system&quot;
      },
      {
        &quot;content&quot;: &quot;What is an API? Explain it in two sentences.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;max_tokens&quot;: 64
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;An API (Application Programming Interface) is a set of rules that lets one software program request information or actions from another. For example, a weather app uses an API to get forecasts from a weather service.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-mu5wwcpm6hxi7lsb&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;model&quot;: &quot;union-alpha&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;An API (Application Programming Interface) is a set of rules that lets one software program request information or actions from another. For example, a weather app uses an API to get forecasts from a weather service.&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 19,
      &quot;completion_tokens&quot;: 45,
      &quot;total_tokens&quot;: 64,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;cost&quot;: 0.000305
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;unbiased/pareto&#x27;,
  {
    messages: [
      { content: &#x27;You explain technical topics in plain language.&#x27;, role: &#x27;system&#x27; },
      { content: &#x27;What is an API? Explain it in two sentences.&#x27;, role: &#x27;user&#x27; },
    ],
    max_tokens: 64,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;unbiased/pareto&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;You explain technical topics in plain language.&quot;,
      &quot;role&quot;: &quot;system&quot;
    },
    {
      &quot;content&quot;: &quot;What is an API? Explain it in two sentences.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;max_tokens&quot;: 64
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Coding Example</strong>
<p>Ask for a short coding example.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Write a JavaScript function that reverses a string. Include one example call.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;max_tokens&quot;: 128
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;```javascript\nfunction reverseString(str) {\n  return Array.from(str).reverse().join(\&quot;\&quot;);\n}\n\nconsole.log(reverseString(\&quot;Hello\&quot;)); // \&quot;olleH\&quot;\n```&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-mu5wwj1mqcjfe7xb&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;model&quot;: &quot;union-alpha&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;```javascript\nfunction reverseString(str) {\n  return Array.from(str).reverse().join(\&quot;\&quot;);\n}\n\nconsole.log(reverseString(\&quot;Hello\&quot;)); // \&quot;olleH\&quot;\n```&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 14,
      &quot;completion_tokens&quot;: 37,
      &quot;total_tokens&quot;: 51,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;cost&quot;: 0.00024875
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;unbiased/pareto&#x27;,
  {
    messages: [
      {
        content: &#x27;Write a JavaScript function that reverses a string. Include one example call.&#x27;,
        role: &#x27;user&#x27;,
      },
    ],
    max_tokens: 128,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;unbiased/pareto&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Write a JavaScript function that reverses a string. Include one example call.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;max_tokens&quot;: 128
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Follow-up Conversation</strong>
<p>Continue a short conversation with prior assistant context.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;I am planning a weekend trip to a coastal city.&quot;,
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;content&quot;: &quot;Consider walkable neighborhoods, local food, and a nearby beach.&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      },
      {
        &quot;content&quot;: &quot;What should I prioritize when choosing where to stay?&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;max_tokens&quot;: 96
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;For a weekend trip, **prioritize location over extra amenities**\u2014less time in transit means more time enjoying the city.\n\n- **Close to your main plans:** Stay near the beach for a beach-focused trip, or near restaurants and sights if you\u2019re more interested in exploring.\n- **Easy transportation:** Check airport or station connections, public transit, and parking costs if you\u2019re driving.\n- **Comfort and quiet:** Recent reviews can reveal street noise, cleanliness issues&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-mu5wwqlruoazrxij&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;model&quot;: &quot;union-alpha&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;For a weekend trip, **prioritize location over extra amenities**\u2014less time in transit means more time enjoying the city.\n\n- **Close to your main plans:** Stay near the beach for a beach-focused trip, or near restaurants and sights if you\u2019re more interested in exploring.\n- **Easy transportation:** Check airport or station connections, public transit, and parking costs if you\u2019re driving.\n- **Comfort and quiet:** Recent reviews can reveal street noise, cleanliness issues&quot;
        },
        &quot;finish_reason&quot;: &quot;length&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 43,
      &quot;completion_tokens&quot;: 96,
      &quot;total_tokens&quot;: 139,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;cost&quot;: 0.00065375
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;unbiased/pareto&#x27;,
  {
    messages: [
      { content: &#x27;I am planning a weekend trip to a coastal city.&#x27;, role: &#x27;user&#x27; },
      {
        content: &#x27;Consider walkable neighborhoods, local food, and a nearby beach.&#x27;,
        role: &#x27;assistant&#x27;,
      },
      { content: &#x27;What should I prioritize when choosing where to stay?&#x27;, role: &#x27;user&#x27; },
    ],
    max_tokens: 96,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;unbiased/pareto&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;I am planning a weekend trip to a coastal city.&quot;,
      &quot;role&quot;: &quot;user&quot;
    },
    {
      &quot;content&quot;: &quot;Consider walkable neighborhoods, local food, and a nearby beach.&quot;,
      &quot;role&quot;: &quot;assistant&quot;
    },
    {
      &quot;content&quot;: &quot;What should I prioritize when choosing where to stay?&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;max_tokens&quot;: 96
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Creative Writing</strong>
<p>Generate a compact piece of creative writing.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;content&quot;: &quot;Write a four-line poem about finding light after a difficult day.&quot;,
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;max_tokens&quot;: 96
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The day lay heavy, stitched with shades of gray,\nUntil one star shone through the frayed dusk\u2019s seam.\nI set my burdens down beside the way,\nAnd let its little light rekindle dream.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-mu5wx6hq2jpgslxe&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;model&quot;: &quot;union-alpha&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;The day lay heavy, stitched with shades of gray,\nUntil one star shone through the frayed dusk\u2019s seam.\nI set my burdens down beside the way,\nAnd let its little light rekindle dream.&quot;
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 12,
      &quot;completion_tokens&quot;: 46,
      &quot;total_tokens&quot;: 58,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0
      },
      &quot;cost&quot;: 0.0003025
    },
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;unbiased/pareto&#x27;,
  {
    messages: [
      { content: &#x27;Write a four-line poem about finding light after a difficult day.&#x27;, role: &#x27;user&#x27; },
    ],
    max_tokens: 96,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;unbiased/pareto&quot;,
  &quot;messages&quot;: [
    {
      &quot;content&quot;: &quot;Write a four-line poem about finding light after a difficult day.&quot;,
      &quot;role&quot;: &quot;user&quot;
    }
  ],
  &quot;max_tokens&quot;: 96
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td></td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/unbiased/pareto/schema-input.json)
- [Output schema](/ai/models/unbiased/pareto/schema-output.json)

