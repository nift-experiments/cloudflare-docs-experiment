<p>Cloudflare One allows your team to connect to your applications using their GitHub login. You do not need to have a GitHub organization to use the integration.</p>
<h2 id="set-up-github-access">Set up GitHub Access</h2>
<p>To configure GitHub access in both GitHub and Cloudflare One:</p>
<ol>
<li>
<p>Log in to <a href="https://github.com/">GitHub</a>.</p>
</li>
<li>
<p>Go to your account &gt; <strong>Settings</strong> &gt; <strong>Developer Settings</strong>.</p>
</li>
<li>
<p>In <strong>Developer Settings</strong>, select <strong>OAuth Apps</strong> and select <strong>New OAuth app</strong>.</p>
</li>
<li>
<p>On the <strong>Register a new OAuth application</strong> page, enter an <strong>Application name</strong>. Your users will see this application name on the login page.</p>
</li>
<li>
<p>In the <strong>Homepage URL</strong> field, enter your team domain:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="6">
<li>In the GitHub <strong>Authorization callback URL</strong> field, enter the following URL:</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="7">
<li>
<p>Select <strong>Register application</strong>.</p>
</li>
<li>
<p>Make note of the <strong>Client ID</strong>.</p>
</li>
<li>
<p>Select <strong>Generate a new client secret</strong> and copy the client secret to a safe place.</p>
</li>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new identity provider</strong> and select <strong>GitHub</strong>.</p>
</li>
<li>
<p>In <strong>App ID</strong>, enter the <strong>Client ID</strong> obtained from GitHub (refer to step 8).</p>
</li>
<li>
<p>In <strong>Client secret</strong>, enter the <strong>Client secret</strong> obtained from GitHub (refer to step 9).</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Select <strong>Finish setup</strong> to launch a GitHub authorization page. You will be asked to grant the following permissions to Cloudflare Access:</p>
<ul>
<li>Organizations and teams (read-only)</li>
<li>Email addresses (read-only)</li>
</ul>
</li>
<li>
<p>Select <strong>Authorize</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> &gt; <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to your GitHub login method. If you have GitHub two-factor authentication enabled, you will need to first login to GitHub directly and return to Access.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="troubleshooting-organization-policies">Troubleshooting organization policies</h3>
@markup("md", "content/.markup/bodies/5058.md")
</aside>
<h2 id="example-api-configuration">Example API Configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;github&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
