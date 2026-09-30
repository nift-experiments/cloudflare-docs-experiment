<p>A <a href="/ai-search/concepts/namespaces/">namespace</a> can expose its own public endpoint. A single URL then searches across several instances in that namespace and merges the results. Use one when a single search experience covers content that lives in several instances, such as documentation, a blog, and a support portal.</p>
<p>A namespace endpoint serves the same paths and takes the same settings as an instance endpoint, including <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domains</a> and <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a>. Refer to <a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint settings</a>. This page covers what is specific to namespaces.</p>
<h2 id="enable-a-namespace-public-endpoint">Enable a namespace public endpoint</h2>
<p>Set <code>public_endpoint_params</code> on the namespace and list the instances to expose in <code>instances_allowed</code>.</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/&lt;NAMESPACE&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;public_endpoint_params&quot;: {&#10;      &quot;enabled&quot;: true,&#10;      &quot;instances_allowed&quot;: [&quot;docs&quot;, &quot;blog&quot;, &quot;support&quot;]&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>The response returns the generated <code>public_endpoint_id</code>. A namespace hostname is prefixed with <code>ns-</code>:</p>
<pre><code class="language-txt">https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search&#10;</code></pre>
<p>Enabling a namespace endpoint does not change the instance endpoints inside it. Each is enabled and disabled separately.</p>
<h2 id="the-instances-allowlist">The instances allowlist</h2>
<p><code>instances_allowed</code> controls which instances the endpoint can reach.</p>
<ul>
<li>Every entry must be an existing instance in that namespace. An unknown entry returns error <code>7097</code>.</li>
<li>The list holds up to 10 instances.</li>
<li>An empty list means nothing is searchable. This is the state a namespace starts in when you first enable the endpoint.</li>
<li>Deleting an instance, or moving it to another namespace, removes it from the allowlist.</li>
</ul>
<p>A request that resolves to no searchable instance returns a <code>404</code> with error <code>60013</code>. This response is identical whether the instance does not exist, is outside the allowlist, or the allowlist is empty, so callers cannot discover which instances a namespace contains.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3097.md")
</aside>
<h2 id="search-a-subset-of-instances">Search a subset of instances</h2>
<p>By default, a request searches every instance in the allowlist. To narrow a single request, set <code>ai_search_options.instance_ids</code> in the request body.</p>
<pre><code class="language-bash">curl https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I configure AI Search?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ],&#10;    &quot;ai_search_options&quot;: {&#10;      &quot;instance_ids&quot;: [&quot;docs&quot;, &quot;support&quot;]&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Every value must be in the allowlist. Rules for this field:</p>
<ul>
<li>Omitting the field, or setting it to <code>null</code>, searches the full allowlist.</li>
<li>A malformed value, such as an empty array or a non-string entry, returns a <code>400</code> with error <code>60012</code>.</li>
<li>A value outside the allowlist returns a <code>404</code> with error <code>60013</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3098.md")
</aside>
<h2 id="disable-a-namespace-public-endpoint">Disable a namespace public endpoint</h2>
<p>Set <code>public_endpoint_params</code> to <code>null</code>. This clears the configuration and stops serving traffic, but keeps the identifier so the URL is reused if you enable the endpoint again.</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/&lt;NAMESPACE&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;public_endpoint_params&quot;: null&#10;  }&#x27;&#10;</code></pre>
<h2 id="errors">Errors</h2>
<table>
<thead>
<tr>
<th>Code</th>
<th>Message</th>
<th>HTTP status</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7097</code></td>
<td><code>instances_allowed_contains_unknown_instances</code></td>
<td>400</td>
<td>An entry in <code>instances_allowed</code> is not an instance in this namespace.</td>
</tr>
<tr>
<td><code>7099</code></td>
<td><code>namespace_modified_concurrently_please_retry</code></td>
<td>409</td>
<td>Another update changed the namespace at the same time. Retry.</td>
</tr>
<tr>
<td><code>60012</code></td>
<td><code>invalid ai_search_options.instance_ids</code></td>
<td>400</td>
<td>The <code>instance_ids</code> value is malformed.</td>
</tr>
<tr>
<td><code>60013</code></td>
<td><code>ai_search_not_found</code></td>
<td>404</td>
<td>No searchable instance matched the request.</td>
</tr>
<tr>
<td><code>60014</code></td>
<td><code>path not supported for namespace-kind hash</code></td>
<td>404</td>
<td>The path is not <code>/search</code>, <code>/chat/completions</code>, or <code>/mcp</code>.</td>
</tr>
<tr>
<td><code>60015</code></td>
<td><code>request body must be a JSON object</code></td>
<td>400</td>
<td>The request body is not a JSON object.</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/concepts/namespaces/"><h3 id="card-namespaces-ai-search-concepts-namespaces">Namespaces</h3><p>Group instances into namespaces and manage them from a Workers binding.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/how-to/search-multiple-sources/"><h3 id="card-search-across-multiple-instances-ai-search-how-to-search-multiple-sources">Search across multiple instances</h3><p>Query several instances from a Worker or the REST API.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/"><h3 id="card-custom-domains-ai-search-configuration-retrieval-public-endpoint-custom-domains">Custom domains</h3><p>Serve a namespace public endpoint from a hostname that you own.</p></a></p>
