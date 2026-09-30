---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/reference/api/
  description: Manage resource monitoring, settings, and detected scripts using the client-side security API.
  full_title: Client-side security API · Client-side security docs
  head_html: <title>Client-side security API · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage resource monitoring, settings, and detected scripts using the client-side security API."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/reference/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/reference/api/index.md"><meta property="og:title" content="Client-side security API · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage resource monitoring, settings, and detected scripts using the client-side security API."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/reference/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Client-side security"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/reference/api/#page","headline":"Client-side security API \u00b7 Client-side security docs","description":"Manage resource monitoring, settings, and detected scripts using the client-side security API.","url":"https://developers.cloudflare.com/client-side-security/reference/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /client-side-security/reference/api/
  schema: 1
---
<p>You can enable and disable client-side security's resource monitoring, configure settings, and fetch information about detected scripts and connections using the <a href="/api/resources/page_shield/methods/get/">client-side security API</a> (formerly known as Page Shield API).</p>
<p>To authenticate API requests you need an <a href="/fundamentals/api/get-started/create-token/">API token</a>. For more information on the required API token permissions, refer to <a href="/client-side-security/reference/roles-and-permissions/">Roles and permissions</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3984.md")
</aside>
<h2 id="endpoints">Endpoints</h2>
<p>You can obtain the complete endpoint by appending the <a href="/api/resources/page_shield/methods/get/">client-side security API</a> endpoints to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{zone_id}</code> argument is the zone ID (a hexadecimal string). You can find this value in the Cloudflare dashboard or using the Cloudflare API's <a href="/fundamentals/account/find-account-and-zone-ids/"><code>/zones</code> endpoint</a>.</p>
<p>The <code>{script_id}</code> argument is the script ID (a hexadecimal string). This value is included in the response of the <a href="/api/resources/page_shield/subresources/scripts/methods/list/">List client-side security scripts</a> operation for every detected script.</p>
<p>The <code>{connection_id}</code> argument is the connection ID (a hexadecimal string). This value is included in the response of the List client-side security connections API operation for every detected connection.</p>
<p>The following table summarizes the available operations:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method + URL stub</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>[Get client-side security settings][1]</td>
<td><code>GET zones/{zone_id}/page_shield</code></td>
<td>Fetch client-side security settings (including the status).</td>
</tr>
<tr>
<td>[Update client-side security settings][2]</td>
<td><code>PUT zones/{zone_id}/page_shield</code></td>
<td>Update client-side security settings.</td>
</tr>
<tr>
<td>[List client-side security scripts][3]</td>
<td><code>GET zones/{zone_id}/page_shield/scripts</code></td>
<td>Fetch a list of detected scripts.</td>
</tr>
<tr>
<td>[Get a client-side security script][4]</td>
<td><code>GET zones/{zone_id}/page_shield/scripts/{script_id}</code></td>
<td>Fetch the details of a script.</td>
</tr>
<tr>
<td>[List client-side security connections][5]</td>
<td><code>GET zones/{zone_id}/page_shield/connections</code></td>
<td>Fetch a list of detected connections.</td>
</tr>
<tr>
<td>[Get a client-side security connection][6]</td>
<td><code>GET zones/{zone_id}/page_shield/connections/{connection_id}</code></td>
<td>Fetch the details of a connection.</td>
</tr>
<tr>
<td>[List client-side security cookies][7]</td>
<td><code>GET zones/{zone_id}/page_shield/cookies</code></td>
<td>Fetch a list of detected cookies.</td>
</tr>
<tr>
<td>[Get a client-side security cookie][8]</td>
<td><code>GET zones/{zone_id}/page_shield/cookies/{cookie_id}</code></td>
<td>Fetch the details of a cookie.</td>
</tr>
<tr>
<td>[List content security rules][9]</td>
<td><code>GET zones/{zone_id}/page_shield/policies</code></td>
<td>Fetch a list of all configured content security rules.</td>
</tr>
<tr>
<td>[Get a content security rule][10]</td>
<td><code>GET zones/{zone_id}/page_shield/policies/{policy_id}</code></td>
<td>Fetch the details of a content security rule.</td>
</tr>
<tr>
<td>[Create a content security rule][11]</td>
<td><code>POST zones/{zone_id}/page_shield/policies</code></td>
<td>Creates a content security rule with the provided configuration.</td>
</tr>
<tr>
<td>[Update a content security rule][12]</td>
<td><code>PUT zones/{zone_id}/page_shield/policies/{policy_id}</code></td>
<td>Updates an existing content security rule.</td>
</tr>
<tr>
<td>[Delete a content security rule][13]</td>
<td><code>DELETE zones/{zone_id}/page_shield/policies/{policy_id}</code></td>
<td>Deletes an existing content security rule.</td>
</tr>
</tbody>
</table>
<h2 id="api-notes">API notes</h2>
<p>The malicious script classification (<code>Malicious</code> or <code>Not malicious</code>) is not directly available in the API. To determine this classification, compare the script's <code>js_integrity_score</code> value with the classification threshold, which is currently set to 10. Scripts with a score value lower than the threshold are considered malicious.</p>
<h2 id="common-api-calls">Common API calls</h2>
<h3 id="get-client-side-security-settings">Get client-side security settings</h3>
<p>This example obtains the current settings of Cloudflare's client-side security, including the status (enabled/disabled).</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;enabled&quot;: true,&#10;		&quot;updated_at&quot;: &quot;2023-05-14T11:47:55.677555Z&quot;,&#10;		&quot;use_cloudflare_reporting_endpoint&quot;: true,&#10;		&quot;use_connection_url_path&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="enable-client-side-security">Enable client-side security</h3>
<p>This example enables Cloudflare's client-side security in the specified zone.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;enabled&quot;: true,&#10;		&quot;updated_at&quot;: &quot;2023-05-14T11:50:41.756996Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="fetch-list-of-detected-scripts">Fetch list of detected scripts</h3>
<p>This <code>GET</code> request fetches a list of scripts detected by Cloudflare's client-side security on hostname <code>example.net</code>, requesting the first page with 15 items per page. The URL query string includes filtering and paging parameters.</p>
<p>By default, the response will only include scripts with <code>active</code> status when you do not specify a <code>status</code> filter parameter in the URL query string.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/scripts \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;8337233faec2357ff84465a919534e4d&quot;,&#10;			&quot;url&quot;: &quot;https://malicious.example.com/badscript.js&quot;,&#10;			&quot;added_at&quot;: &quot;2023-05-18T10:51:10.09615Z&quot;,&#10;			&quot;first_seen_at&quot;: &quot;2023-05-18T10:51:08Z&quot;,&#10;			&quot;last_seen_at&quot;: &quot;2023-05-22T09:57:54Z&quot;,&#10;			&quot;host&quot;: &quot;example.net&quot;,&#10;			&quot;domain_reported_malicious&quot;: false,&#10;			&quot;url_reported_malicious&quot;: true,&#10;			&quot;malicious_url_categories&quot;: [&quot;Malware&quot;],&#10;			&quot;first_page_url&quot;: &quot;http://malicious.example.com/page_one.html&quot;,&#10;			&quot;status&quot;: &quot;active&quot;,&#10;			&quot;url_contains_cdn_cgi_path&quot;: false,&#10;			&quot;hash&quot;: &quot;e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855&quot;,&#10;			&quot;js_integrity_score&quot;: 10,&#10;			&quot;obfuscation_score&quot;: 10,&#10;			&quot;dataflow_score&quot;: 8,&#10;			&quot;malware_score&quot;: 8,&#10;			&quot;cryptomining_score&quot;: 9,&#10;			&quot;magecart_score&quot;: 8,&#10;			&quot;fetched_at&quot;: &quot;2023-05-21T16:58:07Z&quot;&#10;		}&#10;		// (...)&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 15,&#10;		&quot;count&quot;: 15,&#10;		&quot;total_count&quot;: 24,&#10;		&quot;total_pages&quot;: 2&#10;	}&#10;}&#10;</code></pre>
<p>Some fields displayed in the example response may not be available, depending on your Cloudflare plan.</p>
<p>For details on the available filtering, paging, and sorting parameters, refer to the <a href="/api/resources/page_shield/subresources/scripts/methods/list/">API reference</a>.</p>
<h3 id="fetch-list-of-infrequently-reported-scripts">Fetch list of infrequently reported scripts</h3>
<p>This <code>GET</code> request fetches a list of infrequently reported scripts on hostname <code>example.net</code>, requesting the first page with 15 items per page. The URL query string includes filtering and paging parameters.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/scripts \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;83c8da2267394ce8465b74c299658fea&quot;,&#10;			&quot;url&quot;: &quot;https://scripts.example.com/anotherbadscript.js&quot;,&#10;			&quot;added_at&quot;: &quot;2023-05-17T13:16:03.419619Z&quot;,&#10;			&quot;first_seen_at&quot;: &quot;2023-05-17T13:15:23Z&quot;,&#10;			&quot;last_seen_at&quot;: &quot;2023-05-18T09:05:20Z&quot;,&#10;			&quot;host&quot;: &quot;example.net&quot;,&#10;			&quot;domain_reported_malicious&quot;: false,&#10;			&quot;url_reported_malicious&quot;: false,&#10;			&quot;first_page_url&quot;: &quot;http://malicious.example.com/page_one.html&quot;,&#10;			&quot;status&quot;: &quot;infrequent&quot;,&#10;			&quot;url_contains_cdn_cgi_path&quot;: false,&#10;			&quot;hash&quot;: &quot;9245aad577e846dd9b990b1b32425a3fae4aad8b8a28441a8b80084b6bb75a45&quot;,&#10;			&quot;js_integrity_score&quot;: 48,&#10;			&quot;obfuscation_score&quot;: 49,&#10;			&quot;dataflow_score&quot;: 45,&#10;			&quot;malware_score&quot;: 45,&#10;			&quot;cryptomining_score&quot;: 37,&#10;			&quot;magecart_score&quot;: 49,&#10;			&quot;fetched_at&quot;: &quot;2023-05-18T03:58:07Z&quot;&#10;		}&#10;		// (...)&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 15,&#10;		&quot;count&quot;: 15,&#10;		&quot;total_count&quot;: 17,&#10;		&quot;total_pages&quot;: 2&#10;	}&#10;}&#10;</code></pre>
<p>Some fields displayed in the example response may not be available, depending on your Cloudflare plan.</p>
<p>For details on the available filtering, paging, and sorting parameters, refer to the <a href="/api/resources/page_shield/subresources/scripts/methods/list/">API reference</a>.</p>
<h3 id="get-details-of-a-detected-script">Get details of a detected script</h3>
<p>This <code>GET</code> request obtains the details of a script detected by Cloudflare's client-side security with script ID <code>8337233faec2357ff84465a919534e4d</code>.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/scripts/{script_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;8337233faec2357ff84465a919534e4d&quot;,&#10;		&quot;url&quot;: &quot;https://malicious.example.com/badscript.js&quot;,&#10;		&quot;added_at&quot;: &quot;2023-05-18T10:51:10.09615Z&quot;,&#10;		&quot;first_seen_at&quot;: &quot;2023-05-18T10:51:08Z&quot;,&#10;		&quot;last_seen_at&quot;: &quot;2023-05-22T09:57:54Z&quot;,&#10;		&quot;host&quot;: &quot;example.net&quot;,&#10;		&quot;domain_reported_malicious&quot;: false,&#10;		&quot;url_reported_malicious&quot;: true,&#10;		&quot;malicious_url_categories&quot;: [&quot;Malware&quot;],&#10;		&quot;first_page_url&quot;: &quot;http://malicious.example.com/page_one.html&quot;,&#10;		&quot;status&quot;: &quot;active&quot;,&#10;		&quot;url_contains_cdn_cgi_path&quot;: false,&#10;		&quot;hash&quot;: &quot;9245aad577e846dd9b990b1b32425a3fae4aad8b8a28441a8b80084b6bb75a45&quot;,&#10;		&quot;js_integrity_score&quot;: 48,&#10;		&quot;obfuscation_score&quot;: 49,&#10;		&quot;dataflow_score&quot;: 45,&#10;		&quot;malware_score&quot;: 42,&#10;		&quot;cryptomining_score&quot;: 32,&#10;		&quot;magecart_score&quot;: 44,&#10;		&quot;fetched_at&quot;: &quot;2023-05-21T16:58:07Z&quot;,&#10;		&quot;page_urls&quot;: [&#10;			&quot;http://malicious.example.com/page_two.html&quot;,&#10;			&quot;http://malicious.example.com/page_three.html&quot;,&#10;			&quot;http://malicious.example.com/page_four.html&quot;&#10;		],&#10;		&quot;versions&quot;: [&#10;			{&#10;				&quot;hash&quot;: &quot;9245aad577e846dd9b990b1b32425a3fae4aad8b8a28441a8b80084b6bb75a45&quot;,&#10;				&quot;js_integrity_score&quot;: 48,&#10;				&quot;obfuscation_score&quot;: 49,&#10;				&quot;dataflow_score&quot;: 45,&#10;				&quot;malware_score&quot;: 42,&#10;				&quot;cryptomining_score&quot;: 32,&#10;				&quot;magecart_score&quot;: 44,&#10;				&quot;fetched_at&quot;: &quot;2023-05-21T16:58:07Z&quot;&#10;			}&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Some fields displayed in the example response may not be available, depending on your Cloudflare plan.</p>
<h3 id="fetch-list-of-detected-connections">Fetch list of detected connections</h3>
<p>This <code>GET</code> request fetches a list of connections detected by Cloudflare's client-side security, requesting the first page with 15 items per page.</p>
<p>By default, the response will only include connections with <code>active</code> status when you do not specify a <code>status</code> filter parameter in the URL query string.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/connections \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;0a7bb628776f4e50a50d8594c4a01740&quot;,&#10;			&quot;url&quot;: &quot;https://malicious.example.com&quot;,&#10;			&quot;added_at&quot;: &quot;2022-09-18T10:51:10.09615Z&quot;,&#10;			&quot;first_seen_at&quot;: &quot;2022-09-18T10:51:08Z&quot;,&#10;			&quot;last_seen_at&quot;: &quot;2022-09-02T09:57:54Z&quot;,&#10;			&quot;host&quot;: &quot;example.net&quot;,&#10;			&quot;domain_reported_malicious&quot;: true,&#10;			&quot;malicious_domain_categories&quot;: [&quot;Malware&quot;, &quot;Spyware&quot;],&#10;			&quot;url_reported_malicious&quot;: false,&#10;			&quot;malicious_url_categories&quot;: [],&#10;			&quot;first_page_url&quot;: &quot;https://example.net/one.html&quot;,&#10;			&quot;status&quot;: &quot;active&quot;,&#10;			&quot;url_contains_cdn_cgi_path&quot;: false&#10;		}&#10;		// (...)&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 15,&#10;		&quot;count&quot;: 15,&#10;		&quot;total_count&quot;: 16,&#10;		&quot;total_pages&quot;: 2&#10;	}&#10;}&#10;</code></pre>
<p>For details on the available filtering, paging, and sorting parameters, refer to the <a href="/api/resources/page_shield/subresources/scripts/methods/list/">API reference</a>.</p>
<h3 id="get-details-of-a-detected-connection">Get details of a detected connection</h3>
<p>This <code>GET</code> request obtains the details of a connection detected by Cloudflare's client-side security with connection ID <code>0a7bb628776f4e50a50d8594c4a01740</code>.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/connections/{connection_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;0a7bb628776f4e50a50d8594c4a01740&quot;,&#10;		&quot;url&quot;: &quot;https://malicious.example.com&quot;,&#10;		&quot;added_at&quot;: &quot;2022-09-18T10:51:10.09615Z&quot;,&#10;		&quot;first_seen_at&quot;: &quot;2022-09-18T10:51:08Z&quot;,&#10;		&quot;last_seen_at&quot;: &quot;2022-09-02T09:57:54Z&quot;,&#10;		&quot;host&quot;: &quot;example.net&quot;,&#10;		&quot;domain_reported_malicious&quot;: true,&#10;		&quot;malicious_domain_categories&quot;: [&quot;Malware&quot;, &quot;Spyware&quot;],&#10;		&quot;url_reported_malicious&quot;: false,&#10;		&quot;malicious_url_categories&quot;: [],&#10;		&quot;first_page_url&quot;: &quot;https://example.net/one.html&quot;,&#10;		&quot;status&quot;: &quot;active&quot;,&#10;		&quot;url_contains_cdn_cgi_path&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="fetch-list-of-detected-cookies">Fetch list of detected cookies</h3>
<p>This <code>GET</code> request fetches a list of cookies detected by Cloudflare's client-side security, requesting the first page with 15 items per page.</p>
<p>By default, the response will only include cookies with <code>active</code> status when you do not specify a <code>status</code> filter parameter in the URL query string.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/cookies \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;beee03ada7e047e79f076785d8cd8b8e&quot;,&#10;			&quot;type&quot;: &quot;first_party&quot;,&#10;			&quot;name&quot;: &quot;PHPSESSID&quot;,&#10;			&quot;host&quot;: &quot;example.net&quot;,&#10;			&quot;domain_attribute&quot;: &quot;example.net&quot;,&#10;			&quot;expires_attribute&quot;: &quot;2024-10-21T12:28:20Z&quot;,&#10;			&quot;http_only_attribute&quot;: true,&#10;			&quot;max_age_attribute&quot;: null,&#10;			&quot;path_attribute&quot;: &quot;/store&quot;,&#10;			&quot;same_site_attribute&quot;: &quot;strict&quot;,&#10;			&quot;secure_attribute&quot;: true,&#10;			&quot;first_seen_at&quot;: &quot;2024-05-06T10:51:08Z&quot;,&#10;			&quot;last_seen_at&quot;: &quot;2024-05-07T11:56:01Z&quot;,&#10;			&quot;first_page_url&quot;: &quot;example.net/store/products&quot;,&#10;			&quot;page_urls&quot;: [&quot;example.net/store/products/1&quot;]&#10;		}&#10;		// (...)&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 15,&#10;		&quot;count&quot;: 15,&#10;		&quot;total_count&quot;: 16,&#10;		&quot;total_pages&quot;: 2&#10;	}&#10;}&#10;</code></pre>
<p>For details on the available filtering, paging, and sorting parameters, refer to <a href="/fundamentals/api/how-to/make-api-calls/#pagination">Make API calls</a>.</p>
<h3 id="get-details-of-a-detected-cookie">Get details of a detected cookie</h3>
<p>This <code>GET</code> request obtains the details of a cookie detected by Cloudflare's client-side security with ID <code>beee03ada7e047e79f076785d8cd8b8e</code>.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/cookies/{cookie_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;beee03ada7e047e79f076785d8cd8b8e&quot;,&#10;		&quot;type&quot;: &quot;first_party&quot;,&#10;		&quot;name&quot;: &quot;PHPSESSID&quot;,&#10;		&quot;host&quot;: &quot;example.net&quot;,&#10;		&quot;domain_attribute&quot;: &quot;example.net&quot;,&#10;		&quot;expires_attribute&quot;: &quot;2024-10-21T12:28:20Z&quot;,&#10;		&quot;http_only_attribute&quot;: true,&#10;		&quot;max_age_attribute&quot;: null,&#10;		&quot;path_attribute&quot;: &quot;/store&quot;,&#10;		&quot;same_site_attribute&quot;: &quot;strict&quot;,&#10;		&quot;secure_attribute&quot;: true,&#10;		&quot;first_seen_at&quot;: &quot;2024-05-06T10:51:08Z&quot;,&#10;		&quot;last_seen_at&quot;: &quot;2024-05-07T11:56:01Z&quot;,&#10;		&quot;first_page_url&quot;: &quot;example.net/store/products&quot;,&#10;		&quot;page_urls&quot;: [&quot;example.net/store/products/1&quot;]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="create-a-content-security-rule">Create a content security rule</h3>
<p>This <code>POST</code> request creates a content security rule (previously called a policy) with <em>Log</em> action, defining the following scripts as allowed based on where they are hosted:</p>
<ul>
<li>Scripts hosted in <code>myapp.example.com</code> (which does not include scripts in <code>example.com</code>).</li>
<li>Scripts hosted in <code>cdnjs.cloudflare.com</code>.</li>
<li>The Google Analytics script using its full URL.</li>
<li>All scripts in the same origin (same HTTP or HTTPS scheme and hostname).</li>
</ul>
<p>All other scripts would trigger a rule violation, but those scripts would not be blocked.</p>
<p>For more information on <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span> directives and values, refer to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy">MDN documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3983.md")
</aside>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/page_shield/policies \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;My first content security rule in log mode&quot;,&#10;  &quot;action&quot;: &quot;log&quot;,&#10;  &quot;expression&quot;: &quot;http.host eq \&quot;myapp.example.com\&quot;&quot;,&#10;  &quot;enabled&quot;: &quot;true&quot;,&#10;  &quot;value&quot;: &quot;script-src myapp.example.com cdnjs.cloudflare.com https://www.google-analytics.com/analytics.js &#x27;self&#x27;&quot;&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;		&quot;description&quot;: &quot;My first content security rule in log mode&quot;,&#10;		&quot;action&quot;: &quot;log&quot;,&#10;		&quot;expression&quot;: &quot;http.host eq \&quot;myapp.example.com\&quot;&quot;,&#10;		&quot;enabled&quot;: &quot;true&quot;,&#10;		&quot;value&quot;: &quot;script-src myapp.example.com cdnjs.cloudflare.com https://www.google-analytics.com/analytics.js &#x27;self&#x27;&quot;&#10;	}&#10;}&#10;</code></pre>
<p>To create a content security rule with an <em>Allow</em> action instead of <em>Log</em>, use <code>&quot;action&quot;: &quot;allow&quot;</code> in the request body. In the case of such rule, all scripts not allowed by the rule would be blocked.</p>
