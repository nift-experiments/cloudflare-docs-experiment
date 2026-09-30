---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2026-04-27 · Changelog
  head_html: <title>WAF Release - 2026-04-27 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2026-04-27 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/#page","headline":"WAF Release - 2026-04-27 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-27-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-27-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 27, 2026</time><h2 id="post-title">WAF Release - 2026-04-27</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on new improvements to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
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
				<code class="nb-rule-id" title="d866f980582748568385b94480cec1dd">80cec1dd</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.  This rule is merged into the original rule
				"PostgreSQL - SQLi - COPY - Body (ID:{" "}
				<code class="nb-rule-id" title="705a6b5569d5472596910e3ce7265a4e">e7265a4e</code>). The rule previously known as "PostgreSQL - SQLi - COPY" is now renamed to "PostgreSQL - SQLi - COPY - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="71d133c374d94559aa9fdf042903de89">2903de89</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9f1b1b7fd28a401b9d5c172d1036cfa6">1036cfa6</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8e40416659334b8ba789365755ff389e">55ff389e</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - AND/OR MAKE_SET/ELT - Body" (ID:{" "}
				<code class="nb-rule-id" title="0f41a593c8fe42c38a26f709252d3934">252d3934</code>). The rule previously known as "SQLi - AND/OR MAKE_SET/ELT" is now renamed to "SQLi - AND/OR MAKE_SET/ELT - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1e0d4372ee1e41b9804b2d5c346487f9">346487f9</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d2c961a164a64cf6b871c9511ac6ceca">1ac6ceca</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4dacc0e6f32d4c5da3c2293edd471337">dd471337</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Common Patterns - Body" (ID:{" "}
				<code class="nb-rule-id" title="98f746d07a6d48ab9dae669acb5d0b9b">cb5d0b9b</code>). The rule previously known as "SQLi - Common Patterns" is now renamed to "SQLi - Common Patterns - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="53a374379f2e41e9934791c1975c07b7">975c07b7</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9efedebfc371443f9fe7308605b1b06b">05b1b06b</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d53a791496d64700870334f4dd0ba3c7">dd0ba3c7</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Equation - Body" (ID:{" "}
				<code class="nb-rule-id" title="e7691e1e4f4d4769909f3df6c2eb3e7f">c2eb3e7f</code>). The rule previously known as "SQLi - Equation" is now renamed to "SQLi - Equation - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="46efbd3496e64c3f902ad33d3d1c2384">3d1c2384</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="46b937649a424b7ead90f6d0e1149ea6">e1149ea6</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="04d9182545f54ba8a4fa29fe205adbb0">205adbb0</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - AND/OR Digit Operator Digit - Body" (ID:{" "}
				<code class="nb-rule-id" title="762dd334ed0b4273816e3ff13893c564">3893c564</code>). The rule previously known as "SQLi - AND/OR Digit Operator Digit" is now renamed to "SQLi - AND/OR Digit Operator Digit - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="a24e7c15503948bc8766481aad2abbaa">ad2abbaa</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0c55eb362df64f92a85aa46753acbc0d">53acbc0d</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="18c9879b7e184c559d23c1652b45a97d">2b45a97d</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Benchmark Function - Body" (ID:{" "}
				<code class="nb-rule-id" title="ac4e9ebfb43a4f3998f6072d2ebc44ad">2ebc44ad</code>). The rule previously known as "SQLi - Benchmark Function" is now renamed to "SQLi - Benchmark Function - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2adbc36c52324efcb4681b829889aadc">9889aadc</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="69564af3bc54406080deed72491b28e9">491b28e9</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="94b1646f0b0b46ec9b96f7742aa649de">2aa649de</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Comparison - Body" (ID:{" "}
				<code class="nb-rule-id" title="8166da327a614849bfa29317e7907480">e7907480</code>). The rule previously known as "SQLi - Comparison" is now renamed to "SQLi - Comparison - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="455ce87681bd4200bf53456c39e3e013">39e3e013</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="8152816062ed47f69be0f907f4bdb492">f4bdb492</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="d5afd403a0544248b829fe5da1ff3b34">a1ff3b34</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - Body - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. This rule is merged into the original rule "SQLi - String Concatenation - Headers" (ID:{" "}
				<code class="nb-rule-id" title="3b0c61407d0b4f7d87e516472116d2fe">2116d2fe</code>).The rule previously known as "SQLi - String Concatenation - Headers" is now renamed to "SQLi - String Concatenation - Body". </td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="cb0ec290ee454138abe18b750d0e6c3b">0d0e6c3b</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.(Former Id was{" "}
				<code class="nb-rule-id" title="380099df2bb2469c91ebbb7b846d1940">846d1940</code>)</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="c46d9097c9ef419aa4d9f10626cc211f">26cc211f</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. (Former Id was{" "}
				<code class="nb-rule-id" title="bd19397228404b85aa3797238fae8c84">8fae8c84</code>)</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="6542d36980cf4018b4d5e2bfeacc78ab">eacc78ab</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - SELECT Expression - Body" (ID:{" "}
				<code class="nb-rule-id" title="00da180570d34b5bae2121acd0023a36">d0023a36</code>). The rule previously known as "SQLi - SELECT Expression" is now renamed to "SQLi - SELECT Expression - Body".
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="4073f7b575ff45dfb7621b43630bb223">630bb223</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="2721e3184d50466ea637e9afdcd6efb5">dcd6efb5</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="7ecca84c08aa4aad9b5a7bda18c47cea">18c47cea</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - ORD and ASCII- Body" (ID:{" "}
				<code class="nb-rule-id" title="2fc38b34a9d744d2a3cbcc41d0d207f9">d0d207f9</code>). The rule previously known as "SQLi - ORD and ASCII" is now renamed to "SQLi - ORD and ASCII- Body".
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="f6d10e10c9514eb49dcc2122bdb1618f">bdb1618f</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="60704f5c5513425c94cf77031d0906b6">1d0906b6</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="700613b191d3479ea2782b4e9fe4eff5">9fe4eff5</code>
</td>
<td>N/A</td>
<td>SQLi - Destructive Operations</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>					
</tbody>
</table>
</div></article></div>
