<p>Set <code>rejectIfBusy</code> when your application should not wait in a capacity queue. Workers AI rejects the synchronous inference request if capacity is unavailable.</p>
<h2 id="send-a-rest-request">Send a REST request</h2>
<p>For the native REST API, add <code>rejectIfBusy</code> to the request <code>options</code> object:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;Explain what a capacity queue is.&quot;&#10;      }&#10;    ],&#10;    &quot;options&quot;: {&#10;      &quot;rejectIfBusy&quot;: true&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h2 id="use-the-workers-binding">Use the Workers binding</h2>
<p>For the Workers AI binding, pass <code>rejectIfBusy</code> in the third argument to <code>env.AI.run()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15815.md")
</div>
<p>Do not add <code>rejectIfBusy</code> to the model input object. The binding only applies this option from the third argument.</p>
<h2 id="call-chat-completions">Call Chat Completions</h2>
<p>For OpenAI-compatible Chat Completions, add <code>options</code> at the top level of the request body:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;@cf/google/gemma-4-26b-a4b-it&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;Explain what a capacity queue is.&quot;&#10;      }&#10;    ],&#10;    &quot;options&quot;: {&#10;      &quot;rejectIfBusy&quot;: true&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>OpenAI clients that preserve custom fields can send this option. Clients that remove unknown fields do not apply it, so requests proceed normally.</p>
<h2 id="handle-capacity-errors">Handle capacity errors</h2>
<p>Rejected requests return HTTP status <code>429</code> and internal error code <code>3040</code>. The error message is <code>Capacity temporarily exceeded, please try again.</code></p>
<p>Refer to <a href="/workers-ai/platform/errors/">Workers AI errors</a> for error details.</p>
