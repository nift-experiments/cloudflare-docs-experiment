<p>This tutorial uses <a href="https://cloud.google.com/kms/docs/hsm">Google Cloud HSM</a> — a FIPS 140-2 Level 3 certified implementation.</p>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>Make sure that you have:</p>
<ul>
<li>Set up your <a href="https://cloud.google.com/kms/docs/quickstart#before-you-begin">Google Cloud project</a></li>
</ul>
<hr />
<h2 id="1-create-a-key-ring"><ol>
<li>Create a key ring</li>
</ol></h2>
<p>To set up the Google Cloud HSM, <a href="https://cloud.google.com/kms/docs/hsm#kms-create-key-hsm-web">create a key ring</a> and indicate its location.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/14202.md")
</aside>
<hr />
<h2 id="2-create-a-key"><ol start="2">
<li>Create a key</li>
</ol></h2>
<p>Create a key, including the following information:</p>
<table>
<thead>
<tr>
<th width="25%">Field</th>
<th width="25%">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key ring</td>
<td>
				The key ring you created in <b>Step 2</b>
</td>
</tr>
<tr>
<td>Protection level</td>
<td>HSM</td>
</tr>
<tr>
<td>Purpose</td>
<td>Asymmetric Encrypt</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="3-import-the-private-key"><ol start="3">
<li>Import the private key</li>
</ol></h2>
<p>After creating a key ring and key, <a href="https://cloud.google.com/kms/docs/importing-a-key">import the private key</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note:</h3>
@markup("md", "content/.markup/bodies/14201.md")
</aside>
<hr />
<h2 id="4-modify-your-gokeyless-config-file-and-restart-the-service"><ol start="4">
<li>Modify your gokeyless config file and restart the service</li>
</ol></h2>
<p>Once you’ve imported the key, copy the <strong>Resource name</strong> from the UI. Then, add this value to the <code>gokeyless</code> YAML file under <code>private_key_stores</code>.</p>
<p>With the config file saved, restart <code>gokeyless</code> and verify it started successfully.</p>
<pre><code class="language-sh">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
