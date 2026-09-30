---
cp9:
  canonical: https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/
  description: Learn how to troubleshoot various SSL/TLS errors with Cloudflare.
  full_title: General SSL errors · Cloudflare SSL/TLS docs
  head_html: <title>General SSL errors · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to troubleshoot various SSL/TLS errors with Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/index.md"><meta property="og:title" content="General SSL errors · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to troubleshoot various SSL/TLS errors with Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/#page","headline":"General SSL errors \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to troubleshoot various SSL/TLS errors with Cloudflare.","url":"https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/troubleshooting/general-ssl-errors/
  schema: 1
---
<h2 id="let-s-encrypt-chain-update">Let's Encrypt chain update</h2>
<h3 id="symptom">Symptom</h3>
<p>Starting September 9, 2024, visitors that try to connect to your website using older devices - for example, Android 7.0 and earlier - have access problems or reach security warnings.</p>
<h3 id="resolution">Resolution</h3>
<p>The fastest way to resolve this issue is to change your certificate to use <a href="/ssl/reference/certificate-authorities/#google-trust-services">Google Trust Services</a> as the certificate authority.</p>
<h2 id="outdated-browsers">Outdated browsers</h2>
<h3 id="symptom-1">Symptom</h3>
<p>Until Cloudflare provides an SSL certificate for your domain, the following errors may appear in various browsers for HTTPS traffic:</p>
<ul>
<li><strong>Firefox</strong>: <code>_ssl_error_bad_cert_domain</code> / <code>This connection is untrusted</code></li>
<li><strong>Chrome</strong>: <code>Your connection is not private</code></li>
<li><strong>Safari</strong>: <code>Safari can't verify the identity of the website</code></li>
<li><strong>Edge / Internet Explorer</strong>: <code>There is a problem with this website's security certificate</code></li>
</ul>
<h3 id="resolution-1">Resolution</h3>
<p>Even with a Cloudflare SSL certificate provisioned for your domain, older browsers display errors about untrusted SSL certificates because they do not <a href="https://en.wikipedia.org/wiki/Server_Name_Indication#Support">support the Server Name Indication (SNI) protocol</a> used by Cloudflare Universal SSL certificates.</p>
<p>To solve, <a href="https://caniuse.com/#feat=sni">determine if the browser supports SNI</a>. If not, upgrade your browser.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13958.md")
</aside>
<hr />
<h2 id="only-some-of-your-subdomains-return-ssl-errors">Only some of your subdomains return SSL errors</h2>
<h3 id="symptom-2">Symptom</h3>
<p><a href="/ssl/edge-certificates/universal-ssl">Cloudflare Universal SSL certificates</a> only cover the apex domain (<code>example.com</code>) and one level of subdomains (<code>blog.example.com</code>). If visitors to your domain observe errors accessing a second level of subdomains in their browser (such as <code>dev.www.example.com</code>) but not the first level of subdomains, resolve the issue using one of the following methods below.</p>
<h3 id="resolution-2">Resolution</h3>
<ul>
<li>Purchase an <a href="/ssl/edge-certificates/advanced-certificate-manager">advanced certificate</a> that covers <code>dev.www.example.com</code>.</li>
<li>Upload a <a href="/ssl/edge-certificates/custom-certificates">Custom SSL certificate</a> that covers <code>dev.www.example.com</code>.</li>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls">Total TLS</a>.</li>
<li>If you have a valid certificate for the second level subdomains at your origin web server, change the DNS record for <code>dev.www</code> to <a href="/dns/proxy-status/">DNS Only (grey cloud)</a>.</li>
</ul>
<hr />
<h2 id="your-cloudflare-universal-ssl-certificate-is-not-active">Your Cloudflare Universal SSL certificate is not active</h2>
<h3 id="symptom-3">Symptom</h3>
<p>All active Cloudflare domains are provided a <a href="/ssl/edge-certificates/universal-ssl">Universal SSL certificate</a>. If you observe SSL errors and do not have a certificate of <strong>Type</strong> <em>Universal</em> within the <strong>Edge Certificates</strong> tab of the Cloudflare <strong>SSL/TLS</strong> app for your domain, the Universal SSL certificate has not yet provisioned.</p>
<p>Our SSL vendors verify each SSL certificate request before Cloudflare can issue a certificate for a domain name. This process may take anywhere from 15 minutes to 24 hours. Our SSL certificate vendors sometimes flag a domain name for additional review.</p>
<h3 id="resolution-3">Resolution</h3>
<h4 id="no-universal-certificate">No Universal certificate</h4>
<p>If your Cloudflare SSL certificate is not issued within 24 hours of Cloudflare domain activation:</p>
<ul>
<li>If your origin web server has a valid SSL certificate, <a href="/fundamentals/manage-domains/pause-cloudflare/">temporarily pause Cloudflare</a>, and</li>
<li><a href="/support/contacting-cloudflare-support/">Contact Support</a> and provide a screenshot of the errors.</li>
</ul>
<p>Temporarily pausing Cloudflare will allow the HTTPS traffic to be served properly from your origin web server while the support team investigates the issue.</p>
<h4 id="full-dns-setup">Full DNS setup</h4>
<p>If your domain is on a <a href="/dns/zone-setups/full-setup/">full setup</a>, review your DNS records.</p>
<p>Cloudflare SSL/TLS certificates only apply for traffic <a href="/dns/proxy-status/">proxied through Cloudflare</a>. If SSL errors only occur for hostnames not proxied to Cloudflare, proxy those hostnames through Cloudflare.</p>
<h4 id="partial-dns-setup">Partial DNS setup</h4>
<p>If your domain is on a <span class="nb-glossary-tooltip" title="CNAME setup">CNAME setup (partial)</span>, confirm whether you have CAA DNS records enabled at your current hosting provider. If so, ensure you <a href="/ssl/edge-certificates/caa-records/">specify the Certificate Authorities that Cloudflare uses</a> to provision certificates for your domain.</p>
<hr />
<h2 id="ocsp-response-error">OCSP response error</h2>
<h3 id="symptom-4">Symptom</h3>
<p>Visitors to your site observe an OCSP response error.</p>
<h3 id="resolution-4">Resolution</h3>
<p>This error is either caused by the browser version or an issue requiring attention by one of Cloudflare’s SSL vendors. In order to properly diagnose, <a href="/support/contacting-cloudflare-support/">contact Support</a> with the following information provided by the visitor that observes the browser error:</p>
<ol>
<li>The output from <a href="https://aboutmybrowser.com/">https://aboutmybrowser.com/</a>  .</li>
<li>The output of <code>https://&lt;YOUR_DOMAIN&gt;/cdn-cgi/trace</code> from the visitor’s browser.</li>
</ol>
<hr />
<h2 id="incorrect-hsts-headers">Incorrect HSTS headers</h2>
<h3 id="symptom-5">Symptom</h3>
<p>The HSTS headers (<code>Strict-Transport-Security</code> and <code>X-Content-Type-Options</code>) in the response do not match the configuration settings defined in your <a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">HSTS settings</a>.</p>
<h3 id="resolution-5">Resolution</h3>
<p>You may have configured <a href="/rules/transform/response-header-modification">Response Header Transform Rules</a> that are overriding the HSTS header values defined in the <strong>SSL/TLS</strong> app.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Response Header Transform Rules</strong>, search for a rule setting the value of one of the HSTS headers (<code>Strict-Transport-Security</code> or <code>X-Content-Type-Options</code>).</li>
<li>Delete (or edit) the rule so that the HSTS configuration settings defined in the <strong>SSL/TLS</strong> app are applied.</li>
<li>Repeat this procedure for the other HSTS header.</li>
</ol>
<hr />
<h2 id="other-errors">Other errors</h2>
<h3 id="symptom-6">Symptom</h3>
<p>You are getting the error <code>NET::ERR_CERT_COMMON_NAME_INVALID</code> in your browser.</p>
<h3 id="resolution-6">Resolution</h3>
<ul>
<li>Make sure that you are using a browser that supports <a href="https://www.cloudflare.com/learning/ssl/what-is-sni/">SNI (Server Name Indication)</a>. Refer to <a href="/ssl/reference/browser-compatibility/">Browser compatibility</a> for more details.</li>
<li>Ensure that the hostname you are accessing is set to <a href="/dns/proxy-status/">proxied (orange cloud)</a> in the DNS tab of your Cloudflare Dashboard.</li>
<li>If the hostname you are accessing is a second level subdomain (such as <code>dev.www.example.com</code>), you'll need to either:
<ul>
<li>Purchase an <a href="/ssl/edge-certificates/advanced-certificate-manager">advanced certificate</a> that covers <code>dev.www.example.com</code>.</li>
<li>Upload a <a href="/ssl/edge-certificates/custom-certificates">Custom SSL certificate</a> that covers <code>dev.www.example.com</code>.</li>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls">Total TLS</a></li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13957.md")
</aside>
<hr />
<h2 id="kaspersky-antivirus">Kaspersky Antivirus</h2>
<p>To avoid SSL errors with the Cloudflare dashboard when using Kaspersky Antivirus, allow <code>dash.cloudflare.com</code> in Kaspersky.</p>
<hr />
<h2 id="certificate-approval-renewal-email">Certificate Approval renewal email</h2>
<h3 id="symptom-7">Symptom</h3>
<p>When clicking <code>Approve Certificate</code> on a Certificate Approval renewal email, you get the following error message:</p>
<p><code>An error occurred while attempting to validate your domain. Please try again later or contact support for assistance.</code></p>
<h3 id="resolution-7">Resolution</h3>
<p>Check the status of the certificate on the <a href="https://dash.cloudflare.com?to=/:account/:zone/ssl-tls">Cloudflare dashboard</a>. If the status is <code>Active</code>, you can disregard this email and the error message.</p>
