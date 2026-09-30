---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/isolate-application/
  description: Learn about isolate access applications in this guide.
  full_title: Isolate Access applications · Cloudflare Learning Paths
  head_html: <title>Isolate Access applications · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about isolate access applications in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/isolate-application/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/isolate-application/index.md"><meta property="og:title" content="Isolate Access applications · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about isolate access applications in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/isolate-application/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Access,Cloudflare Tunnel,Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/isolate-application/#page","headline":"Isolate Access applications \u00b7 Cloudflare Learning Paths","description":"Learn about isolate access applications in this guide.","url":"https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/isolate-application/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/clientless-access/advanced-workflows/isolate-application/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9687.md")
</aside>
<p><a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a> integrates with your web-delivered Access applications to protect sensitive applications from data loss. You can build Access policies that require certain users to access your application exclusively through Browser Isolation, while other users matching different policies continue to access the application directly. For example, you may wish to layer on additional security measures for third-party contractors or other users without a corporate device.</p>
<p>Cloudflare sends all isolated traffic through our Secure Web Gateway inspection engine, which allows you to apply <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a> such as:</p>
<ul>
<li>Restrict specific actions and HTTP request methods.</li>
<li>Inspect the request body to match against <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a> (DLP) profiles with as much specificity and control as if the user had deployed an endpoint agent.</li>
<li>Control users ability to cut and paste, upload and download files, or print while in an isolated session.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>Your browser must <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#allow-third-party-cookies-in-the-browser">allow third-party cookies</a> on the application domain.</p>
<h2 id="enable-browser-isolation">Enable Browser Isolation</h2>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</p>
</li>
<li>
<p>Turn on <strong>Allow users to open a remote browser without the device client</strong>.</p>
</li>
<li>
<p>Go to <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Choose a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Go to <strong>Policies</strong>.</p>
</li>
<li>
<p>Choose an <a href="/cloudflare-one/access-controls/policies/">Allow policy</a> and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Under <strong>Additional settings</strong>, turn on <strong>Isolate application</strong>.</p>
</li>
<li>
<p>Save the policy.</p>
</li>
</ol>
<p>Browser Isolation is now enabled for users who match this policy. After the user logs into Access, the application will launch in a remote browser. To confirm that the application is isolated, refer to <a href="/cloudflare-one/remote-browser-isolation/setup/#3-check-if-a-web-page-is-isolated">Check if a web page is isolated</a>.</p>
<p>You can optionally add another Allow policy for users on managed devices who do not require isolation.</p>
<h2 id="example-access-policies">Example Access policies</h2>
<p>In the following example, Policy 1 allows employees on corporate devices to access the application directly. Users who do not match Policy 1, such as employees and contractors on unmanaged devices, will load the application in an isolated browser.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Access policies for a private web application&#10;A[Full-time employee]--&gt;policy1--&gt;D&#10;B[Contractor]--&gt;policy2--&gt;E&#10;subgraph C[Access application]&#10;  policy1[&quot;Policy 1:&#10;  Allow employees&#10;  who pass device posture checks&quot;]&#10;  policy2[&quot;Policy 2:&#10;  Allow and isolate contractors&quot;]&#10;end&#10;D[Normal browsing]&#10;E[&quot;Isolated browsing&#10;with HTTP policies applied&quot;]&#10;</code></pre>
<p><strong>Policy 1: Allow employees who pass device posture checks</strong></p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9690.md")
</div></div>
<p><strong>Policy 2: Allow and isolate contractors</strong></p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9693.md")
</div></div>
<h2 id="example-http-policies">Example HTTP policies</h2>
<h3 id="disable-file-downloads-in-isolated-browser">Disable file downloads in isolated browser</h3>
<p>Prevents users on unmanaged devices from downloading any files from your private application.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9696.md")
</div></div>
<h3 id="block-file-downloads-of-sensitive-data">Block file downloads of sensitive data</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9686.md")
</aside>
<p>Block users on unmanaged devices from downloading files that contain credit card numbers. This logic requires two policies:</p>
<ul>
<li>
<p><strong>Policy 1: <a href="/learning-paths/clientless-access/advanced-workflows/isolate-application/#disable-file-downloads-in-isolated-browser">Disable file downloads in isolated browser</a></strong></p>
</li>
<li>
<p><strong>Policy 2: Block credit card numbers</strong></p>
</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9699.md")
</div></div>
