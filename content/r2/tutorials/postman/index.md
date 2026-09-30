<p class="article-summary">Learn how to configure Postman to interact with R2.</p>
<p>Postman is an API platform that makes interacting with APIs easier. This guide will explain how to use Postman to make authenticated R2 requests to create a bucket, upload a new object, and then retrieve the object. The R2 <a href="https://www.postman.com/cloudflare-r2/workspace/cloudflare-r2/collection/20913290-14ddd8d8-3212-490d-8647-88c9dc557659?action=share&amp;creator=20913290">Postman collection</a> includes a complete list of operations supported by the platform.</p>
<h2 id="1-purchase-r2"><ol>
<li>Purchase R2</li>
</ol></h2>
<p>This guide assumes that you have made a Cloudflare account and purchased R2.</p>
<h2 id="2-explore-r2-in-postman"><ol start="2">
<li>Explore R2 in Postman</li>
</ol></h2>
<p>Explore R2's publicly available <a href="https://www.postman.com/cloudflare-r2/workspace/cloudflare-r2/collection/20913290-14ddd8d8-3212-490d-8647-88c9dc557659?action=share&amp;creator=20913290">Postman collection</a>. The collection is organized into a <code>Buckets</code> folder for bucket-level operations and an <code>Objects</code> folder for object-level operations. Operations in the <code>Objects &gt; Upload</code> folder allow for adding new objects to R2.</p>
<h2 id="3-configure-your-r2-credentials"><ol start="3">
<li>Configure your R2 credentials</li>
</ol></h2>
<p>In the <a href="https://www.postman.com/cloudflare-r2/workspace/cloudflare-r2/collection/20913290-14ddd8d8-3212-490d-8647-88c9dc557659?action=share&amp;creator=20913290&amp;ctx=documentation">Postman dashboard</a>, select the <strong>Cloudflare R2</strong> collection and navigate to the <strong>Variables</strong> tab. In <strong>Variables</strong>, you can set variables within the R2 collection. They will be used to authenticate and interact with the R2 platform. Remember to always select <strong>Save</strong> after updating a variable.</p>
<p>To execute basic operations, you must set the <code>account-id</code>, <code>r2-access-key-id</code>, and <code>r2-secret-access-key</code> variables in the Postman dashboard &gt; <strong>Variables</strong>.</p>
<p>To do this:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. In **R2**, under **Manage R2 API Tokens** on the right side of the dashboard, copy your Cloudflare account ID.
3. Go back to the [Postman dashboard](https://www.postman.com/cloudflare-r2/workspace/cloudflare-r2/collection/20913290-14ddd8d8-3212-490d-8647-88c9dc557659?action=share\&creator=20913290\&ctx=documentation).
4. Set the **CURRENT VALUE** of `account-id` to your Cloudflare account ID and select **Save**.
<p>Next, generate an R2 API token:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. On the right hand sidebar, select **Manage R2 API Tokens**.
3. Select **Create API token**.
4. Name your token **Postman** by selecting the pencil icon next to the API name and grant it the **Edit** permission.
<p>Guard this token and the <strong>Access Key ID</strong> and <strong>Secret Access Key</strong> closely. You will not be able to review these values again after finishing this step. Anyone with this information can fully interact with all of your buckets.</p>
<p>After you have created your API token in the Cloudflare dashboard:</p>
<ol>
<li>Go to the <a href="https://www.postman.com/cloudflare-r2/workspace/cloudflare-r2/collection/20913290-14ddd8d8-3212-490d-8647-88c9dc557659?action=share&amp;creator=20913290&amp;ctx=documentation">Postman dashboard</a> &gt; <strong>Variables</strong>.</li>
<li>Copy <code>Access Key ID</code> value from the Cloudflare dashboard and paste it into Postman’s <code>r2-access-key-id</code> variable value and select <strong>Save</strong>.</li>
<li>Copy the <code>Secret Access Key</code> value from the Cloudflare dashboard and paste it into Postman’s <code>r2-secret-access-key</code> variable value and select <strong>Save</strong>.</li>
</ol>
<p>By now, you should have <code>account-id</code>, <code>r2-secret-access-key</code>, and <code>r2-access-key-id</code> set in Postman.</p>
<p>To verify the token:</p>
<ol>
<li>In the Postman dashboard, select the <strong>Cloudflare R2</strong> folder dropdown arrow &gt; <strong>Buckets</strong> folder dropdown arrow &gt; <strong><code>GET</code>ListBuckets</strong>.</li>
<li>Select <strong>Send</strong>.</li>
</ol>
<p>The Postman collection uses AWS SigV4 authentication to complete the handshake.</p>
<p>You should see a <code>200 OK</code> response with a list of existing buckets. If you receive an error, ensure your R2 subscription is active and Postman variables are saved correctly.</p>
<h2 id="4-create-a-bucket"><ol start="4">
<li>Create a bucket</li>
</ol></h2>
<p>In the Postman dashboard:</p>
<ol>
<li>Go to <strong>Variables</strong>.</li>
<li>Set the <code>r2-bucket</code> variable value as the name of your R2 bucket and select <strong>Save</strong>.</li>
<li>Select the <strong>Cloudflare R2</strong> folder dropdown arrow &gt; <strong>Buckets</strong> folder dropdown arrow &gt; <strong><code>PUT</code>CreateBucket</strong> and select <strong>Send</strong>.</li>
</ol>
<p>You should see a <code>200 OK</code> response. If you run the <code>ListBuckets</code> request again, your bucket will appear in the list of results.</p>
<h2 id="5-add-an-object"><ol start="5">
<li>Add an object</li>
</ol></h2>
<p>You will now add an object to your bucket:</p>
<ol>
<li>Go to <strong>Variables</strong> in the Postman dashboard.</li>
<li>Set <code>r2-object</code> to <code>cat-pic.jpg</code> and select <strong>Save</strong>.</li>
<li>Select <strong>Cloudflare R2</strong> folder dropdown arrow &gt; <strong>Objects</strong> folder dropdown arrow &gt; <strong>Multipart</strong> folder dropdown arrow &gt; <strong><code>PUT</code>PutObject</strong> and select <strong>Send</strong>.</li>
<li>Go to <strong>Body</strong> and choose <strong>binary</strong> before attaching your cat picture.</li>
<li>Select <strong>Send</strong> to add the cat picture to your R2 bucket.</li>
</ol>
<p>After a few seconds, you should receive a <code>200 OK</code> response.</p>
<h2 id="6-get-an-object"><ol start="6">
<li>Get an object</li>
</ol></h2>
<p>It only takes a few more more clicks to download our cat friend using the <code>GetObject</code> request.</p>
<ol>
<li>Select the <strong>Cloudflare R2</strong> folder dropdown arrow &gt; <strong>Objects</strong> folder dropdown arrow &gt; <strong><code>GET</code>GetObject</strong>.</li>
<li>Select <strong>Send</strong>.</li>
</ol>
<p>The R2 team will keep this collection up to date as we expand R2 features set. You can explore the rest of the R2 Postman collection by experimenting with other operations.</p>
