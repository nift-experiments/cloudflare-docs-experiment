<p>The format of the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3982.md")
</div> report-only HTTP header added by Cloudflare is the following:
<pre><code class="language-txt">content-security-policy-report-only: script-src &#x27;unsafe-inline&#x27; &#x27;unsafe-eval&#x27;; connect-src &#x27;none&#x27;; report-uri https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report?&lt;QUERY_STRING&gt;&#10;</code></pre>
<p>If you <a href="/client-side-security/reference/settings/#reporting-endpoint">configured the reporting endpoint</a> to use the same hostname, the HTTP header will have the following format:</p>
<pre><code class="language-txt">content-security-policy-report-only: script-src &#x27;unsafe-inline&#x27; &#x27;unsafe-eval&#x27;; connect-src &#x27;none&#x27;; report-uri &lt;YOUR_HOSTNAME&gt;/cdn-cgi/script_monitor/report?&lt;QUERY_STRING&gt;&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/3981.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only">Mozilla Developer Network's (MDN) documentation on Content-Security-Policy-Report-Only</a></li>
</ul>
