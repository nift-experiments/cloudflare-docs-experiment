---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-discord/
  description: Run DNS lookups and WHOIS queries directly in Discord using the 1.1.1.1 bot. Invite the bot to a server or add it to your account to query DNS records without leaving Discord.
  full_title: DNS over Discord · Cloudflare 1.1.1.1 docs
  head_html: <title>DNS over Discord · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Run DNS lookups and WHOIS queries directly in Discord using the 1.1.1.1 bot. Invite the bot to a server or add it to your account to query DNS records without leaving Discord."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-discord/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-discord/index.md"><meta property="og:title" content="DNS over Discord · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run DNS lookups and WHOIS queries directly in Discord using the 1.1.1.1 bot. Invite the bot to a server or add it to your account to query DNS records without leaving Discord."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-discord/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-discord/#page","headline":"DNS over Discord \u00b7 Cloudflare 1.1.1.1 docs","description":"Run DNS lookups and WHOIS queries directly in Discord using the 1.1.1.1 bot. Invite the bot to a server or add it to your account to query DNS records without leaving Discord.","url":"https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-discord/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/additional-options/dns-over-discord/
  schema: 1
---
<p>The 1.1.1.1 DNS over Discord bot allows you to run DNS lookups and WHOIS queries directly inside Discord, which is useful when you are debugging DNS issues collaboratively or need quick record checks without switching to a terminal.</p>
<p><a href="https://cfl.re/3nM6VfQ">Invite the bot to your Discord server</a> to make it available in that server's channels, or <a href="https://dns-over-discord.v4.wtf/invite/user">add the bot to your Discord account</a> to use it anywhere in Discord.</p>
<h2 id="perform-dns-lookups">Perform DNS lookups</h2>
<p>Once the bot is in your server, type <code>/dig</code> to start performing DNS lookups. Discord will display a slash command form where you specify the domain to look up, an optional DNS record type, and an optional flag for a short result.</p>
<p>A DNS lookup queries the Domain Name System to retrieve records associated with a domain (for example, the IP addresses a domain points to, or the mail servers it uses).</p>
<p>If only a domain is given for the command, the bot defaults to looking for <code>A</code> records (which map a domain to one or more IPv4 addresses) and returns the full format result, not the short form.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/dig domain: cloudflare.com&#10;</code></pre>
<h3 id="supported-record-types">Supported record types</h3>
<p>Discord has a limit of 25 options in slash commands, so DNS over Discord offers the 25 most common DNS record types to choose from.</p>
<details class="nb-details"><summary>Supported DNS record types</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1818.md")
</div></details>
<p>To query other DNS record types, or multiple record types at once, use the <code>/multi-dig</code> command.</p>
<h3 id="short-form-response">Short form response</h3>
<p>The <code>/dig</code> command has an optional flag to request a short form response.</p>
<p>When you request a response in the short form, the name and TTL (time-to-live, how long the record is cached) columns are excluded. The command returns only the record data without formatting, similar to the equivalent <code>dig</code> command-line interface response.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/dig domain: cloudflare.com type: AAAA records short: True&#10;</code></pre>
<h3 id="disable-dnssec-checking">Disable DNSSEC checking</h3>
<p>DNSSEC (Domain Name System Security Extensions) validates that DNS responses have not been tampered with. You can disable this validation in the <code>/dig</code> command by passing <code>cdflag</code> as true, which is  useful when troubleshooting domains with misconfigured DNSSEC, where validation failures block otherwise valid records from appearing.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/dig domain: cloudflare.com type: AAAA records cdflag: True&#10;</code></pre>
<h3 id="refreshing-existing-results">Refreshing existing results</h3>
<p>You can refresh the DNS lookup results by clicking the Refresh button. Clicking it will trigger the bot to re-request the DNS query in the message, and update the results in the message. Any user can click this button.</p>
<p>The refresh button is available on all responses to the <code>/dig</code> command, including those that resulted in an error, such as an unknown domain or no records found.</p>
<h3 id="changing-dns-provider">Changing DNS provider</h3>
<p>By default, the DNS over Discord bot uses Cloudflare's 1.1.1.1 DNS service. To compare results across providers (for example, to check whether a DNS propagation issue is provider-specific) select a different provider from the dropdown below the result. The results in the message update to reflect the selected provider. Any user can change the DNS provider.</p>
<h2 id="multi-dig-command"><code>multi-dig</code> command</h2>
<p>If you want to look up multiple DNS record types at once, use the <code>/multi-dig</code> command. This allows you to specify any supported DNS record type, and multiple types separated by a space.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/multi-dig domain: cloudflare.com types: A AAAA&#10;</code></pre>
<h3 id="supported-record-types-1">Supported record types</h3>
<p>Unlike <code>/dig</code>, the <code>/multi-dig</code> command does not show an autocomplete menu for record types. You provide a space-separated list of DNS record types to look up.</p>
<p>If you include an invalid record type, the bot drops it without an error message. So if results seem incomplete, check for typos in your type list. If no valid types are provided, the bot defaults to <code>A</code> records.</p>
<details class="nb-details"><summary>DNS record types supported and considered valid by the bot</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1819.md")
</div></details>
<h3 id="short-form-response-1">Short form response</h3>
<p>Like the main <code>/dig</code> command, the <code>/multi-dig</code> command also supports the optional short flag after the types have been specified in the slash command.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/multi-dig domain: cloudflare.com types: CDS CDNSKEY short: True&#10;</code></pre>
<h3 id="disable-dnssec-checking-1">Disable DNSSEC checking</h3>
<p>As with the <code>dig</code> command, you can disable DNSSEC checking by passing <code>cdflag</code> as true. This will return the DNS records even if the DNSSEC validation fails.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/multi-dig domain: cloudflare.com type: AAAA records cdflag: True&#10;</code></pre>
<h3 id="refreshing-existing-results-1">Refreshing existing results</h3>
<p>The <code>/multi-dig</code> command also provides a refresh button below each set of DNS results requested (or after each block of 10 DNS record types, if you requested more than 10).</p>
<p>As with the <code>/dig</code> command, any user can press the refresh button to refresh the displayed DNS results, including for DNS queries that had previously failed.</p>
<h3 id="changing-dns-provider-1">Changing DNS provider</h3>
<p>Like the <code>/dig</code> command, you can change the DNS provider when using the <code>/multi-dig</code> command. The menu appears after each set of DNS results (or after each block of results if more than 10 record types are requested).</p>
<p>This menu can be used by any user to change the DNS provider used for the lookup.</p>
<h2 id="whois-command"><code>whois</code> command</h2>
<p>The <code>/whois</code> command performs a RDAP/WHOIS lookup in Discord for a given domain, IP address, or ASN (Autonomous System Number, a unique identifier assigned to a network). WHOIS returns registration and ownership information, such as who registered a domain and when it expires.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-txt">/whois query: cloudflare.com&#10;/whois query: 104.16.132.229&#10;/whois query: 2606:4700::6810:84e5&#10;/whois query: 13335&#10;</code></pre>
<h2 id="other-commands">Other commands</h2>
<p>The bot also has a set of helper commands available to get more information about the bot and quick links.</p>
<h3 id="help-command"><code>help</code> command</h3>
<p>The <code>/help</code> command provides in-Discord documentation about all the commands available in the 1.1.1.1 DNS over Discord bot.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/help&#10;</code></pre>
<h3 id="privacy-command"><code>privacy</code> command</h3>
<p>The <code>/privacy</code> command displays the Privacy Policy notice for using the 1.1.1.1 DNS over Discord bot. You can also <a href="https://dns-over-discord.v4.wtf/privacy">refer to the Privacy Policy page</a> to access it.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/privacy&#10;</code></pre>
<h3 id="terms-command"><code>terms</code> command</h3>
<p>The <code>/terms</code> command displays the Terms of Service notice for using the 1.1.1.1 DNS over Discord bot. You can also <a href="https://dns-over-discord.v4.wtf/terms">refer to the Terms of Service page</a> to access it.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/terms&#10;</code></pre>
<h3 id="github-command"><code>github</code> command</h3>
<p>The DNS over Discord bot is open-source, and the <code>/github</code> command provides a quick link to access the GitHub repository. The GitHub repository can be accessed at <a href="https://github.com/MattIPv4/DNS-over-Discord/">https://github.com/MattIPv4/DNS-over-Discord/</a>.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-txt">/github&#10;</code></pre>
<h3 id="invite-command"><code>invite</code> command</h3>
<p>The <code>/invite</code> command provides the user with a quick link to invite the 1.1.1.1 DNS over Discord bot to another Discord server, or to add it to a Discord account.
The bot can be invited at any time with <a href="https://cfl.re/3nM6VfQ">https://cfl.re/3nM6VfQ</a>.
The bot can also be added to accounts with <a href="https://dns-over-discord.v4.wtf/invite/user">https://dns-over-discord.v4.wtf/invite/user</a>.</p>
<pre tabindex="0"><code class="language-txt">/invite&#10;</code></pre>
<hr />
<h2 id="development">Development</h2>
<p>The DNS over Discord bot is deployed on <a href="https://workers.cloudflare.com/">Cloudflare Workers</a>.</p>
<p>You can find the source code for the bot on GitHub, as well as information on getting started with contributing to the project, at <a href="https://github.com/MattIPv4/DNS-over-Discord/">https://github.com/MattIPv4/DNS-over-Discord/</a>.</p>
