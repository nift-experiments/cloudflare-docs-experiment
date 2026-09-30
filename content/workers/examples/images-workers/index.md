<p class="article-summary">Set up custom domain for Images using a Worker or serve images using a prefix path and Cloudflare registered domain.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/images-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<p>To serve images from a custom domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong> &gt; <strong>Workers</strong> &gt; <strong>Create Worker</strong> and create your Worker.</li>
<li>In your Worker, select <strong>Quick edit</strong> and paste the following code.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16432.md")
</div></div>
<p>Another way you can serve images from a custom domain is by using the <code>cdn-cgi/imagedelivery</code> prefix path which is used as path to trigger <code>cdn-cgi</code> image proxy.</p>
<p>Below is an example showing the hostname as a Cloudflare proxied domain under the same account as the Image, followed with the prefix path and the image <code>&lt;ACCOUNT_HASH&gt;</code>, <code>&lt;IMAGE_ID&gt;</code> and <code>&lt;VARIANT_NAME&gt;</code> which can be found in the <strong>Images</strong> on the Cloudflare dashboard.</p>
<pre><code class="language-js">https://example.com/cdn-cgi/imagedelivery/&lt;ACCOUNT_HASH&gt;/&lt;IMAGE_ID&gt;/&lt;VARIANT_NAME&gt;&#10;</code></pre>
