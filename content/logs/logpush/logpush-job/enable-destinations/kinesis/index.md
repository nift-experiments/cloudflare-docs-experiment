<p>Logpush supports <a href="https://aws.amazon.com/kinesis/">Amazon Kinesis</a> as a destination for all datasets. Each Kinesis record that Logpush sends will contain a batch of GZIP-compressed data in newline-delimited JSON format (by default), or in the format specified in the <a href="/logs/logpush/logpush-job/log-output-options/"><code>output_options</code></a> parameter when the job was created.</p>
<h2 id="configure-kinesis-using-sts-assume-role-recommended">Configure Kinesis using STS Assume Role (recommended)</h2>
<ol>
<li>Create an IAM Role for Cloudflare Logpush to Assume with the following trust relationship:</li>
</ol>
<pre><code class="language-java">{&#10;    &quot;Version&quot;: &quot;2012-10-17&quot;,&#10;    &quot;Statement&quot;: [&#10;        {&#10;            &quot;Effect&quot;: &quot;Allow&quot;,&#10;            &quot;Principal&quot;: {&#10;                &quot;AWS&quot;: [&#10;                    &quot;arn:aws:iam::391854517948:user/cloudflare-logpush&quot;&#10;                ]&#10;            },&#10;            &quot;Action&quot;: &quot;sts:AssumeRole&quot;&#10;        }&#10;    ]&#10;}&#10;</code></pre>
<ol start="2">
<li>Ensure that the IAM role has permissions to perform the <code>PutRecord</code> action on your Kinesis stream. Replace <code>&lt;AWS_REGION&gt;</code>, <code>&lt;YOUR_AWS_ACCOUNT_ID&gt;</code> and <code>&lt;STREAM_NAME&gt;</code> with your own values:</li>
</ol>
<pre><code class="language-java">{&#10;    &quot;Version&quot;: &quot;2012-10-17&quot;,&#10;    &quot;Statement&quot;: [&#10;        {&#10;            &quot;Effect&quot;: &quot;Allow&quot;,&#10;            &quot;Action&quot;: &quot;kinesis:PutRecord&quot;,&#10;            &quot;Resource&quot;: &quot;arn:aws:kinesis:&lt;AWS_REGION&gt;:&lt;YOUR_AWS_ACCOUNT_ID&gt;:stream/&lt;STREAM_NAME&gt;&quot;&#10;        }&#10;    ]&#10;}&#10;</code></pre>
<ol start="3">
<li>Create a Logpush job, using the following format for the <code>destination_conf</code> field:</li>
</ol>
<pre><code class="language-bash">kinesis://&lt;STREAM_NAME&gt;?region=&lt;AWS_REGION&gt;&amp;sts-assume-role-arn=arn:aws:iam::&lt;YOUR_AWS_ACCOUNT_ID&gt;:role/&lt;IAM_ROLE_NAME&gt;&#10;</code></pre>
<ol start="4">
<li>(optional) When using STS Assume Role, you can include <code>sts-external-id</code> as a <code>destination_conf</code> parameter so it is included in your Logpush job's requests to Kinesis. Refer to <a href="https://aws.amazon.com/blogs/apn/securely-using-external-id-for-accessing-aws-accounts-owned-by-others/">Securely Using External ID for Accessing AWS Accounts Owned by Others</a> for more information.</li>
</ol>
<pre><code class="language-bash">kinesis://&lt;STREAM_NAME&gt;?region=&lt;AWS_REGION&gt;&amp;sts-assume-role-arn=arn:aws:iam::&lt;YOUR_AWS_ACCOUNT_ID&gt;:role/&lt;IAM_ROLE_NAME&gt;&amp;sts-external-id=&lt;EXTERNAL_ID&gt;&#10;</code></pre>
<h3 id="sts-assume-role-example">STS Assume Role example</h3>
<pre><code class="language-bash">$ curl https://api.cloudflare.com/client/v4/zones/$ZONE_TAG/logpush/jobs \&#10;&#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;&#45;H &#x27;Content-Type: application/json&#x27; -d &#x27;{&#10;  &quot;name&quot;: &quot;kinesis&quot;,&#10;  &quot;destination_conf&quot;: &quot;kinesis://&lt;STREAM_NAME&gt;?region=&lt;AWS_REGION&gt;&amp;sts-assume-role-arn=arn:aws:iam::&lt;YOUR_AWS_ACCOUNT_ID&gt;:role/&lt;IAM_ROLE_NAME&gt;&quot;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;&#10;</code></pre>
<h2 id="configure-kinesis-using-iam-access-keys">Configure Kinesis using IAM Access Keys</h2>
<p>When configuring your Logpush job using IAM Access Keys, ensure that the IAM user has permission to perform the <code>PutRecord</code> action on your Kinesis stream:</p>
<pre><code class="language-bash">kinesis://&lt;STREAM_NAME&gt;?region=&lt;AWS_REGION&gt;&amp;access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;AWS_SECRET_ACCESS_KEY&gt;&#10;</code></pre>
<h3 id="iam-access-key-example">IAM Access Key example</h3>
<pre><code class="language-bash">$ curl https://api.cloudflare.com/client/v4/zones/$ZONE_TAG/logpush/jobs \&#10;&#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;&#45;H &#x27;Content-Type: application/json&#x27; -d &#x27;{&#10;  &quot;name&quot;: &quot;kinesis&quot;,&#10;  &quot;destination_conf&quot;: &quot;kinesis://&lt;STREAM_NAME&gt;?region=&lt;AWS_REGION&gt;&amp;access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;AWS_SECRET_ACCESS_KEY&gt;&quot;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;&#10;</code></pre>
