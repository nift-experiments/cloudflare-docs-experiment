<p>Once you have chosen a domain to scan, Email security allows you to monitor the traffic scanned from your email inboxes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4921.md")
</aside>
<p>To monitor your inbox:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Under <strong>Email security</strong>, select <strong>Monitoring</strong>.</li>
</ol>
<p>The dashboard will display the following metrics:</p>
<ul>
<li>Email activity</li>
<li><a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">Disposition evaluation</a></li>
<li>Detection details</li>
<li><a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">Impersonations</a></li>
<li><a href="/cloudflare-one/email-security/settings/phish-submissions/">Phish submissions</a></li>
<li><a href="/cloudflare-one/email-security/settings/auto-moves/">Auto-move events</a></li>
<li><a href="/cloudflare-one/email-security/settings/detection-settings/">Detection settings metrics</a></li>
</ul>
<h2 id="email-activity">Email activity</h2>
<p>Email activity aggregates statistics about emails scanned and dispositions assigned (the number of email flagged due to a detection) within a given timeframe.</p>
<p>To view the live number of email scanned and dispositions scanned, enable <strong>Live mode</strong>.</p>
<h2 id="disposition-evaluation">Disposition evaluation</h2>
<p>Email traffic that flows through Email security is given a final disposition, which represents Email security's evaluation of that specific message.</p>
<p>Disposition evaluation displays the following dispositions:</p>
<ul>
<li><strong>Malicious</strong>: Traffic associated with active threat campaigns. Malicious messages invoked multiple phishing verdict triggers and met thresholds for bad behavior.
<ul>
<li><strong>Recommendation</strong>: Block.</li>
</ul>
</li>
<li><strong>Spam</strong>: Traffic associated with non-malicious, commercial campaigns.
<ul>
<li><strong>Recommendation</strong>: Route to existing Spam quarantine folder.</li>
</ul>
</li>
<li><strong>Bulk</strong>: Traffic often associated with newsletters or marketing campaigns. Refer to <a href="https://en.wikipedia.org/wiki/Graymail_%28email%29">Graymail</a> for more details.
<ul>
<li><strong>Recommendation</strong>: Monitor or tag.</li>
</ul>
</li>
<li><strong>Suspicious</strong>: Traffic associated with phishing campaigns (and is under further analysis by our automated systems).
<ul>
<li><strong>Recommendation</strong>: Research these messages internally to evaluate legitimacy.</li>
</ul>
</li>
<li><strong>Spoof</strong>: Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies (<a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/">SPF</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/">DKIM</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>) or has mismatching <code>Envelope From</code> and <code>Header From</code> values.
<ul>
<li><strong>Recommendation</strong>: Block after investigating (can be triggered by third-party mail services).</li>
</ul>
</li>
</ul>
<h2 id="detection-details">Detection details</h2>
<p>Detection details displays information about:</p>
<ul>
<li><strong>Malicious</strong> disposition:
<ul>
<li><strong>Email threat types</strong>: Top malicious threat types, and their number relative to the total amount of malicious threats received.</li>
<li><strong>Targeted users</strong>: Top number of emails targeted, and their number relative to the total amount of malicious targets.</li>
<li><strong>Malicious links</strong>: A graph displaying the total number of malicious links and their distribution throughout the month.</li>
<li><strong>Malicious attachments</strong>: Number of malicious attachments, and the top types of malicious files received.</li>
</ul>
</li>
<li><strong>Suspicious</strong> disposition:
<ul>
<li><strong>Suspicious threat types</strong>: Top suspicious threat types, and their number relative to the total amount of threats received.</li>
<li><strong>Suspicious targets</strong>: Top number of emails targeted, and their number relative to the total amount of malicious targets.</li>
<li><strong>Suspicious links</strong>: A graph displaying the total number of suspicious links and their distribution throughout the month.</li>
</ul>
</li>
<li><strong>Spoof</strong> disposition:
<ul>
<li><strong>Spoof users (impersonated names)</strong>: Top number of impersonated names, and their number relative to the total number of detection received.</li>
<li><strong>Spoof targets</strong>: Top number of targeted emails.</li>
<li><strong>Sender v. envelope mismatch</strong>: This field indicates the number of mismatches between the email address the message was sent from, and the email address the message was <em>actually</em> sent from.</li>
</ul>
</li>
</ul>
<h2 id="impersonations">Impersonations</h2>
<p>Impersonations are a form of phishing attack where the actor pretends to be someone else to steal sensitive information.</p>
<p><strong>Impersonations</strong> displays the number of targeted users, and a chart describing the total number of impersonation attempts.</p>
<ul>
<li>To view all targeted users, select <strong>View all targeted users</strong>.</li>
<li>To view all impersonation emails, select <strong>View all impersonation emails</strong>.</li>
<li>To view impersonated users, select <strong>View impersonated users</strong>.</li>
</ul>
<p>Refer to <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">Trusted domains</a> to add a trusted domain, and <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">Impersonation registry</a> to add a user to the impersonation registry.</p>
<h2 id="phish-submissions">Phish submissions</h2>
<p>Phishing is a type of attack that involves stealing sensitive information with the aim of using and selling the information.</p>
<p>A phish submission happens when a user or an administrator reports a phishing attack. Refer to <a href="/cloudflare-one/email-security/settings/phish-submissions/">Phish submissions</a> to learn how to submit a phish.</p>
<p>Phish submissions displays the following information:</p>
<ul>
<li><strong>All submissions</strong>: The total number of phish submissions.</li>
<li><strong>User submissions</strong>: The number of phish submissions reported by your users.</li>
<li><strong>Admin submissions</strong>: The number of phish submissions reported by an administrator.</li>
</ul>
<p>Select <strong>Review submissions</strong> to review a filtered list of phish submissions reported by your team.</p>
<h2 id="auto-move-events">Auto-move events</h2>
<p>Auto-move events are emails moved to different inboxes based on the disposition Email security assigned.</p>
<p>This panel shows you the total number of auto-moves and the source folder from which these retractions are originating from.</p>
<p>Refer to <a href="/cloudflare-one/email-security/settings/auto-moves/">Auto-moves</a> to configure auto-move events.</p>
<h2 id="detection-settings-metrics">Detection settings metrics</h2>
<p>Detection settings metric displays information about:</p>
<ul>
<li><strong>Allowed traffic</strong>: Traffic that Email security will exempt emails that match certain patterns from normal detection scanning. Allowed traffic shows metrics on emails that were allowed to go through user inboxes.</li>
<li><strong>Blocked traffic</strong>: Traffic that Email security automatically blocks from senders. Blocked traffic shows metrics on emails that were blocked from user inboxes.</li>
<li><strong>Domain age</strong>: The number of days since domain registration.</li>
</ul>
<p>Select <strong>Configure</strong> to configure policy and rules for <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allowed traffic</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked traffic</a> and <a href="/cloudflare-one/email-security/settings/detection-settings/additional-detections/">domain age</a>.</p>
