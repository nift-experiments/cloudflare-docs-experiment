---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/mtls/configure/
  description: Set up mTLS authentication rules to require client certificates for API hosts.
  full_title: Configure mTLS · Cloudflare API Shield docs
  head_html: <title>Configure mTLS · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up mTLS authentication rules to require client certificates for API hosts."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/mtls/configure/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/mtls/configure/index.md"><meta property="og:title" content="Configure mTLS · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up mTLS authentication rules to require client certificates for API hosts."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/mtls/configure/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="API Shield"><meta name="pcx_tags" content="mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/mtls/configure/#page","headline":"Configure mTLS \u00b7 Cloudflare API Shield docs","description":"Set up mTLS authentication rules to require client certificates for API hosts.","url":"https://developers.cloudflare.com/api-shield/security/mtls/configure/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS"]}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/mtls/configure/
  schema: 1
---
<p>When you specify API hosts in <a href="/api-shield/security/mtls/">mTLS authentication</a>, Cloudflare will block all requests that do not have a <a href="/ssl/client-certificates/">client certificate</a> for mTLS authentication.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can protect your API or web application with mTLS rules, you need to:</p>
<ul>
<li>Check that the certificate installed on your origin server matches the hostname of the client certificate, for example <code>api.example.com</code>. Origin server wildcard certificates such as <code>*.example.com</code> are not supported.</li>
<li><a href="/ssl/client-certificates/create-a-client-certificate/">Create a client certificate</a>.</li>
<li><a href="/ssl/client-certificates/configure-your-mobile-app-or-iot-device/">Configure your mobile app or IoT device</a> to use your Cloudflare-issued client certificate.</li>
<li><a href="/ssl/client-certificates/enable-mtls/">Enable mutual Transport Layer Security (mTLS) for a host</a> in your zone.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3276.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3275.md")
</aside>
<h2 id="create-an-mtls-rule-via-the-cloudflare-dashboard">Create an mTLS rule via the Cloudflare dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3277.md")
</div>
<p>Once you have deployed your mTLS rule, any requests without a <a href="/ssl/client-certificates/">valid client certificate</a> will be blocked.</p>
<h3 id="expression-builder">Expression Builder</h3>
<p>To review your mTLS rule in the Expression Builder, select the <strong>wrench icon</strong> associated with your rule.</p>
<p>In the <strong>Expression Preview</strong>, your mTLS rule includes a <a href="/ruleset-engine/rules-language/expressions/#compound-expressions">compound expression</a> formed from two <a href="/ruleset-engine/rules-language/expressions/#simple-expressions">simple expressions</a> joined by the <code>and</code> operator.</p>
<p>The first expression — <code>not cf.tls_client_auth.cert_verified</code> — returns <code>true</code> when a request to access your API or web application does not present a valid client certificate.</p>
<p>The second expression uses the <code>http.request.uri.path</code> field, combined with the <code>in</code> operator, to capture the URI paths your mTLS rule applies to.</p>
<p>Because the <a href="/ruleset-engine/rules-language/actions/">action</a> for your rule is <em>Block</em>, only requests that present a valid client certificate can access the specified hosts.</p>
<p>Cloudflare recommends also validating the issuer Subject Key Identifier (SKI) hash. Without this check, any valid client certificate is accepted regardless of which certificate authority (CA) issued it. Adding the SKI hash restricts access to certificates from a specific CA.</p>
<p>You can implement this by using an expression similar to the following:</p>
<pre tabindex="0"><code class="language-txt">not (cf.tls_client_auth.cert_verified and cf.tls_client_auth.cert_issuer_ski eq &quot;A5AC554235DBA6D963B9CDE0185CFAD6E3F55E9F&quot;)&#10;</code></pre>
<p>To obtain the issuer Subject Key Identifier (SKI) hash of a client certificate stored in the <code>mtls.crt</code> file, you can run the following OpenSSL command:</p>
<pre tabindex="0"><code class="language-sh">openssl x509 -noout -ext authorityKeyIdentifier -in mtls.crt | tail -n1 | tr -d &#x27;: &#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">A5AC554235DBA6D963B9CDE0185CFAD6E3F55E9F&#10;</code></pre>
<h3 id="check-for-revoked-certificates">Check for revoked certificates</h3>
<p>To check for <a href="/ssl/client-certificates/revoke-client-certificate/">revoked client certificates</a>, you can either add a new mTLS rule or add a new expression to the <a href="#expression-builder">default rule</a>. To check for revoked certificates, you must use the Expression Builder.</p>
<p>When a request includes a revoked certificate, the <code>cf.tls_client_auth.cert_revoked</code> field is set to <code>true</code>. If you combined this with the <a href="#expression-builder">default mTLS rule</a>, it would look similar to the following:</p>
<pre tabindex="0"><code class="language-sql">((not cf.tls_client_auth.cert_verified or cf.tls_client_auth.cert_revoked) and http.request.uri.path in {&quot;/admin&quot;})&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3274.md")
</aside>
