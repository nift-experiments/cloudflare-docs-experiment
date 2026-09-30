<p>When you set up <strong>allowed patterns</strong>, Email security email security exempts messages that match certain patterns from normal detection scanning.</p>
<h2 id="add-an-allowed-pattern">Add an allowed pattern</h2>
<p>To create a new allowed pattern:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Allow List</strong> &gt; <strong>Allowed Patterns</strong>.</p>
</li>
<li>
<p>Select <strong>+ New Pattern</strong>.</p>
</li>
<li>
<p>Enter the pattern information:</p>
<ul>
<li>
<p><strong>Allowed Pattern</strong>: Enter one of the following types of pattern:</p>
<ul>
<li><strong>Email addresses</strong>: Must be a valid email.</li>
<li><strong>IP addresses</strong>: Can only be IPv4. IPv6 and CIDR are invalid entries.</li>
<li><strong>Regular expressions</strong>: Must be <a href="https://www.freeformatter.com/java-regex-tester.html">valid Java expressions</a>.</li>
</ul>
</li>
<li>
<p><strong>Allow Type</strong>: Choose one or more of the following types:</p>
<ul>
<li><strong>Trusted Sender</strong>: Messages will bypass all <a href="/email-security/reference/dispositions-and-attributes/">detections</a> and link following by Email security. Typically, only applies to <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
</li>
</ul>
</li>
</ol>
@markup("md", "content/.markup/bodies/8558.md")
</div> simulations from vendors such as KnowBe4.
     - **Exempt Recipient**: Will exempt messages from all Email security [detections](/email-security/reference/dispositions-and-attributes/) intended for recipients matching this pattern (email address or regular expression only). Typically, this only applies to submission mailboxes for user reporting to security.
     - **Acceptable Sender**: Will exempt messages from the `SPAM`, `SPOOF`, and `BULK` [dispositions](/email-security/reference/dispositions-and-attributes/#available-values) (but not `MALICIOUS` or `SUSPICIOUS`). Commonly used for external domains and sources that send mail on behalf of your organization, such as marketing emails or internal tools.
<ul>
<li><strong>Notes</strong>: Provide additional notes about the allowed pattern.</li>
</ul>
<ol start="6">
<li>
<p>If you chose <em>Trusted Sender</em> or <em>Acceptable Sender</em> in the previous step, you will be able to choose whether to verify the sender. When the <strong>Verify Sender</strong> option is selected, the allow list entry will only be honored if it aligns with a passing authentication by DMARC or SPF or DKIM.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can also upload a CSV file of multiple allowed patterns. The CSV file must be smaller than 150 KB, start with a header row of all required values, and contain no additional fields.</p>
<p>An example file would look like this:</p>
<pre><code class="language-txt">Pattern, Notes, Verify Email, Trusted Sender,&#10;Exempt Recipient, Acceptable Sender&#10;whale@notaphish.com, not a phish, true, true, false, true&#10;</code></pre>
