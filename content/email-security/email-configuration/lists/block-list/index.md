<p>When you add <strong>blocked senders</strong>, Email security automatically marks all messages from these senders with a <code>MALICIOUS</code> <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8557.md")
</div>.
<h2 id="add-a-blocked-sender">Add a blocked sender</h2>
<p>To create a new blocked pattern:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Block List</strong> &gt; <strong>Blocked Senders</strong>.</p>
</li>
<li>
<p>Select <strong>+ New Sender</strong>.</p>
</li>
<li>
<p>Enter the pattern information:</p>
<ul>
<li>
<p><strong>Sender</strong>: Enter one of the following types of pattern:</p>
<ul>
<li><strong>Email addresses</strong>: Must be a valid email.</li>
<li><strong>IP addresses</strong>: Can only be IPv4. IPv6 and CIDR are invalid entries.</li>
<li><strong>Regular expressions</strong>: Must be <a href="https://www.freeformatter.com/java-regex-tester.html">valid Java expressions</a>. Regular expressions are matched with fields related to the sender email address (<code>envelope from</code>, <code>header from</code>, <code>reply-to</code>), the originating IP address, and the server name for the email.</li>
</ul>
</li>
<li>
<p><strong>Notes</strong>: Provide additional notes about the blocked sender pattern.</p>
</li>
</ul>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can also upload a CSV file of multiple allowed patterns. The CSV file must be smaller than 150 KB, start with a header row of all required values, and contain no additional fields.</p>
<p>An example file would look like this:</p>
<pre><code class="language-txt">Blocked_Sender, Notes&#10;john.smith@email.com, John Smith&#10;melanie.turner@email.com, Melanie Turner&#10;</code></pre>
