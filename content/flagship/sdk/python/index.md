<p>The Python SDK provides an OpenFeature-compatible <code>FlagshipServerProvider</code> for server-side Python applications. It evaluates flags over HTTP and does not support the Cloudflare Workers binding.</p>
<h2 id="installation">Installation</h2>
<p>Install with <code>uv</code> or <code>pip</code>:</p>
<pre><code class="language-sh">uv add cloudflare-flagship&#10;</code></pre>
<pre><code class="language-sh">pip install cloudflare-flagship&#10;</code></pre>
<h2 id="setup">Setup</h2>
<p>Configure the provider with your Flagship app ID, Cloudflare account ID, and an <a href="/flagship/api-tokens/">API token</a> with Flagship Evaluate or Flagship App Evaluate permission.</p>
<pre><code class="language-python">from openfeature import api&#10;from openfeature.evaluation_context import EvaluationContext&#10;from flagship import FlagshipServerProvider&#10;&#10;api.set_provider(&#10;    FlagshipServerProvider(&#10;        app_id=&quot;&lt;APP_ID&gt;&quot;,&#10;        account_id=&quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;        auth_token=&quot;&lt;API_TOKEN&gt;&quot;,&#10;    )&#10;)&#10;&#10;client = api.get_client()&#10;enabled = client.get_boolean_value(&#10;    &quot;new-checkout&quot;,&#10;    False,&#10;    EvaluationContext(targeting_key=&quot;user-42&quot;, attributes={&quot;plan&quot;: &quot;enterprise&quot;}),&#10;)&#10;</code></pre>
<h2 id="flag-types">Flag types</h2>
<p>The Python SDK supports all OpenFeature flag types. Python's OpenFeature SDK separates numeric values into integer and float methods.</p>
<pre><code class="language-python">enabled = client.get_boolean_value(&quot;new-checkout&quot;, False, context)&#10;variant = client.get_string_value(&quot;homepage-hero&quot;, &quot;control&quot;, context)&#10;limit = client.get_integer_value(&quot;upload-limit&quot;, 10, context)&#10;rate = client.get_float_value(&quot;sample-rate&quot;, 0.1, context)&#10;config = client.get_object_value(&quot;ui-config&quot;, {&quot;theme&quot;: &quot;light&quot;}, context)&#10;</code></pre>
<p>Use the <code>*_details</code> methods when you need the resolved value, reason, variant, or error code.</p>
<h2 id="configuration-options">Configuration options</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>app_id</code></td>
<td><code>str</code></td>
<td>None</td>
<td>Flagship app ID.</td>
</tr>
<tr>
<td><code>account_id</code></td>
<td><code>str</code></td>
<td>None</td>
<td>Required with <code>app_id</code>.</td>
</tr>
<tr>
<td><code>auth_token</code></td>
<td><code>str</code></td>
<td>None</td>
<td>Bearer token added to every request.</td>
</tr>
<tr>
<td><code>headers_factory</code></td>
<td><code>Callable[[], dict[str, str]]</code></td>
<td>None</td>
<td>Dynamic per-request headers.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>float</code></td>
<td><code>5.0</code></td>
<td>Request timeout in seconds.</td>
</tr>
<tr>
<td><code>retries</code></td>
<td><code>int</code></td>
<td><code>1</code></td>
<td>Retry attempts on transient errors, capped at <code>10</code>.</td>
</tr>
<tr>
<td><code>retry_delay</code></td>
<td><code>float</code></td>
<td><code>1.0</code></td>
<td>Delay between retries in seconds, capped at <code>30.0</code>.</td>
</tr>
<tr>
<td><code>logging</code></td>
<td><code>bool</code></td>
<td><code>False</code></td>
<td>Enable SDK-level debug output through the SDK logger.</td>
</tr>
<tr>
<td><code>cache_ttl</code></td>
<td><code>float</code></td>
<td>None</td>
<td>Cache TTL in seconds. Enables caching when set.</td>
</tr>
<tr>
<td><code>cache_max_size</code></td>
<td><code>int</code></td>
<td><code>1000</code></td>
<td>Maximum cached entries before least-recently-used eviction.</td>
</tr>
</tbody>
</table>
<h2 id="response-caching">Response caching</h2>
<p>Server-side response caching is off by default. Enable it with <code>cache_ttl</code> when you want repeated evaluations for the same flag, type, and evaluation context to reuse a recent result.</p>
<pre><code class="language-python">FlagshipServerProvider(&#10;    app_id=&quot;&lt;APP_ID&gt;&quot;,&#10;    account_id=&quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;    auth_token=&quot;&lt;API_TOKEN&gt;&quot;,&#10;    cache_ttl=30.0,&#10;    cache_max_size=1000,&#10;)&#10;</code></pre>
<p>Cached values may be stale until the TTL expires. Keep the TTL short for flags that you expect to change during active rollouts. The provider does not cache disabled flags or errors.</p>
<h2 id="evaluation-context">Evaluation context</h2>
<p>Context attributes are sent as URL query parameters. Supported values are strings, integers, floats, booleans, and <code>datetime</code> values. Dictionaries, lists, tuples, and other complex values raise <code>InvalidContextError</code>.</p>
<h2 id="async-evaluation">Async evaluation</h2>
<p>The async API mirrors the sync API:</p>
<pre><code class="language-python">enabled = await client.get_boolean_value_async(&quot;new-checkout&quot;, False, context)&#10;details = await client.get_boolean_details_async(&quot;new-checkout&quot;, False, context)&#10;</code></pre>
<p>When shutting down in an async context, use <code>shutdown_async()</code>:</p>
<pre><code class="language-python">await api.shutdown_async()&#10;</code></pre>
