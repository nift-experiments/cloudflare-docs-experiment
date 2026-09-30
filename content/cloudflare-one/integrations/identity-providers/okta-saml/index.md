<p>Cloudflare One can integrate SAML with Okta as an identity provider.</p>
<h2 id="set-up-okta-as-a-saml-provider">Set up Okta as a SAML provider</h2>
<p>To set up SAML with Okta as your identity provider:</p>
<ol>
<li>
<p>On your Okta admin dashboard, go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create App Integration</strong>.</p>
</li>
<li>
<p>In the pop-up dialog, select <strong>SAML 2.0</strong> and then elect <strong>Next</strong>.</p>
</li>
<li>
<p>Enter an app name and select <strong>Next</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta-saml/okta-saml-1.png" alt="Entering your Cloudflare One callback URL into Okta" /></p>
<ol start="5">
<li>In the <strong>Single sign on URL</strong> and the <strong>Audience URI (SP Entity ID)</strong> fields, enter the following URL:</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="6">
<li>
<p>In the <strong>Attribute Statements</strong> section, enter the following information:</p>
<ul>
<li><strong>Name</strong>: Enter <code>email</code>.</li>
<li><strong>Value</strong>: Enter <code>user.email</code>.</li>
</ul>
</li>
<li>
<p>(Optional) If you are using Okta groups, create a <strong>Group Attribute Statement</strong> with the following information:</p>
<ul>
<li><strong>Name</strong>: Enter <code>groups</code>.</li>
<li><strong>Filter</strong>: Select <em>Matches regex</em> and enter <code>.*</code>.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta-saml/okta-saml-2.png" alt="Configuring attribute statements in Okta" /></p>
<ol start="8">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Select <strong>I'm an Okta customer adding an internal app</strong> and check <strong>This is an internal app that we have created</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta-saml/okta-saml-3.png" alt="Configuring feedback options in Okta" /></p>
<ol start="9">
<li>
<p>Select <strong>Finish</strong>.</p>
</li>
<li>
<p>In the <strong>Assignments</strong> tab, select <strong>Assign</strong> and assign individuals or groups you want to grant access to.</p>
</li>
<li>
<p>Select <strong>Done</strong>. The assigned individuals and groups will display in the <strong>Assignments</strong> tab.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta-saml/okta-saml-4.png" alt="Assigning individuals and groups to Okta application" /></p>
<ol start="12">
<li>To retrieve the SAML provider information, go to the <strong>Sign On</strong> tab and select <strong>View Setup Instructions</strong>. A new page will open showing the <strong>Identity Provider Single Sign-on URL</strong>, <strong>Identity Provider Issuer</strong>, and <strong>X.509 Certificate</strong>. Save this information for configuring your Cloudflare One settings.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta-saml/okta-saml-5.png" alt="Retrieving SAML provider information in Okta" /></p>
<ol start="13">
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity provider</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>, and select <em>SAML</em>.</p>
</li>
<li>
<p>Fill in the following information:</p>
<ul>
<li><strong>Name</strong>: Name your identity provider.</li>
<li><strong>Single Sign On URL</strong>: Enter the Identity Provider Single-Sign-On URL from Okta.</li>
<li><strong>Issuer ID</strong>: Enter the Identity Provider Issuer from Okta, for example <code>http://www.okta.com/&lt;your-okta-entity-id&gt;</code>.</li>
<li><strong>Signing Certificate</strong>: Copy-paste the X.509 Certificate from Okta.</li>
</ul>
</li>
<li>
<p>(Recommended) Enable <strong>Sign SAML authentication request</strong>.</p>
</li>
<li>
<p>(Recommended) Under <strong>SAML attributes</strong>, add the <code>email</code> and <code>groups</code> attributes. The <code>groups</code> attribute is required if you want to create policies based on <a href="/cloudflare-one/traffic-policies/identity-selectors/#okta-saml">Okta groups</a>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta-saml/okta-saml-6.png" alt="Adding optional SAML attributes in Cloudflare One" /></p>
<ol start="18">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to Okta. A success response should return the configured SAML attributes.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5042.md")
</aside>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;http://www.okta.com/exkbhqj29iGxT7GwT0h7&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://dev-abc123.oktapreview.com/app/myapp/exkbhqj29iGxT7GwT0h7/sso/saml&quot;,&#10;		&quot;attributes&quot;: [&quot;email&quot;, &quot;group&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;&quot;,&#10;		&quot;sign_request&quot;: false,&#10;		&quot;idp_public_certs&quot;: [&#10;			&quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;		]&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;okta saml example&quot;&#10;}&#10;</code></pre>
