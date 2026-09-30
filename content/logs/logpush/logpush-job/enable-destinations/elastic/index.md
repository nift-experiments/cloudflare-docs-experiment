<p>Push your Cloudflare logs to Elastic for instant visibility and insights. Enabling this integration with Elastic comes with a predefined dashboard to view all of your Cloudflare observability and security data with ease.</p>
<p>The Cloudflare Logpush integration can be used in three different modes to collect data:</p>
<ul>
<li><strong>HTTP Endpoint mode</strong> - Cloudflare pushes logs directly to an HTTP endpoint hosted by your Elastic Agent.</li>
<li><strong>AWS S3 polling mode</strong> - Cloudflare writes data to S3, and the Elastic Agent polls the S3 bucket by listing its contents and reading new files.</li>
<li><strong>AWS S3 SQS mode</strong> - Cloudflare writes data to S3, S3 pushes a new object notification to SQS, the Elastic Agent receives the notification from SQS, and then reads the S3 object. Multiple Agents can be used in this mode.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10560.md")
</aside>
<h2 id="enable-logpush-job-in-cloudflare">Enable Logpush Job in Cloudflare</h2>
<p>Determine which method you want to use, and configure the appropriate Logpush job in the Cloudflare dashboard or via the API.</p>
<p>Elastic supports the default JSON format.</p>
<p>To push logs to an object storage for short term storage and buffering before ingesting into Elastic (recommended), follow the instructions to configure a Logpush job to push logs to <a href="/logs/logpush/logpush-job/enable-destinations/aws-s3/">AWS S3</a>, <a href="/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/">Google Cloud Storage</a>, or <a href="/logs/logpush/logpush-job/enable-destinations/azure/">Azure Blob Storage</a>.</p>
<p>To use the <a href="/logs/logpush/logpush-job/enable-destinations/http/">HTTP Endpoint mode</a>, use the API to push logs to an HTTP endpoint backed by your Elastic Agent.</p>
<p>Add the same custom header along with its value on both sides for additional security.</p>
<p>For example, while creating a job along with a header and value for a particular dataset:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;PUBLIC_DOMAIN&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;https://&lt;PUBLIC_DOMAIN&gt;:&lt;PUBLIC_PORT&gt;?header_&lt;SECRET_HEADER&gt;=&lt;SECRET_VALUE&gt;&quot;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;RayID&quot;,&#10;      &quot;EdgeStartTimestamp&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  }&#10;}&#x27;</code></pre>
<h2 id="enable-the-integration-in-elastic">Enable the Integration in Elastic</h2>
<p>Once the Logpush job is configured, follow Elastics instructions for <a href="https://docs.elastic.co/integrations/cloudflare_logpush">setting up the Integration</a> in the Elastic app.</p>
<h2 id="view-dashboards">View Dashboards</h2>
<p>Log in to your <a href="https://www.elastic.co/">Elastic account</a> to view prebuilt dashboards and configure alerts.</p>
