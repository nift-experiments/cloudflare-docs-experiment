<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/996.md")
</aside>
<p>This guide will get you started with creating and managing configured Health Checks.</p>
<h2 id="create-a-health-check">Create a Health Check</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Health Checks</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create</strong> and fill out the form, paying special attention to:
<ul>
<li>The values for <strong>Interval</strong> and <strong>Check regions</strong>, because decreasing the <strong>Interval</strong> and increasing <strong>Check regions</strong> may increase the load on your origin server.</li>
<li><strong>Retries</strong>, which specify the number of retries to attempt in case of a timeout before marking the origin as unhealthy.</li>
<li><strong>Response body</strong>, which specifies a substring that must be present in the first 10 KB of the response body for the check to succeed.</li>
</ul>
</li>
<li>Select <strong>Save and Deploy</strong>.</li>
</ol>
<h2 id="manage-health-checks">Manage Health Checks</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Traffic</strong> &gt; <strong>Health Checks</strong>.</li>
<li>Navigate to your health check and select <strong>Edit</strong>.</li>
<li>Edit your Health Check.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/995.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/994.md")
</aside>
