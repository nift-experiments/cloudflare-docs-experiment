---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/
  description: AWS IAM (SAML) in Zero Trust integrations.
  full_title: AWS IAM (SAML) · Cloudflare One docs
  head_html: <title>AWS IAM (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="AWS IAM (SAML) in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/index.md"><meta property="og:title" content="AWS IAM (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="AWS IAM (SAML) in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML,AWS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/#page","headline":"AWS IAM (SAML) \u00b7 Cloudflare One docs","description":"AWS IAM (SAML) in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML","AWS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/aws-saml/
  schema: 1
---
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
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
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
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;https://portal.sso.eu-central-1.amazonaws.com/saml/assertion/b2yJrC4kjy3ZAS0a2SeDJj74ebEAxozPfiURId0aQsal3&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://portal.sso.eu-central-1.amazonaws.com/saml/assertion/b2yJrC4kjy3ZAS0a2SeDJj74ebEAxozPfiURId0aQsal3&quot;,&#10;		&quot;attributes&quot;: [&quot;email&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;email&quot;,&#10;		&quot;sign_request&quot;: true,&#10;		&quot;idp_public_certs&quot;: [&#10;			&quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;		]&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;AWS IAM SAML example&quot;&#10;}&#10;</code></pre>
