<p>Learn how the location of data stored in R2 is determined and about the different available inputs that control the physical location where objects in your buckets are stored.</p>
<h2 id="automatic-recommended">Automatic (recommended)</h2>
<p>When you create a new bucket, the data location is set to Automatic by default. Currently, this option chooses a bucket location in the closest available region to the create bucket request based on the location of the caller.</p>
<h2 id="location-hints">Location Hints</h2>
<p>Location Hints are optional parameters you can provide during bucket creation to indicate the primary geographical location you expect data will be accessed from.</p>
<p>Using Location Hints can be a good choice when you expect the majority of access to data in a bucket to come from a different location than where the create bucket request originates. Keep in mind Location Hints are a best effort and not a guarantee, and they should only be used as a way to optimize performance by placing regularly updated content closer to users.</p>
<h3 id="set-hints-via-the-cloudflare-dashboard">Set hints via the Cloudflare dashboard</h3>
<p>You can choose to automatically create your bucket in the closest available region based on your location or choose a specific location from the list.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create bucket**.
3. Enter a name for the bucket.
4. Under **Location**, leave _None_ selected for automatic selection or choose a region from the list.
5. Select **Create bucket** to complete the bucket creation process.
<h3 id="set-hints-via-the-s3-api">Set hints via the S3 API</h3>
<p>You can set the Location Hint via the <code>LocationConstraint</code> parameter using the S3 API:</p>
<pre><code class="language-js">await S3.send(&#10;	new CreateBucketCommand({&#10;		Bucket: &quot;YOUR_BUCKET_NAME&quot;,&#10;		CreateBucketConfiguration: {&#10;			LocationConstraint: &quot;WNAM&quot;,&#10;		},&#10;	}),&#10;);&#10;</code></pre>
<p>Refer to <a href="/r2/examples/">Examples</a> for additional examples from other S3 SDKs.</p>
<h3 id="available-hints">Available hints</h3>
<p>The following hint locations are supported:</p>
<table>
<thead>
<tr>
<th>Hint</th>
<th>Hint description</th>
</tr>
</thead>
<tbody>
<tr>
<td>wnam</td>
<td>Western North America</td>
</tr>
<tr>
<td>enam</td>
<td>Eastern North America</td>
</tr>
<tr>
<td>weur</td>
<td>Western Europe</td>
</tr>
<tr>
<td>eeur</td>
<td>Eastern Europe</td>
</tr>
<tr>
<td>apac</td>
<td>Asia-Pacific</td>
</tr>
<tr>
<td>oc</td>
<td>Oceania</td>
</tr>
</tbody>
</table>
<h3 id="additional-considerations">Additional considerations</h3>
<p>Location Hints are only honored the first time a bucket with a given name is created. If you delete and recreate a bucket with the same name, the original bucket’s location will be used.</p>
<h2 id="jurisdictional-restrictions">Jurisdictional Restrictions</h2>
<p>Jurisdictional Restrictions guarantee objects in a bucket are stored within a specific jurisdiction.</p>
<p>Use Jurisdictional Restrictions when you need to ensure data is stored and processed within a jurisdiction to meet data residency requirements, including local regulations such as the <a href="https://gdpr-info.eu/">GDPR</a> or <a href="https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/">FedRAMP</a>.</p>
<h3 id="set-jurisdiction-via-the-cloudflare-dashboard">Set jurisdiction via the Cloudflare dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create bucket**.
3. Enter a name for the bucket.
4. Under **Location**, select **Specify jurisdiction** and choose a jurisdiction from the list.
5. Select **Create bucket** to complete the bucket creation process.
<h3 id="using-jurisdictions-from-workers">Using jurisdictions from Workers</h3>
<p>To access R2 buckets that belong to a jurisdiction from <a href="/workers/">Workers</a>, you will need to specify the jurisdiction as well as the bucket name as part of your <a href="/r2/api/workers/workers-api-usage/#3-bind-your-bucket-to-a-worker">bindings</a> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11371.md")
</div>
<p>For more information on getting started, refer to <a href="/r2/api/workers/workers-api-usage/">Use R2 from Workers</a>.</p>
<h3 id="using-jurisdictions-with-the-s3-api">Using jurisdictions with the S3 API</h3>
<p>When interacting with R2 resources that belong to a defined jurisdiction with the S3 API or existing S3-compatible SDKs, you must specify the <a href="#available-jurisdictions">jurisdiction</a> in your S3 endpoint:</p>
<p><code>https://&lt;ACCOUNT_ID&gt;.&lt;JURISDICTION&gt;.r2.cloudflarestorage.com</code></p>
<p>You can use your jurisdiction-specific endpoint for any <a href="/r2/api/s3/api/">supported S3 API operations</a>. When using a jurisdiction endpoint, you will not be able to access R2 resources outside of that jurisdiction.</p>
<p>The example below shows how to create an R2 bucket in the <code>eu</code> jurisdiction using the <a href="https://www.npmjs.com/package/@aws-sdk/client-s3"><code>@aws-sdk/client-s3</code></a> package for JavaScript.</p>
<pre><code class="language-js">import { S3Client, CreateBucketCommand } from &quot;@aws-sdk/client-s3&quot;;&#10;const S3 = new S3Client({&#10;	endpoint: &quot;https://&lt;account_id&gt;.eu.r2.cloudflarestorage.com&quot;,&#10;	credentials: {&#10;		accessKeyId: &quot;&lt;access_key_id&gt;&quot;,&#10;		secretAccessKey: &quot;&lt;access_key_secret&gt;&quot;,&#10;	},&#10;	region: &quot;auto&quot;,&#10;});&#10;await S3.send(&#10;	new CreateBucketCommand({&#10;		Bucket: &quot;YOUR_BUCKET_NAME&quot;,&#10;	}),&#10;);&#10;</code></pre>
<p>Refer to <a href="/r2/examples/">Examples</a> for additional examples from other S3 SDKs.</p>
<h3 id="available-jurisdictions">Available jurisdictions</h3>
<p>The following jurisdictions are supported:</p>
<table>
<thead>
<tr>
<th>Jurisdiction</th>
<th>Jurisdiction description</th>
</tr>
</thead>
<tbody>
<tr>
<td>eu</td>
<td>European Union</td>
</tr>
<tr>
<td>fedramp</td>
<td>FedRAMP</td>
</tr>
<tr>
<td>us</td>
<td>United States</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11370.md")
</aside>
<h3 id="limitations">Limitations</h3>
<p>The following services do not interact with R2 resources with assigned jurisdictions:</p>
<ul>
<li><a href="/logs/logpush/logpush-job/enable-destinations/r2/">Logpush</a>. As a workaround to this limitation, you can set up a <a href="/data-localization/how-to/r2/#send-logs-to-r2-via-s3-compatible-endpoint">Logpush job using an S3-compatible endpoint</a> to store logs in an R2 bucket in the jurisdiction of your choice.</li>
</ul>
<h3 id="additional-considerations-1">Additional considerations</h3>
<p>Once an R2 bucket is created, the jurisdiction cannot be changed.</p>
