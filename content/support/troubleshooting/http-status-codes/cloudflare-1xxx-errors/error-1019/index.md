<h2 id="error-1019-compute-server-error">Error 1019: Compute server error</h2>
<p>This error indicates a compute server error related to a Cloudflare Worker.</p>
<h3 id="common-cause">Common cause</h3>
<p>A Cloudflare Worker script recursively references itself.</p>
<h3 id="resolution">Resolution</h3>
<p>Ensure your Cloudflare Worker does not access a URL that calls the same Workers script.</p>
