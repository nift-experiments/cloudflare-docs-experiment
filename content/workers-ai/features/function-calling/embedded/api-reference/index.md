<p>Learn more about the API reference for <a href="/workers-ai/features/function-calling/embedded">embedded function calling</a>.</p>
<h2 id="runwithtools">runWithTools</h2>
<p>This wrapper method enables you to do embedded function calling. You pass it the AI binding, model, inputs (<code>messages</code> array and <code>tools</code> array), and optional configurations.</p>
<ul>
<li><code>AI Binding</code>Ai
<ul>
<li>The AI binding, such as <code>env.AI</code>.</li>
</ul>
</li>
<li><code>model</code>BaseAiTextGenerationModels
<ul>
<li>The ID of the model that supports function calling. For example, <code>@hf/nousresearch/hermes-2-pro-mistral-7b</code>.</li>
</ul>
</li>
<li><code>input</code>Object
<ul>
<li><code>messages</code>RoleScopedChatInput[]</li>
<li><code>tools</code>AiTextGenerationToolInputWithFunction[]</li>
</ul>
</li>
<li><code>config</code>Object
<ul>
<li><code>streamFinalResponse</code>boolean optional</li>
<li><code>maxRecursiveToolRuns</code>number optional</li>
<li><code>strictValidation</code>boolean optional</li>
<li><code>verbose</code>boolean optional</li>
<li><code>trimFunction</code>boolean optional - For the <code>trimFunction</code>, you can pass it <code>autoTrimTools</code>, which is another helper method we've devised to automatically choose the correct tools (using an LLM) before sending it off for inference. This means that your final inference call will have fewer input tokens.</li>
</ul>
</li>
</ul>
<h2 id="createtoolsfromopenapispec">createToolsFromOpenAPISpec</h2>
<p>This method lets you automatically create tool schemas based on OpenAPI specs, so you don't have to manually write or hardcode the tool schemas. You can pass the OpenAPI spec for any API in JSON or YAML format.</p>
<p><code>createToolsFromOpenAPISpec</code> has a config input that allows you to perform overrides if you need to provide headers like Authentication or User-Agent.</p>
<ul>
<li><code>spec</code>string
<ul>
<li>The OpenAPI specification in either JSON or YAML format, or a URL to a remote OpenAPI specification.</li>
</ul>
</li>
<li><code>config</code>Config optional - Configuration options for the createToolsFromOpenAPISpec function
<ul>
<li><code>overrides</code>ConfigRule[] optional</li>
<li><code>matchPatterns</code>RegExp[] optional</li>
<li><code>options</code> Object optional {
<code>verbose</code> boolean optional
}</li>
</ul>
</li>
</ul>
