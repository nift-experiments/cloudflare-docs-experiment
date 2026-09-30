<p>The following table represents the comparison operators that are supported and example values. Filters are added as escaped JSON strings formatted as <code>{&quot;key&quot;:&quot;&lt;field&gt;&quot;,&quot;operator&quot;:&quot;&lt;comparison_operator&gt;&quot;,&quot;value&quot;:&quot;&lt;value&gt;&quot;}</code>.</p>
<ul>
<li>
<p>Refer to the <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> page for a list of fields related to each dataset.</p>
</li>
<li>
<p>Comparison operators define how values must relate to fields in the log line for an expression to return true.</p>
</li>
<li>
<p>Values represent the data associated with fields.</p>
</li>
</ul>
<table>
<thead>
<tr>
<th>Name</th>
<th>Operator Notation</th>
<th>String</th>
<th>Int</th>
<th>Bool</th>
<th>Array</th>
<th>Object</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Equal</td>
<td><code>eq</code></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientRequestHost&quot;,&quot;operator&quot;:&quot;eq&quot;,&quot;value&quot;:&quot;example.com&quot;}</code></td>
</tr>
<tr>
<td>Not equal</td>
<td><code>!eq</code></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientCountry&quot;,&quot;operator&quot;:&quot;!eq&quot;,&quot;value&quot;:&quot;ca&quot;}</code></td>
</tr>
<tr>
<td>Less than</td>
<td><code>lt</code></td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;BotScore&quot;,&quot;operator&quot;:&quot;lt&quot;,&quot;value&quot;:&quot;30&quot;}</code></td>
</tr>
<tr>
<td>Less than or equal</td>
<td><code>leq</code></td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;BotScore&quot;,&quot;operator&quot;:&quot;leq&quot;,&quot;value&quot;:&quot;30&quot;}</code></td>
</tr>
<tr>
<td>Greater than</td>
<td><code>gt</code></td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;BotScore&quot;,&quot;operator&quot;:&quot;gt&quot;,&quot;value&quot;:&quot;30&quot;}</code></td>
</tr>
<tr>
<td>Greater than or equal</td>
<td><code>geq</code></td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;BotScore&quot;,&quot;operator&quot;:&quot;geq&quot;,&quot;value&quot;:&quot;30&quot;}</code></td>
</tr>
<tr>
<td>Starts with</td>
<td><code>startsWith</code></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientRequestPath&quot;,&quot;operator&quot;:&quot;startsWith&quot;,&quot;value&quot;:&quot;/foo&quot;}</code></td>
</tr>
<tr>
<td>Ends with</td>
<td><code>endsWith</code></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientRequestPath&quot;,&quot;operator&quot;:&quot;endsWith&quot;,&quot;value&quot;:&quot;/foo&quot;}</code></td>
</tr>
<tr>
<td>Does not start with</td>
<td><code>!startsWith</code></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientRequestPath&quot;,&quot;operator&quot;:&quot;!startsWith&quot;,&quot;value&quot;:&quot;/foo&quot;}</code></td>
</tr>
<tr>
<td>Does not end with</td>
<td><code>!endsWith</code></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientRequestPath&quot;,&quot;operator&quot;:&quot;!endsWith&quot;,&quot;value&quot;:&quot;/foo&quot;}</code></td>
</tr>
<tr>
<td>Contains</td>
<td><code>contains</code></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientRequestPath&quot;,&quot;operator&quot;:&quot;contains&quot;,&quot;value&quot;:&quot;/static&quot;}</code></td>
</tr>
<tr>
<td>Does not contain</td>
<td><code>!contains</code></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;ClientRequestPath&quot;,&quot;operator&quot;:&quot;!contains&quot;,&quot;value&quot;:&quot;/static&quot;}</code></td>
</tr>
<tr>
<td>Value is in a set of values</td>
<td><code>in</code></td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;EdgeResponseStatus&quot;,&quot;operator&quot;:&quot;in&quot;,&quot;value&quot;:[200,201]}</code></td>
</tr>
<tr>
<td>Value is not in a set of values</td>
<td><code>!in</code></td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>{&quot;key&quot;:&quot;EdgeResponseStatus&quot;,&quot;operator&quot;:&quot;!in&quot;,&quot;value&quot;:[200,201]}</code></td>
</tr>
</tbody>
</table>
<p>The filter field has limits of approximately 30 operators and 1000 bytes. Anything exceeding this value will return an error.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10521.md")
</aside>
<h2 id="logical-operators">Logical Operators</h2>
<ul>
<li>
<p>Filters can be connected using <code>AND</code>, <code>OR</code> logical operators.</p>
</li>
<li>
<p>Logical operators can be nested.</p>
</li>
</ul>
<p>Here are some examples of how the logical operators can be implemented. <code>X</code>, <code>Y</code> and <code>Z</code> are used to represent filter criteria:</p>
<ul>
<li>
<p>X AND Y AND Z - <code>{&quot;where&quot;:{&quot;and&quot;:[{X},{Y},{Z}]}}</code></p>
</li>
<li>
<p>X OR Y OR Z - <code>{&quot;where&quot;:{&quot;or&quot;:[{X},{Y},{Z}]}}</code></p>
</li>
<li>
<p>X AND (Y OR Z) - <code>{&quot;where&quot;:{&quot;and&quot;:[{X}, {&quot;or&quot;:[{Y},{Z}]}]}}</code></p>
</li>
<li>
<p>(X AND Y) OR Z - <code>{&quot;where&quot;:{&quot;or&quot;:[{&quot;and&quot;: [{X},{Y}]},{Z}]}}</code></p>
</li>
</ul>
<p>Logpush filters act as a pass-through gate, not an exclusion list. When multiple conditions are joined with AND:</p>
<ul>
<li>All conditions must evaluate to TRUE for the log to be pushed.</li>
<li>If any single condition is FALSE, the log is excluded.</li>
</ul>
<p>A common misconception is interpreting the filter as <code>exclude logs matching ALL conditions</code> rather than <code>include logs matching ALL conditions</code>.</p>
<h2 id="set-filters-via-api-or-dashboard">Set filters via API or dashboard</h2>
<p>Filters can be set via API or the Cloudflare dashboard. Note that using a filter is optional, but if used, it must contain the <code>where</code> key.</p>
<h3 id="api">API</h3>
<p>Here is an example request using cURL via API:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;		name: &quot;static-assets&quot;,&#10;		output_options: {&#10;			field_names: [&quot;ClientIP&quot;, &quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;			sample_rate: 0.1,&#10;			timestamp_format: &quot;rfc3339&quot;,&#10;			&quot;CVE-2021-44228&quot;: true,&#10;		},&#10;		dataset: &quot;http_requests&quot;,&#10;		filter: JSON.stringify({&#10;			where: {&#10;				and: [&#10;					{ key: &quot;ClientRequestPath&quot;, operator: &quot;contains&quot;, value: &quot;/static&quot; },&#10;					{ key: &quot;ClientRequestHost&quot;, operator: &quot;eq&quot;, value: &quot;example.com&quot; },&#10;				],&#10;			},&#10;		}),&#10;		destination_conf: &quot;s3://&lt;BUCKET_PATH&gt;?region=us-west-2/&quot;,&#10;	}&#x27;</code></pre>
<h3 id="dashboard">Dashboard</h3>
<p>To set filters through the dashboard:</p>
<ol>
<li>
<p>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page at the account or domain (also known as zone) level.</p>
<p>For account: <div class="nb-dash-button"></div></p>
<p>For domain (also known as zone): <div class="nb-dash-button"></div></p>
</li>
<li>
<p>Select the dataset you want to push to a storage service. Depending on your choice, you have access to <a href="/logs/logpush/logpush-job/datasets/account/">account-scoped datasets</a> and <a href="/logs/logpush/logpush-job/datasets/zone/">zone-scoped datasets</a>, respectively.</p>
</li>
<li>
<p>Below <strong>Select data fields</strong>, in the <strong>Filter</strong> section, you can set up your filters.</p>
</li>
<li>
<p>You need to select a <a href="/logs/logpush/logpush-job/datasets/">dataset field</a>, an <a href="/logs/logpush/logpush-job/filters/#logical-operators">Operator</a>, and a <strong>Value</strong>.</p>
</li>
<li>
<p>You can connect more filters using <code>AND</code> and <code>OR</code> logical operators.</p>
</li>
<li>
<p>Select <strong>Next</strong> to continue the setting up of your Logpush job.</p>
</li>
</ol>
