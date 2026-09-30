<p class="article-summary">Route requests with a URI path starting with `/images` to a specific AWS S3 bucket using Cloud Connector.</p>
<p>To route requests to <code>/images</code> on your domain to an AWS S3 bucket:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13042.md")
</div>
<p>This setup will route all traffic matching <code>http*://&lt;YOUR_HOSTNAME&gt;/images/*</code> (HTTPS and HTTP requests) to your S3 bucket. Make sure to replace <code>&lt;YOUR_HOSTNAME&gt;</code> with your actual hostname and adjust the example paths according to your setup.</p>
