<p>PhishNet is an add-in button that helps users to submit directly to Email security (formerly Area 1) <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8551.md")
</div> samples missed by Email security detection. PhishNet avoids the previous process, where users had to report phish to their email admins, which then had to manually download and forward the sample to Email security.
<h2 id="prerequisites">Prerequisites</h2>
<p>To set up PhishNet with Office 365, you will need:</p>
<ul>
<li>An Email security account with admin access.</li>
<li>Admin access to Microsoft.com.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8550.md")
</aside>
<h2 id="set-up-phishnet-for-office-365">Set up PhishNet for Office 365</h2>
<ol>
<li>
<p>Log in to <a href="https://admin.microsoft.com/">admin.microsoft.com</a> with your admin account.</p>
</li>
<li>
<p>Select the three-line button to open the menu.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> &gt; <strong>Integrated Apps</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step3-apps.png" alt="Select Integrated apps from the menu" /></p>
<ol start="4">
<li>Select <strong>Upload custom apps</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step4-custom-apps.png" alt="Select upload custom apps" /></p>
<ol start="5">
<li>
<p>On a new browser tab, <a href="https://horizon.area1security.com">log in to Email security (formerly Area 1)</a> with an admin account.</p>
</li>
<li>
<p>Select <strong>Settings</strong> (gear icon).</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step6-settings.png" alt="Select settings (the gear icon)" /></p>
<ol start="7">
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Phish Submissions</strong> &gt; <strong>PhishNet O365</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step7-phishnet.png" alt="The PhishNet settings will let you copy the appropriate URL to install it on Office 365" /></p>
<ol start="8">
<li>
<p>Select <strong>Copy</strong> to copy the URL. This URL will let you install PhishNet in Office 365.</p>
</li>
<li>
<p>Go back to the Microsoft admin browser tab.</p>
</li>
<li>
<p>From <strong>Upload Apps to deploy</strong>, select <strong>Provide link to manifest file</strong>, and paste the URL you copied from your Email security dashboard.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step10-upload-apps.png" alt="Paste the URL you have copied from Email security." /></p>
<ol start="11">
<li>
<p>Select <strong>Validate</strong>. Wait for a success message to appear below the input. Then, select <strong>Next</strong>.</p>
</li>
<li>
<p>Under <strong>Assign users</strong>, select <strong>Entire Organization</strong>, and then select <strong>Next</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step12.png" alt="Paste the URL you have copied from Email security." /></p>
<ol start="13">
<li>In <strong>App Permissions and Capabilities</strong>, make sure PhishNet has the correct permissions: <code>Outlook: ReadWriteMailbox, SendReceiveData</code>. Then, select <strong>Next</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step13.png" alt="Make sure PhishNet has the correct permissions." /></p>
<ol start="14">
<li>
<p>In the next screen, make sure that in <strong>Assigned Users</strong> you have <strong>Entire organization</strong>. Then, select <strong>Finish Deployment</strong>.</p>
</li>
<li>
<p>Once deployment is complete, you should see a message confirming it. Note that it can take up to six hours for PhishNet to appear in Office 365 (or six hours to update if previously installed.) Select <strong>Done</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step15.png" alt="PhishNet might take up to six hours to appear in Office 365." /></p>
<p>You have now installed PhishNet for Office 365. After the process is complete, PhishNet will show up on the Integrated Apps screen.</p>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/phishnet-installed-apps.png" alt="Search for PhishNet in the Integrated Apps screen." /></p>
<h2 id="submit-phish-with-phishnet">Submit phish with PhishNet</h2>
<ol>
<li>
<p>Open the message you would like to flag as either spam or phish.</p>
</li>
<li>
<p>Select the PhishNet logo in the task pane, near the other action buttons - such as reply and forward.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8549.md")
</aside>
<ol start="3">
<li>Under <strong>Select Submission Type</strong>, select the type of your submission - Spam or Phish.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-o365/step3-submit-phish.png" alt="Choose the type of submission you would like to make" /></p>
<ol start="4">
<li>Select <strong>Submit Report</strong>.</li>
</ol>
<p>Once the email has been successfully submitted to Email security for review, PhishNet will show you a <strong>Submission Complete</strong> message.</p>
