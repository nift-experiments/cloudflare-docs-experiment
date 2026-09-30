---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/create-project-gcp/
  description: Create a Google Cloud project and enable required APIs for Email Security Gmail BCC setup.
  full_title: Create a project on Google Cloud Console · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Create a project on Google Cloud Console · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a Google Cloud project and enable required APIs for Email Security Gmail BCC setup."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/create-project-gcp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/create-project-gcp/index.md"><meta property="og:title" content="Create a project on Google Cloud Console · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a Google Cloud project and enable required APIs for Email Security Gmail BCC setup."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/api/setup/gsuite-bcc-setup/create-project-gcp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/api/setup/gsuite-bcc-setup/create-project-gcp/
  schema: 1
---
<ol>
<li>Log in to the <a href="https://console.cloud.google.com/welcome/new">Google Cloud Console</a>. From the dashboard, select <strong>CREATE OR SELECT PROJECT</strong>.</li>
<li>Provide the details for the new project, and select <strong>CREATE</strong> to start your new project.</li>
<li>Once the new project has been created, the Google Cloud Platform console will automatically redirect you to the Project console. If not, you can use the Project selector to change to the project you created.</li>
<li>In <strong>Getting Started</strong>, select <strong>Explore and enable APIs</strong> &gt; Select <strong>ENABLE APIs &amp; SERVICES</strong>.</li>
<li>On search bar, search for <code>Admin SDK API</code>. Select <strong>Admin SDK API</strong>, then select <strong>ENABLE</strong>.</li>
<li>Go back to the sidebar, select <strong>Library</strong>, and search for Gmail API. Select <strong>Gmail API</strong>, then select <strong>ENABLE</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have created a project on Google Cloud Console, you need to <a href="/email-security/deployment/api/setup/gsuite-bcc-setup/create-service-account/">create a service account</a> on Google Cloud Console.</p>
