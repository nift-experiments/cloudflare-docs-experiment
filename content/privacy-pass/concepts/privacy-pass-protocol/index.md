---
cp9:
  canonical: https://developers.cloudflare.com/privacy-pass/concepts/privacy-pass-protocol/
  description: The Privacy Pass roles, the issuance and redemption flow.
  full_title: Privacy Pass Protocol · Cloudflare Privacy Pass docs
  head_html: <title>Privacy Pass Protocol · Cloudflare Privacy Pass docs</title><meta name="generator" content="Nift"><meta name="description" content="The Privacy Pass roles, the issuance and redemption flow."><link rel="canonical" href="https://developers.cloudflare.com/privacy-pass/concepts/privacy-pass-protocol/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-pass/concepts/privacy-pass-protocol/index.md"><meta property="og:title" content="Privacy Pass Protocol · Cloudflare Privacy Pass docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The Privacy Pass roles, the issuance and redemption flow."><meta property="og:url" content="https://developers.cloudflare.com/privacy-pass/concepts/privacy-pass-protocol/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Pass"><meta name="algolia_product_filter" content="Privacy Pass"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Privacy Pass"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-pass/concepts/privacy-pass-protocol/#page","headline":"Privacy Pass Protocol \u00b7 Cloudflare Privacy Pass docs","description":"The Privacy Pass roles, the issuance and redemption flow.","url":"https://developers.cloudflare.com/privacy-pass/concepts/privacy-pass-protocol/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-pass/concepts/privacy-pass-protocol/
  schema: 1
---
<p>Privacy Pass splits responsibility across four roles so that no single party knows everything about user's identity and activity. This page explains the information flow of the protocol. For who operates each role and the privacy properties this design provides, refer to <a href="/privacy-pass/concepts/deployment-models/">Deployment Models</a>.</p>
<hr />
<h2 id="roles-overview">Roles overview</h2>
<table>
<thead>
<tr>
<th>Role</th>
<th>Responsibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Requests access, conducts issuance and redemption protocols.</td>
</tr>
<tr>
<td>Origin</td>
<td>Issues token challenges and verifies redeemed tokens.</td>
</tr>
<tr>
<td>Attester</td>
<td>Runs a deployment-specific attestation process to verify the client.</td>
</tr>
<tr>
<td>Issuer</td>
<td>Signs blinded token requests for attested clients. Cloudflare's issuers use publicly verifiable Blind RSA (token type <code>2</code>).</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="protocol-interaction">Protocol interaction</h2>
<p>As defined in RFC 9576, the flow runs across two protocols: <strong>issuance</strong> (obtaining a token) and <strong>redemption</strong> (using it for access).</p>
<pre tabindex="0"><code class="language-txt">   ┌────────┐            ┌────────┐         ┌──────────┐         ┌────────┐&#10;   │ Origin │            │ Client │         │ Attester │         │ Issuer │&#10;   └────────┘            └────────┘         └──────────┘         └────────┘&#10;       │                     │                   │                   │&#10;       │&lt;───── Request ──────│                   │                   │&#10;       │                     │                   │                   │&#10;       │── TokenChallenge ──&gt;│                   │                   │&#10;       │                     │                   │                   │&#10;       │                     │&lt;== Attestation ==&gt;│                   │&#10;       │                     │                                       │&#10;       │                     │─── TokenRequest+Attestation Proof ───&gt;│&#10;       │                     │                                       │[Verifies Attestation]&#10;       │                     │&lt;──────────── TokenResponse ───────────│&#10;       │                     │[Finalises Token]&#10;       │&lt;── Request+Token ───│&#10;       │                     │&#10;       │────── 200 OK ──────&gt;│&#10;</code></pre>
<p><strong>Initial Request</strong></p>
<ol>
<li>The Client sends a request to the Origin.</li>
<li>The Origin responds with a <strong>token challenge</strong>. If the Client has no token to redeem, it begins the <strong>issuance protocol</strong> with an Issuer the Origin trusts.</li>
</ol>
<p><strong>Issuance Protocol</strong></p>
<ol>
<li>The issuance protocol begins with the Client completing a deployment-specific <strong>attestation process</strong>. This step is intentionally open-ended so different use cases can define their own attestation.</li>
<li>Once the Attester verifies the Client, the Client sends a <strong>blinded token request</strong>–a request to sign a masked version of the token, preventing the finalized version from being linked to the original request–to the Issuer, along with proof of attestation.</li>
<li>The Issuer checks the verification, signs the blinded token, and returns it. The Client <strong>finalises</strong> it to recover the Privacy Pass token, completing the issuance protocol.</li>
</ol>
<p><strong>Redemption Protocol</strong></p>
<ol>
<li>The interaction finishes with the <strong>redemption protocol</strong>, where the Client sends the token along with its original request back to the Origin.</li>
<li>The Origin verifies the signature and responds with <code>200 OK</code>, granting access.</li>
</ol>
<hr />
<h2 id="see-it-in-code">See it in code</h2>
<p>To run the complete issuance and redemption flow on your own machine — no Cloudflare setup required — see the local example in <a href="/privacy-pass/getting-started/">Getting started</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://datatracker.ietf.org/doc/rfc9576/">RFC 9576: Privacy Pass Architecture</a></li>
<li><a href="https://datatracker.ietf.org/doc/rfc9577/">RFC 9577: The Privacy Pass HTTP Authentication Scheme</a></li>
<li><a href="https://datatracker.ietf.org/doc/rfc9578/">RFC 9578: Privacy Pass Issuance Protocols</a></li>
</ul>
