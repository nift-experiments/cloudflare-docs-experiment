---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/docusign-access/
  description: Integrate DocuSign with Access.
  full_title: DocuSign · Cloudflare One docs
  head_html: <title>DocuSign · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate DocuSign with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/docusign-access/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/docusign-access/index.md"><meta property="og:title" content="DocuSign · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate DocuSign with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/docusign-access/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/docusign-access/#page","headline":"DocuSign \u00b7 Cloudflare One docs","description":"Integrate DocuSign with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/docusign-access/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/docusign-access/
  schema: 1
---
<p>This guide covers how to configure <a href="https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&amp;topicId=ozd1583359139126.html">Docusign</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Docusign account that has Single Sign-On available</li>
<li>A <a href="https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&amp;topicId=gso1583359141256.html">domain</a> verified in Docusign</li>
</ul>
<h2 id="1-create-the-access-for-saas-application"><ol>
<li>Create the Access for SaaS application</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>SaaS application</strong>.</p>
</li>
<li>
<p>Use the following configuration:</p>
<ul>
<li>Set the <strong>Application</strong> to <em>DocuSign</em>.</li>
<li>Put placeholder values in <strong>EntityID</strong> and <strong>Assertion Consumer Service URL</strong> (for example, <code>https://example.com</code>). We'll come back and update these.</li>
<li>Set <strong>Name ID Format</strong> to: <em>Unique ID</em>.</li>
</ul>
</li>
<li>
<p>DocuSign requires SAML attributes to do Just In Time user provisioning. Ensure you are collecting SAML attributes from your IdP:</p>
<ul>
<li>Group</li>
<li>username</li>
<li>department</li>
<li>firstName</li>
<li>lastName</li>
<li>phone</li>
</ul>
</li>
<li>
<p>These IdP SAML values can then be mapped to the following DocuSign SAML attributes:</p>
<ul>
<li>Email</li>
<li>Surname</li>
<li>Givenname</li>
</ul>
</li>
<li>
<p>Set an Access policy (for example, create a policy based on <em>Emails ending in @example.com</em>).</p>
</li>
<li>
<p>Copy and save the <strong>SSO Endpoint</strong>, <strong>Entity ID</strong> and <strong>Public Key</strong>.</p>
</li>
<li>
<p>Transform the <strong>Public Key</strong> into a fingerprint:</p>
<pre tabindex="0"><code>1. Copy the **Public Key** Value.&#10;&#10;2. Paste the **Public Key** into VIM or another code editor.&#10;&#10;3. Wrap the value in `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.&#10;&#10;4. Set the file extension to `.crt` and save.&#10;</code></pre>
</li>
</ol>
<h2 id="2-configure-your-docusign-sso-instance"><ol start="2">
<li>Configure your DocuSign SSO instance</li>
</ol></h2>
<ol>
<li>
<p>Ensure you have a domain claimed in DocuSign.</p>
</li>
<li>
<p>From the DocuSign Admin dashboard, select <strong>Identity Providers</strong>.</p>
</li>
<li>
<p>On the Identity Providers page, select <strong>ADD IDENTITY PROVIDER</strong>. Use the following mappings from the saved Access Application values:</p>
<ul>
<li><strong>Name</strong>: Pick your desired name.</li>
<li><strong>Identity Provider Issuer</strong>: Entity ID.</li>
<li><strong>Identity Provider Login URL</strong>: Assertion Consumer Service URL.</li>
</ul>
</li>
<li>
<p>Save the Identity Provider.</p>
</li>
<li>
<p>Upload your certificate to the <em>DocuSign Identity Provider</em> menu.</p>
</li>
<li>
<p>Configure your SAML Attribute mappings. The Attribute Names should match the values in <strong>IdP Value</strong> in your Access application.</p>
</li>
<li>
<p>Go back to the Identity Provider's screen and select <strong>Actions</strong> &gt; <strong>Endpoints</strong>. Copy and save the following:</p>
<ul>
<li>Service Provider Issuer URL.</li>
<li>Service Provider Assertion Consumer Service URL.</li>
</ul>
</li>
</ol>
<h2 id="3-finalize-your-cloudflare-configuration"><ol start="3">
<li>Finalize your Cloudflare configuration</li>
</ol></h2>
<ol>
<li>Go back to your DocuSign application under <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Edit</strong>.</li>
<li>Use the following mappings:
<ul>
<li>EntityID-&gt;Service Provider Issuer URL.</li>
<li>Assertion Consumer Service URL -&gt; Service Provider Assertion Consumer Service URL.</li>
</ul>
</li>
<li>Save the application.</li>
</ol>
<p>When ready, enable the SSO for your DocuSign account and you will be able to login to DocuSign via Cloudflare SSO and your Identity Provider.</p>
