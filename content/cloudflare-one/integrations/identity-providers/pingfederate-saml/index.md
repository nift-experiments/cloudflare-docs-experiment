<p>The PingFederate offering from PingIdentity provides SSO identity management. Cloudflare Access supports PingFederate as a SAML identity provider.</p>
<h2 id="set-up-pingfederate-as-an-identity-provider">Set up PingFederate as an identity provider</h2>
<ol>
<li>
<p>Log in to your <strong>Ping</strong> dashboard and go to <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Add Application</strong>.</p>
</li>
<li>
<p>Select <strong>New SAML Application</strong>.</p>
</li>
<li>
<p>Complete the fields for name, description, and category.</p>
</li>
</ol>
<p>These can be any value. A prompt displays to select a signing certificate to use.</p>
<ol start="5">
<li>
<p>In the <strong>SAML attribute configuration</strong> dialog select <strong>Email attribute</strong> &gt; <strong>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</strong>.</p>
</li>
<li>
<p>Go to <strong>SP Connections</strong> &gt; <strong>SP Connection</strong> &gt; <strong>Credentials</strong>.</p>
</li>
<li>
<p>Add the matching certificate that you upload into the Cloudflare SAML configuration for Ping. Select <strong>Include the certificate in the signature <code>&lt;KEYINFO&gt;</code> element</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5028.md")
</aside>
<ol start="8">
<li>
<p>In the <strong>Signature Policy</strong> tab, disable the option to <strong>Always Sign Assertion</strong>.</p>
</li>
<li>
<p>Leave the option enabled for <strong>Sign Response As Required</strong>.</p>
</li>
</ol>
<p>This ensures that SAML destination headers are sent during the integration.</p>
<p>In versions 9.0 above, you can leave both of these options enabled.</p>
<ol start="10">
<li>A prompt displays to download the SAML metadata from Ping.</li>
</ol>
<p>This file shares several fields with Cloudflare Access so you do not have to input this data.</p>
<ol start="11">
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select SAML.</p>
</li>
<li>
<p>In the <strong>IdP Entity ID</strong> field, enter the following URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="15">
<li>
<p>Fill the other fields with values from your Ping dashboard.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Authentication</strong> &gt; <strong>Login methods</strong> and select <strong>Test</strong> next to the login method you want to test.</p>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;https://example.cloudflareaccess.com/cdn-cgi/access/callback&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://sso.connect.pingidentity.com/sso/idp/SSO.saml2?idpid=aebe6668-32fe-4a87-8c2b-avcd3599a123&quot;,&#10;		&quot;attributes&quot;: [&quot;PingOne.AuthenticatingAuthority&quot;, &quot;PingOne.idpid&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;&quot;,&#10;		&quot;sign_request&quot;: false,&#10;		&quot;idp_public_cert&quot;: &quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;ping saml example&quot;&#10;}&#10;</code></pre>
