<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15649.md")
</aside>
<p>Many web applications have suffered <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15650.md")
</div> attacks in the recent past. In these attacks there is a massive number of login attempts using username/password pairs from databases of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/15651.md")
</div>.
<p>Cloudflare offers you automated checks for exposed credentials using Cloudflare Web Application Firewall (WAF).</p>
<p>The WAF provides two mechanisms for this check:</p>
<ul>
<li>
<p>The <a href="/waf/managed-rules/reference/exposed-credentials-check/">Exposed Credentials Check Managed Ruleset</a>, which contains predefined rules for popular CMS applications. By enabling this ruleset for a given zone, you immediately enable checks for exposed credentials for these well-known applications. The managed ruleset is available to all paid plans.</p>
</li>
<li>
<p>The ability to <a href="#exposed-credentials-checks-in-custom-rules">write custom rules</a> at the account level that check for exposed credentials according to your criteria. This configuration option is available to Enterprise customers with a paid add-on.</p>
</li>
</ul>
<p>Cloudflare updates the databases of exposed credentials supporting the exposed credentials check feature on a regular basis.</p>
<p>The username and password credentials in clear text never leave the Cloudflare network. The WAF only uses an anonymized version of the username and password when determining if there are previously exposed credentials. Cloudflare follows the approach based on the <em>k</em>-Anonymity mathematical property described in the following blog post: <a href="https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/">Validating Leaked Passwords with k-Anonymity</a>.</p>
<h2 id="available-actions">Available actions</h2>
<p>The WAF can perform one of the following actions when it detects exposed credentials:</p>
<ul>
<li><strong>Exposed-Credential-Check Header</strong>: Adds a new HTTP header to HTTP requests with exposed credentials. Your application at the origin can then force a password reset, start a two-factor authentication process, or perform any other action. The name of the added HTTP header is <code>Exposed-Credential-Check</code> and its value is <code>1</code>. The action name is <code>Rewrite</code> in <a href="/waf/analytics/security-events/">Security Events</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15648.md")
</aside>
<ul>
<li><strong>Non-Interactive Challenge</strong>: Presents a non-interactive challenge to the clients making HTTP requests with exposed credentials.</li>
<li><strong>Managed Challenge</strong>: Helps reduce the lifetimes of human time spent solving CAPTCHAs across the Internet. Depending on the characteristics of a request, Cloudflare will dynamically choose the appropriate type of challenge based on specific criteria.</li>
<li><strong>Block</strong>: Blocks HTTP requests containing exposed credentials.</li>
<li><strong>Log</strong>: Only available on Enterprise plans. Logs requests with exposed credentials in the Cloudflare logs. Recommended for validating a rule before committing to a more severe action.</li>
<li><strong>Interactive Challenge</strong>: Presents an interactive challenge to the clients making HTTP requests with exposed credentials.</li>
</ul>
<p>The default action for the rules in the Exposed Credentials Check Managed Ruleset is <em>Exposed-Credential-Check Header</em> (named <code>rewrite</code> in the API).</p>
<p>Cloudflare recommends that you only use the following actions: <em>Exposed-Credential-Check Header</em> (named <code>rewrite</code> in the API) and <em>Log</em> (<code>log</code>).</p>
<h2 id="exposed-credentials-checks-in-custom-rules">Exposed credentials checks in custom rules</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15647.md")
</aside>
<p>Besides enabling the <a href="/waf/managed-rules/reference/exposed-credentials-check/">Exposed Credentials Check Managed Ruleset</a>, you can also check for exposed credentials in <a href="/waf/custom-rules/">custom rules</a>. One common use case is to create custom rules on the end user authentication endpoints of your application to check for exposed credentials. Rules that check for exposed credentials run before rate limiting rules.</p>
<p>To check for exposed credentials in a custom rule, include the exposed credentials check in the rule definition at the account level and specify how to obtain the username and password values from the HTTP request. For more information, refer to <a href="/waf/managed-rules/check-for-exposed-credentials/configure-api/#create-a-custom-rule-checking-for-exposed-credentials">Create a custom rule checking for exposed credentials</a>.</p>
