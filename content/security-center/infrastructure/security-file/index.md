---
cp9:
  canonical: https://developers.cloudflare.com/security-center/infrastructure/security-file/
  description: Manage your security.txt file via the dashboard or the API.
  full_title: Set up your security.txt file · Cloudflare Security Center docs
  head_html: <title>Set up your security.txt file · Cloudflare Security Center docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage your security.txt file via the dashboard or the API."><link rel="canonical" href="https://developers.cloudflare.com/security-center/infrastructure/security-file/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security-center/infrastructure/security-file/index.md"><meta property="og:title" content="Set up your security.txt file · Cloudflare Security Center docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage your security.txt file via the dashboard or the API."><meta property="og:url" content="https://developers.cloudflare.com/security-center/infrastructure/security-file/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security Center"><meta name="algolia_product_filter" content="Security Center"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security-center/infrastructure/security-file/#page","headline":"Set up your security.txt file \u00b7 Cloudflare Security Center docs","description":"Manage your security.txt file via the dashboard or the API.","url":"https://developers.cloudflare.com/security-center/infrastructure/security-file/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security-center/infrastructure/security-file/
  schema: 1
---
<p>You can manage your <a href="https://en.wikipedia.org/wiki/Security.txt">security.txt</a> file via the dashboard or the <a href="/api/resources/security_txt/">API</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13821.md")
</aside>
<p>To manage your security.txt file via the Cloudflare dashboard:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select your account and domain.</li>
<li>Go to <strong>Security</strong> &gt; <strong>Settings</strong> and filter by <strong>Web application exploits</strong>.</li>
<li>Under <strong>Security.txt</strong> &gt; <strong>Configurations</strong>, select the edit icon.</li>
</ol>
<p>From here, you can create and manage your <code>security.txt</code> file to provide the security research team with a standardized way to report vulnerabilities.</p>
<p>Fill in the following information:</p>
<ul>
<li>
<p><strong>(Required) Contact</strong>: You can enter one of the following to contact you about security issues:</p>
<ul>
<li>An email address: The email address must start with <code>mailto:</code> (for example, <code>mailto:help@example.com</code>).</li>
<li>A phone number: The phone number must start with <code>tel:</code> (for example, <code>tel:+1 1234567890</code>).</li>
<li>A URL link: The URL link must start with <code>https://</code> (for example, <code>https://example.com</code>).</li>
</ul>
<p>Select <strong>Add more</strong> to add multiple contacts.</p>
</li>
<li>
<p><strong>(Required) Expires at</strong>: Enter the expiration date and time of the <code>security.txt</code> file.</p>
</li>
<li>
<p><strong>Encryption</strong>: A link to a key which security researchers can use to communicate with you.</p>
</li>
<li>
<p><strong>Acknowledgements</strong>: A link to your acknowledgements page.</p>
</li>
<li>
<p><strong>Canonical</strong>: Links to your <code>security.txt</code> file.</p>
</li>
<li>
<p><strong>Hiring</strong>: A link to your security-related job openings.</p>
</li>
<li>
<p><strong>Policy</strong>: A link to a policy describing what security researchers should do when searching for or reporting security issues.</p>
</li>
<li>
<p><strong>Preferred languages</strong>: A list of language codes that your security team speaks.</p>
</li>
</ul>
<p>Once you have entered the necessary information, select <strong>Save</strong>.</p>
<p>To edit your security.txt file:</p>
<ol>
<li>Go to <strong>Security</strong> &gt; <strong>Settings</strong> and filter by <strong>Web application exploits</strong>.</li>
<li>Under <strong>Security.txt</strong> &gt; <strong>Configurations</strong>, select the edit icon.</li>
</ol>
<p>To download your security.txt file:</p>
<ol>
<li>Go to <strong>Security</strong> &gt; <strong>Settings</strong> and filter by <strong>Web application exploits</strong>.</li>
<li>Under <strong>Security.txt</strong> &gt; <strong>Configurations</strong>, select the download icon.</li>
</ol>
<p>To delete your security.txt file:</p>
<ol>
<li>Select <strong>Security</strong> &gt; <strong>Settings</strong> and filter by <strong>Web application exploits</strong>.</li>
<li>Under <strong>Security.txt</strong> &gt; <strong>Configurations</strong>, select the edit icon.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
