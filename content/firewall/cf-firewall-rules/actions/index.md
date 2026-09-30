---
cp9:
  canonical: https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/
  description: Review available actions for firewall rules.
  full_title: Firewall rules actions · Cloudflare Firewall Rules (deprecated) docs
  head_html: <title>Firewall rules actions · Cloudflare Firewall Rules (deprecated) docs</title><meta name="generator" content="Nift"><meta name="description" content="Review available actions for firewall rules."><link rel="canonical" href="https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/index.md"><meta property="og:title" content="Firewall rules actions · Cloudflare Firewall Rules (deprecated) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review available actions for firewall rules."><meta property="og:url" content="https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Firewall Rules (deprecated)"><meta name="algolia_product_filter" content="Firewall Rules (deprecated)"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Firewall Rules (deprecated)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/#page","headline":"Firewall rules actions \u00b7 Cloudflare Firewall Rules (deprecated) docs","description":"Review available actions for firewall rules.","url":"https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /firewall/cf-firewall-rules/actions/
  schema: 1
---
<p>The action of a firewall rule tells Cloudflare how to handle HTTP requests that have matched the rule expression.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8695.md")
</aside>
<h2 id="supported-actions">Supported actions</h2>
<p>The table below lists the actions available in firewall rules. These actions are listed in order of precedence. If the same request matches two different rules which have the same priority, precedence determines the action to take.</p>
<p>For example, the <em>Allow</em> action takes precedence over the <em>Block</em> action. In a case where a request matches a rule with the <em>Allow</em> action and another with the <em>Block</em> action, precedence resolves the tie, and Cloudflare allows the request.</p>
<p>There are two exceptions to this behavior: the <em>Log</em> and <em>Bypass</em> actions. Unlike other actions, <em>Log</em> and <em>Bypass</em> do not terminate further evaluation within firewall rules. This means that if a request matches two different rules and one of those rules specifies the <em>Log</em> or <em>Bypass</em> action, the second action will be triggered instead, even though <em>Log</em>/<em>Bypass</em> has precedence.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8694.md")
</aside>
<table>
<thead>
<tr>
<th>Action</th>
<th>Description</th>
<th>Order of precedence</th>
</tr>
</thead>
<tbody>
<tr>
<td>
        <strong>Log</strong>
<br />
<br />
        API value:<br />
        <code>log</code>
</td>
<td>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;Records matching requests in the Cloudflare Logs.&lt;/li&gt;&#10;      &lt;li&gt;Only available for Enterprise plans.&lt;/li&gt;&#10;      &lt;li&gt;&#10;        Recommended for validating rules before committing to a more severe&#10;        action.&#10;      &lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>1</td>
</tr>
<tr>
<td>
        <strong>Bypass</strong>
<br />
<br />
        API value:<br />
        <code>bypass</code>
</td>
<td>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;&#10;        Allows user to dynamically disable Cloudflare security features for&#10;        a request.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;Available to all plans.&lt;/li&gt;&#10;      &lt;li&gt;&#10;        &lt;p&gt;&#10;          Matching requests exempt from evaluation by a user-defined list&#10;          containing one or more of the following Cloudflare security&#10;          features:&#10;        &lt;/p&gt;&#10;        &lt;ul&gt;&#10;&#10;          &lt;li&gt;&#10;            &lt;a href=&quot;/waf/tools/user-agent-blocking/&quot;&gt;&#10;              User Agent Blocking&#10;            &lt;/a&gt;&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            &lt;a href=&quot;/waf/tools/browser-integrity-check/&quot;&gt;&#10;              Browser Integrity Check&#10;            &lt;/a&gt;&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            &lt;a href=&quot;/waf/tools/scrape-shield/hotlink-protection/&quot;&gt;&#10;              Hotlink Protection&#10;            &lt;/a&gt;&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            &lt;a href=&quot;/waf/tools/security-level/&quot;&gt;&#10;              Security Level (IP Reputation)&#10;            &lt;/a&gt;&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            &lt;a href=&quot;/waf/reference/legacy/old-rate-limiting/&quot;&gt;Rate Limiting&lt;/a&gt; (previous version, deprecated)&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            &lt;a href=&quot;/waf/tools/zone-lockdown/&quot;&gt;Zone Lockdown&lt;/a&gt;&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            &lt;a href=&quot;/waf/reference/legacy/old-waf-managed-rules/&quot;&gt;WAF managed rules&lt;/a&gt; (previous version, deprecated)&#10;          &lt;/li&gt;&#10;&#10;        &lt;/ul&gt;&#10;        &lt;p&gt;&#10;          &lt;strong&gt;Notes:&lt;/strong&gt;&#10;        &lt;/p&gt;&#10;        &lt;ul&gt;&#10;&#10;          &lt;li&gt;&#10;            Currently, you cannot bypass Bot Fight Mode. For more information on this product, refer to &lt;a href=&quot;/bots/&quot;&gt;Cloudflare bot solutions&lt;/a&gt;.&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            You cannot bypass the new &lt;a href=&quot;/waf/managed-rules/&quot;&gt;WAF managed rules&lt;/a&gt; using this&#10;            action, only the previous version of WAF managed rules. To skip&#10;            one or more managed rules in the new WAF for specific requests,&#10;            &lt;a href=&quot;/waf/managed-rules/waf-exceptions/&quot;&gt; create an exception&lt;/a&gt;.&#10;          &lt;/li&gt;&#10;&#10;        &lt;/ul&gt;&#10;        &lt;p&gt;&lt;/p&gt;&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        Requests which match the &lt;em&gt;Bypass&lt;/em&gt; action are still subject to&#10;        evaluation (and thus a challenge or block) within Firewall Rules,&#10;        based on the order of execution.&#10;      &lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>2</td>
</tr>
<tr>
<td>
        <strong>Allow</strong>
