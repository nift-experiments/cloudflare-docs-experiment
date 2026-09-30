<h2 id="background">Background</h2>
<p>The Web Crypto API provides a set of low-level functions for common cryptographic tasks. The Workers runtime implements the full surface of this API, but with some differences in the <a href="#supported-algorithms">supported algorithms</a> compared to those implemented in most browsers.</p>
<p>Performing cryptographic operations using the Web Crypto API is significantly faster than performing them purely in JavaScript. If you want to perform CPU-intensive cryptographic operations, you should consider using the Web Crypto API.</p>
<p>The Web Crypto API is implemented through the <code>SubtleCrypto</code> interface, accessible via the global <code>crypto.subtle</code> binding. A simple example of calculating a digest (also known as a hash) is:</p>
<pre><code class="language-js">const myText = new TextEncoder().encode(&#x27;Hello world!&#x27;);&#10;&#10;const myDigest = await crypto.subtle.digest(&#10;  {&#10;    name: &#x27;SHA-256&#x27;,&#10;  },&#10;  myText // The data you want to hash as an ArrayBuffer&#10;);&#10;&#10;console.log(new Uint8Array(myDigest));&#10;</code></pre>
<p>Some common uses include <a href="/workers/examples/signing-requests/">signing requests</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16124.md")
</aside>
<hr />
<h2 id="constructors">Constructors</h2>
<ul>
<li>
<p><code>crypto.DigestStream(algorithm)</code> DigestStream</p>
<ul>
<li>A non-standard extension to the <code>crypto</code> API that supports generating a hash digest from streaming data. The <code>DigestStream</code> itself is a <a href="/workers/runtime-apis/streams/writablestream/"><code>WritableStream</code></a> that does not retain the data written into it. Instead, it generates a hash digest automatically when the flow of data has ended.</li>
</ul>
</li>
</ul>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><code>algorithm</code>string | object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
</ul>
<h3 id="usage">Usage</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16127.md")
</div></div>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>crypto.randomUUID()</code> : string</p>
<ul>
<li>Generates a new random (version 4) UUID as defined in <a href="https://www.rfc-editor.org/rfc/rfc4122.txt">RFC 4122</a>.</li>
</ul>
</li>
<li>
<p><code>crypto.getRandomValues(bufferArrayBufferView)</code> : ArrayBufferView</p>
<ul>
<li>Fills the passed <code>ArrayBufferView</code> with cryptographically sound random values and returns the <code>buffer</code>.</li>
</ul>
</li>
</ul>
<h3 id="parameters-1">Parameters</h3>
<ul>
<li>
<p><code>buffer</code>ArrayBufferView</p>
<ul>
<li>Must be an Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | BigInt64Array | BigUint64Array.</li>
</ul>
</li>
</ul>
<h2 id="subtlecrypto-methods">SubtleCrypto Methods</h2>
<p>These methods are all accessed via <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto#Methods"><code>crypto.subtle</code></a>, which is also documented in detail on MDN.</p>
<h3 id="encrypt">encrypt</h3>
<ul>
<li>
<p><code>encrypt(algorithm, key, data)</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Returns a Promise that fulfills with the encrypted data corresponding to the clear text, algorithm, and key given as parameters.</li>
</ul>
</li>
</ul>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>key</code>CryptoKey</p>
</li>
<li>
<p><code>data</code>BufferSource</p>
</li>
</ul>
<h3 id="decrypt">decrypt</h3>
<ul>
<li>
<p><code>decrypt(algorithm, key, data)</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Returns a Promise that fulfills with the clear data corresponding to the ciphertext, algorithm, and key given as parameters.</li>
</ul>
</li>
</ul>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/decrypt#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>key</code>CryptoKey</p>
</li>
<li>
<p><code>data</code>BufferSource</p>
</li>
</ul>
<h3 id="sign">sign</h3>
<ul>
<li>
<p><code>sign(algorithm, key, data)</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Returns a Promise that fulfills with the signature corresponding to the text, algorithm, and key given as parameters.</li>
</ul>
</li>
</ul>
<h4 id="parameters-4">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>string | object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/sign#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>key</code>CryptoKey</p>
</li>
<li>
<p><code>data</code>ArrayBuffer</p>
</li>
</ul>
<h3 id="verify">verify</h3>
<ul>
<li>
<p><code>verify(algorithm, key, signature, data)</code> : Promise&lt;boolean&gt;</p>
<ul>
<li>Returns a Promise that fulfills with a Boolean value indicating if the signature given as a parameter matches the text, algorithm, and key that are also given as parameters.</li>
</ul>
</li>
</ul>
<h4 id="parameters-5">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>string | object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/verify#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>key</code>CryptoKey</p>
</li>
<li>
<p><code>signature</code>ArrayBuffer</p>
</li>
<li>
<p><code>data</code>ArrayBuffer</p>
</li>
</ul>
<h3 id="digest">digest</h3>
<ul>
<li>
<p><code>digest(algorithm, data)</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Returns a Promise that fulfills with a digest generated from the algorithm and text given as parameters.</li>
</ul>
</li>
</ul>
<h4 id="parameters-6">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>string | object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>data</code>ArrayBuffer</p>
</li>
</ul>
<h3 id="generatekey">generateKey</h3>
<ul>
<li>
<p><code>generateKey(algorithm, extractable, keyUsages)</code> : Promise&lt;CryptoKey&gt; | Promise&lt;CryptoKeyPair&gt;</p>
<ul>
<li>Returns a Promise that fulfills with a newly-generated <code>CryptoKey</code>, for symmetrical algorithms, or a <code>CryptoKeyPair</code>, containing two newly generated keys, for asymmetrical algorithms. For example, to generate a new AES-GCM key:</li>
</ul>
</li>
</ul>
<pre><code class="language-js">let keyPair = await crypto.subtle.generateKey(&#10;  {&#10;    name: &#x27;AES-GCM&#x27;,&#10;    length: 256,&#10;  },&#10;  true,&#10;  [&#x27;encrypt&#x27;, &#x27;decrypt&#x27;]&#10;);&#10;</code></pre>
<h4 id="parameters-7">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/generateKey#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>extractable</code>bool</p>
</li>
<li>
<p><code>keyUsages</code>Array</p>
<ul>
<li>An Array of strings indicating the <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/generateKey#Syntax">possible usages of the new key</a>.</li>
</ul>
</li>
</ul>
<h3 id="derivekey">deriveKey</h3>
<ul>
<li>
<p><code>deriveKey(algorithm, baseKey, derivedKeyAlgorithm, extractable, keyUsages)</code> : Promise&lt;CryptoKey&gt;</p>
<ul>
<li>Returns a Promise that fulfills with a newly generated <code>CryptoKey</code> derived from the base key and specific algorithm given as parameters.</li>
</ul>
</li>
</ul>
<h4 id="parameters-8">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveKey#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>baseKeyCryptoKey</code></p>
</li>
<li>
<p><code>derivedKeyAlgorithmobject</code></p>
<ul>
<li>Defines the algorithm the derived key will be used for in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveKey#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>extractablebool</code></p>
</li>
<li>
<p><code>keyUsagesArray</code></p>
<ul>
<li>An Array of strings indicating the <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveKey#Syntax">possible usages of the new key</a></li>
</ul>
</li>
</ul>
<h3 id="derivebits">deriveBits</h3>
<ul>
<li>
<p><code>deriveBits(algorithm, baseKey, length)</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Returns a Promise that fulfills with a newly generated buffer of pseudo-random bits derived from the base key and specific algorithm given as parameters. It returns a Promise which will be fulfilled with an <code>ArrayBuffer</code> containing the derived bits. This method is very similar to <code>deriveKey()</code>, except that <code>deriveKey()</code> returns a <code>CryptoKey</code> object rather than an <code>ArrayBuffer</code>. Essentially, <code>deriveKey()</code> is composed of <code>deriveBits()</code> followed by <code>importKey()</code>.</li>
</ul>
</li>
</ul>
<h4 id="parameters-9">Parameters</h4>
<ul>
<li>
<p><code>algorithm</code>object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveBits#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>baseKey</code>CryptoKey</p>
</li>
<li>
<p><code>length</code>int</p>
<ul>
<li>Length of the bit string to derive.</li>
</ul>
</li>
</ul>
<h3 id="importkey">importKey</h3>
<ul>
<li>
<p><code>importKey(format, keyData, algorithm, extractable, keyUsages)</code> : Promise&lt;CryptoKey&gt;</p>
<ul>
<li>Transform a key from some external, portable format into a <code>CryptoKey</code> for use with the Web Crypto API.</li>
</ul>
</li>
</ul>
<h4 id="parameters-10">Parameters</h4>
<ul>
<li>
<p><code>format</code>string</p>
<ul>
<li>Describes <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#Syntax">the format of the key to be imported</a>.</li>
</ul>
</li>
<li>
<p><code>keyData</code>ArrayBuffer</p>
</li>
<li>
<p><code>algorithm</code>object</p>
<ul>
<li>Describes the algorithm to be used, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>extractable</code>bool</p>
</li>
<li>
<p><code>keyUsages</code>Array</p>
<ul>
<li>An Array of strings indicating the <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#Syntax">possible usages of the new key</a></li>
</ul>
</li>
</ul>
<h3 id="exportkey">exportKey</h3>
<ul>
<li>
<p><code>exportKey(formatstring, keyCryptoKey)</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Transform a <code>CryptoKey</code> into a portable format, if the <code>CryptoKey</code> is <code>extractable</code>.</li>
</ul>
</li>
</ul>
<h4 id="parameters-11">Parameters</h4>
<ul>
<li>
<p><code>format</code>string</p>
<ul>
<li>Describes the <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/exportKey#Syntax">format in which the key will be exported</a>.</li>
</ul>
</li>
<li>
<p><code>key</code>CryptoKey</p>
</li>
</ul>
<h3 id="wrapkey">wrapKey</h3>
<ul>
<li>
<p><code>wrapKey(format, key, wrappingKey, wrapAlgo)</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Transform a <code>CryptoKey</code> into a portable format, and then encrypt it with another key. This renders the <code>CryptoKey</code> suitable for storage or transmission in untrusted environments.</li>
</ul>
</li>
</ul>
<h4 id="parameters-12">Parameters</h4>
<ul>
<li>
<p><code>format</code>string</p>
<ul>
<li>Describes the <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/wrapKey#Syntax">format in which the key will be exported</a> before being encrypted.</li>
</ul>
</li>
<li>
<p><code>key</code>CryptoKey</p>
</li>
<li>
<p><code>wrappingKey</code>CryptoKey</p>
</li>
<li>
<p><code>wrapAlgo</code>object</p>
<ul>
<li>Describes the algorithm to be used to encrypt the exported key, including any required parameters, in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/wrapKey#Syntax">an algorithm-specific format</a>.</li>
</ul>
</li>
</ul>
<h3 id="unwrapkey">unwrapKey</h3>
<ul>
<li>
<p><code>unwrapKey(format, key, unwrappingKey, unwrapAlgo, <br/> unwrappedKeyAlgo, extractable, keyUsages)</code> : Promise&lt;CryptoKey&gt;</p>
<ul>
<li>Transform a key that was wrapped by <code>wrapKey()</code> back into a <code>CryptoKey</code>.</li>
</ul>
</li>
</ul>
<h4 id="parameters-13">Parameters</h4>
<ul>
<li>
<p><code>format</code>string</p>
<ul>
<li>Described the <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/unwrapKey#Syntax">data format of the key to be unwrapped</a>.</li>
</ul>
</li>
<li>
<p><code>key</code>CryptoKey</p>
</li>
<li>
<p><code>unwrappingKey</code>CryptoKey</p>
</li>
<li>
<p><code>unwrapAlgo</code>object</p>
<ul>
<li>Describes the algorithm that was used to encrypt the wrapped key, <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/unwrapKey#Syntax">in an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>unwrappedKeyAlgo</code>object</p>
<ul>
<li>Describes the key to be unwrapped, <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/unwrapKey#Syntax">in an algorithm-specific format</a>.</li>
</ul>
</li>
<li>
<p><code>extractable</code>bool</p>
</li>
<li>
<p><code>keyUsages</code>Array</p>
<ul>
<li>An Array of strings indicating the <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/unwrapKey#Syntax">possible usages of the new key</a></li>
</ul>
</li>
</ul>
<h3 id="timingsafeequal">timingSafeEqual</h3>
<ul>
<li>
<p><code>timingSafeEqual(a, b)</code> : bool</p>
<ul>
<li>Compare two buffers in a way that is resistant to timing attacks. This is a non-standard extension to the Web Crypto API.</li>
</ul>
</li>
</ul>
<h4 id="parameters-14">Parameters</h4>
<ul>
<li>
<p><code>a</code>ArrayBuffer | TypedArray</p>
</li>
<li>
<p><code>b</code>ArrayBuffer | TypedArray</p>
</li>
</ul>
<h3 id="supported-algorithms">Supported algorithms</h3>
<p>Workers implements all operations of the <a href="https://www.w3.org/TR/WebCryptoAPI/">WebCrypto standard</a>, as shown in the following table.</p>
<p>A checkmark (✓) indicates that this feature is believed to be fully supported according to the spec.<br/>
An x (✘) indicates that this feature is part of the specification but not implemented.<br/>
If a feature only implements the operation partially, details are listed.</p>
<table>
<thead>
<tr>
<th align="left">Algorithm</th>
<th align="left">sign()<br/>verify()</th>
<th align="left">encrypt()<br/>decrypt()</th>
<th align="left">digest()</th>
<th align="left">deriveBits()<br/>deriveKey()</th>
<th align="left">generateKey()</th>
<th align="left">wrapKey()<br/>unwrapKey()</th>
<th align="left">exportKey()</th>
<th align="left">importKey()</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">RSASSA PKCS1 v1.5</td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">RSA PSS</td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">RSA OAEP</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">ECDSA</td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">ECDH</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">Ed25519<sup><a href="#footnote-1">1</a></sup></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">X25519<sup><a href="#footnote-1">1</a></sup></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">NODE ED25519<sup><a href="#footnote-2">2</a></sup></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">AES CTR</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">AES CBC</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">AES GCM</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">AES KW</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">HMAC</td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">SHA 1</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">SHA 256</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">SHA 384</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">SHA 512</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">MD5<sup><a href="#footnote-3">3</a></sup></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr>
<td align="left">HKDF</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
</tr>
<tr>
<td align="left">PBKDF2</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left">✓</td>
</tr>
</tbody>
</table>
<p><strong>Footnotes:</strong></p>
<ol>
<li>
<p><a name="footnote-1"></a> Algorithms as specified in the <a href="https://wicg.github.io/webcrypto-secure-curves">Secure Curves API</a>.</p>
</li>
<li>
<p><a name="footnote-2"></a> Legacy non-standard EdDSA is supported for the Ed25519 curve in addition to the Secure Curves version. Since this algorithm is non-standard, note the following while using it:</p>
<ul>
<li>Use <code>NODE-ED25519</code> as the algorithm and <code>namedCurve</code> parameters.</li>
<li>Unlike NodeJS, Cloudflare will not support raw import of private keys.</li>
<li>The algorithm implementation may change over time. While Cloudflare cannot guarantee it at this time, Cloudflare will strive to maintain backward compatibility and compatibility with NodeJS's behavior. Any notable compatibility notes will be communicated in release notes and via this developer documentation.</li>
</ul>
</li>
<li>
<p><a name="footnote-3"></a> MD5 is not part of the WebCrypto standard but is supported in Cloudflare Workers for interacting with legacy systems that require MD5. MD5 is considered a weak algorithm. Do not rely upon MD5 for security.</p>
</li>
</ol>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto">SubtleCrypto documentation on MDN</a></li>
<li><a href="https://www.w3.org/TR/WebCryptoAPI//#subtlecrypto-interface">SubtleCrypto documentation as part of the W3C Web Crypto API specification</a></li>
<li><a href="/workers/examples/signing-requests/">Example: signing requests</a></li>
</ul>
