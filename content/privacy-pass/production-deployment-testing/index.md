---
cp9:
  canonical: https://developers.cloudflare.com/privacy-pass/production-deployment-testing/
  description: Validate a Cloudflare-operated Privacy Pass deployment end to end — discover the issuer configuration, request and redeem a token, and verify issuance works.
  full_title: Production Deployment Testing · Cloudflare Privacy Pass docs
  head_html: <title>Production Deployment Testing · Cloudflare Privacy Pass docs</title><meta name="generator" content="Nift"><meta name="description" content="Validate a Cloudflare-operated Privacy Pass deployment end to end — discover the issuer configuration, request and redeem a token, and verify issuance works."><link rel="canonical" href="https://developers.cloudflare.com/privacy-pass/production-deployment-testing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-pass/production-deployment-testing/index.md"><meta property="og:title" content="Production Deployment Testing · Cloudflare Privacy Pass docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Validate a Cloudflare-operated Privacy Pass deployment end to end — discover the issuer configuration, request and redeem a token, and verify issuance works."><meta property="og:url" content="https://developers.cloudflare.com/privacy-pass/production-deployment-testing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Pass"><meta name="algolia_product_filter" content="Privacy Pass"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Privacy Pass"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-pass/production-deployment-testing/#page","headline":"Production Deployment Testing \u00b7 Cloudflare Privacy Pass docs","description":"Validate a Cloudflare-operated Privacy Pass deployment end to end \u2014 discover the issuer configuration, request and redeem a token, and verify issuance works.","url":"https://developers.cloudflare.com/privacy-pass/production-deployment-testing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-pass/production-deployment-testing/
  schema: 1
