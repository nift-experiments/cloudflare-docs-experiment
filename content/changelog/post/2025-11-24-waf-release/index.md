---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2025-11-24 · Changelog
  head_html: <title>WAF Release - 2025-11-24 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2025-11-24 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/#page","headline":"WAF Release - 2025-11-24 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-24-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 24, 2025</time><h2 id="post-title">WAF Release - 2025-11-24</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in FortiWeb, linked to CVE-2025-64446, alongside new detection logic expanding protection against PHP Wrapper Injection techniques.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability enables an unauthenticated attacker to bypass access controls by abusing the <code>CGIINFO</code> header. The latest update strengthens detection logic to ensure a reliable identification of crafted requests attempting to exploit this flaw.</p>
<p><strong>Impact</strong></p>
<ul>
<li>FortiWeb (CVE-2025-64446): Exploitation allows a remote unauthenticated adversary to circumvent authentication mechanisms by sending a manipulated <code>CGIINFO</code> header to FortiWeb’s backend CGI handler. Successful exploitation grants unintended access to restricted administrative functionality, potentially enabling configuration tampering or system-level actions.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b957ace6e9844bf29244401c4e2e1a2e">4e2e1a2e</code>
</td>
<td>N/A</td>
<td>FortiWeb - Authentication Bypass via CGIINFO Header - CVE:CVE-2025-64446</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e3871391a93248fa98a78e03b6c44ed5">b6c44ed5</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - Body - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - Body" (ID:<code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e6b1b66e0e3b46969102baed900f4015">900f4015</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - URI - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - URI" (ID:<code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code>)</td>
</tr>
</tbody>
</table>
</div></article></div>
