<p>The provided examples use the following fields in their rule expressions:</p>
<ul>
<li>
<p><a href="/ruleset-engine/rules-language/fields/reference/http.response.code/"><code>http.response.code</code></a> (Response Status Code): Represents the HTTP status code returned to the client, either set by a Cloudflare product or returned by the origin server. Use this field to customize the response for error codes returned by the origin server or by a Cloudflare product such as a Worker.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/"><code>cf.response.1xxx_code</code></a>: Contains the specific error code for Cloudflare-generated errors. This field will only work for Cloudflare-generated errors such as <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">52X</a> and <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">1XXX</a>.</p>
</li>
</ul>
<h3 id="custom-json-response-for-all-5xx-errors">Custom JSON response for all 5XX errors</h3>
<p>This example configures a custom JSON error response for all 5XX errors (<code>500</code>-<code>599</code>) in a zone. The HTTP status code of the custom error response will be set to <code>530</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12981.md")
</div></div>
<h3 id="custom-html-response-with-updated-status-code">Custom HTML response with updated status code</h3>
<p>This example configures a custom HTML error response for responses with a <code>500</code> HTTP status code, and redefines the response status code to <code>503</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12984.md")
</div></div>
<h3 id="custom-html-response-for-cloudflare-1020-errors">Custom HTML response for Cloudflare 1020 errors</h3>
<p>This example configures a custom HTML error response for <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/">Cloudflare error 1020</a> (Access Denied).</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12987.md")
</div></div>
<h3 id="custom-error-asset-created-from-a-url">Custom error asset created from a URL</h3>
<p>This example configures a custom error rule returning a previously created custom error asset named <code>500_error_template</code> for responses with a <code>500</code> HTTP status code.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12990.md")
</div></div>
