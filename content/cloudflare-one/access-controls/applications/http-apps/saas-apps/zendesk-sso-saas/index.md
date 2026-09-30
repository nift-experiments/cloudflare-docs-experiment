---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/zendesk-sso-saas/
  description: Integrate Zendesk with Access.
  full_title: Zendesk · Cloudflare One docs
  head_html: <title>Zendesk · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Zendesk with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/zendesk-sso-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/zendesk-sso-saas/index.md"><meta property="og:title" content="Zendesk · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Zendesk with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/zendesk-sso-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/zendesk-sso-saas/#page","headline":"Zendesk \u00b7 Cloudflare One docs","description":"Integrate Zendesk with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/zendesk-sso-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/zendesk-sso-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://support.zendesk.com/hc/en-us/articles/4408887505690-Enabling-SAML-single-sign-on#topic_u54_wc3_z2b">Zendesk</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to your Zendesk account</li>
</ul>
<h2 id="configure-zendesk-and-cloudflare">Configure Zendesk and Cloudflare</h2>
<ol>
<li>
<p>Go to your Zendesk administrator dashboard, typically available at <code>&lt;yourdomain&gt;.zendesk.com/admin/security/sso</code>.</p>
</li>
<li>
<p>In a separate tab or window, open the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select your account, and go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>, then choose <strong>SaaS application</strong>.</p>
</li>
<li>
<p>Input the following values in the Cloudflare One application configuration:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Cloudflare One field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Entity ID</strong></td>
<td><code>https://&lt;yoursubdomain&gt;.zendesk.com</code></td>
</tr>
<tr>
<td><strong>Assertion Consumer Service URL</strong></td>
<td>contents of <strong>SAML SSO URL</strong> in Zendesk account</td>
</tr>
<tr>
<td><strong>Name ID Format</strong></td>
<td><em>Email</em></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>(Optional) Configure these Attribute Statements to include a user's first and last name:</li>
</ol>
<table>
<thead>
<tr>
<th>Cloudflare attribute name</th>
<th>IdP attribute value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;first name&gt;</code></td>
<td><code>http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname</code></td>
</tr>
<tr>
<td><code>&lt;last name&gt;</code></td>
<td><code>http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname</code></td>
</tr>
</tbody>
</table>
<p>Zendesk will <a href="https://support.zendesk.com/hc/en-us/articles/203663676#topic_dzb_gl5_2v">use the user's email address as their name</a> if the name is not provided.</p>
<ol start="6">
<li>
<p>To determine who can access Zendesk, <a href="/cloudflare-one/access-controls/policies/">create an Access policy</a>.</p>
</li>
<li>
<p>Copy the <strong>SSO Endpoint</strong> and <strong>Public Key</strong>.</p>
</li>
<li>
<p>Transform the public key into a fingerprint:</p>
<ol>
<li>
<p>Open a <a href="https://www.samltool.com/fingerprint.php">fingerprint calculator</a>.</p>
</li>
<li>
<p>Paste the <strong>Public Key</strong> into <strong>X.509 cert</strong>.</p>
</li>
<li>
<p>Wrap the value with <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</p>
</li>
<li>
<p>Set <strong>Algorithm</strong> to <em>SHA256</em> and select <strong>Calculate Fingerprint</strong>.</p>
</li>
<li>
<p>Copy the <strong>Formatted FingerPrint</strong> value.</p>
</li>
</ol>
</li>
<li>
<p>Add the Cloudflare values to the following Zendesk fields:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Cloudflare IdP field</th>
<th>Zendesk field</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>SSO Endpoint</strong></td>
<td><strong>SAML SSO URL</strong></td>
</tr>
<tr>
<td><strong>Public Key</strong> (transformed to fingerprint)</td>
<td><strong>Certificate Fingerprint</strong></td>
</tr>
</tbody>
</table>
<ol start="10">
<li>Go to <code>https://&lt;yourdomain&gt;.zendesk.com/admin/security/staff_members</code> and enable <strong>External Authentication</strong> &gt; <strong>Single Sign On</strong>.</li>
</ol>
<p>Users should now be able to log in to Zendesk if their Email address exists in the Zendesk user list.</p>
