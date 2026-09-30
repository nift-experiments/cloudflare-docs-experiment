<p>Cloudflare Logpush supports pushing logs directly to Google Cloud Storage (GCS) via the Cloudflare dashboard or via API.</p>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<ol>
<li>
<p>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page at the account or or domain (also known as zone) level.</p>
<p>For account: <div class="nb-dash-button"></div></p>
<p>For domain (also known as zone): <div class="nb-dash-button"></div></p>
</li>
<li>
<p>Depending on your choice, you have access to <a href="/logs/logpush/logpush-job/datasets/account/">account-scoped datasets</a> and <a href="/logs/logpush/logpush-job/datasets/zone/">zone-scoped datasets</a>, respectively.</p>
</li>
<li>
<p>Select <strong>Create a Logpush job</strong>.</p>
</li>
<li>
<p>In <strong>Select a destination</strong>, choose <strong>Google Cloud Storage</strong>.</p>
</li>
<li>
<p>Enter or select the following destination details:</p>
<ul>
<li><strong>Bucket</strong> - GCS bucket name</li>
<li><strong>Path</strong> - bucket location within the storage container</li>
<li><strong>Organize logs into daily subfolders</strong> (recommended)</li>
<li>For <strong>Grant Cloudflare access to upload files to your bucket</strong>, make sure your bucket has added Cloudflare’s IAM as a user with a <a href="https://cloud.google.com/storage/docs/access-control/iam-roles">Storage Object Admin role</a>.</li>
</ul>
</li>
</ol>
<p>When you are done entering the destination details, select <strong>Continue</strong>.</p>
<ol start="6">
<li>
<p>To prove ownership, Cloudflare will send a file to your designated destination. To find the token, select the <strong>Open</strong> button in the <strong>Overview</strong> tab of the ownership challenge file, then paste it into the Cloudflare dashboard to verify your access to the bucket. Enter the <strong>Ownership Token</strong> and select <strong>Continue</strong>.</p>
</li>
<li>
<p>Select the dataset to push to the storage service.</p>
</li>
<li>
<p>In the next step, you need to configure your logpush job:</p>
<ul>
<li>Enter the <strong>Job name</strong>.</li>
<li>Under <strong>If logs match</strong>, you can select the events to include and/or remove from your logs. Refer to <a href="/logs/logpush/logpush-job/filters/">Filters</a> for more information. Not all datasets have this option available.</li>
<li>In <strong>Send the following fields</strong>, you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.</li>
</ul>
</li>
<li>
<p>In <strong>Advanced Options</strong>, you can:</p>
<ul>
<li>Choose the format of timestamp fields in your logs (<code>RFC3339</code> (default), <code>Unix</code>, or <code>UnixNano</code>).</li>
<li>Select a <a href="/logs/logpush/logpush-job/api-configuration/#sampling-rate">sampling rate</a> for your logs or push a randomly-sampled percentage of logs.</li>
<li>Enable redaction for <code>CVE-2021-44228</code>. This option will replace every occurrence of <code>${</code> with <code>x{</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Submit</strong> once you are done configuring your logpush job.</p>
</li>
</ol>
<h2 id="create-and-get-access-to-a-gcs-bucket">Create and get access to a GCS bucket</h2>
<p>Cloudflare uses Google Cloud Identity and Access Management (IAM) to gain access to your bucket. The Cloudflare IAM service account needs admin permission for the bucket.</p>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.
<br /></p>
<p>To enable Logpush to GCS:</p>
<ol>
<li>
<p>Create a GCS bucket. Refer to <a href="https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-console">instructions from GCS</a>.</p>
</li>
<li>
<p>In <strong>Storage</strong> &gt; <strong>Browser</strong> &gt; <strong>Bucket</strong> &gt; <strong>Permissions</strong>, add the member <code>logpush@cloudflare-data.iam.gserviceaccount.com</code> with <code>Storage Object Admin</code> permission.</p>
</li>
</ol>
<h2 id="compression-and-decompressive-transcoding">Compression and decompressive transcoding</h2>
<p>Logpush always delivers log files in gzip-compressed format. When uploading to GCS, Logpush sets <code>Content-Encoding: gzip</code> on the object metadata.</p>
<p>GCS performs <a href="https://cloud.google.com/storage/docs/transcoding">decompressive transcoding</a> by default. This means that when a client downloads an object stored with <code>Content-Encoding: gzip</code>, GCS may automatically decompress the file in transit if the client does not include <code>Accept-Encoding: gzip</code> in the request headers. When this happens, the downloaded file contains uncompressed data even though the filename retains the <code>.gz</code> extension.</p>
<p>To download log files in their original compressed format, use one of the following approaches:</p>
<ul>
<li><strong>Include <code>Accept-Encoding: gzip</code> in your download request headers.</strong> For example, when using gsutil:</li>
</ul>
<pre><code class="language-sh">gsutil -h &quot;Accept-Encoding: gzip&quot; cp gs://your-bucket/path/file.log.gz .&#10;</code></pre>