---
<p>This guide covers obtaining a token from your Cloudflare-operated deployment. By this point, you and Cloudflare have already worked together to build and provision the following components. Use this guide to confirm the deployment issues and redeems tokens end to end.</p>
<p>Privacy Pass is not a self-serve product at the moment: a production deployment is a managed engagement with Cloudflare. If you just want to see Privacy Pass work without any setup, refer to <a href="/privacy-pass/getting-started/">Getting started</a>.</p>
<p><a href="https://www.cloudflare.com/lp/privacy-edge/">Contact us</a> to request access and receive your issuer configuration.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p><strong>What Cloudflare provisions:</strong></p>
<ul>
<li>An issuer endpoint (referred to here as <code>https://your-issuer.example.com</code>), running a public, RFC 9578-compliant issuer.</li>
<li>A public directory endpoint at <code>/.well-known/private-token-issuer-directory</code>.</li>
<li>A <code>/token-request</code> endpoint.</li>
</ul>
<p><strong>What you operate or need in place:</strong></p>
<ul>
<li>A working <strong>Attester</strong>, the service that verifies your claim and, once the Client is verified, proxies the blinded token request to the Issuer. In Cloudflare Issuer deployments, the Client never contacts the Issuer directly. Generally, you operate the Attester to keep roles separate, but Cloudflare can help build it. Refer to <a href="https://github.com/cloudflare/privacypass-attester">cloudflare/privacypass-attester</a> for an implementation for Cloudflare Workers.</li>
<li>The <strong>Origin</strong> (the web service, application, or website a Client is trying to access) configured to verify tokens against the issuer's public key (or Cloudflare redemption at the edge).</li>
<li>The <strong>mTLS client certificate</strong> your Attester uses to authenticate to the issuer.</li>
<li>The <strong>client library</strong> for running the issuance protocol. Library options include TypeScript, Go, and Rust.</li>
</ul>
<p>Implement the Client with the Privacy Pass library for your stack:</p>
<ul>
<li><strong>TypeScript</strong> — <a href="https://github.com/cloudflare/privacypass-ts">@cloudflare/privacypass-ts</a></li>
<li><strong>Go</strong> — <a href="https://github.com/cloudflare/pat-go">cloudflare/pat-go</a> (reference implementation, intended for experimental and interop use)</li>
<li><strong>Rust</strong> — <a href="https://github.com/raphaelrobert/privacypass">raphaelrobert/privacypass</a> (not independently audited)</li>
</ul>
<hr />
<h2 id="1-discover-the-issuer-configuration"><ol>
<li>Discover the issuer configuration</li>
</ol></h2>
<p>Every issuer publishes its configuration at the standard directory endpoint. This endpoint is public, so you can fetch it to confirm the issuer is reachable and read its public keys:</p>
<pre tabindex="0"><code class="language-sh">curl https://your-issuer.example.com/.well-known/private-token-issuer-directory&#10;</code></pre>
<p>The response lists the token-request endpoint and the issuer's public keys. Token type <code>2</code> is Blind RSA:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;issuer-request-uri&quot;: &quot;/token-request&quot;,&#10;  &quot;token-keys&quot;: [&#10;    {&#10;      &quot;token-type&quot;: 2,&#10;      &quot;token-key&quot;: &quot;&lt;base64url-encoded public key&gt;&quot;,&#10;      &quot;not-before&quot;: 1700000000&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>These are the keys your Origin will verify redeemed tokens against.</p>
<hr />
<h2 id="2-request-and-redeem-a-token"><ol start="2">
<li>Request and redeem a token</li>
</ol></h2>
<p>In this deployment the Client never contacts the issuer directly. Getting a token is a round trip across all four roles:</p>
<ol>
<li>The <strong>Origin</strong> returns a <code>WWW-Authenticate</code> challenge.</li>
<li>The <strong>Client</strong> completes attestation with <strong>your Attester</strong> and sends it a blinded token request.</li>
<li>The <strong>Attester</strong> verifies the Client, then authenticates to the issuer (for example, with mTLS) and proxies the request to the issuer's <code>/token-request</code> endpoint.</li>
<li>The <strong>Issuer</strong> signs the blinded request and returns it; the Client unblinds it to recover the finalized token, then redeems it at the Origin.</li>
</ol>
<pre tabindex="0"><code class="language-txt"> Origin              Client              Attester            Issuer&#10;   │                   │                    │                  │&#10;   │- TokenChallenge ─&gt;│                    │                  │&#10;   │                   │&lt;=== Attestation ==&gt;│                  │&#10;   │                   │                    │── TokenRequest ─&gt;│&#10;   │                   │                    │&lt;─ TokenResponse ─│&#10;   │                   │&lt;── TokenResponse ──│                  │&#10;   │&lt;─ Request+Token -─│ [finalize token]   │                  │&#10;   │────- 200 OK ────-&gt;│                    │                  │&#10;</code></pre>
<p>Using the TypeScript library for this example, the Client builds the blinded token request, then sends it to your Attester, which proxies it to the issuer and returns the signed response:</p>
<pre tabindex="0"><code class="language-ts">import { publicVerif } from &#x27;@cloudflare/privacypass-ts&#x27;;&#10;const { BlindRSAMode, Client } = publicVerif;&#10;&#10;// Declare your own sendToAttester transport — see the note below.&#10;declare function sendToAttester(tokenRequest: Uint8Array): Promise&lt;Uint8Array&gt;;&#10;&#10;// `tokenChallenge` comes from the Origin&#x27;s WWW-Authenticate header.&#10;// `issuerPublicKey` is the issuer&#x27;s public key bytes (from the directory in Step 1).&#10;const client = new Client(BlindRSAMode.PSS);&#10;const tokenRequest = await client.createTokenRequest(tokenChallenge, issuerPublicKey);&#10;&#10;// Send the blinded request to your Attester. It verifies the client, proxies the&#10;// request to the issuer, and returns the issuer&#x27;s signed token response.&#10;const tokenResponseBytes = await sendToAttester(tokenRequest.serialize());&#10;&#10;// Deserialize and unblind to recover the finalized token.&#10;const tokenResponse = client.deserializeTokenResponse(tokenResponseBytes);&#10;const token = await client.finalize(tokenResponse);&#10;</code></pre>
<p>The Client then redeems the token by sending it to the Origin in an <code>Authorization</code> header. The Origin (or Cloudflare at the edge – refer to <a href="/privacy-pass/concepts/deployment-models/">Deployment Models</a>) verifies the signature against the issuer's public key and responds with <code>200 OK</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/613.md")
</aside>
<hr />
<h2 id="3-verify-it-works"><ol start="3">
<li>Verify it works</li>
</ol></h2>
<p>Two signals confirm issuance and redemption are working end to end:</p>
<ul>
<li>The directory endpoint returns the issuer's <code>token-keys</code>.</li>
<li>A redeemed token verifies against the issuer's public key, and the Origin returns <code>200 OK</code>.</li>
</ul>
<p>To check that the directory endpoint is reachable, you can use the <a href="https://privacypass-demo.cloudflare.app/">Privacy Pass demo tool</a> to fetch the issuer's directory.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/612.md")
</aside>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/privacy-pass/concepts/privacy-pass-protocol/">Privacy Pass Protocol</a> — the four roles, the issuance and redemption flow, and the blinded signatures that produce tokens.</li>
<li><a href="/privacy-pass/concepts/deployment-models/">Deployment Models</a> — who operates each role and the deployment models.</li>
<li><a href="https://github.com/cloudflare/privacypass-attester">cloudflare/privacypass-attester</a> — reference attester implementation (Turnstile attestation, proxies token requests to an issuer).</li>
<li><a href="https://github.com/cloudflare/privacypass-issuer">cloudflare/privacypass-issuer</a> — reference issuer implementation (Workers, key rotation).</li>
</ul>
