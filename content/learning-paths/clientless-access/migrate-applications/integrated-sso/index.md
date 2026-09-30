---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/clientless-access/migrate-applications/integrated-sso/
  description: Manage applications with existing SSO integrations.
  full_title: Applications with integrated SSO · Cloudflare Learning Paths
  head_html: <title>Applications with integrated SSO · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Manage applications with existing SSO integrations."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/clientless-access/migrate-applications/integrated-sso/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/clientless-access/migrate-applications/integrated-sso/index.md"><meta property="og:title" content="Applications with integrated SSO · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage applications with existing SSO integrations."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/clientless-access/migrate-applications/integrated-sso/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Access,Cloudflare Tunnel,Cloudflare One"><meta name="pcx_tags" content="SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/clientless-access/migrate-applications/integrated-sso/#page","headline":"Applications with integrated SSO \u00b7 Cloudflare Learning Paths","description":"Manage applications with existing SSO integrations.","url":"https://developers.cloudflare.com/learning-paths/clientless-access/migrate-applications/integrated-sso/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SSO"]}</script>
  markdown: true
  noindex: false
  route: /learning-paths/clientless-access/migrate-applications/integrated-sso/
  schema: 1
---
<p>Many organizations in the past few years have recognized the importance of source-of-truth identity and have directly integrated their SSO provider with their internal applications. The SSO provider is only aware of the internal domain on which the application exists (via the configured ACS URL), which means the user must be connected to the local network in order to access the application. This security architecture makes sense for a traditional network perimeter, but it presents challenges for Zero Trust adoption. In the clientless access model, the user's device has no concept of an internal corporate network, only the specific, scoped applications to which they have access. The problem is summarized in the following diagram:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Authorization flow with integrated SSO&#10;A(&quot;User goes to&#10;app.public.com&quot;)--&gt;B(&quot;Cloudflare Tunnel&#10;routes public hostname (app.public.com)&#10;to internal domain (app.internal.com)&quot;)--&gt;C(&quot;app.internal.com redirects&#10;to integrated SSO&quot;)--&gt;D(&quot;SSO ACS URL returns&#10;app.internal.com&quot;)--&gt;E(&quot;404 error&#10;Device cannot resolve&#10;app.internal.com&quot;)&#10;</code></pre>
<h2 id="potential-solutions">Potential solutions</h2>
<p>If your applications use integrated SSO, there are a number of different paths you can take to onboard your applications to Cloudflare Access.</p>
<table>
<thead>
<tr>
<th>Solution</th>
<th>Steps required</th>
<th>Pros</th>
<th>Cons</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#recommended-solution">Present applications exclusively on Cloudflare domains</a></td>
<td>Change SSO ACS URL to the Cloudflare Tunnel public hostname</td>
<td><li> Increased security posture </li> <li> No changes to application code</li> <li> No changes to internal DNS design </li></td>
<td>Hard cutover event when ACS URL changes from internal to external domain</td>
</tr>
<tr>
<td>Present applications on existing internal domains with identical external domains delegated to Cloudflare</td>
<td>Add domains to Cloudflare that match internal domains</td>
<td><li> No changes to SSO ACS URL </li> <li> No change for end users </li></td>
<td><li> Requires careful management of internal and external domains </li> <li> Requires changing internal DNS design </li></td>
</tr>
<tr>
<td><a href="/learning-paths/clientless-access/migrate-applications/consume-jwt/">Consume the Cloudflare JWT in internal applications</a></td>
<td><li> Remove integrated SSO </li> <li> Update application to accept the Cloudflare JWT for user authorization </li></td>
<td><li> Reduced authentication burden for end users </li> <li> No changes to internal DNS design </li> <li> Instantly secure applications without direct SSO integration </li></td>
<td><li> Requires changing application code </li> <li> Hard cutover event when application updates </li></td>
</tr>
<tr>
<td>Use Cloudflare as the direct SSO integration, which then calls your IdP of choice (Okta, OneLogin, etc.)</td>
<td>Swap existing SSO provider for <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS</a></td>
<td><li> Increased flexibility for changing IdPs </li> <li> Ability to use multiple IdPs simultaneously </li></td>
<td><li> Hard cutover event for IdP changes </li> <li> No SCIM provisioning for application </li></td>
</tr>
</tbody>
</table>
<h2 id="recommended-solution">Recommended solution</h2>
<p>If you are able to configure your SSO provider, we recommend presenting all internal web services exclusively on Cloudflare domains. This is the model that Cloudflare takes for web application access internally and the most common method of resolution for customers in this scenario.</p>
<p>With this approach, you do not need to make any changes to your existing DNS infrastructure. Cloudflare Tunnel in your network will manage the translation from external (Cloudflare public) DNS to internal DNS, which is how the system is designed to function. After you update the ACS URL in your SSO provider to the Cloudflare public hostname, the outcome will look like this:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Authorization flow with updated SSO ACS URL&#10;A(&quot;User goes to&#10;app.public.com&quot;)--&gt;B(&quot;Cloudflare Tunnel&#10;routes public hostname (app.public.com)&#10;to internal domain (app.internal.com)&quot;)--&gt;C(&quot;app.internal.com redirects&#10;to integrated SSO&quot;)--&gt;D(&quot;SSO ACS URL returns&#10;app.public.com&quot;)--&gt;E(&quot;Browser displays app.public.com&quot;)&#10;</code></pre>
<p>All users - whether in the office, remote, using or not using the VPN client - will always route through the Cloudflare Access authentication flow at <code>app.public.com</code> to access a private application. This provides a single control plane for policy application and security audits, and no additional user training is necessary.</p>