<br />
<br />
        API value:<br />
        <code>allow</code>
</td>
<td>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;&#10;        Matching requests are exempt from &lt;em&gt;Bypass&lt;/em&gt;, &lt;em&gt;Block&lt;/em&gt;,&#10;        and challenge actions triggered by other firewall rules.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        The scope of the &lt;em&gt;Allow&lt;/em&gt; action is limited to firewall rules;&#10;        matching requests are &lt;strong&gt;not&lt;/strong&gt; exempt from action by&#10;        other Cloudflare security products such as Bot Fight Mode, IP Access&#10;        Rules, and WAF Managed Rules.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        Matched requests will be mitigated if they are part of a DDoS&#10;        attack.&#10;      &lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>3</td>
</tr>
<tr>
<td>
        <strong>Interactive Challenge</strong>
<br />
<br />
        API value:<br />
        <code>challenge</code>
</td>
<td>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;&#10;        This option is not recommended. Instead, choose &lt;strong&gt;Managed Challenge&lt;/strong&gt;, which issues interactive challenges to visitors only when necessary.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        The client that made the request must pass an interactive challenge.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        If successful, Cloudflare accepts the matched request; otherwise, it&#10;        is blocked.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        For additional information, refer to &lt;a href=&quot;#notes-about-challenge-actions&quot;&gt;Notes about challenge actions&lt;/a&gt;.&#10;      &lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>4</td>
</tr>
<tr>
<td>
        <strong>
          Managed Challenge
        </strong>
<br />
<br />
        API value:<br />
        <code>managed_challenge</code>
</td>
<td>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;&#10;        Helps reduce the lifetimes of human time spent solving interactive&#10;        challenges across the Internet.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        Depending on the characteristics of a request, Cloudflare will&#10;        dynamically choose the appropriate type of challenge from the&#10;        following actions based on specific criteria:&#10;        &lt;ul&gt;&#10;&#10;          &lt;li&gt;&#10;            Show a non-interactive challenge page.&#10;          &lt;/li&gt;&#10;          &lt;li&gt;&#10;            Show an interactive challenge (such as requiring the visitor to&#10;            click a button or to perform a task).&#10;          &lt;/li&gt;&#10;&#10;        &lt;/ul&gt;&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        For additional information, refer to &lt;a href=&quot;#notes-about-challenge-actions&quot;&gt;Notes about challenge actions&lt;/a&gt;.&#10;      &lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>5</td>
</tr>
<tr>
<td>
        <strong>Non-Interactive Challenge</strong>
<br />
<br />
        API value:<br />
        <code>js_challenge</code>
</td>
<td>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;&#10;        Useful for ensuring that bots and spam cannot access the requested&#10;        resource; browsers, however, are free to satisfy the challenge&#10;        automatically.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        The client that made the request must pass a Non-Interactive&#10;        Cloudflare challenge before proceeding.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        If successful, Cloudflare accepts the matched request; otherwise, it&#10;        is blocked.&#10;      &lt;/li&gt;&#10;      &lt;li&gt;&#10;        For additional information, refer to &lt;a href=&quot;#notes-about-challenge-actions&quot;&gt;Notes about challenge actions&lt;/a&gt;.&#10;      &lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>6</td>
</tr>
<tr>
<td>
        <strong>Block</strong>
<br />
<br />
        API value:<br />
        <code>block</code>
</td>
<td>Matching requests are denied access to the site.</td>
<td>7</td>
</tr>
</tbody>
</table>
<h2 id="notes-about-challenge-actions">Notes about challenge actions</h2>
<p>When you configure a firewall rule with one of the challenge actions — <em>Non-Interactive Challenge</em>, <em>Managed Challenge</em>, or <em>Interactive Challenge</em> — and a request matches the rule, one of two things can happen:</p>
<ul>
<li>The request is blocked if the visitor fails the challenge</li>
<li>The request is allowed if the visitor passes the challenge</li>
</ul>
<p>In this last case, no further firewall rules will be processed. This means that the action of any later rules with a challenge or <em>Block</em> action also matching the request will not be applied, and the request will be allowed.</p>
