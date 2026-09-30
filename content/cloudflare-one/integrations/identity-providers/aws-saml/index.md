<p>AWS IAM Identity Center provides SSO identity management for users who interact with AWS resources (such as EC2 instances or S3 buckets). You can integrate AWS IAM with Cloudflare Zero Trust as a SAML identity provider, which allows users to authenticate to Zero Trust using their AWS credentials.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Admin access to an IAM Identity Center <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html">organization instance</a></li>
</ul>
<h2 id="set-up-aws-iam-as-a-saml-provider">Set up AWS IAM as a SAML provider</h2>
<p>To set up SAML with AWS IAM as your identity provider:</p>
<ol>
<li>
<p>Open your <a href="https://console.aws.amazon.com/singlesignon">IAM Identity Center console</a> and go to <strong>Applications</strong>.</p>
</li>
<li>
<p>Select the <strong>Customer managed</strong> tab.</p>
</li>
<li>
<p>Select <strong>Add application</strong>.</p>
</li>
<li>
<p>Select <strong>I have an application I want to set up</strong>.</p>
</li>
<li>
<p>For <strong>Application type</strong>, select <strong>SAML 2.0</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Enter a <strong>Display name</strong> for the application (for example, <code>Cloudflare One</code>).</p>
</li>
<li>
<p>Download the <strong>IAM Identity Center SAML metadata file</strong>. You will need this file later when configuring the identity provider in Cloudflare One.</p>
</li>
<li>
<p>Under <strong>Application metadata</strong>, select <strong>Manually type your metadata values</strong>.</p>
</li>
<li>
<p>In <strong>Application ACS URL</strong> and <strong>Application SAML audience</strong>, enter the following URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="11">
<li>
<p>Select <strong>Submit</strong>.</p>
</li>
<li>
<p>Next, select the <strong>Actions</strong> dropdown menu and select <em>Edit attribute mappings</em>.</p>
</li>
<li>
<p>For the <code>Subject</code> user attribute, enter <code>${user:email}</code>.</p>
</li>
<li>
<p>(Recommended) Add user name attributes:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>User attribute</th>
<th>String value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td><code>${user:name}</code></td>
</tr>
<tr>
<td><code>surName</code></td>
<td><code>${user:familyName}</code></td>
</tr>
</tbody>
</table>
<p>| <code>givenName</code>    | <code>${user:givenName}</code>  |</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/aws/aws-saml-attributes.png" alt="Configuring attribute statements in IAM Identity Center" /></p>
<ol start="15">
<li>
<p>Select <strong>Save changes</strong>.</p>
</li>
<li>
<p>Under <strong>Assign users and groups</strong>, add individuals and/or groups that should be allowed to login to Cloudflare One.</p>
</li>
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
<p>Enter a <strong>Name</strong> for the IdP integration (for example, <code>AWS</code>).</p>
</li>
<li>
<p>Upload the <strong>IAM Identity Center SAML metadata file</strong> that you downloaded in Step 8.</p>
</li>
<li>
<p>(Recommended) Enable <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#sign-saml-authentication-request"><strong>Sign SAML authentication request</strong></a>.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test</a> that your connection is working, select <strong>Test</strong>.</p>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;https://portal.sso.eu-central-1.amazonaws.com/saml/assertion/b2yJrC4kjy3ZAS0a2SeDJj74ebEAxozPfiURId0aQsal3&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://portal.sso.eu-central-1.amazonaws.com/saml/assertion/b2yJrC4kjy3ZAS0a2SeDJj74ebEAxozPfiURId0aQsal3&quot;,&#10;		&quot;attributes&quot;: [&quot;email&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;email&quot;,&#10;		&quot;sign_request&quot;: true,&#10;		&quot;idp_public_certs&quot;: [&#10;			&quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;		]&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;AWS IAM SAML example&quot;&#10;}&#10;</code></pre>
