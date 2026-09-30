<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2026</time><h2 id="post-title">Use Google Artifact Registry images with Containers</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Containers now support <a href="https://cloud.google.com/artifact-registry">Google Artifact Registry</a> images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your <a href="/workers/wrangler/configuration/#containers">Wrangler configuration</a> instead of first pushing the image to Cloudflare Registry.</p>
<p>Provide the service account email with <code>--gar-email</code> and pipe the service account JSON key through <code>stdin</code>:</p>
<pre><code class="language-bash">cat &lt;PATH_TO_KEY&gt; | npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt; --secret-name=&lt;SECRET_NAME&gt;&#10;</code></pre>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17714.md")</div>
<p>Only <code>*-docker.pkg.dev</code> hosts are supported. To configure credentials, refer to <a href="/containers/guides/image-management/#use-private-google-artifact-registry-images">Use private Google Artifact Registry images</a>.</p>
<p>For more information, refer to <a href="/containers/guides/image-management/">Image management</a>.</p>
</div></article></div>
