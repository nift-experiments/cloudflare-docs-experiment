<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15470.md")
</aside>
<p>This example configures additional protection for requests with a JSON Web Token (JWT) with a user claim of <code>admin</code>, based on the request's <a href="/waf/detections/attack-score/">attack score</a>.</p>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> that issues a Managed Challenge if the user claim in a JWT is <code>admin</code> and the attack score is below 40.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong></p>
<p>Use the expression editor:<br/>
<code>(lookup_json_string(http.request.jwt.claims[&quot;&lt;TOKEN_CONFIGURATION_ID&gt;&quot;][0], &quot;user&quot;) eq &quot;admin&quot; and cf.waf.score &lt; 40)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Managed Challenge</em></p>
</li>
</ul>
<p>In this example, <code>&lt;TOKEN_CONFIGURATION_ID&gt;</code> is your <a href="/api-shield/security/jwt-validation/api/">token configuration ID</a> found in JWT Validation and <code>user</code> is the JWT claim.</p>
