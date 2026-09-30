---
cp9:
  canonical: https://developers.cloudflare.com/privacy-proxy/concepts/authentication/
  description: Privacy Proxy authentication methods, including pre-shared keys, Privacy Pass tokens, and mutual TLS.
  full_title: Authentication · Cloudflare Privacy Proxy docs
  head_html: <title>Authentication · Cloudflare Privacy Proxy docs</title><meta name="generator" content="Nift"><meta name="description" content="Privacy Proxy authentication methods, including pre-shared keys, Privacy Pass tokens, and mutual TLS."><link rel="canonical" href="https://developers.cloudflare.com/privacy-proxy/concepts/authentication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-proxy/concepts/authentication/index.md"><meta property="og:title" content="Authentication · Cloudflare Privacy Proxy docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Privacy Proxy authentication methods, including pre-shared keys, Privacy Pass tokens, and mutual TLS."><meta property="og:url" content="https://developers.cloudflare.com/privacy-proxy/concepts/authentication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Proxy"><meta name="algolia_product_filter" content="Privacy Proxy"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Privacy Proxy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-proxy/concepts/authentication/#page","headline":"Authentication \u00b7 Cloudflare Privacy Proxy docs","description":"Privacy Proxy authentication methods, including pre-shared keys, Privacy Pass tokens, and mutual TLS.","url":"https://developers.cloudflare.com/privacy-proxy/concepts/authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-proxy/concepts/authentication/
  schema: 1
