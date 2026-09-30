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
<pre><code class="language-txt">   ┌────────┐            ┌────────┐         ┌──────────┐         ┌────────┐&#10;   │ Origin │            │ Client │         │ Attester │         │ Issuer │&#10;   └────────┘            └────────┘         └──────────┘         └────────┘&#10;       │                     │                   │                   │&#10;       │&lt;───── Request ──────│                   │                   │&#10;       │                     │                   │                   │&#10;       │── TokenChallenge ──&gt;│                   │                   │&#10;       │                     │                   │                   │&#10;       │                     │&lt;== Attestation ==&gt;│                   │&#10;       │                     │                                       │&#10;       │                     │─── TokenRequest+Attestation Proof ───&gt;│&#10;       │                     │                                       │[Verifies Attestation]&#10;       │                     │&lt;──────────── TokenResponse ───────────│&#10;       │                     │[Finalises Token]&#10;       │&lt;── Request+Token ───│&#10;       │                     │&#10;       │────── 200 OK ──────&gt;│&#10;</code></pre>
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
