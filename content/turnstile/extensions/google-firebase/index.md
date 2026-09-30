---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/extensions/google-firebase/
  description: Integrate Turnstile with Google Firebase for server-side validation.
  full_title: Implement Turnstile with Google Firebase · Cloudflare Turnstile docs
  head_html: <title>Implement Turnstile with Google Firebase · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Turnstile with Google Firebase for server-side validation."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/extensions/google-firebase/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/extensions/google-firebase/index.md"><meta property="og:title" content="Implement Turnstile with Google Firebase · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Turnstile with Google Firebase for server-side validation."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/extensions/google-firebase/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Google,Integration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/extensions/google-firebase/#page","headline":"Implement Turnstile with Google Firebase \u00b7 Cloudflare Turnstile docs","description":"Integrate Turnstile with Google Firebase for server-side validation.","url":"https://developers.cloudflare.com/turnstile/extensions/google-firebase/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Google","Integration"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/extensions/google-firebase/
  schema: 1
---
<p>Turnstile is <a href="https://extensions.dev/extensions/cloudflare/cloudflare-turnstile-app-check-provider">available as an extension</a> with <a href="https://firebase.google.com/">Google's Firebase</a> platform as an <a href="https://firebase.google.com/docs/app-check">App Check</a> provider. You can leverage Cloudflare Turnstile's bot detection and challenge capabilities to ensure that requests to your Firebase backend services are verified and only authentic human visitors can interact with your application.</p>
<p>Google Firebase is a comprehensive app development platform that provides a variety of tools and services to help developers build, improve, and grow their mobile and web applications.</p>
<p>Firebase App Check helps protect Firebase resources like Cloud Firestore, Realtime Database, Cloud Storage, and Functions from abuse, such as automated fraud attacks and denial of service (DoS) attacks, by ensuring that incoming requests are from legitimate visitors and trusted sources.</p>
<h2 id="1-set-up-a-google-firebase-project"><ol>
<li>Set up a Google Firebase project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15025.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15024.md")
</aside>
<h2 id="2-set-up-cloudflare-turnstile"><ol start="2">
<li>Set up Cloudflare Turnstile</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15026.md")
</div>
<h2 id="3-integrate-firebase-app-check-with-turnstile"><ol start="3">
<li>Integrate Firebase App Check with Turnstile</li>
</ol></h2>
<h3 id="3a-enable-app-check-in-firebase">3a. Enable App Check in Firebase</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15027.md")
</div>
<h3 id="3b-grant-access-to-the-cloudflare-extension">3b. Grant access to the Cloudflare extension</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15028.md")
</div>
<h3 id="3c-configure-firebase-in-your-app-with-turnstile">3c. Configure Firebase in your app with Turnstile</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15029.md")
</div>
<h3 id="3d-verify-the-app-check-token-in-your-web-application">3d. Verify the App Check token in your web application</h3>
<p>To verify the App Check token in your web application, refer to Firebase's <a href="https://firebase.google.com/docs/app-check/custom-resource-backend?hl=en#verification">Token Verification guide</a>.</p>
<pre tabindex="0"><code class="language-js">import express from &quot;express&quot;;&#10;import { initializeApp } from &quot;firebase-admin/app&quot;;&#10;import { getAppCheck } from &quot;firebase-admin/app-check&quot;;&#10;&#10;const expressApp = express();&#10;const firebaseApp = initializeApp();&#10;&#10;const appCheckVerification = async (req, res, next) =&gt; {&#10;    const appCheckToken = req.header(&quot;X-Firebase-AppCheck&quot;);&#10;&#10;    if (!appCheckToken) {&#10;        res.status(401);&#10;        return next(&quot;Unauthorized&quot;);&#10;    }&#10;&#10;    try {&#10;        const appCheckClaims = await getAppCheck().verifyToken(appCheckToken);&#10;&#10;        // If verifyToken() succeeds, continue with the next middleware function in the stack.&#10;        return next();&#10;    } catch (err) {&#10;        res.status(401);&#10;        return next(&quot;Unauthorized&quot;);&#10;    }&#10;}&#10;&#10;expressApp.get(&quot;/yourApiEndpoint&quot;, [appCheckVerification], (req, res) =&gt; {&#10;    // Handle request.&#10;});&#10;</code></pre>
