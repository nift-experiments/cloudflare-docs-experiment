---
cp9:
  canonical: https://developers.cloudflare.com/dns/reference/domain-connect/
  description: Learn how to onboard your templates to use Domain Connect with Cloudflare as DNS provider.
  full_title: Domain Connect · Cloudflare DNS docs
  head_html: <title>Domain Connect · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to onboard your templates to use Domain Connect with Cloudflare as DNS provider."><link rel="canonical" href="https://developers.cloudflare.com/dns/reference/domain-connect/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/reference/domain-connect/index.md"><meta property="og:title" content="Domain Connect · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to onboard your templates to use Domain Connect with Cloudflare as DNS provider."><meta property="og:url" content="https://developers.cloudflare.com/dns/reference/domain-connect/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/reference/domain-connect/#page","headline":"Domain Connect \u00b7 Cloudflare DNS docs","description":"Learn how to onboard your templates to use Domain Connect with Cloudflare as DNS provider.","url":"https://developers.cloudflare.com/dns/reference/domain-connect/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/reference/domain-connect/
  schema: 1
---
<p>If you are a service provider, consider this page for information on how Cloudflare supports <a href="https://www.domainconnect.org/">Domain Connect</a> and how you can onboard your template.</p>
<h2 id="what-is-domain-connect">What is Domain Connect</h2>
<p>Domain Connect is an open standard that allows service providers - such as email or web hosting platforms - to make it easier for their end users to configure functionality, without having to manually edit DNS records.</p>
<p>This is achieved with templates that close the gap between necessary configurations (required by the service provider) and necessary DNS records changes (that must happen at the authoritative DNS provider).</p>
<p>In practice, this means that when a user that owns <code>example.com</code> and has Cloudflare as their authoritative DNS wants to use your service, instead of having to manually update their DNS records, they will only have to authenticate themselves and the necessary changes will be applied automatically.</p>
<h2 id="setup">Setup</h2>
<h3 id="before-you-begin">Before you begin</h3>
<ul>
<li>Note that Cloudflare only supports the <a href="https://www.domainconnect.org/getting-started/">Domain Connect synchronous flow</a>.</li>
<li>Domain Connect templates and tools are published on GitHub, so you must have a GitHub account and be familiar with <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks">GitHub forks and pull requests</a>.</li>
</ul>
<h3 id="1-add-templates-to-the-repository"><ol>
<li>Add templates to the repository</li>
</ol></h3>
<p>Domain Connect templates are published and maintained on a GitHub repository.</p>
<ol>
<li>Create a fork of the <a href="https://github.com/Domain-Connect/Templates">templates repository</a>.</li>
<li>Add your template. You can create a copy of one of the existing templates and edit it according to your needs.
<ul>
<li>Refer to the <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc">Domain Connect Specification</a> for details on the different available fields.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7568.md")
</aside>
   * If present, you must set the `syncBlock` field on your template to `false`. This means the template flow will be synchronous, which is the only option supported by Cloudflare.
   * You must also provide a synchronous public key domain (`syncPubKeyDomain` <sup><a href="#footnote-1">1</a></sup>). When your template is in use, synchronous calls will be digitally signed.
