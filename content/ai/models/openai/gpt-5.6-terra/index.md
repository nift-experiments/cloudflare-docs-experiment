<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-5-6-terra">GPT-5.6 Terra</h1>

<p><code>openai/gpt-5.6-terra</code></p>

GPT-5.6 Terra is an OpenAI GPT-5.6 model that balances intelligence and cost, using the Responses API for reasoning and stateful context management.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,050,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 12, Cached input tokens (per 1M): 0.2, Cache creation tokens (per 1M): 2.5</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic Responses API request for a balanced analysis task

<section class="model-example"><strong>Deployment Comparison</strong>
<p>Basic Responses API request for a balanced analysis task</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Compare blue-green and canary deployments for a small engineering team.&quot;,
    &quot;instructions&quot;: &quot;Answer in two concise paragraphs.&quot;,
    &quot;max_output_tokens&quot;: 512
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Blue-green deployments run two identical production environments: one active (\u201cblue\u201d) and one idle (\u201cgreen\u201d). A new version is deployed and tested on green, then traffic is switched over all at once. This makes rollback very fast\u2014switch traffic back to blue\u2014but requires maintaining duplicate infrastructure and handling database/schema compatibility carefully. For a small team, blue-green is often appealing when releases are infrequent, the system is simple enough to duplicate cheaply, and a clear cutover/rollback procedure matters more than gradual validation.\n\nCanary deployments release the new version to a small percentage of users or requests first, then progressively increase traffic while monitoring errors, latency, and business metrics. They reduce the blast radius of defects and provide real-production validation, but require traffic splitting, strong observability, automated rollout controls, and usually feature-flag or version-compatibility discipline. For a small team, canaries are best when the platform already supports them or when the cost of a faulty release is high; otherwise, blue-green generally offers a simpler operational model.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_06924a0adf314715016a4fe98e1d2c81978067f843c9a357f1&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1783622030,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1783622032,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: &quot;Answer in two concise paragraphs.&quot;,
    &quot;max_output_tokens&quot;: 512,
    &quot;max_tool_calls&quot;: null,
    &quot;model&quot;: &quot;gpt-5.6-terra&quot;,
    &quot;moderation&quot;: null,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;msg_06924a0adf314715016a4fe98e76c4819780adfca3dd3ad1f3&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;Blue-green deployments run two identical production environments: one active (\u201cblue\u201d) and one idle (\u201cgreen\u201d). A new version is deployed and tested on green, then traffic is switched over all at once. This makes rollback very fast\u2014switch traffic back to blue\u2014but requires maintaining duplicate infrastructure and handling database/schema compatibility carefully. For a small team, blue-green is often appealing when releases are infrequent, the system is simple enough to duplicate cheaply, and a clear cutover/rollback procedure matters more than gradual validation.\n\nCanary deployments release the new version to a small percentage of users or requests first, then progressively increase traffic while monitoring errors, latency, and business metrics. They reduce the blast radius of defects and provide real-production validation, but require traffic splitting, strong observability, automated rollout controls, and usually feature-flag or version-compatibility discipline. For a small team, canaries are best when the platform already supports them or when the cost of a faulty release is high; otherwise, blue-green generally offers a simpler operational model.&quot;
          }
        ],
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
    &quot;reasoning&quot;: {
      &quot;context&quot;: &quot;all_turns&quot;,
      &quot;effort&quot;: &quot;medium&quot;,
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
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 29,
      &quot;input_tokens_details&quot;: {
        &quot;cache_write_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 211,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 240
    },
    &quot;user&quot;: null,
    &quot;metadata&quot;: {}
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.6-terra&#x27;,
  {
    input: &#x27;Compare blue-green and canary deployments for a small engineering team.&#x27;,
    instructions: &#x27;Answer in two concise paragraphs.&#x27;,
    max_output_tokens: 512,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.6-terra&quot;,
  &quot;input&quot;: &quot;Compare blue-green and canary deployments for a small engineering team.&quot;,
  &quot;instructions&quot;: &quot;Answer in two concise paragraphs.&quot;,
  &quot;max_output_tokens&quot;: 512
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Customer Incident Update</strong>
<p>Using instructions to tune the model's response style</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Draft a short incident update for customers after elevated API latency.&quot;,
    &quot;instructions&quot;: &quot;Be transparent, calm, and avoid unnecessary technical detail.&quot;,
    &quot;max_output_tokens&quot;: 512
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;**Incident Update:**  \nEarlier today, some customers experienced elevated API latency. Our team identified the issue and applied mitigation steps, and API performance has returned to normal.\n\nWe\u2019ll continue monitoring closely and will share a follow-up with additional details if needed. We apologize for the disruption and appreciate your patience.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0072e6076b1b184d016a4fe99105888190b25ef699c2a83380&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1783622033,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1783622034,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: &quot;Be transparent, calm, and avoid unnecessary technical detail.&quot;,
    &quot;max_output_tokens&quot;: 512,
    &quot;max_tool_calls&quot;: null,
    &quot;model&quot;: &quot;gpt-5.6-terra&quot;,
    &quot;moderation&quot;: null,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;msg_0072e6076b1b184d016a4fe9916d6081909385f3b15352b1a7&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;**Incident Update:**  \nEarlier today, some customers experienced elevated API latency. Our team identified the issue and applied mitigation steps, and API performance has returned to normal.\n\nWe\u2019ll continue monitoring closely and will share a follow-up with additional details if needed. We apologize for the disruption and appreciate your patience.&quot;
          }
        ],
        &quot;phase&quot;: &quot;final_answer&quot;,
        &quot;role&quot;: &quot;assistant&quot;
      }
    ],
    &quot;parallel_tool_calls&quot;: true,
    &quot;presence_penalty&quot;: 0,
    &quot;previous_response_id&quot;: null,
    &quot;prompt_cache_key&quot;: null,
    &quot;prompt_cache_retention&quot;: &quot;in_memory&quot;,
    &quot;reasoning&quot;: {
      &quot;context&quot;: &quot;all_turns&quot;,
      &quot;effort&quot;: &quot;medium&quot;,
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
    &quot;usage&quot;: {
      &quot;input_tokens&quot;: 33,
      &quot;input_tokens_details&quot;: {
        &quot;cache_write_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 64,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 97
    },
    &quot;user&quot;: null,
    &quot;metadata&quot;: {}
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.6-terra&#x27;,
  {
    input: &#x27;Draft a short incident update for customers after elevated API latency.&#x27;,
    instructions: &#x27;Be transparent, calm, and avoid unnecessary technical detail.&#x27;,
    max_output_tokens: 512,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.6-terra&quot;,
  &quot;input&quot;: &quot;Draft a short incident update for customers after elevated API latency.&quot;,
  &quot;instructions&quot;: &quot;Be transparent, calm, and avoid unnecessary technical detail.&quot;,
  &quot;max_output_tokens&quot;: 512
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-5.6-terra/schema-input.json)
- [Output schema](/ai/models/openai/gpt-5.6-terra/schema-output.json)

