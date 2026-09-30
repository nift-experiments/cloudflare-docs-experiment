<h2 id="bulk-redirect-rule">Bulk Redirect Rule</h2>
<p>A fully populated Bulk Redirect Rule object has the following JSON structure:</p>
<pre><code class="language-json">{&#10;	&quot;action&quot;: &quot;redirect&quot;,&#10;	&quot;expression&quot;: &quot;http.request.full_uri in $&lt;LIST_NAME&gt;&quot;,&#10;	&quot;action_parameters&quot;: {&#10;		&quot;from_list&quot;: {&#10;			&quot;name&quot;: &quot;&lt;LIST_NAME&gt;&quot;,&#10;			&quot;key&quot;: &quot;http.request.full_uri&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The JSON object properties must comply with the following:</p>
<ul>
<li>
<p><code>action</code> must be <code>redirect</code></p>
</li>
<li>
<p><code>action_parameters</code> must contain a <code>from_list</code> object with additional settings.</p>
</li>
<li>
<p><code>from_list</code> must contain the following properties:</p>
<ul>
<li><code>name</code>: The name of an existing Bulk Redirect List to associate with the current Bulk Redirect Rule.</li>
<li><code>key</code>: An expression that defines the value that will be matched against the configured URL redirect's source URL values, following the rules of the <a href="/rules/url-forwarding/bulk-redirects/how-it-works/#url-matching-algorithm">URL matching algorithm</a>. Refer to <a href="/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-rules">Bulk Redirects concepts</a> for more information.</li>
</ul>
</li>
<li>
<p><code>expression</code> must reference the request field used in the <code>key</code> property. Refer to <a href="/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-rules">Bulk Redirects concepts</a> for more information.</p>
</li>
</ul>
<h2 id="url-redirect-list-item">URL redirect list item</h2>
<p>A fully populated URL redirect list item object has the following JSON structure:</p>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;7c5dae5552338874e5053f2534d2767a&quot;,&#10;	&quot;redirect&quot;: {&#10;		&quot;source_url&quot;: &quot;https://example.com/blog&quot;,&#10;		&quot;target_url&quot;: &quot;https://example.com/blog/latest&quot;,&#10;		&quot;status_code&quot;: 301,&#10;		&quot;include_subdomains&quot;: false,&#10;		&quot;subpath_matching&quot;: false,&#10;		&quot;preserve_query_string&quot;: false,&#10;		&quot;preserve_path_suffix&quot;: true&#10;	},&#10;	&quot;created_on&quot;: &quot;2021-10-11T12:39:02Z&quot;,&#10;	&quot;modified_on&quot;: &quot;2021-10-11T12:39:02Z&quot;&#10;}&#10;</code></pre>
<p>For details on the <code>redirect</code> object properties, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/parameters/">URL redirect parameters</a>.</p>
