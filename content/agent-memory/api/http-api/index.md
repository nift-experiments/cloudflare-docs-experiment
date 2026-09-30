---
cp9:
  canonical: https://developers.cloudflare.com/agent-memory/api/http-api/
  description: Use Agent Memory from services that call the Cloudflare API directly.
  full_title: HTTP API · Cloudflare Agent Memory docs
  head_html: <title>HTTP API · Cloudflare Agent Memory docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Agent Memory from services that call the Cloudflare API directly."><link rel="canonical" href="https://developers.cloudflare.com/agent-memory/api/http-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agent-memory/api/http-api/index.md"><meta property="og:title" content="HTTP API · Cloudflare Agent Memory docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Agent Memory from services that call the Cloudflare API directly."><meta property="og:url" content="https://developers.cloudflare.com/agent-memory/api/http-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agent Memory"><meta name="algolia_product_filter" content="Agent Memory"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agent Memory"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agent-memory/api/http-api/#page","headline":"HTTP API \u00b7 Cloudflare Agent Memory docs","description":"Use Agent Memory from services that call the Cloudflare API directly.","url":"https://developers.cloudflare.com/agent-memory/api/http-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agent-memory/api/http-api/
  schema: 1
---
<p>Use the HTTP API to call Agent Memory from services that do not run inside <a href="/workers/">Cloudflare Workers</a>. For Workers applications, use the <a href="/agent-memory/api/workers-api/">Workers API</a> through an <code>agent_memory</code> binding.</p>
<p>The HTTP API uses namespaces and profiles. A namespace scopes profiles for your application, and each profile is an isolated memory store. Profiles are created automatically when you first write to them.</p>
<h2 id="authentication">Authentication</h2>
<p>All requests require an <a href="/fundamentals/api/get-started/create-token/">API token</a> with the appropriate Agent Memory permissions.</p>
<p>Include your API token in the <code>Authorization</code> header:</p>
<pre tabindex="0"><code class="language-txt">Authorization: Bearer &lt;API_TOKEN&gt;&#10;</code></pre>
<p>For information about calling the Cloudflare API, refer to <a href="/fundamentals/api/how-to/make-api-calls/">Make API calls</a>.</p>
<h2 id="namespace-management">Namespace management</h2>
<p>A <a href="/agent-memory/concepts/namespaces-profiles/">namespace</a> is a top-level container that scopes memory profiles for your application.</p>
<h3 id="create-a-namespace">Create a namespace</h3>
<p>Creates a new namespace for the given account.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;name&quot;: &quot;support-agent&quot;}&#x27;&#10;</code></pre>
<p>The response includes the namespace name that you use in Worker bindings and HTTP API calls.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;		&quot;name&quot;: &quot;support-agent&quot;,&#10;		&quot;created_at&quot;: &quot;2026-04-21T00:00:00.000Z&quot;,&#10;		&quot;updated_at&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="list-namespaces">List namespaces</h3>
<p>Lists all namespaces for the given account. Results are paginated.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces?per_page=50&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;			&quot;name&quot;: &quot;support-agent&quot;,&#10;			&quot;created_at&quot;: &quot;2026-04-21T00:00:00.000Z&quot;,&#10;			&quot;updated_at&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;cursor&quot;: &quot;next-cursor&quot;,&#10;		&quot;per_page&quot;: 50,&#10;		&quot;count&quot;: 1&#10;	}&#10;}&#10;</code></pre>
<h3 id="get-a-namespace">Get a namespace</h3>
<p>Retrieves a single namespace by name.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;		&quot;name&quot;: &quot;support-agent&quot;,&#10;		&quot;created_at&quot;: &quot;2026-04-21T00:00:00.000Z&quot;,&#10;		&quot;updated_at&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="delete-a-namespace">Delete a namespace</h3>
<p>Marks a namespace for deletion. The namespace name becomes available for reuse after deletion.</p>
<pre tabindex="0"><code class="language-bash">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="profiles">Profiles</h2>
<p>Use profile endpoints to manage profiles and operate on memory stored in a named profile. Profiles are created automatically when you first write to them.</p>
<h3 id="delete-a-profile">Delete a profile</h3>
<p>Marks a profile and all its memories and messages for deletion.</p>
<pre tabindex="0"><code class="language-bash">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="delete-a-session">Delete a session</h3>
<p>Marks all memories and messages in a profile that are tagged with the given session ID for deletion. Rows from other sessions in the same profile are untouched. Idempotent: deleting a session ID that has no rows is a no-op.</p>
<pre tabindex="0"><code class="language-bash">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/sessions/&lt;SESSION_ID&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="ingest-messages">Ingest messages</h3>
<p>Processes a conversation and extracts structured memories from it. Agent Memory identifies facts, events, instructions, and tasks automatically, so you do not need to specify what to remember.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/ingest&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;I prefer concise answers.&quot;,&#10;        &quot;timestamp&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;      }&#10;    ],&#10;    &quot;sessionId&quot;: &quot;chat-2026-04-21&quot;&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p><code>ingest</code> is idempotent. Re-ingesting the same conversation does not create duplicate memories.</p>
<h3 id="remember-a-memory">Remember a memory</h3>
<p>Stores a single memory explicitly. Use <code>remember</code> when your application or agent already knows what should be stored.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/remember&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;content&quot;: &quot;The user prefers concise answers.&quot;,&#10;    &quot;sessionId&quot;: &quot;chat-2026-04-21&quot;&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;		&quot;type&quot;: &quot;instruction&quot;,&#10;		&quot;summary&quot;: &quot;The user prefers concise answers.&quot;,&#10;		&quot;content&quot;: &quot;The user prefers concise answers.&quot;,&#10;		&quot;sessionId&quot;: &quot;chat-2026-04-21&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;,&#10;		&quot;updatedAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="recall-memories">Recall memories</h3>
<p>Searches stored memories in the profile and returns a synthesized answer grounded in the stored content.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/recall&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;query&quot;: &quot;How should I answer this user?&quot;,&#10;    &quot;thinkingLevel&quot;: &quot;low&quot;,&#10;    &quot;responseLength&quot;: &quot;medium&quot;&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;answer&quot;: &quot;The user prefers concise answers.&quot;,&#10;		&quot;count&quot;: 1,&#10;		&quot;candidates&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;				&quot;summary&quot;: &quot;The user prefers concise answers.&quot;,&#10;				&quot;sessionId&quot;: &quot;chat-2026-04-21&quot;,&#10;				&quot;score&quot;: 0.87&#10;			}&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>If no memories match the query, <code>recall</code> returns an empty answer.</p>
<h3 id="list-memories">List memories</h3>
<p>Lists memories stored in the profile.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/memories?per_page=50&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;			&quot;type&quot;: &quot;instruction&quot;,&#10;			&quot;summary&quot;: &quot;The user prefers concise answers.&quot;,&#10;			&quot;sessionId&quot;: &quot;chat-2026-04-21&quot;,&#10;			&quot;createdAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;,&#10;			&quot;updatedAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;cursor&quot;: &quot;next-cursor&quot;,&#10;		&quot;per_page&quot;: 50,&#10;		&quot;count&quot;: 1&#10;	}&#10;}&#10;</code></pre>
<p>List entries omit <code>content</code>. Use the get memory endpoint to retrieve the full memory.</p>
<p>To filter memories, use the <code>session_id</code> and <code>type</code> query parameters.</p>
<h3 id="get-a-memory">Get a memory</h3>
<p>Retrieves a memory by ID.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/memories/&lt;MEMORY_ID&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;		&quot;type&quot;: &quot;instruction&quot;,&#10;		&quot;summary&quot;: &quot;The user prefers concise answers.&quot;,&#10;		&quot;content&quot;: &quot;The user prefers concise answers.&quot;,&#10;		&quot;sessionId&quot;: &quot;chat-2026-04-21&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;,&#10;		&quot;updatedAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="delete-a-memory">Delete a memory</h3>
<p>Deletes a memory by ID. Removes the memory and any source messages linked to it. Returns the deleted memory.</p>
<pre tabindex="0"><code class="language-bash">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/memories/&lt;MEMORY_ID&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;01JSGCEXAMPLE000000000000&quot;,&#10;		&quot;type&quot;: &quot;instruction&quot;,&#10;		&quot;summary&quot;: &quot;The user prefers concise answers.&quot;,&#10;		&quot;content&quot;: &quot;The user prefers concise answers.&quot;,&#10;		&quot;sessionId&quot;: &quot;chat-2026-04-21&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;,&#10;		&quot;updatedAt&quot;: &quot;2026-04-21T00:00:00.000Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="get-a-summary">Get a summary</h3>
<p>Generates a structured Markdown summary of everything stored in a memory profile. Use it to inspect what Agent Memory remembers about a profile.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/agent-memory/namespaces/&lt;NAMESPACE_NAME&gt;/profiles/&lt;PROFILE_NAME&gt;/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;summary&quot;: &quot;## Summary\n\nThe user prefers concise answers.&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>To scope the &quot;Last Session&quot; section of the summary, include the <code>sessionId</code> field in the request body.</p>
<h2 id="error-responses">Error responses</h2>
<p>All endpoints return standard Cloudflare V4 error responses on failure:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 10008,&#10;			&quot;message&quot;: &quot;Namespace name already exists&quot;&#10;		}&#10;	],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Common error scenarios include:</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>HTTP status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Invalid namespace name format</td>
<td><code>400</code></td>
</tr>
<tr>
<td>Authentication failure</td>
<td><code>401</code></td>
</tr>
<tr>
<td>Namespace name already exists</td>
<td><code>409</code></td>
</tr>
<tr>
<td>Namespace not found</td>
<td><code>404</code></td>
</tr>
<tr>
<td>Profile not found</td>
<td><code>404</code></td>
</tr>
</tbody>
</table>
