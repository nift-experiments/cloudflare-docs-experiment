---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/
  description: openai/gpt-6-astra
  full_title: GPT-6 Astra · Cloudflare AI docs
  head_html: <title>GPT-6 Astra · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="openai/gpt-6-astra"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="GPT-6 Astra · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="openai/gpt-6-astra"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/#page","headline":"GPT-6 Astra \u00b7 Cloudflare AI docs","description":"openai/gpt-6-astra","url":"https://developers.cloudflare.com/ai/models/openai/gpt-6-astra/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/openai/gpt-6-astra/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-6-astra">GPT-6 Astra</h1>

<p><code>openai/gpt-6-astra</code></p>

GPT-6 Astra is OpenAI's most capable model, built for complex reasoning, coding, computer use, research, and document creation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,050,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Long-context threshold (input tokens): 272000, Short-context input (per 1M): 10, Short-context cached input (per 1M): 1, Short-context cache write (per 1M): 12, Short-context output (per 1M): 50, Long-context input (per 1M): 20, Long-context cached input (per 1M): 2, Long-context cache write (per 1M): 25, Long-context output (per 1M): 75</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Use reasoning effort for a complex operational decision

<section class="model-example"><strong>Operational Reasoning</strong>
<p>Use reasoning effort for a complex operational decision</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.&quot;,
    &quot;max_output_tokens&quot;: 512,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;high&quot;
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;No. For a 30-day month:\n\n- Total time: \\(30 \\times 24 \\times 60 = 43{,}200\\) minutes\n- Error budget: \\(43{,}200 \\times (1 - 0.999) = 43.2\\) minutes\n- Remaining budget: \\(43.2 - 31 = 12.2\\) minutes\n\nAssuming 31 minutes is the total downtime this month, it is **within the error budget**.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0f4dd4f38f19eb60016a99d9b6aaec87d1ab6bb0c344527fbc&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1788467638,
    &quot;model&quot;: &quot;gpt-6-astra&quot;,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_0f4dd4f38f19eb60016a99d9b77c6087d1ab41b79ccdf5a833&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;encrypted_content&quot;: &quot;gAAAAABqmdm5bNo3TE240J65AqELJf45m_Forsch1ik0e0iiz5B-XZsvljWjY5PfmKXyel-6WvdoKmKulsRo3PX0fCqdNQFUaSYufMITZh61KSdsWBeeKRAwczgj8ihQBEbSF95MmTwkoQzsHX5SBitcf0n7CrMhXt8-LcE2tXqY309dnpgzAtjeI8H318LR1JyAWKsbver3s30gE1TRh0GC3YisTLrfACSclHB8_cOPA5QvEwKJNljm8R7eVDJx7LTFoB2Av93eaSD7l4fbAJzR_afL8K_Akj5NsjYaZVrsbPPxTYlYpqRhE0c-3C2U0oJ31-4UVa6_nT94QYtnDJ9YNjEdRC8sMkq6DwLhkbIIJGVNJGqHmWP3vQu3JCq9VDUtC3ss3FCkgWwhIV5tAFTFOtppnHenz1Xi2UYwaBNwaHWYJdrTBidNcpEQwPcIdSRAfOHv2r-ueFywhAZmj8Rx_GcJO_5_RWjvglhuNRBTbC92icwLx6wt4LWYBpLW-0itkHNtdy2cqsiKYSxWyMRzaEwyhW3wQo6jC9w9MRUG35wT3drTsuvnMDV5yhtzCtxq57eTRpIpCM9343ITl5DUwS-d7vouI7QH2MAIkZknxTO-_vVPYVQrQ4Th0g6Cb8CrGd-nHQ39xYKnPG7oUmvRobLSaGpKmQREzp-uoQeVK8dypZCl3Xd1uHSUO7w-HKsob-t5whmpE-ziHFaqciWh9YcssC0YE1ztbq0f9tGRy386ZzkkihD23sGR0khZukCdiGSw3Njakpe4AMWujU-t2BtomDJa6pdtLEuvG7p3MbIbHRoXkyK-9h74NgBY2jO7fk0BgItjpmqhcPHelCtMxIhP_OroanM0rCUjfQdqcSBVxwOd_hJ5wcNHmWdyf3gVvKEO83M4cj-sVljJ1afzFfhFsAQH5Zw-JTeBI1udknm3oy5lDwEzRoZpTcQs2Ix8lyUBtZ4MypqRLTnKLXzyij8G8XdgTIqwUkOHhMrm8Zc0_ndcrwPoVjwTq0NugRGJMDAxPKl-aqg6XvEfCYCUF2WYIu8jGo3KK6An8GJ5HFLyidgUslKGJtN2TJmKBOPwc0fXoiW4qyUQdVi2Hz23KBMOQE77jIF0cccZAWDToq67zPLVw9I4j-VKRpti-tOfcg9tz0wr4zJRi49uOqTw038Xn03VXzTolhb3GwwQkMZxWLjam3buEX6SLuS1A7XXZn3aKeLu6KhUin6_aR3jP0s2_Y50Mjv3x0EouaIKQJEINqYRgi9K2SKAxzRSKjGksdNGNcNRGs6cydkHSJF-f60p9HRBbBsN7duP8qm0K2URSJ1DX30=&quot;,
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;msg_0f4dd4f38f19eb60016a99d9b7d7f087d191f17156c41c2f32&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;No. For a 30-day month:\n\n- Total time: \\(30 \\times 24 \\times 60 = 43{,}200\\) minutes\n- Error budget: \\(43{,}200 \\times (1 - 0.999) = 43.2\\) minutes\n- Remaining budget: \\(43.2 - 31 = 12.2\\) minutes\n\nAssuming 31 minutes is the total downtime this month, it is **within the error budget**.&quot;
          }
        ],
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      }
    ],
    &quot;status&quot;: &quot;completed&quot;,
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 44,
      &quot;output_tokens&quot;: 151,
      &quot;total_tokens&quot;: 195,
      &quot;input_tokens_details&quot;: {
        &quot;cache_write_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 41
      }
    },
    &quot;access_programs&quot;: {
      &quot;cyber&quot;: &quot;standard&quot;
    },
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1788467641,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 512,
    &quot;max_tool_calls&quot;: null,
    &quot;moderation&quot;: null,
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;24h&quot;,
    &quot;reasoning&quot;: {
      &quot;context&quot;: &quot;all_turns&quot;,
      &quot;effort&quot;: &quot;high&quot;,
      &quot;mode&quot;: &quot;standard&quot;,
      &quot;summary&quot;: null
    },
    &quot;safety_identifier&quot;: null,
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;store&quot;: false,
    &quot;temperature&quot;: 1,
    &quot;text&quot;: {
      &quot;format&quot;: {
        &quot;type&quot;: &quot;text&quot;
      },
      &quot;verbosity&quot;: &quot;medium&quot;
    },
    &quot;tool_choice&quot;: &quot;auto&quot;,
    &quot;tool_usage&quot;: {
      &quot;image_gen&quot;: {
        &quot;input_tokens&quot;: 0,
        &quot;input_tokens_details&quot;: {
          &quot;image_tokens&quot;: 0,
          &quot;text_tokens&quot;: 0
        },
        &quot;output_tokens&quot;: 0,
        &quot;output_tokens_details&quot;: {
          &quot;image_tokens&quot;: 0,
          &quot;text_tokens&quot;: 0
        },
        &quot;total_tokens&quot;: 0
      },
      &quot;web_search&quot;: {
        &quot;num_requests&quot;: 0
      }
    },
    &quot;tools&quot;: [],
    &quot;top_logprobs&quot;: 0,
    &quot;top_p&quot;: 0.98,
    &quot;truncation&quot;: &quot;disabled&quot;,
    &quot;user&quot;: null,
    &quot;metadata&quot;: {},
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-6-astra&#x27;,
  {
    input:
      &#x27;A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.&#x27;,
    max_output_tokens: 512,
    reasoning: { effort: &#x27;high&#x27; },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-6-astra&quot;,
  &quot;input&quot;: &quot;A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.&quot;,
  &quot;max_output_tokens&quot;: 512,
  &quot;reasoning&quot;: {
    &quot;effort&quot;: &quot;high&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Migration Safeguards</strong>
<p>Generate a concise answer through Chat Completions</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;messages&quot;: [
      {
        &quot;role&quot;: &quot;user&quot;,
        &quot;content&quot;: &quot;List three practical safeguards for a production API migration.&quot;
      }
    ],
    &quot;max_completion_tokens&quot;: 256
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;1. **Validate compatibility before rollout.** Run contract and integration tests against real client behaviors. Keep breaking changes behind a new API version, and verify authentication, error formats, and data schemas.\n\n2. **Roll out gradually with monitoring.** Start with internal traffic or a small canary group. Track error rates, latency, and critical business metrics; pause expansion if predefined thresholds are exceeded.\n\n3. **Prepare and test rollback.** Keep the old API available and use a feature flag or traffic switch to revert quickly. Ensure database changes remain backward-compatible, and rehearse the rollback procedure.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;chatcmpl-EK8QDqH1XsfW6m8nEHXxUkrKGcWG5&quot;,
    &quot;object&quot;: &quot;chat.completion&quot;,
    &quot;created&quot;: 1788467641,
    &quot;model&quot;: &quot;gpt-6-astra&quot;,
    &quot;choices&quot;: [
      {
        &quot;index&quot;: 0,
        &quot;message&quot;: {
          &quot;role&quot;: &quot;assistant&quot;,
          &quot;content&quot;: &quot;1. **Validate compatibility before rollout.** Run contract and integration tests against real client behaviors. Keep breaking changes behind a new API version, and verify authentication, error formats, and data schemas.\n\n2. **Roll out gradually with monitoring.** Start with internal traffic or a small canary group. Track error rates, latency, and critical business metrics; pause expansion if predefined thresholds are exceeded.\n\n3. **Prepare and test rollback.** Keep the old API available and use a feature flag or traffic switch to revert quickly. Ensure database changes remain backward-compatible, and rehearse the rollback procedure.&quot;,
          &quot;refusal&quot;: null,
          &quot;annotations&quot;: []
        },
        &quot;finish_reason&quot;: &quot;stop&quot;
      }
    ],
    &quot;usage&quot;: {
      &quot;prompt_tokens&quot;: 16,
      &quot;completion_tokens&quot;: 151,
      &quot;total_tokens&quot;: 167,
      &quot;prompt_tokens_details&quot;: {
        &quot;cached_tokens&quot;: 0,
        &quot;cache_write_tokens&quot;: 0,
        &quot;audio_tokens&quot;: 0
      },
      &quot;completion_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 23,
        &quot;audio_tokens&quot;: 0,
        &quot;accepted_prediction_tokens&quot;: 0,
        &quot;rejected_prediction_tokens&quot;: 0
      }
    },
    &quot;service_tier&quot;: &quot;default&quot;,
    &quot;system_fingerprint&quot;: null,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-6-astra&#x27;,
  {
    messages: [
      { role: &#x27;user&#x27;, content: &#x27;List three practical safeguards for a production API migration.&#x27; },
    ],
    max_completion_tokens: 256,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-6-astra&quot;,
  &quot;messages&quot;: [
    {
      &quot;role&quot;: &quot;user&quot;,
      &quot;content&quot;: &quot;List three practical safeguards for a production API migration.&quot;
    }
  ],
  &quot;max_completion_tokens&quot;: 256
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-6-astra/schema-input.json)
- [Output schema](/ai/models/openai/gpt-6-astra/schema-output.json)

