<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/14203.md")
</aside>
<p>Since the keys are already in place, we merely need to build the configuration file that the key server will read on startup. In this example the device contains a single RSA key pair.</p>
<p>We ask <code>pkcs11-tool</code> (provided by the <code>opensc</code> package) to display the objects stored in the token:</p>
<pre><code class="language-txt">pkcs11-tool --module /opt/nfast/toolkits/pkcs11/libcknfast.so -O&#10;</code></pre>
<pre><code class="language-txt">Using slot 0 with a present token (0x1d622495)&#10;Private Key Object; RSA&#10;  label:      rsa-privkey&#10;  ID:         105013281578de42ea45f5bfac46d302fb006687&#10;  Usage:      decrypt, sign, unwrap&#10;warning: PKCS11 function C_GetAttributeValue(ALWAYS_AUTHENTICATE) failed: rv = CKR_ATTRIBUTE_TYPE_INVALID (0x12)&#10;&#10;Public Key Object; RSA 2048 bits&#10;  label:      rsa-privkey&#10;  ID:         105013281578de42ea45f5bfac46d302fb006687&#10;  Usage:      encrypt, verify, wrap&#10;</code></pre>
<p>The key piece of information is the label of the object, <code>rsa-privkey</code>. Open up <code>/etc/keyless/gokeyless.yaml</code> and immediately after</p>
<pre><code class="language-yaml">private_key_stores:&#10;  &#45; dir: /etc/keyless/keys&#10;</code></pre>
<p>add</p>
<pre><code class="language-yaml">&#45; uri: pkcs11:token=accelerator;object=rsa-privkey?module-path=/opt/nfast/toolkits/pkcs11/libcknfast.so&amp;max-sessions=4&#10;</code></pre>
<p>Save the config file, restart <code>gokeyless</code>, and verify it started successfully.</p>
<pre><code class="language-sh">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
