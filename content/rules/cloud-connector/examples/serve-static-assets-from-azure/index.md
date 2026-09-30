<p class="article-summary">Route requests with a URI path starting with `/static-assets` to an Azure Blob Storage container using Cloud Connector.</p>
<p>To serve static assets from an Azure Blob Storage container:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13040.md")
</div>
<p>This setup ensures that all traffic matching <code>http*://&lt;YOUR_HOSTNAME&gt;/static-assets/*</code> (HTTPS and HTTP requests) is served from your Azure Blob Storage container. Make sure to replace <code>&lt;YOUR_HOSTNAME&gt;</code> with your actual hostname and adjust the example paths according to your setup.</p>
