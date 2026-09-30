---
cp9:
  canonical: https://developers.cloudflare.com/multi-cloud-networking/manage-resources/
  description: Manage cloud on-ramp resources and connections.
  full_title: Manage resources · Cloudflare Multi-Cloud Networking docs
  head_html: <title>Manage resources · Cloudflare Multi-Cloud Networking docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage cloud on-ramp resources and connections."><link rel="canonical" href="https://developers.cloudflare.com/multi-cloud-networking/manage-resources/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/multi-cloud-networking/manage-resources/index.md"><meta property="og:title" content="Manage resources · Cloudflare Multi-Cloud Networking docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage cloud on-ramp resources and connections."><meta property="og:url" content="https://developers.cloudflare.com/multi-cloud-networking/manage-resources/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Multi-Cloud Networking"><meta name="algolia_product_filter" content="Multi-Cloud Networking"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Multi-Cloud Networking"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/multi-cloud-networking/manage-resources/#page","headline":"Manage resources \u00b7 Cloudflare Multi-Cloud Networking docs","description":"Manage cloud on-ramp resources and connections.","url":"https://developers.cloudflare.com/multi-cloud-networking/manage-resources/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /multi-cloud-networking/manage-resources/
  schema: 1
---
<h2 id="cloud-resource-catalog">Cloud resource catalog</h2>
<p>Your cloud environment is built from individual cloud resources, like virtual private clouds (VPCs), subnets, virtual machines (VMs), route tables, and routes. Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta) discovers all of your cloud resources and stores their configuration and status in the Cloud resource catalog, a read-only snapshot of your cloud environment. Discovery runs regularly in the background, keeping your catalog up to date as your environment changes.</p>
<p>To browse the resources in your catalog:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>In <strong>Cloud resources</strong>, select a resource to inspect its details.</li>
</ol>
<h2 id="edit-cloud-integrations">Edit Cloud integrations</h2>
<p>You can change which cloud account the integration is linked to or delete the integration.</p>
<ol>
<li>Go to <strong>Cloud integrations</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your integration &gt; <strong>Edit</strong>.</li>
<li>In <strong>Linked account details</strong>, select <strong>Link integration to a different cloud account</strong>.</li>
<li>Select <strong>Save</strong> when you are finished.</li>
<li>(Optional) You can also select <strong>Delete</strong> to delete your cloud integration.</li>
</ol>
<h2 id="download-cloud-resource-catalog">Download cloud resource catalog</h2>
<p>You can download a JSON file containing metadata and configuration for all your cloud resources:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>In <strong>Cloud resources</strong>, select <strong>Download catalog</strong>.</li>
</ol>
<p>After your browser finishes downloading the ZIP file, expand it to access the JSON with the information about your cloud resources.</p>
