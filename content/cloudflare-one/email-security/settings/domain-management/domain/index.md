---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/domain-management/domain/
  description: How Information about your domain works in Email Security.
  full_title: Information about your domain · Cloudflare One docs
  head_html: <title>Information about your domain · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Information about your domain works in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/domain-management/domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/domain-management/domain/index.md"><meta property="og:title" content="Information about your domain · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Information about your domain works in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/domain-management/domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/domain-management/domain/#page","headline":"Information about your domain \u00b7 Cloudflare One docs","description":"How Information about your domain works in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/domain-management/domain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/domain-management/domain/
  schema: 1
---
<p>When you configure your domain, the Cloudflare dashboard will display you the following fields:</p>
<ul>
<li><strong>Domain</strong>: Domain name. Refer to <a href="/cloudflare-one/email-security/setup/manage-domains/">Manage domains</a> to learn how to add, filter, and delete domains.</li>
<li><strong>Configured method</strong>: The deployment method you used to configure your domain. Depending on how you decided to configure Email security, the dashboard will display:
<ul>
<li><strong>MS Graph API</strong>: Your current email provider is Microsoft 365, and Email security has been configured via the Microsoft Graph API. You do not need to change any MX record.</li>
<li><strong>BCC/Journaling</strong>: You have chosen to set your email via BCC/Journaling. A copy of your email is sent to Cloudflare.</li>
<li><strong>MX/ Inline</strong>: You have configured your email domain using MX/Inline. This configuration requires a <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">DNS record change</a>.</li>
</ul>
</li>
<li><strong>Status</strong>: Status indicates the state of the configuration.
<ul>
<li>For MX/Inline and BCC/Journaling, the dashboard will display <strong>Active</strong> if Email security has processed any email in the last seven days. The dashboard will display <strong>No mail flow</strong> if there has been no email activity in the last seven days. This is likely due to a misconfiguration. Refer to <a href="/cloudflare-one/email-security/setup/#5-configuration-checklist">Configuration checklist</a> to ensure you have configured your environment correctly.</li>
<li>For MS Graph API, the dashboard will display <strong>Active</strong> if your integration has been successfully connected, and Email security can scan your inbox with the integration. The dashboard will display <strong>Broken</strong> if the API is not scanning emails. This could be due to a CASB misconfiguration. To troubleshoot this, refer to <a href="/cloudflare-one/cloud-and-saas-findings/troubleshoot-casb/">Troubleshoot CASB</a>.</li>
</ul>
</li>
<li><strong>Service address</strong>: This is the email address you will use to send a copy of your email.</li>
<li><strong>Source</strong>: Depending on how you added the domains, the dashboard will display <strong>MS integration</strong>, <strong>Google</strong>, <strong>CF zones</strong>, or <strong>Manual add</strong>.</li>
<li><strong>Integration name</strong>: Name of the integration. This field will only be displayed for Microsoft integrations. To rename your integration:
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS</strong>.</li>
<li>Locate your integration, select <strong>Configure</strong>, then select <strong>Edit</strong>.</li>
<li>Rename your integration, then select <strong>Save</strong>.</li>
</ol>
</li>
<li><strong>Hops</strong>: The number of hops. This will not be displayed if the configuration method is Microsoft Graph API. Hop count will be visible only if it has been configured.</li>
<li><strong>Date added</strong>: Date when the domain was added.</li>
</ul>
