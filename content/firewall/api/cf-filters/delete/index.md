<h2 id="delete-multiple-filters">Delete multiple filters</h2>
<p>This example deletes filters with IDs <code>{filter_id_1}</code> and <code>{filter_id_2}</code>.</p>
<pre><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/filters?id={filter_id_1}&amp;id={filter_id_2}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;&lt;FILTER_ID_1&gt;&quot;&#10;    },&#10;    {&#10;      &quot;id&quot;: &quot;&lt;FILTER_ID_2&gt;&quot;&#10;    }&#10;  ],&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="delete-a-single-filter">Delete a single filter</h2>
<p>This example deletes a single filter with ID <code>{filter_id}</code>.</p>
<pre><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/filters/{filter_id}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;&lt;FILTER_ID&gt;&quot;&#10;    }&#10;  ],&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
