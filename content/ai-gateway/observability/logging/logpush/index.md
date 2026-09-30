<p>AI Gateway allows you to securely export logs to an external storage location, where you can decrypt and process them.
You can toggle Workers Logpush on and off in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> settings. This product is available on the Workers Paid plan. For pricing information, refer to <a href="/ai-gateway/reference/pricing">Pricing</a>.</p>
<p>This guide explains how to set up Workers Logpush for AI Gateway, generate an RSA key pair for encryption, and decrypt the logs once they are received.</p>
<p>You can store up to 10 million logs per gateway. If your limit is reached, new logs will stop being saved and will not be exported through Workers Logpush. To continue saving and exporting logs, you must delete older logs to free up space for new logs. Workers Logpush has a limit of 4 jobs and a maximum request size of 1 MB per log.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/2939.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/2938.md")
</aside>
<h2 id="how-logs-are-encrypted">How logs are encrypted</h2>
<p>We employ a hybrid encryption model efficiency and security. Initially, an AES key is generated for each log. This AES key is what actually encrypts the bulk of your data, chosen for its speed and security in handling large datasets efficiently.</p>
<p>Now, for securely sharing this AES key, we use RSA encryption. Here's what happens: the AES key, although lightweight, needs to be transmitted securely to the recipient. We encrypt this key with the recipient's RSA public key. This step leverages RSA's strength in secure key distribution, ensuring that only someone with the corresponding RSA private key can decrypt and use the AES key.</p>
<p>Once encrypted, both the AES-encrypted data and the RSA-encrypted AES key are sent together. Upon arrival, the recipient's system uses the RSA private key to decrypt the AES key. With the AES key now accessible, it is straightforward to decrypt the main data payload.</p>
<p>This method combines the best of both worlds: the efficiency of AES for data encryption with the secure key exchange capabilities of RSA, ensuring data integrity, confidentiality, and performance are all optimally maintained throughout the data lifecycle.</p>
<h2 id="setting-up-workers-logpush">Setting up Workers Logpush</h2>
<p>To configure Workers Logpush for AI Gateway, follow these steps:</p>
<h2 id="1-generate-an-rsa-key-pair-locally"><ol>
<li>Generate an RSA key pair locally</li>
</ol></h2>
<p>You need to generate a key pair to encrypt and decrypt the logs. This script will output your RSA privateKey and publicKey. Keep the private key secure, as it will be used to decrypt the logs. Below is a sample script to generate the keys using Node.js and OpenSSL.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="JSPlusSSL"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2942.md")
</div></div>
<h2 id="2-upload-public-key-to-gateway-settings"><ol start="2">
<li>Upload public key to gateway settings</li>
</ol></h2>
<p>Once you have generated the key pair, upload the public key to your AI Gateway settings. This key will be used to encrypt your logs. In order to enable Workers Logpush, you will need logs enabled for that gateway.</p>
<h2 id="3-set-up-logpush"><ol start="3">
<li>Set up Logpush</li>
</ol></h2>
<p>Uploading your public key enables Workers Logpush for the gateway, but logs will not be exported until you also create and enable a Logpush job that specifies where to send them. Both steps are required.</p>
<p>To create the Logpush job, choose your destination and follow the steps in the <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a> documentation. For example, to export logs to Cloudflare R2, refer to <a href="/logs/logpush/logpush-job/enable-destinations/r2/">Enable Cloudflare R2</a>. When configuring the job, select the AI Gateway dataset.</p>
<h2 id="4-receive-encrypted-logs"><ol start="4">
<li>Receive encrypted logs</li>
</ol></h2>
<p>After configuring Workers Logpush, logs will be sent encrypted using the public key you uploaded. To access the data, you will need to decrypt it using your private key. The logs will be sent to the object storage provider that you have selected.</p>
<h2 id="5-decrypt-logs"><ol start="5">
<li>Decrypt logs</li>
</ol></h2>
<p>To decrypt the encrypted log bodies and metadata from AI Gateway, you can use the following Node.js script or OpenSSL:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="JSPlusSSL"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2945.md")
</div></div>
