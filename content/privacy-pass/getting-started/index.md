<p>There are two self-serve ways to see Privacy Pass in action:</p>
<ul>
<li><strong>Get a real token with the demo tool:</strong> the fastest way to obtain a real, issuer-signed token, using a browser tool and a Cloudflare-provided demo issuer.</li>
<li><strong>See a local example:</strong> run the complete issuance and redemption flow on your own machine in a few minutes, using real Blind RSA cryptography.</li>
</ul>
<p>To understand the protocol itself, refer to <a href="/privacy-pass/concepts/privacy-pass-protocol/">Privacy Pass Protocol</a>. When you are ready to validate a real, Cloudflare-operated deployment, refer to <a href="/privacy-pass/production-deployment-testing/">Production Deployment Testing</a> and <a href="https://www.cloudflare.com/lp/privacy-edge/">contact us</a> to begin setting up the necessary infrastructure.</p>
<hr />
<h2 id="get-a-real-token-with-the-demo-tool">Get a real token with the demo tool</h2>
<p>The quickest way to see what an issuer-signed token looks like is with Cloudflare's <a href="https://privacypass-demo.cloudflare.app/">Privacy Pass Demo Tool</a>. Pointed at an issuer, it runs the full issuance flow in your browser and returns a verified token.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Our <strong>demo issuer directory URL</strong>, provided here: <a href="https://demo-pat.issuer.cloudflare.com/.well-known/private-token-issuer-directory">https://demo-pat.issuer.cloudflare.com/.well-known/private-token-issuer-directory</a>.</li>
</ul>
<h3 id="how-to-get-a-token">How to get a token</h3>
<ol>
<li>Open the <a href="https://privacypass-demo.cloudflare.app/">Privacy Pass demo tool</a>.</li>
<li>In <strong>Fetch from issuer URL</strong>, paste the demo issuer directory URL and submit. The tool displays the issuer directory—a list of <code>token-keys</code> with token type <code>2</code> (Blind RSA)—and automatically fills in the fields for the following steps.</li>
<li>In <strong>Create challenge</strong>, submit the prefilled form. The tool builds a <code>WWW-Authenticate</code> token challenge from the issuer's key.</li>
<li>In <strong>Send Token Request</strong>, submit the prefilled form. The tool blinds the request, sends it to the issuer, unblinds the response, and verifies the result.</li>
</ol>
<p>A successful run shows:</p>
<pre><code class="language-txt">Draft 16 Valid: true&#10;PrivateToken token=...&#10;</code></pre>
<p><code>Draft 16 Valid: true</code> means the issuer returned a real token that verifies against its public key. The <code>PrivateToken token=...</code> value is the finalized token a client would send to an Origin in an <code>Authorization</code> header.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/615.md")
</aside>
<hr />
<h2 id="see-a-local-example">See a local example</h2>
<p>You can run the issuance and redemption flow on your machine in a few minutes, with no Cloudflare setup. It uses real Blind RSA cryptography, but everything happens in one process: the issuer key is generated locally and attestation is stubbed out. It is a quick way to see the protocol in action.</p>
<h3 id="prerequisites-1">Prerequisites</h3>
<ul>
<li><a href="https://nodejs.org/">Node.js</a> and <a href="https://git-scm.com/">git</a>.</li>
</ul>
<h3 id="run-the-example">Run the example</h3>
<p>The <a href="https://github.com/cloudflare/privacypass-ts">@cloudflare/privacypass-ts</a> library ships runnable examples. Clone the repository and install dependencies:</p>
<pre><code class="language-sh">git clone https://github.com/cloudflare/privacypass-ts.git&#10;cd privacypass-ts&#10;npm ci&#10;</code></pre>
<p>The publicly-verifiable example (<a href="https://github.com/cloudflare/privacypass-ts/blob/main/examples/pub_verif.example.ts"><code>pub_verif.example.ts</code></a>) only exports its functions, so add a small runner that calls just that one. Create <code>examples/run-pub-verif.ts</code>:</p>
<pre><code class="language-ts">import { publicVerifiableTokensPSS } from &quot;./pub_verif.example.js&quot;;&#10;&#10;await publicVerifiableTokensPSS();&#10;</code></pre>
<p>Compile the examples and run your runner:</p>
<pre><code class="language-sh">npx tsc -b examples&#10;node ./lib/examples/run-pub-verif.js&#10;</code></pre>
<p>It prints:</p>
<pre><code class="language-txt">Public-Verifiable tokens&#10;    Suite: ...&#10;    Valid token: true&#10;</code></pre>
<p><code>Valid token: true</code> means a token was issued, unblinded, and verified successfully.</p>
<h3 id="how-the-example-maps-to-the-four-roles">How the example maps to the four roles</h3>
<p>The example creates an Issuer, a Client, and an Origin in a single process (the Issuer key pair is generated up front in <code>setup()</code> with <code>Issuer.generateKey</code>), then runs them through the protocol.</p>
<p>The example follows the flow described in the diagram, and only exercises the Origin, Client, and Issuer. The Attester is stubbed and left out of the diagram since no real attestation runs here.</p>
<pre><code class="language-txt"> ┌────────┐              ┌────────┐                ┌────────┐&#10; │ Origin │              │ Client │                │ Issuer │&#10; └────────┘              └────────┘                └────────┘&#10;      │                       │                         │&#10;      │&lt;────── Request ───────│                         │&#10;      │─── TokenChallenge ───&gt;│                         │&#10;      │                       │                         │&#10;      │                       │───── TokenRequest ─────&gt;│&#10;      │                       │&lt;──── TokenResponse ─────│&#10;      │                       │                         │&#10;      │&lt;─── Request+Token ────│                         │&#10;</code></pre>
<p>Each call in the example maps to one step in that flow:</p>
<pre><code class="language-ts">const redemptionContext = crypto.getRandomValues(new Uint8Array(32));&#10;const tokChl = origin.createTokenChallenge(issuer.name, redemptionContext);  // Origin issues a token challenge&#10;const tokReq = await client.createTokenRequest(tokChl, pkIssuer);            // Client sends blinded request&#10;const tokRes = await issuer.issue(tokReq);                                   // Issuer signs the blinded request&#10;const token = await client.finalize(tokRes);                                 // Client finalizes token and resends request with it&#10;const isValid = await origin.verify(token, issuer.publicKey);                // Origin verifies against the issuer key&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/614.md")
</aside>
<hr />
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/privacy-pass/production-deployment-testing/">Production Deployment Testing</a> — when you are ready to go beyond these self-serve demos, this is the in-depth guide to validating a real, Cloudflare-operated deployment, with your Attester, Issuer, and Origin working together.</li>
<li><a href="/privacy-pass/concepts/privacy-pass-protocol/">Privacy Pass Protocol</a> — the four roles, the issuance and redemption flow, and the blinded signatures that produce tokens.</li>
<li><a href="/privacy-pass/concepts/deployment-models/">Deployment Models</a> — who operates each role and the deployment models.</li>
</ul>
