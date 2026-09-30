<p>You can secure access to R2 buckets using <a href="/cloudflare-one/access-controls/applications/http-apps/">Cloudflare Access</a>.</p>
<p>Access allows you to only allow specific users, groups or applications within your organization to access objects within a bucket, or specific sub-paths, based on policies you define.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11366.md")
</aside>
<h2 id="1-create-a-bucket"><ol>
<li>Create a bucket</li>
</ol></h2>
<p><em>If you have an existing R2 bucket, you can skip this step.</em></p>
<p>You will need to create an R2 bucket. Follow the <a href="/r2/get-started/">R2 get started guide</a> to create a bucket before returning to this guide.</p>
<h2 id="2-create-an-access-application"><ol start="2">
<li>Create an Access application</li>
</ol></h2>
<p>Within the <strong>Zero Trust</strong> section of the Cloudflare Dashboard, you will need to create an Access application and a policy to restrict access to your R2 bucket.</p>
<p>If you have not configured Cloudflare Access before, we recommend:</p>
<ul>
<li>Configuring an <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> first to enable Access to use your organization's single-sign on (SSO) provider as an authentication method.</li>
</ul>
<p>To create an Access application for your R2 bucket:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong> and select <strong>Create new application</strong>.</li>
<li>Select <strong>Self-hosted and private</strong>.</li>
<li>Select <strong>Add public hostname</strong> and enter the application domain. The <strong>Domain</strong> must be a domain hosted on Cloudflare, and the <strong>Subdomain</strong> part of the custom domain you will connect to your R2 bucket. For example, if you want to serve files from <code>behind-access.example.com</code> and <code>example.com</code> is a domain within your Cloudflare account, then enter <code>behind-access</code> in the subdomain field and select <code>example.com</code> from the <strong>Domain</strong> list.</li>
<li>Add <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to control who can connect to your application. This should be an <strong>Allow</strong> policy so that users can access objects within the bucket behind this Access application.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11365.md")
</aside>
<ol start="6">
<li>Follow the remaining <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application creation steps</a> to publish the application.</li>
</ol>
<h2 id="3-connect-a-custom-domain"><ol start="3">
<li>Connect a custom domain</li>
</ol></h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11364.md")
</aside>
<p>You will need to <a href="/r2/buckets/public-buckets/#connect-a-bucket-to-a-custom-domain">connect a custom domain</a> to your bucket in order to configure it as an Access application. Make sure the custom domain <strong>is the same domain</strong> you entered when configuring your Access policy.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your bucket.
3. Select **Settings**.
4. Under **Custom Domains**, select **Add**.
5. Enter the domain name you want to connect to and select **Continue**.
6. Review the new record that will be added to the DNS table and select **Connect Domain**.
<p>Your domain is now connected. The status takes a few minutes to change from <strong>Initializing</strong> to <strong>Active</strong>, and you may need to refresh to review the status update. If the status has not changed, select the <em>...</em> next to your bucket and select <strong>Retry connection</strong>.</p>
<h2 id="4-test-your-access-policy"><ol start="4">
<li>Test your Access policy</li>
</ol></h2>
<p>Visit the custom domain you connected to your R2 bucket, which should present a Cloudflare Access authentication page with your selected identity provider(s) and/or authentication methods.</p>
<p>For example, if you connected Google and/or GitHub identity providers, you can log in with those providers. If the login is successful and you pass the Access policies configured in this guide, you will be able to access (read/download) objects within the R2 bucket.</p>
<p>If you cannot authenticate or receive a block page after authenticating, check that you have an <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/#1-add-your-application-to-access">Access policy</a> configured within your Access application that explicitly allows the group your user account is associated with.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/cloudflare-one/access-controls/applications/http-apps/">Access applications</a> and how to configure them.</li>
<li>Understand how to use <a href="/r2/api/s3/presigned-urls/">pre-signed URLs</a> to issue time-limited and prefix-restricted access to objects for users not within your organization.</li>
<li>Review the <a href="/r2/api/tokens/">documentation on using API tokens to authenticate</a> against R2 buckets.</li>
</ul>
