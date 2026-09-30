<p>To validate that Cloudflare is receiving traffic from a user device:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Under <strong>Log traffic activity</strong>, enable activity logging for all DNS logs.</li>
<li>On your device, open a browser and go to any website.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>DNS</strong>.</li>
<li>Make sure DNS queries from your device appear.</li>
</ol>
<h2 id="best-practices">Best practices</h2>
<p>Securing your organization with a Zero Trust Network Access solution usually happens in two phases: the first phase is establishing connectivity, and the second phase is building policies for distinct applications. We recommend verifying that all connectivity is working as expected before moving on to build complex security policies. This will reduce the amount of troubleshooting and challenges that arise from managing complex systems.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="troubleshoot-the-cloudflare-one-client">Troubleshoot the Cloudflare One Client</h3>
@markup("md", "content/.markup/bodies/9905.md")
</aside>
