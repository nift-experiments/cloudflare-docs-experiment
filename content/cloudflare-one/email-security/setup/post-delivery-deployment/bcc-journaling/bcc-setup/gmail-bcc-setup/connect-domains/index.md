<p>To connect your domains, you will need to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/#enable-gmail-bcc-integration">enable your Gmail BCC integration</a>. Once you have enabled your Gmail BCC integration, the Cloudflare dashboard will redirect you to the <strong>Set up Email security</strong> page.</p>
<p>On the <strong>Set up Email security</strong> page:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Add manual domains</strong>: Select <strong>Add domain name</strong> to manually enter additional domains. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Adjust hop count</strong>: Enter the number of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/4954.md")
</div>. Then, select **Continue**. Configuring the hop count will determine where you want Cloudflare to sit in the email processing chain.
4. (**Optional**, select **Skip for now** to skip this step) **Move messages**: Refer to [Auto-moves](/cloudflare-one/email-security/settings/auto-moves/) to configure auto-moves. Then, select **Continue**.
5. **Select your processing location**: Configure where you want Cloudflare to process your email. **Global** will be the default option. If you choose **Global**, `<account tag>@CF-emailsecurity.com` will be your regional service address. Once you have chosen your processing location, select **Continue**. Refer to [Regional processing](/cloudflare-one/email-security/reference/regional-processing/) to learn more.
6. **Review details**: Review your connected domains and service addresses. Then, select **Go to domains.**
<p>Your domains are now added successfully.</p>
<p>On the <strong>Domains</strong> page, select the three dots &gt; <strong>View integration</strong>. The dashboard will display your <a href="/cloudflare-one/email-security/settings/domain-management/domain/">domain information</a>.</p>
<p>Under <strong>Source</strong>, the dashboard will display <strong>Google integration</strong>, along with the <strong>Integration name</strong>.</p>
<h2 id="add-additional-domains">Add additional domains</h2>
<p>To add additional domains:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong> &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Connect an integration</strong> &gt; <strong>BCC/Journaling</strong> &gt; <strong>Integrate with Google</strong> &gt; <strong>Authorize</strong>.</li>
<li><strong>Connect domains</strong>: Select the domains you want to add, then select <strong>Next</strong>.</li>
<li>(Optional) Select <strong>Add manual domains</strong>: Enter additional domains manually, then select <strong>Next</strong>.</li>
<li>(Optional) Select <strong>Adjust hop count</strong>: Enter the number of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/4955.md")
</div>.
6. **Review details**: Review your selected domains, then use the following email to configure the service address with your third-party email provider:
<pre><code class="language-txt">&lt;account tag&gt;@CF-emailsecurity.com&#10;</code></pre>
<ol start="7">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="verify-successful-deployment">Verify successful deployment</h2>
<p>To verify that the deployment has been successful and that your emails are being scanned:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Under <strong>Your domains</strong>, locate your domain, and verify that <strong>Status</strong> (which describes the state of the configuration) displays <strong>Active</strong>.</li>
</ol>
