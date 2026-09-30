<img src="/assets/upstream/images/workers-ai/openai.svg" alt="Openai logo" width="48" height="48">

<h1 id="gpt-5-6-luna">GPT-5.6 Luna</h1>

<p><code>openai/gpt-5.6-luna</code></p>

GPT-5.6 Luna is an OpenAI GPT-5.6 model optimized for cost-sensitive workloads, using the Responses API for efficient text generation.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,050,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://openai.com/policies/">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 0.2, Output tokens (per 1M): 1.2, Cached input tokens (per 1M): 0.02, Cache creation tokens (per 1M): 0.25</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic Responses API request for a concise summary task

<section class="model-example"><strong>Rate Limiting Summary</strong>
<p>Basic Responses API request for a concise summary task</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Summarize the benefits of API rate limiting in three bullets.&quot;,
    &quot;max_output_tokens&quot;: 256
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;- **Protects system stability:** Prevents overload, reduces outages, and ensures predictable performance during traffic spikes.\n- **Ensures fair access:** Stops individual users or applications from consuming disproportionate resources.\n- **Improves security and cost control:** Helps mitigate abuse, brute-force attacks, and unexpected infrastructure usage.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0e481f0cb46bf357016a4fe99bd5fc8194b6ce2049aa65ab08&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1783622043,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1783622044,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: null,
    &quot;max_output_tokens&quot;: 256,
    &quot;max_tool_calls&quot;: null,
    &quot;model&quot;: &quot;gpt-5.6-luna&quot;,
    &quot;moderation&quot;: null,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;msg_0e481f0cb46bf357016a4fe99c2e288194a6fd0ce3f5f88786&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;- **Protects system stability:** Prevents overload, reduces outages, and ensures predictable performance during traffic spikes.\n- **Ensures fair access:** Stops individual users or applications from consuming disproportionate resources.\n- **Improves security and cost control:** Helps mitigate abuse, brute-force attacks, and unexpected infrastructure usage.&quot;
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
      &quot;input_tokens&quot;: 19,
      &quot;input_tokens_details&quot;: {
        &quot;cache_write_tokens&quot;: 0,
        &quot;cached_tokens&quot;: 0
      },
      &quot;output_tokens&quot;: 66,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 85
    },
    &quot;user&quot;: null,
    &quot;metadata&quot;: {}
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.6-luna&#x27;,
  {
    input: &#x27;Summarize the benefits of API rate limiting in three bullets.&#x27;,
    max_output_tokens: 256,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.6-luna&quot;,
  &quot;input&quot;: &quot;Summarize the benefits of API rate limiting in three bullets.&quot;,
  &quot;max_output_tokens&quot;: 256
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Pull Request Description</strong>
<p>Using instructions for a cost-sensitive drafting task</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;input&quot;: &quot;Write a brief pull request description for a bug fix that prevents duplicate webhook deliveries.&quot;,
    &quot;instructions&quot;: &quot;Keep it under 100 words.&quot;,
    &quot;max_output_tokens&quot;: 256
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;## Summary\nPrevents duplicate webhook deliveries by ensuring each event is processed only once, even when retries or concurrent requests occur.\n\n## Changes\n- Added idempotency checks for webhook events.\n- Prevented duplicate delivery attempts.\n- Added regression tests covering retries and concurrent processing.\n\n## Testing\nAll existing and new tests pass.&quot;
  },
  &quot;raw_response&quot;: {
    &quot;id&quot;: &quot;resp_0bed05adeda548a1016a4fe99d1e408194bb0375bad96ab71a&quot;,
    &quot;object&quot;: &quot;response&quot;,
    &quot;created_at&quot;: 1783622045,
    &quot;status&quot;: &quot;completed&quot;,
    &quot;background&quot;: false,
    &quot;billing&quot;: {
      &quot;payer&quot;: &quot;developer&quot;
    },
    &quot;completed_at&quot;: 1783622046,
    &quot;error&quot;: null,
    &quot;frequency_penalty&quot;: 0,
    &quot;incomplete_details&quot;: null,
    &quot;instructions&quot;: &quot;Keep it under 100 words.&quot;,
    &quot;max_output_tokens&quot;: 256,
    &quot;max_tool_calls&quot;: null,
    &quot;model&quot;: &quot;gpt-5.6-luna&quot;,
    &quot;moderation&quot;: null,
    &quot;output&quot;: [
      {
        &quot;id&quot;: &quot;msg_0bed05adeda548a1016a4fe99daa748194992854423ba08e72&quot;,
        &quot;type&quot;: &quot;message&quot;,
        &quot;status&quot;: &quot;completed&quot;,
        &quot;content&quot;: [
          {
            &quot;type&quot;: &quot;output_text&quot;,
            &quot;annotations&quot;: [],
            &quot;logprobs&quot;: [],
            &quot;text&quot;: &quot;## Summary\nPrevents duplicate webhook deliveries by ensuring each event is processed only once, even when retries or concurrent requests occur.\n\n## Changes\n- Added idempotency checks for webhook events.\n- Prevented duplicate delivery attempts.\n- Added regression tests covering retries and concurrent processing.\n\n## Testing\nAll existing and new tests pass.&quot;
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
      &quot;output_tokens&quot;: 69,
      &quot;output_tokens_details&quot;: {
        &quot;reasoning_tokens&quot;: 0
      },
      &quot;total_tokens&quot;: 102
    },
    &quot;user&quot;: null,
    &quot;metadata&quot;: {}
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;openai/gpt-5.6-luna&#x27;,
  {
    input:
      &#x27;Write a brief pull request description for a bug fix that prevents duplicate webhook deliveries.&#x27;,
    instructions: &#x27;Keep it under 100 words.&#x27;,
    max_output_tokens: 256,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/responses \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;openai/gpt-5.6-luna&quot;,
  &quot;input&quot;: &quot;Write a brief pull request description for a bug fix that prevents duplicate webhook deliveries.&quot;,
  &quot;instructions&quot;: &quot;Keep it under 100 words.&quot;,
  &quot;max_output_tokens&quot;: 256
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string or array</td><td>Required.</td></tr><tr><td><code>instructions</code></td><td>string</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_output_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>text</code></td><td>object</td><td></td></tr><tr><td><code>text.format</code></td><td>object</td><td></td></tr><tr><td><code>reasoning</code></td><td>object</td><td></td></tr><tr><td><code>reasoning.effort</code></td><td>string</td><td>Values: none, low, medium, high</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created_at</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>output</code></td><td>array</td><td>Required.</td></tr><tr><td><code>output_text</code></td><td>string</td><td></td></tr><tr><td><code>status</code></td><td>string</td><td>Values: in_progress, completed, failed, incomplete</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.input_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.output_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/openai/gpt-5.6-luna/schema-input.json)
- [Output schema](/ai/models/openai/gpt-5.6-luna/schema-output.json)

