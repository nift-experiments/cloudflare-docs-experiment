<p>You can manipulate the URL of a request through different operations, namely rewrites and redirects:</p>
<ul>
<li>
<p><strong>URL rewrite</strong>: A server-side operation that converts a source URL into a target URL. It occurs before a web server has fully processed a request. A rewrite is not visible to website visitors, since the URL displayed in the browser does not change. Configure URL Rewrite Rules to perform rewrites on the Cloudflare global network without reaching your web server.</p>
</li>
<li>
<p><strong>URL redirect</strong>: A client-side operation that converts a source URL into a target URL. It occurs after the web server has loaded the initial URL. In this case, a website visitor can notice the URL changing when the redirect occurs. Refer to <a href="/rules/url-forwarding/">Redirects</a> to learn more about configuring redirects.</p>
</li>
</ul>
<p>Use a URL rewrite rule to return the content of a URL while displaying a different URL in the browser. You can rewrite the URI path, the query string, or both.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13126.md")
</aside>
<h2 id="static-and-dynamic-rewrites">Static and dynamic rewrites</h2>
<p>URL Rewrite Rules can perform static or dynamic rewrites:</p>
<ul>
<li><strong>Static rewrite</strong>: Replaces a given part of a request URL (path or query string) with a static string.</li>
<li><strong>Dynamic rewrite</strong>: Supports more advanced scenarios where you use a <a href="/ruleset-engine/rules-language/">rewrite expression</a> (a formula based on request properties) to define the resulting path or query string.</li>
</ul>
<p>Create URL Rewrite Rules <a href="/rules/transform/url-rewrite/create-dashboard/">in the dashboard</a>, <a href="/rules/transform/url-rewrite/create-api/">via Cloudflare API</a>, or <a href="/terraform/additional-configurations/transform-rules/#create-a-url-rewrite-rule">using Terraform</a>.</p>
<h2 id="serve-images-from-custom-paths">Serve images from custom paths</h2>
<p>When using Cloudflare Images, you can use URL Rewrite Rules to serve images from a custom path. For more information, refer to <a href="/images/optimization/hosted-images/serve-from-custom-domains/">Serve images from custom domains</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting URL Rewrite Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>URL rewrite rules run in order, and later rules can overwrite changes done by previous rules.</p>
</li>
<li>
<p>The values of request and response fields are immutable within each <a href="/ruleset-engine/about/phases/">phase</a>, such as the <code>http_request_transform</code> phase where URL rewrite rules are defined. This means that later URL rewrite rules will still use the original field values when evaluating their filter expressions, not the values changed by previous rules. Refer to <a href="/ruleset-engine/about/rules/#field-values-during-rule-evaluation">Field values during rule evaluation</a> for more information.</p>
</li>
</ul>
