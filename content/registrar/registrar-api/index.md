---
cp9:
  canonical: https://developers.cloudflare.com/registrar/registrar-api/
  description: Search and register domains via the Registrar API.
  full_title: Registrar API · Cloudflare Registrar docs
  head_html: <title>Registrar API · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Search and register domains via the Registrar API."><link rel="canonical" href="https://developers.cloudflare.com/registrar/registrar-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/registrar-api/index.md"><meta property="og:title" content="Registrar API · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Search and register domains via the Registrar API."><meta property="og:url" content="https://developers.cloudflare.com/registrar/registrar-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/registrar-api/#page","headline":"Registrar API \u00b7 Cloudflare Registrar docs","description":"Search and register domains via the Registrar API.","url":"https://developers.cloudflare.com/registrar/registrar-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/registrar-api/
  schema: 1
---
<p>Use the Cloudflare Registrar API to search for domain names, check real-time availability and pricing, and register supported domains programmatically.</p>
<p>This guide walks through the beta workflow using the Cloudflare API and <code>curl</code>. These same endpoints are in the official Cloudflare API reference and through Cloudflare MCP by default, which means they can be used from scripts, backend services, CI pipelines, and agent-driven tools without additional integration work.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you make your first API request, make sure you have:</p>
<ol>
<li>A Cloudflare account ID.</li>
<li>An API token with Registrar write permissions. Create one at <code>https://dash.cloudflare.com/&lt;ACCOUNT_ID&gt;/api-tokens</code>.</li>
<li>A billing profile with a valid default payment method. Manage billing at <code>https://dash.cloudflare.com/&lt;ACCOUNT_ID&gt;/billing/payment-info</code>.</li>
<li>A default registrant contact configured on the account, plus acceptance of the Domain Registration Agreement on the registrations page: <code>https://dash.cloudflare.com/&lt;ACCOUNT_ID&gt;/domains/registrations</code>.</li>
</ol>
<p>For related setup help, refer to:</p>
<ul>
<li><a href="/fundamentals/account/find-account-and-zone-ids/">Find your account ID</a></li>
<li><a href="/fundamentals/api/get-started/create-token/">Create an API token</a></li>
<li><a href="/fundamentals/api/how-to/make-api-calls/">Make API calls</a></li>
<li><a href="/api/resources/registrar">Registrar API docs</a></li>
</ul>
<h2 id="set-up-authentication">Set up authentication</h2>
<p>Cloudflare API requests use bearer token authentication.</p>
<p>In your terminal, define environment variables for your account ID and API token:</p>
<pre tabindex="0"><code class="language-shell">export ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;export CLOUDFLARE_API_TOKEN=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;</code></pre>
<p>All requests in this guide use the Cloudflare API v4 base URL:</p>
<pre tabindex="0"><code>https://api.cloudflare.com/client/v4/&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/445.md")
</aside>
<h2 id="beta-workflow">Beta workflow</h2>
<p>The beta workflow has three core steps:</p>
<ol>
<li>Search for candidate domain names.</li>
<li>Check real-time availability and pricing for the domain you want.</li>
<li>Register the domain.</li>
</ol>
<p>Search is useful for discovery, but it is not the source of truth. Always call the <code>Check</code> endpoint immediately before registration to reduce the likelihood of hitting an error during registration.</p>
<h2 id="example-prompts-for-agents">Example prompts for agents</h2>
<p>If you are using Cloudflare MCP or another agent-driven workflow, prompts can be as simple as:</p>
<ul>
<li><code>Search for domains for a coffee shop based in Evergreen, Colorado.</code></li>
<li><code>Find 5 available .com or .dev domains for an AI expense tracker.</code></li>
<li><code>Check whether example.com is available and show me the current price.</code></li>
<li><code>Check these domains and tell me which ones are registrable right now: example.com, example.dev, example.cafe</code></li>
<li><code>Register example.com on my Cloudflare account.</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/446.md")
</aside>
<h2 id="1-search-for-domains"><ol>
<li>Search for domains</li>
</ol></h2>
<p>Use the Search endpoint to generate candidate domain names from a keyword, phrase, or partial domain name.</p>
<p>Search results:</p>
<ul>
<li>Are fast and intended for discovery.</li>
<li>Are based on cached data.</li>
<li>Only include extensions supported by the API beta.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/447.md")
</aside>
<pre tabindex="0"><code class="language-shell">curl --request GET \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/registrar/domain-search?q=acme%20corp&amp;limit=3&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Example response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;domains&quot;: [&#10;      {&#10;        &quot;name&quot;: &quot;acmecorp.com&quot;,&#10;        &quot;registrable&quot;: true,&#10;        &quot;tier&quot;: &quot;standard&quot;,&#10;        &quot;pricing&quot;: {&#10;          &quot;currency&quot;: &quot;USD&quot;,&#10;          &quot;registration_cost&quot;: &quot;8.57&quot;,&#10;          &quot;renewal_cost&quot;: &quot;8.57&quot;&#10;        }&#10;      },&#10;      {&#10;        &quot;name&quot;: &quot;acmecorp.dev&quot;,&#10;        &quot;registrable&quot;: true,&#10;        &quot;tier&quot;: &quot;standard&quot;,&#10;        &quot;pricing&quot;: {&#10;          &quot;currency&quot;: &quot;USD&quot;,&#10;          &quot;registration_cost&quot;: &quot;10.11&quot;,&#10;          &quot;renewal_cost&quot;: &quot;10.11&quot;&#10;        }&#10;      },&#10;      {&#10;        &quot;name&quot;: &quot;acmecorp.app&quot;,&#10;        &quot;registrable&quot;: true,&#10;        &quot;tier&quot;: &quot;standard&quot;,&#10;        &quot;pricing&quot;: {&#10;          &quot;currency&quot;: &quot;USD&quot;,&#10;          &quot;registration_cost&quot;: &quot;11.00&quot;,&#10;          &quot;renewal_cost&quot;: &quot;11.00&quot;&#10;        }&#10;      }&#10;    ]&#10;  }&#10;}&#10;</code></pre>
<h2 id="2-check-real-time-availability-and-pricing"><ol start="2">
<li>Check real-time availability and pricing</li>
</ol></h2>
<p>Use the Check endpoint to confirm whether a domain is currently registrable and to retrieve the current price.</p>
<p>Check results:</p>
<ul>
<li>Query the registry directly.</li>
<li>Reflect current registry state.</li>
<li>Should be used immediately before calling the registration endpoint.</li>
<li>Responses can include a <code>reason</code> field when <code>registrable</code> is <code>false</code>.</li>
</ul>
<p>This endpoint accepts up to 20 domains per request.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/448.md")
</aside>
<pre tabindex="0"><code class="language-shell">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/registrar/domain-check&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;domains&quot;: [&quot;acmecorp.dev&quot;]&#10;  }&#x27;&#10;</code></pre>
<p>Example response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;domains&quot;: [&#10;      {&#10;        &quot;name&quot;: &quot;acmecorp.dev&quot;,&#10;        &quot;registrable&quot;: true,&#10;        &quot;tier&quot;: &quot;standard&quot;,&#10;        &quot;pricing&quot;: {&#10;          &quot;currency&quot;: &quot;USD&quot;,&#10;          &quot;registration_cost&quot;: &quot;10.11&quot;,&#10;          &quot;renewal_cost&quot;: &quot;10.11&quot;&#10;        }&#10;      }&#10;    ]&#10;  }&#10;}&#10;</code></pre>
<p>If a domain cannot be registered through the API, the response includes a reason. For example:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;domains&quot;: [&#10;      {&#10;        &quot;name&quot;: &quot;mybrand.uk&quot;,&#10;        &quot;registrable&quot;: false,&#10;        &quot;reason&quot;: &quot;extension_not_supported_via_api&quot;&#10;      }&#10;    ]&#10;  }&#10;}&#10;</code></pre>
<p>Common <code>reason</code> values include:</p>
<ul>
<li><code>domain_unavailable</code></li>
<li><code>extension_not_supported_via_api</code></li>
<li><code>extension_not_supported</code></li>
<li><code>extension_disallows_registration</code></li>
</ul>
<h2 id="3-register-a-domain"><ol start="3">
<li>Register a domain</li>
</ol></h2>
<p>Use the Registration endpoint to start a domain registration workflow.</p>
<p>Important:</p>
<ul>
<li>Successful registrations are billable to the default payment profile.</li>
<li>Registrations are non-refundable once they complete successfully.</li>
<li>Always confirm the domain name and price before calling this endpoint.</li>
</ul>
<p>The simplest request only requires <code>domain_name</code>:</p>
<pre tabindex="0"><code class="language-shell">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/registrar/registrations&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;domain_name&quot;: &quot;acmecorp.dev&quot;&#10;  }&#x27;&#10;</code></pre>
<p>The account must have a default registrant contact configured. If you do not pass a new contact inline, the API uses the default contact automatically. If you want to register the domain with a different contact, you can pass that contact in the request.</p>
<p>Current default behavior:</p>
<ul>
<li><code>auto_renew</code> defaults to <code>false</code>.</li>
<li><code>privacy_mode</code> defaults to <code>redaction</code> when supported for the TLD, otherwise <code>off</code>.</li>
<li>The account's default payment method is charged automatically.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/449.md")
</aside>
<p>To override the default registrant contact for a single registration, provide one inline:</p>
<pre tabindex="0"><code class="language-shell">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/registrar/registrations&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;domain_name&quot;: &quot;acmecorp.dev&quot;,&#10;    &quot;contacts&quot;: {&#10;      &quot;registrant&quot;: {&#10;        &quot;email&quot;: &quot;ada@example.com&quot;,&#10;        &quot;phone&quot;: &quot;+1.5555555555&quot;,&#10;        &quot;postal_info&quot;: {&#10;          &quot;name&quot;: &quot;Ada Lovelace&quot;,&#10;          &quot;organization&quot;: &quot;Example Inc&quot;,&#10;          &quot;address&quot;: {&#10;            &quot;street&quot;: &quot;123 Main St&quot;,&#10;            &quot;city&quot;: &quot;Austin&quot;,&#10;            &quot;state&quot;: &quot;TX&quot;,&#10;            &quot;postal_code&quot;: &quot;78701&quot;,&#10;            &quot;country_code&quot;: &quot;US&quot;&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Example successful response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;domain_name&quot;: &quot;acmecorp.dev&quot;,&#10;    &quot;state&quot;: &quot;succeeded&quot;,&#10;    &quot;completed&quot;: true,&#10;    &quot;created_at&quot;: &quot;2025-10-27T10:00:00Z&quot;,&#10;    &quot;updated_at&quot;: &quot;2025-10-27T10:00:03Z&quot;,&#10;    &quot;context&quot;: {&#10;      &quot;registration&quot;: {&#10;        &quot;domain_name&quot;: &quot;acmecorp.dev&quot;,&#10;        &quot;status&quot;: &quot;active&quot;,&#10;        &quot;created_at&quot;: &quot;2025-10-27T10:00:00Z&quot;,&#10;        &quot;expires_at&quot;: &quot;2026-10-27T10:00:00Z&quot;,&#10;        &quot;auto_renew&quot;: false,&#10;        &quot;privacy_mode&quot;: &quot;redaction&quot;,&#10;        &quot;locked&quot;: true&#10;      }&#10;    },&#10;    &quot;links&quot;: {&#10;      &quot;self&quot;: &quot;/accounts/abc/registrar/registrations/acmecorp.dev/registration-status&quot;,&#10;      &quot;resource&quot;: &quot;/accounts/abc/registrar/registrations/acmecorp.dev&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="handle-registration-responses">Handle registration responses</h2>
<p>By default, the registration endpoint waits for up to 10 seconds before responding.</p>
<p>You can receive either:</p>
<ul>
<li><code>201 Created</code> if the registration completed within the wait window.</li>
<li><code>202 Accepted</code> if the registration is still in progress.</li>
</ul>
<p>To force immediate asynchronous behavior, send <code>Prefer: respond-async</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/450.md")
</aside>
<p>Example asynchronous request:</p>
<pre tabindex="0"><code class="language-shell">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/registrar/registrations&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;Prefer: respond-async&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;domain_name&quot;: &quot;acmecorp.dev&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Example <code>202 Accepted</code> response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;domain_name&quot;: &quot;acmecorp.dev&quot;,&#10;    &quot;state&quot;: &quot;in_progress&quot;,&#10;    &quot;completed&quot;: false,&#10;    &quot;created_at&quot;: &quot;2025-10-27T10:00:00Z&quot;,&#10;    &quot;updated_at&quot;: &quot;2025-10-27T10:00:10Z&quot;,&#10;    &quot;links&quot;: {&#10;      &quot;self&quot;: &quot;/accounts/abc/registrar/registrations/acmecorp.dev/registration-status&quot;,&#10;      &quot;resource&quot;: &quot;/accounts/abc/registrar/registrations/acmecorp.dev&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="poll-registration-status">Poll registration status</h2>
<p>If the registration is still in progress, poll the status endpoint until the workflow reaches a terminal state.</p>
<pre tabindex="0"><code class="language-shell">curl --request GET \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/registrar/registrations/acmecorp.dev/registration-status&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Example response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;domain_name&quot;: &quot;acmecorp.dev&quot;,&#10;    &quot;state&quot;: &quot;succeeded&quot;,&#10;    &quot;completed&quot;: true,&#10;    &quot;created_at&quot;: &quot;2025-10-27T10:00:00Z&quot;,&#10;    &quot;updated_at&quot;: &quot;2025-10-27T10:00:03Z&quot;,&#10;    &quot;context&quot;: {&#10;      &quot;registration&quot;: {&#10;        &quot;domain_name&quot;: &quot;acmecorp.dev&quot;,&#10;        &quot;status&quot;: &quot;active&quot;,&#10;        &quot;created_at&quot;: &quot;2025-10-27T10:00:00Z&quot;,&#10;        &quot;expires_at&quot;: &quot;2026-10-27T10:00:00Z&quot;,&#10;        &quot;auto_renew&quot;: false,&#10;        &quot;privacy_mode&quot;: &quot;redaction&quot;,&#10;        &quot;locked&quot;: true&#10;      }&#10;    },&#10;    &quot;links&quot;: {&#10;      &quot;self&quot;: &quot;/accounts/abc/registrar/registrations/acmecorp.dev/registration-status&quot;,&#10;      &quot;resource&quot;: &quot;/accounts/abc/registrar/registrations/acmecorp.dev&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Possible workflow states include:</p>
<ul>
<li><code>in_progress</code></li>
<li><code>succeeded</code></li>
<li><code>failed</code></li>
<li><code>action_required</code></li>
<li><code>blocked</code></li>
</ul>
<p>If the workflow returns <code>action_required</code>, stop polling and surface the required user action.</p>
<p>If the workflow returns <code>failed</code>, inspect <code>error.code</code> and <code>error.message</code> before retrying.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/451.md")
</aside>
<h2 id="get-the-registration-resource">Get the registration resource</h2>
<p>Once registration is complete, retrieve the registration resource directly:</p>
<pre tabindex="0"><code class="language-shell">curl --request GET \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/registrar/registrations/acmecorp.dev&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Example response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;domain_name&quot;: &quot;acmecorp.dev&quot;,&#10;    &quot;status&quot;: &quot;active&quot;,&#10;    &quot;created_at&quot;: &quot;2025-10-27T10:00:00Z&quot;,&#10;    &quot;expires_at&quot;: &quot;2026-10-27T10:00:00Z&quot;,&#10;    &quot;auto_renew&quot;: false,&#10;    &quot;privacy_mode&quot;: &quot;redaction&quot;,&#10;    &quot;locked&quot;: true&#10;  }&#10;}&#10;</code></pre>
<h2 id="beta-limitations">Beta limitations</h2>
<p>This is the first beta release of the Registrar API.</p>
<p>Current limitations include:</p>
<ul>
<li>Only a subset of supported Cloudflare Registrar extensions are available through the API beta.</li>
<li>Search results are scoped to API-supported extensions only.</li>
<li>Some extensions supported in the dashboard are not yet available for programmatic registration.</li>
<li>When supported, premium domains will require explicit fee acknowledgement before registration.</li>
<li>Renewals are not yet available through the API.</li>
<li>Transfers are not yet available through the API.</li>
<li>Contact updates are not yet available through the API.</li>
</ul>
<p>If you check a domain that Cloudflare supports in the dashboard but not yet in the API, the Check response returns <code>extension_not_supported_via_api</code>.</p>
<p>These core Registrar functions will be added in future versions of the API.</p>
<p>Add a link here to the supported extensions list once it exists.</p>
<h2 id="next-steps">Next steps</h2>
- Review [Cloudflare API auth and request conventions](/fundamentals/api/how-to/make-api-calls/).
<p>If you are building with the Registrar API beta, especially for automation, agents, or multi-tenant platform workflows, we want your feedback.</p>
