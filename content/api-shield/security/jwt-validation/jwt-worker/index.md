<p>Use a Worker to automatically keep your identity provider’s latest public key in the JWT validation configuration.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Find your zone ID. You can locate this ID in your zone overview in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Find your identity provider’s JSON Web Key Set (JWKs) URL. Identity providers commonly list it in Open Authorization (OAuth) settings.</li>
<li>Create a <a href="/api-shield/security/jwt-validation/#add-a-token-validation-configuration">token validation configuration</a>.</li>
<li><a href="https://dash.cloudflare.com/profile/api-tokens">Create a new API token</a> with the API Gateway <code>Write</code> permission.</li>
</ul>
<h2 id="process">Process</h2>
<p>You must manually query the JWKs endpoint to ensure the JWKs exists in the expected location and format. Then, create a Worker to automate updating of the JWKs and a <a href="/workers/configuration/secrets/#via-the-dashboard">Worker Secret</a> to house the API key used for updating API Shield settings. You can then schedule the Worker to automatically update the JWKs.</p>
<h3 id="manually-query-the-jwks-endpoint">Manually query the JWKs endpoint</h3>
<p>Find your Identity Provider’s URL and fetch the keys using <code>curl</code> and <code>jq</code>. Your URL may return more than just the issuer’s keys, so Cloudflare recommends using <code>jq</code> to filter the response to only return the keys. You must update the provided Worker sample code if your JWKs do not have a <code>keys</code> object.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3280.md")
</aside>
<pre><code class="language-sh">curl https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/certs -s | jq .keys&#10;</code></pre>
<pre><code class="language-sh">[&#10;  {&#10;    &quot;kid&quot;: &quot;ca96ae653935dbfb49b4e19de600cc5f9d5c63e3ac2dbee406ed4bf0ae100cce&quot;,&#10;    &quot;kty&quot;: &quot;RSA&quot;,&#10;    &quot;alg&quot;: &quot;RS256&quot;,&#10;    &quot;use&quot;: &quot;sig&quot;,&#10;    &quot;e&quot;: &quot;AQAB&quot;,&#10;    &quot;n&quot;: &quot;9dG9Ph4ffncvEA9FO9pVMfJ1dh_5mtuyiIE4ap9ScrufVPq1I34St_dhcFavKiytK7Id7gTlgQgaouoJ0I5OJ_bytgX-B7oOUQHO-nJOAMycORXN8ZNaMBPKg9nBLL_BFY0YX5HggqrkXkZjJ--R4JpB30ENS8A6hxmEJ__yGMZTE2LHZoiYj9iyGNu3s3JflAoRlmziI8LsFXwyFAJUWRZq4SkSfyrRJ89pXPxIqBn9uYBtnxWzUpWG3xKZu0JAbi9YiwFCJrSe_CarvpARoWsOldtrty5yT1yJ1PZlImlF-yuEwjOoZxeib4WSidABZH0O3pbDACo8MfxR5rghHQ&quot;&#10;  },&#10;  {&#10;    &quot;kid&quot;: &quot;1e590a6dcd60e3e2306c21eca19144c59d591531267a3ebde8d521f40894329d&quot;,&#10;    &quot;kty&quot;: &quot;RSA&quot;,&#10;    &quot;alg&quot;: &quot;RS256&quot;,&#10;    &quot;use&quot;: &quot;sig&quot;,&#10;    &quot;e&quot;: &quot;AQAB&quot;,&#10;    &quot;n&quot;: &quot;6uj6PgDq-bPsdFjiQ6M3yaxMxBUnnYj20xtLciHNafqrygAjnZKjl8LfCO_mtZ7jxfJNCARsz0L3sF9LAtARZqcsUvYLUlNDzflwNTe8woCT7yw0Ml2ZV5BWDbc3izEQnvjlBDGWv9p5jv-D-YNExtIzZKsRKyoy7hSu5FhyxmPfiAXo8b67f0dNy8V8HZfQJ5i9VGyK4Z5xKM-FjHOrC2uIbhzUE6wDe_0M23RTCxj7ZxzXUzZzc-_EBjmZDAI3tI2zBYymO55_gw8zHrNsZ4-32YvNTjBAiTLsjvKlsvNtPTN8q3saoZJWQMSiMi8dRalgA6pUDgcNs5lB9E7tWw&quot;&#10;  }&#10;]&#10;</code></pre>
<h3 id="configure-the-worker">Configure the Worker</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3281.md")
</div>
