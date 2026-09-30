---
cp9:
  canonical: https://developers.cloudflare.com/registrar/get-started/register-domain/
  description: Register a new domain with Cloudflare.
  full_title: Register a new domain · Cloudflare Registrar docs
  head_html: <title>Register a new domain · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Register a new domain with Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/registrar/get-started/register-domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/get-started/register-domain/index.md"><meta property="og:title" content="Register a new domain · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Register a new domain with Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/registrar/get-started/register-domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/get-started/register-domain/#page","headline":"Register a new domain \u00b7 Cloudflare Registrar docs","description":"Register a new domain with Cloudflare.","url":"https://developers.cloudflare.com/registrar/get-started/register-domain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/get-started/register-domain/
  schema: 1
---
<h2 id="prerequisites-and-restrictions">Prerequisites and restrictions</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-nameservers">Cloudflare nameservers</h3>
@markup("md", "content/.markup/bodies/12754.md")
</aside>
<ul>
<li>Cloudflare Registrar does not currently support internationalized domain names (IDNs), also known as Unicode.</li>
<li>You must have a <a href="/fundamentals/user-profiles/verify-email-address/">verified account email address</a>, to transfer or register domains.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12753.md")
</aside>
<h2 id="how-to-register-a-new-domain">How to register a new domain</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12752.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Register domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the search box, enter the domain name you wish to register, and select <strong>Search</strong>. You may also enter one or more keywords. The search results will contain a list of suggested domains. If the domain you entered does not appear in the list, this means it is not available for registration.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/12751.md")
</aside>
<ol start="3">
<li>
<p>Select <strong>Purchase</strong> on the domain you wish to register. In rare instances, a domain that is not available for registration may appear in the search results. After selecting <strong>Purchase</strong>, a definitive availability check will be performed to confirm that the domain is actually available for registration.</p>
</li>
<li>
<p>Select the term (number of years) you wish to register the domain from the <strong>Payment option</strong> drop-down menu. Most top-level domains (TLDs) can be registered for a maximum of ten years. Some TLDs may have different term limits and these will be reflected in the drop-down options.</p>
<p>The expiration date and price will update automatically based on the term selected. The <strong>Renew On</strong> date is the date that the system will attempt to auto-renew the domain. All registrations have Auto-renew turned on by default. However, you may <a href="/registrar/account-options/renew-domains/">disable this option</a> at any time.</p>
</li>
<li>
<p>Enter the contact details for the domain. These details will be used to create all of the required contacts (Registrant, Admin, Technical, and Billing), and may be updated after registration is completed. Refer to <a href="#contact-requirements">Contact requirements</a> to learn the specific requirements for each contact field.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12750.md")
</aside>
<ol start="6">
<li>
<p>In <strong>Payment</strong>, select which type of payment you want to use. If you already have a billing profile, Cloudflare uses this information to automatically fill the form. If there is no billing profile, you need to enter your payment information.</p>
</li>
<li>
<p>Review the terms and conditions, including the Domain Registration Agreement, Self-serve Subscription Agreement, and the Privacy Policy.</p>
</li>
<li>
<p>Select <strong>Complete purchase</strong> to continue. By selecting <strong>Complete purchase</strong>, you acknowledge that you are accepting the terms of the agreements.</p>
</li>
</ol>
<p>The registration process may take up to 30 seconds to complete. Once the registration is complete, the browser will navigate to the domain management page where you may update the contacts, change the auto-renew settings, and add additional years to the term. You will also receive a confirmation email regarding your new domain registration.</p>
<h2 id="contact-requirements">Contact requirements</h2>
<p>At this time, you can only use ASCII characters for contact data. If the default contact has non-ASCII characters, you will need to update the domain contact details before proceeding. Cloudflare recommends that you update your default contact information to include ASCII characters only.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Required?</th>
<th>Restrictions</th>
</tr>
</thead>
<tbody>
<tr>
<td>First Name</td>
<td>Yes</td>
<td>Minimum of two letters.</td>
</tr>
<tr>
<td>Last Name</td>
<td>Yes</td>
<td>Minimum of two letters.</td>
</tr>
<tr>
<td>Email</td>
<td>Yes</td>
<td>Must be a properly formatted email address.</td>
</tr>
<tr>
<td>Organization</td>
<td>No</td>
<td>Optional for most TLDs. In some cases, the Organization field may be populated by default with data from First and Last names.</td>
</tr>
<tr>
<td>Phone number</td>
<td>Yes</td>
<td>Must select a valid country code from the drop-down options. Only numbers will be accepted in the phone number field.</td>
</tr>
<tr>
<td>Ext</td>
<td>No</td>
<td>Only numbers may be entered.</td>
</tr>
<tr>
<td>Address 1</td>
<td>Yes</td>
<td>May not be all numeric.</td>
</tr>
<tr>
<td>Address 2</td>
<td>No</td>
<td>-</td>
</tr>
<tr>
<td>City</td>
<td>Yes</td>
<td>-</td>
</tr>
<tr>
<td>State</td>
<td>Yes</td>
<td>-</td>
</tr>
<tr>
<td>Country</td>
<td>Yes</td>
<td>You must select one from the drop-down options.</td>
</tr>
<tr>
<td>Postal Code</td>
<td>Yes</td>
<td>Must be a properly formatted postal code.</td>
</tr>
</tbody>
</table>
<p>When you register a domain with Cloudflare, your personal information is redacted when permitted by the registry. Refer to <a href="/registrar/account-options/whois-redaction/">WHOIS redaction</a> for more information.</p>
<h2 id="next-steps">Next steps</h2>
<p>To improve the security of your domain, enable <a href="/registrar/get-started/enable-dnssec/">Domain Name System Security Extensions</a> to create a secure layer with a cryptographic signature.</p>
