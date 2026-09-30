<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/14206.md")
</aside>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>Make sure you have:</p>
<ul>
<li>Provisioned an <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html">AWS CloudHSM cluster</a> .</li>
<li>Installed the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-install.html">appropriate software library for PKCS#11</a>.</li>
</ul>
<hr />
<h2 id="1-import-the-public-and-private-key-to-the-hsm"><ol>
<li>Import the public and private key to the HSM</li>
</ol></h2>
<p>Before importing the public key, extract it from the certificate provided by your CA. Place the contents of your private key in <code>privkey.pem</code> and then run the following (replacing certificate.pem with your actual certificate) to populate <code>pubkey.pm</code>.</p>
<pre><code class="language-txt">keyserver$ openssl x509 -pubkey -noout -in certificate.pem &gt; pubkey.pem&#10;</code></pre>
<p>Log in to the CloudHSM using a previously created <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-users.html#crypto-user">crypto user</a> (CU) account and generate a key encryption key that will be used to import your private key.</p>
<pre><code class="language-txt">keyserver$ /opt/cloudhsm/bin/key_mgmt_util&#10;Command: loginHSM -u CU -s patrick -p donahue&#10;Command: genSymKey -t 31 -s 16 -sess -l import-wrapping-key&#10;...&#10;Symmetric Key Created.  Key Handle: 658&#10;...&#10;</code></pre>
<p>Referencing the key handle returned above, import the private and public key and then log out of the HSM:</p>
<pre><code class="language-txt">Command: importPrivateKey -f privkey.pem -l mykey -id 1 -w 658&#10;...&#10;Cfm3WrapHostKey returned: 0x00 : HSM Return: SUCCESS&#10;Cfm3CreateUnwrapTemplate returned: 0x00 : HSM Return: SUCCESS&#10;Cfm3UnWrapKey returned: 0x00 : HSM Return: SUCCESS&#10;...&#10;Private Key Unwrapped.  Key Handle: 658&#10;&#10;&#10;Command: importPubKey -f pubkey.pem -l mykey -id 1&#10;Cfm3CreatePublicKey returned: 0x00 : HSM Return: SUCCESS&#10;...&#10;Public Key Handle: 941&#10;&#10;&#10;Command: logoutHSM&#10;Command: exit&#10;</code></pre>
<hr />
<h2 id="2-modify-the-gokeyless-config-file-and-restart-the-service"><ol start="2">
<li>Modify the gokeyless config file and restart the service</li>
</ol></h2>
<p>Now that the keys are in place, we need to modify the configuration file that the key server will read on startup. Change the <code>object=mykey</code> and <code>pin-value=username:password</code> values to match the key label you provided and CU user you created.</p>
<p>Open <code>/etc/keyless/gokeyless.yaml</code> and immediately after:</p>
<pre><code class="language-yaml">private_key_stores:&#10;  &#45; dir: /etc/keyless/keys&#10;</code></pre>
<p>add:</p>
<pre><code class="language-yaml">&#45; uri: pkcs11:token=cavium;object=mykey?module-path=/opt/cloudhsm/lib/libcloudhsm_pkcs11_standard.so&amp;pin-value=patrick:donahue&amp;max-sessions=1&#10;</code></pre>
<p>With the config file saved, restart <code>gokeyless</code> and verify it started successfully.</p>
<pre><code class="language-sh">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
