<h1 id="http-request-jwt-claims-aud">http.request.jwt.claims.aud</h1>

**Data type:** Map<Array<String>>

<p>The <code>aud</code> (audience) claim identifies the recipients that the JSON Web Token (JWT) is intended for.</p>

<p>Each principal intended to process the JWT must identify itself with a value in the audience claim. In the general case, the <code>aud</code> value is an array of case-sensitive strings, each containing a <code>StringOrURI</code> value. For details, refer to the <a href="https://datatracker.ietf.org/doc/html/rfc7519#section-4.1">Registered Claim Names</a> in RFC 7519.</p>
<p>Requires a Cloudflare Enterprise plan with a paid add-on.</p>
<p>For more information on validating JSON Web Tokens, refer to <a href="/api-shield/security/jwt-validation/">JSON Web Tokens Validation</a> in the API Shield documentation.</p>

<h2 id="categories">Categories</h2>

- Request
- JWT validation

**Keywords:** request, jwt, api shield, client, visitor

