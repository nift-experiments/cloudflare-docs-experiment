<p>AI Gateway supports exporting traces to OpenTelemetry-compatible backends, enabling you to monitor and analyze AI request performance alongside your existing observability infrastructure.</p>
<h2 id="overview">Overview</h2>
<p>The OpenTelemetry (OTEL) integration automatically exports trace spans for AI requests processed through your gateway. These spans include detailed information about:</p>
<ul>
<li>Request model and provider</li>
<li>Token usage (input and output)</li>
<li>Request prompts and completions</li>
<li>Cost estimates</li>
<li>Custom metadata</li>
</ul>
<p>This integration follows the <a href="https://opentelemetry.io/docs/specs/otel/">OpenTelemetry specification</a> for distributed tracing and uses the OTLP (OpenTelemetry Protocol) format, supporting both JSON and protobuf encoding.</p>
<h2 id="configuration">Configuration</h2>
<p>To enable OpenTelemetry tracing for your gateway, configure one or more OTEL exporters in your gateway settings. Each exporter accepts:</p>
<ul>
<li><strong>URL</strong> (required): The endpoint URL of your OTEL collector</li>
<li><strong>Headers</strong> (optional): Additional custom headers to include in export requests. If your collector requires authentication, pass it here (for example, <code>Authorization: Bearer &lt;token&gt;</code>).</li>
<li><strong>Authorization</strong> (optional): A reference to a secret in <a href="/secrets-store/">Secrets Store</a> containing your collector's authorization header value. When set, AI Gateway resolves the secret at runtime and sends it as the <code>Authorization</code> header on export requests. For most use cases, passing authentication via <strong>Headers</strong> is simpler.</li>
<li><strong>Content type</strong> (optional): The export format — <code>json</code> (default) or <code>protobuf</code>.</li>
</ul>
<h3 id="configuration-via-dashboard">Configuration via Dashboard</h3>
<ol>
<li>Navigate to your AI Gateway in the Cloudflare dashboard.</li>
<li>Go to <strong>Settings</strong> tab.</li>
<li>Add an OTEL exporter with your collector endpoint URL.</li>
<li>If your collector requires authentication, add an <code>Authorization</code> header in the <strong>Headers</strong> field with your token value.</li>
</ol>
<h2 id="exported-span-attributes">Exported Span Attributes</h2>
<p>AI Gateway exports spans with the following attributes following the <a href="https://opentelemetry.io/docs/specs/semconv/gen-ai/">Semantic Conventions for Gen AI</a>:</p>
<h3 id="standard-attributes">Standard Attributes</h3>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gen_ai.request.model</code></td>
<td>string</td>
<td>The AI model used for the request</td>
</tr>
<tr>
<td><code>gen_ai.model.provider</code></td>
<td>string</td>
<td>The AI provider (e.g., <code>openai</code>, <code>anthropic</code>)</td>
</tr>
<tr>
<td><code>gen_ai.usage.input_tokens</code></td>
<td>int</td>
<td>Number of input tokens consumed</td>
</tr>
<tr>
<td><code>gen_ai.usage.output_tokens</code></td>
<td>int</td>
<td>Number of output tokens generated</td>
</tr>
<tr>
<td><code>gen_ai.prompt_json</code></td>
<td>string</td>
<td>JSON-encoded prompt/messages sent to the model</td>
</tr>
<tr>
<td><code>gen_ai.completion_json</code></td>
<td>string</td>
<td>JSON-encoded completion/response from the model</td>
</tr>
<tr>
<td><code>gen_ai.usage.cost</code></td>
<td>double</td>
<td>Estimated cost of the request</td>
</tr>
</tbody>
</table>
<h3 id="custom-metadata">Custom Metadata</h3>
<p>Any custom metadata added to your requests via the <code>cf-aig-metadata</code> header will also be included as span attributes. This allows you to correlate traces with user IDs, team names, or other business context.</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;-header &#x27;Authorization: Bearer {api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;cf-aig-metadata: {&quot;user_id&quot;: &quot;user123&quot;, &quot;team&quot;: &quot;engineering&quot;}&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;gpt-4o&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>The above request will include <code>user_id</code> and <code>team</code> as additional span attributes in the exported trace.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2799.md")
</aside>
<h2 id="trace-context-propagation">Trace Context Propagation</h2>
<p>AI Gateway supports trace context propagation, allowing you to link AI Gateway spans with your application's traces. You can provide trace context using custom headers:</p>
<ul>
<li><code>cf-aig-otel-trace-id</code> (optional): A 32-character hex string to use as the trace ID</li>
<li><code>cf-aig-otel-parent-span-id</code> (optional): A 16-character hex string to use as the parent span ID</li>
</ul>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;-header &#x27;cf-aig-otel-trace-id: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6&#x27; \&#10;  &#45;-header &#x27;cf-aig-otel-parent-span-id: a1b2c3d4e5f6g7h8&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;gpt-4o&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>When these headers are provided, the AI Gateway span will use them to link with your existing trace. If not provided, AI Gateway will generate a new trace ID automatically.</p>
<h2 id="common-otel-backends">Common OTEL Backends</h2>
<p>AI Gateway's OTEL integration works with any OpenTelemetry-compatible backend, including:</p>
<ul>
<li><a href="https://www.honeycomb.io/">Honeycomb</a></li>
<li><a href="https://www.braintrust.dev/docs/integrations/sdk-integrations/opentelemetry">Braintrust</a></li>
<li><a href="https://langfuse.com/integrations/native/opentelemetry">Langfuse</a></li>
<li><a href="https://docs.datadoghq.com/opentelemetry/setup/agentless/">Datadog</a></li>
<li><a href="https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-otlp/">New Relic</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2798.md")
</aside>
<p>Refer to your observability platform's documentation for the correct OTLP endpoint URL and authentication requirements.</p>
