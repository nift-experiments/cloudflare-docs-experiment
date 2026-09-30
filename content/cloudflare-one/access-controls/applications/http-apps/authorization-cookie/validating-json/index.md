---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/
  description: Validate JWTs in Access.
  full_title: Validate JWTs · Cloudflare One docs
  head_html: <title>Validate JWTs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Validate JWTs in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/index.md"><meta property="og:title" content="Validate JWTs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Validate JWTs in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="JSON web token (JWT)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#page","headline":"Validate JWTs \u00b7 Cloudflare One docs","description":"Validate JWTs in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON web token (JWT)"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/
  schema: 1
---
<p>When Cloudflare sends a request to your origin, the request will include an <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a> as a <code>Cf-Access-Jwt-Assertion</code> request header. Requests made through a browser will also pass the token as a <code>CF_Authorization</code> cookie.</p>
<p>Cloudflare signs the token with a key pair unique to your account. You should validate the token with your public key to ensure that the request came from Access and not a malicious third party. We recommend validating the <code>Cf-Access-Jwt-Assertion</code> header instead of the <code>CF_Authorization</code> cookie, since the cookie is not guaranteed to be passed.</p>
<h2 id="access-signing-keys">Access signing keys</h2>
<p>The public key for the signing key pair is located at <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/certs</code>, where <code>&lt;your-team-name&gt;</code> is your Cloudflare One <span class="nb-glossary-tooltip" title="team name">team name</span>.</p>
<p>By default, Access rotates the signing key every 6 weeks. This means you will need to programmatically or manually update your keys as they rotate. Previous keys remain valid for 7 days after rotation to allow time for you to make the update.</p>
<p>You can also manually rotate the key using the <a href="/api/resources/zero_trust/subresources/access/subresources/keys/methods/rotate/">API</a>. This can be done for testing or security purposes.</p>
<p>As shown in the example below, <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/certs</code> contains two public keys: the current key used to sign all new tokens, and the previous key that has been rotated out.</p>
<ul>
<li><code>keys</code>: both keys in JWK format</li>
<li><code>public_cert</code>: current key in PEM format</li>
<li><code>public_certs</code>: both keys in PEM format</li>
</ul>
<pre tabindex="0"><code class="language-txt">{&#10;  &quot;keys&quot;: [&#10;    {&#10;      &quot;kid&quot;: &quot;1a1c3986a44ce6390be42ec772b031df8f433fdc71716db821dc0c39af3bce49&quot;,&#10;      &quot;kty&quot;: &quot;RSA&quot;,&#10;      &quot;alg&quot;: &quot;RS256&quot;,&#10;      &quot;use&quot;: &quot;sig&quot;,&#10;      &quot;e&quot;: &quot;AQAB&quot;,&#10;      &quot;n&quot;: &quot;5PKw-...-AG7MyQ&quot;&#10;    },&#10;    {&#10;      &quot;kid&quot;: &quot;6c3bffef71bb0a90c9cbef3b7c0d4a1c7b4b8b76b80292a623afd9dac45d1c65&quot;,&#10;      &quot;kty&quot;: &quot;RSA&quot;,&#10;      &quot;alg&quot;: &quot;RS256&quot;,&#10;      &quot;use&quot;: &quot;sig&quot;,&#10;      &quot;e&quot;: &quot;AQAB&quot;,&#10;      &quot;n&quot;: &quot;pwVn...AA6Hw&quot;&#10;    }&#10;  ],&#10;  &quot;public_cert&quot;: {&#10;    &quot;kid&quot;: &quot;6c3bffef71bb0a90c9cbef3b7c0d4a1c7b4b8b76b80292a623afd9dac45d1c65&quot;,&#10;    &quot;cert&quot;: &quot;-----BEGIN CERTIFICATE----- ... -----END CERTIFICATE----- &quot;&#10;  },&#10;  &quot;public_certs&quot;: [&#10;    {&#10;      &quot;kid&quot;: &quot;1a1c3986a44ce6390be42ec772b031df8f433fdc71716db821dc0c39af3bce49&quot;,&#10;      &quot;cert&quot;: &quot;-----BEGIN CERTIFICATE----- ... -----END CERTIFICATE----- &quot;&#10;    },&#10;    {&#10;      &quot;kid&quot;: &quot;6c3bffef71bb0a90c9cbef3b7c0d4a1c7b4b8b76b80292a623afd9dac45d1c65&quot;,&#10;      &quot;cert&quot;: &quot;-----BEGIN CERTIFICATE----- ... -----END CERTIFICATE----- &quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="avoid-key-rotation-issues">Avoid key rotation issues</h3>
@markup("md", "content/.markup/bodies/4873.md")
</aside>
<h2 id="verify-the-jwt-manually">Verify the JWT manually</h2>
<p>To verify the token manually:</p>
<ol>
<li>
<p>Copy the JWT from the <code>Cf-Access-Jwt-Assertion</code> request header.</p>
</li>
<li>
<p>Go to <a href="https://jwt.io/">jwt.io</a>.</p>
</li>
<li>
<p>Select the RS256 algorithm.</p>
</li>
<li>
<p>Paste the JWT into the <strong>Encoded</strong> box.</p>
</li>
<li>
<p>In the <strong>Payload</strong> box, ensure that the <code>iss</code> field points to your team domain (<code>https://&lt;your-team-name&gt;.cloudflareaccess.com</code>). <code>jwt.io</code> uses the <code>iss</code> value to fetch the public key for token validation.</p>
</li>
<li>
<p>Ensure that the page says <strong>Signature Verified</strong>.</p>
</li>
</ol>
<p>You can now trust that this request was sent by Access.</p>
<h2 id="programmatic-verification">Programmatic verification</h2>
<p>You can run an automated script on your origin server to validate incoming requests. The provided sample code gets the application token from a request and checks its signature against your public key. You will need to insert your own team domain and Application Audience (AUD) tag into the sample code.</p>
<h3 id="get-your-aud-tag">Get your AUD tag</h3>
<p>Cloudflare Access assigns a unique AUD tag to each application. The <code>aud</code> claim in the token payload specifies which application the JWT is valid for.</p>
<p>To get the AUD tag:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Configure</strong> for your application.</li>
<li>From <strong>Additional settings</strong>, copy the <strong>Application Audience (AUD) Tag</strong>.</li>
</ol>
<p>You can now paste the AUD tag into your token validation script. The AUD tag will never change unless you delete or recreate the Access application.</p>
<h3 id="cloudflare-workers-example">Cloudflare Workers example</h3>
<p>When Cloudflare Access is in front of your <a href="/workers">Worker</a>, your Worker still needs to validate the JWT that Cloudflare Access adds to the <code>Cf-Access-Jwt-Assertion</code> header on the incoming request.</p>
<p>The following code will validate the JWT using the <a href="https://www.npmjs.com/package/jose">jose NPM package</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4875.md")
</div>
<h4 id="required-environment-variables">Required environment variables</h4>
<p>Add these <a href="/workers/configuration/environment-variables/">environment variables</a> to your Worker:
- <code>POLICY_AUD</code>: Your application's <a href="#get-your-aud-tag">AUD tag</a>
- <code>TEAM_DOMAIN</code>: <code>https://&lt;your-team-name&gt;.cloudflareaccess.com</code>, where <code>&lt;your-team-name&gt;</code> is replaced with your actual <span class="nb-glossary-tooltip" title="team name">team name</span>.</p>
<p>You can set these variables by adding them to your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, or via the Cloudflare dashboard under <strong>Workers &amp; Pages</strong> &gt; <strong>your-worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment Variables</strong>.</p>
<h3 id="golang-example">Golang example</h3>
<pre tabindex="0"><code class="language-go">package main&#10;&#10;import (&#10;    &quot;context&quot;&#10;    &quot;fmt&quot;&#10;    &quot;net/http&quot;&#10;&#10;    &quot;github.com/coreos/go-oidc/v3/oidc&quot;&#10;)&#10;&#10;var (&#10;    ctx        = context.TODO()&#10;    teamDomain = &quot;https://test.cloudflareaccess.com&quot;&#10;    certsURL   = fmt.Sprintf(&quot;%s/cdn-cgi/access/certs&quot;, teamDomain)&#10;&#10;    // The Application Audience (AUD) tag for your application&#10;    policyAUD = &quot;4714c1358e65fe4b408ad6d432a5f878f08194bdb4752441fd56faefa9b2b6f2&quot;&#10;&#10;    config = &amp;oidc.Config{&#10;        ClientID: policyAUD,&#10;    }&#10;    keySet   = oidc.NewRemoteKeySet(ctx, certsURL)&#10;    verifier = oidc.NewVerifier(teamDomain, keySet, config)&#10;)&#10;&#10;// VerifyToken is a middleware to verify a CF Access token&#10;func VerifyToken(next http.Handler) http.Handler {&#10;    fn := func(w http.ResponseWriter, r *http.Request) {&#10;        headers := r.Header&#10;&#10;        // Make sure that the incoming request has our token header&#10;        //  Could also look in the cookies for CF_AUTHORIZATION&#10;        accessJWT := headers.Get(&quot;Cf-Access-Jwt-Assertion&quot;)&#10;        if accessJWT == &quot;&quot; {&#10;            w.WriteHeader(http.StatusUnauthorized)&#10;            w.Write([]byte(&quot;No token on the request&quot;))&#10;            return&#10;        }&#10;&#10;        // Verify the access token&#10;        ctx := r.Context()&#10;        _, err := verifier.Verify(ctx, accessJWT)&#10;        if err != nil {&#10;            w.WriteHeader(http.StatusUnauthorized)&#10;            w.Write([]byte(fmt.Sprintf(&quot;Invalid token: %s&quot;, err.Error())))&#10;            return&#10;        }&#10;        next.ServeHTTP(w, r)&#10;    }&#10;    return http.HandlerFunc(fn)&#10;}&#10;&#10;func MainHandler() http.Handler {&#10;    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {&#10;        w.Write([]byte(&quot;welcome&quot;))&#10;    })&#10;}&#10;&#10;func main() {&#10;    http.Handle(&quot;/&quot;, VerifyToken(MainHandler()))&#10;    http.ListenAndServe(&quot;:3000&quot;, nil)&#10;}&#10;</code></pre>
<h3 id="python-example">Python example</h3>
<p><code>pip</code> install the following:</p>
<ul>
<li>flask</li>
<li>requests</li>
<li>PyJWT</li>
<li>cryptography</li>
</ul>
<pre tabindex="0"><code class="language-python">from flask import Flask, request&#10;import requests&#10;import jwt&#10;import json&#10;import os&#10;app = Flask(__name__)&#10;&#10;&#10;&#35; The Application Audience (AUD) tag for your application&#10;POLICY_AUD = os.getenv(&quot;POLICY_AUD&quot;)&#10;&#10;&#35; Your CF Access team domain&#10;TEAM_DOMAIN = os.getenv(&quot;TEAM_DOMAIN&quot;)&#10;CERTS_URL = &quot;{}/cdn-cgi/access/certs&quot;.format(TEAM_DOMAIN)&#10;&#10;def _get_public_keys():&#10;    &quot;&quot;&quot;&#10;    Returns:&#10;        List of RSA public keys usable by PyJWT.&#10;    &quot;&quot;&quot;&#10;    r = requests.get(CERTS_URL)&#10;    public_keys = []&#10;    jwk_set = r.json()&#10;    for key_dict in jwk_set[&#x27;keys&#x27;]:&#10;        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key_dict))&#10;        public_keys.append(public_key)&#10;    return public_keys&#10;&#10;def verify_token(f):&#10;    &quot;&quot;&quot;&#10;    Decorator that wraps a Flask API call to verify the CF Access JWT&#10;    &quot;&quot;&quot;&#10;    def wrapper():&#10;				&#35; Check for the POLICY_AUD environment variable&#10;				if not POLICY_AUD:&#10;					return &quot;missing required audience&quot;, 403&#10;&#10;        token = &#x27;&#x27;&#10;        if &#x27;CF_Authorization&#x27; in request.cookies:&#10;            token = request.cookies[&#x27;CF_Authorization&#x27;]&#10;        else:&#10;            return &quot;missing required cf authorization token&quot;, 403&#10;        keys = _get_public_keys()&#10;&#10;        &#35; Loop through the keys since we can&#x27;t pass the key set to the decoder&#10;        valid_token = False&#10;        for key in keys:&#10;            try:&#10;                &#35; decode returns the claims that has the email when needed&#10;                jwt.decode(token, key=key, audience=POLICY_AUD, algorithms=[&#x27;RS256&#x27;])&#10;                valid_token = True&#10;                break&#10;            except:&#10;                pass&#10;        if not valid_token:&#10;            return &quot;invalid token&quot;, 403&#10;&#10;        return f()&#10;    return wrapper&#10;&#10;&#10;@app.route(&#x27;/&#x27;)&#10;@verify_token&#10;def hello_world():&#10;    return &#x27;Hello, World!&#x27;&#10;&#10;&#10;if __name__ == &#x27;__main__&#x27;:&#10;    app.run()&#10;</code></pre>
<h3 id="javascript-node-js-example">JavaScript (Node.js) example</h3>
<pre tabindex="0"><code class="language-javascript">const express = require(&quot;express&quot;);&#10;const jose = require(&quot;jose&quot;);&#10;&#10;// The Application Audience (AUD) tag for your application&#10;const AUD = process.env.POLICY_AUD;&#10;&#10;// Your CF Access team domain&#10;const TEAM_DOMAIN = process.env.TEAM_DOMAIN;&#10;const CERTS_URL = `${TEAM_DOMAIN}/cdn-cgi/access/certs`;&#10;&#10;const JWKS = jose.createRemoteJWKSet(new URL(CERTS_URL));&#10;&#10;// verifyToken is a middleware to verify a CF authorization token&#10;const verifyToken = async (req, res, next) =&gt; {&#10;	// Check for the AUD environment variable&#10;	if (!AUD) {&#10;		return res.status(403).send({&#10;			status: false,&#10;			message: &quot;missing required audience&quot;,&#10;		});&#10;	}&#10;&#10;	const token = req.headers[&quot;cf-access-jwt-assertion&quot;];&#10;&#10;	// Make sure that the incoming request has our token header&#10;	if (!token) {&#10;		return res.status(403).send({&#10;			status: false,&#10;			message: &quot;missing required cf authorization token&quot;,&#10;		});&#10;	}&#10;&#10;	try {&#10;		const result = await jose.jwtVerify(token, JWKS, {&#10;			issuer: TEAM_DOMAIN,&#10;			audience: AUD,&#10;		});&#10;&#10;		req.user = result.payload;&#10;		next();&#10;	} catch (err) {&#10;		return res.status(403).send({&#10;			status: false,&#10;			message: &quot;invalid token&quot;,&#10;		});&#10;	}&#10;};&#10;&#10;const app = express();&#10;&#10;app.use(verifyToken);&#10;&#10;app.get(&quot;/&quot;, (req, res) =&gt; {&#10;	res.send(&quot;Hello World!&quot;);&#10;});&#10;&#10;app.listen(3333);&#10;</code></pre>
