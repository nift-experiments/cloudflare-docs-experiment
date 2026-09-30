<h2 id="disposition-actions">Disposition actions</h2>
<p>Create actions for emails with specific <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8564.md")
</div>. `URL defang` means that every URL in an email of the selected type will be rewritten so that the user cannot follow the link. For example, `https://www.example.com` will become `https[:]//www[.]example[.]com`.
<p>To update or create a new disposition action:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Email Policies</strong> &gt; <strong>Link Actions</strong>.</li>
<li>In <strong>Disposition Actions</strong> select <strong>Edit</strong>.</li>
<li>For each disposition, such as <code>MALICIOUS</code>, <code>SPAM</code>, and <code>BULK</code>, choose the action you want to perform.</li>
</ol>
<h2 id="email-link-isolation">Email Link Isolation</h2>
<p>Email Link Isolation rewrites links that could be exploited, alerts users when there is uncertainty around the website they are visiting, and protects against malware and vulnerabilities through <a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a>.</p>
<p>When you enable Email Link Isolation, the service rewrites links in emails and opens them in a browser tab where all page contents are fetched and rendered on a remote server. When this feature is enabled, any malware that might be present in a web page or email link is isolated at the server level, and will not infect and compromise the client network at the endpoint.</p>
<p>Suspicious hyperlinks are system-determined, and triggered by a dynamic isolation list maintained by Cloudflare’s security team.</p>
<h3 id="previous-disposition-actions">Previous disposition actions</h3>
<p>When you enable Email Link Isolation, Cloudflare no longer takes into account <a href="#disposition-actions">URL actions</a> based on the <a href="/email-security/reference/dispositions-and-attributes/">email’s dispositions</a>. URL actions are, rather, based on attributes of the link.</p>
<p>Link rewriting applies to all email dispositions. If you have link actions set for dispositions, you will see a warning when enabling Email Link Isolation. This indicates that Email Link Isolation's rewriting will apply globally.</p>
<h3 id="enable-email-link-isolation">Enable Email Link Isolation</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="email-link-isolation-and-microsoft-o365">Email Link Isolation and Microsoft O365</h3>
@markup("md", "content/.markup/bodies/8563.md")
</aside>
<p>To enable Email Link Isolation you must have an <a href="/email-security/deployment/inline/">inline deployment</a> for your Email security setup. Email Link Isolation is not available if Email security is deployed through <a href="/email-security/deployment/api/setup/">journaling or BCC</a> setups.</p>
<p>Email Link Isolation can only be used when there are no other security applications doing URL rewrites. Double link rewrites are not supported.</p>
<p>To enable Email Link Isolation:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Email Policies</strong> &gt; <strong>Link Actions</strong>.</li>
<li>Scroll to <strong>Email Link Isolation</strong> and enable it.</li>
</ol>
<p>Email Link Isolation is now enabled.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8562.md")
</aside>
<h2 id="url-rewrite-ignore-patterns">URL rewrite ignore patterns</h2>
<p>Use this option to ignore rewrites on URLs matching specific patterns. This feature allows you to ensure that internal corporate services never have links rewritten for them.</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Email Policies</strong> &gt; <strong>Link Actions</strong>.</li>
<li>Scroll to <strong>URL Rewrite Ignore Patterns</strong>.</li>
<li>Add a new URL pattern to <strong>URL pattern</strong> and select <strong>Add Pattern</strong>.</li>
</ol>
