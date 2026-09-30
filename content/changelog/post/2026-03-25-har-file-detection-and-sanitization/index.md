---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/
  description: New updates and improvements at Cloudflare.
  full_title: Detect and sanitize HAR files · Changelog
  head_html: <title>Detect and sanitize HAR files · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Detect and sanitize HAR files · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/#page","headline":"Detect and sanitize HAR files \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-25-har-file-detection-and-sanitization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-25-har-file-detection-and-sanitization/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 25, 2026</time><h2 id="post-title">Detect and sanitize HAR files</h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>HTTP Archive (HAR) files are used by engineering and support teams to capture and share web traffic logs for troubleshooting. However, these files routinely contain highly sensitive data — including session cookies, authorization headers, and other credentials — that can pose a significant risk if uploaded to third-party services without being reviewed or cleaned first.</p>
<p>Gateway now includes a predefined DLP profile called <strong>Unsanitized HAR</strong> that detects HAR files in HTTP traffic. You can use this profile in a Gateway HTTP policy to either block HAR file uploads entirely or redirect users to a sanitization tool before allowing the upload to proceed.</p>
<h4 id="how-to-configure-a-har-file-policy">How to configure a HAR file policy</h4>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to  <strong>Zero Trust</strong> &gt;  <strong>Traffic policies</strong> &gt; <strong>Firewall Policies</strong> &gt; <strong>HTTP</strong> and create a new HTTP policy using the <strong>DLP Profile</strong> selector:</p>
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
<td>DLP Profile</td>
<td>in</td>
<td><em>Unsanitized HAR</em></td>
<td></td>
</tr>
</tbody>
</table>
<p>Then choose one of the following actions:</p>
<ul>
<li><strong>Block</strong>: Prevents the upload of any HAR file that has not been sanitized by Cloudflare's sanitizer. Use this for strict environments where HAR file sharing must be disallowed entirely.</li>
<li><strong>Block</strong> with <strong>Gateway Redirect</strong>: Intercepts the upload and redirects the user to <code>https://har-sanitizer.pages.dev/</code>, where they can sanitize the file. Once sanitized, the user can re-upload the clean file and proceed with their workflow.</li>
</ul>
<h4 id="sanitized-har-recognition">Sanitized HAR recognition</h4>
<p>HAR files processed by the Cloudflare HAR sanitizer receive a tamper-evident sanitized marker. DLP recognizes this marker and will not re-trigger the policy on a file that has already been sanitized and has not been modified since. If a previously sanitized file is edited, it will be treated as unsanitized and flagged again.</p>
<h4 id="visibility-in-gateway-logs">Visibility in Gateway logs</h4>
<p>Gateway logs will reflect whether a detected HAR file was classified as <strong>Unsanitized</strong> or <strong>Sanitized</strong>, giving your security team full visibility into HAR file activity across your organization.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>
</div></article></div>
