<p>Yandex is a web search engine that also offers identity provider (IdP) services.</p>
<h2 id="set-up-yandex">Set up Yandex</h2>
<p>To set up Yandex for Cloudflare Access:</p>
<ol>
<li>
<p>Log in to your Yandex account.</p>
</li>
<li>
<p>Select <strong>Open a new OAuth Application</strong>.</p>
</li>
<li>
<p>Select <strong>New client</strong>.</p>
</li>
<li>
<p>Complete the required fields.</p>
</li>
<li>
<p>Choose <strong>Yandex.Passport API</strong> to set the basic scopes.</p>
</li>
<li>
<p>Select the <strong>Access to email address</strong>, <strong>Access to user avatar,</strong> and <strong>Access to username, first name and surname, gender</strong> options.</p>
</li>
<li>
<p>Select <strong>Platform</strong> and select <strong>Web Services.</strong></p>
</li>
<li>
<p>In the <strong>Callback URL #1</strong> field, enter the following URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/yandex/yandex-3.png" alt="Yandex Platform interface with Web services checked and callback URI in open form field" /></p>
<ol start="9">
<li>
<p>Select <strong>Add</strong>.</p>
</li>
<li>
<p>Scroll to the <strong>Platforms</strong> card, and select <strong>Submit</strong>.</p>
<p><strong>Yandex OAuth</strong> card titled <strong>Cloudflare Access App</strong> displays.</p>
</li>
<li>
<p>Copy the <strong>ID</strong> and <strong>Password</strong>.</p>
</li>
<li>
<p>In Cloudflare One, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select Yandex.</p>
</li>
<li>
<p>Paste the ID and password in the appropriate fields.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="example-api-config">Example API Config</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;yandex&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
