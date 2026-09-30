---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/
  description: Keycloak (SAML) in Zero Trust integrations.
  full_title: Keycloak (SAML) · Cloudflare One docs
  head_html: <title>Keycloak (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Keycloak (SAML) in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/index.md"><meta property="og:title" content="Keycloak (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Keycloak (SAML) in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/#page","headline":"Keycloak (SAML) \u00b7 Cloudflare One docs","description":"Keycloak (SAML) in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/keycloak/
  schema: 1
---
<p>Keycloak is an open source identity and access management solution built by JBoss.</p>
<h2 id="set-up-keycloak-saml">Set up Keycloak (SAML)</h2>
<p>To set up Keycloak (SAML) as your identity provider:</p>
<ol>
<li>
<p>In Keycloak, select the realm that you want Cloudflare Access to use.</p>
</li>
<li>
<p>Go to <strong>Clients</strong> &gt; <strong>Create client</strong>.</p>
</li>
<li>
<p>For <strong>Client type</strong>, select <strong>SAML</strong>.</p>
</li>
<li>
<p>Under <strong>Client ID</strong>, enter your Cloudflare Access callback URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="5">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Change <strong>Name ID format</strong> to <strong>email</strong>.</p>
</li>
<li>
<p>In <strong>Valid redirect URIs</strong>, enter your Cloudflare Access callback URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="8">
<li>In <strong>Master SAML Processing URL</strong>, enter the SAML endpoint for your Keycloak realm:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;keycloak_domain&gt;/realms/&lt;realm_name&gt;/protocol/saml&#10;</code></pre>
<p>Keycloak v17 and later use <code>/realms/&lt;realm_name&gt;/protocol/saml</code> by default. Keycloak v16 and earlier may use <code>/auth/realms/&lt;realm_name&gt;/protocol/saml</code> instead.</p>
<ol start="9">
<li>
<p>If you wish to enable client signatures, enable <strong>Client Signature Required</strong> and select <strong>Save</strong>.</p>
<ol>
<li>
<p>You will need to <a href="/cloudflare-one/integrations/identity-providers/signed_authn/">follow the steps here to get the certificate and enable it in the Cloudflare dashboard</a>.</p>
</li>
<li>
<p>Import the Access certificate you downloaded into the <strong>Keys</strong> tab. Use <strong>Certificate PEM</strong> as the format.</p>
</li>
</ol>
</li>
<li>
<p>Configure a protocol mapper for the user's email address.</p>
<ol>
<li>Go to <strong>Clients</strong> &gt; your Cloudflare Access SAML client &gt; <strong>Client scopes</strong>.</li>
<li>Select the dedicated client scope for the client.</li>
<li>Go to <strong>Mappers</strong> &gt; <strong>Add mapper</strong> &gt; <strong>By configuration</strong>.</li>
<li>Select <strong>User Property</strong>.</li>
<li>Set <strong>Property</strong> to <code>email</code> and <strong>SAML Attribute Name</strong> to <code>email</code>.</li>
</ol>
<p>Next, you will need to integrate with Cloudflare Access.</p>
</li>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Choose <strong>SAML</strong> on the next page.</p>
<p>You will need to input the Keycloak details manually. The examples below should be replaced with the specific domains in use with Keycloak and Cloudflare Access.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single Sign-On URL</td>
<td><code>https://&lt;keycloak_domain&gt;/realms/&lt;realm_name&gt;/protocol/saml</code></td>
</tr>
<tr>
<td>IdP Entity ID or Issuer URL</td>
<td><code>https://&lt;unique_id&gt;.cloudflareaccess.com/cdn-cgi/access/callback</code></td>
</tr>
<tr>
<td>Signing certificate</td>
<td>Use the X509 certificate from the Keycloak realm keys</td>
</tr>
</tbody>
</table>
<ol start="14">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to the login method you want to test.</p>
