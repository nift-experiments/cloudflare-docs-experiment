<p>Cloudflare offers a few public LoRA adapters that can immediately be used for fine-tuned inference. You can try them out immediately via our <a href="https://playground.ai.cloudflare.com">playground</a>.</p>
<p>Public LoRAs will have the name <code>cf-public-x</code>, and the prefix will be reserved for Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15822.md")
</aside>
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Compatible with</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://huggingface.co/predibase/magicoder">cf-public-magicoder</a></td>
<td>Coding tasks in multiple languages</td>
<td><code>@cf/mistral/mistral-7b-instruct-v0.1</code> <br/> <code>@hf/mistral/mistral-7b-instruct-v0.2</code></td>
</tr>
<tr>
<td><a href="https://huggingface.co/predibase/jigsaw">cf-public-jigsaw-classification</a></td>
<td>Toxic comment classification</td>
<td><code>@cf/mistral/mistral-7b-instruct-v0.1</code> <br/> <code>@hf/mistral/mistral-7b-instruct-v0.2</code></td>
</tr>
<tr>
<td><a href="https://huggingface.co/predibase/cnn">cf-public-cnn-summarization</a></td>
<td>Article summarization</td>
<td><code>@cf/mistral/mistral-7b-instruct-v0.1</code> <br/> <code>@hf/mistral/mistral-7b-instruct-v0.2</code></td>
</tr>
</tbody>
</table>
<p>You can also list these public LoRAs with an API call:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/finetunes/public \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="running-inference-with-public-loras">Running inference with public LoRAs</h2>
<p>To run inference with public LoRAs, you just need to define the LoRA name in the request.</p>
<p>We recommend that you use the prompt template that the LoRA was trained on. You can find this in the HuggingFace repos linked above for each adapter.</p>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/mistral/mistral-7b-instruct-v0.1 \&#10;  &#45;-header &#x27;Authorization: Bearer {cf_token}&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;Write a python program to check if a number is even or odd.&quot;&#10;      }&#10;    ],&#10;    &quot;lora&quot;: &quot;cf-public-magicoder&quot;&#10;  }&#x27;&#10;</code></pre>
<h3 id="javascript">JavaScript</h3>
<pre><code class="language-js">const answer = await env.AI.run(&quot;@cf/mistral/mistral-7b-instruct-v0.1&quot;, {&#10;	stream: true,&#10;	raw: true,&#10;	messages: [&#10;		{&#10;			role: &quot;user&quot;,&#10;			content:&#10;				&quot;Summarize the following: Some newspapers, TV channels and well-known companies publish false news stories to fool people on 1 April. One of the earliest examples of this was in 1957 when a programme on the BBC, the UKs national TV channel, broadcast a report on how spaghetti grew on trees. The film showed a family in Switzerland collecting spaghetti from trees and many people were fooled into believing it, as in the 1950s British people didn&#x27;t eat much pasta and many didn&#x27;t know how it was made! Most British people wouldnt fall for the spaghetti trick today, but in 2008 the BBC managed to fool their audience again with their Miracles of Evolution trailer, which appeared to show some special penguins that had regained the ability to fly. Two major UK newspapers, The Daily Telegraph and the Daily Mirror, published the important story on their front pages.&quot;,&#10;		},&#10;	],&#10;	lora: &quot;cf-public-cnn-summarization&quot;,&#10;});&#10;</code></pre>
