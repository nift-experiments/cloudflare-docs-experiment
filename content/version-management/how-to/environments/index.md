---
cp9:
  canonical: https://developers.cloudflare.com/version-management/how-to/environments/
  description: Create and configure Version Management environments.
  full_title: Manage environments · Cloudflare Version Management docs
  head_html: <title>Manage environments · Cloudflare Version Management docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and configure Version Management environments."><link rel="canonical" href="https://developers.cloudflare.com/version-management/how-to/environments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/version-management/how-to/environments/index.md"><meta property="og:title" content="Manage environments · Cloudflare Version Management docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and configure Version Management environments."><meta property="og:url" content="https://developers.cloudflare.com/version-management/how-to/environments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Version Management"><meta name="algolia_product_filter" content="Version Management"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Version Management"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/version-management/how-to/environments/#page","headline":"Manage environments \u00b7 Cloudflare Version Management docs","description":"Create and configure Version Management environments.","url":"https://developers.cloudflare.com/version-management/how-to/environments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /version-management/how-to/environments/
  schema: 1
---
<p>An environment is a place to test different versions of your zone configurations.</p>
<hr />
<h2 id="create-environment">Create environment</h2>
<p>Once you <a href="/version-management/how-to/enable/">enable</a> Version Management, Cloudflare will automatically create:</p>
<ul>
<li><strong>Version Zero</strong>, think about this as the configuration of your current zone. Once default environments are created, Version Zero is automatically deployed to them, guaranteeing no disruption in your live traffic. This Version is also permanently editable. In case you decide to disable Zone Versioning, Version Zero will become your zone again.</li>
<li><strong>Global Configuration</strong>, you can find all the configurations here that are not supported by Version Management.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15312.md")
</aside>
<p>On the Environments page, you can create default environments for <strong>Production</strong>, <strong>Staging</strong>, and <strong>Development</strong>.</p>
<p>Based on your organization's needs, you may need to create additional environments to test and roll out changes.
<br/></p>
<p>To create a new environment:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and zone.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Version Management</strong>.</li>
<li>Go to <strong>Environments</strong>.</li>
<li>Select <strong>Create Environment</strong>.</li>
<li>Provide the following information:</li>
</ol>
<ul>
<li><strong>Environment Name</strong>: A unique, descriptive name for the environment.</li>
<li><a href="/version-management/reference/traffic-filters/"><strong>Traffic filter</strong></a>: Limits which requests are sent to this environment.</li>
<li><strong>Initial position</strong>: Controls where this environment should be in your testing process.</li>
</ul>
<ol start="6">
<li>Select <strong>Create</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15311.md")
</aside>
<hr />
<h2 id="edit-environment">Edit environment</h2>
<p>To edit an environment:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and zone.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Version Management</strong>.</li>
<li>Select <strong>Environments</strong>.</li>
<li>On a specific environment, select <strong>Edit</strong>.</li>
<li>Make any required changes.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<hr />
<h2 id="change-environment-version">Change environment version</h2>
<p>To prevent accidental changes, you can only update an environment's version through the process of <strong>Promotion</strong> or <strong>Roll back</strong>.</p>
<p>For more details on the flow of versions and environments, refer to <a href="/version-management/about/">How it works</a>.</p>
<h3 id="promote-a-version">Promote a version</h3>
<p>Promotion moves a version from a lower-ranked environment to the next highest one.</p>
<p>To promote a version:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and zone.</li>
<li>Go to <strong>Version Management</strong>.</li>
<li>Select <strong>Environments</strong>.</li>
<li>On the environment in which you tested the version, select <strong>Promote</strong>. This option will only be available if the lower-ranked environment has a different version than the higher-ranked environment.</li>
</ol>
<p>Promoting a version to a read-only environment will make the version permanently read-only.
<br/></p>
<h3 id="roll-back-a-version">Roll back a version</h3>
<p>When you roll back a version, you revert the environment to the previous version assigned to it.</p>
<p>To roll back a version:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and zone.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Version Management</strong>.</li>
<li>Select <strong>Environments</strong>.</li>
<li>On a specific environment, select <strong>Roll back</strong>.</li>
</ol>
<hr />
<h2 id="delete-environment">Delete environment</h2>
<p>To delete an environment:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and zone.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Version Management</strong>.</li>
<li>Select <strong>Environments</strong>.</li>
<li>On a specific environment, select <strong>Edit</strong>.</li>
<li>Select <strong>Delete Environment</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15310.md")
</aside>
