---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/profiles/
  description: Maintain separate logins and switch accounts per directory.
  full_title: Authentication profiles · Cloudflare Workers docs
  head_html: <title>Authentication profiles · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Maintain separate logins and switch accounts per directory."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/profiles/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/profiles/index.md"><meta property="og:title" content="Authentication profiles · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Maintain separate logins and switch accounts per directory."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/profiles/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/profiles/#page","headline":"Authentication profiles \u00b7 Cloudflare Workers docs","description":"Maintain separate logins and switch accounts per directory.","url":"https://developers.cloudflare.com/workers/wrangler/profiles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/profiles/
  schema: 1
---
<p>Wrangler authenticates as one user at a time. A profile is a named OAuth login that you scope to a chosen set of accounts and can bind to a directory.</p>
<p>Use profiles to switch between accounts for different projects without re-running <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a>. Profiles live under <a href="/workers/wrangler/commands/general/#auth"><code>wrangler auth</code></a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15906.md")
</aside>
<h2 id="when-to-use-profiles">When to use profiles</h2>
<p>Use profiles when you work across more than one Cloudflare account on the same machine:</p>
<ul>
<li><strong>Agency and client work</strong> — keep a separate login for each client account and bind it to that client's project directory. Commands run in each directory use the matching profile automatically.</li>
<li><strong>Account-separated environments</strong> — keep staging and production in different accounts, then bind a profile to each. Pair a profile with an <code>account_id</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> so a command cannot reach the wrong account.</li>
</ul>
<h2 id="how-profiles-work">How profiles work</h2>
<p>A profile combines two things:</p>
<ul>
<li>A login, created through OAuth. During the OAuth flow you choose which accounts the profile may reach. One profile can hold access to several accounts that your user holds.</li>
<li>A directory binding. When you activate a profile in a directory, that directory and its subdirectories use the profile.</li>
</ul>
<h3 id="resolution-order">Resolution order</h3>
<p>For each command, Wrangler selects a profile in this order, highest priority first:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15907.md")
</div>
<h3 id="account-selection">Account selection</h3>
<p>Within the resolved profile, Wrangler selects the target account in this order:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15908.md")
</div>
<p>If a command targets an account that the active profile cannot reach, Wrangler fails with an error that names the account and profile. Wrangler does not fall back to another account.</p>
<h2 id="create-a-profile">Create a profile</h2>
<p>Run <a href="/workers/wrangler/commands/general/#auth-create"><code>wrangler auth create</code></a> with a name. Wrangler starts the OAuth flow, where you choose which accounts the profile may reach.</p>
<pre tabindex="0"><code class="language-sh">wrangler auth create work&#10;</code></pre>
<p>Run the command again with the same name to re-authenticate an existing profile, for example after its token expires.</p>
<h2 id="activate-a-profile-in-a-directory">Activate a profile in a directory</h2>
<p>Run <a href="/workers/wrangler/commands/general/#auth-activate"><code>wrangler auth activate</code></a> to bind a profile to a directory. The binding applies to that directory and its subdirectories. The directory defaults to the current working directory.</p>
<pre tabindex="0"><code class="language-sh">wrangler auth activate work ~/projects/work&#10;</code></pre>
<p>A subdirectory can override the profile bound above it by activating a different profile.</p>
<h2 id="work-across-multiple-client-accounts">Work across multiple client accounts</h2>
<p>This example sets up one profile per client for agency work.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15909.md")
</div>
<p>Commands run in <code>~/clients/client-a</code> now use the <code>client-a</code> profile, and commands in <code>~/clients/client-b</code> use the <code>client-b</code> profile. You do not need to log in again to switch between them.</p>
<h2 id="separate-staging-and-production-accounts">Separate staging and production accounts</h2>
<p>When staging and production live in different accounts, bind a profile to each environment's directory and pin the account in each project's configuration. The <code>account_id</code> acts as a failsafe, so a command cannot deploy to the wrong account even if the profile can reach both.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15911.md")
</div>
<h2 id="switch-profiles-for-a-single-command">Switch profiles for a single command</h2>
<p>Use the <code>--profile</code> flag to run one command with a specific profile, without changing any directory binding.</p>
<pre tabindex="0"><code class="language-sh">wrangler deploy --profile staging&#10;</code></pre>
<p>The <code>--profile</code> flag is not supported by the <code>auth</code>, <code>login</code>, <code>logout</code>, and <code>whoami</code> commands.</p>
<h2 id="list-profiles">List profiles</h2>
<p>Run <a href="/workers/wrangler/commands/general/#auth-list"><code>wrangler auth list</code></a> to see every profile and the directories bound to it.</p>
<pre tabindex="0"><code class="language-sh">wrangler auth list&#10;</code></pre>
<h2 id="remove-a-binding-or-a-profile">Remove a binding or a profile</h2>
<p>To stop a directory from using a profile, run <a href="/workers/wrangler/commands/general/#auth-deactivate"><code>wrangler auth deactivate</code></a> in that directory. The directory returns to the profile bound above it, or to the default profile.</p>
<pre tabindex="0"><code class="language-sh">wrangler auth deactivate ~/projects/staging&#10;</code></pre>
<p>To remove a profile and all of its directory bindings, run <a href="/workers/wrangler/commands/general/#auth-delete"><code>wrangler auth delete</code></a>.</p>
<pre tabindex="0"><code class="language-sh">wrangler auth delete staging&#10;</code></pre>
<h2 id="profiles-and-environment-variables">Profiles and environment variables</h2>
<p>Profiles are a local-machine convenience. They do not apply in CI, containers, or other automated environments, which authenticate per environment with <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>CLOUDFLARE_API_TOKEN</code></a>. For more information, refer to <a href="/workers/ci-cd/">Running Wrangler in CI/CD</a>.</p>
<p>Two rules apply when environment variables are present:</p>
<ul>
<li>When <code>CLOUDFLARE_API_TOKEN</code> is set, Wrangler uses it instead of any profile. You cannot create, activate, deactivate, or delete profiles while it is set.</li>
<li><code>CLOUDFLARE_ACCOUNT_ID</code> and an <code>account_id</code> in your Wrangler configuration file are always respected, including within an active profile.</li>
</ul>
