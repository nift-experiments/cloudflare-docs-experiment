---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/
  description: Learn how to transfer a domain between Cloudflare accounts, including requirements, DNS settings, and SSL/TLS certificate management for seamless migration.
  full_title: Move a domain between Cloudflare accounts · Cloudflare Fundamentals docs
  head_html: <title>Move a domain between Cloudflare accounts · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to transfer a domain between Cloudflare accounts, including requirements, DNS settings, and SSL/TLS certificate management for seamless migration."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/index.md"><meta property="og:title" content="Move a domain between Cloudflare accounts · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to transfer a domain between Cloudflare accounts, including requirements, DNS settings, and SSL/TLS certificate management for seamless migration."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/#page","headline":"Move a domain between Cloudflare accounts \u00b7 Cloudflare Fundamentals docs","description":"Learn how to transfer a domain between Cloudflare accounts, including requirements, DNS settings, and SSL/TLS certificate management for seamless migration.","url":"https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-domains/move-domain/
  schema: 1
---
<p>You will have to move or transfer domains from one Cloudflare account to another if you:</p>
<ul>
<li>Manage a multi-user organization and need to segment domain access by user.</li>
<li>Receive a <code>Cloudflare is already hosting under a different account</code> error.</li>
<li>Lose access to your email address or Cloudflare account (though you can also use the <a href="/fundamentals/user-profiles/2fa/#use-a-backup-code">backup codes</a> if you have two-factor authentication enabled).</li>
<li>Registered a Cloudflare account with a typo in your email.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8904.md")
</aside>
<h2 id="requirements">Requirements</h2>
<p>To transfer a domain from one Cloudflare account to another, you will need:</p>
<ul>
<li>Access to your domain registrar. If your domain is using Cloudflare Registrar, refer to <a href="/registrar/account-options/inter-account-transfer/">Transfer a Cloudflare Registrar domain registration between accounts</a>.</li>
<li>At least one Cloudflare account associated with the domain.</li>
</ul>
<h2 id="transfer-your-domain">Transfer your domain</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8903.md")
</aside>
<p>If you still have access to your previous Cloudflare account, you can copy over the Cloudflare account settings manually. You must reissue <a href="#issue-new-certificates">SSL/TLS certificates</a> and <a href="/dns/manage-dns-records/how-to/create-dns-records/">recreate and validate DNS records</a> when transferring domains between Cloudflare accounts.</p>
<p>If you lose access to the email address associated with your Cloudflare account and do not have backup codes, you will need to manually transfer your domain to a new Cloudflare account associated with a different email address.</p>
<p>The domain transfer process depends on your DNS settings. If Cloudflare is your authoritative DNS provider (that is, your domain nameservers point to Cloudflare), you must:</p>
<ol>
<li><a href="/fundamentals/account/create-account/">Create a new Cloudflare account</a> or log in to an existing Cloudflare account.</li>
<li><a href="/fundamentals/manage-domains/add-site/">Add the domain</a> to the account (as if you were adding it for the first time).</li>
<li>Log in to your domain registrar account and <a href="/dns/zone-setups/full-setup/setup/">update the nameservers</a> to the provided Cloudflare nameservers.</li>
<li>Finalize the nameserver update by selecting your domain in the dashboard &gt; <strong>Overview</strong> &gt; <strong>Re-check now</strong>.</li>
</ol>
<p>Once the Cloudflare network recognizes the nameserver change, the domain in the new account will be marked as <strong>Active</strong>. While the domain in the new account is <strong>Pending</strong>, it cannot proxy traffic through Cloudflare and the origin IP addresses will be returned until the domain is marked as <strong>Active</strong>.</p>
<p>In the old account, the domain will be marked as <strong>Moved Away</strong>. After seven days in <strong>Moved Away</strong> status, the domain will be marked as <strong>Deleted</strong>. After seven days in the <strong>Deleted</strong> status, the domain will be permanently removed.</p>
<p>For more information, refer to <a href="/dns/zone-setups/reference/domain-status/">Zone status</a>.</p>
<h2 id="issue-new-certificates">Issue new certificates</h2>
<p>SSL/TLS certificates associated with your previous Cloudflare account will not be transferred to your new account. If your site requires an SSL/TLS certificate prior to domain transfer, refer to <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#minimize-downtime">Minimize downtime</a>.</p>
<p>If you were using <a href="/ssl/edge-certificates/custom-certificates/">custom certificates</a>, you will need to delete them from the previous zone and upload them to the new zone. You can upload the certificates while the new zone is in <strong>Pending</strong> status - if you do so, once you upload the certificates, they will have a <a href="/ssl/reference/certificate-statuses/#custom-certificates"><strong>Holding Deployment</strong></a> status and will become active once the zone is active.</p>
<p>You can order an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a> prior to transferring your domain. ACM certificates will automatically deploy to active domains.</p>
