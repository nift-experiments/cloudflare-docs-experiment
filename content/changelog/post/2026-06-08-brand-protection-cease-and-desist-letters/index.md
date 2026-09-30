---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/
  description: New updates and improvements at Cloudflare.
  full_title: Automated Cease and Desist templates for Brand Protection · Changelog
  head_html: <title>Automated Cease and Desist templates for Brand Protection · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Automated Cease and Desist templates for Brand Protection · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/#page","headline":"Automated Cease and Desist templates for Brand Protection \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 10, 2026</time><h2 id="post-title">Automated Cease and Desist templates for Brand Protection</h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p><strong>TL;DR:</strong> Brand Protection now features an <strong>Automated Cease &amp; Desist (C&amp;D)</strong> workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.</p>
<h4 id="why-this-matters">Why this matters</h4>
This update introduces a major shift from pure detection to actionable enforcement, eliminating the manual burden for your Trust & Safety and Legal teams:
<ul>
<li><strong>Instant WHOIS and Recipient Lookup:</strong> We automatically scrape registrar data and WHOIS contact information (such as the registrant or registrar abuse email) behind the scenes, highlighting exactly where your notice needs to be sent</li>
<li><strong>Smart Template Automation:</strong> We pre-fill your custom-branded templates with essential metadata, including the infringing domain, registrar name, and discovery date.</li>
<li><strong>Tailored Enforcement Tones:</strong> Choose from three default layout strategies depending on the severity of the infrastructure match:
<ul>
<li><em>Exact Match:</em> A formal demand for identical trademark infringements</li>
<li><em>Similar Match:</em> A standard notice optimized for typosquatting (one-character distance matches)</li>
<li><em>Friendly Tone:</em> An amicable initial outreach for potential unintentional or accidental infringements</li>
</ul>
</li>
<li><strong>Full Editing Control:</strong> Before creating the final PDF, a real-time review screen allows you to fine-tune the messaging, modify placeholders, and ensure your text aligns perfectly with internal legal standards</li>
</ul>
<h4 id="how-it-works">How it works</h4>
When reviewing a malicious domain match inside your dashboard, your enforcement path splits depending on where the attacker is located:
<ol>
<li><strong>On the Cloudflare Network:</strong> If the domain uses Cloudflare’s network or registrar, trigger our existing integrated abuse reporting flow with one click.</li>
<li><strong>Hosted Elsewhere:</strong> If the domain is hosted on an external provider, click the <strong>Generate C&amp;D Letter</strong> option to launch the new document builder, pick your template, verify the auto-populated recipient data, and download your finalized PDF.</li>
</ol>
<p>You can manage your templates and enforce matches by going to the <strong>Cloudflare Dashboard &gt; Application Security &gt; Brand Protection</strong> and selecting your detected Brand Protection matches.
For more information, read the <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>
<blockquote>
<p><strong>Note:</strong> Cloudflare does not represent you and cannot provide you with legal advice. Only you can decide whether your rights have been infringed, whether a cease and desist letter is appropriate, and what that letter should say.</p>
</blockquote>
</div></article></div>
