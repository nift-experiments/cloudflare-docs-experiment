<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5087.md")
</aside>
<p>Active Directory is a directory service developed by Microsoft for Windows domain networks. It is included in most Windows Server operating systems as a set of processes and services. Active Directory integrates with Cloudflare Access using Security Assertion Markup Language (<div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5088.md")
</div>).
<h2 id="before-you-start">Before you start</h2>
<p>To get started, you need:</p>
<ul>
<li>An Active Directory Domain Controller where all users have an email attribute.</li>
<li>Generic SAML enabled for your Access Identity Provider (IdP).</li>
<li>A Microsoft server running with Active Directory Federation Services (AD FS) installed. All screenshots in these instructions are for Server 2012R2. Similar steps will work for newer versions.</li>
<li>A browser safe certificate for Active Directory Federation Services (AD FS).</li>
</ul>
<p>Once you fulfill the requirements above, you are ready to begin. Installation and basic configuration of Active Directory Federation Services (AD FS) is outside the scope of this guide. A detailed guide can be found in a <a href="https://docs.microsoft.com/en-us/previous-versions/dynamicscrm-2016/deployment-administrators-guide/gg188612(v=crm.8)">Microsoft KB</a>.</p>
<p>Then to begin the connection between Cloudflare Access and AD FS create a Relying Party Trust in AD FS.</p>
<h2 id="create-a-relying-party-trust">Create a Relying Party Trust</h2>
<p>Run the Add Relying Party Trust wizard to begin SAML AD integration with Cloudflare Access.</p>
<p>To create a Relying Party Trust:</p>
<ol>
<li>
<p>In <strong>Windows Server</strong>, launch the <strong>ADFS Management</strong> tool.</p>
</li>
<li>
<p>Select the <strong>Relying Party Trusts</strong> folder.</p>
</li>
<li>
<p>On the <strong>Actions</strong> sidebar, select <strong>Add Relying Party Trust</strong>. The <strong>Add Relying Party Trust Wizard</strong> launches.</p>
</li>
<li>
<p>In the left menu, choose <strong>Select Data Source</strong>.</p>
</li>
<li>
<p>Select the <strong>Enter data about the relying party manually</strong> option.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Enter a <strong>Display name</strong>. We suggest you use a recognizable name. Include any information regarding this connection in the <strong>Notes</strong> field.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Choose Profile</strong> step displays.</p>
</li>
<li>
<p>Select the <strong>AD FS profile</strong> option.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Configure Certificate</strong> step displays.</p>
</li>
<li>
<p>Leave the <strong>Certificate</strong> options at their defaults.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Configure URL</strong> step displays.</p>
</li>
<li>
<p>Select the <strong>Enable support for the SAML 2.0 WebSSO protocol</strong> option.</p>
</li>
<li>
<p>In the <strong>Relying party SAML 2.0 SSO service URL</strong> field, enter the following URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<pre><code>You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<ol start="15">
<li>Select <strong>Next</strong>. The <strong>Configure Identifiers</strong> step displays.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/adfs/adfs-7.png" alt="Add relying party trust wizard with callback URL pasted into open form field" /></p>
<ol start="16">
<li>
<p>Paste your callback URL in the <strong>Relying party trust identifier</strong> field.</p>
</li>
<li>
<p>Select <strong>Next</strong>. In the <strong>Configure Multi-factor Authentication Now?</strong> step, you can configure multi-factor authentication.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Choose Issuance Authorization Rules</strong> step displays.</p>
</li>
<li>
<p>Select the <strong>Permit all users to access this relying party</strong> option.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Ready to Add Trust</strong> step displays.</p>
</li>
<li>
<p>Review your settings.</p>
</li>
<li>
<p>Select <strong>Next</strong>. Cloudflare now relies on AD FS for user-identity authorization.</p>
</li>
</ol>
<p>The <strong>Edit Claim Rules for CF Login</strong> screen automatically displays.</p>
<h2 id="create-claim-rules">Create claim rules</h2>
<p>Now create 2 Claim Rules so that AD FS can take information from Cloudflare and return it to create <a href="/cloudflare-one/access-controls/policies/">Access policies</a>.</p>
<p>If you closed the Add Relying Trust wizard, use Explorer to find the <strong>Relying Party Trusts</strong> folder, select the newly created RPT file, and select <strong>Edit Claim Rules</strong> in the <strong>Action</strong> sidebar.</p>
<p>To create Claim Rules:</p>
<ol>
<li>
<p>In the <strong>Edit Claim Rules for CF Login</strong> window, select <strong>Add Rule</strong>. The <strong>Choose Rule Type</strong> step displays.</p>
</li>
<li>
<p>In the <strong>Claim rule template</strong> field, select <strong>Send LDAP Attributes as Claims</strong> from the drop-down list.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Edit Rule — Send Email</strong> step displays.</p>
</li>
<li>
<p>Enter a descriptive <strong>Claim rule name</strong>.</p>
</li>
<li>
<p>Select <strong>Active Directory</strong> from the <strong>Attribute store</strong> drop-down list.</p>
</li>
<li>
<p>Select <strong>E-mail-Addresses</strong> from the <strong>LDAP Attribute</strong> and <strong>Outgoing Claim Type</strong> drop-down lists.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="ad-fs-groups">AD FS groups</h3>
@markup("md", "content/.markup/bodies/5086.md")
</aside>
<ol start="7">
<li>
<p>Select <strong>OK</strong>. You return to the <strong>Choose Rule Type</strong> step.</p>
</li>
<li>
<p>Select <strong>Transform an Incoming Claim</strong> from the <strong>Claim rule template</strong> drop-down list to create the second rule.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Edit - Create Transient Name Identifier</strong> window displays.</p>
</li>
<li>
<p>Enter a descriptive <strong>Claim rule name</strong>.</p>
</li>
<li>
<p>Select <strong>E-Mail Address</strong> from the <strong>Incoming claim type</strong> drop-down list.</p>
</li>
<li>
<p>Select <strong>Name ID</strong> from the <strong>Outgoing claim type</strong> drop-down list.</p>
</li>
<li>
<p>Select <strong>Transient Identifier</strong> from the <strong>Outgoing name ID format</strong> drop-down list.</p>
</li>
<li>
<p>Ensure that the <strong>Pass through all claim values</strong> option is selected.</p>
</li>
<li>
<p>Select <strong>OK</strong>.</p>
</li>
</ol>
<p>Both Claim Rules are now available to export to your Cloudflare Access account.</p>
<h2 id="export-the-certificate">Export the certificate</h2>
<p>Now you'll configure Cloudflare to recognize AD FS by extracting the <em>token-signing certificate</em> from AD FS.</p>
<p>To export the certificate:</p>
<ol>
<li>
<p>Within the AD FS management console, select the <strong>Service</strong> under AD FS and choose the <strong>Certificates</strong> folder which contains the certificate to export.</p>
</li>
<li>
<p>In the <strong>Certificates</strong> card, right-click on the entry under <strong>Token-signing</strong>, and select <strong>View certificate</strong>. The <strong>Certificates</strong> window displays.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/adfs/adfs-16.png" alt="Certificates window with token-signing certificate selected" /></p>
<ol start="3">
<li>
<p>Select the <strong>Details</strong> tab, and select the <strong>Copy to File</strong> option.</p>
</li>
<li>
<p>The <strong>Certificate Export Wizard</strong> displays.</p>
</li>
<li>
<p>Select <strong>Next</strong>. The <strong>Export File Format</strong> window displays.</p>
</li>
<li>
<p>Select the <strong>Base-64 encoded X.509 (.CER)</strong> option.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Enter a name for the file.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Select <strong>Finish</strong>.</p>
<p>Note the file path for later.</p>
</li>
</ol>
<h2 id="configure-ad-fs-to-sign-saml-responses">Configure AD FS to sign SAML responses</h2>
<p>To ensure that AD FS signs the full response when communicating with Cloudflare, open your local <strong>PowerShell</strong> and enter the following command:</p>
<pre><code class="language-bash">Set-ADFSRelyingPartyTrust -TargetName &quot;Name of RPT Display Name&quot; -SamlResponseSignature &quot;MessageAndAssertion&quot;&#10;</code></pre>
<h2 id="configure-cloudflare-one">Configure Cloudflare One</h2>
<p>To enable Cloudflare One to accept the claims and assertions sent from AD FS, follow these steps:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>SAML</strong>.</p>
</li>
<li>
<p>Enter an IdP <strong>Name</strong>.</p>
</li>
<li>
<p>Under <strong>Single Sign On URL</strong> enter:</p>
</li>
</ol>
<pre><code class="language-txt">https://hostnameOfADFS/adfs/ls/&#10;</code></pre>
<p>This is the default location. You can find your federation service identifier in AD FS.</p>
<ol start="6">
<li>In the <strong>IdP Entity ID or Issuer URL</strong> field, enter your Cloudflare Zero Trust team domain and include this callback at the end of the path: <code>/cdn-cgi/access/callback</code>. For example:</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="7">
<li>
<p>Under <strong>Signing certificate</strong>, paste the exported certificate.</p>
<p>There can be no spaces or return characters in the text field.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to the identity provider you want to test.</p>
<h2 id="download-sp-metadata-optional">Download SP metadata (optional)</h2>
<p>Some IdPs allow administrators to upload metadata files from their SP (service provider).</p>
<p>To get your Cloudflare metadata file:</p>
<ol>
<li>Download your unique SAML metadata file at the following URL:</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/saml-metadata&#10;</code></pre>
<p>In Cloudflare Access, you can find a link to this URL in the <strong>Edit a SAML identity provider</strong> dialog. The link returns a web page with your SAML SP data in XML format.</p>
<ol start="2">
<li>
<p>Save the file in XML format.</p>
</li>
<li>
<p>Upload the XML document to your <strong>Active Directory</strong> account.</p>
</li>
</ol>
<h2 id="example-api-configuration">Example API Configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;https://&lt;your-team-name&gt;.cloudflareaccess.com/&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://adfs.example.com/adfs/ls/&quot;,&#10;		&quot;attributes&quot;: [&quot;email&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;&quot;,&#10;		&quot;sign_request&quot;: false,&#10;		&quot;idp_public_cert&quot;: &quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;adfs saml example&quot;&#10;}&#10;</code></pre>
