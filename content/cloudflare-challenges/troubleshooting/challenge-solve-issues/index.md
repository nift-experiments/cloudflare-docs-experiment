---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/
  description: Fix challenge loops, unsupported browser errors, and other solve failures.
  full_title: Challenge solve issues · Cloudflare challenges docs
  head_html: <title>Challenge solve issues · Cloudflare challenges docs</title><meta name="generator" content="Nift"><meta name="description" content="Fix challenge loops, unsupported browser errors, and other solve failures."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/index.md"><meta property="og:title" content="Challenge solve issues · Cloudflare challenges docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fix challenge loops, unsupported browser errors, and other solve failures."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Challenges"><meta name="algolia_product_filter" content="Challenges"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Challenges"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/#page","headline":"Challenge solve issues \u00b7 Cloudflare challenges docs","description":"Fix challenge loops, unsupported browser errors, and other solve failures.","url":"https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-challenges/troubleshooting/challenge-solve-issues/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4025.md")
</aside>
<h2 id="challenge-loops">Challenge loops</h2>
<p>You may encounter a challenge loop where the challenge keeps reappearing without being solved. This is in very specific cases where we detect strong bot signals. If you are a legitimate human, you can follow the troubleshooting guide below to resolve the issue or submit a feedback report. Challenge loops can happen for several reasons:</p>
<ul>
<li><strong>Network issues</strong>: Poor or unstable network connections can prevent the challenge from being completed.</li>
<li><strong>Browser configuration</strong>: Some browser settings or extensions may block the scripts needed to execute the challenge.</li>
<li><strong>Unsupported browsers</strong>: Using a browser that is not supported by Turnstile.</li>
<li><strong>JavaScript disabled</strong>: Turnstile relies on JavaScript to function properly.</li>
<li><strong>Detection errors</strong>: If Turnstile suspects bot-like behavior, you may encounter repeated challenges for verification.</li>
</ul>
<p>Most challenges are quick to complete and typically take only a few seconds. If it takes longer, ensure your network is stable and follow the <a href="#troubleshooting">troubleshooting steps</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4024.md")
</aside>
<h2 id="401-response-on-a-private-access-token-request">401 response on a Private Access Token request</h2>
<p>When a Challenge Page loads, the browser may request a <a href="/cloudflare-challenges/reference/private-access-tokens/">Private Access Token (PAT)</a> from a <code>/cdn-cgi/challenge-platform/.../pat/...</code> endpoint. On devices, browsers, or networks that cannot issue a token, this request returns an HTTP <code>401</code>.</p>
<p>This response is <strong>expected</strong> and does not mean the visitor was blocked or that the widget failed. Cloudflare falls back to a standard challenge and the visitor proceeds as normal. A <code>401</code> on this request — for example, one seen in browser developer tools or a HAR capture — is not, on its own, a sign of a misconfiguration, a false positive, or a block. For more details, refer to <a href="/cloudflare-challenges/reference/private-access-tokens/">Private Access Tokens</a>.</p>
<h2 id="failed-subdomain-network-requests-during-turnstile-challenges">Failed subdomain network requests during Turnstile challenges</h2>
<p>When looking at browser developer tools or capturing a HAR for Turnstile, it is not uncommon to notice certain requests to specific subdomains failing due to DNS host lookup errors. These subdomains live under the parent domain of <code>challenges.cloudflare.com</code> and <code>dnstest.dev</code>. The requests to them are part of Turnstile's normal execution. That said, these errors should not be perceived as failure root causes, as they are <strong>non-blocking</strong> to visitors.</p>
<p>Given that these DNS host lookup failures are <strong>expected</strong> and <strong>non-fatal</strong> for Turnstile's execution, avoid surfacing them as fatal execution errors, especially in the case of handler-based integrations of Turnstile such as WebView embeddings. For more fine-grained control, consider dropping network errors originating from requests to the <code>*.challenges.cloudflare.com</code> wildcard while preserving error visibility for the <code>challenges.cloudflare.com</code> apex.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>Follow the steps below to ensure that your environment is properly configured.</p>
<ol>
<li>Verify your browser compatibility.
<ul>
<li>Turnstile supports all major browsers, except Internet Explorer.</li>
<li>Ensure your browser is up to date. For more information, refer to our <a href="/cloudflare-challenges/reference/supported-browsers/">Supported browsers</a>.</li>
<li>Run a test on the <a href="https://debug.challenges.cloudflare.com/">compatibility checking tool</a>.</li>
</ul>
</li>
<li>Disable your browser extensions.
<ul>
<li>Some browser extensions, such as ad blockers, may block the scripts Turnstile needs to operate.</li>
<li>Temporarily disable all extensions and reload the page.</li>
</ul>
</li>
<li>Enable JavaScript.
<ul>
<li>Turnstile requires JavaScript to run. Ensure it is enabled in your browser settings. Refer to your browser's documentation for instructions on enabling JavaScript.</li>
</ul>
</li>
<li>Try Incognito or Private mode.
<ul>
<li>Use your browser's incognito or private mode to rule out issues caused by extensions or cached data.</li>
</ul>
</li>
<li>Test another browser or device.
<ul>
<li>Switch to a different browser or device to see if the issue is specific to your current setup.</li>
</ul>
</li>
<li>Avoid VPNs or proxies.
<ul>
<li>Some virtual private networks (VPN) or proxies may interfere with Turnstile. Disable them temporarily to test.</li>
</ul>
</li>
<li>Switch to a different network.
<ul>
<li>Your current network may have restrictions causing Turnstile challenges to fail. Try switching to another network, such as a mobile hotspot.</li>
</ul>
</li>
</ol>
<h2 id="collect-diagnostic-information">Collect diagnostic information</h2>
<p>If the issue persists, collect the following information before contacting the website administrator or Cloudflare Support:</p>
<ul>
<li>A HAR file captured while reproducing the issue. For challenge loops, enable <strong>Preserve log</strong> in your browser's developer tools before reproducing the problem. You may also need to select <strong>Disable cache</strong>.</li>
<li>A browser console log export captured during the same session.</li>
</ul>
<p>For step-by-step instructions, refer to <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">Gathering information for troubleshooting sites</a>.</p>
<h2 id="webview-and-mobile-app-implementations">WebView and mobile app implementations</h2>
<p>If the challenge fails only inside a native app's WebView, review the required WebView settings in <a href="/turnstile/get-started/mobile-implementation/">Mobile implementation</a>. Common causes include disabled JavaScript, missing DOM storage or cookie support, blocked access to <code>challenges.cloudflare.com</code>, and a User Agent that changes during the session.</p>
<p>If none of the above resolves your issue, contact the website administrator with the <a href="/turnstile/troubleshooting/client-side-errors/error-codes/">error code</a> and Ray ID or submit a <a href="/turnstile/troubleshooting/feedback-reports/">feedback report</a> through the Turnstile widget by selecting <strong>Submit Feedback</strong>.</p>
