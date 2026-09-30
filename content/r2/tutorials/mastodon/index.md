<p><a href="https://joinmastodon.org/">Mastodon</a> is a popular <a href="https://en.wikipedia.org/wiki/Fediverse">fediverse</a> software. This guide will explain how to configure R2 to be the object storage for a self hosted Mastodon instance, for either <a href="#set-up-a-new-instance">a new instance</a> or <a href="#migrate-to-r2">an existing instance</a>.</p>
<h2 id="set-up-a-new-instance">Set up a new instance</h2>
<p>You can set up a self hosted Mastodon instance in multiple ways. Refer to the <a href="https://docs.joinmastodon.org/">official documentation</a> for more details. When you reach the <a href="https://docs.joinmastodon.org/admin/config/#files">Configuring your environment</a> step in the Mastodon documentation after installation, refer to the procedures below for the next steps.</p>
<h3 id="1-determine-the-hostname-to-access-files"><ol>
<li>Determine the hostname to access files</li>
</ol></h3>
<p>Different from the default hostname of your Mastodon instance, object storage for files requires a unique hostname. As an example, if you set up your Mastodon's hostname to be <code>mastodon.example.com</code>, you can use <code>mastodon-files.example.com</code> or <code>files.example.com</code> for accessing files. This means that when visiting your instance on <code>mastodon.example.com</code>, whenever there are media attached to a post such as an image or a video, the file will be served under the hostname determined at this step, such as <code>mastodon-files.example.com</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11362.md")
</aside>
<h3 id="2-create-and-set-up-an-r2-bucket"><ol start="2">
<li>Create and set up an R2 bucket</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create bucket**.
3. Enter your bucket name and then select **Create bucket**. This name is internal when setting up your Mastodon instance and is not publicly accessible.
4. Once the bucket is created, navigate to the **Settings** tab of this bucket and copy the value of **S3 API**.
5. From the **Settings** tab, select **Connect Domain** and enter the hostname from step 1.
6. Navigate back to the R2's overview page and select **Manage R2 API Tokens**.
7. Select **Create API token**.
8. Name your token `Mastodon` by selecting the pencil icon next to the API name and grant it the **Edit** permission. Select **Create API Token** to finalize token creation.
9. Copy the values of **Access Key ID** and **Secret Access Key**.
<h3 id="3-configure-r2-for-mastodon"><ol start="3">
<li>Configure R2 for Mastodon</li>
</ol></h3>
<p>While configuring your Mastodon instance based on the official <a href="https://github.com/mastodon/mastodon/blob/main/.env.production.sample">configuration file</a>, replace the <strong>File storage</strong> section with the following details.</p>
<pre><code>S3_ENABLED=true&#10;S3_ALIAS_HOST={{mastodon-files.example.com}}                  # Change to the hostname determined in step 1&#10;S3_BUCKET={{your-bucket-name}}                                # Change to the bucket name set in step 2&#10;S3_ENDPOINT=https://{{unique-id}}.r2.cloudflarestorage.com/   # Change the {{unique-id}} to the part of S3 API retrieved in step 2&#10;AWS_ACCESS_KEY_ID={{your-access-key-id}}                      # Change to the Access Key ID retrieved in step 2&#10;AWS_SECRET_ACCESS_KEY={{your-secret-access-key}}              # Change to the Secret Access Key retrieved in step 2&#10;S3_PROTOCOL=https&#10;S3_PERMISSION=&#10;</code></pre>
<p>Leave <code>S3_PERMISSION</code> empty. This prevents Mastodon from sending ACL headers, which R2 does not support.</p>
<p>After configuration, you can run your instance. After the instance is running, upload a media attachment and verify the attachment is retrieved from the hostname set above. When navigating back to the bucket's page in R2, you should see the following structure.</p>
<p><img src="/assets/upstream/images/r2/mastodon-r2-bucket-structure.png" alt="Mastodon bucket structure after instance is set up and running" /></p>
<h2 id="migrate-to-r2">Migrate to R2</h2>
<p>If you already have an instance running, you can migrate the media files to R2 and benefit from <a href="/r2/pricing/">no egress cost</a>.</p>
<h3 id="1-set-up-an-r2-bucket-and-start-file-migration"><ol>
<li>Set up an R2 bucket and start file migration</li>
</ol></h3>
<ol>
<li>(Optional) To minimize the number of migrated files, you can use the <a href="https://docs.joinmastodon.org/admin/tootctl/#media">Mastodon admin CLI</a> to clean up unused files.</li>
<li>Set up an R2 bucket ready for file migration by following steps 1 and 2 from <a href="#set-up-a-new-instance">Setting up a new instance</a> section above.</li>
<li>Migrate all the media files to R2. Refer to the <a href="/r2/examples/">examples</a> provided to connect various providers together. If you currently host these media files locally, you can use <a href="/r2/examples/rclone/"><code>rclone</code></a> to upload these local files to R2.</li>
</ol>
<h3 id="2-optional-set-up-file-path-redirects"><ol start="2">
<li>(Optional) Set up file path redirects</li>
</ol></h3>
<p>While the file migration is in progress, which may take a while, you can prepare file path redirect settings.</p>
<p>If you had the media files hosted locally, you will likely need to set up redirects. By default, media files hosted locally would have a path similar to <code>https://mastodon.example.com/cache/...</code>, which needs to be redirected to a path similar to <code>https://mastodon-files.example.com/cache/...</code> after the R2 bucket is up and running alongside your Mastodon instance. If you already use another S3 compatible object storage service and would like to keep the same hostname, you do not need to set up redirects.</p>
<p><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a> are available for all plans. Refer to <a href="/rules/url-forwarding/bulk-redirects/create-dashboard/">Create Bulk Redirects in the dashboard</a> for more information.</p>
<p><img src="/assets/upstream/images/r2/mastodon-r2-bulk-redirects.png" alt="List of Source URLs and their new Target URLs as part of Bulk Redirects" /></p>
<h3 id="3-verify-bucket-and-redirects"><ol start="3">
<li>Verify bucket and redirects</li>
</ol></h3>
<p>Depending on your migration plan, you can verify if the bucket is accessible publicly and the redirects work correctly. To verify, open an existing uploaded media file with a path like <code>https://mastodon.example.com/cache/...</code> and replace the hostname from <code>mastodon.example.com</code> to <code>mastodon-files.example.com</code> and visit the new path. If the file opened correctly, proceed to the final step.</p>
<h3 id="4-finalize-migration"><ol start="4">
<li>Finalize migration</li>
</ol></h3>
<p>Your instance may be still running during migration, and during migration, you likely have new media files created either through direct uploads or fetched from other federated instances. To upload only the newly created files, you can use a program like <a href="/r2/examples/rclone/"><code>rclone</code></a>. Note that when re-running the sync program, all existing files will be checked using at least <a href="/r2/pricing/#class-b-operations">Class B operations</a>.</p>
<p>Once all the files are synced, you can restart your Mastodon instance with the new object storage configuration as mentioned in <a href="#3-configure-r2-for-mastodon">step 3</a> of Set up a new instance.</p>