---
<p>Privacy Proxy requires clients to authenticate before proxying traffic. This page explains the supported authentication methods and when to use them.</p>
<h2 id="authentication-methods">Authentication methods</h2>
<p>Privacy Proxy supports three authentication methods:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Use case</th>
<th>Privacy level</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pre-shared key (PSK)</td>
<td>Proof of concept, testing</td>
<td>Lower</td>
</tr>
<tr>
<td>Privacy Pass tokens</td>
<td>Client to server</td>
<td>High</td>
</tr>
<tr>
<td>mTLS</td>
<td>Server to server</td>
<td>Higher</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="pre-shared-key-psk">Pre-shared key (PSK)</h2>
<p>Pre-shared keys provide a simple way to authenticate during development and proof-of-concept testing. Cloudflare provides a secret key that clients include in each request.</p>
<h3 id="how-it-works">How it works</h3>
<p>Include the PSK in the <code>Proxy-Authorization</code> header:</p>
<pre tabindex="0"><code class="language-http">CONNECT example.com:443 HTTP/2&#10;Host: example.com&#10;Proxy-Authorization: Preshared &lt;YOUR_PSK&gt;&#10;</code></pre>
<p>The proxy validates the key and allows the connection if it matches.</p>
<h3 id="limitations">Limitations</h3>
<p>PSK authentication has limitations that make it unsuitable for production.</p>
<ul>
<li><strong>Shared secret</strong>: All clients use the same key, so you cannot revoke access for individual users.</li>
<li><strong>No rate limiting per user</strong>: You cannot enforce per-user quotas or limits.</li>
<li><strong>Linkability</strong>: The proxy can link all requests using the same PSK, which reduces user privacy.</li>
</ul>
<p>Use PSK only for testing. For production deployments, use <a href="#privacy-pass-tokens">Privacy Pass tokens</a>.</p>
<hr />
<h2 id="privacy-pass-tokens">Privacy Pass tokens</h2>
<p><a href="https://datatracker.ietf.org/wg/privacypass/about/">Privacy Pass</a> is a protocol that allows clients to authenticate without revealing their identity. Tokens are cryptographically unlinkable, meaning the proxy cannot correlate different requests from the same user.</p>
<h3 id="how-it-works-1">How it works</h3>
<p>Privacy Pass uses a three-party architecture:</p>
<ul>
<li><strong>Attester</strong>: Verifies that the Client is a legitimate user (for example, has a valid account) and forwards token requests to the Issuer.</li>
<li><strong>Issuer</strong>: Signs blinded tokens without learning which Client requested them.</li>
<li><strong>Origin (Privacy Proxy)</strong>: Accepts tokens as proof of authorization.</li>
</ul>
<h3 id="token-issuance">Token issuance</h3>
<pre tabindex="0"><code>┌──────────┐    1. Attestation request   ┌──────────┐&#10;│          │ ──────────────────────────▶ │          │&#10;│  Client  │                             │ Attester │&#10;│          │ ◀────────────────────────── │          │&#10;└──────────┘    2. Attestation OK        └──────────┘&#10;     │&#10;     │ 3. Blinded token request&#10;     ▼&#10;┌──────────┐    4. Forward request       ┌──────────┐&#10;│          │ ──────────────────────────▶ │          │&#10;│ Attester │                             │  Issuer  │&#10;│          │ ◀────────────────────────── │          │&#10;└──────────┘    5. Signed blinded token  └──────────┘&#10;     │&#10;     │ 6. Return to Client&#10;     ▼&#10;┌──────────┐&#10;│  Client  │  (unblinds and stores token)&#10;└──────────┘&#10;</code></pre>
<p>The Client sends the token request through the Attester to maintain unlinkability. This ensures the Issuer cannot correlate token requests with specific attestation events or Client identities.</p>
<h3 id="token-redemption">Token redemption</h3>
<pre tabindex="0"><code>┌──────────┐    1. Present token         ┌──────────┐&#10;│          │ ──────────────────────────▶ │          │&#10;│  Client  │                             │  Privacy │&#10;│          │ ◀────────────────────────── │  Proxy   │&#10;└──────────┘    2. Connection OK         └──────────┘&#10;</code></pre>
<p>The Privacy Proxy validates the token using the Issuer's public key. The proxy learns only that the token is valid, not who it was issued to.</p>
<p>The token issuance process:</p>
<ol>
<li>The client proves their identity to the attester (for example, by signing in with an account).</li>
<li>The attester confirms the client is valid.</li>
<li>The client generates blinded tokens and sends them to the issuer.</li>
<li>The issuer signs the blinded tokens and returns them.</li>
<li>The client unblinds the tokens and stores them.</li>
</ol>
<p>When making a request:</p>
<ol>
<li>The client includes a token in the <code>Proxy-Authorization</code> header.</li>
<li>The proxy verifies the token signature with the issuer's public key.</li>
<li>The proxy allows the connection if the token is valid.</li>
</ol>
<p>Because tokens are blinded during issuance, the issuer cannot link tokens to specific issuance requests. The proxy sees only that a token is valid, not who it was issued to.</p>
<h3 id="token-format">Token format</h3>
<p>Privacy Pass tokens are included in the <code>Proxy-Authorization</code> header using the <code>PrivateToken</code> scheme:</p>
<pre tabindex="0"><code class="language-http">CONNECT example.com:443 HTTP/2&#10;Host: example.com&#10;Proxy-Authorization: PrivateToken token=&lt;base64-encoded-token&gt;&#10;</code></pre>
<h3 id="set-up-privacy-pass">Set up Privacy Pass</h3>
<p>For production deployments using Privacy Pass:</p>
<ol>
<li>Choose an issuer. Cloudflare can operate a token issuer, or you can integrate with a third-party issuer.</li>
<li>Configure attestation to define how clients prove their identity before receiving tokens.</li>
<li>Distribute issuer configuration. Clients need the issuer's public key and endpoint to request tokens.</li>
</ol>
<p><a href="https://www.cloudflare.com/lp/privacy-edge/">Contact us</a> to configure Privacy Pass for your deployment.</p>
<hr />
<h2 id="mutual-tls-mtls">Mutual TLS (mTLS)</h2>
<p><a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">Mutual TLS (mTLS) authentication</a> ensures that traffic is both secure and trusted in both directions. The client presents a certificate to the proxy, and the proxy validates it before allowing the connection.</p>
<h3 id="how-it-works-2">How it works</h3>
<p>The client includes a TLS client certificate during the TLS handshake. The proxy validates the certificate against a configured certificate authority (CA) and allows the connection if the certificate is trusted.</p>
<h3 id="limitations-1">Limitations</h3>
<p>You must provision and manage certificates for each client or service. mTLS is designed for server-to-server communication, not for authenticating individual users. The proxy can identify the client by its certificate, which reduces privacy compared to Privacy Pass.</p>
<p>Use mTLS for server-to-server integrations where both parties are trusted services.</p>
<hr />
<h2 id="authentication-in-double-hop-deployments">Authentication in double-hop deployments</h2>
<p>In <a href="/privacy-proxy/concepts/deployment-models/#double-hop">double-hop deployments</a>, authentication occurs at two levels:</p>
<h3 id="user-to-proxy-a">User to Proxy A</h3>
<p>Proxy A (which you operate) authenticates users. Common methods include:</p>
<ul>
<li>Account credentials (username/password, SSO)</li>
<li>Privacy Pass tokens issued by your infrastructure</li>
<li>Client certificates (mTLS)</li>
</ul>
<h3 id="proxy-a-to-proxy-b">Proxy A to Proxy B</h3>
<p>Proxy B authenticates itself to Proxy A using TLS. Depending on your configuration, this can use:</p>
<ul>
<li>Standard TLS certificates</li>
<li>Raw Public Key (RPK) TLS extension for reduced certificate overhead</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://datatracker.ietf.org/wg/privacypass/about/">Privacy Pass Working Group</a> - IETF working group developing the Privacy Pass protocol.</li>
<li><a href="https://blog.cloudflare.com/supporting-the-latest-version-of-the-privacy-pass-protocol/">Supporting the latest version of the Privacy Pass protocol</a> - Cloudflare blog post on Privacy Pass implementation.</li>
</ul>
