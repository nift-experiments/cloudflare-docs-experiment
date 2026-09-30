---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/redirects/
  description: Define URL redirects for your Cloudflare Pages site using a _redirects file.
  full_title: Redirects · Cloudflare Pages docs
  head_html: <title>Redirects · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Define URL redirects for your Cloudflare Pages site using a _redirects file."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/redirects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/redirects/index.md"><meta property="og:title" content="Redirects · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Define URL redirects for your Cloudflare Pages site using a _redirects file."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/redirects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/redirects/#page","headline":"Redirects \u00b7 Cloudflare Pages docs","description":"Define URL redirects for your Cloudflare Pages site using a redirects file.","url":"https://developers.cloudflare.com/pages/configuration/redirects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/redirects/
  schema: 1
---
<p>To apply custom redirects on Cloudflare Pages, declare your redirects in a plain text file called <code>_redirects</code> without a file extension, in the static asset directory of your project. This file will not itself be served as a static asset, but will instead be parsed by Cloudflare Pages and its rules will be applied to static asset responses.</p>
<p>If you are using a framework, you will often have a directory named <code>public/</code> or <code>static/</code>, and this usually contains deploy-ready assets, such as favicons, <code>robots.txt</code> files, and site manifests. These files get copied over to a final output directory during the build, so this is the perfect place to author your <code>_redirects</code> file. If you are not using a framework, the <code>_redirects</code> file can go directly into your <a href="/pages/configuration/build-configuration/">build output directory</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11060.md")
</aside>
<h2 id="structure">Structure</h2>
<h3 id="per-line">Per line</h3>
<p>Only one redirect can be defined per line and must follow this format, otherwise it will be ignored.</p>
<pre tabindex="0"><code class="language-txt">[source] [destination] [code?]&#10;</code></pre>
<ul>
<li>
<p><code>source</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>A file path.</li>
<li>Can include <a href="#splats">wildcards (<code>*</code>)</a> and <a href="#placeholders">placeholders</a>.</li>
<li>Because fragments are evaluated by your browser and not Cloudflare's network, any fragments in the source are not evaluated.</li>
</ul>
</li>
<li>
<p><code>destination</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>A file path or external link.</li>
<li>Can include fragments, query strings, <a href="#splats">splats</a>, and <a href="#placeholders">placeholders</a>.</li>
</ul>
</li>
<li>
<p><code>code</code> <span class="nb-type">number</span> <span class="nb-metainfo">(default: 302) optional</span></p>
<ul>
<li>Optional parameter</li>
</ul>
</li>
</ul>
<p>Lines starting with a <code>#</code> will be treated as comments.</p>
<h3 id="per-file">Per file</h3>
<p>A <code>_redirects</code> file is limited to 2,000 static redirects and 100 dynamic redirects, for a combined total of 2,100 redirects. Each redirect declaration has a 1,000-character limit.</p>
<p>In your <code>_redirects</code> file:</p>
<ul>
<li>The order of your redirects matter. If there are multiple redirects for the same <code>source</code> path, the top-most redirect is applied.</li>
<li>Static redirects should appear before dynamic redirects.</li>
<li>Redirects are always followed, regardless of whether or not an asset matches the incoming request.</li>
</ul>
<p>A complete example with multiple redirects may look like the following:</p>
<pre tabindex="0"><code class="language-txt">/home301 / 301&#10;/home302 / 302&#10;/querystrings /?query=string 301&#10;/twitch https://twitch.tv&#10;/trailing /trailing/ 301&#10;/notrailing/ /nottrailing 301&#10;/page/ /page2/#fragment 301&#10;/blog/* https://blog.my.domain/:splat&#10;/products/:code/:name /products?code=:code&amp;name=:name&#10;</code></pre>
<h2 id="advanced-redirects">Advanced redirects</h2>
<p>Cloudflare currently offers limited support for advanced redirects.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Support</th>
<th>Example</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Redirects (301, 302, 303, 307, 308)</td>
<td>✅</td>
<td><code>/home / 301</code></td>
<td>302 is used as the default status code.</td>
</tr>
<tr>
<td>Rewrites (other status codes)</td>
<td>❌</td>
<td><code>/blog/* /blog/404.html 404</code></td>
<td></td>
</tr>
<tr>
<td>Splats</td>
<td>✅</td>
<td><code>/blog/* /posts/:splat</code></td>
<td>Refer to <a href="#splats">Splats</a>.</td>
</tr>
<tr>
<td>Placeholders</td>
<td>✅</td>
<td><code>/blog/:year/:month/:date/:slug /news/:year/:month/:date/:slug</code></td>
<td>Refer to <a href="#placeholders">Placeholders</a>.</td>
</tr>
<tr>
<td>Query Parameters</td>
<td>❌</td>
<td><code>/shop id=:id /blog/:id 301</code></td>
<td></td>
</tr>
<tr>
<td>Proxying</td>
<td>✅</td>
<td><code>/blog/* /news/:splat 200</code></td>
<td>Refer to <a href="#proxying">Proxying</a>.</td>
</tr>
<tr>
<td>Domain-level redirects</td>
<td>❌</td>
<td><code>workers.example.com/* workers.example.com/blog/:splat 301</code></td>
<td></td>
</tr>
<tr>
<td>Redirect by country or language</td>
<td>❌</td>
<td><code>/ /us 302 Country=us</code></td>
<td></td>
</tr>
<tr>
<td>Redirect by cookie</td>
<td>❌</td>
<td><code>/\* /preview/:splat 302 Cookie=preview</code></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="redirects-and-header-matching">Redirects and header matching</h2>
<p>Redirects execute before headers, so in the case of a request matching rules in both files, the redirect will win out.</p>
<h3 id="splats">Splats</h3>
<p>On matching, a splat (asterisk, <code>*</code>) will greedily match all characters. You may only include a single splat in the URL.</p>
<p>The matched value can be used in the redirect location with <code>:splat</code>.</p>
<h3 id="placeholders">Placeholders</h3>
<p>A placeholder can be defined with <code>:placeholder_name</code>. A colon (<code>:</code>) followed by a letter indicates the start of a placeholder and the placeholder name that follows must be composed of alphanumeric characters and underscores (<code>:[A-Za-z]\w*</code>). Every named placeholder can only be referenced once. Placeholders match all characters apart from the delimiter, which when part of the host, is a period (<code>.</code>) or a forward-slash (<code>/</code>) and may only be a forward-slash (<code>/</code>) when part of the path.</p>
<p>Similarly, the matched value can be used in the redirect values with <code>:placeholder_name</code>.</p>
<pre tabindex="0"><code class="language-txt">/movies/:title /media/:title&#10;</code></pre>
<h3 id="proxying">Proxying</h3>
<p>Proxying will only support relative URLs on your site. You cannot proxy external domains.</p>
<p>Only the first redirect in your file will apply. For example, in the following example, a request to <code>/a</code> will render <code>/b</code>, and a request to <code>/b</code> will render <code>/c</code>, but <code>/a</code> will not render <code>/c</code>.</p>
<pre tabindex="0"><code>/a /b 200&#10;/b /c 200&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11059.md")
</aside>
<h2 id="surpass-redirects-limits">Surpass <code>_redirects</code> limits</h2>
<p>A <a href="/pages/platform/limits/#redirects"><code>_redirects</code></a> file has a maximum of 2,000 static redirects and 100 dynamic redirects, for a combined total of 2,100 redirects. Use <a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a> to handle redirects that surpasses the 2,100 redirect rules limit of <code>_redirects</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11058.md")
</aside>
<p>To use Bulk Redirects, refer to the <a href="/rules/url-forwarding/bulk-redirects/create-dashboard/">Bulk Redirects dashboard documentation</a> or the <a href="/rules/url-forwarding/bulk-redirects/create-api/">Bulk Redirects API documentation</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/rules/transform/">Transform Rules</a></li>
</ul>
