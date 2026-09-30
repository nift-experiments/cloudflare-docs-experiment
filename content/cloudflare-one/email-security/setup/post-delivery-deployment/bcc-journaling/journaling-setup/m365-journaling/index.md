<p>Microsoft 365 journaling is a post-delivery setup method that ensures a copy of every incoming and outgoing email is forwarded to Cloudflare for analysis. When you create a <a href="https://learn.microsoft.com/en-us/exchange/security-and-compliance/journaling/journaling#journal-rules">journal rule</a> in the Microsoft Purview compliance portal, Cloudflare can scan messages that have already landed in your inbox.</p>
<p>The following diagram shows how this works:</p>
<p><img src="/assets/upstream/email-security/M365Deployment_Journaling.png" alt="Email flow when setting up Microsoft 365 with Email security." /></p>
<p>To enable Microsoft 365 journaling deployment:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Select <strong>Overview</strong>. If you have not purchased Email security, select <strong>Contact Sales</strong>. Otherwise, select <strong>Set up</strong> &gt; <strong>BCC/Journaling</strong>.</li>
<li>Select <strong>Integrate with MS</strong> &gt; <strong>Authorize</strong>.</li>
<li>Continue with <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/m365-journaling/#1-integrate-with-microsoft-365">Integrate with Microsoft 365</a> to connect your Microsoft integration.</li>
</ol>
<h2 id="1-integrate-with-microsoft-365"><ol>
<li>Integrate with Microsoft 365</li>
</ol></h2>
<p>To integrate with Microsoft 365:</p>
<ol>
<li><strong>Name integration</strong>: Add your integration name, then select <strong>Continue</strong>.</li>
<li><strong>Authorize integration</strong>:
<ul>
<li>Select <strong>Authorize</strong>. Selecting <strong>Authorize</strong> will take you to the <strong>Microsoft Sign in</strong> page where you will have to enter your email address.</li>
<li>Once you enter your email address, select <strong>Next</strong>.</li>
<li>After selecting <strong>Next</strong>, the dashboard will show you a dialog box with a list of requested permissions. Select <strong>Accept to authorize Email security</strong>. Upon authorization, you will be redirected to a page where you can review details and enroll the integration.</li>
</ul>
</li>
<li><strong>Review details</strong>: Review your integration details, then:
<ul>
<li>Select <strong>Complete Email security set up</strong> where you will be able to connect your domains and configure auto-moves.</li>
<li>Select <strong>Continue to Email security</strong>.</li>
</ul>
</li>
</ol>
<p>Continue with <a href="#connect-your-domains">Connect your domains</a> for the next steps.</p>
<h3 id="connect-your-domains">Connect your domains</h3>
<p>On the <strong>Set up Email security</strong> page:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Add manual domains</strong>: Select <strong>Add domain name</strong> to manually enter additional domains. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Adjust hop count</strong>: Enter the number of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/4948.md")
</div>. Then, select **Continue**.
4. (**Optional**, select **Skip for now** to skip this step) **Move messages**: Refer to [Auto-moves](/cloudflare-one/email-security/settings/auto-moves/) to configure auto-moves. Then, select **Continue**.
5. **Select your processing location**: Configure where you want Cloudflare to [process your email](/cloudflare-one/email-security/reference/regional-processing/). **Global** will be the default option. If you choose **Global**, `<account tag>@CF-emailsecurity.com` will be your regional service address. Once you have chosen your processing location, select **Continue**.
6. **Review details**: Review your connected domains and service addresses. Then, select **Go to domains.**
<p>Your domains are now added successfully.</p>
<p>To view your connected domains:</p>
<ol>
<li>Go to <strong>Settings</strong>.</li>
<li>Locate your domain, select the three dots &gt; <strong>View domain</strong>. Selecting <strong>View domain</strong> will display information about your domain.</li>
</ol>
<h2 id="2-configure-journal-rule"><ol start="2">
<li>Configure journal rule</li>
</ol></h2>
<ol>
<li>
<p>Log in to the <a href="https://compliance.microsoft.com/homepage">Microsoft Purview compliance portal</a>.</p>
</li>
<li>
<p>On the sidebar, go to <strong>Settings</strong> (the gear icon) &gt; <strong>Data Lifecycle Management</strong> &gt; <strong>Exchange (legacy)</strong>.</p>
</li>
<li>
<p>In <strong>Send undeliverable journal reports to</strong> enter the email address of a valid user account. Note that you cannot use a team or group address. Select <strong>Save</strong> once you entered the email address.</p>
</li>
<li>
<p>On the sidebar, go to <strong>Solutions</strong> &gt; <strong>Data Lifecycle Management</strong> &gt; <strong>Exchange (legacy)</strong>.</p>
</li>
<li>
<p>Select <strong>Journal rules</strong>.</p>
</li>
<li>
<p>Select <strong>New rule</strong> to configure a journaling rule, and configure it as follows:</p>
<ul>
<li><strong>Send journal reports to</strong>: This is the address you copied and pasted in step 5 of <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/m365-journaling/#connect-your-domains">Connect your domains</a>.</li>
<li><strong>Journal rule name</strong>: <code>Journal Messages to Email security</code></li>
<li><strong>Journal messages sent or received from</strong>: <em>Everyone</em></li>
<li><strong>Type of message to journal</strong>: <em>External messages only</em></li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Verify the information is correct, and select <strong>Submit</strong> &gt; <strong>Done</strong>.</p>
</li>
</ol>
<p>Once saved, the rule is automatically active. However, it may take a few minutes for the configuration to propagate and start pushing messages to Email security. After it propagates, you can <a href="/cloudflare-one/email-security/monitoring/">monitor your inbox</a> in the Cloudflare dashboard to check the number of messages processed. This number will grow as journaled messages are sent to Email security from your Exchange server.</p>
<h2 id="verify-successful-deployment">Verify successful deployment</h2>
<p>To verify that the deployment has been successful and that your emails are being scanned:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Under <strong>Your domains</strong>, locate your domain, and verify that <strong>Status</strong> (which describes the state of the configuration) displays <strong>Active</strong>.</li>
</ol>
<h2 id="verify-successful-addition">Verify successful addition</h2>
<p>To verift that your domain has been added successfully and that your emails are being scanned:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Under <strong>Your domains</strong>, locate your domain, and verify that <strong>Status</strong> is set to <strong>Active</strong>. The <strong>Configured method</strong> should be <strong>BCC/Journaling</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Enable logs</a> to send detection data to an endpoint of your choice.</p>
