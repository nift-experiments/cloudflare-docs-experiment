<p>This page will teach you how to manually add domains via BCC/Journaling on the Cloudflare dashboard.</p>
<p>This setup is ideal if your email provider is not Microsoft 365 or Google Workspace, or you do not want to directly integrate your account. Beware that manually add does not support <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move</a> or <a href="/cloudflare-one/email-security/directories/">directory synchronization</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Email security, you will need to have:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>A <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a></li>
<li>A domain to protect</li>
</ul>
<h2 id="manually-add-domains">Manually add domains</h2>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Select <strong>Overview</strong>. If you have not purchased Email security, select <strong>Contact Sales</strong>. Otherwise, select <strong>Set up</strong> &gt; <strong>BCC/Journaling</strong>.</li>
<li>Select <strong>Manual add</strong>.</li>
</ol>
<h2 id="users-with-domains-on-cloudflare">Users with domains on Cloudflare</h2>
<p>On the <strong>Set up Email security</strong> page:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Add manual domains</strong>: Manually enter additional domains. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Adjust hop count</strong>: Enter the number of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/4946.md")
</div>, and then select **Continue**.
4. **Select your processing location**: Configure where you want Cloudflare to process your email. **Global** will be the default option. If you choose **Global**, `<account tag>@CF-emailsecurity.com` will be your regional service address. Once you have chosen your processing location, select **Continue**.
5. **Review details**: Review your connected domains and regional service address. Then, select **Go to domains.**
<h2 id="users-who-do-not-have-domains-with-cloudflare">Users who do not have domains with Cloudflare</h2>
<p>If you do not have domains with Cloudflare, the Cloudflare dashboard will display two options:</p>
<ul>
<li>Add a domain to Cloudflare.</li>
<li>Enter domain manually.</li>
</ul>
<h3 id="add-a-domain-to-cloudflare">Add a domain to Cloudflare</h3>
<p>Selecting <strong>Add a domain to Cloudflare</strong> will redirect you to a new page where you will connect your domain to Cloudflare. Once you have entered an existing domain, select <strong>Continue</strong>.</p>
<h3 id="enter-domain-manually">Enter domain manually</h3>
<p>On the <strong>Set up Email security</strong> page:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Add manual domains</strong>: Manually enter additional domains. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Adjust hop count</strong>: Enter the number of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/4947.md")
</div>, and then select **Continue**.
4. **Configure service address with your third party email provider**: Copy and paste the service address into your third-party email provider to allow BCC/Journaling: `<account tag>@CF-emailsecurity.com`.
5. **Review details**: Review your connected domains. Then, select **Go to domains.**
<h2 id="enable-auto-moves">Enable auto-moves</h2>
<p>To enable auto-move events, you will have to associate an integration.</p>
<p>To associate an integration:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong> &gt; Select <strong>View</strong>.</li>
<li>On the <strong>Domain management</strong> page, locate your domain, select the three dots, then select <strong>Associate an integration</strong>.</li>
<li>Select <strong>Connect an integration</strong>. Follow the steps to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">enable the Microsoft 365 integration</a>.</li>
<li>Select the three dots, then select <strong>Associate an integration</strong>. Select the integration, then select <strong>Associate</strong>.</li>
</ol>
<p>Now that your domain has an associated integration, enable <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move events</a> on your domain.</p>
