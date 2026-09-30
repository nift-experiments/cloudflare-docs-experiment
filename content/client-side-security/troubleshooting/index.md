<h2 id="cloudflare-does-not-show-any-client-side-resources-after-activation">Cloudflare does not show any client-side resources after activation</h2>
<p>Cloudflare does not collect data on every single page view. Instead, it uses a sampling approach to gather information efficiently. This means that domains with lower traffic might take longer to generate initial reports, as these domains need more page views to accumulate enough samples. To speed up the reporting process, it is recommended that you actively generate traffic to your application after <a href="/client-side-security/get-started/">activating client-side resource monitoring</a>. This will provide Cloudflare with more data to work with, leading to faster report generation.</p>
<p>Other steps you can take to troubleshoot this issue:</p>
<ul>
<li>Verify that <a href="/client-side-security/get-started/#1-activate-client-side-resource-monitoring">client-side resource monitoring is turned on</a>.</li>
<li>After enabling client-side resource monitoring and generating some traffic to your application (at least 100 requests), wait approximately one hour to ensure that Cloudflare has already collected and processed enough data to display in the client-side resource monitoring dashboard.</li>
<li>Use your browser's dev tools (<strong>Network</strong> tab) to check if the <a href="/client-side-security/reference/csp-header/"><code>content-security-policy-report-only</code> HTTP header</a> is present.</li>
<li>Use analytics dashboards to verify if traffic is being proxied by Cloudflare.</li>
<li>Check if there are duplicate or conflicting Content Security Policy (CSP) headers in responses. Your origin server might be adding CSP headers to the response.</li>
</ul>
<h2 id="the-dashboard-shows-scripts-and-connections-that-i-do-not-recognize">The dashboard shows scripts and connections that I do not recognize</h2>
<p>Scripts often reference other scripts outside your application.</p>
<p>But, if you see unexpected scripts on your resource monitoring dashboard, check them for signs of malicious activity.</p>
<h2 id="i-get-warnings-in-my-browser-s-developer-tools-related-to-content-security-policy-csp">I get warnings in my browser's developer tools related to Content Security Policy (CSP)</h2>
<p>Cloudflare uses a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1337.md")
</div> report-only directive to gather a list of all scripts running on your application.
<p>Some browsers display scripts being reported as warnings in the console pane of their developer tools. For example:</p>
<pre><code class="language-txt">[Report Only] Refused to execute inline script because it violates&#10;the following Content Security Policy directive: &quot;script-src &#x27;none&#x27;&quot;.&#10;&#10;Either the &#x27;unsafe-inline&#x27; keyword, a hash (&#x27;sha256-RFWPLDbv2BY+rCkDzsE+0fr8ylGr2R2faWMhq4lfEQc=&#x27;), or a nonce (&#x27;nonce-...&#x27;)&#10;is required to enable inline execution.&#10;</code></pre>
<p>You can safely ignore these warnings, since they are related to the reports that Cloudflare requires to detect loaded scripts. For more information, refer to <a href="/client-side-security/how-it-works/">How client-side security works</a>.</p>
<h2 id="i-get-rule-violation-reports-for-a-domain-i-allowlisted">I get rule violation reports for a domain I allowlisted</h2>
<h3 id="redirects-to-other-domains">Redirects to other domains</h3>
<p>Rule violations reported via CSP's <a href="/client-side-security/reference/csp-header/">report-only directive</a> do not take into consideration any redirects or redirect HTTP status codes. This is <a href="https://www.w3.org/TR/CSP3/#create-violation-for-request">by design</a> for security reasons.</p>
<p>Some third-party services you may want to cover in your allow rules perform redirects. An example of such a service is Google Ads, which <a href="https://support.google.com/adsense/thread/102839782?hl=en&amp;msgid=103611259">does not work well with CSP policies</a>.</p>
<p>For example, if you add the <code>adservice.google.com</code> domain to an allow rule, you could get rule violation reports for this domain due to redirects to a different domain (not present in your allow rule). In this case, the violation report would still mention the original domain, and not the domain of the redirected destination, which can cause some confusion.</p>
<p>To try to solve this issue, add the domain of the redirected destination to your allow rule. You may need to add several domains to your rule due to redirects.</p>
<h3 id="ad-blocking-browser-extensions">Ad-blocking browser extensions</h3>
<p>If the violation reports reference domains that belong to user consent management or behavioral tracking services, an ad-blocking browser extension installed on the visitor's browser is a likely cause.</p>
<p>These extensions commonly block requests to such domains, often by redirecting them to a local resource instead of letting them reach the destination. Since the violation report mentions the original domain requested by the page, not this blocked or redirected destination, you may see violation reports for a domain you already allowlisted.</p>
<p>Because only visitors with these extensions installed trigger this behavior, the violation reports are sparse compared to your site's overall traffic volume.</p>
<h2 id="i-get-scoped-alerts-for-hostnames-i-do-not-manage-on-a-saas-root-zone">I get scoped alerts for hostnames I do not manage on a SaaS root zone</h2>
<p>If you operate an <a href="/cloudflare-for-platforms/cloudflare-for-saas/">SSL for SaaS</a> root zone with custom hostnames, and you configured a <a href="/client-side-security/alerts/#scoped-alerts">scoped alert</a> with a content security rule that uses the <code>'self'</code> keyword, you will receive alerts for resources detected across all custom hostnames served under your root zone, not only on your own application surfaces.</p>
<p>This is expected behavior:</p>
<ul>
<li>SSL for SaaS applies your root zone's content security rule to every custom hostname served under it.</li>
<li>The <code>'self'</code> keyword in a CSP directive matches the hostname of the request being served. When a custom hostname loads its own scripts, those scripts match <code>'self'</code> and the scoped alert fires.</li>
</ul>
<p>At SaaS scale, this can produce a high volume of alerts across hostnames you do not manage, and makes it difficult to isolate the scope of your own compliance audits (for example, the specific pages where you collect cardholder data).</p>
<p>There is currently no way to scope a content security rule to the root zone only, excluding custom hostnames. If you only need to monitor your own application surfaces, consider one of the following:</p>
<ul>
<li>Use a content security rule expression that matches only the specific page paths you control (for example, the request paths where you collect cardholder data).</li>
<li>Replace <code>'self'</code> with an explicit list of hostnames you control. Note that this is rarely feasible at SaaS scale because CSP headers have practical size limits.</li>
<li>If neither workaround fits, contact your account team to track interest in scoping content security rules to the SaaS root zone only.</li>
</ul>
<h2 id="my-rule-is-not-triggering-csp-header-not-added">My rule is not triggering (CSP header not added)</h2>
<p>If you have configured a content security rule but the expected CSP header is not being added to responses, <a href="/rules/transform/">Transform Rules</a> may be rewriting the request path before the content security rule is evaluated.</p>
<p>Cloudflare evaluates rules in a <a href="/ruleset-engine/reference/phases-list/">specific order</a> across different phases. <a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a> run early in the request lifecycle, while content security rules are evaluated later, during response phases.</p>
<p>This means that if your content security rule is matching incoming requests based on the request URI path (for example, using the field <code>http.request.uri.path</code>), the content security rule will evaluate against the rewritten path, not the original URI path requested by the visitor.</p>
<h3 id="solution">Solution</h3>
<p>To fix this issue, choose one of the following approaches:</p>
<ul>
<li>
<p><strong>Update the content security rule condition to match the rewritten path</strong>: Change your rule's expression to match the rewritten URI path instead of the original visitor's URI path.</p>
</li>
<li>
<p><strong>Use raw fields to match the original URI path</strong>: Use the <a href="/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.path/"><code>raw.http.request.uri.path</code></a> field instead of the <a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.path/"><code>http.request.uri.path</code></a> field in your content security rule expression. <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Raw+fields">Raw fields</a> preserve the original request values and are not affected by Transform Rules.</p>
</li>
</ul>
<p>When troubleshooting this issue, consider using <a href="/rules/trace-request/">Cloudflare Trace</a> to verify how the request path changes as it passes through different phases.</p>
<h2 id="responses-contain-duplicate-csp-headers">Responses contain duplicate CSP headers</h2>
<p>If responses have duplicate <code>Content-Security-Policy</code> or <code>Content-Security-Policy-Report-Only</code> headers, this is likely caused by having both client-side security and a <a href="/rules/transform/response-header-modification/">response header transform rule</a> adding the same header type.</p>
<p>Content security rules automatically add CSP headers to responses:</p>
<ul>
<li><a href="/client-side-security/rules/#rule-actions">Log rules</a> add <code>Content-Security-Policy-Report-Only</code> headers.</li>
<li><a href="/client-side-security/rules/#rule-actions">Allow rules</a> add <code>Content-Security-Policy</code> headers.</li>
</ul>
<p>If you have a response header transform rule configured with the <strong>Add</strong> operation for the same header type, both headers will be present in the response.</p>
<p>When browsers encounter multiple CSP headers, they enforce all of them, and the most restrictive policy wins. This can lead to unexpected blocking of legitimate resources.</p>
<h3 id="solution-1">Solution</h3>
<p>If you need to use Response Header Transform Rules alongside client-side security policies, use the <strong>Set static</strong> or <strong>Set dynamic</strong> operations. These operations replace any existing header value, including headers added by Cloudflare's client-side security. Using these operations will make your transform rule take precedence over client-side security.</p>
<p>Follow these steps to troubleshoot this issue:</p>
<ol>
<li>Use your browser's dev tools (<strong>Network</strong> tab) to inspect the response headers and check for duplicate CSP headers.</li>
<li>Review your configured <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> and check if any are using the <strong>Add</strong> operation for <code>Content-Security-Policy</code> or <code>Content-Security-Policy-Report-Only</code> headers.</li>
<li>Change the operation from <strong>Add</strong> to <strong>Set static</strong> or <strong>Set dynamic</strong> if you want the transform rule to override client-side security's CSP headers.</li>
<li>Alternatively, disable or adjust the content security rule scope to avoid overlap with your transform rule.</li>
</ol>
<h3 id="recommended-patterns">Recommended patterns</h3>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Recommended approach</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client-side security manages all CSP headers</td>
<td>Do not create Response Header Transform Rules for CSP headers.</td>
</tr>
<tr>
<td>Transform Rule manages all CSP headers</td>
<td>Use <strong>Set static</strong> or <strong>Set dynamic</strong> operations, and consider excluding the affected paths from your content security rule.</td>
</tr>
<tr>
<td>Different CSP headers for different paths</td>
<td>Use content security rule conditions to target specific paths, and avoid overlapping Transform Rules.</td>
</tr>
</tbody>
</table>
