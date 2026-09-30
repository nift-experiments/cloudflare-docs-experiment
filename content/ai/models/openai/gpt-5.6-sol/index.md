<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-5-6-sol">GPT-5.6 Sol</h1>

<p><code>openai/gpt-5.6-sol</code></p>

GPT-5.6 Sol is OpenAI's frontier GPT-5.6 model for complex professional work, using the Responses API for reasoning and stateful context management.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,050,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 2, Output tokens (per 1M): 10, Cached input tokens (per 1M): 0.25, Cache creation tokens (per 1M): 3.125</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic Responses API request for complex professional planning

<section class="model-example"><strong>Launch Checklist</strong>
<p>Basic Responses API request for complex professional planning</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Create a concise launch checklist for migrating a production API to a new region.&quot;,
    &quot;instructions&quot;: &quot;Use five bullets and focus on risk reduction.&quot;,
    &quot;max_output_tokens&quot;: 512
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;- **Validate readiness:** Confirm capacity, quotas, security controls, certificates, secrets, dependencies, and compliance requirements in the new region.\n- **Protect data:** Take verified backups; validate replication consistency, encryption, retention, and restore procedures before cutover.\n- **Test end to end:** Run load, latency, failover, integration, and smoke tests using production-like traffic and data.\n- **Control cutover:** Lower DNS TTLs, deploy gradually with canary traffic, freeze risky changes, and monitor errors, latency, saturation, and data integrity.\n- **Prepare rollback:** Define go/no-go thresholds, owners, communication channels, and a rehearsed rollback plan; retain the old region until stability is confirmed.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0f038c9de2c94eb6016a4fe97e94f081909f0edfecbfb2abd9&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1783622014,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1783622017,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: &quot;Use five bullets and focus on risk reduction.&quot;,
    &quot;max_output_tokens&quot;: 512,
    &quot;max_tool_calls&quot;: null,
    &quot;model&quot;: &quot;gpt-5.6-sol&quot;,
    &quot;moderation&quot;: null,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_0f038c9de2c94eb6016a4fe97f2bac81909bf1c27c448cf46b&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;msg_0f038c9de2c94eb6016a4fe97fa0688190a1b4958a6a0aa218&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;- **Validate readiness:** Confirm capacity, quotas, security controls, certificates, secrets, dependencies, and compliance requirements in the new region.\n- **Protect data:** Take verified backups; validate replication consistency, encryption, retention, and restore procedures before cutover.\n- **Test end to end:** Run load, latency, failover, integration, and smoke tests using production-like traffic and data.\n- **Control cutover:** Lower DNS TTLs, deploy gradually with canary traffic, freeze risky changes, and monitor errors, latency, saturation, and data integrity.\n- **Prepare rollback:** Define go/no-go thresholds, owners, communication channels, and a rehearsed rollback plan; retain the old region until stability is confirmed.&quot;
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
      &quot;input_tokens&quot;: 34,
      &quot;input_tokens_details&quot;: {
        &quot;cache_write_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 182,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 32
      },
      &quot;total_tokens&quot;: 216
    },
    &quot;user&quot;: null,
    &quot;metadata&quot;: {}
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.6-sol&#x27;,
  {
    input: &#x27;Create a concise launch checklist for migrating a production API to a new region.&#x27;,
    instructions: &#x27;Use five bullets and focus on risk reduction.&#x27;,
    max_output_tokens: 512,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.6-sol&quot;,
  &quot;input&quot;: &quot;Create a concise launch checklist for migrating a production API to a new region.&quot;,
  &quot;instructions&quot;: &quot;Use five bullets and focus on risk reduction.&quot;,
  &quot;max_output_tokens&quot;: 512
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Operational Reasoning</strong>
<p>Using reasoning effort for a multi-step operational decision</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.&quot;,
    &quot;max_output_tokens&quot;: 512,
    &quot;reasoning&quot;: {
      &quot;effort&quot;: &quot;medium&quot;
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;- Total minutes in 30 days: \\(30 \\times 24 \\times 60 = 43{,}200\\)\n- Error budget at 99.9% availability: \\(43{,}200 \\times 0.001 = 43.2\\) minutes\n- Downtime used: 31 minutes\n\n**No**, it has not exceeded the monthly error budget. It has **12.2 minutes remaining**.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0fcb12a6aa68f25a016a4fe98205b881978b6ab83321e02e3b&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1783622018,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1783622020,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 512,
    &quot;max_tool_calls&quot;: null,
    &quot;model&quot;: &quot;gpt-5.6-sol&quot;,
    &quot;moderation&quot;: null,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;rs_0fcb12a6aa68f25a016a4fe98293e081979139ff657f9b612b&quot;,
        &quot;type&quot;: &quot;reasoning&quot;,
        &quot;content&quot;: [],
        &quot;summary&quot;: []
      },
      {
        &quot;id&quot;: &quot;msg_0fcb12a6aa68f25a016a4fe98354fc8197a4b488662491fdd8&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;- Total minutes in 30 days: \\(30 \\times 24 \\times 60 = 43{,}200\\)\n- Error budget at 99.9% availability: \\(43{,}200 \\times 0.001 = 43.2\\) minutes\n- Downtime used: 31 minutes\n\n**No**, it has not exceeded the monthly error budget. It has **12.2 minutes remaining**.&quot;
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
      &quot;input_tokens&quot;: 44,
      &quot;input_tokens_details&quot;: {
        &quot;cache_write_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 159,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 63
      },
      &quot;total_tokens&quot;: 203
    },
    &quot;user&quot;: null,
    &quot;metadata&quot;: {}
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.6-sol&#x27;,
  {
    input:
      &#x27;A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.&#x27;,
    max_output_tokens: 512,
    reasoning: { effort: &#x27;medium&#x27; },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.6-sol&quot;,
  &quot;input&quot;: &quot;A service has 99.9% monthly availability and just had 31 minutes of downtime. Has it exceeded the monthly error budget for a 30-day month? Show the calculation briefly.&quot;,
  &quot;max_output_tokens&quot;: 512,
  &quot;reasoning&quot;: {
    &quot;effort&quot;: &quot;medium&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-5.6-sol/schema-input.json)
- [Output schema](/ai/models/openai/gpt-5.6-sol/schema-output.json)

