<p>You can forward information from a <a href="/api-shield/security/jwt-validation/">JSON Web Token (JWT)</a> to the origin in a header by creating <a href="/rules/transform/">Transform Rules</a> using claims that Cloudflare has verified via the JSON Web Token.</p>
<p>Claims are available through the <code>http.request.jwt.claims</code> firewall fields.</p>
<p>For example, the following expression will extract the user claim from a token processed by the token configuration with <code>TOKEN_CONFIGURATION_ID</code>:</p>
<pre><code class="language-txt">lookup_json_string(http.request.jwt.claims[&quot;&lt;TOKEN_CONFIGURATION_ID&gt;&quot;][0], &quot;claim_name&quot;)&#10;</code></pre>
<p>Refer to <a href="/api-shield/security/jwt-validation/api/">Configure JWT validation</a> for more information about creating a token configuration.</p>
<h2 id="create-a-transform-rule">Create a Transform Rule</h2>
<p>As an example, to send the <code>x-send-jwt-claim-user</code> request header to the origin, you must create a Transform Rule:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3278.md")
</div>
