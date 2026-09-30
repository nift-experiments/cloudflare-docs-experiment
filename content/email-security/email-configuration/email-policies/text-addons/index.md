<p>When a message receives a specific <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8561.md")
</div> from Email security (formerly Area 1), you can add additional information to the subject and body of each message.
<p>This information provides additional context to your employees, which can help them make better decisions if you choose to have a more permissive email policy:</p>
<ul>
<li><strong>Subject prefixes</strong>: Can tell recipients which category the message is in. Subject prefixes always state the final <a href="/email-security/reference/dispositions-and-attributes/">disposition</a> of the message.</li>
<li><strong>Body prefixes</strong>: Provide more context about why the message was added to a specific category. Body prefixes include all the detections that were triggered. This information depends on the <a href="#update-text-add-ons">prefixes you enable</a>.</li>
</ul>
<p>For example, an email might have the dispositions <code>EXTERNAL MALICIOUS</code> in the subject, and <code>EXTERNAL MALICIOUS SUSPICIOUS UCE</code> in its body.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8560.md")
</aside>
<h2 id="update-text-add-ons">Update text add-ons</h2>
<p>To update or add a new add-on to the subject or body of a message:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Email Policies</strong> &gt; <strong>Text Add-Ons</strong>.</p>
</li>
<li>
<p>Select <strong>Edit</strong>.</p>
</li>
<li>
<p>For each <strong>Disposition</strong>, choose whether prefixes are <strong>Enabled</strong> and whether you want to update the <strong>Custom Label</strong>.</p>
</li>
<li>
<p>If desired, you can also use <strong>Subject Prefix</strong> or <strong>Body Prefix</strong> to update the text added before or after the rendered disposition:</p>
<ul>
<li><strong>Subject Prefix</strong>: Includes a dynamic value for <code>%LABELS</code> that lists the disposition and can include additional text.</li>
<li><strong>Body Prefix</strong>: Includes a dynamic value for <code>%LABELS</code> that lists the disposition and <code>%REASONS</code> that lists the reasons behind an assigned disposition. Can include additional, HTML-formatted text.</li>
</ul>
</li>
<li>
<p>Select <strong>Update Text Add-Ons</strong>.</p>
</li>
</ol>
