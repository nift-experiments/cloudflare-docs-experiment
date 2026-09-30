<p>The HTTP requests dataset includes most standard log information by default. However, if you need to capture additional request or response headers or cookies, you can use custom fields to tailor the logs to your specific needs</p>
<p>Custom fields are configured per zone and, once set up, are enabled for all Logpush jobs in that zone that use the HTTP requests dataset and include the request headers, response headers, or cookie fields. You can log these fields in their raw form or as transformed values.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="by-default">By default:</h3>
@markup("md", "content/.markup/bodies/10525.md")
</aside>
<p>This default behavior can be changed. You can configure either request or response headers to be logged as raw or transformed, depending on your needs - but not both for the same header.</p>
<p>Custom fields can be enabled via API or the Cloudflare dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10524.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10523.md")
</aside>
<h2 id="enable-custom-rules-via-api">Enable custom rules via API</h2>
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a rule that configures custom fields. For more information on concepts like phases, rulesets, and rules, as well as the available API operations, refer to the <a href="/ruleset-engine/">Ruleset Engine</a> documentation.</p>
<p>To configure custom fields:</p>
<ol>
<li>Create a rule to configure the list of custom fields.</li>
<li>Include the <code>Cookies</code>, <code>RequestHeaders</code>, and/or <code>ResponseHeaders</code> fields in your Logpush job.</li>
</ol>
<h3 id="1-create-a-rule-to-configure-the-list-of-custom-fields"><ol>
<li>Create a rule to configure the list of custom fields</li>
</ol></h3>
<p>Create a rule configuring the list of custom fields in the <code>http_log_custom_fields</code> phase at the zone level. Set the rule action to <code>log_custom_field</code> and the rule expression to <code>true</code>.</p>
<p>The <code>action_parameters</code> object that you must include in the rule that configures the list of custom fields should have the following structure:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;//select raw (default) or transformed request header&#10;  &quot;request_fields&quot;: [&#10;    { &quot;name&quot;: &quot;&lt;http_request_header_raw&gt;&quot; }&#10;  ],&#10;  &quot;transformed_request_fields&quot;: [&#10;    { &quot;name&quot;: &quot;&lt;http_request_header_transformed&gt;&quot; }&#10;  ],&#10;//select raw or transformed (default) response header&#10;  &quot;response_fields&quot;: [&#10;    { &quot;name&quot;: &quot;&lt;http_response_header_transformed&gt;&quot; }&#10;  ],&#10;  &quot;raw_response_fields&quot;: [&#10;    { &quot;name&quot;: &quot;&lt;http_response_header_raw&gt;&quot; }&#10;  ],&#10;  &quot;cookie_fields&quot;: [&#10;    { &quot;name&quot;: &quot;&lt;cookie_name&gt;&quot; }&#10;  ]&#10;}&#10;</code></pre>
<p>Ensure that your rule definition complies with the following:</p>
<ul>
<li>You must include at least one of the following arrays in the <code>action_parameters</code> object: <code>request_fields</code>, <code>transformed_request_fields</code>, <code>response_fields</code>, <code>raw_response_fields</code>, and <code>cookie_fields</code>.</li>
<li>You must enter HTTP request and response header names in lower case.</li>
<li>Cookie names are case sensitive — you must enter cookie names with the same capitalization they have in the HTTP request.</li>
<li>You must set the rule expression to <code>true</code>.</li>
<li>You can only log raw or transformed values for either request or response headers but not both for the same header.</li>
</ul>
<p>Perform the following steps to create the rule:</p>
<ol>
<li>Use the <a href="/ruleset-engine/rulesets-api/view/#list-existing-rulesets">List zone rulesets</a> operation to check if there is already an <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> for the <code>http_log_custom_fields</code> phase at the zone level (you can only have one entry point ruleset per phase):</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>If there is an entry point ruleset for the <code>http_log_custom_fields</code> phase (that is, a ruleset with <code>&quot;kind&quot;: &quot;zone&quot;</code> and <code>&quot;phase&quot;: &quot;http_log_custom_fields&quot;</code>), take note of the ruleset ID.</p>
<ol start="2">
<li>(Optional) If the response did not include a ruleset with <code>&quot;kind&quot;: &quot;zone&quot;</code> and <code>&quot;phase&quot;: &quot;http_log_custom_fields&quot;</code>, create the phase entry point ruleset using the <a href="/ruleset-engine/rulesets-api/create/">Create a zone ruleset</a> operation:</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;  &quot;kind&quot;: &quot;zone&quot;,&#10;  &quot;description&quot;: &quot;This ruleset configures custom log fields.&quot;,&#10;  &quot;phase&quot;: &quot;http_log_custom_fields&quot;&#10;}&#x27;</code></pre>
<p>Take note of the ruleset ID included in the response.</p>
<ol start="3">
<li>
<p>Use the <a href="/ruleset-engine/rulesets-api/update/">Update a zone ruleset</a> operation to define the rules of the entry point ruleset you found (or created in the previous step), adding a rule with the custom fields configuration. The rules you include in the request will replace all the rules in the ruleset.</p>
<p>The following example configures custom fields with the names of the HTTP request headers, HTTP response headers, and cookies you wish to include in Logpush logs:</p>
</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;log_custom_field&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Set Logpush custom fields for HTTP requests&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;request_fields&quot;: [&#10;          {&#10;            &quot;name&quot;: &quot;content-type&quot;&#10;          },&#10;          {&#10;            &quot;name&quot;: &quot;x-forwarded-for&quot;&#10;          }&#10;        ],&#10;        &quot;transformed_request_fields&quot;: [&#10;          {&#10;            &quot;name&quot;: &quot;host&quot;&#10;          }&#10;        ],&#10;        &quot;response_fields&quot;: [&#10;          {&#10;            &quot;name&quot;: &quot;server&quot;&#10;          },&#10;          {&#10;            &quot;name&quot;: &quot;content-type&quot;&#10;          }&#10;        ],&#10;        &quot;raw_response_fields&quot;: [&#10;          {&#10;            &quot;name&quot;: &quot;allow&quot;&#10;          }&#10;        ],&#10;        &quot;cookie_fields&quot;: [&#10;          {&#10;            &quot;name&quot;: &quot;__ga&quot;&#10;          },&#10;          {&#10;            &quot;name&quot;: &quot;accountNumber&quot;&#10;          },&#10;          {&#10;            &quot;name&quot;: &quot;__cfruid&quot;&#10;          }&#10;        ]&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;description&quot;: &quot;This ruleset configures custom log fields.&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;2&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;log_custom_field&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;request_fields&quot;: [&#10;						{ &quot;name&quot;: &quot;content-type&quot; },&#10;						{ &quot;name&quot;: &quot;x-forwarded-for&quot; }&#10;					],&#10;					&quot;transformed_request_fields&quot;: [{ &quot;name&quot;: &quot;host&quot; }],&#10;					&quot;response_fields&quot;: [&#10;						{ &quot;name&quot;: &quot;server&quot; },&#10;						{ &quot;name&quot;: &quot;content-type&quot; }&#10;					],&#10;					&quot;raw_response_fields&quot;: [{ &quot;name&quot;: &quot;allow&quot; }],&#10;					&quot;cookie_fields&quot;: [&#10;						{ &quot;name&quot;: &quot;__ga&quot; },&#10;						{ &quot;name&quot;: &quot;accountNumber&quot; },&#10;						{ &quot;name&quot;: &quot;__cfruid&quot; }&#10;					]&#10;				},&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;Set Logpush custom fields for HTTP requests&quot;,&#10;				&quot;last_updated&quot;: &quot;2021-11-21T11:02:08.769537Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_1&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2021-11-21T11:02:08.769537Z&quot;,&#10;		&quot;phase&quot;: &quot;http_log_custom_fields&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h4 id="record-duplicate-response-header-values">Record duplicate response header values</h4>
<p>Some headers sent from the origin — such as <code>set-cookie</code> — may have multiple values that you want to capture. You can use the Rulesets API to specify which headers should have all their values logged.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;log_custom_field&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Set Logpush custom fields for HTTP requests&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;response_fields&quot;: [&#10;          {&#10;            &quot;name&quot;: &quot;set-cookie&quot;,&#10;            &quot;preserve_duplicates&quot;: true&#10;          }&#10;        ]&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<p>Note that <code>preserve_duplicates</code> applies to both <code>response_fields</code> and <code>raw_response_fields</code>. If there are no transform rules that affect a header, including <code>preserve_duplicates</code> in either <code>response_fields</code> or <code>raw_response_fields</code> should achieve the same result.</p>
<p>In this example, all values of the <code>set-cookie</code> headers will be logged. They will appear as an array of string values under <code>ResponseFields</code>, for example:</p>
<pre><code class="language-json">{&#10;  // ...&#10;  &quot;ResponseFields&quot;: {&#10;    &quot;set-cookie&quot;: [&quot;name1=val1&quot;, &quot;name2=val2&quot;, ...]&#10;  }&#10;}&#10;</code></pre>
<p>You can use a worker or custom logic at your logpush destination to extract these values.</p>
<h3 id="2-include-the-custom-fields-in-your-logpush-job"><ol start="2">
<li>Include the custom fields in your Logpush job</li>
</ol></h3>
<p>Next, include <code>Cookies</code>, <code>RequestHeaders</code>, <code>ResponseHeaders</code>, and/or <code>ResponseFields</code>, depending on your custom field configuration, in the list of fields of the <code>output_options</code> job parameter when creating or updating a job. The logs will contain the configured custom fields and their values in the request/response.</p>
<p>For example, consider the following request that creates a job that includes custom fields:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;s3://&lt;BUCKET_PATH&gt;?region=us-west-2&quot;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;RayID&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;Cookies&quot;,&#10;      &quot;RequestHeaders&quot;,&#10;      &quot;ResponseHeaders&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;ownership_challenge&quot;: &quot;&lt;OWNERSHIP_CHALLENGE_TOKEN&gt;&quot;&#10;}&#x27;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-for-cloudflare-access-users">Note for Cloudflare Access users</h3>
@markup("md", "content/.markup/bodies/10522.md")
</aside>
<h2 id="enable-custom-fields-via-dashboard">Enable custom fields via dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>Custom log fields</strong> section, select <strong>Edit Custom Fields</strong>.</li>
<li>Select <strong>Set new Custom Field</strong>.</li>
<li>From the <strong>Field Type</strong> dropdown, select <em>Request Header</em>, <em>Response Header</em> or <em>Cookies</em> and type the <strong>Field Name</strong>.</li>
<li>When you are done, select <strong>Save</strong>.</li>
</ol>
<h2 id="use-case-logging-mtls-certificate-headers">Use case: Logging mTLS certificate headers</h2>
<p>To log mTLS certificate details (such as <code>cf-cert-subject-dn</code> or <code>cf-cert-issuer-dn</code>) in Logpush, you need to:</p>
<ol>
<li>Enable the <a href="/rules/transform/managed-transforms/reference/#add-tls-client-auth-headers">Add TLS client auth headers</a> Managed Transform to inject the certificate headers.</li>
<li>Configure Logpush custom fields using <code>transformed_request_fields</code> (not <code>request_fields</code>) to capture these Cloudflare-injected headers.</li>
<li>Ensure your Logpush job includes the <code>RequestHeaders</code> field.</li>
</ol>
<p>The mTLS headers are injected by Cloudflare after the client request is received, so they must be captured using <code>transformed_request_fields</code> rather than <code>request_fields</code>.</p>
<p>For more information on configuring client certificates, refer to <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Custom fields allow 100 headers per field type — this applies separately to <code>request_fields</code>, <code>transformed_request_fields</code>, <code>response_fields</code>, <code>raw_response_fields</code>, and <code>cookie_fields</code>.</li>
<li>The request header <code>Range</code> is currently not supported by Custom Fields.</li>
<li>Transformed and raw values for request and response headers are available only via the API and cannot be set through the UI.</li>
</ul>
