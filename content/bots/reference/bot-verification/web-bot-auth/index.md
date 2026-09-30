---
cp9:
  canonical: https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/
  description: Verify bot identity using cryptographic HTTP message signatures.
  full_title: Web Bot Auth · Cloudflare bot solutions docs
  head_html: <title>Web Bot Auth · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Verify bot identity using cryptographic HTTP message signatures."><link rel="canonical" href="https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/index.md"><meta property="og:title" content="Web Bot Auth · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify bot identity using cryptographic HTTP message signatures."><meta property="og:url" content="https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><meta name="pcx_tags" content="Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/#page","headline":"Web Bot Auth \u00b7 Cloudflare bot solutions docs","description":"Verify bot identity using cryptographic HTTP message signatures.","url":"https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Authentication"]}</script>
  markdown: true
  noindex: false
  route: /bots/reference/bot-verification/web-bot-auth/
  schema: 1
---
<p>Web Bot Auth is an authentication method that leverages cryptographic signatures in HTTP messages to verify that a request comes from an automated bot. Web Bot Auth is used as a verification method for <a href="/bots/concepts/bot/verified-bots/">verified bots and agents</a>.</p>
<p>It relies on IETF drafts: a <a href="https://datatracker.ietf.org/doc/html/draft-meunier-http-message-signatures-directory-03">directory draft</a> allowing the crawler to share their public keys, and a <a href="https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture-02">protocol draft</a> defining how these keys should be used to attach the crawler's identity to HTTP requests.</p>
<p>This documentation goes over specific integration within Cloudflare.</p>
<h2 id="1-generate-a-valid-signing-key"><ol>
<li>Generate a valid signing key</li>
</ol></h2>
<p>You need to generate a signing key which will be used to authenticate your bot's requests.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3574.md")
</div>
<p>By following these steps, you have generated a private key and a public key, then converted the public key to a JWK.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3572.md")
</aside>
<h2 id="2-host-a-key-directory"><ol start="2">
<li>Host a key directory</li>
</ol></h2>
<p>You need to host a key directory which creates a way for your bot to authenticate its requests to Cloudflare.
This directory should follow the definition from <a href="https://datatracker.ietf.org/doc/html/draft-meunier-http-message-signatures-directory-03">draft-meunier-http-message-signatures-directory-03</a>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3575.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3571.md")
</aside>
<p>You can use the Cloudflare-developed <a href="https://crates.io/crates/http-signature-directory"><code>http-signature-directory</code> CLI tool</a> to assist you in validating your directory.</p>
<h2 id="3-register-your-bot-and-key-directory"><ol start="3">
<li>Register your bot and key directory</li>
</ol></h2>
<p>You need to register your bot and its key directory to add your bot to the list of verified bots.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3576.md")
</div>
<p>Cloudflare accepts all valid Ed25519 keys found in your key directory. In the event a key already exists in Cloudflare's registered database, Cloudflare will work with you to supply a new key, or rotate your existing key.</p>
<p>After successful verification, you will be able to send verified requests.</p>
<h2 id="4-after-verification-sign-your-requests"><ol start="4">
<li>(After verification) Sign your requests</li>
</ol></h2>
<p>After your bot has been successfully verified, your bot is ready to sign its requests. The signature protocol is defined in <a href="https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture-02">draft-meunier-web-bot-auth-architecture-02</a></p>
<h3 id="4-1-choose-a-set-of-components-to-sign">4.1. Choose a set of components to sign</h3>
<p>Choose a set of components to sign.</p>
<p>A component is either an HTTP header, or any <a href="https://www.rfc-editor.org/rfc/rfc9421#name-derived-components">derived components</a> in the HTTP Message Signatures specification. Cloudflare recommends the following:</p>
<ul>
<li>Choose at least the <code>@authority</code> derived component, which represents the domain you are sending requests to. For example, a request to <code>https://example.com</code> will be interpreted to have an <code>@authority</code> of <code>example.com</code>.</li>
<li>Use components that only contain ASCII values. HTTP Message Signature specification disallows non-ASCII characters, which will result in failure to validate your bot's requests.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-components-with-only-ascii-values">Use components with only ASCII values</h3>
@markup("md", "content/.markup/bodies/3570.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="content-digest-header">`Content-Digest` header</h3>
@markup("md", "content/.markup/bodies/3569.md")
</aside>
<h3 id="4-2-calculate-the-jwk-thumbprint">4.2. Calculate the JWK thumbprint</h3>
<p><a href="https://www.rfc-editor.org/rfc/rfc8037.html#appendix-A.3">Calculate the base64 URL-encoded JWK thumbprint</a> from the public key you registered with Cloudflare.</p>
<h3 id="4-3-construct-the-required-headers">4.3. Construct the required headers</h3>
<p>Construct the three required headers for Web Bot Auth.</p>
<h4 id="signature-input-header"><code>Signature-Input</code> header</h4>
<p>Construct a <a href="https://www.rfc-editor.org/rfc/rfc9421#name-the-signature-input-http-fi"><code>Signature-Input</code> header</a> over your chosen components. The header must meet the following requirements.</p>
<table>
<thead>
<tr>
<th>Required component parameter</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tag</code></td>
<td>This should be equal to <code>web-bot-auth</code>.</td>
</tr>
<tr>
<td><code>keyid</code></td>
<td>This should be equal to the thumbprint computed in step 2.</td>
</tr>
<tr>
<td><code>created</code></td>
<td>This should be equal to a <code>Unix</code> timestamp associated with when the message was sent by your application.</td>
</tr>
<tr>
<td><code>expires</code></td>
<td>This should be equal to a <code>Unix</code> timestamp associated with when Cloudflare should no longer attempt to verify the message. A short <code>expires</code> reduces the likelihood of replay attacks, and Cloudflare recommends choosing suitable short-lived intervals.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="nonce">`nonce`</h3>
@markup("md", "content/.markup/bodies/3568.md")
</aside>
<h4 id="signature-header"><code>Signature</code> header</h4>
<p>Construct a <a href="https://www.rfc-editor.org/rfc/rfc9421#name-the-signature-http-field"><code>Signature</code> header</a> over your chosen components.</p>
<h4 id="signature-agent-header"><code>Signature-Agent</code> header</h4>
<p>Construct a <a href="https://datatracker.ietf.org/doc/html/draft-meunier-http-message-signatures-directory-03#name-header-field-definition"><code>Signature-Agent</code> header</a> that points to your key directory. Cloudflare implements the <code>Signature-Agent</code> format from <code>draft-meunier-http-message-signatures-directory-03</code>, where the header value is a structured string such as <code>&quot;https://signature-agent.test&quot;</code>.</p>
<p>Cloudflare will fail to verify a message if:</p>
<ul>
<li>The message includes a <code>Signature-Agent</code> header that is not an <code>https://</code>.</li>
<li>The message includes a valid URI but does not enclose it in double quotes. This is due to Signature-Agent being a structured field.</li>
<li>The message uses the dictionary form from later drafts, such as <code>sig2=&quot;https://signature-agent.test&quot;</code>.</li>
<li>The message has a valid <code>Signature-Agent</code> header, but does not include it in the component list in <code>Signature-Input</code>.</li>
</ul>
<h3 id="4-4-add-the-headers-to-your-bot-s-requests">4.4. Add the headers to your bot's requests</h3>
<p>Attach these three headers to your bot's requests.</p>
<p>An example request may look like this:</p>
<pre tabindex="0"><code class="language-txt">Signature-Agent: &quot;https://signature-agent.test&quot;&#10;Signature-Input: sig2=(&quot;@authority&quot; &quot;signature-agent&quot;)&#10; ;created=1735689600&#10; ;keyid=&quot;poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U&quot;&#10; ;alg=&quot;ed25519&quot;&#10; ;expires=1735693200&#10; ;nonce=&quot;e8N7S2MFd/qrd6T2R3tdfAuuANngKI7LFtKYI/vowzk4lAZYadIX6wW25MwG7DCT9RUKAJ0qVkU0mEeLElW1qg==&quot;&#10; ;tag=&quot;web-bot-auth&quot;&#10;Signature: sig2=:jdq0SqOwHdyHr9+r5jw3iYZH6aNGKijYp/EstF4RQTQdi5N5YYKrD+mCT1HA1nZDsi6nJKuHxUi/5Syp3rLWBA==:&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3567.md")
</aside>
<hr />
<h2 id="transitive-trust-and-the-forwarded-header">Transitive trust and the <code>Forwarded</code> header</h2>
<p>An agent that reaches your site is often not operated by the company that built it. A platform can run automations on behalf of many different end users, so the operator and the end user are not the same party. Cloudflare refers to this chain — website owner → bot operator → end user — as <strong>transitive trust</strong>.</p>
<p>To carry an operator's identity through that chain, Cloudflare is experimenting with the <code>Forwarded</code> header defined in <a href="https://www.rfc-editor.org/info/rfc7239">RFC 7239</a>. This works like <code>X-Forwarded-For</code> does for IP addresses: a preference to allow an operator holds whether that operator reaches you directly or through intermediaries that Cloudflare trusts.</p>
<p>The operator is identified with the <code>for</code> parameter:</p>
<pre tabindex="0"><code class="language-txt">Forwarded: for=&quot;openai&quot;&#10;</code></pre>
<p>The header can also carry the <a href="/bots/additional-configurations/managed-robots-txt/#content-use-signal"><code>content-use</code></a> value that the operator commits to for the content it accesses:</p>
<pre tabindex="0"><code class="language-txt">Forwarded: for=&quot;openai&quot;;use=&quot;reference&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3566.md")
</aside>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Cloudflare's implementation of Web Bot Auth does not support every component and parameter defined in IETF RFC 9421. If you include any of the following in your request's Signature-Input header, verification will fail.</p>
<ul>
<li><code>@query-params</code>: Cloudflare recommends signing the whole query using the <code>@query</code> component instead of signing an individual parameter.</li>
<li><code>@status</code>: This is not possible to include in the request path.</li>
</ul>
<p>The following component parameters defined in IETF RFC 9421 are not supported, and Cloudflare will fail to verify a message if they are included:</p>
<ul>
<li><code>sf</code> (for HTTP header fields)</li>
<li><code>bs</code> (for HTTP header fields)</li>
<li><code>key</code> (for HTTP header fields)</li>
<li><code>req</code> (for HTTP header fields or derived components)</li>
<li><code>name</code> (for <code>@query-param</code> support - this requires <code>@query-param</code> support)</li>
</ul>
<hr />
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="failed-message-validation">Failed message validation</h3>
<p>If your message is failing validation, the cause(s) may include:</p>
<ul>
<li>Ensure you have a <a href="/bots/reference/bot-verification/web-bot-auth/#signature-agent-header"><code>Signature-Agent</code> header</a>, and that its value is in double-quotes.</li>
<li>Ensure your <a href="/bots/reference/bot-verification/web-bot-auth/#signature-agent-header"><code>Signature-Agent</code> header</a> uses a structured string, not a dictionary.</li>
<li>Ensure you include <code>signature-agent</code> in the component list in your <a href="/bots/reference/bot-verification/web-bot-auth/#signature-agent-header"><code>Signature-Input</code> header</a>.</li>
<li>Ensure your <code>expires</code> timestamp is not too short, such that, by the time it arrives at Cloudflare servers, it has already expired. A minute is often sufficient.</li>
<li>Ensure you are not signing components containing non-ASCII values, or on the unsupported list.</li>
</ul>
<h3 id="use-http-message-signatures-web-bot-auth-on-a-zone-without-cloudflare-s-verification">Use HTTP message signatures / Web Bot Auth on a zone without Cloudflare's verification</h3>
<p>If you wish to use HTTP Message Signatures (Web Bot Auth) for your own origin processing and do not want Cloudflare's verification to intervene or populate the <code>cf.bot_management.verified_bot</code> field, you can request that the Cloudflare verification feature be disabled for your zone.</p>
<p>To disable Web Bot Auth verification, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<p>Disabling this feature means that Cloudflare will not validate incoming signatures. Verified bots will then fall back to other methods (such as reverse DNS validation) to determine if traffic is legitimate.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>You may wish to refer to the following resources.</p>
<ul>
<li>Cloudflare blog: <a href="https://blog.cloudflare.com/verified-bots-with-cryptography">Message Signatures are now part of our Verified Bots Program</a>.</li>
<li>Cloudflare blog: <a href="https://blog.cloudflare.com/web-bot-auth/">Forget IPs: using cryptography to verify bot and agent traffic</a>.</li>
<li>Cloudflare's <a href="https://crates.io/crates/web-bot-auth"><code>web-bot-auth</code> library in Rust</a>.</li>
<li>Cloudflare's <a href="https://www.npmjs.com/package/web-bot-auth"><code>web-bot-auth</code> npm package in Typescript</a>.</li>
</ul>
