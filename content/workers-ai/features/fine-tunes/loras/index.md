<p>Workers AI supports fine-tuned inference with adapters trained with <a href="https://blog.cloudflare.com/fine-tuned-inference-with-loras">Low-Rank Adaptation</a>. This feature is in open beta and free during this period.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>We only support LoRAs for a <a href="/workers-ai/models/?capabilities=LoRA">variety of models</a> (must not be quantized)</li>
<li>Adapter must be trained with rank <code>r &lt;=8</code> as well as larger ranks if up to 32. You can check the rank of a pre-trained LoRA adapter through the adapter's <code>config.json</code> file</li>
<li>LoRA adapter file must be &lt; 300MB</li>
<li>LoRA adapter files must be named <code>adapter_config.json</code> and <code>adapter_model.safetensors</code> exactly</li>
<li>You can test up to 100 LoRA adapters per account</li>
</ul>
<hr />
<h2 id="choosing-compatible-lora-adapters">Choosing compatible LoRA adapters</h2>
<h3 id="finding-open-source-lora-adapters">Finding open-source LoRA adapters</h3>
<p>We have started a <a href="https://huggingface.co/collections/Cloudflare/workers-ai-compatible-loras-6608dd9f8d305a46e355746e">Hugging Face Collection</a> that lists a few LoRA adapters that are compatible with Workers AI. Generally, any LoRA adapter that fits our limitations above should work.</p>
<h3 id="training-your-own-lora-adapters">Training your own LoRA adapters</h3>
<p>To train your own LoRA adapter, follow the <a href="/workers-ai/guides/tutorials/fine-tune-models-with-autotrain/">tutorial</a>.</p>
<hr />
<h2 id="uploading-lora-adapters">Uploading LoRA adapters</h2>
<p>In order to run inference with LoRAs on Workers AI, you'll need to create a new fine tune on your account and upload your adapter files. You should have a <code>adapter_model.safetensors</code> file with model weights and <code>adapter_config.json</code> with your config information. <em>Note that we only accept adapter files in these types.</em></p>
<p>Right now, you can't edit a fine tune's asset files after you upload it. We will support this soon, but for now you will need to create a new fine tune and upload files again if you would like to use a new LoRA.</p>
<p>Before you upload your LoRA adapter, you'll need to edit your <code>adapter_config.json</code> file to include <code>model_type</code> as one of <code>mistral</code>, <code>gemma</code> or <code>llama</code> like below.</p>
<pre><code class="language-json">{&#10;  &quot;alpha_pattern&quot;: {},&#10;  &quot;auto_mapping&quot;: null,&#10;  ...&#10;  &quot;target_modules&quot;: [&#10;    &quot;q_proj&quot;,&#10;    &quot;v_proj&quot;&#10;  ],&#10;  &quot;task_type&quot;: &quot;CAUSAL_LM&quot;,&#10;  &quot;model_type&quot;: &quot;mistral&quot;,&#10;}&#10;</code></pre>
<h3 id="wrangler">Wrangler</h3>
<p>You can create a finetune and upload your LoRA adapter via wrangler with the following commands:</p>
<pre><code class="language-bash">npx wrangler ai finetune create &lt;model_name&gt; &lt;finetune_name&gt; &lt;folder_path&gt;&#10;&#35;🌀 Creating new finetune &quot;test-lora&quot; for model &quot;@cf/mistral/mistral-7b-instruct-v0.2-lora&quot;...&#10;&#35;🌀 Uploading file &quot;/Users/abcd/Downloads/adapter_config.json&quot; to &quot;test-lora&quot;...&#10;&#35;🌀 Uploading file &quot;/Users/abcd/Downloads/adapter_model.safetensors&quot; to &quot;test-lora&quot;...&#10;&#35;✅ Assets uploaded, finetune &quot;test-lora&quot; is ready to use.&#10;&#10;npx wrangler ai finetune list&#10;┌──────────────────────────────────────┬─────────────────┬─────────────┐&#10;│ finetune_id                          │ name            │ description │&#10;├──────────────────────────────────────┼─────────────────┼─────────────┤&#10;│ 00000000-0000-0000-0000-000000000000 │ test-lora       │             │&#10;└──────────────────────────────────────┴─────────────────┴─────────────┘&#10;</code></pre>
<h3 id="rest-api">REST API</h3>
<p>Alternatively, you can use our REST API to create a finetune and upload your adapter files. You will need a Cloudflare API Token with <code>Workers AI: Edit</code> permissions to make calls to our REST API, which you can generate via the Cloudflare Dashboard.</p>
<h4 id="creating-a-fine-tune-on-your-account">Creating a fine-tune on your account</h4>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/finetunes \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;model&quot;: &quot;SUPPORTED_MODEL_NAME&quot;,&#10;  &quot;name&quot;: &quot;FINETUNE_NAME&quot;,&#10;  &quot;description&quot;: &quot;OPTIONAL_DESCRIPTION&quot;&#10;}&#x27;</code></pre>
<h4 id="uploading-your-adapter-weights-and-config">Uploading your adapter weights and config</h4>
<p>You have to call the upload endpoint each time you want to upload a new file, so you usually run this once for <code>adapter_model.safetensors</code> and once for <code>adapter_config.json</code>. Make sure you include the <code>@</code> before your path to files.</p>
<p>You can either use the finetune <code>name</code> or <code>id</code> that you used when you created the fine tune.</p>
<pre><code class="language-bash">&#35;# Input: finetune_id, adapter_model.safetensors, then adapter_config.json&#10;&#35;# Output: success true/false&#10;&#10;curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/finetunes/{FINETUNE_ID}/finetune-assets/ \&#10;    &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;    &#45;H &#x27;Content-Type: multipart/form-data&#x27; \&#10;    &#45;F &#x27;file_name=adapter_model.safetensors&#x27; \&#10;    &#45;F &#x27;file=@{PATH/TO/adapter_model.safetensors}&#x27;&#10;</code></pre>
<h4 id="list-fine-tunes-in-your-account">List fine-tunes in your account</h4>
<p>You can call this method to confirm what fine-tunes you have created in your account</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/finetunes \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: [&#10;		[&#10;			{&#10;				&quot;id&quot;: &quot;00000000-0000-0000-0000-000000000&quot;,&#10;				&quot;model&quot;: &quot;@cf/meta-llama/llama-2-7b-chat-hf-lora&quot;,&#10;				&quot;name&quot;: &quot;llama2-finetune&quot;,&#10;				&quot;description&quot;: &quot;test&quot;&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;00000000-0000-0000-0000-000000000&quot;,&#10;				&quot;model&quot;: &quot;@cf/mistralai/mistral-7b-instruct-v0.2-lora&quot;,&#10;				&quot;name&quot;: &quot;mistral-finetune&quot;,&#10;				&quot;description&quot;: &quot;test&quot;&#10;			}&#10;		]&#10;	]&#10;}&#10;</code></pre>
<hr />
<h2 id="running-inference-with-loras">Running inference with LoRAs</h2>
<p>To make inference requests and apply the LoRA adapter, you will need your model and finetune <code>name</code> or <code>id</code>. You should use the chat template that your LoRA was trained on, but you can try running it with <code>raw: true</code> and the messages template like below.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15825.md")
</div></div>
