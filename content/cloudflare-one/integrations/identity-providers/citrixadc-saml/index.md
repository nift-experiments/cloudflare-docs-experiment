<p>Cloudflare One can integrate with Citrix ADC (formerly Citrix NetScaler ADC) as a SAML IdP. Documentation from Citrix shows you <a href="https://docs.citrix.com/en-us/citrix-adc/12-1/aaa-tm/saml-authentication/citrix-adc-saml-idp.html">how to configure Citrix ADC as a SAML IdP</a>. These steps are specific to Cloudflare One.</p>
<h2 id="set-up-citrix-adc-saml">Set up Citrix ADC (SAML)</h2>
<p>To set up Citrix ADC (SAML) as your identity provider:</p>
<ol>
<li>
<p>First, you'll need to configure 2 SAML certificates:</p>
<ul>
<li>A certificate to <strong>terminate TLS at the vServer</strong>. Ensure that the certificate is issued by a publicly trusted CA.</li>
<li>A certificate for <strong>signing SAML assertions</strong>.</li>
</ul>
<p>If you do not already have a certificate for signing SAML assertions, you can use a self-signed certificate generated on Citrix ADC by following these steps:</p>
<ol>
<li>Go to <strong>Traffic Management</strong> &gt; <strong>SSL</strong>.</li>
<li>Select <strong>Create and Install a Server Test Certificate</strong>.</li>
</ol>
</li>
<li>
<p>Select <strong>Configuration</strong> and enter a <strong>Certificate File Name</strong>, <strong>Fully Qualified Domain Name</strong>, and a select a <strong>Country</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/citrixadc/citrixadc-saml-2.png" alt="Citrix AD Create and Install Test Certificate interface with file name, domain name, and country" /></p>
<ol start="3">
<li>
<p>Create a publicly accessible authentication vServer and configure the user identity source (like, local users, LDAP) by following this <a href="https://docs.citrix.com/en-us/citrix-adc/12-1/aaa-tm/authentication-virtual-server/ns-aaa-setup-auth-vserver-tsk.html">Citrix documentation</a>.</p>
<p>For the rest of this example, the user refers to the IdP address <code>idp.yourdomain.com</code>.</p>
</li>
</ol>
<h2 id="add-a-new-profile">Add a new profile</h2>
<ol>
<li>
<p>Go to <strong>Security</strong> &gt; <strong>AAA - Application Traffic</strong> &gt; <strong>Policies</strong> &gt; <strong>Authentication</strong> &gt; <strong>Advanced Policies</strong> &gt; <strong>SAML IDP</strong> to add a new profile.</p>
<p>Include the following required configuration details:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Name</strong></td>
<td>The certificate name you defined while <a href="#set-up-citrix-adc-saml">configuring SAML</a></td>
</tr>
<tr>
<td><strong>Assertion Consumer Service URL</strong></td>
<td><code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback</code></td>
</tr>
<tr>
<td><strong>IdP Certificate Name</strong></td>
<td>The IdP certificate name you defined while <a href="#set-up-citrix-adc-saml">configuring SAML</a></td>
</tr>
<tr>
<td><strong>Issuer Name</strong></td>
<td><code>https://idp.&lt;yourdomain&gt;.com/saml/login</code></td>
</tr>
<tr>
<td><strong>Service Provider ID</strong></td>
<td><code>https://idp.&lt;yourdomain&gt;.com/saml/login</code></td>
</tr>
<tr>
<td><strong>Name ID Format</strong></td>
<td>EmailAddress</td>
</tr>
<tr>
<td><strong>Attribute 1</strong></td>
<td><code>email = AAA.USER.ATTRIBUTE(&quot;email&quot;)</code></td>
</tr>
</tbody>
</table>
<p>Cloudflare Access currently sends the IdP address in place of the <em>Service Provider ID</em> for the AuthN request.</p>
<ol start="2">
<li>Create an Authentication Policy that refers to the Profile just created, and bind it to the authentication vServer mentioned above.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/citrixadc/citrixadc-saml-4.png" alt="Citrix AD Configure Authentication SAML IDP Policy" /></p>
<p>To configure all of the above using just the CLI, run the following:</p>
<pre><code class="language-json">add authentication samlIdPProfile samlProf_CloudflareAccess \&#10;    &#45;samlIdPCertName SAML_Signing \&#10;    &#45;assertionConsumerServiceURL &quot;https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&quot; \&#10;    &#45;samlIssuerName &quot;https://idp.yourdomain.com/saml/login&quot; \&#10;    &#45;rejectUnsignedRequests OFF \&#10;    &#45;NameIDFormat emailAddress \&#10;    &#45;Attribute1 email \&#10;    &#45;Attribute1Expr &quot;AAA.USER.ATTRIBUTE(\&quot;email\&quot;)&quot; \&#10;    &#45;Attribute1Format Basic \&#10;    &#45;serviceProviderID &quot;https://idp.yourdomain.com/saml/login&quot;&#10;&#10;add authentication samlIdPPolicy samlPol_CloudflareAccess -rule true -action samlProf_CloudflareAccess&#10;bind authentication vserver nsidp -policy samlPol_CloudflareAccess&#10;</code></pre>
<ol start="3">
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Configure the fields as follows:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Name</strong></td>
<td>Your chosen name</td>
</tr>
<tr>
<td><strong>Single Sign On URL</strong></td>
<td>The FQDN of the IdP, with the path <code>/saml/login</code></td>
</tr>
<tr>
<td><strong>IdP Entity ID/Issuer URL</strong></td>
<td>As above</td>
</tr>
<tr>
<td><strong>Signing Certificate</strong></td>
<td>The public certificate from the NetScaler</td>
</tr>
<tr>
<td><strong>Email attribute name</strong></td>
<td>This is listed under <strong>Optional configurations</strong></td>
</tr>
</tbody>
</table>
<ol start="6">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to the identity provider you want to test.</p>
