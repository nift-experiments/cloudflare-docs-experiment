---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/
  description: Test certificate changes in a staging environment before production.
  full_title: Staging environment · Cloudflare SSL/TLS docs
  head_html: <title>Staging environment · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Test certificate changes in a staging environment before production."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/index.md"><meta property="og:title" content="Staging environment · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Test certificate changes in a staging environment before production."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/#page","headline":"Staging environment \u00b7 Cloudflare SSL/TLS docs","description":"Test certificate changes in a staging environment before production.","url":"https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/staging-environment/
  schema: 1
---
<p>Use your certificate staging environment to test new custom (modern) certificates before pushing them to your production environment. This process helps you solve potential certificate problems <strong>before</strong> there's an incident, such as when:</p>
<ul>
<li>You make a mistake when uploading a new custom certificate.</li>
<li>You misunderstand the order of your certificates.</li>
<li>Clients have previously pinned your custom certificate, causing a TLS termination error.</li>
</ul>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes (open beta)</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="use-your-staging-environment">Use your staging environment</h2>
<h3 id="1-upload-certificate"><ol>
<li>Upload certificate</li>
</ol></h3>
<p>To upload custom (modern) certificates to your staging environment:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Staging Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Upload Custom Staging Certificate</strong>.</li>
<li>Upload your custom (modern) certificate (<a href="/ssl/edge-certificates/custom-certificates/uploading/">detailed instructions</a>).</li>
<li>Your certificate will appear in the dashboard with a status of <strong>Staging Deployment</strong>. If you refresh the page, its status should go to <strong>Staging Active</strong>.</li>
</ol>
<h3 id="2-test-certificate"><ol start="2">
<li>Test certificate</li>
</ol></h3>
<p>Test your custom (modern) certificate by sending <code>curl</code> requests to the IP addresses listed on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/staging-certificates"><strong>Staging Certificates</strong></a> page:</p>
<pre tabindex="0"><code class="language-txt">curl --resolve &lt;HOSTNAME&gt;:&lt;PORT&gt;:&lt;STAGING_IP&gt; https://&lt;HOSTNAME&gt; -iv&#10;</code></pre>
<p>You should confirm whether:</p>
<ul>
<li>TLS termination is successful.</li>
<li>The right certificate is being served at the edge.</li>
<li>Any clients are pinning the old certificate.</li>
</ul>
<h3 id="3-push-certificate-to-production"><ol start="3">
<li>Push certificate to production</li>
</ol></h3>
<p>Assuming there are no issues, push your custom (modern) certificate to your production environment:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Staging Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select a custom certificate.</li>
<li>Select <strong>Push to Production</strong>.</li>
</ol>
<p>If there were issues with your certificate, you can keep it in your staging environment or select <strong>Deactivate</strong> on the certificate itself.</p>
<h3 id="4-optional-push-certificate-back-to-staging"><ol start="4">
<li>(Optional) Push certificate back to staging</li>
</ol></h3>
<p>If you roll out a custom (modern) certificate to production and encounter issues, you can deactivate that certificate to delete the certificate from the edge and then push the certificate back to your staging environment for additional testing:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select a custom certificate.</li>
<li>Select <strong>Deactivate</strong>.</li>
<li>Select <strong>Push to Staging</strong>.</li>
</ol>
<hr />
<h2 id="limitations">Limitations</h2>
<h3 id="access">Access</h3>
<p>Currently, staging environments are only available to Enterprise customers participating in an open beta. To get access to the beta, contact your Account team.</p>
<h3 id="functionality">Functionality</h3>
<p>At the moment, staging environments have limited functionality:</p>
<ul>
<li>Only custom (modern) certificates</li>
<li>Only accessed via the dashboard</li>
</ul>
