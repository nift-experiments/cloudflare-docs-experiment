<p>To import images, Cloudflare Images requires access to your Amazon S3 bucket. You can use credentials for any AWS Identity and Access Management (IAM) user with the correct permissions.</p>
<p>Cloudflare recommends creating a user with narrowly scoped permissions.</p>
<p>To create the required permissions:</p>
<ol>
<li>
<p>Log in to your AWS IAM account.</p>
</li>
<li>
<p>Create a policy with the following format (replace <code>&lt;BUCKET_NAME&gt;</code> with the bucket you want to grant access to):</p>
</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Action&quot;: [&quot;s3:Get*&quot;, &quot;s3:List*&quot;],&#10;			&quot;Resource&quot;: [&#10;				&quot;arn:aws:s3:::&lt;BUCKET_NAME&gt;&quot;,&#10;				&quot;arn:aws:s3:::&lt;BUCKET_NAME&gt;/*&quot;&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<ol start="3">
<li>Next, create a new user and attach the created policy to that user.</li>
</ol>
<p>You can now use both the Access Key ID and Secret Access Key to create a new source. Refer to <a href="/images/storage/upload-images/import-from-s3/enable/">Import images from S3</a> for setup instructions.</p>
