---
cp9:
  canonical: https://developers.cloudflare.com/bots/plans/pro/
  description: Bot protection features included in the Cloudflare Pro plan.
  full_title: Plans — Pro · Cloudflare bot solutions docs
  head_html: <title>Plans — Pro · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Bot protection features included in the Cloudflare Pro plan."><link rel="canonical" href="https://developers.cloudflare.com/bots/plans/pro/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/plans/pro/index.md"><meta property="og:title" content="Plans — Pro · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bot protection features included in the Cloudflare Pro plan."><meta property="og:url" content="https://developers.cloudflare.com/bots/plans/pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/plans/pro/#page","headline":"Plans \u2014 Pro \u00b7 Cloudflare bot solutions docs","description":"Bot protection features included in the Cloudflare Pro plan.","url":"https://developers.cloudflare.com/bots/plans/pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/plans/pro/
  schema: 1
---
<p>To learn more about features and functionality, select a plan.</p>
<p><a class="nb-link-button" href="/bots/plans/free/">Free</a><a class="nb-link-button" href="/bots/plans/pro/">Pro</a><a class="nb-link-button" href="/bots/plans/biz-and-ent/">Business</a><a class="nb-link-button" href="/bots/plans/bm-subscription/">Bot Management for Enterprise</a></p>
<table>
<thead>
<tr>
<th width="25%"></th>
<th width="30%"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
				<b>Plan name</b>
</td>
<td>Super Bot Fight Mode</td>
</tr>
<tr>
<td>
				<b>Availability</b>
</td>
<td>All Pro customers</td>
</tr>
<tr>
<td>
				<b>Type of bots detected</b>
</td>
<td>Simple bots and headless browsers</td>
</tr>
<tr>
<td>
				<b>Actions</b>
</td>
<td>Customer chooses whether to allow, block, or challenge</td>
</tr>
<tr>
<td>
				<b>Analytics</b>
</td>
<td>
				Limited analytics available in a <b>Bot Report</b>
</td>
</tr>
<tr>
<td>
				<b>Control</b>
</td>
<td>Applied to all traffic across a domain</td>
</tr>
<tr>
<td>
				<b>Additional features</b>
</td>
<td>
				<a href="/bots/additional-configurations/block-ai-bots/">Block AI bots</a>, <br/>
				<a href="/bots/additional-configurations/ai-labyrinth/">AI Labyrinth</a>, <br />
				<a href="/bots/additional-configurations/managed-robots-txt/">Instruct AI bot traffic with <code>robots.txt</code></a>, <br />
				<a href="/bots/concepts/bot-score/#bot-groupings">Definitely automated bots</a>, <br />
				<a href="/bots/concepts/bot/verified-bots/">Verified bots</a>, <br />
				<a href="/bots/additional-configurations/static-resources/">Static resource protection</a>, <br />
				<a href="/bots/troubleshooting/wordpress-loopback-issue/">Optimize for WordPress</a>, <br />
				<a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a> 
</td>
</tr>
</tbody>
</table>
<h2 id="bot-settings-versus-custom-rules">Bot settings versus custom rules</h2>
<p>The following features are handled automatically in <strong>Security Settings</strong> and do not require custom rules:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Handled by bot settings</th>
<th>Requires custom rules</th>
</tr>
</thead>
<tbody>
<tr>
<td>Block or challenge definitely automated traffic</td>
<td>Yes</td>
<td>Only for path-specific or threshold-tuned rules</td>
</tr>
<tr>
<td>Block or challenge likely automated traffic</td>
<td>Not available on Pro</td>
<td>Yes, with <a href="/bots/plans/bm-subscription/">Bot Management</a></td>
</tr>
<tr>
<td>Allow or block verified bots</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Block AI crawlers</td>
<td>Yes</td>
<td>Only to target individual AI crawlers</td>
</tr>
<tr>
<td>Protect static resources</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Optimize for WordPress</td>
<td>Yes</td>
<td>No</td>
</tr>
</tbody>
</table>
<p>For more details on when custom rules are needed, refer to <a href="/bots/additional-configurations/custom-rules/">custom rules</a>.</p>
<h2 id="how-do-i-get-started">How do I get started?</h2>
<p>To get started, review our <a href="/bots/get-started/">setup guides</a>. If you have any questions, visit the <a href="https://community.cloudflare.com/">community</a> to engage with other Cloudflare users.</p>
