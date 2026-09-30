<p>Use the API operations described in the following sections to list and view the details of rulesets at the account or zone level.</p>
<ul>
<li><a href="#list-existing-rulesets">List existing rulesets</a></li>
<li><a href="#view-a-specific-ruleset">View a specific ruleset</a></li>
<li><a href="#list-all-versions-of-a-ruleset">List all versions of a ruleset</a></li>
<li><a href="#view-a-specific-version-of-a-ruleset">View a specific version of a ruleset</a></li>
<li><a href="#list-rules-in-a-managed-ruleset-with-a-specific-tag">List rules in a managed ruleset with a specific tag</a></li>
</ul>
<h2 id="list-existing-rulesets">List existing rulesets</h2>
<p>Returns the list of existing rulesets at the account level or at the zone level.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/methods/list/">List account rulesets</a><br/>
<code>GET /accounts/{account_id}/rulesets</code></li>
<li><a href="/api/resources/rulesets/methods/list/">List zone rulesets</a><br/>
<code>GET /zones/{zone_id}/rulesets</code></li>
</ul>
<p>The result includes rulesets across all phases at a given level (account or zone). The <code>phase</code> field in each result element indicates the <a href="/ruleset-engine/about/phases/">phase</a> where that ruleset is defined.</p>
<p>Also, the list of rulesets at the zone level includes the account-level rulesets you may want to deploy to the specified zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13236.md")
</aside>
<p>The result does not include the list of rules in the ruleset. Refer to <a href="#view-a-specific-version-of-a-ruleset">View a specific version of a ruleset</a> to learn how to obtain the list of rules.</p>
<h3 id="example">Example</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;PHASE_RULESET_ID&gt;&quot;,&#10;			&quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;			&quot;description&quot;: &quot;&quot;,&#10;			&quot;kind&quot;: &quot;zone&quot;,&#10;			&quot;version&quot;: &quot;5&quot;,&#10;			&quot;last_updated&quot;: &quot;2025-03-18T18:30:08.122758Z&quot;,&#10;			&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="view-a-specific-ruleset">View a specific ruleset</h2>
<p>Returns the properties of the most recent version of the ruleset with the specified ruleset ID.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/methods/get/">Get an account ruleset</a><br/>
<code>GET /accounts/{account_id}/rulesets/{ruleset_id}</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/methods/get/">Get an account entry point ruleset</a><br/>
<code>GET /accounts/{account_id}/rulesets/phases/{phase_name}/entrypoint</code></li>
<li><a href="/api/resources/rulesets/methods/get/">Get a zone ruleset</a><br/>
<code>GET /zones/{zone_id}/rulesets/{ruleset_id}</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a><br/>
<code>GET /zones/{zone_id}/rulesets/phases/{phase_name}/entrypoint</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13235.md")
</aside>
<p>The API returns a <code>404 Not Found</code> HTTP status code under these conditions:</p>
<ul>
<li>When a ruleset cannot be found.</li>
<li>When the specified ruleset is not a managed ruleset the calling account is entitled to execute.</li>
</ul>
<h3 id="example-1">Example</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;description&quot;: &quot;Executes a managed ruleset.&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;3&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;&#10;				},&#10;				&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="list-all-versions-of-a-ruleset">List all versions of a ruleset</h2>
<p>Returns a list of all the versions of a ruleset.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/subresources/versions/methods/list/">List account ruleset versions</a><br/>
<code>GET /accounts/{account_id}/rulesets/{ruleset_id}/versions</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/subresources/versions/methods/list/">List account entry point ruleset versions</a><br/>
<code>GET /accounts/{account_id}/rulesets/phases/{phase_name}/entrypoint/versions</code></li>
<li><a href="/api/resources/rulesets/subresources/versions/methods/list/">List zone ruleset versions</a><br/>
<code>GET /zones/{zone_id}/rulesets/{ruleset_id}/versions</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/subresources/versions/methods/list/">List zone entry point ruleset versions</a><br/>
<code>GET /zones/{zone_id}/rulesets/phases/{phase_name}/entrypoint/versions</code></li>
</ul>
<p>The result contains the ruleset properties of each version, but it does not include the list of rules. Refer to <a href="#view-a-specific-version-of-a-ruleset">View a specific version of a ruleset</a> for instructions on obtaining this information.</p>
<p>When the specified phase entry point ruleset does not exist, this API method returns an empty array in the <code>result</code> field.</p>
<h3 id="example-2">Example</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/versions \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;			&quot;name&quot;: &quot;Zone Ruleset 1&quot;,&#10;			&quot;description&quot;: &quot;&quot;,&#10;			&quot;kind&quot;: &quot;zone&quot;,&#10;			&quot;version&quot;: &quot;1&quot;,&#10;			&quot;last_updated&quot;: &quot;2023-02-17T11:15:13.128705Z&quot;,&#10;			&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;		},&#10;		{&#10;			&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;			&quot;name&quot;: &quot;Zone Ruleset 1&quot;,&#10;			&quot;description&quot;: &quot;&quot;,&#10;			&quot;kind&quot;: &quot;zone&quot;,&#10;			&quot;version&quot;: &quot;2&quot;,&#10;			&quot;last_updated&quot;: &quot;2023-02-17T11:24:06.869326Z&quot;,&#10;			&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="view-a-specific-version-of-a-ruleset">View a specific version of a ruleset</h2>
<p>Returns the configuration of a specific version of a ruleset, including its rules.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/subresources/versions/methods/get/">Get an account ruleset version</a><br/>
<code>GET /account/{account_id}/rulesets/{ruleset_id}/versions/{version_number}</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/subresources/versions/methods/get/">Get an account entry point ruleset version</a><br/>
<code>GET /accounts/{account_id}/rulesets/phases/{phase_name}/entrypoint/versions/{version_number}</code></li>
<li><a href="/api/resources/rulesets/subresources/versions/methods/get/">Get a zone ruleset version</a><br/>
<code>GET /zones/{zone_id}/rulesets/{ruleset_id}/versions/{version_number}</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/subresources/versions/methods/get/">Get a zone entry point ruleset version</a><br/>
<code>GET /zones/{zone_id}/rulesets/phases/{phase_name}/entrypoint/versions/{version_number}</code></li>
</ul>
<p>When the specified phase entry point ruleset does not exist, this API method returns a <code>404 Not Found</code> HTTP status code.</p>
<h3 id="example-3">Example</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;description&quot;: &quot;Executes a managed ruleset.&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;&lt;RULESET_VERSION&gt;&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;&#10;				},&#10;				&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13234.md")
</aside>
<h2 id="list-rules-in-a-managed-ruleset-with-a-specific-tag">List rules in a managed ruleset with a specific tag</h2>
<p>Returns a list of all the rules in a managed ruleset with a specific tag.</p>
<ul>
<li>List an account ruleset version's rules by tag<br/>
<code>GET /accounts/{account_id}/rulesets/{ruleset_id}/versions/{version_number}/by_tag/{tag_name}</code></li>
</ul>
<h3 id="example-4">Example</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Cloudflare Managed Ruleset&quot;,&#10;		&quot;description&quot;: &quot;Managed ruleset created by Cloudflare&quot;,&#10;		&quot;kind&quot;: &quot;managed&quot;,&#10;		&quot;version&quot;: &quot;2&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;,&#10;				&quot;version&quot;: &quot;2&quot;,&#10;				&quot;action&quot;: &quot;log&quot;,&#10;				&quot;categories&quot;: [&#10;					&quot;cve-2014-5265&quot;,&#10;					&quot;cve-2014-5266&quot;,&#10;					&quot;cve-2014-5267&quot;,&#10;					&quot;dos&quot;,&#10;					&quot;drupal&quot;,&#10;					&quot;wordpress&quot;&#10;				],&#10;				&quot;description&quot;: &quot;Drupal, WordPress - DoS - XMLRPC - CVE:CVE-2014-5265, CVE:CVE-2014-5266, CVE:CVE-2014-5267&quot;,&#10;				&quot;last_updated&quot;: &quot;2025-03-19T16:54:32.942986Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_1&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;,&#10;				&quot;version&quot;: &quot;2&quot;,&#10;				&quot;action&quot;: &quot;block&quot;,&#10;				&quot;categories&quot;: [&quot;broken-access-control&quot;, &quot;cve-2018-12895&quot;, &quot;wordpress&quot;],&#10;				&quot;description&quot;: &quot;WordPress - Broken Access Control - CVE:CVE-2018-12895&quot;,&#10;				&quot;last_updated&quot;: &quot;2025-03-19T16:54:32.942986Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_2&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;			// (...)&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-19T16:54:32.942986Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
