<p>Jobs in Logpush now have a new key, <strong>output_options</strong>, which replaces <strong>logpull_options</strong> and allows for more flexible formatting. You can modify <strong>output_options</strong> via the API.</p>
<h2 id="replace-logpull-options">Replace logpull_options</h2>
<p>Previously, Logpush jobs could be customized by specifying the list of fields, sampling rate, and timestamp format in <strong>logpull_options</strong> as <a href="/logs/logpush/logpush-job/api-configuration/#options">URL-encoded parameters</a>. For example:</p>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &lt;JOB_ID&gt;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: false,&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;logpull_options&quot;: &quot;fields=ClientIP,EdgeStartTimestamp,RayID&amp;sample=0.1&amp;timestamps=rfc3339&quot;,&#10;  &quot;destination_conf&quot;: &quot;s3://&lt;BUCKET_PATH&gt;?region=us-west-2&quot;&#10;}&#10;</code></pre>
<p>We have replaced this with <strong>output_options</strong> as it is used for both Logpull and Logpush.</p>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &lt;JOB_ID&gt;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: false,&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;    &quot;sample_rate&quot;: 0.1,&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;destination_conf&quot;: &quot;s3://&lt;BUCKET_PATH&gt;?region=us-west-2&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="updates-replace-output-options-in-full">Updates replace output_options in full</h3>
@markup("md", "content/.markup/bodies/10520.md")
</aside>
