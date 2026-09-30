<p>This tutorial uses <a href="https://azure.microsoft.com/en-us/updates/akv-managed-hsm-public-preview/">Microsoft Azure’s Managed HSM</a> — a FIPS 140-2 Level 3 certified implementation — to deploy a VM with the Keyless SSL daemon.</p>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>Make sure you have:</p>
<ul>
<li>Followed Microsoft's <a href="https://docs.microsoft.com/en-us/azure/key-vault/managed-hsm/quick-create-cli">tutorial</a> for provisioning and activating the managed HSM</li>
<li>Set up a VM for your key server</li>
</ul>
<hr />
<h2 id="1-create-a-vm"><ol>
<li>Create a VM</li>
</ol></h2>
<p>Create a VM where you will deploy the keyless daemon.</p>
<hr />
<h2 id="2-deploy-the-keyless-server"><ol start="2">
<li>Deploy the keyless server</li>
</ol></h2>
<p>Follow <a href="/ssl/keyless-ssl/configuration/cloudflare-tunnel/#4-set-up-and-activate-key-server">these instructions</a> to deploy your keyless server.</p>
<hr />
<h2 id="3-set-up-the-azure-cli"><ol start="3">
<li>Set up the Azure CLI</li>
</ol></h2>
<p>Set up the Azure CLI (used to access the private key).</p>
<p>For example, if you were using macOS:</p>
<pre><code class="language-bash">brew install azure-cli&#10;</code></pre>
<hr />
<h2 id="4-set-up-the-managed-hsm"><ol start="4">
<li>Set up the Managed HSM</li>
</ol></h2>
<ol>
<li>Log in through the Azure CLI and create a resource group for the Managed HSM in one of the supported regions:</li>
</ol>
<pre><code class="language-sh">az login&#10;az group create --name HSMgroup --location southcentralus&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14205.md")
</aside>
<ol start="2">
<li>
<p><a href="https://docs.microsoft.com/en-us/azure/key-vault/managed-hsm/quick-create-cli">Create, provision, and activate</a> the HSM.</p>
</li>
<li>
<p>Add your private key to the <code>keyvault</code>, which returns the URI you need for <strong>Step 4</strong>:</p>
</li>
</ol>
<pre><code>az keyvault key import --hsm-name &quot;KeylessHSM&quot; --name &quot;hsm-pub-keyless&quot; --pem-file server.key&#10;</code></pre>
<ol start="4">
<li>
<p>If the key server is running in an Azure VM in the same account, use <strong>Managed services</strong> for authorization:</p>
<ol>
<li>Enable managed services on the VM in the UI.</li>
<li>Give your service user (associated with your VM) HSM sign permissions</li>
</ol>
</li>
</ol>
<pre><code>az keyvault role assignment create  --hsm-name KeylessHSM --assignee $(az vm identity show --name &quot;hsmtestvm&quot; --resource-group &quot;HSMgroup&quot; --query principalId -o tsv) --scope / --role &quot;Managed HSM Crypto User&quot;&#10;</code></pre>
<ol start="5">
<li>In the <code>gokeyless</code> YAML file, add the URI from <strong>Step 2</strong> under <code>private_key_stores</code>. See our <a href="https://github.com/cloudflare/gokeyless/blob/master/README.md">README</a> for an example.</li>
</ol>
<h2 id="5-restart-gokeyless"><ol start="5">
<li>Restart gokeyless</li>
</ol></h2>
<p>Once you save the config file, restart <code>gokeyless</code> and verify that it started successfully:</p>
<pre><code class="language-bash">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
