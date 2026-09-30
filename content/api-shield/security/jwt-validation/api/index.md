---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/jwt-validation/api/
  description: Configure JWT validation and act on its results using the Cloudflare API.
  full_title: Configure JWT validation via the API · Cloudflare API Shield docs
  head_html: <title>Configure JWT validation via the API · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure JWT validation and act on its results using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/jwt-validation/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/jwt-validation/api/index.md"><meta property="og:title" content="Configure JWT validation via the API · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure JWT validation and act on its results using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/jwt-validation/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="API Shield"><meta name="pcx_tags" content="JSON web token (JWT)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/jwt-validation/api/#page","headline":"Configure JWT validation via the API \u00b7 Cloudflare API Shield docs","description":"Configure JWT validation and act on its results using the Cloudflare API.","url":"https://developers.cloudflare.com/api-shield/security/jwt-validation/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON web token (JWT)"]}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/jwt-validation/api/
  schema: 1
---
<p>Use the Cloudflare API to configure <a href="/api-shield/security/jwt-validation/">JWT validation</a>. A token configuration defines how Cloudflare finds and validates JWTs. You then use a WAF custom rule or a token validation rule to <a href="#act-on-validation-results">act on the results</a>.</p>
<h2 id="token-configurations">Token configurations</h2>
<p>A token configuration defines the JSON Web Key Set (JWKS) used to validate JSON Web Tokens (JWTs). It also defines where Cloudflare finds JWTs in requests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3294.md")
</aside>
<p>Token configurations require the following information:</p>
<table>
<thead>
<tr>
<th><span style="width:120px">Field name</span></th>
<th>Description</th>
<th>Example</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>title</code></td>
<td>A human-readable name for the configuration that allows you to quickly identify the purpose of the configuration.</td>
<td>Production JWT configuration</td>
<td>Limited to 50 characters.</td>
</tr>
<tr>
<td><code>description </code></td>
<td>A human-readable description that gives more details than <code>title</code> which serves as a means to allow customers to better document the use of the configuration.</td>
<td>This configuration checks the JWT in the authorization header.</td>
<td>Limited to 500 characters.</td>
</tr>
<tr>
<td><code>token_sources</code></td>
<td>A list of possible locations where then JWT can be found on the request.</td>
<td><code>http.request.headers[\&quot;authorization\&quot;][0]</code> <br /> <code>http.request.cookies[\&quot;Authorization\&quot;][0]</code></td>
<td>Refer to the <a href="#token-sources">information</a> below.</td>
</tr>
<tr>
<td><code>token_type</code></td>
<td>This specifies the type of token to validate.</td>
<td><code>jwt</code></td>
<td>Only <code>jwt</code> is currently supported.</td>
</tr>
<tr>
<td><code>credentials</code></td>
<td>This describes the cryptographic keys that should be used to validate JWTs. Each key must be a JSON Web Key (JWK).</td>
<td>Refer to the example below.</td>
<td>Refer to the <a href="#credentials">information</a> below.</td>
</tr>
</tbody>
</table>
<h3 id="token-sources">Token sources</h3>
<p>Each item must be a Ruleset Engine expression that resolves to a string.</p>
<p>Currently supported fields are <code>http.request.headers</code> and <code>http.request.cookies</code>.</p>
<p>You can set up to four token sources. If a request has more than one of these fields set, only one will be used. Leading <code>Bearer: </code> strings in request tokens are automatically ignored.</p>
<p>Refer to the <a href="/ruleset-engine/rules-language/fields">Ruleset Engine documentation</a> for details on working with Ruleset Engine fields.</p>
<h3 id="credentials">Credentials</h3>
<p>API Shield supports asymmetric RSA and elliptic curve keys and symmetric hash-based message authentication code (HMAC) keys:</p>
<table>
<thead>
<tr>
<th>Key type</th>
<th>Supported algorithms</th>
<th>Requirements</th>
</tr>
</thead>
<tbody>
<tr>
<td>RSA</td>
<td><code>RS256</code>, <code>RS384</code>, <code>RS512</code>, <code>PS256</code>, <code>PS384</code>, and <code>PS512</code></td>
<td>RSA keys must be at least 2,048 bits.</td>
</tr>
<tr>
<td>EC</td>
<td><code>ES256</code> and <code>ES384</code></td>
<td>Use curve <code>P-256</code> with <code>ES256</code> and curve <code>P-384</code> with <code>ES384</code>.</td>
</tr>
<tr>
<td>HMAC</td>
<td><code>HS256</code>, <code>HS384</code>, and <code>HS512</code></td>
<td>Use a symmetric secret of at least 32, 48, or 64 bytes, respectively.</td>
</tr>
</tbody>
</table>
<p>Each JWK must have an <code>alg</code> and a <code>kid</code>. The JWT header must contain matching <code>alg</code> and <code>kid</code> values so API Shield can select the correct key.</p>
<p>Provide an <code>alg</code> value for every JWK. The effective algorithm, whether provided or defaulted, must match the <code>alg</code> value in the JWT header. HMAC keys must always specify <code>alg</code>.</p>
<p>For compatibility with identity providers that omit <code>alg</code>, API Shield defaults an RSA key without <code>alg</code> to <code>RS256</code>. RSA key size does not identify which signing algorithm an identity provider uses. Specify <code>alg</code> explicitly if the identity provider uses another supported algorithm.</p>
<p>For an HMAC key, set <code>kty</code> to <code>oct</code>. Set <code>k</code> to the raw symmetric credential encoded with unpadded Base64url. The decoded credential must meet the minimum length for its algorithm.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3293.md")
</aside>
<p>Cloudflare will remove any fields that are unnecessary from each key and will drop keys that we do not support.</p>
<p>It is highly recommended to validate the output of the API call to check that the resulting keys appear as intended.</p>
<h2 id="token-configuration-json-object">Token configuration JSON object</h2>
<p>The example below shows a JSON object with all of the information necessary to create a token configuration using the Cloudflare API. If you would like to create JWKs for testing, refer to <a href="https://mkjwk.org/">mkjwk JSON Web Key Generator</a>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;title&quot;: &quot;Production JWT configuration&quot;,&#10;	&quot;description&quot;: &quot;This configuration checks the JWT in the authorization header or cookie.&quot;,&#10;	&quot;token_sources&quot;: [&#10;		&quot;http.request.headers[\&quot;authorization\&quot;][0]&quot;,&#10;		&quot;http.request.cookies[\&quot;Authorization\&quot;][0]&quot;&#10;	],&#10;	&quot;token_type&quot;: &quot;jwt&quot;,&#10;	&quot;credentials&quot;: {&#10;		&quot;keys&quot;: [&#10;			{&#10;				&quot;kty&quot;: &quot;EC&quot;,&#10;				&quot;use&quot;: &quot;sig&quot;,&#10;				&quot;crv&quot;: &quot;P-256&quot;,&#10;				&quot;kid&quot;: &quot;93UrzmNu1mqXs5cZcvCPkTlMHB2Jya30vSTkiBb0vhU&quot;,&#10;				&quot;x&quot;: &quot;QG3VFVwUX4IatQvBy7sqBvvmticCZ-eX5-nbtGKBOfI&quot;,&#10;				&quot;y&quot;: &quot;A3PXCshn7XcG7Ivvd2K_DerW4LHAlIVKdqhrUnczTD0&quot;,&#10;				&quot;alg&quot;: &quot;ES256&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<h3 id="symmetric-key-example">Symmetric key example</h3>
<p>The following example configures JWT validation with an <code>HS256</code> symmetric key. Replace <code>&lt;BASE64URL_ENCODED_SECRET&gt;</code> with an unpadded Base64url-encoded credential containing at least 32 decoded bytes.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;title&quot;: &quot;Production HMAC JWT configuration&quot;,&#10;	&quot;description&quot;: &quot;This configuration checks the JWT in the authorization header.&quot;,&#10;	&quot;token_sources&quot;: [&quot;http.request.headers[\&quot;authorization\&quot;][0]&quot;],&#10;	&quot;token_type&quot;: &quot;jwt&quot;,&#10;	&quot;credentials&quot;: {&#10;		&quot;keys&quot;: [&#10;			{&#10;				&quot;kty&quot;: &quot;oct&quot;,&#10;				&quot;alg&quot;: &quot;HS256&quot;,&#10;				&quot;kid&quot;: &quot;production-hmac-key&quot;,&#10;				&quot;k&quot;: &quot;&lt;BASE64URL_ENCODED_SECRET&gt;&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<p>The response includes <code>kty</code>, <code>alg</code>, and <code>kid</code>, but does not include <code>k</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;credentials&quot;: {&#10;		&quot;keys&quot;: [&#10;			{&#10;				&quot;kty&quot;: &quot;oct&quot;,&#10;				&quot;alg&quot;: &quot;HS256&quot;,&#10;				&quot;kid&quot;: &quot;production-hmac-key&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<h2 id="create-a-token-configuration-using-the-cloudflare-api">Create a token configuration using the Cloudflare API</h2>
<p>Use cURL or any other API client tool to send the new configuration to Cloudflare’s API to enable JWT validation. Make sure to replace <code>{zone_id}</code> with the relevant zone ID and add your <a href="/fundamentals/api/get-started/create-token/">authentication credentials</a> header.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/config&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;    &quot;title&quot;: &quot;Production JWT configuration&quot;,&#10;    &quot;description&quot;: &quot;This configuration checks the JWT in the authorization header or cookie.&quot;,&#10;    &quot;token_sources&quot;: [&#10;        &quot;http.request.headers[\&quot;authorization\&quot;][0]&quot;,&#10;        &quot;http.request.cookies[\&quot;Authorization\&quot;][0]&quot;&#10;    ],&#10;    &quot;token_type&quot;: &quot;jwt&quot;,&#10;    &quot;credentials&quot;: {&#10;        &quot;keys&quot;: [&#10;            {&#10;                &quot;kty&quot;: &quot;EC&quot;,&#10;                &quot;use&quot;: &quot;sig&quot;,&#10;                &quot;crv&quot;: &quot;P-256&quot;,&#10;                &quot;kid&quot;: &quot;93UrzmNu1mqXs5cZcvCPkTlMHB2Jya30vSTkiBb0vhU&quot;,&#10;                &quot;x&quot;: &quot;QG3VFVwUX4IatQvBy7sqBvvmticCZ-eX5-nbtGKBOfI&quot;,&#10;                &quot;y&quot;: &quot;A3PXCshn7XcG7Ivvd2K_DerW4LHAlIVKdqhrUnczTD0&quot;,&#10;                &quot;alg&quot;: &quot;ES256&quot;&#10;            }&#10;        ]&#10;    }&#10;}&#x27;&#10;</code></pre>
<p>The response will be in a Cloudflare <code>v4</code> response envelope and the result contains the created configuration. Note the returned ID. You can use it to reference the token configuration in JWT claim fields or token validation rules.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;d5902294-00c3-4aed-b517-57e752e9cd58&quot;,&#10;		&quot;token_type&quot;: &quot;JWT&quot;,&#10;		&quot;title&quot;: &quot;Production JWT configuration&quot;,&#10;		&quot;description&quot;: &quot;This configuration checks the JWT in the authorization header or cookie.&quot;,&#10;		&quot;token_sources&quot;: [&#10;			&quot;http.request.headers[\&quot;authorization\&quot;][0]&quot;,&#10;			&quot;http.request.cookies[\&quot;Authorization\&quot;][0]&quot;&#10;		],&#10;		&quot;credentials&quot;: {&#10;			&quot;keys&quot;: [&#10;				{&#10;					&quot;x&quot;: &quot;QG3VFVwUX4IatQvBy7sqBvvmticCZ-eX5-nbtGKBOfI&quot;,&#10;					&quot;y&quot;: &quot;A3PXCshn7XcG7Ivvd2K_DerW4LHAlIVKdqhrUnczTD0&quot;,&#10;					&quot;alg&quot;: &quot;ES256&quot;,&#10;					&quot;crv&quot;: &quot;P-256&quot;,&#10;					&quot;kid&quot;: &quot;93UrzmNu1mqXs5cZcvCPkTlMHB2Jya30vSTkiBb0vhU&quot;,&#10;					&quot;kty&quot;: &quot;EC&quot;&#10;				}&#10;			]&#10;		},&#10;		&quot;created_at&quot;: &quot;2023-11-08T16:45:17.236841Z&quot;,&#10;		&quot;last_updated&quot;: &quot;2023-11-08T16:45:17.236841Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>If API Shield defaults an omitted algorithm, the response includes the effective algorithm in <code>result</code>. The <code>messages</code> array also contains one message for each defaulted key:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;code&quot;: 110003,&#10;	&quot;message&quot;: &quot;keys[0].alg was omitted and defaulted to \&quot;RS256\&quot; (kid \&quot;key-1\&quot;)&quot;&#10;}&#10;</code></pre>
<p>Inspect both <code>result</code> and <code>messages</code> to confirm the effective credentials.</p>
<h2 id="act-on-validation-results">Act on validation results</h2>
<p>After you create a token configuration, Cloudflare checks every request in the zone for a JWT at the configured token sources and validates any token it finds. You do not need a token validation rule or an operation in Endpoint Management for validation. Rules determine how Cloudflare acts on the results.</p>
<p>For new security policies, Cloudflare generally recommends using WAF custom rules.</p>
<ul>
<li><strong><a href="/waf/custom-rules/">WAF custom rules</a></strong> — use these for zone-wide policies based on verified JWT claims. Custom rules can combine claims with other signals, such as <a href="/waf/detections/attack-score/">attack score</a>. Endpoints do not need to be in Endpoint Management.</li>
<li><strong>Token validation rules</strong> — use these when enforcement must apply only to specific operations in Endpoint Management. These rules support the <code>is_jwt_valid()</code> and <code>is_jwt_present()</code> functions, which are not available in custom rules.</li>
</ul>
<p>To reference a custom claim in a rule expression, you can use <code>lookup_json_*</code> functions like <a href="/ruleset-engine/rules-language/functions/#lookup_json_string"><code>lookup_json_string()</code></a> with your token configuration ID and the claim name. For a complete example, refer to <a href="/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/">Issue challenge for admin user in JWT claim based on attack score</a>. For all available fields and standard claims, refer to the <a href="/ruleset-engine/rules-language/fields/reference/?field-category=JWT+validation">JWT validation fields</a> reference.</p>
<h2 id="token-validation-rules">Token validation rules</h2>
<p>Token validation rules enforce a security policy using existing token configurations and operations in Endpoint Management.</p>
<p>Token validation rules can be configured using the Cloudflare API or <a href="/api-shield/security/jwt-validation/#add-a-jwt-validation-rule">dashboard</a>.</p>
<table>
<thead>
<tr>
<th><span style="width:120px">Field name</span></th>
<th>Description</th>
<th>Example</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>title</code></td>
<td>A human-readable name allowing you to quickly identify it.</td>
<td>JWT validation on <code>v1</code> and <code>v2.example.com</code></td>
<td>Limited to 50 characters.</td>
</tr>
<tr>
<td><code>description</code></td>
<td>A human-readable description that gives more details than <code>title</code> and helps to document it.</td>
<td>Log requests without a valid <code>authorization</code> header.</td>
<td>Limited to 500 characters.</td>
</tr>
<tr>
<td><code>action</code></td>
<td>The Firewall Action taken on requests that do not meet <code>expression</code>.</td>
<td><code>log</code></td>
<td>Possible: <code>log</code> or <code>block</code></td>
</tr>
<tr>
<td><code>enabled</code></td>
<td>Enable or disable the rule.</td>
<td><code>true</code></td>
<td>Possible: <code>true</code> or <code>false</code></td>
</tr>
<tr>
<td><code>expression</code></td>
<td>The rule's security policy.</td>
<td><code>is_jwt_valid (&quot;00170473-ec24-410e-968a-9905cf0a7d03&quot;)</code></td>
<td>Make sure to escape any quotes when creating rules using the Cloudflare API. <br /> Refer to <a href="#define-a-security-policy">Define a security policy</a> below.</td>
</tr>
<tr>
<td><code>selector</code></td>
<td>Configure what operations are covered by this rule.</td>
<td></td>
<td>Refer to <a href="#apply-a-rule-to-operations">Applying a rule to operations</a> below.</td>
</tr>
</tbody>
</table>
<h3 id="selectors">Selectors</h3>
<p>Selectors control to which operations from Endpoint Management Cloudflare applies the action of a token validation rule.</p>
<p>If you only need enforcement on specific hostnames or subdomains of your apex domain, use the hostname in a selector to include matching operations in the JWT validation rule.</p>
<p>If you need to exclude endpoints from enforcement, use the endpoint's operation ID in a selector. For example, you can exclude an endpoint that issues or refreshes JWTs.</p>
<p>To find the operation ID, refer to <a href="/api-shield/management-and-monitoring/">Endpoint Management</a> or use the <a href="/api/resources/api_gateway/subresources/operations/methods/list/">Cloudflare API</a>.</p>
<h2 id="define-a-security-policy">Define a security policy</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3292.md")
</aside>
<p>A token validation rule's expression defines a security policy that a request must meet.</p>
<p>For example, the expression <code>is_jwt_valid(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;) or is_jwt_valid(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;)</code> will trigger if an incoming request does not have at least one valid authentication token.</p>
<p>These expressions are similar to <a href="/ruleset-engine/rules-language/">expressions used in Ruleset Engine</a>, with a few key differences:</p>
<ul>
<li>The token validation rule actions trigger if the expression evaluates <code>false</code>, as opposed to Ruleset expressions.</li>
<li>The token validation rules can use dedicated functions that reference token configurations.</li>
</ul>
<p>Operators such as <code>or</code>, <code>and</code>, <code>eq</code>, and more are usable in expressions in the same way as in expressions used in Ruleset Engine.</p>
<p>The following functions can be used to interact with JWT Tokens on a request:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/functions/#is_jwt_valid"><code>is_jwt_valid(token_configuration_id)</code></a> — Returns true if the request has a valid token according to the token configuration with the ID <code>token_configuration_id</code>.</li>
<li><a href="/ruleset-engine/rules-language/functions/#is_jwt_present"><code>is_jwt_present(token_configuration_id)</code></a> — Returns true if the request has a token as configured in the token configuration with the ID <code>token_configuration_id</code>.</li>
</ul>
<p>These functions are only available in token validation rules. They are not available in WAF custom rules.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>Refer to the following example use cases to understand which security policy to use. For most use cases, Cloudflare recommends requiring a valid token across your API and excluding any paths that are used to establish or refresh tokens using selectors.</p>
<h4 id="require-a-token">Require a token</h4>
<p>The <code>is_jwt_present(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;)</code> expression will trigger an action if a request is missing a JWT.</p>
<p>It can be combined with a <code>log</code> action in the token validation rule to log requests that are missing an authentication header.</p>
<h4 id="require-a-valid-token">Require a valid token</h4>
<p>The <code>is_jwt_valid(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;)</code> expression will trigger an action if a request does not have a valid JWT.</p>
<p>It can be combined with a <code>block</code> action in the token validation rule to block requests with no or invalid credentials.</p>
<h4 id="require-at-least-one-of-two-possible-tokens">Require at least one of two possible tokens</h4>
<p>The <code>is_jwt_valid(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;) or is_jwt_valid(&quot;fddfc39e-3686-4683-ab23-bf917da6bb43&quot;)</code> expressions will trigger an action if a request does not have at least one valid token.</p>
<p>This can occur if you need to split JWKs into multiple token configurations.</p>
<h4 id="require-a-valid-token-but-ignore-requests-without-a-token">Require a valid token but ignore requests without a token</h4>
<p>The <code>is_jwt_valid(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;) or not is_jwt_present(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;)</code> expressions will trigger an action if a request has an invalid token, ignoring requests with no tokens at all.</p>
<h2 id="apply-a-rule-to-operations">Apply a rule to operations</h2>
<p>Only one token validation rule can apply to an operation. If an operation is covered by multiple rules, then the rule with highest precedence will take effect.</p>
<p>You can configure which operations JWT validation is enforced on using the <code>selector</code> field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3291.md")
</aside>
<p>For example, the following selector will apply a rule to all operations in <code>v1.example.com</code> and <code>v2.example.com</code>, except for two operations on these hosts:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;include&quot;: [&#10;		{&#10;			&quot;host&quot;: [&quot;v1.example.com&quot;, &quot;v2.example.com&quot;]&#10;		}&#10;	],&#10;	&quot;exclude&quot;: [&#10;		{&#10;			&quot;operation_ids&quot;: [&#10;				&quot;f9c5615e-fe15-48ce-bec6-cfc1946f1bec&quot;, // POST v1.example.com/login&#10;				&quot;56828eae-035a-4396-ba07-51c66d680a04&quot; // POST v2.example.com/login&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Operations can be included at a host level and ignored on a per-operation basis.</p>
<p>You can use the <code>POST /zones/{zone_id}/token_validation/rules/preview</code> endpoint to see the operations covered by this rule:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/rules/preview&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;    &quot;include&quot;: [&#10;        {&#10;            &quot;host&quot;: [&#10;                &quot;v1.example.com&quot;,&#10;                &quot;v2.example.com&quot;&#10;            ]&#10;        }&#10;    ],&#10;    &quot;exclude&quot;: [&#10;        {&#10;            &quot;operation_ids&quot;: [&#10;                &quot;f9c5615e-fe15-48ce-bec6-cfc1946f1bec&quot;, // POST v1.example.com/login&#10;                &quot;56828eae-035a-4396-ba07-51c66d680a04&quot;  // POST v2.example.com/login&#10;            ]&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>The response will include all operations on a zone with an additional <code>state</code> field.</p>
<p>The <code>state</code> field can be <code>ignored</code>, <code>excluded</code>, or <code>included</code>. Included operations will match the hostname selectors you specified. Excluded operations will match the operation IDs you specified in the selector. Ignored operations are those that do not match anything specified in the selector.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;operations&quot;: [&#10;			{&#10;				&quot;operation_id&quot;: &quot;ed15fcb6-5a73-41cd-91af-8c61e5bb1cdb&quot;,&#10;				&quot;method&quot;: &quot;GET&quot;,&#10;				&quot;host&quot;: &quot;example.com&quot;,&#10;				&quot;endpoint&quot;: &quot;/api/accounts/{var1}&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-05-24T14:54:34.806506Z&quot;,&#10;				&quot;state&quot;: &quot;ignored&quot;&#10;			},&#10;			{&#10;				&quot;operation_id&quot;: &quot;e7a582cd-3cfb-4061-ab5b-722e6e42f545&quot;,&#10;				&quot;method&quot;: &quot;GET&quot;,&#10;				&quot;host&quot;: &quot;v1.example.com&quot;,&#10;				&quot;endpoint&quot;: &quot;/api/accounts/{var1}&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-05-24T14:54:34.806506Z&quot;,&#10;				&quot;state&quot;: &quot;included&quot;&#10;			},&#10;			{&#10;				&quot;operation_id&quot;: &quot;ddd5df5a-795c-40ce-b38c-38e9d7ef9ae8&quot;,&#10;				&quot;method&quot;: &quot;GET&quot;,&#10;				&quot;host&quot;: &quot;v2.example.com&quot;,&#10;				&quot;endpoint&quot;: &quot;/api/accounts/{var1}&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-05-24T14:54:34.806506Z&quot;,&#10;				&quot;state&quot;: &quot;included&quot;&#10;			},&#10;			{&#10;				&quot;operation_id&quot;: &quot;4d20befb-0120-45d5-9b29-5835fd41b44e&quot;,&#10;				&quot;method&quot;: &quot;GET&quot;,&#10;				&quot;host&quot;: &quot;v3.example.com&quot;,&#10;				&quot;endpoint&quot;: &quot;/api/accounts/{var1}&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-05-24T14:54:34.806506Z&quot;,&#10;				&quot;state&quot;: &quot;ignored&quot;&#10;			},&#10;			{&#10;				&quot;operation_id&quot;: &quot;f9c5615e-fe15-48ce-bec6-cfc1946f1bec&quot;,&#10;				&quot;method&quot;: &quot;POST&quot;,&#10;				&quot;host&quot;: &quot;v1.example.com&quot;,&#10;				&quot;endpoint&quot;: &quot;/login&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-05-24T14:54:34.806506Z&quot;,&#10;				&quot;state&quot;: &quot;excluded&quot;&#10;			},&#10;			{&#10;				&quot;operation_id&quot;: &quot;56828eae-035a-4396-ba07-51c66d680a04&quot;,&#10;				&quot;method&quot;: &quot;POST&quot;,&#10;				&quot;host&quot;: &quot;v2.example.com&quot;,&#10;				&quot;endpoint&quot;: &quot;/login&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-05-24T14:54:34.806506Z&quot;,&#10;				&quot;state&quot;: &quot;excluded&quot;&#10;			},&#10;			{&#10;				&quot;operation_id&quot;: &quot;cf86874c-8d0c-4337-ae14-4e2459b541ac&quot;,&#10;				&quot;method&quot;: &quot;GET&quot;,&#10;				&quot;host&quot;: &quot;v3.example.com&quot;,&#10;				&quot;endpoint&quot;: &quot;login&quot;,&#10;				&quot;last_updated&quot;: &quot;2023-05-24T14:54:34.806506Z&quot;,&#10;				&quot;state&quot;: &quot;ignored&quot;&#10;			}&#10;		],&#10;		&quot;total&quot;: 7,&#10;		&quot;included&quot;: 2,&#10;		&quot;excluded&quot;: 2,&#10;		&quot;ignored&quot;: 3,&#10;		&quot;selected_hosts&quot;: [&quot;v1.example.com&quot;, &quot;v2.example.com&quot;],&#10;		&quot;available_hosts&quot;: [&#10;			&quot;example.com&quot;,&#10;			&quot;v1.example.com&quot;,&#10;			&quot;v1.example.com&quot;,&#10;			&quot;v3.example.com&quot;&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 20,&#10;		&quot;count&quot;: 20,&#10;		&quot;total_count&quot;: 1631&#10;	}&#10;}&#10;</code></pre>
<p>Operations with a <code>included</code> state will be covered by the token validation rule. The response also shows the hostnames of included operations in <code>result.selected_hosts</code> and shows all hostnames used by all zone operations in <code>result.available_hosts</code>.</p>
<p>You can also send an empty object in the request body:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/rules/preview&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{ }&#x27;&#10;</code></pre>
<p>The response will show all zone operations and all possible hosts, which you can use to build your own selector.</p>
<h2 id="token-validation-rule-json-object">Token validation rule JSON object</h2>
<p>The example below shows a JSON object with all the necessary information to create a token validation rule using the Cloudflare API.</p>
<p>Replace any token configurations IDs and operation IDs with the IDs that exist in your zone.</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;title&quot;: &quot;JWT Validation on v1 and v2.example.com&quot;,&#10;		&quot;description&quot;: &quot;Log requests without a valid authorization header.&quot;,&#10;		&quot;action&quot;: &quot;log&quot;,&#10;		&quot;enabled&quot;: true,&#10;		&quot;expression&quot;: &quot;is_jwt_valid(\&quot;00170473-ec24-410e-968a-9905cf0a7d03\&quot;)&quot;,&#10;		&quot;selector&quot;: {&#10;			&quot;include&quot;: [&#10;				{&#10;					&quot;host&quot;: [&quot;v1.example.com&quot;, &quot;v2.example.com&quot;]&#10;				}&#10;			],&#10;			&quot;exclude&quot;: [&#10;				{&#10;					&quot;operation_ids&quot;: [&#10;						&quot;f9c5615e-fe15-48ce-bec6-cfc1946f1bec&quot;,&#10;						&quot;56828eae-035a-4396-ba07-51c66d680a04&quot;&#10;					]&#10;				}&#10;			]&#10;		}&#10;	}&#10;]&#10;</code></pre>
<h2 id="create-a-token-validation-rule-using-the-cloudflare-api">Create a token Validation rule using the Cloudflare API</h2>
<p>Use cURL or any other API client tool to send the new configuration to Cloudflare's API to enable JWT validation. Make sure to replace <code>{zone_id}</code> with the relevant zone ID and add your <a href="/fundamentals/api/get-started/create-token/">authentication credentials</a> header.</p>
<p>Replace any token configurations IDs and operation IDs with the IDs that exist in your zone.</p>
<p>A single request can create multiple rules. To do so, pass multiple rule objects in the JSON array of the request body.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/rules/bulk&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;[&#10;    {&#10;        &quot;title&quot;: &quot;JWT Validation on v1 and v2.example.com&quot;,&#10;        &quot;description&quot;: &quot;Log requests without a valid authorization header.&quot;,&#10;        &quot;action&quot;: &quot;log&quot;,&#10;        &quot;enabled&quot;: true,&#10;        &quot;expression&quot;: &quot;is_jwt_valid(\&quot;00170473-ec24-410e-968a-9905cf0a7d03\&quot;)&quot;,&#10;        &quot;selector&quot;: {&#10;            &quot;include&quot;: [&#10;                {&#10;                    &quot;host&quot;: [&#10;                        &quot;v1.example.com&quot;,&#10;                        &quot;v2.example.com&quot;&#10;                    ]&#10;                }&#10;            ],&#10;            &quot;exclude&quot;: [&#10;                {&#10;                    &quot;operation_ids&quot;: [&#10;                        &quot;f9c5615e-fe15-48ce-bec6-cfc1946f1bec&quot;,&#10;                        &quot;56828eae-035a-4396-ba07-51c66d680a04&quot;&#10;                    ]&#10;                }&#10;            ]&#10;        }&#10;    }&#10;]&#x27;&#10;</code></pre>
<p>The response will be in a Cloudflare <code>v4</code> response envelope and the result contains the created rules. Note the returned ID for each rule, which can be used to edit or delete an existing rule.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;5ec7c417-6964-4b24-b82c-a23a7ec8f90c&quot;,&#10;			&quot;title&quot;: &quot;JWT Validation on v1 and v2.example.com&quot;,&#10;			&quot;description&quot;: &quot;Log requests without a valid authorization header.&quot;,&#10;			&quot;action&quot;: &quot;log&quot;,&#10;			&quot;enabled&quot;: true,&#10;			&quot;expression&quot;: &quot;is_jwt_valid(\&quot;00170473-ec24-410e-968a-9905cf0a7d03\&quot;)&quot;,&#10;			&quot;selector&quot;: {&#10;				&quot;include&quot;: [&#10;					{&#10;						&quot;host&quot;: [&quot;v1.example.com&quot;, &quot;v2.example.com&quot;]&#10;					}&#10;				],&#10;				&quot;exclude&quot;: [&#10;					{&#10;						&quot;operation_ids&quot;: [&#10;							&quot;f9c5615e-fe15-48ce-bec6-cfc1946f1bec&quot;,&#10;							&quot;56828eae-035a-4396-ba07-51c66d680a04&quot;&#10;						]&#10;					}&#10;				]&#10;			},&#10;			&quot;created_at&quot;: &quot;2023-10-18T12:08:09.575388Z&quot;,&#10;			&quot;last_updated&quot;: &quot;2023-10-18T12:08:09.575388Z&quot;,&#10;			&quot;modified_by&quot;: &quot;user@cloudflare.com&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="maintenance">Maintenance</h2>
<h3 id="update-token-configuration">Update token configuration</h3>
<p>It is best practice to rotate keys regularly. You can add a new key, start issuing JWTs with that key, and then remove the old key.</p>
<p>The input to updating the keys is the same as when creating a configuration where you supplied the initial keys using the credentials key and needs to be a JWK.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3290.md")
</aside>
<p>Credential updates use the same algorithm compatibility behavior as configuration creation. The response includes normalized credentials and a message for each defaulted algorithm.</p>
<p>Use <code>PUT</code> to replace the complete key set. Every symmetric key in a <code>PUT</code> request must include <code>k</code>. Keys omitted from the request are removed.</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/config/{config_id}/credentials&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;    &quot;keys&quot;: [&#10;        {&#10;            &quot;kty&quot;: &quot;EC&quot;,&#10;            &quot;use&quot;: &quot;sig&quot;,&#10;            &quot;kid&quot;: &quot;test&quot;,&#10;            &quot;x&quot;: &quot;-0LNzBheJPn-Zy6JmanTIUX7xc3jgqU714IQY0oU6mw&quot;,&#10;            &quot;y&quot;: &quot;KONxBybUcRsJQmtu17jMAHsILSw009AuU3ulfUGv3FI&quot;,&#10;            &quot;alg&quot;: &quot;ES256&quot;&#10;        },&#10;        {&#10;            &quot;kty&quot;: &quot;EC&quot;,&#10;            &quot;crv&quot;: &quot;P-256&quot;,&#10;            &quot;kid&quot;: &quot;test-2&quot;,&#10;            &quot;x&quot;: &quot;iIbPRbOeLzjGPvv7iwmzCOTU03R0xDqbenp2D6GUcWo&quot;,&#10;            &quot;y&quot;: &quot;tDkEh95PnfWwIXciCtdBBVA7wfghx_egmZ1Zcvu2lWw&quot;,&#10;            &quot;alg&quot;: &quot;ES256&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>Make sure to replace <code>{zone_id}</code> with the relevant zone ID and add your <a href="/fundamentals/api/get-started/create-token/">authentication credentials</a> header.</p>
<h4 id="preserve-or-rotate-a-symmetric-credential">Preserve or rotate a symmetric credential</h4>
<p>Use <code>PATCH</code> to update the complete key set without resubmitting stored symmetric credentials. Cloudflare matches an existing key using its <code>alg</code> and <code>kid</code> values.</p>
<ul>
<li>Omit <code>k</code> for a matching symmetric key to preserve its credential.</li>
<li>Include a new <code>k</code> value to rotate the credential.</li>
<li>Include <code>k</code> when adding a symmetric key that does not already exist.</li>
<li>Omit a key from <code>keys</code> to remove it from the configuration.</li>
<li>Do not set <code>k</code> to <code>null</code>.</li>
</ul>
<p>This example preserves the credential for <code>production-hmac-key</code> while adding an EC key:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;&#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/config/{config_id}/credentials&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;    &quot;keys&quot;: [&#10;        {&#10;            &quot;kty&quot;: &quot;oct&quot;,&#10;            &quot;alg&quot;: &quot;HS256&quot;,&#10;            &quot;kid&quot;: &quot;production-hmac-key&quot;&#10;        },&#10;        {&#10;            &quot;kty&quot;: &quot;EC&quot;,&#10;            &quot;alg&quot;: &quot;ES256&quot;,&#10;            &quot;crv&quot;: &quot;P-256&quot;,&#10;            &quot;kid&quot;: &quot;production-ec-key&quot;,&#10;            &quot;x&quot;: &quot;&lt;BASE64URL_ENCODED_X_COORDINATE&gt;&quot;,&#10;            &quot;y&quot;: &quot;&lt;BASE64URL_ENCODED_Y_COORDINATE&gt;&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>This example rotates the credential for the existing HMAC key:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;&#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/config/{config_id}/credentials&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;    &quot;keys&quot;: [&#10;        {&#10;            &quot;kty&quot;: &quot;oct&quot;,&#10;            &quot;alg&quot;: &quot;HS256&quot;,&#10;            &quot;kid&quot;: &quot;production-hmac-key&quot;,&#10;            &quot;k&quot;: &quot;&lt;NEW_BASE64URL_ENCODED_SECRET&gt;&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<h3 id="update-token-validation-rules">Update token validation rules</h3>
<p>Token validation rules can be updated with a <code>PATCH</code> request. A single <code>PATCH</code> request can update multiple rules.</p>
<p>A <code>PATCH</code> request is specified as a JSON array in the request body. Each item in that array contains updates to a single rule, defined by <code>id</code>.</p>
<p>The following example updates one rule and disables another:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/rules/bulk&quot;  \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;    {&#10;        &quot;id&quot;: &quot;714d3dd0-cc59-4911-862f-8a27e22353cc&quot;,&#10;        &quot;action&quot;: &quot;log&quot;,&#10;        &quot;title&quot;: &quot;updated title&quot;&#10;    },&#10;    {&#10;        &quot;id&quot;: &quot;7124f9bc-d6b5-430d-b488-b6bc2892f2fb&quot;,&#10;        &quot;enabled&quot;: false&#10;    }&#10;]&#x27;&#10;</code></pre>
<p>Rules can be reordered by setting a position field in the <code>PATCH</code> body.</p>
<p>This example places rule <code>714d3dd0-cc59-4911-862f-8a27e22353cc</code> after rule <code>7124f9bc-d6b5-430d-b488-b6bc2892f2fb</code>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/rules/bulk&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;[&#10;    {&#10;        &quot;id&quot;: &quot;714d3dd0-cc59-4911-862f-8a27e22353cc&quot;,&#10;        &quot;position&quot;: {&#10;            &quot;after&quot;: &quot;7124f9bc-d6b5-430d-b488-b6bc2892f2fb&quot;&#10;        }&#10;    }&#10;]&#x27;&#10;</code></pre>
<p>This example places rule <code>714d3dd0-cc59-4911-862f-8a27e22353cc</code> before rule <code>7124f9bc-d6b5-430d-b488-b6bc2892f2fb</code>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/token_validation/rules/bulk&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;[&#10;    {&#10;        &quot;id&quot;: &quot;714d3dd0-cc59-4911-862f-8a27e22353cc&quot;,&#10;        &quot;position&quot;: {&#10;            &quot;before&quot;: &quot;7124f9bc-d6b5-430d-b488-b6bc2892f2fb&quot;&#10;        }&#10;    }&#10;]&#x27;&#10;</code></pre>
<h2 id="perform-jwt-validation">Perform JWT validation</h2>
<p>Here is an overview of how JWT validation processes incoming requests:</p>
<ol>
<li>We extract the JWT in accordance with the configuration from the incoming request.</li>
<li>We decode the JWT and look for the JWTs header KID claim.</li>
<li>We use the KID and ALG claim to find the correct keys in the list of supplied keys.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3288.md")
</aside>
<ol start="4">
<li>We validate the authenticity of the JWT by checking the signature using the selected key.</li>
<li>Should the JWT contain an EXP claim (expiration time), we validate that the JWT is not expired.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3287.md")
</aside>
<ol start="6">
<li>Should the JWT contain a NBF claim (not before time), we validate that the JWT is already valid.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3286.md")
</aside>
<ol start="7">
<li>
<p>Cloudflare makes verified claims available as <code>http.request.jwt.claims</code> fields. WAF custom rules can act on these claims. Token validation rules can act on token presence and validity.</p>
</li>
<li>
<p>Security Analytics events in the Cloudflare dashboard for the <code>API Shield - Token Validation</code> service will explain violation reasons in the <code>Token validation violations</code> section of the event.</p>
</li>
</ol>
