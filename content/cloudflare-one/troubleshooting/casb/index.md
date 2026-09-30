<p>Use this guide to troubleshoot common issues with Cloud Access Security Broker (CASB).</p>
<h2 id="security-findings">Security findings</h2>
<h3 id="findings-not-appearing">Findings not appearing</h3>
If you do not see findings for an integrated application:
- **Wait for scan**: Initial scans can take up to 24 hours depending on the size of the application.
- **Permissions**: Ensure the account used to integrate the application has the necessary administrative permissions.
- **Enabled status**: Verify that the integration is enabled in the Zero Trust dashboard.
<h3 id="false-positives">False positives</h3>
If CASB flags a configuration that is intended for your organization:
1. Go to **CASB** &gt; **Findings**.
2. Select the finding and choose **Dismiss**.
3. Provide a reason for dismissal to help refine future scans.
<hr />
<h2 id="more-casb-resources">More CASB resources</h2>
<p>For more information, refer to the full CASB documentation.</p>
<p><a class="nb-link-button" href="/cloudflare-one/integrations/cloud-and-saas/troubleshooting/">CASB troubleshooting ❯</a></p>
