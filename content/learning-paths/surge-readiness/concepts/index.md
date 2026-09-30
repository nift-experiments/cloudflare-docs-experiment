---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/surge-readiness/concepts/
  description: Prepare your site for traffic surges.
  full_title: Prerequisites · Cloudflare Learning Paths
  head_html: <title>Prerequisites · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Prepare your site for traffic surges."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/surge-readiness/concepts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/surge-readiness/concepts/index.md"><meta property="og:title" content="Prerequisites · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Prepare your site for traffic surges."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/surge-readiness/concepts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF,Cache / CDN,DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/surge-readiness/concepts/#page","headline":"Prerequisites \u00b7 Cloudflare Learning Paths","description":"Prepare your site for traffic surges.","url":"https://developers.cloudflare.com/learning-paths/surge-readiness/concepts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/surge-readiness/concepts/
  schema: 1
---
<p>Reach out to your account team at least 30 days prior to the expected traffic surge to schedule a Security Optimization walkthrough with your Customer Solution Engineer.</p>
<p>To learn more about our service offerings, refer to <a href="https://www.cloudflare.com/success-offerings/">Customer Success offerings</a>.</p>
<h2 id="register-your-users">Register your users</h2>
<p>For the security and protection of your account, be sure to register all account users.</p>
<ol>
<li>In the Cloudflare dashboard, go to the  <strong>Manage Account</strong> &gt; <strong>Members</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select more than one Super Administrator to ensure appropriate access when needed.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10277.md")
</aside>
<p>Failure to register account users can create issues with our ticketing system. Unverified users who contact support will be funneled to the self-serve queue rather than the Enterprise queue which can result in long wait times.</p>
<p>We strongly advise against credential-sharing which can jeopardize the trust and safety of your account.</p>
<h2 id="confirm-user-and-domain-administration">Confirm user and domain administration</h2>
<ul>
<li><strong>Multi-User:</strong> Provide role-based permissions to a group of users to better control the administration of your domains. Each user has their own role and limited API key.</li>
<li><strong>Enforce 2FA:</strong> Ensure your entire dashboard is secure by <a href="/fundamentals/user-profiles/2fa/">enforcing 2-factor authentication</a> for your organization.
<ul>
<li>To disable 2FA, submit a support ticket and allow 1-2 business days to validate your request.</li>
</ul>
</li>
<li><strong>Leverage API Access:</strong> Work easily with our system programmatically using our <a href="https://api.cloudflare.com">API</a>.</li>
</ul>
<h2 id="additional-items">Additional items</h2>
<ul>
<li>Check when your <a href="/ssl/edge-certificates/custom-certificates/renewing/">SSL Certificates expire (only custom and origin certificates)</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10276.md")
</aside>
- Review your Operational and Disaster recovery preparedness
    - Enable Load Balancing with smart cache strategies: Use [Cloudflare Load Balancing](/reference-architecture/architectures/load-balancing) to distribute traffic across multiple healthy origins, and increase cache-hit ratios by leveraging [custom cache rules](/cache/performance-review/cache-analytics) and [edge compute](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/) (e.g., Cloudflare Workers) to offload origin traffic during high-demand periods.
    - Configure failover pools and back up DNS with a playbook: Set up [Cloudflare Load Balancer failover pools](/reference-architecture/architectures/load-balancing) to automatically redirect traffic to healthy origins if one fails. Export DNS records for safekeeping and prepare a clear [incident response plan](https://www.cloudflare.com/learning/performance/preventing-downtime) that includes steps for re-routing or recovery.
- Review and update your current users' access
- Check your domain registry validity
