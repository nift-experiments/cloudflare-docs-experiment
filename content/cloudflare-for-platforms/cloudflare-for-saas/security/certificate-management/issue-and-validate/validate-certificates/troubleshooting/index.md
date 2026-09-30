---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/
  description: Resolve certificate validation issues including high-risk domains and CA errors.
  full_title: Troubleshooting · Cloudflare for Platforms docs
  head_html: <title>Troubleshooting · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve certificate validation issues including high-risk domains and CA errors."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve certificate validation issues including high-risk domains and CA errors."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare for Platforms docs","description":"Resolve certificate validation issues including high-risk domains and CA errors.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/
  schema: 1
---
<h2 id="high-risk-domains">High-risk domains</h2>
<p>Cloudflare's CA partners occasionally flag a domain as &quot;high risk&quot; — typically only for domains that Google's Safe Browsing service has flagged for phishing or malware.</p>
<p>If a domain is flagged by the CA, you need to contact Support before validation can finish. The API call will return indicating the failure, along with a link to where the ticket can be filed.</p>
<hr />
<h2 id="certificate-authority-authorization-caa-records">Certificate Authority Authorization (CAA) records</h2>
<p>CAA is a DNS resource record type defined in <a href="https://datatracker.ietf.org/doc/html/rfc6844">RFC 6844</a> that allows a domain owner to indicate which CAs are allowed to issue certificates for them.</p>
<h3 id="for-saas-providers">For SaaS providers</h3>
<p>If your customer has CAA records set on their domain, they will either need to add the following or remove CAA entirely:</p>
<pre tabindex="0"><code class="language-txt">example.com. IN CAA 0 issue &quot;pki.goog&quot;&#10;example.com. IN CAA 0 issue &quot;letsencrypt.org&quot;&#10;example.com. IN CAA 0 issue &quot;ssl.com&quot;&#10;</code></pre>
<p>While it is possible for CAA records to be set on the subdomain your customer wishes to use with your service, it will usually be set on the domain apex. If they have CAA records on the subdomain, those will also have to be removed.</p>
<h3 id="for-saas-customers">For SaaS customers</h3>
<p>In some cases, the validation may be prevented because your hostname points to a CNAME target where CAA records are defined.</p>
<p>In this case you would need to either select a Certificate Authority whose CAA records are present at the target, or review the configuration with the service provider that owns the target.</p>
<hr />
<h2 id="time-outs">Time outs</h2>
<p>If a certificate issuance times out, the error message will indicate where the timeout occurred:</p>
<ul>
<li>Timed Out (Initializing)</li>
<li>Timed Out (Validation)</li>
<li>Timed Out (Issuance)</li>
<li>Timed Out (Deployment)</li>
<li>Timed Out (Deletion)</li>
</ul>
<p>To fix this error, send a <a href="/api/resources/custom_hostnames/methods/edit/">PATCH request</a> through the API or select <strong>Refresh</strong> for the specific custom hostname in the dashboard. If using the API, make sure that the <code>--data</code> field contains an <code>ssl</code> object with the same <code>method</code> and <code>type</code> as the original request.</p>
<p>If these return an error, delete and recreate the custom hostname.</p>
<hr />
<h2 id="conflicting-acme-challenge-txt-records">Conflicting <code>_acme-challenge</code> TXT records</h2>
<p>If certificate validation is stuck despite the correct CNAME or TXT records being in place, a conflicting <code>_acme-challenge</code> TXT record may be preventing the certificate authority from completing validation.</p>
<h3 id="how-to-diagnose">How to diagnose</h3>
<p>Check whether the delegation CNAME is in place at the <code>_acme-challenge</code> hostname:</p>
<pre tabindex="0"><code class="language-sh">dig _acme-challenge.example.com CNAME +short&#10;</code></pre>
<ul>
<li>If this returns <strong>nothing</strong>, the delegation CNAME is missing. Run a <code>TXT</code> query to check whether a hardcoded record is also present:</li>
</ul>
<pre tabindex="0"><code class="language-sh">dig _acme-challenge.example.com TXT +short&#10;</code></pre>
<p>If this returns a raw token string, a hardcoded <code>_acme-challenge</code> TXT record is blocking certificate issuance — remove it before adding the delegation CNAME.</p>
<ul>
<li>If this returns a <strong>CNAME target</strong> but certificate validation is still stuck, the conflict is likely a hardcoded <code>_acme-challenge</code> TXT record inside your customer's direct Cloudflare zone. Because resolvers follow the CNAME chain rather than exposing records at the source name, the only way to confirm this is to inspect the customer's zone directly: go to <strong>DNS</strong> &gt; <strong>Records</strong> in the Cloudflare dashboard for their zone and look for any <code>_acme-challenge</code> TXT entries.</li>
</ul>
<h3 id="common-causes-and-remediation">Common causes and remediation</h3>
<p><strong>Record from a prior Cloudflare certificate order</strong> — Cloudflare adds <code>_acme-challenge</code> TXT records during certificate issuance. Records from a previous or abandoned order may persist and are not always visible in the Cloudflare dashboard. <a href="/support/contacting-cloudflare-support/">Contact Cloudflare Support</a> to have them removed.</p>
<p><strong>Record in a direct Cloudflare zone</strong> — If your customer's domain is also present in a direct Cloudflare zone (for example, they proxy <code>example.com</code> through their own Cloudflare account), that zone may have an <code>_acme-challenge</code> TXT record from a Universal SSL or Advanced certificate order. When the certificate authority queries <code>_acme-challenge.example.com</code>, it resolves the record from the direct zone rather than following the delegated DCV CNAME.</p>
<p>To resolve this, ask your customer to remove the <code>_acme-challenge</code> TXT record from their zone's DNS settings in the Cloudflare dashboard, then <a href="#immediate-validation-checks">trigger an immediate validation check</a>.</p>
<hr />
<h2 id="immediate-validation-checks">Immediate validation checks</h2>
<p>You can send a <a href="/api/resources/custom_hostnames/methods/edit/">PATCH request</a> to request an immediate validation check on any certificate. The PATCH data should include the same <code>ssl</code> object as the original request.</p>
<hr />
