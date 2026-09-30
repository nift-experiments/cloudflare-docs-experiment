<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15652.md")
</aside>
<p>WAF rules can include a check for exposed credentials. When enabled in a given rule, exposed credentials checking happens when there is a match for the rule expression (that is, the rule expression evaluates to <code>true</code>).</p>
<p>At this point, the WAF looks up the username/password pair in the request against a database of publicly available stolen credentials. When both the rule expression and the exposed credentials check are true, there is a rule match, and Cloudflare performs the action configured in the rule.</p>
<h2 id="example">Example</h2>
<p>For example, the following rule matches <code>POST</code> requests to the <code>/login.php</code> URI when Cloudflare identifies the submitted credentials as previously exposed:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/15653.md")
</div>
<p>When there is a match for the rule above and Cloudflare detects exposed credentials, the WAF presents the user with a challenge.</p>
