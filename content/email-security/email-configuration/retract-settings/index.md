<p>When you are using an <a href="/email-security/deployment/api/">API setup</a> for Email security, you cannot prevent mail from reaching a recipient's mailbox.</p>
<p>However — so long as you also have <a href="/email-security/deployment/api/setup/#journaling-setup">journaling</a>, <a href="/email-security/deployment/api/setup/#bcc-setup">BCC</a> or <a href="/email-security/deployment/api/setup/office365-graph-api/">MS Graph</a> configured — you can set up message retraction to take post-delivery actions against suspicious messages. These retractions happen through API integrations with Microsoft 365 and Google Workspaces (Gmail).</p>
<h2 id="retraction-options">Retraction options</h2>
<p>Once you set up retraction, you can retract messages manually or set up automatic retractions to move messages matching certain <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8547.md")
</div> to specific folders within a user’s mailbox. You can also enable Post Delivery Response and Phish Submission Response to re-evaluate messages previously delivered against new information gathered by Email security. Scanned emails that were previously delivered and now match this new <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8548.md")
</div> information will be retracted.
<p>Refer to <a href="/email-security/deployment/api/setup/gsuite-bcc-setup/add-retraction/">Gmail</a> and <a href="/email-security/email-configuration/retract-settings/office365-retraction/">Office 365</a> guides for detailed information regarding these options.</p>
<h2 id="retraction-metrics">Retraction metrics</h2>
<p>Setting up retraction also gives you access to metrics for this feature. After logging in to your <a href="https://horizon.area1security.com">Email security dashboard</a>, search for the <strong>Retractions</strong> card. Metrics for retractions include information such as:</p>
<ul>
<li><strong>Total retractions</strong>: Displays the total amount of retractions performed.</li>
<li><strong>Success</strong>: Shows the percentage of messages Email security was able to find and retract successfully.</li>
<li><strong>Fail</strong>: Displays the percentage of messages Email security was not successfully able to retract. Reasons for failure include:
<ul>
<li>The user has already deleted or marked the message as junk, either manually or via a mailbox filter.</li>
<li>The specific copy of the message being retracted was sent to a distribution list address that may not exist as a mailbox, and so the retraction will fail. Separate copies of the message that are sent to each member of that distribution list will be retracted.</li>
<li>The retraction is not, or is no longer, authorized.</li>
</ul>
</li>
<li><strong>Unread/Read</strong>: Refers to the state of the message at the time it was retracted. For automated retractions, Email security tries to perform retraction as quickly as possible so the user has no time to see or open the message. Manual retraction might happen at a later time, and so the messages are more likely to have already been read.</li>
<li><strong>Auto/Manual</strong>: Refers to the percentage of messages retracted through the automatic/manual modes.</li>
</ul>
<p>Selecting <strong>View details</strong> will perform a search for retracted emails for the selected time interval.</p>
