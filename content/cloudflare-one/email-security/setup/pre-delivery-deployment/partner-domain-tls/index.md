<p>To add additional TLS (Transport Layer Security) requirements for emails coming from certain domains, you can enforce higher levels of SSL/TLS inspection. If TLS is required, mail without TLS from the specified domain will be dropped.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4943.md")
</aside>
<p>To set up a partner domain:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Partner domain TLS</strong> &gt; <strong>View</strong>.</li>
<li>Select <strong>Add a domain</strong>.</li>
<li>Enter a valid domain name. You can also exclude subdomains by selecting <strong>Add exclude</strong>.</li>
<li>(Optional) Add an optional note to describe your rule(s).</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To edit a partner domain, select the three dots &gt; <strong>Edit</strong>.</p>
<p>To delete a partner domain, select the three dots &gt; <strong>Delete</strong>.</p>
