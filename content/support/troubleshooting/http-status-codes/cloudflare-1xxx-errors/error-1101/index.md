<h2 id="error-1101-rendering-error">Error 1101: Rendering error</h2>
<p>This error indicates a rendering issue.</p>
<h3 id="common-cause">Common cause</h3>
<p>This error typically occurs when a Cloudflare Worker encounters a runtime JavaScript exception.</p>
<h3 id="debugging">Debugging</h3>
<p>To identify the specific JavaScript exception:</p>
<ol>
<li>Check your Workers logs in the Cloudflare dashboard under <strong>Workers &amp; Pages</strong> &gt; <strong>Your Worker</strong> &gt; <strong>Logs</strong>.</li>
<li>Review the Workers code for potential runtime errors such as:
<ul>
<li>Undefined variables or functions</li>
<li>Type errors</li>
<li>Promise rejections</li>
<li>Network request failures</li>
</ul>
</li>
<li>Test the <a href="/workers/local-development/#local-development">Worker locally</a> with sample requests to reproduce the error.</li>
<li>Refer to <a href="/workers/observability/errors/">Workers error handling</a> for more details on debugging Workers.</li>
</ol>
<h3 id="resolution">Resolution</h3>
<p>Fix the JavaScript exception in your Workers code. If you need assistance, <a href="/support/contacting-cloudflare-support/">provide appropriate issue details</a> to Cloudflare Support, including:</p>
<ul>
<li>The Ray ID from the error page</li>
<li>The Worker name</li>
<li>Recent changes to the Worker code</li>
<li>Steps to reproduce the error</li>
</ul>
<h3 id="related-errors">Related errors</h3>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/">Error 1102</a> - Workers CPU time limit exceeded</li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/">Error 500</a> - Internal server error (can be caused by Workers exceptions)</li>
</ul>
