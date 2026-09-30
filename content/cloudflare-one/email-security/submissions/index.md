<p>Submitting messages allows you to choose the disposition of your messages if the disposition is incorrect. This helps improve Email security's detection accuracy and ensures proper handling of email threats.</p>
<h2 id="submit-messages-for-review">Submit messages for review</h2>
<p>To submit a message for review:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong> and select <strong>Investigation</strong>.</li>
<li>On the <strong>Investigation</strong> page, under <strong>Your matching messages</strong>, select the message you want to reclassify.</li>
<li>Select the three dots, then select <strong>Submit for review</strong>.</li>
<li>Under <strong>New disposition</strong>, select among the following:
<ul>
<li><strong>Malicious</strong>: Traffic invoked multiple phishing verdict triggers, met thresholds for bad behavior, and is associated with active campaigns.</li>
<li><strong>Spoof</strong>: Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies (SPF, DKIM, DMARC) or has mismatching Envelope From and <code>Header From</code> values.</li>
<li><strong>Spam</strong>: Traffic associated with non-malicious, commercial campaigns.</li>
<li><strong>Bulk</strong>: Traffic associated with <a href="https://en.wikipedia.org/wiki/Graymail_%28email%29">Graymail</a>, that falls in between the definitions of <code>SPAM</code> and <code>SUSPICIOUS</code>. For example, a marketing email that intentionally obscures its unsubscribe link.</li>
<li><strong>Clean</strong>: Traffic not associated with any phishing campaigns.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To submit messages in bulk, select <strong>Select all messages</strong> &gt; <strong>Action</strong> &gt; <strong>Request submissions</strong>.</p>
<p>To release messages in bulk, select <strong>Select all messages</strong> &gt; <strong>Action</strong> &gt; <strong>Release</strong>.</p>
<h2 id="upload-eml-files">Upload EML files</h2>
<p>Email security classifies certain emails as &quot;Clean&quot;. If you disagree with the disposition, you can upload an EML file and reclassify the email.</p>
<p>On the <strong>Investigation</strong> page:</p>
<ol>
<li>Go to the email marked as <strong>Clean</strong>.</li>
<li>Select the three dots &gt; <strong>Submit for review</strong>.</li>
<li>Upload the EML file.</li>
<li>Select a new disposition.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="view-submissions">View submissions</h2>
<p>Once you have submitted your messages, you can access those on <strong>Submissions</strong>.</p>
<p>To view submissions:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong> &gt; <strong>Submissions</strong>.</li>
<li>Choose from the following submission types:
<ul>
<li><a href="/cloudflare-one/email-security/submissions/team-submissions/"><strong>Team submissions</strong></a>: View emails your security team submitted for submissions.</li>
<li><a href="/cloudflare-one/email-security/submissions/user-submissions/"><strong>User submissions</strong></a>: View emails your users submitted for submissions.</li>
<li><a href="/cloudflare-one/email-security/submissions/invalid-submissions/"><strong>Invalid submissions</strong></a>: View submissions that could not be processed.</li>
</ul>
</li>
</ol>
