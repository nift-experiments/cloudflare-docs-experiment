<p>Cloud Connector currently supports the following cloud providers and services:</p>
<ul>
<li>Cloudflare R2</li>
<li>Amazon Web Services - S3</li>
<li>Google Cloud Platform - Cloud Storage</li>
<li>Microsoft Azure - Blob Storage</li>
<li>Oracle Cloud - Object Storage</li>
</ul>
<h2 id="cloudflare-r2">Cloudflare R2</h2>
<p>The Cloudflare R2 bucket must be public and <a href="/r2/buckets/public-buckets/">exposed using a custom domain</a>. Buckets exposed using an <code>r2.dev</code> subdomain are not supported.</p>
<p>Additionally, the custom domain must be defined in the same zone where you are configuring the Cloud Connector rule.</p>
<h2 id="amazon-web-services-s3">Amazon Web Services - S3</h2>
<p>The hostname of your S3 bucket URL must have one of the following formats (where <code>*</code> is a wildcard character):</p>
<ul>
<li><code>*s3.amazonaws.com</code></li>
<li><code>*s3.&lt;REGION&gt;.amazonaws.com</code></li>
<li><code>*s3-website.&lt;REGION&gt;.amazonaws.com</code></li>
<li><code>*s3-website-&lt;REGION&gt;.amazonaws.com</code></li>
</ul>
<p>Cloud Connector supports both subdomain and URI path-style URLs:</p>
<ul>
<li><strong>Subdomain-style URLs</strong>: Set the hostname to <code>&lt;BUCKET_NAME&gt;.s3.amazonaws.com</code>. In this case, your files are accessible directly under the root of the bucket. For example, <code>https://example.com/index.html</code> will map to <code>https://&lt;BUCKET_NAME&gt;.s3.amazonaws.com/index.html</code>. When using <strong>Full (Strict)</strong> SSL/TLS mode, the <code>&lt;BUCKET_NAME&gt;</code> cannot include dots (use dashes instead). Refer to <a href="#ssl-connections-to-aws-s3-endpoints">SSL connections to AWS S3 endpoints</a> for details.</li>
<li><strong>URI path-style URLs</strong>: Set the hostname to <code>s3.amazonaws.com</code>. Here, your bucket name must be part of the URI path in your requests. For example, if your bucket name is <code>&lt;BUCKET_NAME&gt;</code>, files will be available on paths like <code>https://example.com/&lt;BUCKET_NAME&gt;/index.html</code>, and your Cloud Connector rule should filter traffic based on the URI path starting with <code>/&lt;BUCKET_NAME&gt;</code>.</li>
</ul>
<h3 id="ssl-connections-to-aws-s3-endpoints">SSL connections to AWS S3 endpoints</h3>
<p>The SSL setting applied to requests between Cloud Connector and AWS S3 depends on the type of S3 endpoint you use:</p>
<ul>
<li><strong>HTTPS-supported endpoints</strong>: For hostnames like <code>*s3.&lt;REGION&gt;.amazonaws.com</code> and <code>*s3.amazonaws.com</code>, Cloudflare will connect to AWS S3 over HTTPS if you set your zone's SSL/TLS mode to <strong>Full</strong> or <strong>Full (Strict)</strong>. When using <strong>Full (Strict)</strong>, the bucket name cannot include dots (use dashes instead).</li>
<li><strong>Non-HTTPS endpoints</strong>: For website-style hostnames such as <code>*s3-website.&lt;REGION&gt;.amazonaws.com</code> or <code>*s3-website-&lt;REGION&gt;.amazonaws.com</code>, which do not support HTTPS, Cloudflare will default to <strong>Flexible SSL</strong>.</li>
</ul>
<h3 id="get-the-bucket-url">Get the bucket URL</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13030.md")
</div>
<p>For more information, refer to the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/EnableWebsiteHosting.html">Amazon S3 documentation</a>.</p>
<p>Once you configure Cloud Connector with your storage provider's public bucket, you may wish that only Cloudflare can access the objects in that bucket. To achieve this, check your provider's documentation on how to create a policy that only allows incoming requests from <a href="https://www.cloudflare.com/ips/">Cloudflare IP addresses</a>.</p>
<h2 id="google-cloud-platform-cloud-storage">Google Cloud Platform - Cloud Storage</h2>
<p>The hostname of your Cloud Storage bucket URL must be the following (where <code>*</code> is a wildcard character):</p>
<ul>
<li><code>*storage.googleapis.com</code></li>
<li><code>*storage.cloud.google.com</code></li>
</ul>
<p>Cloud Connector supports both subdomain and URI path-style URLs:</p>
<ul>
<li><strong>Subdomain-style URLs</strong>: Set the hostname to <code>&lt;BUCKET_NAME&gt;.storage.googleapis.com</code>. In this case, your files are accessible directly under the root of the bucket. For example, <code>https://example.com/index.html</code> will map to <code>https://&lt;BUCKET_NAME&gt;.storage.googleapis.com/index.html</code>.</li>
<li><strong>URI path-style URLs</strong>: Set the hostname to <code>storage.googleapis.com</code>. Here, your bucket name must be part of the URI path in your requests. For example, if your bucket name is <code>&lt;BUCKET_NAME&gt;</code>, files will be available on paths like <code>https://example.com/&lt;BUCKET_NAME&gt;/index.html</code>, and your Cloud Connector rule should filter traffic based on the URI path starting with <code>/&lt;BUCKET_NAME&gt;</code>.</li>
</ul>
<h3 id="get-the-bucket-url-1">Get the bucket URL</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13031.md")
</div>
<p>If the files in your bucket are not publicly accessible, you must change the bucket permissions. For details, refer to the <a href="https://cloud.google.com/storage/docs/access-control/making-data-public#buckets">Google Cloud Storage documentation</a>.</p>
<p>Once you configure Cloud Connector with your storage provider's public bucket, you may wish that only Cloudflare can access the objects in that bucket. To achieve this, check your provider's documentation on how to create a policy that only allows incoming requests from <a href="https://www.cloudflare.com/ips/">Cloudflare IP addresses</a>.</p>
<h2 id="microsoft-azure-blob-storage">Microsoft Azure - Blob Storage</h2>
<p>The hostname of your Blob Storage bucket URL must have one of the following formats:</p>
<ul>
<li><code>&lt;BUCKET_NAME&gt;.blob.core.windows.net</code></li>
<li><code>&lt;BUCKET_NAME&gt;.web.core.windows.net</code></li>
</ul>
<p>For Azure Blog Storage, Cloud Connector supports only subdomain URLs like <code>&lt;BUCKET_NAME&gt;.blob.core.windows.net</code>. This means that your files will be accessible directly under the root of the bucket. For example, <code>https://example.com/index.html</code> will map to <code>https://&lt;BUCKET_NAME&gt;.blob.core.windows.net/index.html</code>.</p>
<h3 id="get-the-bucket-url-2">Get the bucket URL</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13032.md")
</div>
<p>If the blob container is not configured for public access, you must change the container settings. For details, refer to the <a href="https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=portal">Azure Storage documentation</a>.</p>
<p>Once you configure Cloud Connector with your storage provider's public bucket, you may wish that only Cloudflare can access the objects in that bucket. To achieve this, check your provider's documentation on how to create a policy that only allows incoming requests from <a href="https://www.cloudflare.com/ips/">Cloudflare IP addresses</a>.</p>
<h2 id="oracle-cloud-infrastructure-object-storage">Oracle Cloud Infrastructure Object Storage</h2>
<p>Cloud Connector supports Oracle Cloud Infrastructure (OCI) Object Storage through the Amazon S3 Compatibility API.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="public-buckets-only">Public buckets only</h3>
@markup("md", "content/.markup/bodies/13029.md")
</aside>
<p>Enter an OCI hostname without a protocol, port, or path. Cloud Connector accepts the following formats:</p>
<table>
<thead>
<tr>
<th>Addressing style</th>
<th>Hostname format</th>
<th>Request path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Path style (traditional)</td>
<td><code>&lt;NAMESPACE&gt;.compat.objectstorage.&lt;REGION&gt;.oraclecloud.com</code></td>
<td><code>/&lt;BUCKET_NAME&gt;/&lt;OBJECT_NAME&gt;</code></td>
</tr>
<tr>
<td>Path style (dedicated)</td>
<td><code>&lt;NAMESPACE&gt;.compat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com</code></td>
<td><code>/&lt;BUCKET_NAME&gt;/&lt;OBJECT_NAME&gt;</code></td>
</tr>
<tr>
<td>Virtual-hosted style</td>
<td><code>&lt;BUCKET_NAME&gt;.vhcompat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com</code></td>
<td><code>/&lt;OBJECT_NAME&gt;</code></td>
</tr>
</tbody>
</table>
<p>For path-style endpoints, include the bucket name in the incoming request path. For example, <code>https://example.com/&lt;BUCKET_NAME&gt;/index.html</code> maps to the same path on the OCI endpoint.</p>
<p>For virtual-hosted endpoints, the bucket name is part of the hostname. An incoming request to <code>https://example.com/index.html</code> maps to <code>/index.html</code> on that bucket. OCI requires virtual-hosted bucket names to use a regional scope and a DNS-compatible name that is unique within the region.</p>
<p>For more information, refer to <a href="https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/dedicatedendpoints.htm">Object Storage Dedicated Endpoints</a>, <a href="https://docs.oracle.com/en-us/iaas/Content/Object/s3-virtual-style.htm">Amazon S3 Compatibility API Hosted Style Support in Object Storage</a>, and <a href="https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm">Changing an Object Storage Bucket's Visibility</a>.</p>
<p>Once you configure Cloud Connector with your storage provider's public bucket, you may wish that only Cloudflare can access the objects in that bucket. To achieve this, check your provider's documentation on how to create a policy that only allows incoming requests from <a href="https://www.cloudflare.com/ips/">Cloudflare IP addresses</a>.</p>
