<p>This guide will instruct you through setting up Microsoft 365 with Email security via the Cloudflare dashboard.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Email security, you will need to have:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>A <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a></li>
<li>A domain to protect</li>
</ul>
<h2 id="enable-email-security-via-the-dashboard">Enable Email security via the dashboard</h2>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and select <strong>Email security</strong>..</li>
<li>Select <strong>Overview</strong>. Select one of the following options depending on your use case:</li>
</ol>
<ul>
<li>If you have not purchased Email security, select <strong>Contact sales</strong>.</li>
<li>If you have not associated any integration:
<ul>
<li>Select <strong>Set up</strong>.</li>
<li>Choose <strong>MS Graph API</strong> &gt; <strong>Authorize</strong>.</li>
<li>Refer to <a href="#enable-microsoft-integration">Enable Microsoft integration</a> to continue the onboarding process.</li>
</ul>
</li>
<li>If you have associated an integration, but have not connected a domain:
<ul>
<li>Select <strong>Connect a domain</strong>.</li>
<li>Choose <strong>MS Graph API</strong>. Refer to <a href="#connect-your-domains">Connect your domains</a> to connect your domain(s).</li>
</ul>
</li>
</ul>
<h3 id="enable-microsoft-integration">Enable Microsoft integration</h3>
<p>To enable Microsoft integration:</p>
<ol>
<li><strong>Configure policy</strong>: Choose how <a href="/cloudflare-one/integrations/cloud-and-saas/">CASB</a> interacts with your data. Select <strong>Read-only mode</strong> or <strong>Read-Write mode</strong>. It is recommended that you choose <strong>Read-Write mode</strong>.</li>
<li><strong>Name integration</strong>: Add your integration name, then select <strong>Continue</strong>.</li>
<li><strong>Authorize integration</strong>:
<ul>
<li>Select <strong>Authorize</strong>. Selecting <strong>Authorize</strong> will take you to the Microsoft Sign in page where you will have to enter your email address.</li>
<li>Once you enter your email address, select <strong>Next</strong>.</li>
<li>After selecting <strong>Next</strong>, the system will show a dialog box with a list of requested permissions. Select <strong>Accept</strong> to authorize Email security. Upon authorization, you will be redirected to a page where you can review details and enroll integration.</li>
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
<p>On the <strong>Set up Email security</strong> page, you will be able to connect your Microsoft domains. To connect your domains:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(Optional) <strong>Modify default scanning</strong>: You can configure which folder Email security can scan.</li>
<li>(Optional - select <strong>Skip for now</strong> to skip this step) <strong>Redirect messages</strong>: Refer to <a href="/cloudflare-one/email-security/settings/auto-moves/">Auto-moves</a> to learn what auto-moves are, and how to configure auto-moves.</li>
<li><strong>Review details</strong>: Review your connected domains, then select <strong>Go to Domains</strong>.</li>
</ol>
<p>Your domains are now connected successfully.</p>
<h3 id="connect-new-domains">Connect new domains</h3>
<p>To connect new domains:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Select <strong>Add a domain</strong>.</li>
<li>Select a method for connecting your mail environment to Email security:
<ul>
<li>If you select <strong>MS Graph API</strong>, refer to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">Enable Microsoft integration</a>.</li>
<li>If you select BCC/Journaling, choose how to connect your domains:
<ul>
<li>If you select <strong>Integrate with MS</strong>, refer to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">Enable Microsoft integration</a>.</li>
<li>If you select <strong>Integrate with Google</strong>, refer to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/">Connect your domains</a>.</li>
<li>If you select <strong>Manual add</strong>, refer to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/#enter-domain-manually">Enter domain manually</a>.</li>
</ul>
</li>
</ul>
</li>
</ol>
<h2 id="prevent-cloudflare-from-scanning-a-domain">Prevent Cloudflare from scanning a domain</h2>
<p>If you want to prevent Cloudflare from scanning a domain:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>On the <strong>Domain management</strong> page, select the domain you do not want to be scanned.</li>
<li>Select the three dots &gt; <strong>Stop scanning</strong>.</li>
</ol>
<h2 id="view-an-integration">View an integration</h2>
<p>To view the integration for each connected domain:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Select a domain.</li>
<li>Select the three dots &gt; <strong>View integration</strong>.</li>
</ol>
<p>Once you have set up Email security to scan through your inbox, Email security will display detailed information about your inbox. Refer to <a href="/cloudflare-one/email-security/monitoring/">Monitor your inbox</a> to learn more.</p>
<h2 id="verify-successful-deployment">Verify successful deployment</h2>
<p>To verify that the deployment has been successful and that your emails are being scanned:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Under <strong>Your domains</strong>, locate your domain, and verify that <strong>Status</strong> (which describes the state of the configuration) displays <strong>Active</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Enable logs</a> to send detection data to an endpoint of your choice.</p>
