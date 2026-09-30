<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4293.md")
</aside>
<p>This tutorial covers how to build a <a href="/r2/buckets/">Cloudflare R2 bucket</a> to store logs, and how to connect the bucket to the Zero Trust <a href="/cloudflare-one/insights/logs/logpush/">Logpush service</a> to store logs persistently and export them into other tools.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Ensure Cloudflare R2 and the Zero Trust Logpush integration are included in your plan. For more information, contact your account team.</li>
</ul>
<h2 id="create-a-cloudflare-r2-bucket">Create a Cloudflare R2 bucket</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to the <strong>R2 Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create bucket</strong>.</li>
<li>Enter an identifiable name for the bucket, then select <strong>Create bucket</strong>.</li>
</ol>
<h2 id="create-an-r2-api-token">Create an R2 API token</h2>
<ol>
<li>Return to <strong>R2</strong>, then select <strong>Manage R2 API tokens</strong>.</li>
<li>Select <strong>Create API token</strong>.</li>
<li>In <strong>Permissions</strong>, select <strong>Object Read &amp; Write</strong>.</li>
<li>In <strong>Specify bucket(s)</strong>, choose <em>Apply to specific buckets only</em>. Select the bucket you created.</li>
<li>Configure other token settings to your preferences.</li>
<li>Select <strong>Create API Token</strong>.</li>
<li>Copy the <strong>Access Key ID</strong>, <strong>Secret Access Key</strong>, and endpoint URL values. You will not be able to access these values again.</li>
<li>Select <strong>Finish</strong>.</li>
</ol>
<h2 id="connect-a-zero-trust-logpush-job">Connect a Zero Trust Logpush job</h2>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Logs</strong>. Select <strong>Manage Logpush</strong>.</li>
<li>Select <strong>Connect a service</strong>.</li>
<li>Choose which data sets and fields you want to send to your bucket. Select <strong>Next</strong>.</li>
<li>Select <strong>S3 Compatible</strong>.</li>
<li>In <strong>S3 Compatible Bucket Path</strong>, enter the name of your bucket.</li>
<li>In <strong>Bucket region</strong>, enter <code>auto</code>.</li>
<li>Enter the values for <strong>Access Key ID</strong>, <strong>Secret Access Key</strong>, and <strong>Endpoint URL</strong> in their corresponding fields.</li>
<li>Select <strong>Push</strong>. If prompted, you do not need to prove ownership with a token challenge.</li>
</ol>
<p>The Logpush job will send the selected Zero Trust logs to your R2 bucket.</p>
