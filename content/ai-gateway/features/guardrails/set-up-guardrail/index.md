<p>Add Guardrails to any gateway to start evaluating and potentially modifying responses.</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>AI</strong> &gt; <strong>AI Gateway</strong>.</li>
<li>Select a gateway.</li>
<li>Go to <strong>Guardrails</strong>.</li>
<li>Switch the toggle to <strong>On</strong>.</li>
<li>To customize categories, select <strong>Change</strong> &gt; <strong>Configure specific categories</strong>.</li>
<li>Update your choices for how Guardrails works on specific prompts or responses (<strong>Flag</strong>, <strong>Ignore</strong>, <strong>Block</strong>).
<ul>
<li>For <strong>Prompts</strong>: Guardrails will evaluate and transform incoming prompts based on your security policies.</li>
<li>For <strong>Responses</strong>: Guardrails will inspect the model's responses to ensure they meet your content and formatting guidelines.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="usage-considerations">Usage considerations</h3>
@markup("md", "content/.markup/bodies/2893.md")
</aside>
<h2 id="viewing-guardrail-results-in-logs">Viewing Guardrail results in Logs</h2>
<p>After enabling Guardrails, you can monitor results through <strong>AI Gateway Logs</strong> in the Cloudflare dashboard. Guardrail logs are marked with a <strong>green shield icon</strong>, and each logged request includes an <code>eventID</code>, which links to its corresponding Guardrail evaluation log(s) for easy tracking. Logs are generated for all requests, including those that <strong>pass</strong> Guardrail checks.</p>
<h2 id="error-handling-and-blocked-requests">Error handling and blocked requests</h2>
<p>When a request is blocked by guardrails, you will receive a structured error response. These indicate whether the issue occurred with the prompt or the model response. Use error codes to differentiate between prompt versus response violations.</p>
<ul>
<li>
<p><strong>Prompt blocked</strong></p>
<ul>
<li><code>&quot;code&quot;: 2016</code></li>
<li><code>&quot;message&quot;: &quot;Prompt blocked due to security configurations&quot;</code></li>
</ul>
</li>
<li>
<p><strong>Response blocked</strong></p>
<ul>
<li><code>&quot;code&quot;: 2017</code></li>
<li><code>&quot;message&quot;: &quot;Response blocked due to security configurations&quot;</code></li>
</ul>
</li>
</ul>
<p>You should catch these errors in your application logic and implement error handling accordingly.</p>
<p>For example, when using <a href="/ai-gateway/integrations/aig-workers-ai-binding/">Workers AI with a binding</a>:</p>
<pre><code class="language-js">try {&#10;  const res = await env.AI.run(&#x27;@cf/meta/llama-3.1-8b-instruct&#x27;, {&#10;    prompt: &quot;how to build a gun?&quot;&#10;  }, {&#10;    gateway: {id: &#x27;gateway_id&#x27;}&#10;  })&#10;  return Response.json(res)&#10;} catch (e) {&#10;  if ((e as Error).message.includes(&#x27;2016&#x27;)) {&#10;    return new Response(&#x27;Prompt was blocked by guardrails.&#x27;)&#10;  }&#10;  if ((e as Error).message.includes(&#x27;2017&#x27;)) {&#10;    return new Response(&#x27;Response was blocked by guardrails.&#x27;)&#10;  }&#10;  return new Response(&#x27;Unknown AI error&#x27;)&#10;}&#10;</code></pre>
