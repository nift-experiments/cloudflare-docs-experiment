---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/
  description: Deprecation notice and migration guide for SSL for SaaS Version 1.
  full_title: Deprecation notice for SSL for SaaS - Version 1 · Cloudflare for Platforms docs
  head_html: <title>Deprecation notice for SSL for SaaS - Version 1 · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Deprecation notice and migration guide for SSL for SaaS Version 1."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/index.md"><meta property="og:title" content="Deprecation notice for SSL for SaaS - Version 1 · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deprecation notice and migration guide for SSL for SaaS Version 1."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><meta name="pcx_tags" content="Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/#page","headline":"Deprecation notice for SSL for SaaS - Version 1 \u00b7 Cloudflare for Platforms docs","description":"Deprecation notice and migration guide for SSL for SaaS Version 1.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Migration"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/
  schema: 1
---
<p>The first version of SSL for SaaS will be deprecated on September 1, 2021.</p>
<h2 id="why-is-ssl-for-saas-changing">Why is SSL for SaaS changing?</h2>
<p>In SSL for SaaS v1, traffic for Custom Hostnames is proxied to the origin based on the IP addresses assigned to the zone with SSL for SaaS enabled. This IP-based routing introduces complexities that prevented customers from making changes with zero downtime.</p>
<p>SSL for SaaS v2 removes IP-based routing and its associated problems. Instead, traffic is proxied to the origin based on the custom hostname of the SaaS zone. This means that Custom Hostnames will now need to pass a <strong>hostname verification</strong> step after Custom Hostname creation and in addition to SSL certificate validation. This adds a layer of security from SSL for SaaS v1 by ensuring that only verified hostnames are proxied to your origin.</p>
<h2 id="what-action-is-needed">What action is needed?</h2>
<p>To ensure that your service is not disrupted, you need to perform an additional ownership check on every new Custom Hostname. There are three methods to verify ownership: TXT, HTTP, and CNAME. Use TXT and HTTP for pre-validation to validate the Custom Hostname before traffic is proxied by Cloudflare’s edge.</p>
<h3 id="recommended-validation-methods">Recommended validation methods</h3>
<p>Using a <a href="#dns-txt-record">TXT</a> or <a href="#http-token">HTTP</a> validation method helps you avoid downtime during your migration. If you choose to use <a href="#cname-validation">CNAME validation</a>, your domain might fall behind on its <a href="/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/">backoff schedule</a>.</p>
<h4 id="dns-txt-record">DNS TXT Record</h4>
<p>When creating a Custom Hostname with the TXT method through the <a href="/api/resources/custom_hostnames/methods/create/">API</a>, a TXT ownership_verification record is provided for your customer to add to their DNS for the ownership validation check. When the TXT record is added, the Custom Hostname will be marked as <strong>Active</strong> in the Cloudflare SSL/TLS app under the Custom Hostnames tab.</p>
<h4 id="http-token">HTTP Token</h4>
<p>When creating a Custom Hostname with the HTTP through the <a href="/api/resources/custom_hostnames/methods/create/">API</a>, an HTTP ownership_verification token is provided. HTTP verification is used mainly by organizations with a large deployed base of custom domains with HTTPS support. Serving the HTTP token from your origin web server allows hostname verification before proxying domain traffic through Cloudflare.</p>
<p>Cloudflare sends GET requests to the http_url using <code>User-Agent: Cloudflare Custom Hostname Verification</code>.</p>
<p>If you validated a hostname that is not proxying traffic through Cloudflare, the Custom Hostname will be marked as <strong>Active</strong> in the Cloudflare SSL/TLS app when the HTTP token is verified (under the <strong>Custom Hostnames</strong> tab).</p>
<p>If your hostname is already proxying traffic through Cloudflare, then HTTP validation is not enough by itself and the hostname will only go active when DNS-based validation is complete.</p>
<h3 id="other-validation-methods">Other validation methods</h3>
<p>Though you can use <a href="#cname-validation">CNAME validation</a>, we recommend you either use a <a href="#dns-txt-record">TXT</a> or <a href="#http-token">HTTP</a> validation method.</p>
<h4 id="cname-validation">CNAME Validation</h4>
<p>Custom Hostnames can also be validated once Cloudflare detects that the Custom Hostname is a CNAME record pointing to the fallback record configured for the SSL for SaaS domain. Though this is the simplest validation method, it increases the risk of errors. Since a CNAME record would also route traffic to Cloudflare’s edge, traffic may reach our edge before the Custom Hostname has completed validation or the SSL certificate has issued.</p>
<p>Once you have tested and added the hostname validation step to your Custom Hostname creation process, please contact your account team to schedule a date to migrate your SSL for SaaS v1 zones. Your account team will work with you to validate your existing Custom Hostnames without downtime.</p>
<h2 id="if-you-are-using-byoip-or-apex-proxying">If you are using BYOIP or Apex Proxying:</h2>
<p>Both BYOIP addresses and IP addresses configured for Apex Proxying allow for hostname validation to complete successfully by having either a BYOIP address or an Apex Proxy IP address as the target of a DNS A record for a custom hostname.</p>
<h2 id="what-is-available-in-the-new-version-of-ssl-for-saas">What is available in the new version of SSL for SaaS?</h2>
<p>SSL for SaaS v2 is functionally equivalent to SSL for SaaS v1, but removes the requirements to use specific anycast IP addresses at Cloudflare’s edge and Cloudflare’s Universal SSL product with the SSL for SaaS zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4092.md")
</aside>
<h2 id="what-happens-during-the-migration">What happens during the migration?</h2>
<p>Once the migration has been started for your zone(s), Cloudflare will require every Custom Hostname to pass a hostname verification check. Existing Custom Hostnames that are proxying to Cloudflare with a DNS CNAME record will automatically re-validate and migrate to the new version with no downtime. Any Custom Hostnames created after the start of the migration will need to pass the hostname validation check using one of the validation methods mentioned above.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4091.md")
</aside>
<h3 id="before-the-migration">Before the migration</h3>
<p>Before your migration, you should:</p>
<ol>
<li>To test validation methods, set up a test zone and ask your account team to enable SSL for SaaS v2.</li>
<li>Wait for your account team to run our pre-migration tool. This tool groups your hostnames into one of the following statuses:
<ul>
<li><code>test_pending</code>: In the process of being verified or was unable to be verified and re-queued for verification. A custom hostname will be re-queued 25 times before moving to the <code>test_failed</code> status.</li>
<li><code>test_active</code>: Passed CNAME verification</li>
<li><code>test_active_apex</code>: Passed Apex Proxy verification</li>
<li><code>test_blocked</code>: Hostname will be blocked during the migration because hostname belongs to a banned zone. Contact your account team to verify banned custom hostnames and proceed with the migration.</li>
<li><code>test_failed</code>: Failed hostname verification 25 times</li>
</ul>
</li>
<li>Review the results of our pre-migration tool (run by your account team) using one of the following methods:
<ul>
<li>Via the API: <code>https://api.cloudflare.com/client/v4/zones/{zone_tag}/custom_hostnames?hostname_status={status}</code></li>
<li>Via a CSV file (provided by your account team)</li>
<li>Via the Cloudflare dashboard:
<img src="/assets/upstream/images/cloudflare-for-platforms/ssl-migration-status.png" alt="Review SSL migration status in the dashboard" /></li>
</ul>
</li>
<li>Approve the migration. Your account team will work with you to schedule a migration window for each of your SSL for SaaS zones.</li>
</ol>
<h2 id="during-the-migration">During the migration</h2>
<p>After the migration has started and has had some time to progress, Cloudflare will generate a list of Custom Hostnames that failed to migrate and ask for your approval to complete the migration. When you give your approval, the migration will be complete, SSL for SaaS v1 will be disabled for the zone, and any Custom Hostname that has not completed hostname validation will no longer function.</p>
<p>The migration timeline depends on the number of Custom Hostnames. For example, if a zone has fewer than 10,000 Custom Hostnames, the list can be generated around an hour after beginning the migration. If a zone has millions of Custom Hostnames, it may take up to 24 hours to identify instances that failed to successfully migrate.</p>
<p>When your account team asks for approval to complete the migration, please respond in a timely manner. You will have <strong>two weeks</strong> to validate any remaining Custom Hostnames before they are systematically deleted.</p>
<h2 id="when-is-the-migration">When is the migration?</h2>
<p>The migration process starts on March 31, 2021 and will continue until final deprecation on September 1, 2021.</p>
<p>If you would like to begin the migration process before March 31, 2021, please contact your account team and they will work with you to expedite the process. Otherwise, your account team will reach out to you with a time for a migration window so that your zones are migrated before <strong>September 1, 2021</strong> end-of-life date.</p>
<h2 id="what-if-i-have-additional-questions">What if I have additional questions?</h2>
<p>If you have any questions, please contact your account team or <a href="mailto:saasv2@cloudflare.com">SaaSv2@cloudflare.com</a>.</p>
