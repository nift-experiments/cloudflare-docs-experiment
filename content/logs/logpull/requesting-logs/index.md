<h2 id="endpoints">Endpoints</h2>
<p>The three endpoints supported by the Logpull API are:</p>
<ul>
<li><code>GET /logs/received</code> - returns HTTP request log data based on the parameters specified</li>
<li><code>GET /logs/received/fields</code> - returns the list of all available log fields</li>
<li><code>GET /logs/rayids/{ray_id}</code> - returns HTTP request log data matching <code>{ray_id}</code></li>
</ul>
<h2 id="required-authentication-headers">Required authentication headers</h2>
<p>The following headers are required for all endpoint calls:</p>
<ul>
<li><code>X-Auth-Email</code> - the Cloudflare account email address associated with the domain</li>
<li><code>X-Auth-Key</code> - the Cloudflare API key</li>
</ul>
<p>Alternatively, API tokens with Logs Read permissions can also be used for authentication:</p>
<ul>
<li><code>Authorization: Bearer &lt;API_TOKEN&gt;</code></li>
</ul>
<h2 id="parameters">Parameters</h2>
<p>The API expects endpoint parameters in the GET request query string. The following are example formats:</p>
<p><code>logs/received</code></p>
<pre><code class="language-bash">https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/received?start=&lt;unix|rfc3339&gt;&amp;end=&lt;unix|rfc3339&gt;[&amp;count=&lt;int&gt;][&amp;sample=&lt;float&gt;][&amp;fields=&lt;FIELDS&gt;][&amp;timestamps=&lt;string&gt;][&amp;CVE-2021-44228=&lt;boolean&gt;]&#10;</code></pre>
<p><code>logs/rayids/{ray_id}</code></p>
<pre><code class="language-bash">https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/rayids/{ray_id}?[&amp;fields=&lt;FIELDS&gt;][&amp;timestamps=&lt;string&gt;]&#10;</code></pre>
<p>The following table describes the parameters available:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Applies to</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td>start</td>
<td><p>- Inclusive</p> <p>- Timestamp formatted as <code>UNIX</code> (UTC by definition), <code>UNIX Nano</code>, or <code>rfc3339</code>. To specify <code>rfc3339</code> time zone in URL query parameters, the URL needs to be encoded, like this <code>start=2024-08-07T07:00:00%2B08:00&amp;end=2024-08-07T07:01:00%2B08:00</code>. </p> <p>- Must be no more than 7 days earlier than now</p></td>
<td>/logs/received</td>
<td>Yes</td>
</tr>
<tr>
<td>end</td>
<td><p>- Exclusive</p> <p>- Same format as <em>start</em></p> <p>- Must be at least 1 minute earlier than now and later than <em>start</em></p></td>
<td>/logs/received</td>
<td>Yes</td>
</tr>
<tr>
<td>count</td>
<td><p>- Return up to that many records</p> <p>- Do not include if returning all records</p> <p>- Results are not sorted; therefore, different data for repeated requests is likely</p> <p></p> <p>- Applies to number of total records returned, not number of sampled records</p></td>
<td>/logs/received</td>
<td>No</td>
</tr>
<tr>
<td>sample</td>
<td><p>- Return only a sample of records</p> <p>- Do not include if returning all records</p> <p>- Value can range from <code>0.0</code> (exclusive) to <code>1.0</code> (inclusive)</p> <p>- <code>sample=0.1</code> means return 10% (1 in 10) of all records</p> <p>- Results are random; therefore, different numbers of results for repeated requests are likely</p></td>
<td>/logs/received</td>
<td>No</td>
</tr>
<tr>
<td>fields</td>
<td><p>- Comma-separated list of fields to return</p> <p>- If empty, the default list is returned</p></td>
<td><p>/logs/received</p> <p>/logs/rayids</p></td>
<td>No</td>
</tr>
<tr>
<td>timestamps</td>
<td><p>- Format in which timestamp fields will be returned</p> <p>- Value options are: <code>unixnano</code> (default), <code>unix</code>, <code>rfc3339</code></p> <p>- Timestamps returned as integers for <code>unix</code> and <code>unixnano</code> and as strings for <code>rfc3339</code></p></td>
<td><p>/logs/received</p> <p>/logs/rayids</p></td>
<td>No</td>
</tr>
<tr>
<td>CVE-2021-44228</td>
<td><p>- Optional redaction for <a href="https://www.cve.org/CVERecord?id=CVE-2021-44228">CVE-2021-44228</a>. This option will replace every occurrence of the string <code>${</code> with <code>x{</code>.</p> <p> For example: <code>CVE-2021-44228=true</code> </p></td>
<td><p>/logs/received</p></td>
<td>No</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10478.md")
</aside>
<h2 id="example-api-requests-using-curl">Example API requests using cURL</h2>
<p><code>logs/received</code></p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/received?start=2017-07-18T22:00:00Z&amp;end=2017-07-18T22:01:00Z&amp;count=1&amp;fields=ClientIP,ClientRequestHost,ClientRequestMethod,ClientRequestURI,EdgeEndTimestamp,EdgeResponseBytes,EdgeResponseStatus,EdgeStartTimestamp,RayID&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p><code>logs/rayids/{ray_id}</code></p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/rayids/{ray_id}}?timestamps=rfc3339&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/10477.md")
</aside>
<h2 id="fields">Fields</h2>
<p>Unless specified in the <strong>fields</strong> parameter, the API returns a limited set of log fields. This default field set may change at any time. The list of all available fields is at:</p>
<p><code>https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/received/fields</code></p>
<p>The order in which fields are specified does not matter, and the order of fields in the response is not specified.</p>
<p>Using bash subshell and <code>jq</code>, you can download the logs with all available fields without manually copying and pasting the fields into the request. For example:</p>
<pre><code class="language-bash">FIELDS=$(curl https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/received/fields \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;| jq &#x27;. | to_entries[] | .key&#x27; -r | paste -sd &quot;,&quot; -)&#10;&#10;curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/received?start=2017-07-18T22:00:00Z&amp;end=2017-07-18T22:01:00Z&amp;count=1&amp;fields=$FIELDS&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>Refer to <a href="https://jqlang.github.io/jq/download/">Download jq</a> for more information on obtaining and installing <code>jq</code>.</p>
<p>Refer to <a href="/logs/logpush/logpush-job/datasets/zone/http_requests">HTTP request fields</a> for the currently available fields.</p>
