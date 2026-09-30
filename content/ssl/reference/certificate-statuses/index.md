---
cp9:
  canonical: https://developers.cloudflare.com/ssl/reference/certificate-statuses/
  description: Understand certificate statuses in Cloudflare SSL/TLS, including stages like Initializing, Pending Validation, and Active. Monitor via dashboard or command line.
  full_title: Certificate statuses · Cloudflare SSL/TLS docs
  head_html: <title>Certificate statuses · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand certificate statuses in Cloudflare SSL/TLS, including stages like Initializing, Pending Validation, and Active. Monitor via dashboard or command line."><link rel="canonical" href="https://developers.cloudflare.com/ssl/reference/certificate-statuses/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/reference/certificate-statuses/index.md"><meta property="og:title" content="Certificate statuses · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand certificate statuses in Cloudflare SSL/TLS, including stages like Initializing, Pending Validation, and Active. Monitor via dashboard or command line."><meta property="og:url" content="https://developers.cloudflare.com/ssl/reference/certificate-statuses/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/reference/certificate-statuses/#page","headline":"Certificate statuses \u00b7 Cloudflare SSL/TLS docs","description":"Understand certificate statuses in Cloudflare SSL/TLS, including stages like Initializing, Pending Validation, and Active. Monitor via dashboard or command line.","url":"https://developers.cloudflare.com/ssl/reference/certificate-statuses/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/reference/certificate-statuses/
  schema: 1
---
<p>Certificates statuses show which stage of the issuance process each certificate is in.</p>
<h2 id="new-certificates">New certificates</h2>
<p>When you order a new certificate, either an <a href="/ssl/edge-certificates/">edge certificate</a> or a certificate used for a <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">custom hostname</a>, its status will move through various stages as it progresses to Cloudflare's global network:</p>
<ol>
<li>Initializing</li>
<li>Pending Validation</li>
<li>Pending Issuance</li>
<li>Pending Deployment</li>
<li>Active</li>
</ol>
<p>Once you issue a certificate, it should be in <strong>Pending Validation</strong>, but change to <strong>Active</strong> after the validation is completed. If you see any errors, you or your customer may need to take additional actions to validate the certificate.</p>
<p>If you deactivate a certificate, it will become a <strong>Deactivating</strong> and then an <strong>Inactive</strong> status.</p>
<h3 id="certificate-replacement">Certificate replacement</h3>
<p>When replacing a certificate, you may note a <strong>Pending Cleanup</strong> status. Old certificates are not deleted until the replacement has been successfully issued. This ensures TLS will not break for the hostname while the certificate is being replaced.</p>
<p>When the new certificate is successfully issued and activated, the status for the old certificate will transition from <strong>Pending Cleanup</strong>, and the certificate will be deleted.</p>
<h2 id="custom-certificates">Custom certificates</h2>
<p>If you are using a <a href="/ssl/edge-certificates/custom-certificates/">custom certificate</a> and your <a href="/dns/zone-setups/reference/domain-status/">zone status</a> is <strong>Pending</strong> or <strong>Moved</strong>, your certificate may have a status of <strong>Holding Deployment</strong>.</p>
<p>When your zone becomes active, your custom certificate will deploy automatically (also moving to an <strong>Active</strong> status).</p>
<p>If your zone is already active when you upload a custom certificate, you will not see this status.</p>
<h2 id="staging-certificates">Staging certificates</h2>
<p>When you create certificates in your <a href="/ssl/edge-certificates/staging-environment/">staging environment</a>, those staging certificates have their own set of statuses:</p>
<ul>
<li><strong>Staging deployment</strong>: Similar to <strong>Pending Deployment</strong>, but for staging certificates.</li>
<li><strong>Staging active</strong>: Similar to <strong>Active</strong>, but for staging certificates.</li>
<li><strong>Deactivating</strong>: Your staging certificate is in the process of becoming <strong>Inactive</strong>.</li>
<li><strong>Inactive</strong>: Your staging certificate is not at the edge, but you can deploy it if needed.</li>
</ul>
<h2 id="client-certificates">Client certificates</h2>
<p>When you use <a href="/ssl/client-certificates/">client certificates</a>, those client certificates have their own set of statuses:</p>
<ul>
<li><strong>Active</strong>: The client certificate is active.</li>
<li><strong>Revoked</strong>: The client certificate is revoked.</li>
<li><strong>Pending Reactivation</strong>: The client certificate was revoked, but it is being restored.</li>
<li><strong>Pending Revocation</strong>: The client certificate was active, but it is being revoked.</li>
</ul>
<hr />
<h2 id="monitor-certificate-statuses">Monitor certificate statuses</h2>
<h3 id="ssl-tls">SSL/TLS</h3>
<p>Monitor a certificate's status on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page or by using the <a href="/api/resources/ssl/subresources/certificate_packs/methods/get/">Get Certificate Pack endpoint</a>.</p>
<p>For more details on certificate validation, refer to <a href="/ssl/edge-certificates/changing-dcv-method/">Domain Control Validation</a>.</p>
<h3 id="ssl-for-saas">SSL for SaaS</h3>
<p>Monitor a certificate's status on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/custom-hostnames"><strong>Custom Hostnames</strong></a> page or by using the <a href="/api/resources/custom_hostnames/methods/get/">Custom Hostname Details endpoint</a>.</p>
<p>The Custom Hostname Details endpoint returns separate status fields for hostname activation and certificate status. Use the top-level <code>status</code> field to monitor hostname activation. Use the nested <code>ssl.status</code> field to monitor certificate issuance and deployment.</p>
<p>For production HTTPS, treat a custom hostname as ready when both status fields are <code>active</code> and the customer's DNS points to your Cloudflare for SaaS target.</p>
<p>For more details on certificate validation, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/">Issue and validate certificates</a>.</p>
<h3 id="via-the-command-line">Via the command line</h3>
<p>To view certificates, use <code>openssl</code> or your browser. The command below can be used in advance of your customer pointing the <code>app.example.com</code> hostname to the edge (<a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/">provided validation was completed</a>).</p>
<pre tabindex="0"><code class="language-sh">openssl s_client -servername app.example.com -connect $CNAME_TARGET:443 &lt;/dev/null 2&gt;/dev/null | openssl x509 -noout -text | grep app.example.com&#10;</code></pre>