3. Make sure you follow the naming format defined by Domain Connect: `<providerId>.<serviceId>.json`.
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tip">Tip</h3>
@markup("md", "content/.markup/bodies/7567.md")
</aside>
<ol start="4">
<li>Submit a pull request to have your templates added to the repository.</li>
</ol>
<p>Once your pull request has been reviewed and merged, contact Cloudflare as specified below.</p>
<h3 id="2-contact-cloudflare-to-onboard-your-template"><ol start="2">
<li>Contact Cloudflare to onboard your template</li>
</ol></h3>
<p>When your template is onboarded, a graphical user interface flow will be available to your end users.</p>
<p>Send an email to <code>domain-connect@cloudflare.com</code>, including the following information:</p>
<ol>
<li>List of templates you want to onboard, with their corresponding GitHub hyperlinks.</li>
<li>Fully qualified domain names to query for the <code>syncPubKeyDomain</code><sup><a href="#footnote-1">1</a></sup> TXT records.</li>
<li>A logo to be displayed as part of the Domain Connect flow. Preferably in <code>SVG</code> format.</li>
<li>The default <a href="/dns/proxy-status/">proxy status</a> you would like Cloudflare to set for <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records that are part of your templates. Proxying other record types is not supported.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7566.md")
</aside>
<ol start="5">
<li>
<p>(Optional) A Cloudflare <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> for you to test the flow.</p>
<p>If you have a <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc#dns-provider-discovery">DNS provider discovery</a> automation in place and will not list new DNS providers manually, Cloudflare can initially restrict your template to be exposed to the specified account only. Once you confirm everything is working as expected, Cloudflare will publish your template on the discovery endpoint, to be picked up by your automation.</p>
</li>
</ol>
<h2 id="properties-support">Properties support</h2>
<p>In the <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc">Domain Connect Specification</a> you will find the following properties:</p>
<ul>
<li>Properties that you can use with your <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc#apply-template">apply template URL</a>.</li>
<li>Properties for <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc#template-definition">defining the template itself</a>.</li>
<li>Properties for defining the individual <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc#template-record">DNS records</a>.</li>
</ul>
<p>While most of these are supported by Cloudflare, some are required and others are not supported.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="linter-tool">Linter tool</h3>
@markup("md", "content/.markup/bodies/7565.md")
</aside>
<h3 id="apply-template-url">Apply template URL</h3>
<p>For the full list, refer to the <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc">Domain Connect Specification</a>. Below are the details specific to Cloudflare.</p>
<ul>
<li><strong>Redirect URI</strong>: Domain Connect's documentation states that it must be scoped to the <code>syncRedirectDomain</code> from the template, or the request must be signed. Cloudflare requires the request to be signed and, as such, does not check if the <code>redirect_uri</code> is scoped to the <code>syncRedirectDomain</code>.</li>
<li><strong>State</strong>: Is not supported and will be ignored.</li>
<li><strong>Service Name</strong>: Is not supported and will be ignored.</li>
<li><strong>Signature</strong>: Required. It also must be the last query parameter.</li>
<li><strong>Key</strong>: Required. You must publish your public key and place it in a DNS TXT record on a domain specified in the template as <code>syncPubKeyDomain</code>. To allow for key rotation, the hostname of the TXT record must be appended as another variable on the query string of the form.</li>
</ul>
<h3 id="template-definition">Template definition</h3>
<p>For the full list, refer to the <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc">Domain Connect Specification</a>. Below are the details specific to Cloudflare.</p>
<ul>
<li><strong>Service Provider Name</strong>: Will be displayed on the user interface.</li>
<li><strong>Service Name</strong>: Will <strong>not</strong> be displayed on the user interface.</li>
<li><strong>Logo</strong>: If present, will be displayed on the user interface.</li>
<li><strong>Synchronous Block</strong>: Is not supported and will be ignored. Cloudflare only supports the synchronous flow.</li>
<li><strong>Shared</strong>: Is not supported and will be ignored.</li>
<li><strong>Shared Service Name</strong>: Is not supported and will be ignored.</li>
<li><strong>Synchronous Public Key Domain</strong>: Required. Cloudflare only supports the synchronous flow and always checks for signature.</li>
<li><strong>Synchronous Redirect Domains</strong>: Is not supported and will be ignored. Cloudflare looks at the <code>redirect_uri</code> provided in the signed apply template URL.</li>
<li><strong>Multiple Instance</strong>: Is not supported and will be ignored.</li>
<li><strong>Warn Phishing</strong>: Is not supported and will be ignored.</li>
<li><strong>Host Required</strong>: Is not supported and will be ignored.</li>
</ul>
<h3 id="dns-records">DNS records</h3>
<p>For the full list, refer to the <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc">Domain Connect Specification</a>. Below are the details specific to Cloudflare.</p>
<ul>
<li><strong>Essential</strong>: Is not supported and will be ignored.</li>
<li><strong>TXT Conflict Matching Mode</strong>: Is not supported and will be ignored.</li>
<li><strong>TXT Conflict Matching Prefix</strong>: Is not supported and will be ignored.</li>
</ul>
<h4 id="custom-record-types">Custom record types</h4>
<p>The following record types are described in the <a href="https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc#extensionsexclusions">extensions/exclusions</a> section of the Domain Connect Specification. Below are the details specific to Cloudflare.</p>
<ul>
<li><strong>APEXCNAME</strong>: This custom record type is not supported and will cause the onboarding to fail. You can use a standard CNAME record instead, as Cloudflare automatically applies <a href="/dns/cname-flattening/">CNAME flattening</a> at the zone apex.</li>
<li><strong>REDIR301</strong> and <strong>REDIR302</strong>: When applied, these records are converted to zone-specific <a href="/rules/url-forwarding/bulk-redirects/">bulk redirect</a> rules. If a zone has existing bulk redirects before applying the template, they will be replaced.</li>
</ul>
<h2 id="template-updates">Template updates</h2>
<p>Since September, 2024, template updates are picked up by an automation.</p>
<p>The automation compares the template version number in Cloudflare with the authoritative source of the template on the Internet. This check runs multiple times a day. Although Cloudflare cannot guarantee when exactly each update will be picked up, the process is expected to take no longer than eight hours.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7564.md")
</aside>
<p>You can contact Cloudflare to opt out of the automatic updates. Once the automation is disabled, you can request template updates individually, by writing to <code>domain-connect@cloudflare.com</code>.</p>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>Send an email to <code>domain-connect@cloudflare.com</code> with the following information:</p>
<ol>
<li>
<p>Detailed description of what is wrong, including:</p>
<ul>
<li>Date and time when the issue occurred.</li>
<li>The <code>providerId</code> and <code>serviceId</code> of the template.</li>
<li>Description of what the request did.</li>
<li>Description of what you expected to happen.</li>
</ul>
</li>
<li>
<p>A <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file">HAR file</a> attachment containing the problematic update.</p>
</li>
</ol>
<h3 id="validation-errors">Validation errors</h3>
<p>The most common issues after template onboarding are validation errors, typically caused by <code>syncPubKeyDomain</code> TXT records.</p>
<p>You can fix these by republishing the signature, using tools such as the one provided by <a href="https://exampleservice.domainconnect.org/sig">Domain Connect</a>. Additionally, you can test signature validation with this <a href="https://github.com/kerolasa/dc-debug-pubkey">public key debug tool</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">A domain that can be queried for `TXT` records containing a public key to verify your digital signature. Refer to [digitally signed requests](https://github.com/Domain-Connect/spec/blob/master/Domain%20Connect%20Spec%20Draft.adoc#digitally-sign-requests) for details.</li></ol></section>
