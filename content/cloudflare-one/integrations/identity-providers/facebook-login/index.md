<p>Use these steps to set up Facebook as your identity provider.</p>
<ol>
<li>
<p>Go to <a href="https://developers.facebook.com/">developers.facebook.com</a>. Create a Developer account if you do not have one.</p>
</li>
<li>
<p>Select <strong>Create App</strong> at the top-right. The <strong>Create an app</strong> card displays.</p>
</li>
<li>
<p>Enter the <strong>App name</strong> and <strong>App contact email</strong>. Then, select <strong>Next</strong>.</p>
</li>
<li>
<p>In the <strong>Add use cases</strong> page, select <strong>Authenticate and request data from users with Facebook Login</strong>. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Fill in the necessary information and select <strong>Next</strong> until you reach <strong>Overview</strong>. Then, select <strong>Create app</strong>.</p>
</li>
<li>
<p>In the <strong>My Apps</strong> page, go to <strong>App settings</strong> &gt; <strong>Basic</strong>.</p>
</li>
<li>
<p>Copy the <strong>App ID</strong> and <strong>App Secret</strong>.</p>
</li>
<li>
<p>In the <a href="https:/dash.cloudflare.com">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add an identity provider</strong>.</p>
</li>
<li>
<p>Fill in the <strong>App ID</strong> and <strong>App Secret</strong> obtained from Facebook.</p>
</li>
<li>
<p>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a>. PKCE will be performed on all login attempts.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Go back to <strong>My Apps</strong> in <a href="https://developers.facebook.com/">developers.facebook.com</a>, and select your app.</p>
</li>
<li>
<p>Under <strong>App customization and requirements</strong>, select <strong>Customize the Authenticate and request data from users with Facebook Login use case</strong>.</p>
</li>
<li>
<p>Select <strong>Settings</strong>, and ensure that <strong>Use Strict Mode for redirect URIs</strong> slider is set to <strong>Yes</strong>.</p>
</li>
<li>
<p>In the <strong>Valid OAuth Redirect URIs</strong> field, enter the following URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<pre><code>You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<ol start="16">
<li>Select <strong>Save Changes</strong>.</li>
</ol>
<p>To test that your connection is working, follow the steps on <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">SSO Integration</a>.</p>
<h2 id="example-api-configuration">Example API Configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;facebook&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
