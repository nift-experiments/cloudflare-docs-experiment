---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/phishnet-gworkspace/
  description: Deploy the PhishNet add-in for Google Workspace so users can report missed phishing emails to Email security.
  full_title: PhishNet for Google Workspace · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>PhishNet for Google Workspace · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy the PhishNet add-in for Google Workspace so users can report missed phishing emails to Email security."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/phishnet-gworkspace/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/phishnet-gworkspace/index.md"><meta property="og:title" content="PhishNet for Google Workspace · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy the PhishNet add-in for Google Workspace so users can report missed phishing emails to Email security."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/phishnet-gworkspace/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/phish-submissions/phishnet-gworkspace/
  schema: 1
---
<p>PhishNet is an add-in button that helps users to submit directly to Email security (formerly Area 1) <span class="nb-glossary-tooltip" title="phishing">phish</span> samples missed by Area 1’s detection. PhishNet avoids the previous process, where users had to report phish to their email admins, which then had to manually download and forward the sample to Email security.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To set up PhishNet with Google Workspace you need admin access to your Google Workspace account.</p>
<h2 id="set-up-phishnet-for-google-workspace">Set up PhishNet for Google Workspace</h2>
<ol>
<li>
<p>Log in to <a href="https://workspace.google.com/marketplace/app/cloudflare_phishnet/11369379045">Google Workspace Marketplace apps</a> using this direct link and an administrator account.</p>
</li>
<li>
<p>Select <strong>Admin install</strong> to install Cloudflare PhishNet. Read the warning, and select <strong>Continue</strong>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-gworkspace/step1-phishnet-install.png" alt="Select Admin install to start installing Cloudflare PhishNet" /></p>
</div>
<ol start="3">
<li>In the window that opens, choose between installing Cloudflare PhishNet for <strong>Everyone at your organization</strong> or <strong>Certain groups or organizational units</strong>. If you choose this last option, you will also have to select which users you want to install PhishNet to.</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-gworkspace/step3-select-users.png" alt="Select to which users you want to install PhishNet to" /></p>
</div>
<ol start="4">
<li>
<p>After choosing the groups you want to install PhishNet for, agree with Google’s terms of service, and select <strong>Finish</strong>.</p>
</li>
<li>
<p>Google Workspace will inform you that Cloudflare PhishNet has been installed. Select <strong>Done</strong> to continue.</p>
</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-gworkspace/step5-done.png" alt="If everything goes well, you will need to select Done to continue." /></p>
</div>
<p>Cloudflare PhishNet is now installed.</p>
<h2 id="submit-phish-with-phishnet">Submit phish with PhishNet</h2>
<ol>
<li>
<p>In your Gmail web client, open the message you would like to flag as either spam or phish.</p>
</li>
<li>
<p>(Optional) Open Gmail’s <strong>side panel</strong> if it is not already opened.</p>
</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-gworkspace/step2-side-panel.png" alt="Open the side panel on Gmail's interface if you need to" /></p>
</div>
<ol start="3">
<li>Select the <strong>PhishNet logo</strong>.</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-gworkspace/step3-logo.png" alt="Select PhishNet's logo" /></p>
</div>
<ol start="4">
<li>Under <strong>Select Submission Type</strong>, select the type of your submission — <em>Spam</em> or <em>Phish</em>.</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/phish-submissions/phishnet-gworkspace/step4-submission-type.png" alt="Choose the type of submission you'd like to make" /></p>
</div>
<ol start="5">
<li>Select <strong>Submit Report</strong>.</li>
</ol>
<p>PhishNet will show you a <strong>Submission Complete</strong> message once the email has been successfully submitted to Email security (formerly Area 1) for review.</p>
