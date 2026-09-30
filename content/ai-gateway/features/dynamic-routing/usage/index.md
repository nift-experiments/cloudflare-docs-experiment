<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2894.md")
</aside>
<h2 id="examples">Examples</h2>
<h3 id="openai-sdk">OpenAI SDK</h3>
<pre><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;&#10;const cloudflareToken = &quot;CF_AIG_TOKEN&quot;;&#10;const accountId = &quot;{account_id}&quot;;&#10;const gatewayId = &quot;{gateway_id}&quot;;&#10;const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/compat`;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: cloudflareToken,&#10;	baseURL,&#10;});&#10;&#10;try {&#10;	const model = &quot;dynamic/&lt;your-dynamic-route-name&gt;&quot;;&#10;	const messages = [{ role: &quot;user&quot;, content: &quot;What is a neuron?&quot; }];&#10;	const chatCompletion = await openai.chat.completions.create({&#10;		model,&#10;		messages,&#10;	});&#10;	const response = chatCompletion.choices[0].message;&#10;	console.log(response);&#10;} catch (e) {&#10;	console.error(e);&#10;}&#10;</code></pre>
<h3 id="fetch">Fetch</h3>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \&#10;  &#45;-header &#x27;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;dynamic/&lt;your-dynamic-route-name&gt;&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="workers">Workers</h3>
<pre><code class="language-ts">export interface Env {&#10;	AI: Ai;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const response = await env.AI.gateway(&quot;default&quot;).run({&#10;			provider: &quot;compat&quot;,&#10;			endpoint: &quot;chat/completions&quot;,&#10;			headers: {},&#10;			query: {&#10;				model: &quot;dynamic/&lt;your-dynamic-route-name&gt;&quot;,&#10;				messages: [&#10;					{&#10;						role: &quot;user&quot;,&#10;						content: &quot;What is Cloudflare?&quot;,&#10;					},&#10;				],&#10;			},&#10;		});&#10;		return Response(response);&#10;	},&#10;};&#10;</code></pre>
<h2 id="response-metadata">Response Metadata</h2>
<p>The response from a dynamic route is the same as the response from a model. There is additional metadata used to notify the model and provider used, you can check the following headers</p>
<ul>
<li><code>cf-aig-model</code> - The model used</li>
<li><code>cf-aig-provider</code> - The slug of provider used</li>
</ul>
