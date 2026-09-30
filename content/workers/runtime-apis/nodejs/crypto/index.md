<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17157.md")
</aside>
<p>The <a href="https://nodejs.org/docs/latest/api/crypto.html"><code>node:crypto</code></a> module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.</p>
<p>All <code>node:crypto</code> APIs are fully supported in Workers with the following exceptions:</p>
<ul>
<li>The functions <a href="https://nodejs.org/api/crypto.html#cryptogeneratekeypairtype-options-callback">generateKeyPair</a> and <a href="https://nodejs.org/api/crypto.html#cryptogeneratekeypairsynctype-options">generateKeyPairSync</a>
do not support DSA or DH key pairs.</li>
<li><code>argon2</code> and <code>argon2Sync</code> are not supported.</li>
<li><code>ed448</code> and <code>x448</code> curves are not supported.</li>
<li>It is not possible to manually enable or disable <a href="https://nodejs.org/docs/latest/api/crypto.html#fips-mode">FIPS mode</a>.</li>
</ul>
<p>The full <code>node:crypto</code> API is documented in the <a href="https://nodejs.org/api/crypto.html">Node.js documentation for <code>node:crypto</code></a>.</p>
<p>The <a href="/workers/runtime-apis/web-crypto/">WebCrypto API</a> is also available within Cloudflare Workers. This does not
require the <code>nodejs_compat</code> compatibility flag.</p>
