<ol>
<li>Use the <a href="/api/resources/addressing/subresources/prefixes/methods/get/">Prefix Details endpoint</a> to check if any issues were found during validation.</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">&#10; &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;72823e95d6c64d48a8111fec81179816&quot;,&#10;    &quot;created_at&quot;: &quot;2025-02-25T00:34:11.423722Z&quot;,&#10;    &quot;modified_at&quot;: &quot;2025-02-25T00:34:11.423722Z&quot;,&#10;    &quot;cidr&quot;: &quot;203.0.113.0/24&quot;,&#10;    &quot;account_id&quot;: &quot;654c5f71c324478cc9f68d60065d4620&quot;,&#10;    &quot;description&quot;: &quot;&quot;,&#10;    &quot;approved&quot;: &quot;P&quot;,&#10;    &quot;on_demand_enabled&quot;: false,&#10;    &quot;on_demand_locked&quot;: false,&#10;    &quot;advertised&quot;: null,&#10;    &quot;advertised_modified_at&quot;: null,&#10;    &quot;loa_document_id&quot;: &quot;b9ff4afe312246a8b2e7324d98f40b23&quot;,&#10;    &quot;asn&quot;: 13335,&#10;    &quot;ownership_validation_token&quot;: &quot;&lt;OWNERSHIP_VALIDATION_TOKEN&gt;&quot;,&#10;    &quot;delegate_loa_creation&quot; : true,&#10;    &quot;irr_validation_state&quot;: &quot;valid&quot;,&#10;    &quot;rpki_validation_state&quot;: &quot;valid&quot;,&#10;    &quot;ownership_validation_state&quot;: &quot;missing&quot;,&#10;  }&#10;</code></pre>
<ol start="2">
<li>Consider the states returned in the API response (for example, <code>missing</code>, <code>invalid</code>, <code>mismatch_asn</code>) and review your IRR record, <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/3723.md")
</div>, and ownership validation method accordingly.
<pre><code>- Information in the IRR and ROA records should meet the [onboarding prerequisites](/byoip/get-started/#before-you-begin).&#10;&#10;- [Ownership validation](/byoip/get-started/#validate-prefix-ownership) requires a matching ROA and the correct validation token found in all DNS TXT records or in the IRR record.&#10;</code></pre>
<ol start="3">
<li></li>
</ol>
<p>After applying the necessary changes, use the Validate Prefix endpoint to trigger the validation checks.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/validate \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
