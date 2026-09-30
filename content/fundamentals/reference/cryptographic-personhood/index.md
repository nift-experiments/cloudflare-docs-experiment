<p>Cloudflare developed an <a href="https://blog.cloudflare.com/introducing-cryptographic-attestation-of-personhood/">alternative</a> to CAPTCHA authentication, the Cryptographic Attestation of Personhood (CAP).</p>
<p>CAP lets you prove that you are a legitimate website visitor by touching a hardware key, instead of solving a CAPTCHA puzzle.</p>
<p>This article provides answers to common questions about usability and privacy concerns.</p>
<p>You can also test CAP by going to the <a href="https://cloudflarechallenge.com/">demo site</a>.</p>
<h2 id="privacy-questions">Privacy questions</h2>
<p>The answer to most privacy concerns are summarized in this table:</p>
<table>
<thead>
<tr>
<th>Property</th>
<th>Cloudflare could</th>
<th>Cloudflare does</th>
</tr>
</thead>
<tbody>
<tr>
<td>Collect biometrics (fingerprints or face pictures)</td>
<td>No</td>
<td>N/A</td>
</tr>
<tr>
<td>Collect information about your hardware authenticator</td>
<td>Yes, limited to the number of keys in your batch</td>
<td>Yes, when available</td>
</tr>
</tbody>
</table>
<p>No, Cloudflare cannot collect biometrics. Our CAP process uses the WebAuthn API, which prevents the collection of <a href="https://www.w3.org/TR/webauthn-2/#sctn-biometric-privacy">biometrics by default</a>. When your device asks for a biometric authentication — such as via a fingerprint sensor — it all happens locally. </p>
<p>As such, we never see your biometric data: that remains on your device. Once your device confirms a match, it sends only a basic attestation message. In effect, your device sends a message proving “yes, someone correctly entered a fingerprint on this trustworthy device” and never sends the fingerprint itself.</p>
<p>Yes, Cloudflare does collect a limited amount of data about your key. We store the manufacturer of your key and batch identifier (<a href="https://fidoalliance.org/specs/fido-uaf-v1.1-ps-20170202/fido-uaf-protocol-v1.1-ps-20170202.html#full-basic-attestation">minimum of 100,000</a> keys per batch) for verification purposes. From our perspective, your key looks like all other keys in the batch.</p>
<p>Some self-signed keys and keys from certain manufacturers have been found to <a href="https://www.chromium.org/security-keys">not meet this requirement</a> and should be avoided if you are minimizing your online privacy risk.</p>
<hr />
<p>For more details on how we set up Cryptographic Attestation of Personhood, refer to the <a href="https://blog.cloudflare.com/introducing-cryptographic-attestation-of-personhood/">introductory blog post</a>.</p>
<hr />
<h2 id="what-devices-are-and-are-not-allowed">What devices are and are not allowed?</h2>
<h3 id="allowed-devices">Allowed devices</h3>
<p>CAP supports a wide variety of hardware authenticators:</p>
<ul>
<li><strong>Roaming (cross-platform) authenticators</strong>:
<ul>
<li><em>Supported</em>: All security keys found in the <a href="https://fidoalliance.org/metadata/">FIDO Metadata Service 3.0</a>, unless they have been revoked for security reasons.</li>
<li><em>Examples</em>: YubiKeys, HyperFIDO keys, Thetis FIDO U2F keys</li>
</ul>
</li>
<li><strong>Platform authenticators:</strong>
<ul>
<li><em>Examples</em>: Apple Touch ID and Face ID on iOS mobile devices and macOS laptops; Android mobile devices with fingerprint readers; Windows Hello</li>
</ul>
</li>
</ul>
<h3 id="known-limitations">Known limitations</h3>
<p>Most combinations of web browsers and WebAuthn-capable authenticators will work, but there are some known compatibility issues with WebAuthn attestation that may prevent CAP from working successfully:</p>
<ul>
<li><strong>Basic CAP</strong>:
<ul>
<li><em>macOS desktop</em>: For TouchID, browser must be Safari</li>
<li><em>Android</em>: Browser must be Chrome</li>
</ul>
</li>
<li><strong>CAP with Zero-Knowledge Proof</strong>:
<ul>
<li><em>Apple platform authenticators</em> (e.g., iPhone with Touch ID/Face ID) are incompatible with the <a href="https://blog.cloudflare.com/introducing-zero-knowledge-proofs-for-private-web-attestation-with-cross-multi-vendor-hardware/">zero-knowledge proof system</a>. If this fails, you will immediately be redirected to basic CAP route without having to take any further action. Since Apple uses a privacy-preserving <a href="https://www.w3.org/TR/webauthn/#sctn-apple-anonymous-attestation">Apple Anonymous Attestation</a> to show that an authenticator is valid while blocking tracking, this method maintains a high standard of privacy.</li>
</ul>
</li>
</ul>
<p>We are updating this list as the ecosystem evolves and as we continue to test different combinations.</p>
<h2 id="can-hackers-bypass-the-cryptographic-attestation-of-personhood">Can hackers bypass the Cryptographic Attestation of Personhood?</h2>
<p>CAP is one of many techniques to identify and block bots. To date, we have seen some attempts to test CAP’s security system, such as <a href="https://betterappsec.com/building-a-webauthn-click-farm-are-captchas-obsolete-bfab07bb798c">one thoughtfully-executed, well-documented test</a>. The blog post discussing the test specifically calls out that this method does not break the Cloudflare threat model.</p>
<p>This does not mean that CAP is broken, but rather shows that it raises the cost of an attack over the current CAPTCHA model.</p>
<h2 id="what-happens-if-i-lose-my-key">What happens if I lose my key?</h2>
<p>If you do not have the necessary hardware (such as a Yubikey), you can still solve a regular CAPTCHA challenge (e.g., selecting pictures).</p>
<h2 id="what-are-the-common-error-codes-and-what-do-they-mean">What are the common error codes and what do they mean?</h2>
<ul>
<li><strong>Unsupported_att_fmt</strong>:
<ul>
<li><em>Cause</em>: Your authenticator is using an unsupported attestation format (combination of browser and key). Also occurs when you use <em>Firefox</em> and select the option to &quot;anonymise your key&quot;.</li>
<li><em>Solution:</em> If this error occurs during <a href="https://blog.cloudflare.com/introducing-zero-knowledge-proofs-for-private-web-attestation-with-cross-multi-vendor-hardware/">zero-knowledge version of CAP</a>, you will automatically be redirected to the basic CAP flow. If basic CAP fails, try a different combination of supported hardware device and browser or opt for a CAPTCHA.</li>
</ul>
</li>
<li><strong>Unsupported_issuer</strong>:
<ul>
<li><em>Cause</em>: Your key is currently not supported.</li>
<li><em>Solution</em>: Use a <a href="#allowed-devices">supported key</a>.</li>
</ul>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://cloudflarechallenge.com/">https://cloudflarechallenge.com</a> (demo site)</li>
<li><a href="https://blog.cloudflare.com/introducing-cryptographic-attestation-of-personhood/">Introducing Cryptographic Attestation of Personhood</a> (blog)</li>
<li><a href="https://blog.cloudflare.com/cap-expands-support/">Expanding Crypotgraphic Attestation of Personhood</a> (blog)</li>
<li><a href="https://blog.cloudflare.com/introducing-zero-knowledge-proofs-for-private-web-attestation-with-cross-multi-vendor-hardware/">Introducing Zero-Knowledge Proofs</a> (blog)</li>
</ul>
