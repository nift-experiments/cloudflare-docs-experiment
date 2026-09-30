---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/
  description: Reference information for Isolation policies in Browser Isolation.
  full_title: Isolation policies · Cloudflare One docs
  head_html: <title>Isolation policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Isolation policies in Browser Isolation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/index.md"><meta property="og:title" content="Isolation policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Isolation policies in Browser Isolation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#page","headline":"Isolation policies \u00b7 Cloudflare One docs","description":"Reference information for Isolation policies in Browser Isolation.","url":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/remote-browser-isolation/isolation-policies/
  schema: 1
---
<p>With Browser Isolation, you can define policies to dynamically isolate websites based on identity, security threats, or content.</p>
<h2 id="isolate">Isolate</h2>
<p>When an HTTP policy applies the Isolate action, the user's web browser is transparently served an HTML compatible remote browser client. Isolation policies can be applied to requests that include <code>Accept: text/html*</code> (requests for web pages). This allows Browser Isolation policies to co-exist with API traffic.</p>
<p>The following example enables isolation for all web traffic:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>matches regex</td>
<td><code>.*</code></td>
<td>Isolate</td>
</tr>
</tbody>
</table>
<p>If instead you need to isolate specific pages, you can list the domains for which you would like to isolate traffic:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>In</td>
<td><code>example.com</code>, <code>example.net</code></td>
<td>Isolate</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="isolate-identity-providers-for-applications">Isolate identity providers for applications</h3>
@markup("md", "content/.markup/bodies/4451.md")
</aside>
<h2 id="do-not-isolate">Do Not Isolate</h2>
<p>You can choose to disable isolation for certain destinations or categories. The following configuration disables isolation for traffic directed to <code>example.com</code>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>In</td>
<td><code>example.com</code></td>
<td>Do Not Isolate</td>
</tr>
</tbody>
</table>
<h2 id="policy-settings">Policy settings</h2>
<p>When you isolate a website, you can also restrict what users do on that site. The following optional settings appear in the Gateway HTTP policy builder when you select the <em>Isolate</em> action. Configure these settings to <a href="https://blog.cloudflare.com/data-protection-browser/">prevent data loss</a> when users interact with untrusted websites in the remote browser — for example, to stop a user from copying confidential data out of an isolated internal application.</p>
<h3 id="copy-from-remote-to-client">Copy (from remote to client)</h3>
<pre tabindex="0"><code class="language-mermaid">    flowchart LR&#10;			subgraph remotebrowser[Remote browser]&#10;        siteA[&quot;Isolated&#10;				website&quot;]--Data--&gt;remoteclip[&quot;Remote&#10;				clipboard&quot;]&#10;      end&#10;			subgraph client[Client]&#10;        localclip[&quot;Local&#10;				clipboard&quot;]&#10;      end&#10;			remoteclip--&gt;localclip&#10;</code></pre>
<ul>
<li><em>Allow</em>: (Default) Users can copy content from an isolated website to their local clipboard.</li>
<li><em>Allow only within isolated browser</em>: Users can only copy content from an isolated website to the remote clipboard. Users cannot copy content out of the remote browser to the local clipboard. You can use this setting alongside <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#paste-from-client-to-remote"><strong>Paste (from client to remote)</strong>: <em>Allow only within isolated browser</em></a> to only allow copy-pasting between isolated websites.</li>
<li><em>Do not allow</em>: Prohibits users from copying content from an isolated website.</li>
</ul>
<h3 id="paste-from-client-to-remote">Paste (from client to remote)</h3>
<pre tabindex="0"><code class="language-mermaid">    flowchart LR&#10;			subgraph client[Client]&#10;        localclip[&quot;Local&#10;				clipboard&quot;]&#10;      end&#10;			subgraph remotebrowser[Remote browser]&#10;				remoteclip[&quot;Remote&#10;				clipboard&quot;]--&gt;siteA[&quot;Isolated&#10;				website&quot;]&#10;      end&#10;			localclip--Data--&gt;remoteclip&#10;</code></pre>
<ul>
<li><em>Allow</em>: (Default) Users can paste content from their local clipboard to an isolated website.</li>
<li><em>Allow only within isolated browser</em>: Users can only paste content from the remote clipboard to an isolated website. Users cannot paste content from their local clipboard to the remote browser. You can use this setting alongside <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#copy-from-remote-to-client"><strong>Copy (from remote to client)</strong>: <em>Allow only within isolated browser</em></a> to only allow copy-pasting between isolated websites.</li>
<li><em>Do not allow</em>: Prohibits users from pasting content into an isolated website.</li>
</ul>
<h3 id="file-downloads">File downloads</h3>
<ul>
<li><em>Allow</em>: (Default) User can download files from an isolated website to their local machine.</li>
<li><em>Do not allow</em>: Prohibits users from downloading files from an isolated website to their local machine.</li>
<li><em>View in remote browser</em>: Users can open and view files in an isolated environment.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4450.md")
</aside>
<h3 id="file-uploads">File uploads</h3>
<ul>
<li><em>Allow</em>: (Default) Users can upload files from their local machine into an isolated website.</li>
<li><em>Do not allow</em>: Prohibits users from uploading files from their local machine into an isolated website.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4449.md")
</aside>
<h3 id="keyboard">Keyboard</h3>
<ul>
<li><em>Allow</em>: (Default) Users can perform keyboard inputs into an isolated website.</li>
<li><em>Do not allow</em>: Prohibits users from performing keyboard inputs into an isolated website.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4448.md")
</aside>
<h3 id="printing">Printing</h3>
<ul>
<li><em>Allow</em>: (Default) Users can print isolated web pages to their local machine.</li>
<li><em>Do not allow</em>: Prohibits users from printing isolated web pages to their local machine.</li>
</ul>
<h2 id="custom-block-dialog">Custom block dialog <span class="nb-badge">Beta</span></h2>
<p>With custom block dialogs, you can host a custom block page when users are blocked from taking specific actions, like <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#copy-from-remote-to-client">copying</a>, <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#paste-from-client-to-remote">pasting</a>, <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#file-downloads">downloading</a>, <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#file-uploads">uploading</a>, <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#keyboard">performing keyboard inputs</a>, or <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#printing">printing</a>, within an isolated browser session.</p>
<p>Administrators can configure custom block dialogs to explain the reason for the block, and guide the users on how to resolve their issue using the provided query parameters:</p>
<ul>
<li><code>action</code>: copy, paste, download, upload, perform keyboard inputs, and print</li>
<li><code>cf_colo</code>: for example, <code>sea01</code></li>
<li><code>client_url</code>: for example, <code>https://example.com</code></li>
<li><code>policy_id</code>: 32-character id</li>
<li><code>rbi_debug_id</code>: 32-character id</li>
<li><code>user_id</code>: 32-character id</li>
</ul>
<p>Custom block dialogs are still in beta. Contact your account team to start using custom block dialogs.</p>
<h2 id="common-policies">Common policies</h2>
<h3 id="isolate-all-security-threats">Isolate all security threats</h3>
<p>Isolate security threats such as malware and phishing.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4454.md")
</div></div>
<h3 id="isolate-high-risk-content">Isolate high risk content</h3>
<p>Isolate high risk content categories such as newly registered domains.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4457.md")
</div></div>
<h3 id="isolate-news-and-media">Isolate news and media</h3>
<p>Isolate news and media sites, which are targets for malvertising attacks.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4460.md")
</div></div>
<h3 id="isolate-uncategorized-content">Isolate uncategorized content</h3>
<p>Isolate content that has not been categorized by <a href="/radar/">Cloudflare Radar</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4463.md")
</div></div>
<h3 id="isolate-chatgpt">Isolate ChatGPT</h3>
<p>Isolate the use of ChatGPT.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4466.md")
</div></div>
