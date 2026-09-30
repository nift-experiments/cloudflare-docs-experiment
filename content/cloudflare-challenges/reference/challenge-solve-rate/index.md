---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/
  description: Measure the percentage of issued challenges that visitors solve successfully.
  full_title: Challenge solve rate (CSR) · Cloudflare challenges docs
  head_html: <title>Challenge solve rate (CSR) · Cloudflare challenges docs</title><meta name="generator" content="Nift"><meta name="description" content="Measure the percentage of issued challenges that visitors solve successfully."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/index.md"><meta property="og:title" content="Challenge solve rate (CSR) · Cloudflare challenges docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Measure the percentage of issued challenges that visitors solve successfully."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Challenges"><meta name="algolia_product_filter" content="Challenges"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Challenges"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/#page","headline":"Challenge solve rate (CSR) \u00b7 Cloudflare challenges docs","description":"Measure the percentage of issued challenges that visitors solve successfully.","url":"https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-challenges/reference/challenge-solve-rate/
  schema: 1
---
<p>The Challenge solve rate (CSR) is the percentage of issued challenges — Non-Interactive Challenge, Managed Challenge, or Interactive Challenge actions — that were solved.</p>
<p>Every challenge involves two separate events:</p>
<ul>
<li><strong>Challenge trigger</strong>: The original request matches a WAF rule with a challenge action. Cloudflare issues a challenge to the visitor's browser.</li>
<li><strong>Challenge solved</strong>: The visitor's browser completes the challenge and sends back a validated response. This event is logged as challenge Solved.</li>
</ul>
<p>Most automated traffic abandons immediately upon encountering the challenge script and never reaches the second event. This is why the count of unsolved challenges is typically very large — those abandonments count as failures in the formula.</p>
<pre tabindex="0"><code class="language-txt">CSR = number of challenges solved / number of challenges issued&#10;</code></pre>
<p>CSR indicates the false positive percentage of a rule. A high CSR means a large share of issued challenges were solved by real visitors, which may indicate the rule is matching too much legitimate traffic. Use CSR to evaluate whether your rule's criteria or action needs adjustment.</p>
<p>You can find the CSR of a rule by going to its corresponding dashboard page:</p>
<p>For <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, go to your zone &gt; <strong>Security</strong> &gt; <strong>Security rules</strong>.</p>
<hr />
<h2 id="challenge-actions-in-security-events">Challenge actions in Security Events</h2>
<p>If you find a Challenge Solved action, such as <code>[js]challengeSolved</code> or <code>challengeSolved</code>, in your Security Events that does not match the underlying rule criteria, it is because this action refers to the successful mitigation of a previous request — not a re-match of the original rule.</p>
<p>The parameters of the solved request may no longer match the original rule's expression. For example, if a challenge was issued due to a low bot score, the score for the solved request may have already changed to a non-suspicious value upon successful verification.</p>
<p>The Challenge Solved action is an informative signal that a previously issued challenge was answered, allowing the visitor's traffic to proceed.</p>
<hr />
<h2 id="failed-challenges">Failed Challenges</h2>
<p>You will not find a dedicated metric for failed challenges in Security Analytics because Cloudflare calculates failure indirectly, based on the difference between challenges issued and challenges solved.</p>
<p>The system views any issued challenge that does not result in a successful clearance cookie as a failure. This is why the number of failed challenges may appear exceptionally high: the majority of issued challenges are never completed.</p>
<p>The official calculation for failures is:</p>
<pre tabindex="0"><code class="language-txt">Failed Challenges = Total Challenges Issued − Total Challenges Solved&#10;</code></pre>
<p>The large number of unmatched challenges is primarily due to automated traffic (bots or scrapers) that abandon the process immediately upon encountering the initial challenge script.</p>
<p>Key reasons a challenge may be issued but never solved:</p>
<ul>
<li>The visitor gives up on the challenge or navigates away from the page.</li>
<li>The visitor attempts to solve the challenge but cannot provide a valid answer.</li>
<li>The system receives an invalid or malformed answer from the client.</li>
<li>The script environment (often a bot's controlled browser) fails to run the necessary client-side checks.</li>
</ul>
