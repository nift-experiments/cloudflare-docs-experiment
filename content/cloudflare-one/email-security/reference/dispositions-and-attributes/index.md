<p>Email security uses a variety of factors to determine whether a given email message, domain, URL, or packet is part of a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4920.md")
</div> campaign. These small pattern assessments are dynamic in nature and — in many cases — no single pattern will determine the final verdict.
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="detection-vs-disposition">Detection vs. disposition</h3>
@markup("md", "content/.markup/bodies/4919.md")
</aside>
<h2 id="dispositions">Dispositions</h2>
<p>Any traffic that flows through Email security is given a final disposition, which represents our evaluation of that specific message. Each message will receive only one disposition header, so your organization can take clear and specific actions on different message types.</p>
<p>You can use disposition values when <a href="/cloudflare-one/email-security/settings/auto-moves/">setting up auto-moves</a>.</p>
<h3 id="available-values">Available values</h3>
<p>The following disposition values follow an order of maliciousness:</p>
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
<h3 id="header-structure">Header structure</h3>
<p>When Email security adds a disposition header to an email message, that header matches the following format:</p>
<pre><code class="language-txt">X-CFEmailSecurity-Disposition: [Value]&#10;</code></pre>
<p>Note that emails with a disposition of <code>SPAM</code> will be tagged with <code>UCE</code> (unsolicited commercial emails) in their headers:</p>
<pre><code class="language-txt">X-CFEmailSecurity-Disposition: UCE&#10;</code></pre>
<h2 id="attributes">Attributes</h2>
<p>Traffic that flows through Email security can also receive one or more Attributes, which indicate that a specific condition has been met.</p>
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
<td>Indicates that an email address was contained in your <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a> list. Associated with <code>MALICIOUS</code> or <code>SPOOF</code> dispositions.</td>
</tr>
</tbody>
</table>
<h3 id="header-structure-1">Header structure</h3>
<p>When Email security adds a disposition header to an email message, that header matches the following format:</p>
<pre><code class="language-txt">X-CFEmailSecurity-Attribute: [Value]&#10;X-CFEmailSecurity-Attribute: [Value2]&#10;</code></pre>
