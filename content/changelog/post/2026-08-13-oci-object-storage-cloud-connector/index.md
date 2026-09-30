<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 13, 2026</time><h2 id="post-title">Oracle Cloud Infrastructure Object Storage support in Cloud Connector</h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.</p>
<p>OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional <code>oraclecloud.com</code> and dedicated <code>customer-oci.com</code> path-style endpoints.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="public-buckets-only">Public buckets only</h4>
@markup("md", "content/.markup/bodies/17751.md")</aside>
<h4 id="api-example">API example</h4>
<p>Set <code>provider</code> to <code>oci_storage</code> and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:</p>
<pre><code class="language-json">{&#10;	&quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/assets/*\&quot;&quot;,&#10;	&quot;provider&quot;: &quot;oci_storage&quot;,&#10;	&quot;description&quot;: &quot;Route assets to OCI Object Storage&quot;,&#10;	&quot;enabled&quot;: true,&#10;	&quot;parameters&quot;: {&#10;		&quot;host&quot;: &quot;&lt;BUCKET_NAME&gt;.vhcompat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For endpoint formats and bucket requirements, refer to <a href="/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage">Supported cloud providers in Cloud Connector</a>.</p>
</div></article></div>
