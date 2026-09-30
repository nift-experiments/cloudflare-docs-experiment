<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8470.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8469.md")
</aside>
<p>Email security uses a variety of factors to determine whether a given email message, domain, URL, or packet is part of a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8471.md")
</div> campaign. These small pattern assessments are dynamic in nature and — in many cases — no single pattern will determine the final verdict.
<p>Based on these patterns, Email security may add <code>X-Headers</code> to each email message that passes through our system.</p>
<h2 id="dispositions">Dispositions</h2>
<p>Any traffic that flows through Email security is given a final disposition, which represents our evaluation of that specific message. Each message will only receive one disposition header so your organization can take clear and specific actions on different message types.</p>
<p>You can use disposition values when <a href="/email-security/email-configuration/domains-and-routing/domains/">creating your quarantine policy</a> or <a href="/email-security/email-configuration/retract-settings/">setting up auto-retract</a>.</p>
<h3 id="available-values">Available values</h3>
<table>
<thead>
<tr>
<th>Disposition</th>
<th>Description</th>
<th>Recommendation</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>MALICIOUS</code></td>
<td>Traffic invoked multiple phishing verdict triggers, met thresholds for bad behavior, and is associated with active campaigns.</td>
<td>Block</td>
</tr>
<tr>
<td><code>SUSPICIOUS</code></td>
<td>Traffic associated with phishing campaigns (and is under further analysis by our automated systems).</td>
<td>Research these messages internally to evaluate legitimacy.</td>
</tr>
<tr>
<td><code>SPOOF</code></td>
<td>Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies (SPF, DKIM, DMARC) or has mismatching <code>Envelope From</code> and <code>Header From</code> values.</td>
<td>Block after investigating (can be triggered by third-party mail services).</td>
</tr>
<tr>
<td><code>UCE</code> (Unsolicited Commercial Emails)</td>
<td>Traffic associated with non-malicious, commercial campaigns.</td>
<td>Route to existing Spam quarantine folder.</td>
</tr>
<tr>
<td><code>BULK</code> (dashboard only)</td>
<td>Traffic often associated with newsletters or marketing campaigns. Refer to <a href="https://en.wikipedia.org/wiki/Graymail_%28email%29">Graymail</a> for more details.</td>
<td>Monitor or tag</td>
</tr>
</tbody>
</table>
<h3 id="header-structure">Header structure</h3>
<p>When Email security adds a disposition header to an email message, that header matches the following format:</p>
<pre><code class="language-txt">X-Area1Security-Disposition: [Value]&#10;</code></pre>
<p>Note that emails with a disposition of <code>SPAM</code> will be tagged with <code>UCE</code> (unsolicited commercial emails) in their headers:</p>
<pre><code class="language-txt">X-Area1Security-Disposition: UCE&#10;</code></pre>
<h2 id="attributes">Attributes</h2>
<p>Traffic that flows through Email security can also receive one or more <strong>Attributes</strong>, which indicate that a specific condition has been met.</p>
<h3 id="available-values-1">Available values</h3>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CUSTOM_BLOCK_LIST</code></td>
<td>This message matches a value you have defined in your custom block list.</td>
</tr>
<tr>
<td><code>NEW_DOMAIN_SENDER=&lt;REGISTRATION_DATE&gt;</code></td>
<td>Alerts to mail from a newly registered domain. Formatted as yyyy-MM-dd HH:mm:ss ZZZ.</td>
</tr>
<tr>
<td><code>NEW_DOMAIN_LINK=&lt;REGISTRATION_DATE&gt;</code></td>
<td>Alerts to mail with links pointing out to a newly registered domain. Formatted as yyyy-MM-dd HH:mm:ss ZZZ.</td>
</tr>
<tr>
<td><code>ENCRYPTED</code></td>
<td>Email message is encrypted.</td>
</tr>
<tr>
<td><code>EXECUTABLE</code></td>
<td>Email message contains an executable file.</td>
</tr>
<tr>
<td><code>BEC</code></td>
<td>Indicates that email address was contained in your <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/">business email compromise (BEC)</a> list. Associated with <code>MALICIOUS</code> or <code>SPOOF</code> dispositions.</td>
</tr>
</tbody>
</table>
<h3 id="header-structure-1">Header structure</h3>
<p>When Email security adds a disposition header to an email message, that header matches the following format.</p>
<pre><code class="language-txt">X-Area1Security-Attribute: [Value]&#10;X-Area1Security-Attribute: [Value2]&#10;</code></pre>
