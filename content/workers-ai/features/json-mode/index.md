<p>response_format: {
title: &quot;JSON Mode&quot;,
type: &quot;object&quot;,
properties: {
type: {
type: &quot;string&quot;,
enum: [&quot;json_object&quot;, &quot;json_schema&quot;],
},
json_schema: {},
}
}
}`;</p>
<p>&quot;messages&quot;: [
{
&quot;role&quot;: &quot;system&quot;,
&quot;content&quot;: &quot;Extract data about a country.&quot;
},
{
&quot;role&quot;: &quot;user&quot;,
&quot;content&quot;: &quot;Tell me about India.&quot;
}
],
&quot;response_format&quot;: {
&quot;type&quot;: &quot;json_schema&quot;,
&quot;json_schema&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;name&quot;: {
&quot;type&quot;: &quot;string&quot;
},
&quot;capital&quot;: {
&quot;type&quot;: &quot;string&quot;
},
&quot;languages&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: {
&quot;type&quot;: &quot;string&quot;
}
}
},
&quot;required&quot;: [
&quot;name&quot;,
&quot;capital&quot;,
&quot;languages&quot;
]
}
}
}`;</p>
<p>&quot;response&quot;: {
&quot;name&quot;: &quot;India&quot;,
&quot;capital&quot;: &quot;New Delhi&quot;,
&quot;languages&quot;: [
&quot;Hindi&quot;,
&quot;English&quot;,
&quot;Bengali&quot;,
&quot;Telugu&quot;,
&quot;Marathi&quot;,
&quot;Tamil&quot;,
&quot;Gujarati&quot;,
&quot;Urdu&quot;,
&quot;Kannada&quot;,
&quot;Odia&quot;,
&quot;Malayalam&quot;,
&quot;Punjabi&quot;,
&quot;Sanskrit&quot;
]
}
}`;</p>
<p>When we want text-generation AI models to interact with databases, services, and external systems programmatically, typically when using tool calling or building AI agents, we must have structured response formats rather than natural language.</p>
<p>Workers AI supports JSON Mode, enabling applications to request a structured output response when interacting with AI models.</p>
<h2 id="schema">Schema</h2>
<p>JSON Mode is compatible with OpenAI’s implementation; to enable add the <code>response_format</code> property to the request object using the following convention:</p>
<pre><code class="language-json">{&#10;  response_format: {&#10;    title: &quot;JSON Mode&quot;,&#10;    type: &quot;object&quot;,&#10;    properties: {&#10;      type: {&#10;        type: &quot;string&quot;,&#10;        enum: [&quot;json_object&quot;, &quot;json_schema&quot;],&#10;      },&#10;      json_schema: {},&#10;    }&#10;  }&#10;}</code></pre>
<p>Where <code>json_schema</code> must be a valid <a href="https://json-schema.org/">JSON Schema</a> declaration.</p>
<h2 id="json-mode-example">JSON Mode example</h2>
<p>When using JSON Format, pass the schema as in the example below as part of the request you send to the LLM.</p>
<pre><code class="language-json">{&#10;  &quot;messages&quot;: [&#10;    {&#10;      &quot;role&quot;: &quot;system&quot;,&#10;      &quot;content&quot;: &quot;Extract data about a country.&quot;&#10;    },&#10;    {&#10;      &quot;role&quot;: &quot;user&quot;,&#10;      &quot;content&quot;: &quot;Tell me about India.&quot;&#10;    }&#10;  ],&#10;  &quot;response_format&quot;: {&#10;    &quot;type&quot;: &quot;json_schema&quot;,&#10;    &quot;json_schema&quot;: {&#10;      &quot;type&quot;: &quot;object&quot;,&#10;      &quot;properties&quot;: {&#10;        &quot;name&quot;: {&#10;          &quot;type&quot;: &quot;string&quot;&#10;        },&#10;        &quot;capital&quot;: {&#10;          &quot;type&quot;: &quot;string&quot;&#10;        },&#10;        &quot;languages&quot;: {&#10;          &quot;type&quot;: &quot;array&quot;,&#10;          &quot;items&quot;: {&#10;            &quot;type&quot;: &quot;string&quot;&#10;          }&#10;        }&#10;      },&#10;      &quot;required&quot;: [&#10;        &quot;name&quot;,&#10;        &quot;capital&quot;,&#10;        &quot;languages&quot;&#10;      ]&#10;    }&#10;  }&#10;}</code></pre>
<p>The LLM will follow the schema, and return a response such as below:</p>
<pre><code class="language-json">{&#10;  &quot;response&quot;: {&#10;    &quot;name&quot;: &quot;India&quot;,&#10;    &quot;capital&quot;: &quot;New Delhi&quot;,&#10;    &quot;languages&quot;: [&#10;      &quot;Hindi&quot;,&#10;      &quot;English&quot;,&#10;      &quot;Bengali&quot;,&#10;      &quot;Telugu&quot;,&#10;      &quot;Marathi&quot;,&#10;      &quot;Tamil&quot;,&#10;      &quot;Gujarati&quot;,&#10;      &quot;Urdu&quot;,&#10;      &quot;Kannada&quot;,&#10;      &quot;Odia&quot;,&#10;      &quot;Malayalam&quot;,&#10;      &quot;Punjabi&quot;,&#10;      &quot;Sanskrit&quot;&#10;    ]&#10;  }&#10;}</code></pre>
<p>As you can see, the model is complying with the JSON schema definition in the request and responding with a validated JSON object.</p>
<h2 id="supported-models">Supported Models</h2>
<p>This is the list of models that now support JSON Mode:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/">@cf/meta/llama-3.3-70b-instruct-fp8-fast</a></li>
<li><a href="/workers-ai/models/llama-3-8b-instruct/">@cf/meta/llama-3-8b-instruct</a></li>
<li><a href="/workers-ai/models/llama-3.1-8b-instruct/">@cf/meta/llama-3.1-8b-instruct</a></li>
<li><a href="/workers-ai/models/hermes-2-pro-mistral-7b/">@hf/nousresearch/hermes-2-pro-mistral-7b</a></li>
<li><a href="/workers-ai/models/deepseek-coder-6.7b-instruct-awq/">@hf/thebloke/deepseek-coder-6.7b-instruct-awq</a></li>
<li><a href="/workers-ai/models/deepseek-r1-distill-qwen-32b/">@cf/deepseek-ai/deepseek-r1-distill-qwen-32b</a></li>
</ul>
<p>We will continue extending this list to keep up with new, and requested models.</p>
<p>Note that Workers AI can't guarantee that the model responds according to the requested JSON Schema. Depending on the complexity of the task and adequacy of the JSON Schema, the model may not be able to satisfy the request in extreme situations. If that's the case, then an error <code>JSON Mode couldn't be met</code> is returned and must be handled.</p>
<p>JSON Mode currently doesn't support streaming.</p>
