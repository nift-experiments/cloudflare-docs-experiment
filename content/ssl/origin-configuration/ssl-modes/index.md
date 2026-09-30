---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/
  description: Encryption modes allow you to control how Cloudflare connects to your origin web server and how certificates presented by your origin are validated.
  full_title: Encryption modes · Cloudflare SSL/TLS docs
  head_html: <title>Encryption modes · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Encryption modes allow you to control how Cloudflare connects to your origin web server and how certificates presented by your origin are validated."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/index.md"><meta property="og:title" content="Encryption modes · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Encryption modes allow you to control how Cloudflare connects to your origin web server and how certificates presented by your origin are validated."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/#page","headline":"Encryption modes \u00b7 Cloudflare SSL/TLS docs","description":"Encryption modes allow you to control how Cloudflare connects to your origin web server and how certificates presented by your origin are validated.","url":"https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/ssl-modes/
  schema: 1
---
<p>Your zone's <strong>SSL/TLS Encryption Mode</strong> controls how Cloudflare manages two connections: one between your visitors and Cloudflare, and the other between Cloudflare and your origin server.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: SSL/TLS Encryption mode&#10;    A[Visitor] &lt;--Connection 1--&gt; B((Cloudflare))&lt;--Connection 2--&gt; C[(Origin server)]&#10;</code></pre>
<br />
<p>If possible, Cloudflare strongly recommends using <a href="/ssl/origin-configuration/ssl-modes/full/"><strong>Full</strong></a> or <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (strict)</strong></a> modes to prevent malicious connections to your origin.</p>
<p>For more details on how encryption modes fit into the bigger picture of Cloudflare SSL/TLS protection, refer to <a href="/ssl/concepts/#ssltls-certificate">Concepts</a>.</p>
<h2 id="available-encryption-modes">Available encryption modes</h2>
<p><a href="#automatic-ssltls-default">Automatic SSL/TLS</a> relies on the probes developed for the SSL/TLS Recommender to determine what encryption mode is the most secure and safest for a website to be set to. If there is a more secure option for your website (based on your origin certification or capabilities), Automatic SSL/TLS will find it and apply it for your domain. The other option, <a href="#custom-ssltls">Custom SSL/TLS</a>, will work exactly like the setting the encryption mode does today.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14255.md")
</aside>
<p>To understand how the various encryption modes affect your cache, refer to the section on <a href="/cache/how-to/cache-keys/#impact-of-ssl-settings-on-cache-behavior">Impact of SSL setting on cache behavior</a>.</p>
<h3 id="automatic-ssl-tls-default">Automatic SSL/TLS (default)</h3>
<p>Automatic SSL/TLS leverages advanced methods developed by the SSL/TLS Recommender to select the most secure encryption mode for your website. The Recommender crawls your site using the Cloudflare-SSLDetector user agent, recognized as a trusted bot by Cloudflare, and bypasses <code>robots.txt</code> rules (except those that specifically target it) to ensure accuracy. It downloads content from your origin server over both HTTP and HTTPS, then applies a content similarity algorithm to assess consistency. By understanding your current SSL/TLS encryption mode and evaluating your origin's certification and capabilities, the Recommender can automatically adjust settings to maintain the highest security for your domain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14254.md")
</aside>
<p>Automatic upgrades are applied gradually. Automatic SSL/TLS begins to upgrade the domain by starting with just 1% of its traffic. If no issues are found, the new SSL/TLS encryption mode is applied to traffic in 10% increments until 100% of traffic uses the recommended mode.  If origin connectivity fails during this process, Cloudflare aborts the upgrade, immediately rolls traffic back to the previous mode, and logs the failure. Once 100% of traffic has been successfully upgraded with no TLS-related errors, the domain's SSL/TLS setting is permanently updated.</p>
<p>Flexible → Full/Strict transitions are handled with extra caution since the origin scheme change (HTTP → HTTPS) alters cache keys. In this case, the ramp-up may proceed more slowly to allow cache warm-up before resuming standard increments.</p>
<h4 id="additional-details">Additional details</h4>
<ul>
<li>
<p><strong>Scan frequency</strong>: Automatic scans currently occur approximately once per month, though they may happen more frequently in some cases (for example, configuration changes or upgrades). Scans stop when:</p>
<ul>
<li>The site is already using the most secure mode (for example, <strong>Full (strict)</strong>), or</li>
<li>You switch from auto mode to <strong>Custom SSL/TLS</strong>.</li>
</ul>
</li>
<li>
<p><strong>Error checking before upgrades</strong>: To prevent disruptions, Cloudflare checks for <code>5XX</code> errors (like <code>502</code> or <code>503</code>) and evaluates whether the HTTP and HTTPS content is consistent before upgrading a zone's encryption mode.</p>
</li>
<li>
<p><strong>Upgrade notifications</strong>: Cloudflare sends weekly digest emails listing which zones have been upgraded. These emails are currently sent to Super Admins only.</p>
</li>
</ul>
<h4 id="opt-out-single-zone">Opt out single zone</h4>
<p>If you want to opt a zone out via the API, you can make this API call on or before the grace period expiration date.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/{setting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;value&quot;: &quot;custom&quot;&#10;}&#x27;</code></pre>
<h4 id="opt-out-multiple-zones">Opt out multiple zones</h4>
<p>If you wanted to opt out multiple zones:</p>
<ol>
<li>Create an API token with the following permissions:
<ul>
<li><code>Zone - Zone - Read</code></li>
<li><code>Zone - Zone Settings - Read</code></li>
<li><code>Zone - Zone Settings - Edit</code></li>
</ul>
</li>
<li>Make a <a href="/api/resources/zones/methods/list/"><code>GET</code> request</a> to get a list of zones (you can filter this list by <code>account.id</code>).</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones?account.id=&lt;ACCOUNT_ID&gt;&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer &lt;CF_API_TOKEN&gt;&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27;&#10;</code></pre>
<ol start="3">
<li>Create a list of zone IDs you want to opt-out with each zone ID on a separate line (newline separate), stored in a file such as <code>zones.txt</code>.</li>
<li>Create a bash script for <code>opt-out-multiple-zones.sh</code> and add the following. Add <code>zones.txt</code> to the same directory or update the path accordingly.</li>
</ol>
<pre tabindex="0"><code class="language-bash">for zoneID in $(cat zone.txt); do&#10;  printf &quot;Opting out ${zoneID}:\n&quot;&#10;&#10;  curl --request PATCH \&#10;		&#45;-url https://api.cloudflare.com/client/v4/zones/$zoneID/settings/ssl_automatic_mode \&#10;		&#45;-header &#x27;Authorization: Bearer &lt;CF_API_TOKEN&gt;&#x27; \&#10;		&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;		&#45;-data &#x27;{&quot;value&quot;:&quot;custom&quot;}&#x27;&#10;&#10;  printf &quot;\n\n&quot;&#10;done&#10;</code></pre>
<ol start="5">
<li>Open your command line and run:</li>
</ol>
<pre tabindex="0"><code class="language-bash">bash opt-out-multiple-zones.sh&#10;</code></pre>
<h3 id="custom-ssl-tls">Custom SSL/TLS</h3>
<p>To use Custom SSL/TLS, select the custom option (if you prefer to manually set the encryption mode instead of using <a href="#automatic-ssltls-default">Automatic SSL/TLS</a>):</p>
<ul class="directory-listing"><li><a href="/ssl/origin-configuration/ssl-modes/off/">Off (no encryption)</a><p>No encryption is used for traffic between visitors and Cloudflare or between Cloudflare and origins. Everything is cleartext HTTP.</p></li><li><a href="/ssl/origin-configuration/ssl-modes/flexible/">Flexible</a><p>Traffic from visitors to Cloudflare can be encrypted via HTTPS, but traffic from Cloudflare to the origin server is not. This mode is common for origins that do not support TLS, though upgrading the origin configuration is recommended whenever possible.</p></li><li><a href="/ssl/origin-configuration/ssl-modes/full/">Full</a><p>Cloudflare matches the visitor request protocol when connecting to the origin. If the visitor uses HTTP, Cloudflare connects to the origin via HTTP; if HTTPS, Cloudflare uses HTTPS without validating the origin’s certificate. This mode is common for origins that use self-signed or otherwise invalid certificates.</p></li><li><a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict)</a><p>Similar to Full Mode, but with added validation of the origin server’s certificate, which can be issued by a public CA like Let’s Encrypt or by Cloudflare Origin CA.</p></li><li><a href="/ssl/origin-configuration/ssl-modes/ssl-only-origin-pull/">Strict (SSL-Only Origin Pull)</a><p>Regardless of whether the visitor-to-Cloudflare connection uses HTTP or HTTPS, Cloudflare always connects to the origin over HTTPS with certificate validation.</p></li></ul>
<h2 id="update-your-encryption-mode">Update your encryption mode</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14258.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14253.md")
</aside>
