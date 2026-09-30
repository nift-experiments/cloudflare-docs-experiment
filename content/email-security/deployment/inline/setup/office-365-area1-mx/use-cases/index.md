---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/
  description: Office 365 deployment use cases for Email Security with junk folder and quarantine configurations.
  full_title: Office 365 use cases · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Office 365 use cases · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Office 365 deployment use cases for Email Security with junk folder and quarantine configurations."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/index.md"><meta property="og:title" content="Office 365 use cases · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Office 365 deployment use cases for Email Security with junk folder and quarantine configurations."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/inline/setup/office-365-area1-mx/use-cases/
  schema: 1
---
<p>Before following our use case tutorials, read through this how-to guide related to best practices. This will show you how to prepare your Email security dashboard and enable options such as tagging and <a href="/email-security/email-configuration/email-policies/link-actions/">defanging emails</a>, as well as <a href="/email-security/email-configuration/email-policies/link-actions/#email-link-isolation">Email Link Isolation</a>, before setting up Office 365.</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Email Configuration</strong> &gt; <strong>Email Policies</strong> &gt; <strong>Link Actions</strong>.</p>
</li>
<li>
<p>What you do next depends on if you are an Advantage or Enterprise customer:</p>
<ol>
<li>If you are an <strong>Advantage</strong> customer:
<ol>
<li>In <strong>Disposition Actions</strong>, select <strong>Edit</strong>.</li>
<li>In the <code>SUSPICIOUS</code> disposition drop-down menu, change the action to <code>URL Defang</code>.</li>
</ol>
</li>
</ol>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/defang-suspicious.png" alt="Defang suspicious emails" /></p>
</div>
      3. Select **Save Disposition Actions**.
<ol start="2">
<li>If you are an <strong>Enterprise</strong> customer:
<ol>
<li>Enable <strong>Email Link Isolation</strong>.</li>
</ol>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step4-enterprise-advantage-customer.png" alt="Enable Email Link Isolation" /></p>
</div>
<ol start="5">
<li>
<p>Under <strong>Email Policies</strong>, select <strong>Text add-Ons</strong>.</p>
</li>
<li>
<p>Select <strong>Edit</strong>.</p>
</li>
<li>
<p>Enable the following options under <strong>Add Prefix To Subject</strong>:</p>
<ul>
<li><strong>Malicious</strong> - Enabled.</li>
<li><strong>Suspicious</strong> - Enabled.</li>
<li><strong>Spam</strong> - Enabled.</li>
<li><strong>Bulk</strong> - Enabled.</li>
<li><strong>Spoof</strong> - Enabled.</li>
<li><strong>Originated Outside of Company</strong> - Optional.</li>
<li><strong>Contains Encrypted Content</strong> - Optional.</li>
<li><strong>Subject Prefix</strong> - Format as desired.</li>
</ul>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/prefix-subject.png" alt="Enable all the options mentioned in step 9" /></p>
</div>
<ol start="8">
<li>In the same window, scroll down and enable the following options under <strong>Add Prefix To Body</strong>:
<ul>
<li><strong>Malicious</strong> - Enabled.</li>
<li><strong>Suspicious</strong> - Enabled.</li>
<li><strong>Spam</strong> - Disabled.</li>
<li><strong>Bulk</strong> - Disabled.</li>
<li><strong>Spoof</strong> - Enabled.</li>
<li><strong>Originated Outside of Company</strong> - Optional.</li>
<li><strong>Body Prefix</strong> - Format as desired. You can use the default settings. The body prefix supports HTML tags for formatting.</li>
</ul>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/o365-area1-mx/prefix-subject-enterprise.png" alt="Enable all the options mentioned in step 7" /></p>
</div>
<ol start="9">
<li>Select <strong>Update Text Add-Ons</strong>.</li>
</ol>
<h3 id="use-cases">Use cases</h3>
<p>Refer to the following use cases to learn how to set up your environment for different scenarios.</p>
<ul class="directory-listing"><li><a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/one-junk-admin-quarantine/">1 - Junk email and Email security (formerly Area 1) Admin Quarantine</a></li><li><a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/two-junk-user-quarantine/">2 - Junk email and user managed quarantine</a></li><li><a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/three-junk-admin-quarantine/">3 - Junk email and administrative quarantine</a></li><li><a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/four-user-quarantine-admin-quarantine/">4 - User managed quarantine and administrative quarantine</a></li><li><a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/five-junk-admin-quarantine/">5 - Junk email folder and administrative quarantine</a></li></ul>
