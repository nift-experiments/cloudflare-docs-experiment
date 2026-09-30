---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2025-05-27 · Changelog
  head_html: <title>WAF Release - 2025-05-27 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2025-05-27 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/#page","headline":"WAF Release - 2025-05-27 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-05-27-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 27, 2025</time><h2 id="post-title">WAF Release - 2025-05-27</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup covers nine vulnerabilities, including six critical RCEs and one dangerous file upload. Affected platforms span cloud services, CI/CD pipelines, CMSs, and enterprise backup systems. Several are now addressed by updated WAF managed rulesets.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Ingress-Nginx (CVE-2025-1098): Unauthenticated RCE via unsafe annotation handling. Impacts Kubernetes clusters.</li>
<li>GitHub Actions (CVE-2025-30066): RCE through malicious workflow inputs. Targets CI/CD pipelines.</li>
<li>Craft CMS (CVE-2025-32432): Template injection enables unauthenticated RCE. High risk to content-heavy sites.</li>
<li>F5 BIG-IP (CVE-2025-31644): RCE via TMUI exploit, allowing full system compromise.</li>
<li>AJ-Report (CVE-2024-15077): RCE through untrusted template execution. Affects reporting dashboards.</li>
<li>NAKIVO Backup (CVE-2024-48248): RCE via insecure script injection. High-value target for ransomware.</li>
<li>SAP NetWeaver (CVE-2025-31324): Dangerous file upload flaw enables remote shell deployment.</li>
<li>Ivanti EPMM (CVE-2025-4428, 4427): Auth bypass allows full access to mobile device management.</li>
<li>Vercel (CVE-2025-32421): Information leak via misconfigured APIs. Useful for attacker recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose critical components across Kubernetes, CI/CD pipelines, and enterprise systems to severe threats including unauthenticated remote code execution, authentication bypass, and information leaks. High-impact flaws in Ingress-Nginx, Craft CMS, F5 BIG-IP, and NAKIVO Backup enable full system compromise, while SAP NetWeaver and AJ-Report allow remote shell deployment and template-based attacks. Ivanti EPMM’s auth bypass further risks unauthorized control over mobile device fleets.</p>
<p>GitHub Actions and Vercel introduce supply chain and reconnaissance risks, allowing malicious workflow inputs and data exposure that aid in targeted exploitation. Organizations should prioritize immediate patching, enhance monitoring, and deploy updated WAF and IDS signatures to defend against likely active exploitation.</p>
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
				<code class="nb-rule-id" title="6a61a14f44af4232a44e45aad127592a">d127592a</code>
</td>
<td>100746</td>
<td>Vercel - Information Disclosure</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100754</td>
<td>AJ-Report - Remote Code Execution - CVE:CVE-2024-15077</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6a13bd6e5fc94b1d9c97eb87dfee7ae4">dfee7ae4</code>
</td>
<td>100756</td>
<td>NAKIVO Backup - Remote Code Execution - CVE:CVE-2024-48248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a4af6f2f15c9483fa9eab01d1c52f6d0">1c52f6d0</code>
</td>
<td>100757</td>
<td>Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1098</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100759</td>
<td>SAP NetWeaver - Dangerous File Upload - CVE:CVE-2025-31324</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dab2df4f548349e3926fee845366ccc1">5366ccc1</code>
</td>
<td>100760</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2025-32432</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb23f172ed64ee08895e161eb40686b">eb40686b</code>
</td>
<td>100761</td>
<td>GitHub Action - Remote Code Execution - CVE:CVE-2025-30066</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="827037f2d5f941789efcba6260fc041c">60fc041c</code>
</td>
<td>100762</td>
<td>Ivanti EPMM - Auth Bypass - CVE:CVE-2025-4428, CVE:CVE-2025-4427</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ddee6d1c4f364768b324609cebafdfe6">ebafdfe6</code>
</td>
<td>100763</td>
<td>F5 Big IP - Remote Code Execution - CVE:CVE-2025-31644</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
